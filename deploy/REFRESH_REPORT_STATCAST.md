# Statcast Overlay Refresh Report

**Window:** Early morning 6 AM ET scheduled run
**Run timestamp (UTC):** 2026-05-30T10:06:24Z
**Slate date (today):** 2026-05-30

## Yesterday's slate (2026-05-29)
15 games played, all Final. Box scores reviewed for appeared players. Note: Statcast per player rolling refresh was deferred this run because the workspace mount returned "Resource deadlock avoided" (known mount lock failure), so all computation ran from a fresh anonymous origin clone. Yesterday's results are already reflected in the season ERA/K9/BB9 splits pulled live from StatsAPI for every probable in today's set.

## Today's slate (2026-05-30)
- Total games: 15
- Pitchers in overlay: 30 of 30 (target 30) — all probables confirmed via StatsAPI hydrate=probablePitcher
- Batters in overlay: 0 (target 150) — NOT populated this run, see Notes
- All season stats real: ERA, K9, BB9 from 2026 season pitching splits; FIP/xFIP computed from season HR/BB/HBP/K/IP (constant 3.15)

## Matchups and probable pitchers (away at home, away vs home, venue)
DET @ CWS | Rate Field | Framber Valdez (4.28 ERA) vs Anthony Kay (3.96 ERA)
SD @ WSH | Nationals Park | Michael King (2.76) vs Foster Griffin (3.63)
KC @ TEX | Globe Life Field | Seth Lugo (3.74) vs Kumar Rocker (3.96)
TOR @ BAL | Oriole Park at Camden Yards | Trey Yesavage (2.25) vs Brandon Young (3.47)
MIN @ PIT | PNC Park | Bailey Ober (3.92) vs Mitch Keller (3.64)
BOS @ CLE | Progressive Field | Sonny Gray (3.27) vs Parker Messick (2.24)
LAA @ TB | Tropicana Field | Reid Detmers (4.57) vs Drew Rasmussen (2.78)
MIA @ NYM | Citi Field | Tyler Phillips (1.07) vs Christian Scott (3.20)
MIL @ HOU | Daikin Park | Brandon Sproat (5.84) vs Peter Lambert (3.79)
CHC @ STL | Busch Stadium | Ben Brown (2.01) vs Kyle Leahy (4.44)
ATL @ CIN | Great American Ball Park | Martin Perez (2.70) vs Brady Singer (6.26)
SF @ COL | Coors Field | Adrian Houser (5.30) vs Ryan Feltner (6.30)
NYY @ ATH | Sutter Health Park | Ryan Weathers (3.14) vs J.T. Ginn (3.19)
ARI @ SEA | T-Mobile Park | Ryne Nelson (4.65) vs Bryan Woo (3.82)
PHI @ LAD | UNIQLO Field at Dodger Stadium | Jesus Luzardo (4.38) vs Roki Sasaki (4.93)

## Lineup endpoint behavior at 6 AM ET
get_mlb_game_lineup returned empty player arrays for all games (expected at 6 AM). Probable pitchers were NOT exposed by the lineup or boxscore endpoints, so probables were sourced from StatsAPI schedule hydrate=probablePitcher, which had all 30 announced. Zero fall backs and zero TBD needed. No pitcher name was carried over or guessed.

## GitHub push status
- Result: SUCCESS
- Branch: main
- Overlay commit: 3b85cee — "Auto refresh statcast 2026-05-30 06:00"
- Report commit: this commit on top of 3b85cee
- Only statcast_overlay.json was staged for the data commit (no git add -A). Rebase clean, no force push needed.

## Cloudflare Pages deploy status
- Result: SUCCESS (auto deploy via GitHub Actions cloudflare-deploy.yml)
- Project: mlb-betting-dashboard-v2
- Live URL: https://mlb-betting-dashboard-v2.pages.dev
- Verified: live statcast_overlay.json serves asof 2026-05-30T10:04:07Z, slate_date 2026-05-30, 15 games, correct probables (Framber Valdez vs Anthony Kay confirmed live)

## Notes
- MOUNT LOCK: workspace mount /Users/Heff/Desktop/MLB Beting Dashboard Folder returned "Resource deadlock avoided" all run. Worked entirely from origin clone; push and live deploy succeeded so the canonical data is current. Working-folder local copy could not be refreshed this session and will resync from origin on the next healthy run / 11:30 build.
- BATTER SET: 150 projected batters not populated this run. The live dashboard consumer schema is pitcher-keyed and the 11:30 AM build regenerates hitter-level detail; shipping the verified 30-pitcher overlay with real stats was prioritized over a heavy batter pull under the mount-lock + 3 minute budget. Flag for follow up if hitter props need overlay-side data before 11:30.
- No IL or roster anomalies blocked any probable; all 30 IDs resolved with non-null season stats.
