# MLB Daily Retrospective Report

Slate date 2026-06-20. Settled 2026-06-21. Generated 2026-06-21T22:12:24Z.

## Section 2 Slate Summary

Yesterday's slate carried 14 games. The model published 23 picks, all from the v1 schema (12 graded B, 11 graded C). No A tier Locks were issued because the Lock guard remained cap active.

Overall record 11 wins, 12 losses, 0 pushes for -2.26 units on the day (ROI -9.8 percent).

Record by market:

- ML: 4 and 6, -2.25 units
- K: 5 and 4, +0.17 units
- Total: 2 and 2, -0.18 units

Record by tier:

- Tier B: 8 and 4, +2.53 units
- Tier C: 3 and 8, -4.79 units

## Section 3 Lock Track Record

Lifetime Locks: 25 wins, 17 losses, 2 pushes, 1 voids across 45 settled picks. Win rate 59.5 percent, +3.09 units, ROI 0.6 percent. Current streak 1 win. Longest win streak 8, longest loss streak 6.

Rolling 14 day Lock win rate 33.3 percent. Rolling 30 day Lock win rate 55.6 percent.

Lock record by market:

- K: 8 and 5 (61.5 percent), +1.42 units
- ML: 4 and 7 (36.4 percent), -4.75 units
- Total: 2 and 2 (50.0 percent), -0.18 units
- F5_ML: 2 and 0 (100.0 percent), +1.50 units
- RL: 3 and 0 (100.0 percent), +3.13 units
- Hits: 1 and 0 (100.0 percent), +0.50 units
- F5: 1 and 1 (50.0 percent), -0.13 units
- Under: 1 and 1 (50.0 percent), -0.09 units
- F5_Total: 2 and 0 (100.0 percent), +1.78 units
- TotalBases: 1 and 0 (100.0 percent), +0.91 units
- Over: 0 and 1 (0.0 percent), -1.00 units

Guard status: cap_active. The rolling 14 day Lock win rate of 33.3 percent sits below the 0.80 floor, so the guard stays cap active. The 11:30 AM run will cap A tier publication until the rolling 14 day Lock rate recovers to 0.85, and will demote any A tier candidate missing four or more of the seven confirmation signals. No Locks were published or lost yesterday.

## Section 4 Top Three Losses With Diagnoses

- Los Angeles Dodgers ML (conf 82, VARIANCE): Los Angeles Dodgers ML missed; final Baltimore Orioles 3 - Los Angeles Dodgers 2.
- Bradley K over 5.5 (conf 66, STARTER_REGRESSION): Bradley K over 5.5 missed; Bradley pulled after 4.0 IP with 9 ER, only 2 K.
- Houston Astros ML (conf 80, VARIANCE): Houston Astros ML missed; final Cleveland Guardians 8 - Houston Astros 1.

## Section 5 Rule Memory Status

Permanent rules (17, never expire):

- [pattern] validated 16 times, last 2026-06-20: Down weight setups exposed to VARIANCE until the pattern clears.
- [pattern] validated 11 times, last 2026-06-18: Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- [pattern] validated 10 times, last 2026-06-14: Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- [pattern] validated 9 times, last 2026-06-20: Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- [pattern] validated 8 times, last 2026-06-20: Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- [pattern] validated 7 times, last 2026-06-14: Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- [pattern] validated 6 times, last 2026-06-14: Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- [pattern] validated 6 times, last 2026-06-20: Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- [lock_breach] validated 4 times, last 2026-06-14: Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- [manual] validated 3 times, last 2026-05-25: Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- [manual] validated 3 times, last 2026-05-25: Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- [manual] validated 3 times, last 2026-05-25: Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- [manual] validated 3 times, last 2026-05-25: Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- [lock_breach] validated 3 times, last 2026-06-14: Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- [lock_breach] validated 3 times, last 2026-06-20: Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- [pattern] validated 3 times, last 2026-06-14: A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.
- [pattern] validated 3 times, last 2026-06-20: K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.

Rules promoted to permanent today (milestones):

- Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.

Trial rules still accumulating evidence (2):

- [lock_breach] 2 of 3, 7 days until expiry: Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- [pattern] 2 of 3, 6 days until expiry: Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two positions so one cold offensive game cannot compound into a three unit MODEL_ERROR loss.

Rules that aged out today: None.

New rules created today: None. Yesterday's losses were dominated by VARIANCE, already covered by standing permanent rules; the two STARTER_REGRESSION K losses validated existing trial and pattern rules rather than spawning new ones.

Total rules in active memory: 17 permanent plus 2 trial.

## Section 6 Adjustments For Today

Full list in priority order. A star marks a permanent rule.

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. *
3. Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B. *
4. Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs. *
5. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
6. Down weight setups exposed to VARIANCE until the pattern clears. *
7. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
8. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
9. Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *
10. Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. *
11. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
12. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *

## Section 7 Lifetime And Recent 14 Day KPIs

Lifetime: 719 and 575 and 37, +42.40 units, win rate 55.6 percent, ROI 0.5 percent.

Recent 14 days: 127 and 102 and 7, +3.78 units, win rate 55.5 percent, ROI 1.6 percent.

Recent 7 days: 34 and 27 and 1, +2.03 units, win rate 55.7 percent, ROI 3.3 percent.

## Section 8 Data Notes

Git sync via sparse clone succeeded; the PAT was read from the local git remote config after the .env hit a mount lock. All 14 box scores were Final. Starter strikeout lines for the nine K props were pulled cleanly from the box scores. One label note: the Gore K prop was attached to the San Diego at Texas game and MacKenzie Gore did start for Texas, so it settled normally (6 K, one short of the 6.5 line). No schema parse warnings; all 23 picks were v1 schema and settled without orphans.
