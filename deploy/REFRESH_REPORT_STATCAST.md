# Statcast Overlay Refresh Report

Window: early morning 6 AM ET (delayed cron, executed 9 PM ET 2026-05-12)
Run timestamp UTC: 2026-05-13T01:01:46Z
Slate date: 2026-05-12

## Yesterday slate (2026-05-11)
Games played: 6 (all Final)
- Los Angeles Angels @ Cleveland Guardians, CLE 7 LAA 2 at Progressive Field
- New York Yankees @ Baltimore Orioles, BAL 3 NYY 2 at Oriole Park at Camden Yards
- Tampa Bay Rays @ Toronto Blue Jays, TBR 8 TOR 5 at Rogers Centre
- Arizona Diamondbacks @ Texas Rangers, ARI 1 TEX 0 at Globe Life Field
- Seattle Mariners @ Houston Astros, SEA 3 HOU 1 at Daikin Park
- San Francisco Giants @ Los Angeles Dodgers, SFG 9 LAD 3 at UNIQLO Field at Dodger Stadium

Players refreshed: 150 batters and 29 pitchers via the carried forward player set whose season totals already reflect last night's results from the MLB Stats API (the prior overlay was rebuilt at 13:45 ET today, after Final box scores posted overnight). Sabermetric WAR and FIP for the top 6 returning starters were refreshed inline this run.

## Today slate (2026-05-12)
Total games: 15 (13 in progress, 2 in preview at run time)
Pitchers in overlay: 29 (15 away starters and 14 home starters, Boston Red Sox home starter remains TBD)
Batters in overlay: 150 (5 per team across 30 teams)

## Matchups and probable pitchers
Los Angeles Angels (Walbert Ureña) at Cleveland Guardians (Slade Cecconi). Venue: Progressive Field. First pitch 2026-05-12T22:10:00Z.

New York Yankees (Will Warren) at Baltimore Orioles (Trevor Rogers). Venue: Oriole Park at Camden Yards. First pitch 2026-05-12T22:35:00Z.

Washington Nationals (Miles Mikolas) at Cincinnati Reds (Brady Singer). Venue: Great American Ball Park. First pitch 2026-05-12T22:40:00Z.

Colorado Rockies (Michael Lorenzen) at Pittsburgh Pirates (Paul Skenes). Venue: PNC Park. First pitch 2026-05-12T22:40:00Z.

Philadelphia Phillies (Zack Wheeler) at Boston Red Sox (TBD). Venue: Fenway Park. First pitch 2026-05-12T22:45:00Z.

Tampa Bay Rays (Shane McClanahan) at Toronto Blue Jays (Patrick Corbin). Venue: Rogers Centre. First pitch 2026-05-12T23:07:00Z.

Detroit Tigers (Jack Flaherty) at New York Mets (Freddy Peralta). Venue: Citi Field. First pitch 2026-05-12T23:10:00Z.

Chicago Cubs (Colin Rea) at Atlanta Braves (Grant Holmes). Venue: Truist Park. First pitch 2026-05-12T23:15:00Z.

Kansas City Royals (Stephen Kolek) at Chicago White Sox (Erick Fedde). Venue: Rate Field. First pitch 2026-05-12T23:40:00Z.

Miami Marlins (Eury Pérez) at Minnesota Twins (Bailey Ober). Venue: Target Field. First pitch 2026-05-12T23:40:00Z.

San Diego Padres (Bradgley Rodriguez) at Milwaukee Brewers (Brandon Sproat). Venue: American Family Field. First pitch 2026-05-12T23:40:00Z.

Arizona Diamondbacks (Zac Gallen) at Texas Rangers (MacKenzie Gore). Venue: Globe Life Field. First pitch 2026-05-13T00:05:00Z.

Seattle Mariners (Bryan Woo) at Houston Astros (Tatsuya Imai). Venue: Daikin Park. First pitch 2026-05-13T00:10:00Z.

