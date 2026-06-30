# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM). Run timestamp (UTC): 2026-06-30T18:58:53Z
Slate date: 2026-06-30. Games on slate: 15.
Commit: 6110372 pushed to main. Cloudflare Pages auto deploy verified at https://mlb-betting-dashboard-v2.pages.dev (asOf 2026-06-30T18:55:22Z, all 15 cards resolve non zero).

## API data quality
Probable pitchers confirmed: 29 of 30 starter slots (29 confirmed, 1 TBD). Only Arizona home starter is TBD.
Weather fetched successfully for 15 of 15 parks via Open Meteo at first pitch hour. Retractable roofs treated as open.
All pitcher season stats pulled live from the MLB Stats API people endpoint in one batch call.

## Per game summary

| Game | Grade | Proj | Picks | Primary chips |
|---|---|---|---|---|
| CWS @ BAL | C60 | 4.4-4.2 | 6 | Pass / lean only |
| TEX @ CLE | C64 | 4.0-3.5 | 6 | Rangers ML -130 to -145 |
| PIT @ PHI | B72 | 4.2-5.1 | 6 | Phillies ML -150 to -165 ; Sánchez K over 5.5 |
| DET @ NYY | B72 | 3.3-3.3 | 6 | Under 7.1 ; Schlittler K over 5.5 |
| NYM @ TOR | D47 | 4.3-4.3 | 6 | Pass / lean only |
| WSH @ BOS | B70 | 3.9-4.6 | 6 | Red Sox ML -140 to -155 |
| STL @ ATL | C59 | 3.3-4.2 | 6 | Pass / lean only |
| TB @ KC | C58 | 4.4-4.2 | 6 | Pass / lean only |
| CIN @ MIL | C58 | 4.7-4.6 | 6 | Pass / lean only |
| SD @ CHC | C58 | 5.0-5.3 | 6 | Pass / lean only |
| MIN @ HOU | B80 | 5.2-3.7 | 6 | Twins ML -180 to -195 ; Ryan K over 5.5 |
| MIA @ COL | C60 | 5.6-5.7 | 6 | Pass / lean only |
| LAD @ ATH | C69 | 4.9-4.1 | 6 | Dodgers ML -145 to -160 |
| LAA @ SEA | B76 | 4.0-2.8 | 6 | Angels ML -165 to -180 ; Soriano K over 5.5 |
| SF @ AZ | C60 | 3.9-4.5 | 6 | Pass / lean only |

## Overlay game counts
odds_overlay.json: 15 games. statcast_overlay.json: 15 games (ERA based estimates). picks_log.json: 11 new primary chips appended, idempotent upsert by id.

## Learnings adjustments applied
12 active adjustments held throughout the run. Lock guard healthy; no A tier published. All cards capped at B+ (84) because lineups are projected at 2:08 PM. Key effects: VARIANCE downweight on correlated under and favorite clusters, K over capped to half unit with six inning floor, Coors altitude variance cap, cold form favorites held below B for moneyline.

## Errors and fallbacks
Workspace mount hit the known resource deadlock (errno 35) on .env and overlay reads; recovered the PAT from .git/config and read all overlays from the fresh /tmp clone. First push rebase hit upstream conflicts from the 11:30 AM run; aborted, hard reset to origin/main, re-spliced over the fresh index.html and re-merged picks_log, then pushed clean. Bullpen overlay data missing for four teams (Cardinals, Braves, Rays, Royals); analyst defaults applied.