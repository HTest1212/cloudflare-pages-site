# MLB Daily Retrospective Report

Report date 2026-06-18 . Settlement target slate 2026-06-17

## Section 2 . Slate Summary

Yesterday slate date 2026-06-17 . Total games 15 . All games Final.

HARD ERROR: Zero picks were found for 2026-06-17 across all three picks_log schemas (v2, v1, midday). The full 15 game slate finalized but no recommendations exist to settle. The most recent picks in picks_log are dated 2026-06-15.

Record by schema: v2 0 . v1 0 . midday 0 . Overall 0W 0L 0P 0 void.
No record breakdown by market or tier is possible for this date.

## Section 3 . Lock Track Record

Lifetime Locks (A tier): 25W 17L 2P 1 void . Win rate 59.5% . Units +3.09 . ROI 7.0%
Current streak: loss 1 . Longest win streak 8 . Longest loss streak 6
Rolling 14d Lock win rate 33.3% . Rolling 30d Lock win rate 54.3%

Lock by market:

| Market | Picks | W | L | Win rate | Units | ROI |
|---|---|---|---|---|---|---|
| K | 13 | 8 | 5 | 61.5% | +1.42 | 10.9% |
| ML | 11 | 4 | 7 | 36.4% | -4.75 | -43.2% |
| Total | 5 | 2 | 2 | 50.0% | -0.18 | -3.6% |
| F5_ML | 3 | 2 | 0 | 100.0% | +1.50 | 49.9% |
| RL | 3 | 3 | 0 | 100.0% | +3.13 | 104.3% |
| F5 | 2 | 1 | 1 | 50.0% | -0.13 | -6.5% |
| F5_Total | 2 | 2 | 0 | 100.0% | +1.78 | 88.9% |
| Under | 2 | 1 | 1 | 50.0% | -0.09 | -4.5% |
| Hits | 1 | 1 | 0 | 100.0% | +0.50 | 50.0% |
| Over | 1 | 0 | 1 | 0.0% | -1.00 | -100.0% |
| TotalBases | 1 | 1 | 0 | 100.0% | +0.91 | 90.9% |

Guard status: cap_active. The rolling 14d Lock win rate of 33.3% sits below the 0.80 threshold, so the cap remains active. The 11:30 AM run will cap A tier publication until the rolling 14d Lock win rate recovers to 0.85 and will demote any A tier candidate missing four or more of the seven confirmation signals. The four Lock losses driving this cap occurred on 2026-06-10 and age out of the 14d window after 2026-06-24.

## Section 4 . Top Three Losses With Diagnoses

No picks settled for 2026-06-17, so there are no losses to diagnose for this date.

## Section 5 . Rule Memory Status

Permanent rules (never expire): 15
- [pattern, validated 13x, first learned 2026-05-29] Down weight setups exposed to VARIANCE until the pattern clears.
- [pattern, validated 10x, first learned 2026-05-28] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- [pattern, validated 10x, first learned 2026-05-30] Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- [pattern, validated 8x, first learned 2026-06-01] Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- [pattern, validated 7x, first learned 2026-05-30] Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- [pattern, validated 6x, first learned 2026-05-30] Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- [pattern, validated 5x, first learned 2026-06-10] Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- [lock_breach, validated 4x, first learned 2026-06-10] Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- [pattern, validated 4x, first learned 2026-06-10] Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- [manual, validated 3x, first learned 2026-05-20] Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- [manual, validated 3x, first learned 2026-05-20] Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- [manual, validated 3x, first learned 2026-05-20] Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- [manual, validated 3x, first learned 2026-05-20] Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- [lock_breach, validated 3x, first learned 2026-06-10] Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- [pattern, validated 3x, first learned 2026-06-11] A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.

Rules promoted to permanent today: 0

Trial rules still accumulating evidence: 4
- [lock_breach, validated 2 of 3, expires 2026-06-28] Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- [lock_breach, validated 2 of 3, expires 2026-06-28] Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- [pattern, validated 1 of 3, expires 2026-06-17] Down weight setups exposed to BAD_PARK_READ; require an extra confirming signal before grading above C.
- [pattern, validated 2 of 3, expires 2026-06-21] K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.

Rules that aged out today: 0
New rules created today: 0 (no losses to learn from)
Total rules in active memory: 15 permanent + 4 trial

## Section 6 . Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. *
3. Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B. *
4. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
5. Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
6. Down weight setups exposed to VARIANCE until the pattern clears. *
7. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
8. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
9. Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *
10. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
11. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *
12. Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. *

Star marks a permanent rule. Item 1 is the active Lock guard directive.

## Section 7 . Lifetime And Recent 14 Day KPIs

Lifetime: 685W 548L 36P 155 void . Win rate 55.6% . Units +40.37 . ROI 3.2%
Recent 14 days: 110W 82L 6P 51 void . Win rate 57.3% . Units +9.70 . ROI 4.9%

## Section 8 . Data Notes

Git sync: sparse clone from origin succeeded. PAT was recovered from the git remote URL in .git/config after the workspace mount blocked direct reads of .env (Resource deadlock avoided).
Boxscores: not pulled this run because no picks required settlement.
Schema parse: picks_log read cleanly. Latest dated picks are 2026-06-15.

Open issues requiring attention:
- 30 picks dated 2026-06-15 remain unsettled (outcomes_log ends 2026-06-14). No A tier Locks among them, but lifetime stats are missing these results. A targeted settle of 2026-06-15 is recommended.
- No picks logged for 2026-06-16 or 2026-06-17 despite full slates. The midday pick generation run appears to have stopped producing or committing picks after 2026-06-15. This is the root cause of the empty settlement and should be investigated before tonight.
- The 2026-06-16, 2026-06-17, and 2026-06-18 morning retrospectives did not run; this 2026-06-18 run is the first since the one that settled 2026-06-14.
