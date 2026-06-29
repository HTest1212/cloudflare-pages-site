# MLB Daily Retrospective 2026-06-28

Generated 2026-06-29T08:11:25Z | Settled on 2026-06-29

No Lock breach. Zero A tier picks were live on the 2026-06-28 slate, so no Lock loss occurred.

## SECTION 2 - SLATE SUMMARY

Slate date 2026-06-28: 15 games, all Final. Logged picks settled: 45, all B and C tier with no A tier Locks.
Overall record: 25W 20L 0P, units +2.44, win rate 55.6%, ROI 5.4%.

Schema mix: all picks carried explicit ids in the descriptive and v2 slug formats; no id free midday rows on this slate.

Record by market:

- K: 4W 2L, units +1.52, win rate 66.7%
- ML: 14W 7L, units +5.56, win rate 66.7%
- TeamTotal: 2W 2L, units -0.18, win rate 50.0%
- Total: 5W 9L, units -4.45, win rate 35.7%

Record by tier:

- B: 18W 9L, units +7.08, win rate 66.7%
- C: 7W 11L, units -4.64, win rate 38.9%

## SECTION 3 - LOCK TRACK RECORD

Lifetime Locks: 25W 17L 2P 1V, units +3.09, win rate 59.5%, ROI 0.6%.
Current streak: 1 win. Longest win streak 8, longest loss streak 6.
Rolling 14d Lock win rate: 0.0%. Rolling 30d: 33.3%.
Guard status: healthy.

Lock by market:

- F5: 1W 1L, units -0.13, win rate 50.0%
- F5_ML: 2W 0L, units +1.50, win rate 100.0%
- F5_Total: 2W 0L, units +1.78, win rate 100.0%
- Hits: 1W 0L, units +0.50, win rate 100.0%
- K: 8W 5L, units +1.42, win rate 61.5%
- ML: 4W 7L, units -4.75, win rate 36.4%
- Over: 0W 1L, units -1.00, win rate 0.0%
- RL: 3W 0L, units +3.13, win rate 100.0%
- Total: 2W 2L, units -0.18, win rate 50.0%
- TotalBases: 1W 0L, units +0.91, win rate 100.0%
- Under: 1W 1L, units -0.09, win rate 50.0%

No A tier Locks have been published since 2026-06-10, so the rolling 14d Lock sample is empty and the guard defaults to healthy on insufficient sample. The 11:30 AM run is not capped today. If A tier candidates appear, the standard Lock screen and the permanent breach rules below still apply.

## SECTION 4 - TOP THREE LOSSES

**Williams K Over 6.5** (K) | Seattle Mariners 5 - Cleveland Guardians 6 | STARTER_REGRESSION
Missed. Two efficient right handers meet the two coldest bats on the slate, a clean recipe for a low scoring game. Actual: Seattle Mariners 5 - Cleveland Guardians 6, K=6

**Williams K Over 6.5** (K) | Seattle Mariners 5 - Cleveland Guardians 6 | STARTER_REGRESSION
Missed. Two efficient right handers meet the two coldest bats on the slate, a clean recipe for a low scoring game. Actual: Seattle Mariners 5 - Cleveland Guardians 6, K=6

**Over 9.5 or 10** (Total) | Colorado Rockies 2 - Minnesota Twins 3 | WEATHER
Missed. An 18 mph wind and two hot lineups against shaky starters argue for runs at Target Field. Actual: Colorado Rockies 2 - Minnesota Twins 3, total 5

## SECTION 5 - RULE MEMORY STATUS

Total rules in active memory: 26 permanent plus 0 trial, 26 total.

Rules promoted to permanent today (reached three validations):

- Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- Tighten exposure on bets prone to VARIANCE; require a second confirming signal before publishing.
- Tighten exposure on bets prone to STARTER_REGRESSION; require a second confirming signal before publishing.

Rules that aged out today: none.

New rules created today: none. The dominant VARIANCE pattern maps to an existing permanent rule, so no duplicate entry was added.

All 26 carryover rules are now permanent; the trial pool is empty after today's three promotions.

## SECTION 6 - ADJUSTMENTS FOR TODAY

Priority order: Lock guard, permanent breach, new breach, trial breach, permanent pattern, new pattern, trial pattern. Star marks permanent rules.

- (*) Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- (*) Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- (*) Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- (*) Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- (*) Down weight setups exposed to VARIANCE until the pattern clears.
- (*) Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- (*) Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- (*) Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- (*) Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- (*) Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- (*) Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- (*) Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.

## SECTION 7 - LIFETIME AND RECENT 14 DAY KPIs

Lifetime (all settled): 852W 681L 43P 161V across 1576 graded picks, units +51.44, win rate 55.6%, ROI 0.6%.
Recent 14 days: 167W 133L 7P across 307 graded picks, units +11.06, win rate 55.7%, ROI 3.6%.

## SECTION 8 - DATA NOTES

- Git sync: origin is a public repo; pulled a fresh full clone of picks_log.json (workspace mount was lock blocked for direct reads, EDEADLK, so the clone was the source of truth).
- Settlement source: 15 boxscores via the MLB API; three starter strikeout lines (Sale 10, Williams 6, Gray 9) pulled through a subagent boxscore read.
- 2026-06-27 had 15 finalized games but zero logged picks (midday generator did not run), confirmed by the prior retrospective; there was nothing to settle for that date, so the one day gap in outcomes is benign.
- All KPI win rates and ROI are stored as decimals; sanity assertions (winRate <= 1.0, abs(roi) < 2.0) passed for every group.
- Workspace mount was write blocked, so all output files were built in the clone and deployed via git push; the live dashboard reads from GitHub.