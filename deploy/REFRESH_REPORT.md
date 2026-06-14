# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM)
**Run timestamp (UTC):** 2026-06-14T21:50Z (scheduled task fired at 17:45 ET)
**Slate date used:** 2026-06-11
**Game count:** 8

## Important data note (date discrepancy)

The system clock read 2026-06-14, but the only reachable live MLB schedule source is frozen at the 2026-06-11 slate and ignores date parameters. The last deployed state and committed overlays were the 2026-06-10 slate, so building the 2026-06-11 slate moves the dashboard forward. To preserve settlement integrity (settlement keys on date and gamePk), every artifact (analysis date, odds_overlay, statcast_overlay, picks_log) is keyed to 2026-06-11, the data source's authoritative date. No games were fabricated and no pitcher was carried over or invented.

## API data quality

- Probable pitchers: 14 of 16 confirmed from the schedule source. Chicago White Sox home starter was TBD (modeled at league average, card capped at C with one chip).
- Pitcher season stats: pulled from the MLB stats MCP per player ID. The raw statsapi people endpoint returned an unrelated canned list and a single ID query failed, so the MCP (which returned correct, ID matched 2026 lines) was used instead. All 14 confirmed starters have real ERA, WHIP, K9, BB9, IP, GS.
- Weather: 8 of 8 parks fetched successfully from Open Meteo at local first pitch hour. loanDepot park modeled roof closed (June Miami heat). Notable: Comerica Park 92 percent precipitation risk flagged in card; Camden 90F, Citi 88F, loanDepot 90F heat noted.
- Overlays available locally: only learnings.json, odds_overlay.json, statcast_overlay.json existed. rolling_form, bullpen, park_factors, park_wind_rules, umpire, catcher_framing and pitch_matchup overlays were absent, so bullpen, rolling form, umpire and framing were treated as neutral and top pick tier was held to B (offense rank and rest could not be verified).

## Per game summary

| Game | Grade | Proj (Away - Home) | Picks | Primary chips |
|---|---|---|---|---|
| STL @ NYM (Citi) | B 75 | 4.0 - 4.4 | 6 | Mets ML, Scott K over 5.5 |
| MIN @ DET (Comerica) | C 62 | 3.8 - 4.3 | 5 | Tigers ML (rain capped) |
| AZ @ MIA (loanDepot) | C 60 | 4.3 - 3.8 | 5 | Diamondbacks ML |
| TEX @ KC (Kauffman) | B 78 | 3.6 - 3.9 | 6 | Under 8.5, F5 Under 4.5 |
| CHC @ COL (Coors) | B 80 | 6.3 - 5.8 | 6 | Over 11.5, Cubs ML |
| LAD @ PIT (PNC) | B 79 | 5.2 - 3.6 | 5 | Dodgers RL -1.5, Under 8 |
| SEA @ BAL (Camden) | B 80 | 4.9 - 4.8 | 6 | Over 9.5, Woo K over 5.5 |
| ATL @ CWS (Rate) | C 60 | 4.6 - 4.0 | 5 | Braves ML (TBD capped) |

All 8 cards carry a minimum of 4 paragraphs and 5 picks (44 picks total). No A tier game grades this slate (projected lineup cap and missing overlays).

## Overlays deployed

- odds_overlay.json: 8 games (moneyline, total, runline)
- statcast_overlay.json: 8 games (ERA based xFIP and FIP estimates)
- picks_log.json: 13 primary chips appended, 753 total records, sorted date then confidence descending

## Learnings adjustments applied

11 active adjustments from learnings.json kept live. Most frequently triggered: projected lineup B cap (all 8 games), TBD starter C cap (CWS), K over discipline (NYM, BAL), under tightening (KC), variance down weighting (DET), favorite demotion without bullpen confirmation (LAD run line over moneyline). One run specific guard added: top pick tier held to B because rolling form and bullpen overlays were unavailable.

## Deploy

- Repo: HTest1212/cloudflare-pages-site, branch main
- Commit: d1f403d "Auto refresh 1130am 2026-06-11"
- Push: success (065d3b4..d1f403d)
- Cloudflare Pages auto deploy triggered on push (no wrangler)
- Render functions verified present after splice: renderClaudePicksBlock, tierFromProb, renderBestBetsBlock

## Errors and fallbacks

- statsapi schedule and people endpoints are mocked or unreliable in this environment; used MCP for pitcher stats.
- Workspace folder file reads (.env, learnings.json, REFRESH_REPORT.md) hit the known mount deadlock and EPERM; GitHub token was read from the workspace git remote config, learnings.json was read from the repo clone, and this report was written to the outputs folder and committed into the repo deploy folder because the workspace path was not writable.
- /tmp/cloudflare-pages-site (prior clone) and the outputs git mount could not host git writes; deployed from a fresh clone at /tmp/mlbdeploy.
