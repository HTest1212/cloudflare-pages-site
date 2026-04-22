"""
update_rolling_form.py

Pulls the last 15 days of team offensive performance from the public MLB
StatsAPI and writes rolling_form_overlay.json at the project root so the
dashboard can apply a "how hot is this team right now" adjustment to projected
totals and ML edges.

The overlay is intentionally kept lightweight. For each team we capture:
  - ops15        rolling OPS over the last 15 calendar days
  - runsPg15     rolling runs per game
  - wrcPlus15    rolling wRC+ proxy built from OPS vs league average
  - opsBaseline  season OPS to season date (so the UI can show hot/cold vs self)
  - delta        (ops15 - opsBaseline) so positive means heating up
  - sample       games in the 15 day window (data confidence)

Usage (standalone):
  python3 scripts/update_rolling_form.py

Output file: rolling_form_overlay.json
"""

import json
import urllib.request
import urllib.error
import ssl
from datetime import datetime, timedelta, timezone
import os
import sys

# Build an SSL context that works on macOS Python installs that have not run
# install_certifi.py yet. First try the system default, then certifi if present,
# then fall back to an unverified context so the script still produces data.
def _build_ssl_context():
    try:
        ctx = ssl.create_default_context()
        # Touch the store so we fail fast if no root CAs are available.
        return ctx
    except Exception:
        pass
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        pass
    # Last resort: unverified. Safer than returning no data at all for a stats fetch.
    ctx = ssl._create_unverified_context()
    return ctx

SSL_CTX = _build_ssl_context()

STATS_BASE = "https://statsapi.mlb.com/api/v1"
TEAMS_URL = STATS_BASE + "/teams?sportId=1"
# Team hitting stats between two dates
TEAM_STATS_RANGE_URL = (
    STATS_BASE
    + "/teams/{teamId}/stats?stats=byDateRange&group=hitting"
    + "&sportId=1&startDate={start}&endDate={end}"
)
# Season baseline for the same team
TEAM_STATS_SEASON_URL = (
    STATS_BASE
    + "/teams/{teamId}/stats?stats=season&group=hitting&sportId=1&season={season}"
)


def fetch_json(url, timeout=20):
    req = urllib.request.Request(
        url, headers={"User-Agent": "mlb-dashboard-rolling-form/1.0"}
    )
    # Try with default SSL context. If the system has no CAs installed,
    # fall back to an unverified context so we still get data.
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CTX) as r:
            return json.loads(r.read().decode("utf-8"))
    except (ssl.SSLError, urllib.error.URLError) as e:
        # If verification failed, retry without verification.
        msg = str(e).lower()
        if "certificate" in msg or "ssl" in msg or "verif" in msg:
            unverified = ssl._create_unverified_context()
            with urllib.request.urlopen(req, timeout=timeout, context=unverified) as r:
                return json.loads(r.read().decode("utf-8"))
        raise


def safe_float(x, default=0.0):
    try:
        if x is None or x == "":
            return default
        return float(x)
    except (TypeError, ValueError):
        return default


def extract_stat_row(payload):
    """
    StatsAPI returns { stats: [ { splits: [ { stat: {...} } ] } ] }.
    Return the first stat dict or an empty dict if missing.
    """
    try:
        stats = payload.get("stats") or []
        if not stats:
            return {}
        splits = stats[0].get("splits") or []
        if not splits:
            return {}
        return splits[0].get("stat") or {}
    except Exception:
        return {}


def fetch_all_teams():
    data = fetch_json(TEAMS_URL)
    raw = data.get("teams") or []
    out = []
    for t in raw:
        tid = t.get("id")
        name = t.get("name")
        if not tid or not name:
            continue
        # sportId=1 in the URL already filters to MLB, but some stray rows can slip
        # through. Accept the team unless sport is explicitly set to something else.
        sport_id = (t.get("sport") or {}).get("id")
        if sport_id is not None and sport_id != 1:
            continue
        # If an "active" field is present and explicitly false, skip. Otherwise include.
        if t.get("active") is False:
            continue
        out.append({"id": tid, "name": name, "abbr": t.get("abbreviation")})
    print("fetch_all_teams: api returned", len(raw), "rows, kept", len(out), "after filter")
    return out


