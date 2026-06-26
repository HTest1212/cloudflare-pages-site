# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM)
Run timestamp (UTC): 2026-06-26T18:21:26Z
Slate date: 2026-06-26
Game count: 15 (all Preview/Scheduled)
Commit: 82e1d7eb903983e21c6e063eae89b89d1b11882d
Push status: success, remote HEAD matches, Cloudflare Pages auto deploy verified live

## API Data Quality
Pitchers confirmed: 27 of 30 slots, TBD: 3 (Mets home, White Sox home, Giants home).
Opener flagged: Steven Cruz (KC) gamesStarted 0, treated as opener, that card capped at C.
Lineups: all 15 projected (no lineup endpoint players at 2:08 PM), every card capped at B plus.
Weather: 14 of 14 outdoor parks fetched from Open Meteo. Tropicana Field skipped as fixed dome.

## Overlays Read
rolling_form_overlay (30 teams), bullpen_availability_overlay (30 teams), hitter_advanced_overlay, bvp_overlay, splits_overlay, learnings.json.
Missing factor overlays: park_factors, park_wind_rules, umpire_factors, catcher_framing, pitch_matchup. Analyst defaults used and top tier held to B.

## Learnings Adjustments Applied
12 active adjustments (VARIANCE downweight, STARTER_REGRESSION downweight, K over floor, road favorite caps, Coors caps, slate exposure cap). Lock guard status: healthy.
Effect: blanket minus 2 on base, top tier held to B, no A tier published, only 5 primary chips across the slate.

## Per Game Summary
| Matchup | Grade | Proj | Picks | Primary Chips |
|---|---|---|---|---|
| HOU @ DET | C/57 | 3.8-3.6 | 6 | Pass/none |
| CIN @ PIT | C/61 | 3.2-3.9 | 6 | Pass/none |
| WSH @ BAL | C/66 | 5.2-3.9 | 6 | WSH ML -105 to -125 |
| TEX @ TOR | C/59 | 4.3-4.8 | 6 | Pass/none |
| SEA @ CLE | C/60 | 3.3-4.1 | 6 | Pass/none |
| ARI @ TB | C/66 | 3.7-4.4 | 6 | TB ML -130 to -150 |
| PHI @ NYM | C/68 | 5.2-3.6 | 6 | Pass/none |
| NYY @ BOS | C/57 | 3.9-3.9 | 6 | Pass/none |
| KC @ CWS | C/68 | 5.6-4.9 | 6 | Pass/none |
| CHC @ MIL | B/70 | 4.4-4.8 | 6 | MIL ML -110 to -130, Misiorowski K over 6.5 |
| COL @ MIN | C/59 | 4.2-5.2 | 6 | Pass/none |
| MIA @ STL | C/57 | 3.7-3.9 | 6 | Pass/none |
| ATH @ LAA | C/65 | 4.1-4.2 | 6 | Pass/none |
| LAD @ SD | C/63 | 3.7-4.5 | 6 | SD ML -110 to -130 |
| ATL @ SF | C/63 | 3.4-3.7 | 6 | Pass/none |

## Overlay Output Counts
odds_overlay.json: 15 games. statcast_overlay.json: 15 games. picks_log.json: 5 new primary chip entries appended (1047 total).

## Errors and Fallbacks
.env unreadable due to mount Resource deadlock; PAT recovered from mount .git/config. Stale prior /tmp clone not removable; built from a fresh self owned clone. No other errors.