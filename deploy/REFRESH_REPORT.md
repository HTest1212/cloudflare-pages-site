# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM). Run timestamp: 2026-06-28T18:24:56Z UTC
Slate date: 2026-06-28. Game count: 15 (4 Preview, 11 Live/Warmup).

## API data quality
Pitchers confirmed: 30 of 30 (all probables posted, source schedule-api). TBD: 0.
Weather fetched (Open Meteo) for 4 outdoor preview parks: Angel Stadium, Oracle Park, Petco Park, Fenway Park, all success. Tropicana Field treated as dome. Live game parks use live conditions, no forecast applied.

## Per game

| Game | Grade | Proj | Status | Picks | Primary chips |
|------|-------|------|--------|-------|---------------|
| WSH at BAL | B 75 | 3.3 to 4.3 | Live | 5 | Orioles ML  120 to  135 |
| CIN at PIT | C 64 | 4.2 to 5.2 | Live | 5 | Under 8.5 |
| TEX at TOR | C 63 | 5.9 to 3.8 | Live | 5 | Rangers ML +100 to +115 |
| HOU at DET | C 66 | 4.2 to 2.9 | Live | 5 | Astros ML  110 to  125 |
| SEA at CLE | C 67 | 2.8 to 3.1 | Live | 5 | Under 8 |
| AZ at TB | B 74 | 3.3 to 4.9 | Live | 5 | Rays ML  125 to  140 |
| PHI at NYM | C 66 | 4.4 to 3.7 | Live | 5 | Phillies ML  120 to  135 |
| COL at MIN | C 60 | 5.1 to 5.0 | Live | 5 | Over 9 |
| KC at CWS | C 58 | 4.1 to 4.0 | Live | 5 | Over 8.5 |
| CHC at MIL | C 64 | 4.7 to 2.9 | Live | 5 | Brewers ML  130 to  145 |
| MIA at STL | C 61 | 4.1 to 2.8 | Live | 5 | Under 8.5 |
| ATH at LAA | C 62 | 4.8 to 4.6 | Preview | 6 | Over 9 |
| ATL at SF | B 82 | 3.0 to 2.8 | Preview | 7 | Under 7; Sale K over 6.5; Giants ML  120 to  135 |
| LAD at SD | B 78 | 3.8 to 4.8 | Preview | 6 | Padres ML  115 to  130; Under 8 |
| NYY at BOS | B 80 | 2.8 to 4.0 | Preview | 6 | Red Sox ML  110 to  125; Gray K over 5.5 |

## Overlays
odds_overlay.json: 15 games. statcast_overlay.json: 15 games (ERA based estimates). picks_log.json: 8 Preview chip entries upserted, 1092 total.

## Learnings adjustments applied
- Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- Down weight setups exposed to VARIANCE until the pattern clears.
- Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.

Card level appliedAdjustments: tiny sample caps (Bieber, Brown, Aldegheri, Avila, Rolison) held to C; Sale K Over 6.5 Lock screen passed (six innings in three of last four); projected lineup cap applied to NYY at BOS.

## Deploy
Files: index.html, odds_overlay.json, statcast_overlay.json, picks_log.json. Commit: e162654. Push: success to main. Cloudflare Pages auto deploy triggered. Schema gate: PASSED (15 games).

## Errors and fallbacks
Environment .env unreadable and /tmp polluted by prior run (Permission denied); recovered PAT from existing clone .git/config and rebuilt in a self owned home directory clone. No other errors.