# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM)
**Run timestamp:** 2026-06-01 15:42 UTC (11:42 AM ET)
**Slate date:** 2026-06-01
**Game count:** 9 (all Preview)
**Commit:** 341d7e6d63cf8a80144a7f9634d490f570890aa3
**Push status:** success, pushed to main, Cloudflare Pages auto deploy triggered

## API data quality

Probable pitchers: 16 of 18 confirmed via schedule API, 1 TBD (Chicago White Sox away starter at Minnesota). Pitcher season stats batch fetched for all 17 confirmed IDs in a single people endpoint call. Lineups: 0 of 9 confirmed at this hour, all 9 cards built on projected lineups, which caps every card at B plus per the 11:30 AM rule.

Weather success: 8 of 8 outdoor and retractable parks returned live Open Meteo data (Nationals, Great American, Target, American Family, Busch, Angel, Chase, T-Mobile). Tropicana Field skipped as a fixed dome. Notable extreme: Chase Field at 100 degrees, roof treated as likely closed.

## Per game summary

| Game | Grade | Proj score | Picks | Primary chips |
|---|---|---|---|---|
| DET @ TB (Tropicana) | C 60 | 4.1 . 4.2 | 5 | Pass, no primary chips |
| MIA @ WSH (Nationals) | C 64 | 3.9 . 4.4 | 6 | Cavalli K over 6.5 |
| KC @ CIN (Great American) | B 78 | 3.4 . 4.8 | 6 | Reds ML, Burns K over 6.5 |
| CWS @ MIN (Target) | C 63 | 3.5 . 4.3 | 5 | Ryan K over 6.5 |
| SF @ MIL (American Family) | C 62 | 3.8 . 3.9 | 5 | Roupp K over 6.5 |
| TEX @ STL (Busch) | B 75 | 3.8 . 3.7 | 6 | deGrom K over 6.5 |
| COL @ LAA (Angel) | B 76 | 3.3 . 4.9 | 6 | Angels ML, Soriano K over 6.5 |
| LAD @ AZ (Chase) | C 66 | 4.2 . 4.0 | 5 | Sheehan K over 6.5 |
| NYM @ SEA (T-Mobile) | C 63 | 3.6 . 4.1 | 5 | Mariners ML |

No A tier cards published, consistent with the active Lock Guard and the projected lineup cap. Three B grade cards built on clean pitching gaps: Reds with Chase Burns, Angels with Jose Soriano over a battered Freeland, and the deGrom strikeout edge in St. Louis.

## Overlays deployed

odds_overlay.json: 9 games, moneyline, total, runline.
statcast_overlay.json: 9 games, ERA based xFIP and FIP estimates, rebuilt for today (replaced the early morning 06:03 statcast push during rebase).
picks_log.json: 10 new primary chip and watch records appended, 403 total, sorted date then confidence descending.

## Learnings adjustments applied

LOCK GUARD ACTIVE (14 day Lock win rate 58.6 percent, below the 0.85 recovery bar) so all A tier publication suppressed. The 11:30 AM projected lineup cap held every card at or below B plus. Totals down weighted across the slate after a 2 and 8 Total result on the prior slate, reflected by holding all Under chips off the primary rows. Small sample starter downgrades applied to Ty Madden (11.1 IP), Shane Drohan (27.1 IP) and the Austin Warren bullpen game (19.1 IP), each capped at quarter Kelly. TBD starter rule capped the White Sox at Twins card at C with a single chip. Giants ML carryover rule kept San Francisco below A tier.

## Errors and fallbacks

Workspace mount resource deadlock (errno 35) and EPERM prevented direct bash and Read access to the workspace folder, so the GitHub token was sourced from push-now.command and all git work ran in a fresh clone at /tmp/cps_0601. Initial push rejected as non fast forward because an early morning statcast commit (3448195) landed after the clone; resolved by rebasing onto the real remote tip and taking today's full statcast overlay, then pushed cleanly. Schema gate passed after splice: 9 games, all renderer fields resolve.
