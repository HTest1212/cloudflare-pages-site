"""
update_pitch_matchups.py

Builds pitch_matchup_overlay.json from the public MLB StatsAPI pitch arsenal
endpoint and Baseball Savant's per pitch type xSLG leaderboards. The overlay
lets the dashboard compute, for each SP vs opposing lineup matchup:
  (pitcher usage by pitch type) * (hitter xSLG vs that pitch type)
aggregated across the pitcher's whole arsenal. That sum, versus the league
baseline xSLG, becomes a signed run delta applied to totals and team totals.

Output shape:
{
  "asOf": "YYYY-MM-DD",
  "source": "mlb+savant",
  "baseline": { "xSlgByPitch": { "FF": 0.450, ... } },
  "pitchers": { "<pitcherId>": { "arsenal": { "FF": 0.48, ... }, "name": "..." } },
  "hitters":  { "<batterId>":  { "xSlgByPitch": { "FF": 0.460, ... }, "name": "..." } },
  "teams":    { "<teamId>":    { "xSlgByPitch": { "FF": 0.430, ... } } }
}

Usage:
  python3 scripts/update_pitch_matchups.py

Safe to run daily. If the fetch fails the existing overlay is left on disk so
the dashboard keeps working on stale but valid data.
"""

import csv
import io
import json
import os
import ssl
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone


def _build_ssl_context():
    try:
        return ssl.create_default_context()
    except Exception:
        pass
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    return ssl._create_unverified_context()


SSL_CTX = _build_ssl_context()

STATS_BASE = "https://statsapi.mlb.com/api/v1"
TEAMS_URL = STATS_BASE + "/teams?sportId=1"
# MLB pitch arsenal endpoint: returns a pitcher's usage mix.
PITCH_ARSENAL_URL = (
    STATS_BASE
    + "/people/{pid}/stats?stats=pitchArsenal&group=pitching&season={year}&sportId=1"
)
# Savant pitch type leaderboard (hitter view) returns xSLG by pitch type.
SAVANT_HITTER_URL = (
    "https://baseballsavant.mlb.com/leaderboard/pitch-arsenal-stats"
    "?type=batter&pitchType={pt}&year={year}&min=50&csv=true"
)

# Pitch code normalization. Savant sometimes returns long names, sometimes short.
CODE_MAP = {
    "4-SEAM FASTBALL": "FF", "FOUR-SEAM FASTBALL": "FF", "4-SEAM": "FF", "FASTBALL": "FF",
    "SINKER": "SI", "TWO-SEAM FASTBALL": "SI", "2-SEAM FASTBALL": "SI",
    "CUTTER": "FC",
    "SLIDER": "SL",
    "SWEEPER": "ST",
    "CURVE": "CU", "CURVEBALL": "CU",
    "KNUCKLE CURVE": "KC", "KNUCKLE-CURVE": "KC",
    "CHANGEUP": "CH", "CHANGE-UP": "CH",
    "SPLITTER": "FS", "SPLIT-FINGER": "FS",
}

TARGET_PITCH_CODES = ["FF", "SI", "FC", "SL", "ST", "CU", "KC", "CH", "FS"]


def _http_get(url, tries=3):
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "mlb-dash/1.0"})
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=20) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            last = e
    raise last or RuntimeError("http_get failed")


def _http_json(url):
    body = _http_get(url)
    return json.loads(body)


def _normalize_code(raw):
    if not raw:
        return None
    up = raw.upper().strip()
    if up in CODE_MAP:
        return CODE_MAP[up]
    # Already short form?
    if up in TARGET_PITCH_CODES:
        return up
    return None


def fetch_team_pitchers(year):
    """Gather probable pitcher IDs from every active team. We use the 40 man roster
    as a reasonable superset so we capture anyone who might start this season."""
    teams_payload = _http_json(TEAMS_URL)
    teams = [t for t in teams_payload.get("teams", []) if t.get("sport", {}).get("id") == 1]
    pitcher_ids = {}
    for t in teams:
        tid = t["id"]
        roster_url = STATS_BASE + "/teams/{0}/roster?rosterType=40Man".format(tid)
        try:
            payload = _http_json(roster_url)
            for r in payload.get("roster", []):
                pos = r.get("position", {}).get("abbreviation") or r.get("position", {}).get("code")
                if pos in ("P", "1"):
                    pid = r.get("person", {}).get("id")
                    name = r.get("person", {}).get("fullName")
                    if pid:
                        pitcher_ids[pid] = {"name": name, "teamId": tid, "team": t.get("name")}
        except Exception:
            continue
    return pitcher_ids, teams


