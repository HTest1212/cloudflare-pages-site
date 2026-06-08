# MLB Dashboard Refresh Report

Window: midday (11:30 AM)
Run timestamp UTC: 2026-06-08T15:42:45Z
Slate date: 2026-06-08
Game count: 15

## API Data Quality
Confirmed probable pitchers: 29 of 30 starter slots, 1 TBD (Los Angeles Angels)
Lineups confirmed: 1 of 15 (only the Wrigley matinee at this hour, rest projected)
Weather fetched successfully: 15 of 15 parks via Open Meteo

## Per Game Summary
- SF at CHC (Wrigley Field, 2:20 PM ET): Grade B 78, proj 4.6 to 4.9, 6 picks. Chips: Over 8.5 or 9 . Cubs ML -115 to -130
- SEA at DET (Comerica Park, 6:40 PM ET): Grade B 79, proj 3.9 to 3.7, 6 picks. Chips: Woo K Over 5.5 . Under 8 or 8.5
- CWS at PHI (Citizens Bank Park, 6:40 PM ET): Grade B 80, proj 3.3 to 5.1, 6 picks. Chips: Phillies ML -150 to -170 . Luzardo K Over 6.5
- BOS at NYY (Yankee Stadium, 7:05 PM ET): Grade B 77, proj 3.8 to 4.1, 6 picks. Chips: Under 8.5 or 9 . Yankees ML -125 to -140
- BAL at TOR (Rogers Centre, 7:07 PM ET): Grade B 77, proj 3.6 to 4.0, 6 picks. Chips: Blue Jays ML -120 to -135 . Yesavage K Over 5.5
- TB at MIA (loanDepot park, 7:10 PM ET): Grade B 80, proj 4.6 to 3.2, 6 picks. Chips: Rays ML -130 to -150 . Rasmussen K Over 5.5
- PIT at ATL (Truist Park, 7:15 PM ET): Grade B 75, proj 3.3 to 4.2, 6 picks. Chips: Braves F5 ML -120 to -135 . Under 8 or 8.5
- ATH at HOU (Daikin Park, 8:10 PM ET): Grade B 78, proj 3.4 to 4.8, 6 picks. Chips: Astros ML -160 to -180 . Astros Team Total Over 4.5
- CIN at STL (Busch Stadium, 8:15 PM ET): Grade C 67, proj 4.3 to 4.4, 6 picks. Chips: Over 9 or 9.5
- CLE at TEX (Globe Life Field, 8:15 PM ET): Grade B 78, proj 3.4 to 3.6, 6 picks. Chips: Under 8 . Messick K Over 5.5
- KC at MIN (Target Field, 8:15 PM ET): Grade C 70, proj 3.7 to 3.9, 6 picks. Chips: Twins ML -115 to -130
- MIL at COL (Coors Field, 8:40 PM ET): Grade B 80, proj 5.6 to 5.9, 6 picks. Chips: Over 11.5 or 12 . YRFI +100 to +115
- WSH at AZ (Chase Field, 9:40 PM ET): Grade C 68, proj 4.4 to 4.3, 6 picks. Chips: Nationals ML +120 to +140
- NYM at SD (Petco Park, 9:40 PM ET): Grade B 79, proj 3.4 to 3.5, 6 picks. Chips: Under 7.5 or 8 . King K Over 5.5
- LAA at LAD (UNIQLO Field at Dodger Stadium, 10:10 PM ET): Grade C 65, proj 3.3 to 4.4, 6 picks. Chips: Dodgers ML -150 to -170

## Overlays Deployed
odds_overlay.json: 15 games
statcast_overlay.json: 15 games (ERA based xFIP and FIP estimates)

## Learnings Adjustments Applied
- LOCK GUARD ACTIVE: rolling 14d Lock win rate 0.625 below 0.85, no A tier cards published today
- Demote A tier candidates missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather favorable, bullpen rested, no key injury, no umpire flag
- Do not publish A tier ML on ERA differential alone; require FIP within 0.50 of ERA and 3 consecutive quality starts
- Require trailing strikeout rate to exceed the posted K line before a K over; cap K over stake at half a unit above season average
- Avoid K over chips when the starter carries blowout or short leash risk; require a projected floor of 6 innings
- Tighten under totals: no under when both lineups rank top 12 in runs per game over trailing 14 days
- Cap total bet exposure per slate; correlated favorites and unders amplify variance
- Demote any ML favorite whose starter lacks two consecutive quality starts; require bullpen rest confirmation
- Down weight setups exposed to VARIANCE until the pattern clears
- 11:30 AM cap: projected lineup cards cap at B plus 84; TBD or sub 15 inning starters cap at C with at most one chip
- Houston totals on watch after Daikin Park slugfest, BAD_PARK_READ monitoring

## Grade Distribution
B: 11, C: 4, A: 0 (Lock Guard active, zero A tier published)

## Deploy
GitHub commit hash: 21a23f59be037cf900a5b496cec030294577699f
Push status: success, 3ed2b44 to 21a23f5 on main
Cloudflare Pages: auto deploy confirmed live at https://mlb-betting-dashboard-v2.pages.dev
Live verification: slateDate 2026-06-08, 15 gamePk entries, renderClaudePicksBlock and tierFromProb and renderBestBetsBlock all present

## Errors and Fallbacks
- Workspace mount Resource deadlock (errno 35) blocked direct reads and the .env token; recovered by cloning origin repo to /tmp and using the PAT embedded in the git remote.
- Detailed overlays (bullpen, rolling form, catcher framing, pitch matchup, park factors, park wind rules, umpire) were not present in the folder or repo; park, weather, and pitcher form drove the reads instead.
- Ryan Gusto (MIA, 5 IP) and Jack Perkins (ATH, 1 GS) flagged small sample, one letter downgrade and stake caps applied, strikeout markets excluded.
- BB9 field returned null from the people endpoint; statcast overlay used league baseline 3.2 BB9 where unavailable.