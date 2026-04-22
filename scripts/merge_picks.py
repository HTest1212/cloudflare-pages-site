#!/usr/bin/env python3
"""
merge_picks.py

Merges a client-exported daily picks file into picks_log.json.

The dashboard's Value Bets tab has an "Export picks" button that downloads a
file like picks_export_2026-04-20.json. When the user places that file in the
repo root and commits it, this script (or the GitHub workflow) rolls it into
picks_log.json and removes the export file so the next day starts clean.

Input:
  - picks_export_*.json at repo root
  - picks_log.json at repo root (or new)

Output:
  Updated picks_log.json with new entries appended (idempotent by pickId).

Export file shape (from the dashboard):
  {
    "date": "2026-04-20",
    "asOf": "2026-04-20T17:45:00Z",
    "bankroll": 1000,
    "entries": [
      {
        "pickId": "2026-04-20-824371-away-ml",
        "date": "2026-04-20",
        "gamePk": 824371,
        "pick": "Yankees ML",
        "pickTeam": "New York Yankees",
        "side": "away",
        "betType": "moneyline",
        "priceAtLock": -140,
        "fairAtLock": 0.575,
        "modelProb": 0.62,
        "edgePts": 4.5,
        "kelly": 0.021,
        "tier": "value",
        "book": "consensus",
        "lockAt": "2026-04-20T17:45:00Z"
      }
    ]
  }
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import datetime as dt
import glob


PICKS_PATH = Path(os.environ.get("PICKS_LOG_PATH", "picks_log.json"))


def log(msg: str) -> None:
    print(f"[merge_picks] {msg}", flush=True)


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def main() -> int:
    exports = sorted(glob.glob("picks_export_*.json"))
    if not exports:
        log("no export files found, nothing to merge")
        return 0

    picks_doc = load_json(PICKS_PATH, {"entries": []})
    entries = picks_doc.get("entries") or []
    by_id = {e.get("pickId"): i for i, e in enumerate(entries) if e.get("pickId")}

    added = 0
    updated = 0
    for exp_path in exports:
        try:
            exp = json.loads(Path(exp_path).read_text())
        except Exception as e:
            log(f"skip {exp_path}: {e}")
            continue
        for entry in exp.get("entries", []):
            pid = entry.get("pickId")
            if not pid:
                continue
            if pid in by_id:
                entries[by_id[pid]] = entry
                updated += 1
            else:
                entries.append(entry)
                by_id[pid] = len(entries) - 1
                added += 1

    picks_doc["entries"] = entries
    picks_doc["asOf"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    PICKS_PATH.write_text(json.dumps(picks_doc, indent=2) + "\n", encoding="utf-8")
    log(f"merged: {added} new, {updated} updated, {len(entries)} total")

    # Remove the consumed export files so they don't get re-processed
    for exp_path in exports:
        try:
            Path(exp_path).unlink()
            log(f"removed {exp_path}")
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
