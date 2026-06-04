# Statcast Overlay Refresh Report

**Window:** Early morning (6 AM ET)
**Run timestamp (UTC):** 2026-06-04T10:06:06Z
**Overlay asof:** 2026-06-04T10:06:06Z
**Slate date:** 2026-06-04

## Yesterday's slate (2026-06-03)

15 games played, all Final. Today's probable pitchers carry a 7 day Statcast window (2026-05-28 to 2026-06-04) that already reflects last night's results, so every probable who pitched recently is current. Final scores: Miami 4 @ Washington 1, Detroit 7 @ Tampa Bay 2, Chicago White Sox 8 @ Minnesota 0, NY Mets 7 @ Seattle 1, San Diego 2 @ Philadelphia 3, Baltimore 1 @ Boston 8, Cleveland 5 @ NY Yankees 4, Kansas City 5 @ Cincinnati 2, Toronto 3 @ Atlanta 7, San Francisco 1 @ Milwaukee 0, Texas 3 @ St. Louis 5, Athletics 5 @ Chicago Cubs 4, Pittsburgh 9 @ Houston 11, Colorado 4 @ LA Angels 11, LA Dodgers 7 @ Arizona 0.

## Today's slate (2026-06-04)

Total games: 9
Pitchers in overlay: 17 of 18 (one TBD). Each has real playerId, season ERA / K9 / BB9, sabermetrics FIP / xFIP, and a 7 day Statcast block (avg velo, K, pitch count).
Batters in overlay: 90 (top 5 by plate appearances per team, 18 teams, season hitting line each).

Note on target counts: the SKILL targets of 30 pitchers and 150 batters assume a 15 game, 30 team slate. Today is a 9 game, 18 team slate, so the scaled set is 17 pitchers (one TBD) and 90 batters. All teams and probables on the slate are covered.

## Matchups and probable pitchers (away at home, away vs home, venue)

| Away | Home | Away SP (ERA) | Home SP (ERA) | Venue |
|---|---|---|---|---|
| San Diego | Philadelphia | Lucas Giolito (4.97) | Zack Wheeler (2.27) | Citizens Bank Park |
| Baltimore | Boston | Trevor Rogers (6.84) | Brayan Bello (5.63) | Fenway Park |
| Cleveland | NY Yankees | Slade Cecconi (5.25) | Carlos Rodon (3.32) | Yankee Stadium |
| San Francisco | Milwaukee | Adrian Houser (5.59) | Coleman Crow (3.14) | American Family Field |
| Toronto | Atlanta | TBD | Chris Sale (2.01) | Truist Park |
| Kansas City | Minnesota | Seth Lugo (3.55) | Andrew Morris (4.07) | Target Field |
| Athletics | Chicago Cubs | J.T. Ginn (2.87) | Shota Imanaga (4.37) | Wrigley Field |
| Pittsburgh | Houston | Jared Jones (10.38) | Kai-Wei Teng (2.57) | Daikin Park |
| LA Dodgers | Arizona | Justin Wrobleski (2.87) | Ryne Nelson (4.82) | Chase Field |

## Lineup endpoint behavior at 6 AM ET

As expected, game lineup and boxscore player arrays are empty this early. Probable pitchers were resolved from the MLB Stats API schedule feed with hydrate=probablePitcher, which is populated the night before. 17 of 18 starters were announced. The one gap (Toronto away at Atlanta) is marked TBD; no prior overlay copy was applied because yesterday's slate had a different Toronto opponent and copying an unrelated probable would be misleading. Projected hitters were built from active rosters plus season hitting (top 5 by plate appearances per team) since lineups are not yet posted.

## GitHub push status

Result: success
Branch: main
Commit hash: 2af143cf591b5be3b92d75a12e7371f8f70499fc
Commit message: Auto refresh statcast 2026-06-04 10:06
Notes: Only statcast_overlay.json was staged for the deploy commit (explicit add by name, no -A). Remote fast forwarded 19908e7 to 2af143c, no rebase or force push needed.

## Cloudflare Pages deploy status

Result: auto deploy via GitHub integration
Project: mlb-betting-dashboard-v2
Live URL: https://mlb-betting-dashboard-v2.pages.dev/statcast_overlay.json
Notes: No local wrangler. The GitHub Pages integration auto builds on every push to main, so the successful push is the deploy. Verified by fetching the live overlay and confirming the new asof.

## Notes and data gaps

- Statcast velocity is the mean release speed across all pitch types in the 7 day window, so values run lower than fastball only velo (roughly 84 to 93 mph this slate). Real pitch level data, replacing the prior overlay placeholder of 92.0 for every pitcher.
- Baseball Savant CSV is firewalled here (403). All Statcast came through the MLB Statcast tool, which proxies the same pitch level data server side.
- One probable still TBD: Toronto at Atlanta (away side). Worth a follow up before the 11:30 build.
- Jared Jones (Pittsburgh) 10.38 ERA and Lucas Giolito (San Diego) 8.53 BB9 are small sample outliers, values faithful to the API.
- Workspace mount was locked (EDEADLK in bash, EPERM in file tools), so the overlay was built and pushed from a fresh origin clone. The user working folder copy was not updated by this run; a recovery script is staged in outputs to refresh the local copy if desired.
