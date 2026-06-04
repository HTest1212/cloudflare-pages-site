# MLB Dashboard Refresh Report

Window: midday (11:30 AM ET)
Run timestamp: 2026-06-04T15:46:41Z UTC
Slate date: 2026-06-04
Game count: 9

## API data quality
Schedule pulled from MLB Stats API with a date guard. A CDN cache intermittently served a stale 2026-05-30 slate for the hydrated query, so a verify and retry loop locked the correct 2026-06-04 response before any card was built.

Starters confirmed: 16 of 17 probable pitchers confirmed from schedule-api. One TBD (Toronto away starter at Atlanta), capped at C with a single chip per rule.

Pitcher stats: batch fetched in one people call for all 17 confirmed pitcher ids.

Weather: 9 of 9 parks fetched from Open Meteo. Retractable roofs at American Family Field, Daikin Park, and Chase Field projected closed given heat and rain, treated as neutral.

## Per game summary
| Game | Grade | Proj score | Picks | Primary chip |
|---|---|---|---|---|
| SD @ PHI (Citizens Bank) | B 81 | SD 2.9 . PHI 5.3 | 6 | Phillies ML -160 to -175 |
| BAL @ BOS (Fenway) | B 76 | BAL 5.0 . BOS 5.4 | 5 | Over 9.5 |
| CLE @ NYY (Yankee Stadium) | B 77 | CLE 3.6 . NYY 5.3 | 5 | Yankees ML -150 to -165 |
| SF @ MIL (American Family) | C 63 | SF 4.1 . MIL 4.4 | 5 | none (pass) |
| TOR @ ATL (Truist) | C 66 | TOR 3.4 . ATL 4.6 | 5 | Sale K over 6.5 |
| KC @ MIN (Target Field) | C 65 | KC 4.4 . MIN 4.3 | 5 | Royals F5 ML +105 to +120 |
| ATH @ CHC (Wrigley) | C 64 | ATH 4.2 . CHC 4.4 | 5 | none (Over in picks) |
| PIT @ HOU (Daikin Park) | C 65 | PIT 3.5 . HOU 5.1 | 5 | Astros ML -160 to -180 |
| LAD @ AZ (Chase Field) | B 71 | LAD 4.8 . AZ 3.7 | 5 | Dodgers ML -150 to -170 |

Seven primary chips published, all single chips. No A tier cards (Lock Guard active).

## Overlays deployed
odds_overlay.json: 9 games (moneyline, total, runline).
statcast_overlay.json: 9 games, ERA based xFIP and FIP estimates.
picks_log.json: 7 new pending records appended, total 491, sorted date then confidence descending.

## Learnings adjustments applied
12 adjustments active in learnings.json, Lock Guard ACTIVE after a rough prior day (14 and 15, minus 2.46 units). Applied across cards: no A tier publication, ace edges (Wheeler, Sale) capped at B or C, sub 15 inning starters (Giolito, Crow, Jones) downgraded and stake capped, TBD starter capped at C, slate exposure cap held every game to a single chip, K over plays restricted to lines the season rate clears.

## Deploy
Commit: d650daa0a3a7df8b821a1bb86a59a5142d19c410 (analysis), plus this report commit
Message: Auto refresh 1130am 2026-06-04
Push: success to main
Cloudflare Pages auto-deploy verified live, slateDate 2026-06-04, generatedAt 2026-06-04T15:46:41Z, 9 games on the live page.

## Errors and fallbacks
1. Stale slate: hydrated schedule query intermittently returned the 2026-05-30 slate from CDN cache. Mitigated with a date guarded verify and retry loop. Only a verified 2026-06-04 response was used.
2. curl URL globbing: the people endpoint hydrate string contains brackets which curl treated as glob ranges, producing an empty file. Fixed with curl -g.
3. Disk and mount: the /sessions filesystem was full at 0 bytes free, which surfaced as a Resource deadlock on workspace writes. All temp work ran under /tmp and the repo was cloned fresh from origin and spliced there per runbook. The local workspace copies and report could not be written to the mount, so the report is committed to the repo deploy folder instead.
4. Missing overlays: bullpen_availability, rolling_form, catcher_framing, pitch_matchup, park_factors, park_wind_rules, and umpire_factors overlay files were not present on disk. Cards used live API pitcher data, fetched weather, and reasoned park and wind context.
