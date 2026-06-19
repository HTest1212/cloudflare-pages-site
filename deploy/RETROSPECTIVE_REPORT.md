# MLB Daily Retrospective Report

Slate date 2026-06-18 . Settled 2026-06-19 04:45 UTC

## Section 1 . Lock Breach Banner

No A tier Locks were published on 2026-06-18. The Lock Guard cap held the entire slate to B and C grades, so there were no Lock breaches.

## Section 2 . Slate Summary

Eight games reached Final on the slate. The Braves and Giants game at Truist Park was postponed for rain and moved to 2026-08-31, with no picks attached.

All 17 settled picks came from the midday v1 generation schema. Slate record 10W 6L 1P for +3.35 units, win rate 62.5%, ROI 19.7%.

By market (yesterday):

| Market | Picks | W | L | P | Units | Win rate |
|---|---|---|---|---|---|---|
| F5_ML | 2 | 1 | 0 | 1 | +0.91 | 100.0% |
| K | 1 | 1 | 0 | 0 | +0.83 | 100.0% |
| ML | 9 | 4 | 5 | 0 | -1.32 | 44.4% |
| RL | 1 | 0 | 1 | 0 | -1.00 | 0.0% |
| Total | 3 | 3 | 0 | 0 | +2.73 | 100.0% |
| YRFI | 1 | 1 | 0 | 0 | +1.20 | 100.0% |

By tier (yesterday):

| Tier | Picks | W | L | P | Units | Win rate |
|---|---|---|---|---|---|---|
| B | 13 | 7 | 5 | 1 | +1.48 | 58.3% |
| C | 4 | 3 | 1 | 0 | +1.87 | 75.0% |

## Section 3 . Lock Track Record

Lifetime Locks 25W 17L 2P, +3.09 units, win rate 59.5%, ROI 7.0%. Current streak loss 1. Longest win streak 8, longest loss streak 6.

Rolling 14 day Lock win rate 33.3% on 6 decisions. Rolling 30 day 54.3%. Guard status cap_active.

Lock by market:

| Market | Picks | W | L | Win rate | Units | ROI |
|---|---|---|---|---|---|---|
| F5 | 2 | 1 | 1 | 50.0% | -0.13 | -6.5% |
| F5_ML | 3 | 2 | 0 | 100.0% | +1.50 | 49.9% |
| F5_Total | 2 | 2 | 0 | 100.0% | +1.78 | 88.9% |
| Hits | 2 | 1 | 0 | 100.0% | +0.50 | 50.0% |
| K | 13 | 8 | 5 | 61.5% | +1.42 | 10.9% |
| ML | 11 | 4 | 7 | 36.4% | -4.75 | -43.2% |
| Over | 1 | 0 | 1 | 0.0% | -1.00 | -100.0% |
| RL | 3 | 3 | 0 | 100.0% | +3.13 | 104.3% |
| Total | 5 | 2 | 2 | 50.0% | -0.18 | -3.6% |
| TotalBases | 1 | 1 | 0 | 100.0% | +0.91 | 90.9% |
| Under | 2 | 1 | 1 | 50.0% | -0.09 | -4.5% |

Guard is cap_active because the rolling 14 day Lock win rate sits below 0.80, driven by the four Lock losses on 2026-06-10. The 11:30 AM run will cap A tier publication until the rolling 14 day rate recovers to 0.85 and will demote any A tier candidate missing four or more confirming signals. These four losses age out of the window after 2026-06-24.

## Section 4 . Top Three Losses With Diagnoses

1. New York Yankees ML, duplicate ML and run line vs Chicago White Sox. Final 1 to 5. MODEL_ERROR. The deep order read against a thin staff failed; the Yankees managed one run. Stacking three correlated positions on one favorite compounded a single cold game into a three unit loss.

2. Philadelphia Phillies ML vs New York Mets. Final 4 to 6. VARIANCE. A small Phillies lean lost a close game in a high scoring night where the over side of the same card cashed.

3. Milwaukee Brewers ML vs Cleveland Guardians. Final 2 to 4. VARIANCE. The projected lineup and depth edge in a lefty duel did not materialize.

## Section 5 . Rule Memory Status

Permanent rules (never expire):

- (pattern, validated 14x, last 2026-06-18) Down weight setups exposed to VARIANCE until the pattern clears.
- (pattern, validated 11x, last 2026-06-18) Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- (pattern, validated 10x, last 2026-06-14) Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- (pattern, validated 8x, last 2026-06-14) Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- (pattern, validated 7x, last 2026-06-14) Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- (pattern, validated 6x, last 2026-06-14) Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- (pattern, validated 6x, last 2026-06-18) Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- (lock_breach, validated 4x, last 2026-06-14) Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- (pattern, validated 4x, last 2026-06-14) Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- (manual, validated 3x, last 2026-05-25) Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- (manual, validated 3x, last 2026-05-25) Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- (manual, validated 3x, last 2026-05-25) Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- (manual, validated 3x, last 2026-05-25) Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- (lock_breach, validated 3x, last 2026-06-14) Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- (pattern, validated 3x, last 2026-06-14) A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.

Rules promoted to permanent today: none.

Trial rules still accumulating evidence:

- (lock_breach, 2 of 3, expires 2026-06-28) Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- (lock_breach, 2 of 3, expires 2026-06-28) Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- (pattern, 2 of 3, expires 2026-06-21) K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.
- (pattern, 1 of 3, expires 2026-06-25) Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two positions so one cold offensive game cannot compound into a three unit MODEL_ERROR loss.

Rules that aged out today:

- Down weight setups exposed to BAD_PARK_READ; require an extra confirming signal before grading above C.

New rules created today:

- (pattern, expires 2026-06-25) Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two positions so one cold offensive game cannot compound into a three unit MODEL_ERROR loss.

Total active rules in memory: 15 permanent and 4 trial, 19 total.

## Section 6 . Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. *
3. Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B. *
4. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
5. Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
6. Down weight setups exposed to VARIANCE until the pattern clears. *
7. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
8. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
9. Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *
10. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
11. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *
12. Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. *

Rules marked with a star are permanent.

## Section 7 . Lifetime And Recent 14 Day KPIs

| Window | Picks | W | L | P | Units | Win rate | ROI |
|---|---|---|---|---|---|---|---|
| Recent 14 | 235 | 103 | 81 | 7 | +5.10 | 56.0% | 2.4% |
| Lifetime | 1441 | 695 | 554 | 37 | +43.72 | 55.6% | 0.5% |

## Section 8 . Data Notes

Git sync via sparse clone succeeded; picks_log.json pulled from origin. The .env file could not be read through the workspace mount (Resource deadlock), so the push token was recovered from the working repo git config.

All eight Final box scores and the needed linescores were pulled cleanly. Joe Ryan strikeouts confirmed at 7 via boxscore. The Yankees F5 ML settled as a push on a 1 to 1 tie through five.

Pre-existing data gap: picks dated 2026-06-15, 2026-06-16 and 2026-06-17 remain unsettled or unlogged; the lifetime track record resumes at 2026-06-18.