def fetch_arsenal(pid, year):
    try:
        payload = _http_json(PITCH_ARSENAL_URL.format(pid=pid, year=year))
    except Exception:
        return None
    splits = (payload.get("stats", [{}])[0] or {}).get("splits", [])
    if not splits:
        return None
    # Each split is a pitch type with a "stat" block that contains percentage thrown.
    arsenal = {}
    total = 0.0
    for s in splits:
        pt = s.get("type", {}).get("description") or s.get("stat", {}).get("type")
        pct = s.get("stat", {}).get("percentage")
        if pct is None:
            pct = s.get("stat", {}).get("pitchPercentage")
        try:
            pct = float(pct)
        except (TypeError, ValueError):
            continue
        # percentage is sometimes 0-100 and sometimes 0-1. Normalize to 0-1.
        if pct > 1.5:
            pct = pct / 100.0
        code = _normalize_code(pt)
        if not code:
            continue
        arsenal[code] = arsenal.get(code, 0) + pct
        total += pct
    if not arsenal or total <= 0:
        return None
    # Re-normalize so usage sums to 1. The API rounds so we may be ~0.99 or ~1.02.
    return {k: round(v / total, 4) for k, v in arsenal.items()}


def fetch_hitter_xslg_by_pitch(year):
    """Returns dicts keyed by batter id and team id with xSLG per pitch type."""
    hitters = {}
    teams = {}
    for pt in TARGET_PITCH_CODES:
        try:
            csv_text = _http_get(SAVANT_HITTER_URL.format(pt=pt, year=year))
        except Exception:
            continue
        reader = csv.DictReader(io.StringIO(csv_text))
        by_team_vals = {}
        for row in reader:
            row = {k.strip(): (v or "").strip() for k, v in row.items()}
            name = row.get("player_name") or row.get("Name") or row.get("Player")
            pid = row.get("player_id") or row.get("player-id")
            team_id = row.get("team_id") or row.get("team-id")
            xslg = row.get("est_slg") or row.get("xSLG") or row.get("xslg")
            if not pid or xslg in (None, ""):
                continue
            try:
                pid_i = int(pid)
                xslg_f = float(xslg)
            except ValueError:
                continue
            hitters.setdefault(pid_i, {"name": name, "xSlgByPitch": {}})
            hitters[pid_i]["xSlgByPitch"][pt] = round(xslg_f, 3)
            if team_id:
                try:
                    tid_i = int(team_id)
                    by_team_vals.setdefault(tid_i, []).append(xslg_f)
                except ValueError:
                    pass
        for tid_i, vals in by_team_vals.items():
            if not vals:
                continue
            avg = sum(vals) / len(vals)
            teams.setdefault(tid_i, {"xSlgByPitch": {}})
            teams[tid_i]["xSlgByPitch"][pt] = round(avg, 3)
    return hitters, teams


def build_overlay(year):
    pitcher_ids, _teams = fetch_team_pitchers(year)
    pitchers = {}
    for pid, meta in pitcher_ids.items():
        arsenal = fetch_arsenal(pid, year)
        if arsenal:
            pitchers[str(pid)] = {"arsenal": arsenal, "name": meta.get("name"), "teamId": meta.get("teamId")}

    hitters, teams = fetch_hitter_xslg_by_pitch(year)

    return {
        "asOf": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "source": "mlb+savant",
        "year": year,
        "baseline": {
            "xSlgByPitch": {
                "FF": 0.450, "SI": 0.420, "FC": 0.400, "SL": 0.370, "ST": 0.365,
                "CU": 0.350, "KC": 0.350, "CH": 0.385, "FS": 0.370
            }
        },
        "pitchers": pitchers,
        "hitters": {str(k): v for k, v in hitters.items()},
        "teams": {str(k): v for k, v in teams.items()},
    }


def main():
    year = os.environ.get("PITCH_MATCHUP_YEAR") or (
        sys.argv[1] if len(sys.argv) > 1 else str(datetime.now(timezone.utc).year)
    )
    out_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "pitch_matchup_overlay.json",
    )
    try:
        overlay = build_overlay(year)
    except Exception as e:
        sys.stderr.write("pitch matchup update failed: {0}\n".format(e))
        sys.exit(1)

    # Only overwrite when we actually pulled meaningful data.
    if not overlay.get("pitchers") or len(overlay["pitchers"]) < 20:
        sys.stderr.write("pitch matchup: too few pitchers in response, keeping existing file\n")
        sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(overlay, f, indent=2, sort_keys=False)
    sys.stdout.write(
        "Wrote {0} pitchers / {1} hitters / {2} teams to {3}\n".format(
            len(overlay["pitchers"]), len(overlay["hitters"]), len(overlay["teams"]), out_path
        )
    )


if __name__ == "__main__":
    main()
