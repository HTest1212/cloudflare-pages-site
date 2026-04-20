#!/usr/bin/env python3
"""
fetch_odds.py

Builds odds_overlay.json for the MLB betting dashboard.

Flow:
  1. Pull today's MLB schedule from statsapi.mlb.com to get each game's gamePk
     plus canonical home/away team names.
  2. Pull today's MLB odds from The Odds API (moneyline, totals, run line spreads).
  3. Match odds rows to statsapi games by fuzzy team name.
  4. Pick a consensus price from the major US books (DraftKings, FanDuel, BetMGM,
     Caesars, PointsBet) using the median to resist outlier books.
  5. Emit odds_overlay.json at the repo root.

Env:
  ODDS_API_KEY   required. Free tier key from the-odds-api.com.
  ODDS_DEBUG     optional. Set to "1" to dump raw API payloads into ./odds_debug/.

Exit code:
  0 on success (file written, even if odds are partial)
  1 on hard failure (API key missing, network dead, statsapi down)
"""

from __future__ import annotations
import json
import os
import sys
import statistics
import datetime as dt
from pathlib import Path
from urllib.parse import urlencode

import urllib.request
import urllib.error

ODDS_API_KEY = os.environ.get("ODDS_API_KEY", "").strip()
ODDS_DEBUG = os.environ.get("ODDS_DEBUG") == "1"

STATSAPI_SCHEDULE = "https://statsapi.mlb.com/api/v1/schedule"
ODDS_URL = "https://api.the-odds-api.com/v4/sports/baseball_mlb/odds"

# Books to pull a consensus from. Ordered by US market share.
CONSENSUS_BOOKS = [
    "draftkings", "fanduel", "betmgm", "caesars", "pointsbetus",
    "williamhill_us", "betrivers", "wynnbet",
]

# Canonical MLB team names as they appear in statsapi.
# Extend this map if a book returns an unusual abbreviation.
TEAM_ALIASES = {
    "arizona diamondbacks": "Arizona Diamondbacks",
    "atlanta braves": "Atlanta Braves",
    "baltimore orioles": "Baltimore Orioles",
    "boston red sox": "Boston Red Sox",
    "chicago cubs": "Chicago Cubs",
    "chicago white sox": "Chicago White Sox",
    "cincinnati reds": "Cincinnati Reds",
    "cleveland guardians": "Cleveland Guardians",
    "colorado rockies": "Colorado Rockies",
    "detroit tigers": "Detroit Tigers",
    "houston astros": "Houston Astros",
    "kansas city royals": "Kansas City Royals",
    "los angeles angels": "Los Angeles Angels",
    "los angeles dodgers": "Los Angeles Dodgers",
    "miami marlins": "Miami Marlins",
    "milwaukee brewers": "Milwaukee Brewers",
    "minnesota twins": "Minnesota Twins",
    "new york mets": "New York Mets",
    "new york yankees": "New York Yankees",
    "oakland athletics": "Oakland Athletics",
    "athletics": "Oakland Athletics",
    "philadelphia phillies": "Philadelphia Phillies",
    "pittsburgh pirates": "Pittsburgh Pirates",
    "san diego padres": "San Diego Padres",
    "san francisco giants": "San Francisco Giants",
    "seattle mariners": "Seattle Mariners",
    "st. louis cardinals": "St. Louis Cardinals",
    "st louis cardinals": "St. Louis Cardinals",
    "tampa bay rays": "Tampa Bay Rays",
    "texas rangers": "Texas Rangers",
    "toronto blue jays": "Toronto Blue Jays",
    "washington nationals": "Washington Nationals",
}


def log(msg: str) -> None:
    print(f"[fetch_odds] {msg}", flush=True)


def http_get_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "mlb-dashboard-odds/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def canonical_team(name: str) -> str:
    if not name:
        return ""
    return TEAM_ALIASES.get(name.strip().lower(), name.strip())


def today_iso_eastern() -> str:
    """statsapi uses US date keys. We use Eastern noon so cron in UTC still
    matches the day the games are played in the US."""
    now_utc = dt.datetime.now(dt.timezone.utc)
    # Eastern is UTC-5 standard, UTC-4 DST. Approximation good enough for date picking.
    eastern = now_utc - dt.timedelta(hours=5)
    return eastern.strftime("%Y-%m-%d")


def fetch_schedule(date_str: str) -> list[dict]:
    qs = urlencode({"sportId": 1, "date": date_str, "hydrate": "team"})
    url = f"{STATSAPI_SCHEDULE}?{qs}"
    log(f"GET schedule {url}")
    data = http_get_json(url)
    games = []
    for day in data.get("dates", []):
        for g in day.get("games", []):
            games.append({
                "gamePk": g["gamePk"],
                "home": canonical_team(g["teams"]["home"]["team"]["name"]),
                "away": canonical_team(g["teams"]["away"]["team"]["name"]),
                "gameDate": g.get("gameDate"),
            })
    log(f"schedule: {len(games)} games")
    return games


def fetch_odds() -> list[dict]:
    if not ODDS_API_KEY:
        raise SystemExit("ODDS_API_KEY not set in environment")
    qs = urlencode({
        "apiKey": ODDS_API_KEY,
        "regions": "us",
        "markets": "h2h,totals,spreads",
        "oddsFormat": "american",
        "dateFormat": "iso",
    })
    url = f"{ODDS_URL}?{qs}"
    log("GET odds from the-odds-api.com")
    data = http_get_json(url)
    if ODDS_DEBUG:
        Path("odds_debug").mkdir(exist_ok=True)
        Path("odds_debug/raw_odds.json").write_text(json.dumps(data, indent=2))
    log(f"odds rows: {len(data)}")
    return data


