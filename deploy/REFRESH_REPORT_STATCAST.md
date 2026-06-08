# Statcast Overlay Refresh Report

**Window:** Early morning (6 AM ET scheduled run)
**Run timestamp (UTC):** 2026-06-08T15:06:01Z
**Slate date:** 2026-06-08

## Yesterday's slate (2026-06-07)
Games played: 15, all Final. Box scores reviewed for player participation. No Statcast player refresh was persisted this run because today's overlay carries no per player season Statcast block for arbitrary players (the consumed schema stores only today's slate pitchers). With today's probable pitchers unavailable at 6 AM (see below), there were no overlapping player IDs to refresh into the overlay.

## Today's slate (2026-06-08)
Total games: 8
Pitchers in overlay: 16 slots (8 away, 8 home), all marked TBD
Batters in overlay: 0 (existing consumed schema is pitcher only; parity preserved)

### Matchups and probable pitchers (away at home, away pitcher vs home pitcher, venue)
1. Seattle Mariners at Baltimore Orioles, TBD vs TBD, Oriole Park at Camden Yards, first pitch 2026-06-08T22:35:00Z
2. Boston Red Sox at Tampa Bay Rays, TBD vs TBD, Tropicana Field, first pitch 2026-06-08T22:40:00Z
3. New York Yankees at Cleveland Guardians, TBD vs TBD, Progressive Field, first pitch 2026-06-08T22:40:00Z
4. Philadelphia Phillies at Toronto Blue Jays, TBD vs TBD, Rogers Centre, first pitch 2026-06-08T23:07:00Z
5. Houston Astros at Los Angeles Angels, TBD vs TBD, Angel Stadium, first pitch 2026-06-09T01:38:00Z
6. Cincinnati Reds at San Diego Padres, TBD vs TBD, Petco Park, first pitch 2026-06-09T01:40:00Z
7. Washington Nationals at San Francisco Giants, TBD vs TBD, Oracle Park, first pitch 2026-06-09T01:45:00Z
8. Milwaukee Brewers at Athletics, TBD vs TBD, Las Vegas Ballpark (Athletics home series in Las Vegas), first pitch 2026-06-09T02:05:00Z

### Lineup endpoint behavior at 6 AM ET
As expected, get_mlb_game_lineup returned empty player arrays for all 8 games. The preview boxscore carried no probablePitcher field either. Probable pitchers were therefore not retrievable through the available MCP endpoints at this hour.

Fallback per spec is to copy yesterday's probable from the prior overlay where the team series matches. The prior overlay is dated 2026-06-06, and all 8 of today's games are series openers (seriesGameNumber 1) with no continuation from that slate, so no series match was available. All 16 pitcher slots were marked TBD. The 11:30 AM dashboard build populates ERA based pitcher estimates once probables are announced.

## GitHub push status
Result: success
Branch: main
Commit hash: 3691bb2 (from 2ea455c)
Commit message: Auto refresh statcast 2026-06-08 11:06
Notes: The mounted working folder git index was locked (HEAD failed to resolve, the known mount lock condition), so the deploy was performed from a fresh shallow clone of origin/main in a scratch directory. Only statcast_overlay.json was staged for the overlay commit. No rebase or force push was needed; the push fast forwarded.

## Cloudflare Pages deploy status
Result: success (auto build on push to main)
Project: mlb-betting-dashboard-v2
Live URL: https://mlb-betting-dashboard-v2.pages.dev
Verification: fetched the live statcast_overlay.json and confirmed the new asof 2026-06-08T15:06:01Z, slate_date 2026-06-08, 8 games.
Recovery notes: wrangler was not invoked (no wrangler token in the sandbox); the deploy relied on Cloudflare Pages auto build from the GitHub push, the established path for this project.

## Notes / data gaps
- Probable pitchers for all 8 games are TBD. Root cause: at 6 AM ET neither the lineup nor the preview boxscore endpoint exposes probable pitchers for this slate, and no prior overlay series match existed for fallback. This is the single blocking gap; pitcher Statcast splits and batter projections both depend on player IDs, so neither could be assembled this run.
- The overlay schema was kept in parity with the dashboard consumed shape (asof, slate_date, generated_by, games keyed by gamePk with venue, first_pitch, pitchers). away and home team names were added per the enumerated schema as harmless enrichment.
- Sibling overlay files were untouched.
- No IL or roster moves were inspected this run since player level pulls were not reached.
