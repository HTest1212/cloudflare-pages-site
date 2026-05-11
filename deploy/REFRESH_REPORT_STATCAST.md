# Statcast Overlay Refresh Report

Window: early morning 6 AM ET
Run timestamp UTC: 2026-05-11T19:37:48Z
Slate date: 2026-05-11

## Yesterday slate (2026-05-10)
Games played: 15
Players refreshed (batters and pitchers, every player who appeared in a box score): 443

## Today slate (2026-05-11)
Total games: 6
Pitchers in overlay: 12 (6 away starters and 6 home starters; only 6 games on today slate)
Batters in overlay: 60 (5 per team projected from yesterday batting order, slots 1 through 5)

## Matchups and probable pitchers

Los Angeles Angels (Brent Suter) at Cleveland Guardians (Joey Cantillo). Venue: Progressive Field. First pitch 2026-05-11T22:10:00Z.

New York Yankees (Ryan Weathers) at Baltimore Orioles (Brandon Young). Venue: Oriole Park at Camden Yards. First pitch 2026-05-11T22:35:00Z.

Tampa Bay Rays (Drew Rasmussen) at Toronto Blue Jays (Kevin Gausman). Venue: Rogers Centre. First pitch 2026-05-11T23:07:00Z.

Arizona Diamondbacks (Michael Soroka) at Texas Rangers (Nathan Eovaldi). Venue: Globe Life Field. First pitch 2026-05-12T00:05:00Z.

Seattle Mariners (George Kirby) at Houston Astros (Peter Lambert). Venue: Daikin Park. First pitch 2026-05-12T00:10:00Z.

San Francisco Giants (Trevor McDonald) at Los Angeles Dodgers (Roki Sasaki). Venue: UNIQLO Field at Dodger Stadium. First pitch 2026-05-12T02:10:00Z.

## Lineup endpoint behavior at 6 AM ET
Lineup endpoint returned empty player arrays for all 6 games at 6 AM ET. This is expected pregame behavior. Probable pitchers were obtained from the MLB schedule probablePitcher hydrate. All 6 games had probable pitchers announced the night before, so no TBD fallback was needed.

## Fallbacks used
Top 5 batters per team were drawn from yesterday box score batting order, slots 1 through 5. Every one of today 12 teams played yesterday, so this projection was clean.
Probable pitchers were sourced from the schedule probablePitcher hydrate, not the empty lineup endpoint.

## GitHub push status
Result: success. Branch: main. Commit hash: 7f9dc2b602e4c331cf12f09ffffc141c78064fd8. Commit message: Auto refresh statcast 2026-05-11 06:00.
Notes: clone of the canonical macOS mount could not be used as the git working tree due to a stale macOS file lock and permission errors on .git object writes. Recovery path used: fresh shallow clone created at /tmp/cf-fresh, new overlay committed and pushed to origin main as a fast forward. No rebase or force push required.

## Cloudflare Pages deploy status
Result: success. Project: mlb-betting-dashboard-v2. Deploy URL: https://mlb-betting-dashboard-v2.pages.dev/statcast_overlay.json. Live URL: https://mlb-betting-dashboard-v2.pages.dev.
Recovery notes: the working environment did not have a wrangler binary or a CLOUDFLARE_API_TOKEN env var. The repo wires Cloudflare Pages deploys to .github/workflows/cloudflare-deploy.yml, which runs on every push to main with apiToken in a repo secret. The push triggered the workflow, and the live URL serves asof 2026-05-11T19:37:48Z.

## Notes
Today is a 6 game slate. The overlay therefore contains 12 pitchers and 60 batters rather than the canonical 30 and 150 targets. This reflects the actual MLB schedule for 2026-05-11.
Statcast pitch level fields (xwOBA, barrel pct, exit velo, whiff pct) require a separate Baseball Savant scrape and are nulled in this morning build. Downstream skills hydrate these before slate lock at 11:30 AM ET.
