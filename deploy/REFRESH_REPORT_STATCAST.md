# Statcast Overlay Refresh Report

Window: early morning 6 AM ET. Run timestamp: 2026-06-14 10:06 UTC.
Slate date: 2026-06-14.

## Yesterday's slate (2026-06-13)
15 games played, all Final. Every starter and qualified hitter on tonight's teams carries results through 2026-06-13 because the Statcast pull window (2026-05-30 to 2026-06-14) and the season and sabermetric pulls both include last night. Pitchers refreshed: 29 of 30 of today's starters with live Statcast. Batters refreshed: 150 (top 5 by plate appearances per team, season hitting current through last night).

## Today's slate (2026-06-14)
Total games: 15. Pitchers in overlay: 30 of 30 announced (zero TBD). Real Statcast velocity on 29 of 30. Batters in overlay: 150 (5 per team across 30 teams).

## Matchups and probable pitchers

Away at Home, away pitcher vs home pitcher, venue, first pitch UTC.

- MIA at PIT: Max Meyer vs Paul Skenes . PNC Park . 2026-06-14T16:15:00Z
- SD at BAL: Walker Buehler vs Trevor Rogers . Oriole Park at Camden Yards . 2026-06-14T17:35:00Z
- SEA at WSH: Emerson Hancock vs Miles Mikolas . Nationals Park . 2026-06-14T17:35:00Z
- NYY at TOR: Will Warren vs Patrick Corbin . Rogers Centre . 2026-06-14T17:37:00Z
- AZ at CIN: Zac Gallen vs Andrew Abbott . Great American Ball Park . 2026-06-14T17:40:00Z
- DET at CLE: Casey Mize vs Gavin Williams . Progressive Field . 2026-06-14T17:40:00Z
- ATL at NYM: Bryce Elder vs Freddy Peralta . Citi Field . 2026-06-14T17:40:00Z
- HOU at KC: Spencer Arrighetti vs Stephen Kolek . Kauffman Stadium . 2026-06-14T18:10:00Z
- STL at MIN: Michael McGreevy vs Taj Bradley . Target Field . 2026-06-14T18:10:00Z
- LAD at CWS: Emmet Sheehan vs Erick Fedde . Rate Field . 2026-06-14T18:10:00Z
- PHI at MIL: Cristopher Sánchez vs Kyle Harrison . American Family Field . 2026-06-14T18:10:00Z
- COL at ATH: Tomoyuki Sugano vs Jeffrey Springs . Las Vegas Ballpark . 2026-06-14T19:05:00Z
- CHC at SF: Ryan Rolison vs Logan Webb . Oracle Park . 2026-06-14T19:10:00Z
- TB at LAA: Casey Legumina vs Grayson Rodriguez . Angel Stadium . 2026-06-14T20:07:00Z
- TEX at BOS: Nathan Eovaldi vs Connelly Early . Fenway Park . 2026-06-14T23:20:00Z

## Lineup endpoint behavior at 6 AM ET
Lineup player arrays were empty as expected at 6 AM ET. Probable pitchers were resolved straight from statsapi per game feed/live gameData.probablePitchers, bound by authoritative gamePk to avoid stale slate duplicates. No fall back to a prior overlay was needed because all 30 starters were announced.

## GitHub push status
Result: success. Branch: main. Commit: 653a224. Message: Auto refresh statcast 2026-06-14 06:0x. No rebase or force push needed (fast forward). Only statcast_overlay.json was staged.

## Cloudflare Pages deploy status
Result: success. Project: mlb-betting-dashboard-v2. Auto deploy via .github/workflows/cloudflare-deploy.yml on push to main. Live URL: https://mlb-betting-dashboard-v2.pages.dev/statcast_overlay.json verified serving asof 2026-06-14T10:04:59Z with 15 games. No wrangler or recovery paths required.

## Notes
- Casey Mize (DET, 663554) returned no Statcast rows in the 15 day window; he carries real season and sabermetric stats only, velocity null. All other 29 starters have live release speed.
- Prior overlay had a placeholder 92.0 velo for every pitcher; this run replaces it with real per pitcher average release speed across all pitch types.
- Workspace mount was writable this run; canonical statcast_overlay.json updated in place via stage plus atomic rename, and the live deploy matches.
- No IL or roster anomalies spotted while pulling player stats.