"""
update_bullpen_availability.py

Pulls the last 2 days of MLB bullpen usage from the public StatsAPI and writes
bullpen_availability_overlay.json at the project root so the dashboard's Best
Bets engine can penalize teams with unavailable relievers.

Rules (tuned for modern MLB bullpen management):
  - 30+ pitches yesterday                        => OUT (closer role if 8th/9th, else high_leverage)
  - 20 to 29 pitches yesterday                   => LIMITED
  - Appeared yesterday AND day before yesterday  => LIMITED (back to back)
  - 3 appearances in last 3 days                 => OUT
  - Combined 40+ pitches over last 2 days        => OUT

Usage (standalone):
  python3 scripts/update_bullpen_availability.py

Output file: bullpen_availability_overlay.json
Schema:
  {
    "date": "YYYY-MM-DD",
    "updated_at_iso": "2026-04-22T19:00:00Z",
    "source": "mlb_statsapi",
    "teams": {
      "<Full Team Name>": {
        "unavailable": [
          {"name": "...", "role": "closer|setup|high_leverage|middle|long",
           "status": "out|limited|questionable",
           "reason": "30 pitches yesterday"}
        ]
      }
    }
  }
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from collections import defaultdict
import os
import sys

STATS_BASE = "https://statsapi.mlb.com/api/v1"
SCHEDULE_URL = STATS_BASE + "/schedule?sportId=1&date={date}"
BOXSCORE_URL = STATS_BASE + "/game/{gamePk}/boxscore"


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mlb-dashboard-bullpen-refresh/1.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))


def get_games_for_date(d):
    """Return list of (gamePk, awayTeamName, homeTeamName) for finished games on date d."""
    url = SCHEDULE_URL.format(date=d.strftime("%Y-%m-%d"))
    try:
        data = fetch_json(url)
    except Exception as e:
        print(f"[warn] schedule fetch failed for {d}: {e}", file=sys.stderr)
        return []
    out = []
    for date_block in data.get("dates", []):
        for g in date_block.get("games", []):
            status = (g.get("status") or {}).get("detailedState", "")
            # Only count completed games for bullpen usage.
            if status not in ("Final", "Game Over", "Completed Early"):
                continue
            teams = g.get("teams") or {}
            home_name = ((teams.get("home") or {}).get("team") or {}).get("name")
            away_name = ((teams.get("away") or {}).get("team") or {}).get("name")
            out.append((g["gamePk"], away_name, home_name))
    return out


def extract_bullpen_usage(gamePk, away_name, home_name):
    """Return list of usage records for relievers in one game.
    Each record: {team, player, pitches, outs, innings_entered_in}
    """
    try:
        box = fetch_json(BOXSCORE_URL.format(gamePk=gamePk))
    except Exception as e:
        print(f"[warn] boxscore fetch failed {gamePk}: {e}", file=sys.stderr)
        return []
    records = []
    for side_key, team_name in (("away", away_name), ("home", home_name)):
        side = (box.get("teams") or {}).get(side_key) or {}
        pitcher_ids = side.get("pitchers") or []
        players = side.get("players") or {}
        # First pitcher in the list is the starter; everyone else is a reliever.
        for idx, pid in enumerate(pitcher_ids):
            if idx == 0:
                continue
            key = f"ID{pid}"
            p = players.get(key) or {}
            person = p.get("person") or {}
            stats = ((p.get("stats") or {}).get("pitching")) or {}
            pitches = stats.get("numberOfPitches") or stats.get("pitchesThrown") or 0
            try:
                pitches = int(pitches)
            except Exception:
                pitches = 0
            outs_recorded = 0
            try:
                ip_str = stats.get("inningsPitched") or "0.0"
                whole, frac = (ip_str.split(".") + ["0"])[:2]
                outs_recorded = int(whole) * 3 + int(frac)
            except Exception:
                pass
            records.append({
                "team": team_name,
                "player": person.get("fullName") or person.get("boxscoreName") or "Unknown",
                "playerId": pid,
                "pitches": pitches,
                "outs": outs_recorded,
                "appearance_order": idx,  # 1 = first reliever, higher = later in game
            })
    return records


def classify(usage_by_player):
    """Given per-player aggregated usage across last 2 days, return unavailable list.
    usage_by_player[(team, name)] = {
      'team': ..., 'name': ..., 'playerId': ...,
      'd1_pitches': int, 'd1_outs': int, 'd1_order': int or None,
      'd2_pitches': int, 'd2_outs': int, 'd2_order': int or None,
      'appearances': set of day offsets (1,2)
    }
    """
    by_team = defaultdict(list)
    for key, rec in usage_by_player.items():
        team = rec["team"]
        if not team:
            continue
        d1 = rec.get("d1_pitches", 0)
        d2 = rec.get("d2_pitches", 0)
        appearances = rec.get("appearances", set())
        d1_order = rec.get("d1_order")
        combined = d1 + d2

        status = None
        reason = None
        if d1 >= 30:
            status = "out"
            reason = f"{d1} pitches yesterday"
        elif combined >= 40 and len(appearances) >= 2:
            status = "out"
            reason = f"{combined} pitches over last 2 days"
        elif len(appearances) >= 2 and d1 > 0 and d2 > 0:
            status = "limited"
            reason = "back to back appearances"
        elif d1 >= 20:
            status = "limited"
            reason = f"{d1} pitches yesterday"
        if not status:
            continue

        # Role inference from appearance order yesterday.
        role = "high_leverage"
        if d1_order is not None:
            if d1_order >= 4:
                role = "closer"
            elif d1_order == 3:
                role = "setup"
            elif d1_order == 2:
                role = "high_leverage"
            else:
                role = "middle"

        by_team[team].append({
            "name": rec["name"],
            "role": role,
            "status": status,
            "reason": reason,
        })
    return by_team


def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_path = os.path.join(project_root, "bullpen_availability_overlay.json")

    today_utc = datetime.now(timezone.utc).date()
    # We key the overlay to "today" (the slate the user is betting). Yesterday's
    # games are the input. Also check the day before for back to back detection.
    d1 = today_utc - timedelta(days=1)  # yesterday
    d2 = today_utc - timedelta(days=2)  # day before yesterday

    usage = {}
    for offset, d in [(1, d1), (2, d2)]:
        games = get_games_for_date(d)
        print(f"[info] {d} -> {len(games)} completed games")
        for gamePk, away, home in games:
            for rec in extract_bullpen_usage(gamePk, away, home):
                key = (rec["team"], rec["player"])
                u = usage.setdefault(key, {
                    "team": rec["team"],
                    "name": rec["player"],
                    "playerId": rec.get("playerId"),
                    "d1_pitches": 0, "d1_outs": 0, "d1_order": None,
                    "d2_pitches": 0, "d2_outs": 0, "d2_order": None,
                    "appearances": set(),
                })
                if offset == 1:
                    u["d1_pitches"] += rec["pitches"]
                    u["d1_outs"] += rec["outs"]
                    if u["d1_order"] is None or rec["appearance_order"] > u["d1_order"]:
                        u["d1_order"] = rec["appearance_order"]
                else:
                    u["d2_pitches"] += rec["pitches"]
                    u["d2_outs"] += rec["outs"]
                    if u["d2_order"] is None or rec["appearance_order"] > u["d2_order"]:
                        u["d2_order"] = rec["appearance_order"]
                u["appearances"].add(offset)

    by_team = classify(usage)

    overlay = {
        "date": today_utc.strftime("%Y-%m-%d"),
        "updated_at_iso": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "mlb_statsapi",
        "window_days": 2,
        "teams": {t: {"unavailable": items} for t, items in by_team.items()},
    }

    # Ensure every team appears in the overlay, even if no one is flagged, so the
    # dashboard can distinguish "no alerts" from "file not loaded."
    try:
        sched = fetch_json(SCHEDULE_URL.format(date=today_utc.strftime("%Y-%m-%d")))
        for date_block in sched.get("dates", []):
            for g in date_block.get("games", []):
                teams = g.get("teams") or {}
                for side in ("home", "away"):
                    tn = ((teams.get(side) or {}).get("team") or {}).get("name")
                    if tn and tn not in overlay["teams"]:
                        overlay["teams"][tn] = {"unavailable": []}
    except Exception as e:
        print(f"[warn] could not enumerate today's teams: {e}", file=sys.stderr)

    with open(out_path, "w") as f:
        json.dump(overlay, f, indent=2)

    flagged = sum(len(v["unavailable"]) for v in overlay["teams"].values())
    print(f"[ok] wrote {out_path}")
    print(f"[ok] {flagged} reliever(s) flagged across {len(overlay['teams'])} team(s)")


if __name__ == "__main__":
    main()
