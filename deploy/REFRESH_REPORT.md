# MLB Dashboard Refresh Report

Window: midday (11:30 AM ET)

Run timestamp: 2026-06-09 19:36:31Z UTC

Slate date: 2026-06-09

Game count: 15

## API data quality

Pitchers confirmed: 30 of 30 (all via schedule-api). TBD: 0.
Weather fetched via Open Meteo for 13 outdoor and retractable parks. Tropicana Field skipped (dome). All 13 weather pulls succeeded.
Input overlays (bullpen, rolling form, catcher framing, pitch matchup, park factors, park wind rules, umpire) were not present in the working folder this run and the workspace mount returned resource deadlock on reads, so cards were built from live MLB Stats API pitcher data, Open Meteo weather, and park baselines. learnings.json was read from the origin clone.

## Learnings adjustments applied

LOCK GUARD ACTIVE (rolling 14d Lock win rate 0.625 below 0.85): no A tier cards published. All 15 cards capped at B and all picks capped at B or C tier.
11:30 AM projected lineup cap applied (B plus 84 ceiling); no lineups confirmed at this hour.
K over guards, Oracle under guard, and per slate exposure cap noted across relevant cards.

## Per game summary

- SEA at BAL (Oriole Park at Camden Yards) 6:35 PM ET: grade B 79, proj 5.0 to 4.0, 6 picks. Chips: Mariners ML -120 to -135 | Gilbert K over 6.5
- LAD at PIT (PNC Park) 6:40 PM ET: grade B 80, proj 3.6 to 2.7, 6 picks. Chips: Under 7.5 or 8 | Skenes K over 6.5
- BOS at TB (Tropicana Field) 6:40 PM ET: grade B 78, proj 3.2 to 3.4, 5 picks. Chips: Under 7 | Tolle K over 5.5
- MIN at DET (Comerica Park) 6:40 PM ET: grade C 67, proj 3.7 to 3.5, 5 picks. Chips: Under 8.5
- AZ at MIA (loanDepot park) 6:40 PM ET: grade B 78, proj 4.4 to 3.5, 6 picks. Chips: Marlins ML -110 to -125 | Meyer K over 6.5
- NYY at CLE (Progressive Field) 6:40 PM ET: grade B 74, proj 4.7 to 3.7, 5 picks. Chips: Yankees ML -130 to -145
- PHI at TOR (Rogers Centre) 7:07 PM ET: grade B 81, proj 3.4 to 3.2, 6 picks. Chips: Under 7.5 | Cease K over 7.5 | Wheeler K over 6.5
- STL at NYM (Citi Field) 7:10 PM ET: grade B 76, proj 3.4 to 4.2, 5 picks. Chips: Mets ML -125 to -140 | Peralta K over 6.5
- TEX at KC (Kauffman Stadium) 7:40 PM ET: grade C 66, proj 4.2 to 3.9, 5 picks. Chips: Eovaldi K over 5.5
- ATL at CWS (Rate Field) 7:40 PM ET: grade B 77, proj 4.9 to 3.9, 5 picks. Chips: Braves ML -125 to -140 | Holmes K over 5.5
- CHC at COL (Coors Field) 8:40 PM ET: grade B 80, proj 6.3 to 6.0, 5 picks. Chips: Over 11.5 or 12 | Cubs Team Total Over 5.5
- HOU at LAA (Angel Stadium) 9:38 PM ET: grade C 64, proj 4.0 to 3.8, 5 picks. Chips: Astros Team Total Over 4
- CIN at SD (Petco Park) 9:40 PM ET: grade B 78, proj 3.8 to 3.0, 5 picks. Chips: Reds ML -110 to -125 | Burns K over 6.5
- WSH at SF (Oracle Park) 9:45 PM ET: grade B 78, proj 3.5 to 2.8, 5 picks. Chips: Under 7.5 or 8 | F5 Under 4
- MIL at ATH (Las Vegas Ballpark) 10:05 PM ET: grade C 69, proj 5.2 to 4.6, 5 picks. Chips: Over 9 or 9.5

## Overlays deployed

odds_overlay.json: 15 games
statcast_overlay.json: 15 games
picks_log.json: 26 entries appended for 2026-06-09 (574 total)

## Deploy

GitHub commit: 6f8405216a7071d5290aca4f1344c32ffbb9ea60
Push status: success (3c97813..6f84052 main). Required an unshallow fetch and rebase, resolving a statcast_overlay.json conflict in favor of the fresh 11:30 build.
Cloudflare Pages auto deploy verified live: date 2026-06-09, 15 games, window midday (11:30 AM).

## Errors and fallbacks

Workspace mount resource deadlock blocked direct reads of input overlay files; token and learnings recovered from the workspace .git/config and the origin clone respectively. .env file was not present; GitHub token read from the workspace git remote config. Input overlay data substituted with API plus park baselines as noted above.