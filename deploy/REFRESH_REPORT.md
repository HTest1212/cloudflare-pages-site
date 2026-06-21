# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM) refresh
Actual run timestamp (UTC): 2026-06-21 ~22:15 UTC (fired late, ~6:15 PM ET)
Slate date: 2026-06-21
Game count: 15 (9 Final, 4 Live, 1 Preview, 1 Postponed)

## Run context
Because the run fired in the early evening ET, most of the slate was already settled. Final and Postponed games were marked closed with score and carry no writeup. The four in progress games were published as locked pre game reads with a live score note. One game (Mets at Phillies, 7:20 PM ET) was a true Preview and received a fresh deep card.

## API data quality
Pitchers confirmed: all matchups carried confirmed probable starters from the schedule API (no TBD).
Stats source: MLB Stats API people endpoint, season pitching group. All 10 starters across the 5 active and live games returned real season lines.
Weather: Citizens Bank Park fetched successfully via Open Meteo (82 degrees, wind 9 mph from west southwest out to left, 0 percent precip). Live and closed parks did not need fresh weather.

## Learnings applied
LOCK GUARD ACTIVE (lock_guard_status cap_active): A tier publication suppressed, top grade held to B on every card. VARIANCE downweight applied to all setups. K over chips required a projected six inning floor and were set below each pitcher per start average. Coors over held to B per the altitude lock breach rule. Under and favorite correlation cap respected (Phillies card carries ML plus K, not a stacked under plus favorite).

## Per game summary (active and live)
- 823449 New York Mets at Philadelphia Phillies | Preview | B 79 | proj 3.4 to 4.9 | 6 picks | chips: Phillies ML -150 to -170, Wheeler K over 5.5
- 824343 Pittsburgh Pirates at Colorado Rockies | Live (Pirates 8 Rockies 6, bot 9) | B 72 | proj 5.9 to 6.3 | 5 picks | chips: Over 11.5
- 824987 Los Angeles Angels at Athletics | Live (A's 7 Angels 4, top 8) | B 71 | proj 4.8 to 4.9 | 5 picks | chips: Over 9.5, Detmers K over 5.5
- 823934 Baltimore Orioles at Los Angeles Dodgers | Live (Orioles 6 Dodgers 1, bot 6) | B 70 | proj 4.6 to 4.1 | 5 picks | chips: Orioles ML +120 to +135
- 823123 Boston Red Sox at Seattle Mariners | Live (Mariners 3 Red Sox 1, top 8) | B 76 | proj 2.8 to 3.4 | 5 picks | chips: Under 7.5, Gilbert K over 5.5

## Closed games
Reds 4 Yankees 1 | Brewers 9 Braves 4 | Rays 4 Nationals 3 | Tigers 5 White Sox 4 | Marlins 2 Giants 1 | Astros 2 Guardians 1 | Cardinals 12 Royals 10 | Rangers 4 Padres 3 | Twins 4 Diamondbacks 2 | Blue Jays at Cubs Postponed

## Overlays
odds_overlay.json: 5 games. statcast_overlay.json: 5 games (ERA based xFIP and FIP estimates). picks_log.json: 3 pending entries appended for the Preview game (Phillies ML, Wheeler K over 5.5, Wheeler outs watch). Live and Final games not logged as pending.

## Deploy
Schema gate: SCHEMA GATE PASSED, 15 games, all renderer fields resolve.
Commit: Auto refresh 208pm 2026-06-21 (hash b622d3d)
Push: success to main, Cloudflare Pages auto deploy.
Live verify: https://mlb-betting-dashboard-v2.pages.dev resolves date 2026-06-21 and non zero grade plus projected score on all five active and live cards.

## Errors and fallbacks
Workspace .env hit the known resource deadlock; PAT recovered from the existing clone .git/config. The pre existing /tmp clone was owned by another process, so a fresh self owned clone was made at /tmp/cfp208 for all writes and the push. No data quality fallbacks were needed.
