# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM)
**Run timestamp (UTC):** 2026-06-16T01:24:00Z
**Executed (ET):** 2026-06-15 9:24 PM ET

> Note: the 11:30 AM scheduled job ran late this cycle, at roughly 9:24 PM ET. By run time seven of ten games were already Live and three were in Preview (west coast). Cards were built on confirmed pre game data and each live game records its current inning and score in a liveNote field.

## Slate
- Slate date: 2026-06-15 (America/New_York). UTC clock had already rolled to 2026-06-16, so the New York date was used per instruction.
- Game count: 10

## API Data Quality
- Probable pitchers: 20 of 20 confirmed from the schedule API (source schedule-api). No TBD starters.
- Lineups: 10 of 10 games returned confirmed lineups (9 vs 9). All cards marked confirmed_both.
- Pitcher season stats: raw statsapi people endpoint returned empty across all retries (known issue). Recovered via MCP get_multiple_mlb_player_stats, extracted in a subagent.
- Weather: fetched live for the three Preview parks. Chase Field 99.7 degrees outside so roof treated closed and neutral. Sutter Health Park 87 degrees, brisk southwest wind near 18 mph, outdoor. Dodger Stadium 67 degrees, 12 mph west southwest. Globe Life and Daikin Park roof closed. The seven Live games used seasonal estimates for display since first pitch had passed.

## Per Game Summary
| Game | Grade | Proj Score | Picks | Primary Chips | Status |
|---|---|---|---|---|---|
| MIA @ PHI | B 83 | 3.0 - 5.1 | 6 | Phillies ML, Wheeler K over 6.5 | Live 5-0 PHI |
| KC @ WSH | C 60 | 4.2 - 4.8 | 6 | Nationals ML | Live 7-3 WSH |
| NYM @ CIN | B 82 | 3.4 - 4.6 | 6 | Reds ML, Burns K over 7.5 | Live 9-0 CIN |
| SD @ STL | C 61 | 3.3 - 3.9 | 6 | Under 8 | Live 3-0 STL |
| COL @ CHC | B 80 | 3.2 - 4.7 | 6 | Cubs ML, Imanaga K over 6 | Live 1-0 CHC |
| MIN @ TEX | C 65 | 4.0 - 4.1 | 6 | Gore K over 5.5 | Live 3-2 MIN |
| DET @ HOU | C 66 | 4.2 - 4.0 | 6 | Anderson K over 6.5 | Live 5-0 DET |
| LAA @ ARI | C 62 | 4.4 - 4.5 | 6 | Over 9 | Preview |
| PIT @ ATH | C 64 | 4.3 - 4.6 | 6 | Over 9.5 | Preview |
| TB @ LAD | B 80 | 4.3 - 3.8 | 6 | Rays ML, Over 8.5 | Preview |

No card graded above B. Lock guard is active and the bullpen, rolling form, catcher framing, pitch matchup, park factors, park wind, and umpire overlays were not present in the repo, so the top tier was held to B per the active rules.

## Overlays Deployed
- odds_overlay.json: 10 games (moneyline, total, runline)
- statcast_overlay.json: 10 games, ERA based xFIP and FIP estimates, playerId null

## Learnings Adjustments Applied
- Lock Guard active: A tier capped (rolling 14d Lock win rate 33 percent, below the 85 percent floor). All cards held to B or lower.
- Down weight VARIANCE and STARTER_REGRESSION: extra confirming signal required above C. Applied to KC@WSH, SD@STL, MIN@TEX, DET@HOU, LAA@ARI, PIT@ATH.
- K Over six inning floor and trailing rate check applied; K lines kept modest where short leash or thin sample risk existed (Gore, Anderson, Ginn).
- Low ERA or sub 1.10 WHIP not treated as protection: flagged Urena 5.37 BB9 and Peralta opener role.
- Road ML favorite demoted: Tampa Bay held to B at Dodger Stadium.

## Deploy
- Commit: 34cf50a6f3b71a5dd96d487b3ee30b84277f76c0
- Message: Auto refresh 1130am 2026-06-15
- Push: success, 9f7bbd6..34cf50a main
- Cloudflare Pages: auto deploy confirmed live. generatedAt 2026-06-16T01:23:48Z serving at https://mlb-betting-dashboard-v2.pages.dev
- Schema gate: PASSED, 10 games, all renderer fields resolve.
- Render functions verified present: renderClaudePicksBlock, tierFromProb, renderBestBetsBlock.

## Errors and Fallbacks Used
- statsapi people endpoint returned empty on all attempts. Fallback: MCP get_multiple_mlb_player_stats parsed by subagent. Handedness null in payload, filled from known pitcher data.
- Workspace folder mount hit the known Resource deadlock (errno 35) on all content reads, including learnings.json and .env. Fallback: read learnings.json from the committed repo copy, extracted the push token from the existing clone git config, then made a fresh self owned clone for all writes and the push. REFRESH_REPORT.md was written into the repo deploy folder because the workspace mount could not be written via the file tools.
- Overlay files bullpen_availability, rolling_form, catcher_framing, pitch_matchup, park_factors, park_wind_rules, umpire_factors were not present. Cards built from confirmed API data, fetched weather, and park knowledge. Top tier held to B.
- picks_log.json: appended 14 primary chip records, total now 783 entries, sorted by date then confidence descending, idempotent on id.
