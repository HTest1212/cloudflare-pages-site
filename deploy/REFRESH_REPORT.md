# MLB Dashboard Refresh Report

**Window:** early afternoon (2:08 PM)
**Run timestamp:** 2026-06-25 18:10 UTC (2:10 PM ET)
**Slate date:** 2026-06-25
**Game count:** 9 (2 Live, 7 Preview)
**Commit:** 91586d1 — pushed to main, Cloudflare Pages auto deploy verified live (HTTP 200, window and grades resolve non zero)

## API data quality

Probable pitchers: 18 of 18 confirmed from schedule API, zero TBD. All season stats pulled in one batch people call.

Weather fetched for 7 outdoor or retractable parks (Oracle, Comerica, Nationals, Rogers, Citi, Fenway, Busch), all successful. Tropicana Field skipped as a fixed dome. PNC and Trop games already Live.

## Per game summary

| Game | Grade | Proj | Picks | Primary chips | Status |
|---|---|---|---|---|---|
| KC @ TB | C 70 | 1.0 - 8.0 | 5 | Under 8 or 8.5 | Live, Rays 8 to 0 in 8th |
| SEA @ PIT | C 70 | 1.0 - 3.0 | 5 | Under 7.5 or 8 | Live, Pirates 3 to 1 in 6th |
| ATH @ SF | B 74 | 3.7 - 3.6 | 6 | Under 8 or 8.5, Roupp K over 5.5 | Preview, lineups confirmed |
| HOU @ DET | C 66 | 3.8 - 4.3 | 6 | Tigers ML +100 to +115, Under 8.5 or 9 | Preview, lineups projected |
| PHI @ WSH | B 80 | 5.2 - 3.4 | 6 | Phillies ML, Sanchez K over 6.5 | Preview, lineups projected |
| TEX @ TOR | B 74 | 3.5 - 4.4 | 6 | Blue Jays ML, Under 8 or 8.5 | Preview, lineups projected |
| CHC @ NYM | C 67 | 5.2 - 4.4 | 6 | Over 8.5 or 9, Cubs ML | Preview, lineups projected |
| NYY @ BOS | B 78 | 4.1 - 3.0 | 6 | Yankees ML, Under 8 or 8.5 | Preview, lineups projected |
| ARI @ STL | B 73 | 4.0 - 5.0 | 6 | Cardinals ML, Over 8.5 or 9 | Preview, lineups projected |

Top grade on the slate is PHI at B 80, held to B by the active Lock guard despite an ace Sanchez setup. No A tier published.

## Overlay game counts

odds_overlay.json: 9 games. statcast_overlay.json: 9 games (ERA based xFIP and FIP estimates). picks_log.json: 14 upserts for Preview primary and Watch List B entries, 1002 total, Live games not logged as pending.

Bullpen availability overlay covered all 18 teams. Rolling form overlay covered all teams with runsPg15 and form tier. Missing overlays: park_factors, park_wind_rules, umpire_factors, catcher_framing, pitch_matchup — analyst defaults applied and top tier held to B plus per guard.

## Learnings adjustments applied

Lock guard active, A tier capped to B. K over chips required a six inning floor and a trailing rate clearing the line; blocked on Imai and Boyd for low sample and blowup risk. Cold and cool teams (Rangers, Yankees, Red Sox, Cardinals, Mets) never graded ML above C unless a starter mismatch carried a B side. Demoted Cubs ML to a lean on Boyd low sample. Correlated under plus favorite clustering monitored across the slate.

## Errors and fallbacks

Workspace mount unreadable for .env (errno 35 deadlock as expected); recovered PAT from a fresh self owned /tmp clone .git/config. Live URL fetch required following the 308 redirect from /index.html to root. No other errors.
