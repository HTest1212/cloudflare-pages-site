# MLB Dashboard Refresh Report

Window: midday (11:30 AM)  
Run timestamp: 2026-06-01 01:55:38 UTC  
Slate date: 2026-05-31  
Game count: 15

## API data quality

Pitchers confirmed: 30 of 30 (all probable pitchers present in schedule API). TBD: 0.
Note: the schedule people batch endpoint returned a mismatched id set, so pitcher season stats were pulled per id with individual stats calls and joined to the schedule probable names. All 30 returned valid season lines.
Weather: 13 parks fetched from Open Meteo, 2 skipped (dome or no coordinates: Rate Field live, Tropicana dome).

## Per game summary

| Matchup | Grade | Proj Score | Picks | Primary Chips |
|---|---|---|---|---|
| DET@CWS | LIVE | 4.2-4.2 | locked | none (live) |
| SD@WSH | C 62 | 4.0-4.0 | 6 | none |
| KC@TEX | C 58 | 4.1-4.4 | 6 | none |
| TOR@BAL | C 69 | 4.2-3.8 | 6 | none |
| MIN@PIT | C 60 | 4.0-4.4 | 6 | none |
| BOS@CLE | C 66 | 3.4-4.0 | 6 | none |
| LAA@TB | C 69 | 3.7-4.4 | 6 | none |
| MIA@NYM | C 69 | 3.9-3.6 | 6 | none |
| MIL@HOU | B 80 | 4.1-5.4 | 6 | Astros ML -118 to -106, Astros F5 ML -120 to -130 |
| CHC@STL | B 80 | 4.6-3.3 | 6 | Cubs ML -118 to -106, Cubs F5 ML -120 to -130 |
| ATL@CIN | B 80 | 5.6-4.0 | 6 | Braves ML -118 to -106, Braves F5 ML -120 to -130 |
| SF@COL | C 67 | 5.1-5.9 | 6 | none |
| NYY@ATH | C 63 | 3.8-4.2 | 6 | none |
| AZ@SEA | B 71 | 3.5-4.4 | 6 | Mariners ML -118 to -106, Mariners F5 ML -120 to -130 |
| PHI@LAD | C 61 | 4.4-4.5 | 6 | none |

Cards with primary chips: 4 (MIL@HOU, CHC@STL, ATL@CIN, AZ@SEA).  
Total picks generated: 85. Total primary chips: 8.

## Overlays deployed

odds_overlay.json: 15 games. statcast_overlay.json: 15 games (ERA based xFIP and FIP estimates). picks_log.json: 11 new primary or watch entries appended, 393 total records.

## Learnings adjustments applied

- LOCK GUARD ACTIVE: rolling 14d Lock win rate 0.5862 is below the 0.85 threshold, so A tier publication was suppressed. Confidence capped at B (max 84). No A grade or A tier pick was published.
- VARIANCE down weight: prior slate logged 16 VARIANCE losses, setups exposed to that pattern were down weighted.
- Totals down weighted: prior slate totals went 2 and 8, so Under and Over were kept out of every primary chip row and routed to picks and watch list only.

## Deploy

GitHub commit: 110a690d3d2ae326b065cefae61034ab10c3d3fb  
Push status: success (018e48d..110a690 main). First push was rejected by a concurrent retrospective commit, resolved by reset to FETCH_HEAD, re-splice, and re-push.  
Cloudflare Pages auto deploy triggered on push. Wrangler not used.

## Errors and fallbacks

- Workspace mount hit errno 35 resource deadlock on reads, so all repo work was done from the /tmp clone per runbook.
- Pitcher batch people endpoint returned a scrambled id set (zero overlap with schedule ids); fell back to per pitcher season stats calls which returned correct data for all 30.
- Render functions renderClaudePicksBlock, tierFromProb, renderBestBetsBlock verified present after splice.