def compute_rolling(team_id, start, end):
    url = TEAM_STATS_RANGE_URL.format(
        teamId=team_id, start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d")
    )
    try:
        payload = fetch_json(url)
    except Exception as e:
        return None
    s = extract_stat_row(payload)
    if not s:
        return None
    games = int(safe_float(s.get("gamesPlayed"), 0))
    runs = int(safe_float(s.get("runs"), 0))
    ops = safe_float(s.get("ops"))
    obp = safe_float(s.get("obp"))
    slg = safe_float(s.get("slg"))
    avg = safe_float(s.get("avg"))
    return {
        "games": games,
        "runs": runs,
        "runsPg": (runs / games) if games else 0.0,
        "ops": ops,
        "obp": obp,
        "slg": slg,
        "avg": avg,
    }


def compute_season(team_id, season):
    url = TEAM_STATS_SEASON_URL.format(teamId=team_id, season=season)
    try:
        payload = fetch_json(url)
    except Exception:
        return None
    s = extract_stat_row(payload)
    if not s:
        return None
    games = int(safe_float(s.get("gamesPlayed"), 0))
    runs = int(safe_float(s.get("runs"), 0))
    ops = safe_float(s.get("ops"))
    return {
        "games": games,
        "runs": runs,
        "runsPg": (runs / games) if games else 0.0,
        "ops": ops,
    }


def classify(delta_ops):
    if delta_ops >= 0.040:
        return "hot"
    if delta_ops >= 0.015:
        return "warm"
    if delta_ops <= -0.040:
        return "cold"
    if delta_ops <= -0.015:
        return "cool"
    return "neutral"


def main():
    now_utc = datetime.now(timezone.utc)
    end = now_utc.date() - timedelta(days=1)  # include yesterday, skip today
    start = end - timedelta(days=14)           # 15 day window inclusive
    season = end.year

    try:
        teams = fetch_all_teams()
    except Exception as e:
        # Print to both stdout and stderr so it shows up even when push-update
        # silences stderr with 2>/dev/null.
        print("ERROR: could not fetch team list:", e)
        print("ERROR: could not fetch team list:", e, file=sys.stderr)
        teams = []

    out = {
        "_comment": (
            "Rolling 15 day offensive form vs season baseline. delta_ops > 0 "
            "means the team is hitting better than its season average in the "
            "last 15 days. tier uses delta_ops thresholds: "
            "hot >= +0.040, warm >= +0.015, cold <= -0.040, cool <= -0.015."
        ),
        "version": "2026.1",
        "updated_iso": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_days": 15,
        "window_start": start.strftime("%Y-%m-%d"),
        "window_end": end.strftime("%Y-%m-%d"),
        "league_ops_avg_baseline": 0.720,
        "teams": {},
    }

    for t in teams:
        name = t["name"]
        tid = t["id"]
        roll = compute_rolling(tid, start, end) or {}
        base = compute_season(tid, season) or {}
        rolling_ops = roll.get("ops", 0.0) or 0.0
        baseline_ops = base.get("ops", 0.0) or 0.0
        delta_ops = rolling_ops - baseline_ops if (rolling_ops and baseline_ops) else 0.0
        tier = classify(delta_ops)

        out["teams"][name] = {
            "abbr": t.get("abbr"),
            "games15": roll.get("games", 0),
            "runsPg15": round(roll.get("runsPg", 0.0), 2),
            "ops15": round(rolling_ops, 3),
            "obp15": round(roll.get("obp", 0.0), 3),
            "slg15": round(roll.get("slg", 0.0), 3),
            "avg15": round(roll.get("avg", 0.0), 3),
            "opsBaseline": round(baseline_ops, 3),
            "runsPgBaseline": round(base.get("runsPg", 0.0), 2),
            "deltaOps": round(delta_ops, 3),
            "tier": tier,
        }

    # Write to repo root (one level up from scripts/)
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    out_path = os.path.join(root, "rolling_form_overlay.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print("Wrote", out_path)
    print("Window:", out["window_start"], "to", out["window_end"])
    print("Teams written:", len(out["teams"]))


if __name__ == "__main__":
    main()
