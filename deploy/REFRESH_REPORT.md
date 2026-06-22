# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM ET)
Run timestamp UTC: 2026-06-22T18:25:21Z
Slate date: 2026-06-22 | Game count: 13 (all Preview)

## API data quality
Pitchers: 24 confirmed across 11 games via schedule-api batch fetch; 2 TBD away starters (Phillies at WSH gamePk 822720, Brewers at CIN gamePk 824502) set to league average and capped at C with one chip.
Weather: Open Meteo fetched for 12 outdoor or retractable parks (Tropicana dome skipped). All 12 returned. Notable: Coors 88F, Rate Field cool 63F inbound N wind, Nationals 42 percent rain, Citi 41 percent rain.

## Per game
- New York Yankees at Detroit Tigers (824261) B76 | proj 3.6 to 3.4 | 6 picks | chips: Under 7.5 / Yankees ML -118 to -108
- Kansas City Royals at Tampa Bay Rays (822964) B75 | proj 4.1 to 4.0 | 6 picks | chips: Rays ML -120 to -110 / Under 8
- Texas Rangers at Miami Marlins (823851) C64 | proj 3.6 to 4.0 | 6 picks | chips: Marlins ML +100 to +115
- Philadelphia Phillies at Washington Nationals (822720) C62 | proj 4.8 to 4.0 | 6 picks | chips: Phillies ML -120 to -108
- Houston Astros at Toronto Blue Jays (822800) B77 | proj 3.8 to 4.0 | 6 picks | chips: Cease K over 6.5 / Under 8.5
- Chicago Cubs at New York Mets (823613) B76 | proj 5.0 to 4.0 | 6 picks | chips: Cubs ML -110 to +105 / Over 8.5
- Milwaukee Brewers at Cincinnati Reds (824502) C60 | proj 4.5 to 4.6 | 6 picks | chips: Over 9
- Los Angeles Dodgers at Minnesota Twins (823692) B80 | proj 4.0 to 5.4 | 6 picks | chips: Twins ML -120 to -108 / Over 9
- Cleveland Guardians at Chicago White Sox (824585) B74 | proj 3.8 to 3.4 | 6 picks | chips: Under 8 / Williams K over 5.5
- Arizona Diamondbacks at St. Louis Cardinals (823040) C64 | proj 4.3 to 4.4 | 6 picks | chips: Over 9
- Boston Red Sox at Colorado Rockies (824344) B75 | proj 5.5 to 6.0 | 6 picks | chips: Over 11.5 / Red Sox team total over 5.5
- Baltimore Orioles at Los Angeles Angels (824016) B73 | proj 4.8 to 4.4 | 6 picks | chips: Orioles ML -110 to +105 / Over 9
- Atlanta Braves at San Diego Padres (823288) B78 | proj 3.0 to 4.2 | 6 picks | chips: Padres ML -130 to -118 / Under 8

## Overlays
rolling_form_overlay: 26 teams | bullpen_availability_overlay: 26 teams | odds_overlay rebuilt: 13 games | statcast_overlay rebuilt: 13 games | picks_log: 22 primary chips appended for today (idempotent, prior 11:30 today entries replaced).
Missing factor overlays (park_factors, park_wind_rules, umpire_factors, catcher_framing, pitch_matchup): top tier held to B.

## Learnings adjustments applied
Lock guard cap active (no A tier published). Recent form two way modifier applied. Cold form team moneylines (TEX, LAD, STL, ATL) held to C or lower; backed only the opposing warm side. K overs require a six inning floor and trailing form (Cease kept at 6.5, Rasmussen and Bradish trimmed to 5.5). Coors over not locked on wind alone (capped B). Small sample starters (Brown, Bennett, Aldegheri, Alexander) downgraded. VARIANCE down weight enforced.

## Deploy
Commit 714c837 "Auto refresh 208pm 2026-06-22" pushed to main. Remote HEAD matches local (confirmed via git ls-remote). Schema gate PASSED: 13 games, all renderer fields resolve, all four render functions intact. Cloudflare Pages auto-build triggered on push.
Note: sandbox cannot reach pages.dev for live URL confirmation (network allowlist) and web_fetch is provenance restricted; verification rests on confirmed remote HEAD plus passing local schema gate against the pushed index.html.
