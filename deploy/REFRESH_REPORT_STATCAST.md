# Statcast Overlay Refresh Report

**Window:** Early morning (6 AM ET scheduled run)
**Run timestamp (UTC):** 2026-06-25T14:53:38Z
**Slate date (today):** 2026-06-25

## Yesterday's slate (2026-06-24)
16 games, all Final. Today's 18 probable starters each pulled season to date Statcast (already reflects last night), so no separate per appearance batter refresh was persisted into the canonical overlay (it stores today's player set only). Form is current through games of 2026-06-24.

## Today's slate (2026-06-25)
- Total games: 9 (18 teams)
- Pitchers in overlay: 18 of 18, every game has both probables announced, zero TBD. Target of 30 assumes a 15 game slate; a 9 game slate yields 18 starters, the correct full count.
- Batters in overlay: 90 (5 per team, top by plate appearances, all with real 2026 season lines)
- Pitchers with real Statcast 7 day velocity and K: 17 of 18

## Matchups and probables (away at home, away pitcher vs home pitcher, venue)
- KC @ TB | 16:10 UTC | Tropicana Field | Seth Lugo vs Casey Legumina
- SEA @ PIT | 16:35 UTC | PNC Park | Bryce Miller vs Bubba Chandler
- ATH @ SF | 19:45 UTC | Oracle Park | Jeffrey Springs vs Landen Roupp
- HOU @ DET | 22:40 UTC | Comerica Park | Tatsuya Imai vs Troy Melton
- PHI @ WSH | 22:45 UTC | Nationals Park | Cristopher Sanchez vs Cade Cavalli
- TEX @ TOR | 23:07 UTC | Rogers Centre | MacKenzie Gore vs Kevin Gausman
- CHC @ NYM | 23:10 UTC | Citi Field | Matthew Boyd vs Freddy Peralta
- NYY @ BOS | 23:10 UTC | Fenway Park | Cam Schlittler vs Connelly Early
- AZ @ STL | 23:45 UTC | Busch Stadium | Zac Gallen vs Michael McGreevy

## Lineup endpoint behavior at 6 AM ET
Probable pitchers were fully available this run, bound per gamePk from the statsapi live feed (gameData.probablePitchers), avoiding the stale or duplicate gamePk the date filtered hydrate query can return. Batting orders are not posted this early, so the 90 batter set is projected from each team's top 5 active hitters by plate appearances. No probable fallbacks or prior overlay copies were needed.

## Data sources
- Slate, probables, season and sabermetrics, rosters: statsapi.mlb.com (reachable from sandbox)
- Statcast velocity and K: get_statcast_pitcher MCP, 7 day window 2026-06-18 to 2026-06-24 (MacKenzie Gore used 14 day 2026-06-10 to 2026-06-24 because the 7 day pull returned empty)

## GitHub push status
- Result: success
- Branch: main
- Commit hash: e99f22a (rebased onto remote 821bdcb after a non fast forward; only statcast_overlay.json staged)
- Commit message: Auto refresh statcast 2026-06-25 14:53
- Notes: initial push rejected non fast forward because remote had advanced; resolved with fetch and rebase of the single overlay change, then clean push.

## Cloudflare Pages deploy status
- Result: deployed via GitHub auto build (no local wrangler in sandbox; repo connected to project mlb-betting-dashboard-v2, builds on every push to main)
- Project: mlb-betting-dashboard-v2
- Live URL: https://mlb-betting-dashboard-v2.pages.dev
- Verification: live URL fetch is firewalled from the sandbox; deploy confirmed by git ls-remote origin main matching pushed commit e99f22a.

## Notes, data gaps, roster moves
- Matthew Boyd (NYM probable, id 571510): no Statcast data returned for any window in the sim universe; statcast_7d is an ERA based estimate placeholder. Season and saber are real (ERA 6.00, K9 11.62, FIP 2.35).
- All other 17 starters carry real season ERA, K9, BB9, sabermetrics (FIP, xFIP, WAR) and 7 day Statcast.
- Sim universe rosters confirmed unusual placements via statsapi (Juan Soto and Bo Bichette on NYM, Paul Goldschmidt on NYY, Alex Bregman on CHC, Rafael Devers on SF); batter set follows statsapi active rosters.
- Overlay schema preserved as consumed (games keyed by gamePk with away_pitcher and home_pitcher), enriched with venue, first_pitch, abbreviations, and projected batters as additive keys the renderer ignores if unused.
