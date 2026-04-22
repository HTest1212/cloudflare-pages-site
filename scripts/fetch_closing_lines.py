#!/usr/bin/env python3
"""
fetch_closing_lines.py

Snapshots the latest market price for every game on today's slate so the PNL
tab can compute closing line value (CLV) after each game settles.

Runs often (every 15 min during daytime). For each game on today's statsapi
schedule, records the current consensus moneyline home and away prices plus
their vig-free fair probabilities. The last recorded value before first pitch
is treated as the closing line.

Input:
  - odds_overlay.json at repo root (produced by fetch_odds.py)
  - statsapi schedule for today (Eastern date)
  - existing closing_lines.json at repo root (optional, will be updated in place)

Output:
  closing_lines.json shape:
  {
    "asOf": "...",
    "byGameSide": {
      "<gamePk>:<side>:moneyline": {
        "priceLast": -140,
        "fairLast": 0.575,
        "priceClose": null,        # filled only when game has started
        "fairClose": null,
        "recordedAt": "...",
        "sideLabel": "Yankees"
      }
    }
  }

Env:
  CLOSING_LINES_PATH  optional override (default: closing_lines.json)
"""
from __future__ import annotations
import json
import os
import datetime as dt
from pathlib import Path
from urllib.parse import urlencode

import urllib.request


CLOSING_LINES_PATH = Path(os.environ.get("CLOSING_LINES_PATH", "closing_lines.json"))
ODDS_OVERLAY_PATH = Path("odds_overlay.json")
STATSAPI_SCHEDULE = "https://statsapi.mlb.com/api/v1/schedule"


def log(msg: str) -> None:
    print(f"[closing_lines] {msg}", flush=True)


def today_iso_eastern() -> str:
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")
    except Exception:
        return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=4)).strftime("%Y-%m-%d")


def american_to_prob(odds) -> float | None:
    try:
        o = float(odds)
    except (TypeError, ValueError):
        return None
    if o > 0:
        return 100.0 / (o + 100.0)
    if o < 0:
        return (-o) / ((-o) + 100.0)
    return None


def devig(p_home: float | None, p_away: float | None) -> tuple[float | None, float | None]:
    if p_home is None or p_away is None:
        return p_home, p_away
    tot = p_home + p_away
    if tot <= 0:
        return p_home, p_away
    return p_home / tot, p_away / tot


def http_get_json(url: str, timeout: int = 15) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "mlb-dashboard-closing/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_schedule(date_str: str) -> list[dict]:
    qs = urlencode({"sportId": 1, "date": date_str})
    data = http_get_json(f"{STATSAPI_SCHEDULE}?{qs}")
    out = []
    for day in data.get("dates", []):
        for g in day.get("games", []):
            out.append({
                "gamePk": str(g["gamePk"]),
                "home": g["teams"]["home"]["team"]["name"],
                "away": g["teams"]["away"]["team"]["name"],
                "state": (g.get("status") or {}).get("detailedState", ""),
                "startedUtc": g.get("gameDate"),
            })
    return out


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def main() -> int:
    date_str = today_iso_eastern()
    log(f"snapshotting closing lines for {date_str}")

    odds_doc = load_json(ODDS_OVERLAY_PATH, {})
    games_odds = (odds_doc or {}).get("games", {}) or {}
    schedule = fetch_schedule(date_str)
    log(f"schedule: {len(schedule)} games; odds rows: {len(games_odds)}")

    store = load_json(CLOSING_LINES_PATH, {"byGameSide": {}})
    by_gs = store.get("byGameSide") or {}
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    updated = 0
    for g in schedule:
        pk = g["gamePk"]
        row = games_odds.get(pk)
        if not row:
            continue
        ml = (row or {}).get("moneyline") or {}
        ph = american_to_prob(ml.get("home"))
        pa = american_to_prob(ml.get("away"))
        fh, fa = devig(ph, pa)

        # Game has started or finished: freeze the last value as closing.
        started = bool(g.get("state")) and g["state"].lower() not in ("scheduled", "pre-game", "warmup", "delayed start")

        for side, price, fair, label in [
            ("home", ml.get("home"), fh, g["home"]),
            ("away", ml.get("away"), fa, g["away"]),
        ]:
            key = f"{pk}:{side}:moneyline"
            prev = by_gs.get(key) or {}
            entry = {
                "priceLast": price,
                "fairLast": fair,
                "priceClose": prev.get("priceClose"),
                "fairClose": prev.get("fairClose"),
                "recordedAt": now,
                "sideLabel": label,
            }
            if started and entry["priceClose"] is None:
                entry["priceClose"] = price
                entry["fairClose"] = fair
            by_gs[key] = entry
            updated += 1

    store["byGameSide"] = by_gs
    store["asOf"] = now
    CLOSING_LINES_PATH.write_text(json.dumps(store, indent=2) + "\n", encoding="utf-8")
    log(f"wrote {CLOSING_LINES_PATH} ({updated} side snapshots)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
