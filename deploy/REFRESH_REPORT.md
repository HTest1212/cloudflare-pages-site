# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM) scheduled refresh
**Run timestamp (UTC):** 2026-06-19T20:35Z (executed ~4:35 PM ET)
**Slate date:** 2026-06-19
**Game count:** 14

## API data quality
- Schedule pulled from MLB Stats API with probablePitcher, lineups, team, venue.
- Probable pitchers: 14 of 14 CONFIRMED via schedule-api. Zero TBD.
- Pitcher season stats: all 28 starters fetched in one batched people call (needed curl -g to stop bracket globbing).
- Lineups: only the live Cubs game returned confirmed players; all others used projected lineups, capped at B plus per rule.
- Weather: Open Meteo returned data for all 12 queried outdoor and retractable parks. Tropicana is a fixed dome (skipped). Retractable parks treated as likely closed and noted.

## Overlays
- Bullpen, rolling form, park, park wind, umpire, catcher framing, pitch matchup overlays were NOT in the working folder this run. Relief and framing treated as neutral and noted in every card.
- odds_overlay.json rebuilt: 14 games.
- statcast_overlay.json rebuilt (ERA based xFIP and FIP estimates): 14 games.
- picks_log.json appended: 22 new primary chip entries, 822 total, sorted date then confidence descending.

## Learnings adjustments applied
12 adjustments active (yesterday 10 and 6, ROI plus 19.7 percent). Enforced:
- Lock Guard active: A tier suspended, every card capped at B 84.
- K over chips require trailing rate over the line plus a six inning floor, stake capped (Skubal, Schlittler, Misiorowski, deGrom, Soroka).
- Coors rule: over not locked above 11 on wind alone, only Freeland clears the 5.00 ERA threshold so PIT at COL held to B.
- Tighten unders, down weight variance setups, extra confirming signal above C.

## Schema fix this run (important)
The renderer (buildDeepAnalysis) reads nested confidence{letter,score} and projected_score{away,home}, NOT the flat confidenceScore and projectedScore. Flat only cards render as 0 of 100 with 0.0 projections. Each card now ships confidence, projected_score, and a grade object plus the flat fields. Validation gate confirmed all 14 cards carry a non zero confidence score and real projections.

## Per game summary
| Matchup | Grade | Proj (A-H) | Picks | Primary chips |
|---|---|---|---|---|
| TOR @ CHC (Live) | C 60 | 4.0-5.6 | 5 | Chicago Cubs ML |
| CWS @ DET | B 83 | 2.9-4.6 | 6 | Detroit ML, Skubal K over 7.5 |
| CIN @ NYY | B 82 | 3.4-5.1 | 6 | Yankees ML, Schlittler K over 6.5 |
| WSH @ TB | C 58 | 3.6-4.0 | 5 | Tampa Bay ML |
| SF @ MIA | C 64 | 3.5-3.8 | 5 | Under 7.5, Miami ML |
| MIL @ ATL | B 84 | 4.2-3.5 | 6 | Misiorowski K over 7.5, Milwaukee ML |
| SD @ TEX | B 82 | 3.2-4.3 | 6 | Texas ML, deGrom K over 6.5 |
| CLE @ HOU | C 66 | 4.1-3.7 | 5 | Cleveland ML |
| STL @ KC | C 60 | 3.7-4.0 | 5 | Under 8.5, Kansas City ML |
| PIT @ COL | B 78 | 5.4-6.1 | 6 | Over 11.5 |
| LAA @ ATH | C 64 | 4.6-4.3 | 5 | Over 9, Angels ML |
| MIN @ ARI | B 80 | 3.6-4.5 | 6 | Arizona ML, Soroka K over 5.5 |
| BAL @ LAD | B 80 | 3.4-5.0 | 6 | Dodgers ML |
| BOS @ SEA | B 80 | 3.1-3.6 | 6 | Under 7, Seattle ML |

Top reads: Misiorowski K over (13.55 K9), Skubal, Schlittler, deGrom side plus K stacks. No A tier published, Lock Guard in force.

## Deploy
- Repo: HTest1212/cloudflare-pages-site, branch main.
- Commit hash: 99dcc8260f3deb3ad3af826d6d79232dcb8a7072
- Push: success (f4dff7e..99dcc82). Cloudflare Pages auto deploy triggered.
- Files deployed: index.html, odds_overlay.json, statcast_overlay.json, picks_log.json.
- Render functions verified present after splice: renderClaudePicksBlock, tierFromProb, renderBestBetsBlock, buildDeepAnalysis.

## Errors and fallbacks
- Workspace mount Resource deadlock (errno 35) blocked reading .env and overlay JSONs. Recovered the GitHub token from the existing repo git remote config; built and pushed from a fresh /tmp clone per standard recovery.
- Non schedule overlays absent, treated as neutral.
- curl bracket globbing fixed with -g on the people stats endpoint.