def match_odds_to_game(game: dict, odds_rows: list[dict]) -> dict | None:
    """Match by canonical team names on both sides."""
    for row in odds_rows:
        rh = canonical_team(row.get("home_team", ""))
        ra = canonical_team(row.get("away_team", ""))
        if rh == game["home"] and ra == game["away"]:
            return row
    return None


def consensus_american(prices: list[float]) -> float | None:
    if not prices:
        return None
    # Median in implied-probability space, then convert back.
    probs = []
    for p in prices:
        try:
            p = float(p)
        except (TypeError, ValueError):
            continue
        if p > 0:
            probs.append(100.0 / (p + 100.0))
        elif p < 0:
            probs.append((-p) / ((-p) + 100.0))
    if not probs:
        return None
    med = statistics.median(probs)
    if med >= 0.5:
        return round(-med * 100 / (1 - med))
    else:
        return round((1 - med) * 100 / med)


def extract_market(row: dict) -> dict:
    """Pull moneyline, total and run line from a single odds-api game row."""
    ml_away: list[float] = []
    ml_home: list[float] = []
    total_lines: list[float] = []
    total_over: list[float] = []
    total_under: list[float] = []
    rl_fav_side: list[str] = []
    rl_fav_price: list[float] = []
    rl_dog_price: list[float] = []

    home_name = canonical_team(row.get("home_team", ""))
    away_name = canonical_team(row.get("away_team", ""))

    for book in row.get("bookmakers", []):
        key = book.get("key", "")
        if CONSENSUS_BOOKS and key not in CONSENSUS_BOOKS:
            continue
        for mkt in book.get("markets", []):
            mtype = mkt.get("key")
            outs = mkt.get("outcomes", [])
            if mtype == "h2h":
                for o in outs:
                    name = canonical_team(o.get("name", ""))
                    price = o.get("price")
                    if name == home_name and price is not None:
                        ml_home.append(price)
                    elif name == away_name and price is not None:
                        ml_away.append(price)
            elif mtype == "totals":
                # Each book posts one line. Take the (line, over, under) triple as-is.
                o_over = next((o for o in outs if o.get("name") == "Over"), None)
                o_under = next((o for o in outs if o.get("name") == "Under"), None)
                if o_over and o_under and o_over.get("point") is not None:
                    total_lines.append(float(o_over["point"]))
                    if o_over.get("price") is not None:
                        total_over.append(o_over["price"])
                    if o_under.get("price") is not None:
                        total_under.append(o_under["price"])
            elif mtype == "spreads":
                # Run line: find the -1.5 favorite.
                for o in outs:
                    pt = o.get("point")
                    name = canonical_team(o.get("name", ""))
                    price = o.get("price")
                    if pt is None or price is None:
                        continue
                    if abs(pt + 1.5) < 0.01:  # favorite side at -1.5
                        rl_fav_side.append("home" if name == home_name else "away")
                        rl_fav_price.append(price)
                    elif abs(pt - 1.5) < 0.01:  # dog side at +1.5
                        rl_dog_price.append(price)

    out: dict = {}
    ml_a = consensus_american(ml_away)
    ml_h = consensus_american(ml_home)
    if ml_a is not None and ml_h is not None:
        out["moneyline"] = {
            "away": ml_a,
            "home": ml_h,
            "book": "consensus",
        }

    if total_lines and total_over and total_under:
        out["total"] = {
            "line": round(statistics.median(total_lines) * 2) / 2,  # snap to nearest 0.5
            "over": consensus_american(total_over),
            "under": consensus_american(total_under),
        }

    if rl_fav_side and rl_fav_price and rl_dog_price:
        fav_side = statistics.mode(rl_fav_side) if rl_fav_side else "home"
        out["runline"] = {
            "spread": -1.5,
            "favSide": fav_side,
            "favPrice": consensus_american(rl_fav_price),
            "dogPrice": consensus_american(rl_dog_price),
        }

    return out


def build_overlay() -> dict:
    date_str = today_iso_eastern()
    games = fetch_schedule(date_str)
    try:
        odds_rows = fetch_odds()
    except (urllib.error.URLError, urllib.error.HTTPError) as e:
        log(f"odds fetch failed: {e}")
        odds_rows = []

    overlay_games: dict = {}
    matched = 0
    for g in games:
        row = match_odds_to_game(g, odds_rows)
        if not row:
            continue
        mkt = extract_market(row)
        if not mkt:
            continue
        matched += 1
        overlay_games[str(g["gamePk"])] = mkt

    return {
        "asOf": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "date": date_str,
        "slateSize": len(games),
        "matched": matched,
        "source": "the-odds-api.com consensus across major US books",
        "games": overlay_games,
    }


def main() -> int:
    try:
        overlay = build_overlay()
    except Exception as e:
        log(f"FATAL: {e!r}")
        return 1

    out_path = Path("odds_overlay.json")
    out_path.write_text(json.dumps(overlay, indent=2) + "\n", encoding="utf-8")
    log(f"wrote {out_path} ({overlay.get('matched', 0)} of {overlay.get('slateSize', 0)} games priced)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
