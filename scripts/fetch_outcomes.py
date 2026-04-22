#!/usr/bin/env python3
"""
fetch_outcomes.py

Grades every ungraded pick in picks_log.json by pulling the final score from
the statsapi schedule, writing results into outcomes_log.json keyed by pickId.

Supported bet types:
  - moneyline      : W if pickTeam = winner, else L. Push only if game was
                     called a tie (rare).
  - runline        : uses pick's spread (default -1.5 for fav, +1.5 for dog).
  - total          : Over/Under with half-point or integer line. Integer
                     line that matches exactly is graded as a push.
  - f5             : first 5 innings over/under (requires linescore pull).

Input:
  - picks_log.json at repo root
  - existing outcomes_log.json (optional)

Output:
  outcomes_log.json:
  {
    "asOf": "...",
    "byPickId": {
      "<pickId>": { "result": "W"|"L"|"P"|"void",
                    "finalHome": 7, "finalAway": 3,
                    "settledAt": "...", "note": "..." }
    }
  }

Exit 0 on success (even if some picks stay pending because their games had
no final score yet).
"""
from __future__ import annotations
import json
import os
import datetime as dt
from pathlib import Path
from urllib.parse import urlencode

import urllib.request


PICKS_PATH = Path(os.environ.get("PICKS_LOG_PATH", "picks_log.json"))
OUTCOMES_PATH = Path(os.environ.get("OUTCOMES_LOG_PATH", "outcomes_log.json"))
STATSAPI_SCHEDULE = "https://statsapi.mlb.com/api/v1/schedule"
STATSAPI_LINESCORE = "https://statsapi.mlb.com/api/v1/game/{pk}/linescore"


def log(msg: str) -> None:
    print(f"[outcomes] {msg}", flush=True)


def http_get_json(url: str, timeout: int = 15):
    req = urllib.request.Request(url, headers={"User-Agent": "mlb-dashboard-outcomes/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def fetch_schedule_range(start_iso: str, end_iso: str) -> dict[str, dict]:
    qs = urlencode({"sportId": 1, "startDate": start_iso, "endDate": end_iso, "hydrate": "linescore"})
    data = http_get_json(f"{STATSAPI_SCHEDULE}?{qs}")
    out: dict[str, dict] = {}
    for day in data.get("dates", []):
        for g in day.get("games", []):
            status = (g.get("status") or {}).get("detailedState", "")
            is_final = "Final" in status or "Completed" in status
            home = g["teams"]["home"]["team"]["name"]
            away = g["teams"]["away"]["team"]["name"]
            rh = ((g.get("teams") or {}).get("home") or {}).get("score")
            ra = ((g.get("teams") or {}).get("away") or {}).get("score")
            out[str(g["gamePk"])] = {
                "home": home, "away": away,
                "finalHome": rh, "finalAway": ra,
                "isFinal": is_final, "status": status,
            }
    return out


def fetch_f5_score(gamepk: str) -> tuple[int | None, int | None]:
    try:
        data = http_get_json(STATSAPI_LINESCORE.format(pk=gamepk))
    except Exception:
        return None, None
    innings = data.get("innings") or []
    if len(innings) < 5:
        return None, None
    ah = 0
    aa = 0
    for i in innings[:5]:
        ah += int(((i.get("home") or {}).get("runs") or 0))
        aa += int(((i.get("away") or {}).get("runs") or 0))
    return ah, aa


def name_matches(pick_team_name: str, candidate: str) -> bool:
    if not pick_team_name or not candidate:
        return False
    a = pick_team_name.strip().lower()
    b = candidate.strip().lower()
    return a in b or b in a


def grade_pick(pick: dict, games: dict) -> dict | None:
    gp = str(pick.get("gamePk") or "")
    g = games.get(gp)
    if not g or not g.get("isFinal"):
        return None
    fh = g.get("finalHome")
    fa = g.get("finalAway")
    if fh is None or fa is None:
        return None

    bet_type = (pick.get("betType") or "moneyline").lower()
    pick_side = (pick.get("side") or "").lower()  # "home" | "away"
    pick_team = pick.get("pickTeam") or pick.get("pick") or ""

    note = ""
    result = "void"

    if bet_type == "moneyline":
        winner_side = "home" if fh > fa else "away" if fa > fh else "tie"
        if winner_side == "tie":
            result = "P"
            note = "tie declared"
        elif pick_side in ("home", "away"):
            result = "W" if pick_side == winner_side else "L"
        else:
            side_guess = "home" if name_matches(pick_team, g["home"]) else (
                         "away" if name_matches(pick_team, g["away"]) else None)
            if side_guess is None:
                return None
            result = "W" if side_guess == winner_side else "L"

    elif bet_type == "runline":
        spread = float(pick.get("spread") or -1.5)
        side = pick_side or ("home" if name_matches(pick_team, g["home"]) else "away")
        margin = (fh - fa) if side == "home" else (fa - fh)
        if margin + spread > 0:
            result = "W"
        elif margin + spread < 0:
            result = "L"
        else:
            result = "P"

    elif bet_type == "total":
        line = float(pick.get("line") or 0)
        direction = (pick.get("direction") or pick.get("ou") or "").lower()  # "over" | "under"
        total = fh + fa
        if total > line:
            result = "W" if direction == "over" else "L"
        elif total < line:
            result = "W" if direction == "under" else "L"
        else:
            result = "P"

    elif bet_type in ("f5", "f5_over", "f5_under"):
        ah, aa = fetch_f5_score(gp)
        if ah is None:
            return None
        line = float(pick.get("line") or 4.5)
        direction = (pick.get("direction") or ("over" if bet_type == "f5_over" else "under")).lower()
        tot = ah + aa
        if tot > line:
            result = "W" if direction == "over" else "L"
        elif tot < line:
            result = "W" if direction == "under" else "L"
        else:
            result = "P"

    else:
        note = f"unsupported betType: {bet_type}"
        result = "void"

    return {
        "result": result,
        "finalHome": fh, "finalAway": fa,
        "settledAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "note": note,
    }


def main() -> int:
    picks_doc = load_json(PICKS_PATH, {"entries": []})
    entries = picks_doc.get("entries") or []
    outcomes_doc = load_json(OUTCOMES_PATH, {"byPickId": {}})
    by_pick = outcomes_doc.get("byPickId") or {}

    # Figure out the date range we need to pull
    dates = set()
    for e in entries:
        d = e.get("date")
        if d:
            dates.add(str(d)[:10])
    if not dates:
        log("no picks to grade")
        outcomes_doc["asOf"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        outcomes_doc["byPickId"] = by_pick
        OUTCOMES_PATH.write_text(json.dumps(outcomes_doc, indent=2) + "\n", encoding="utf-8")
        return 0

    start = min(dates)
    end = max(dates)
    log(f"pulling schedule range {start} to {end}")
    games = fetch_schedule_range(start, end)
    log(f"fetched {len(games)} games across range")

    graded = 0
    skipped = 0
    for e in entries:
        pid = e.get("pickId")
        if not pid:
            continue
        if pid in by_pick and by_pick[pid].get("result") in ("W", "L", "P"):
            continue
        grade = grade_pick(e, games)
        if grade is None:
            skipped += 1
            continue
        by_pick[pid] = grade
        graded += 1

    outcomes_doc["asOf"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    outcomes_doc["byPickId"] = by_pick
    OUTCOMES_PATH.write_text(json.dumps(outcomes_doc, indent=2) + "\n", encoding="utf-8")
    log(f"graded {graded} picks; {skipped} still pending; {len(by_pick)} total in log")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
