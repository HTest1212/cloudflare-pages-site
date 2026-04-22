"""
update_catcher_framing.py

Pulls season to date catcher framing runs (CSAA) from Baseball Savant and writes
catcher_framing_overlay.json at the project root. The overlay is read by the
dashboard to nudge projected team Ks, SP Ks, SP ER, and total runs based on
which catcher is actually catching today.

Output shape:
{
  "asOf": "YYYY-MM-DD",
  "source": "baseballsavant",
  "teams": {
    "Team Name": {
      "starter": { "name", "csaa", "kNudgePerGame", "runNudgePerGame" },
      "backup":  { "name", "csaa", "kNudgePerGame", "runNudgePerGame" }
    }
  },
  "catchers": {
    "Catcher Name": { "csaa", "kNudgePerGame", "runNudgePerGame", "team" }
  }
}

Notes on the math:
  csaa       = Savant framing runs divided by games caught (per game baseline).
               Savant's "runs_extra_strikes" column is total framing runs on
               the season. Dividing by games caught lands us on a per game
               basis so the dashboard can apply it cleanly to a single game.
  kNudgePerGame  = csaa * 0.10. Rough rule of thumb: ten extra strikes per
               game is roughly one extra K, since many stolen strikes end ABs.
  runNudgePerGame = csaa * 0.04. One framing run prevents roughly 0.04 runs
               per game once you average across how often framed pitches turn
               into outs instead of hits or walks.

Usage:
  python3 scripts/update_catcher_framing.py

Safe to run on a schedule. If the fetch fails the existing overlay is left
untouched, which keeps the dashboard working on stale but valid data.
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

# Baseball Savant catcher framing leaderboard CSV endpoint. Year is parameterized
# so we always pull the current season; min=q pulls qualified catchers, then we
# rerun with min=10 to pick up backup catchers who have caught at least 10 games.
SAVANT_URL_TEMPLATE = (
    "https://baseballsavant.mlb.com/leaderboard/catcher-framing"
    "?year={year}&team=&min={min_q}&sort=4,1&csv=true"
)

# Savant team abbreviations (used in some responses) to full names used by the
# MLB StatsAPI. Dashboard keys everything by the StatsAPI team.name.
TEAM_ABBR_TO_NAME = {
    "ARI": "Arizona Diamondbacks",
    "ATL": "Atlanta Braves",
    "BAL": "Baltimore Orioles",
    "BOS": "Boston Red Sox",
    "CHC": "Chicago Cubs",
    "CWS": "Chicago White Sox",
    "CIN": "Cincinnati Reds",
    "CLE": "Cleveland Guardians",
    "COL": "Colorado Rockies",
    "DET": "Detroit Tigers",
    "HOU": "Houston Astros",
    "KC":  "Kansas City Royals",
    "LAA": "Los Angeles Angels",
    "LAD": "Los Angeles Dodgers",
    "MIA": "Miami Marlins",
    "MIL": "Milwaukee Brewers",
    "MIN": "Minnesota Twins",
    "NYM": "New York Mets",
    "NYY": "New York Yankees",
    "OAK": "Athletics",
    "ATH": "Athletics",
    "PHI": "Philadelphia Phillies",
    "PIT": "Pittsburgh Pirates",
    "SD":  "San Diego Padres",
    "SF":  "San Francisco Giants",
    "SEA": "Seattle Mariners",
    "STL": "St. Louis Cardinals",
    "TB":  "Tampa Bay Rays",
    "TEX": "Texas Rangers",
    "TOR": "Toronto Blue Jays",
    "WSH": "Washington Nationals",
}


def _http_get(url, tries=3):
    last_err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "mlb-dash/1.0"})
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=20) as resp:
                return resp.read().decode("utf-8", errors="ignore")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last_err = e
    raise last_err if last_err else RuntimeError("http_get failed")


def _parse_csv(text):
    """Parse a Savant CSV payload into a list of dicts."""
    out = []
    if not text:
        return out
    reader = csv.DictReader(io.StringIO(text))
    for row in reader:
        out.append({k.strip(): (v or "").strip() for k, v in row.items()})
    return out


def _to_float(v, default=0.0):
    if v is None or v == "":
        return default
    try:
        return float(v)
    except ValueError:
        return default


def _extract_catchers(rows):
    """Pull out name, team, games caught, framing runs from Savant rows.

    Savant changes its column headers between seasons, so this function tries a
    handful of likely keys. Falls back to 0 rather than crashing.
    """
    out = []
    for r in rows:
        name = r.get("Player") or r.get("Name") or r.get("player_name") or ""
        if not name:
            continue
        team_abbr = r.get("Team") or r.get("team_abbr") or r.get("team") or ""
        games = _to_float(r.get("Games") or r.get("G") or r.get("n_called_pitches") or 0, 0)
        # Framing runs total. Column has used several names.
        runs = _to_float(
            r.get("Runs Extra Strikes")
            or r.get("Runs_Extra_Strikes")
            or r.get("runs_extra_strikes")
            or r.get("Framing Runs")
            or 0.0,
            0.0,
        )
        # Games caught isn't always exposed. If we only have called-pitches count,
        # convert by assuming ~130 called pitches per game.
        games_caught = games
        if games_caught > 1000:  # that's pitches, not games
            games_caught = max(1.0, games_caught / 130.0)
        if games_caught < 1:
            continue
        csaa = runs / games_caught
        out.append({
            "name": name,
            "team": TEAM_ABBR_TO_NAME.get(team_abbr.upper(), team_abbr),
            "games": games_caught,
            "runs_total": runs,
            "csaa": csaa,
        })
    return out


def build_overlay(year):
    # Pull qualified and min=10 so we capture starters and primary backups.
    primary_raw = _http_get(SAVANT_URL_TEMPLATE.format(year=year, min_q="q"))
    secondary_raw = _http_get(SAVANT_URL_TEMPLATE.format(year=year, min_q="10"))
    primary = _extract_catchers(_parse_csv(primary_raw))
    secondary = _extract_catchers(_parse_csv(secondary_raw))

    # Merge by name, preferring the higher sample size.
    by_name = {}
    for c in primary + secondary:
        existing = by_name.get(c["name"])
        if not existing or c["games"] > existing["games"]:
            by_name[c["name"]] = c

    # Build the per catcher map.
    catchers = {}
    by_team = {}
    for c in by_name.values():
        entry = {
            "csaa": round(c["csaa"], 3),
            "kNudgePerGame": round(c["csaa"] * 0.10, 3),
            "runNudgePerGame": round(c["csaa"] * 0.04, 3),
            "team": c["team"],
            "games": int(round(c["games"])),
        }
        catchers[c["name"]] = entry
        by_team.setdefault(c["team"], []).append({"name": c["name"], **entry})

    # For each team pick the catcher with the most games as starter, next as backup.
    teams = {}
    for team_name, lst in by_team.items():
        lst.sort(key=lambda r: r.get("games", 0), reverse=True)
        starter = lst[0]
        backup = lst[1] if len(lst) > 1 else None
        teams[team_name] = {"starter": starter}
        if backup:
            teams[team_name]["backup"] = backup

    return {
        "asOf": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "source": "baseballsavant",
        "year": year,
        "teams": teams,
        "catchers": catchers,
    }


def main():
    # Default to the current year. Allow override via env var or first argv for testing.
    year = os.environ.get("CATCHER_FRAMING_YEAR") or (
        sys.argv[1] if len(sys.argv) > 1 else str(datetime.now(timezone.utc).year)
    )
    out_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "catcher_framing_overlay.json",
    )
    try:
        overlay = build_overlay(year)
    except Exception as e:
        sys.stderr.write("catcher framing update failed: {0}\n".format(e))
        sys.exit(1)

    # Only overwrite when we pulled at least five teams, otherwise keep the
    # existing file. This guards against Savant serving an empty CSV.
    if not overlay.get("teams") or len(overlay["teams"]) < 5:
        sys.stderr.write("catcher framing: too few teams in response, keeping existing file\n")
        sys.exit(1)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(overlay, f, indent=2, sort_keys=False)
    sys.stdout.write(
        "Wrote {0} catchers across {1} teams to {2}\n".format(
            len(overlay["catchers"]), len(overlay["teams"]), out_path
        )
    )


if __name__ == "__main__":
    main()