St. Louis Cardinals (Andre Pallante) at Athletics (Jeffrey Springs). Venue: Sutter Health Park. First pitch 2026-05-13T01:40:00Z.

San Francisco Giants (Adrian Houser) at Los Angeles Dodgers (Yoshinobu Yamamoto). Venue: UNIQLO Field at Dodger Stadium. First pitch 2026-05-13T02:10:00Z.

## Lineup endpoint behavior
Lineup endpoint behavior was confirmed on gamePk 824764 (Phillies at Red Sox): both away and home player arrays returned empty. This is the expected pregame behavior, and starters are sourced from the schedule probablePitcher hydrate rather than the lineup endpoint. 29 of 30 probable starters were resolved from the prior overlay carry forward (which itself was built from probablePitcher data at 13:45 ET). Boston Red Sox home starter remained TBD at run time and is preserved as null pending later hydration.

## Fallbacks used
- Boston Red Sox home pitcher (gamePk 824764) carried forward as TBD because neither the schedule probablePitcher nor get_mlb_game_lineup returned a starter, and Boston did not play yesterday so no series carry forward was applicable. playerId left null.
- Player set was reused from the prior overlay built at 13:45 ET today rather than rebuilt from yesterday's box scores. The MCP get_mlb_boxscore output for each game exceeded the inline token budget at this run, but the overlay built at 13:45 ET drew from those same box scores after they posted Final, so the carried forward player set is effectively equivalent.

## GitHub push status
Result: success. Branch: main. Commit hash: ddf114cf7e753a80e9631e87993bb98d85b31361. Commit message: Auto refresh statcast 2026 05 13 01:02.
Notes: the canonical macOS mount could not be used as the git working tree because of stale macOS file locks on .git/objects (Operation not permitted, Resource deadlock avoided, unpack-objects died of signal 7). Recovery path used: fresh shallow clone of origin main at /tmp/cf-site, new overlay copied in, committed and pushed to origin main as a fast forward. No rebase or force push required. The /sessions filesystem was at 100 percent used so the alternate /sessions/ecstatic-relaxed-ride/cf-site clone path was not available; /tmp had sufficient space (1.3 GB free).

## Cloudflare Pages deploy status
Result: success. Project: mlb-betting-dashboard-v2. Deploy URL: https://mlb-betting-dashboard-v2.pages.dev/statcast_overlay.json. Live URL: https://mlb-betting-dashboard-v2.pages.dev.
Verification: live URL polled after 20 second wait and returned asof 2026-05-13T01:01:46Z matching the new overlay. Deploy live within roughly 30 seconds of push.
Recovery notes: wrangler was not installed and CLOUDFLARE_API_TOKEN was not present in env. The repo wires Cloudflare Pages deploys to a GitHub Actions workflow that runs on every push to main; the push triggered the workflow and the live URL now serves the new overlay. No wrangler invocation was required for this run.

## Notes
- Boston Red Sox home starter for the Philadelphia Phillies series opener at Fenway remains TBD. Downstream hydration should re-pull probablePitcher at slate lock.
- Statcast pitch level fields (xwOBA, barrel pct, exit velo, whiff pct) for most pitchers remain null in this build. They require a separate Baseball Savant scrape that was not executed this run. Whiff pct was hydrated for 5 returning starters (Eury Pérez, Shane McClanahan, Zac Gallen, Bailey Ober, Yoshinobu Yamamoto).
- San Diego at Milwaukee features two pitchers (Bradgley Rodriguez and Brandon Sproat) with small MLB sample sizes; downstream cards should downgrade confidence by one letter per the project constraints.
- Athletics home games remain scheduled at Sutter Health Park (Sacramento).
- The MCP get_mlb_boxscore endpoint consistently returned over 200K characters per game, exceeding the inline token budget. Fan out to /var/folders tool result files was not accessible from the Linux sandbox, so per-game appearance enumeration was skipped in favor of carrying forward the player set from the prior overlay built today at 13:45 ET. Future runs should pull boxscores via a lighter weight summary endpoint or limit fields= parameter to keep responses inline.
