# MLB Daily Retrospective — 2026-05-30

Generated 2026-06-01T01:51:47Z

## Section 1 — Lock Breach Banner

No A tier Locks were on yesterday's slate, so there were zero Lock breaches. Guard status is driven by the trailing 14 day Lock window, which sits below target (see Section 3).

## Section 2 — Slate Summary

Slate date 2026-05-30, 15 games, all Final.

Picks settled: 27 (all from the midday B and C schema, no A tier published). Record 11W 16L 0P, -6.90 units, ROI -25.6%.

Record by market:

- F5_Total: 0W 1L, -1.00u
- K: 1W 0L, +0.80u
- ML: 6W 7L, -2.30u
- Team Total: 2W 0L, +1.82u
- Total: 2W 8L, -6.22u

Record by tier: B and C only yesterday. No Locks.

## Section 3 — Lock Track Record

Lifetime Locks: 23W 13L 2P, +5.45 units, win rate 63.9%, ROI 14.3%.
Current streak: 5 win. Longest win streak 8, longest loss streak 6.
Rolling 14d Lock win rate 58.6%; rolling 30d 63.9%.
Guard status: **cap_active** (threshold 14d 80.0%).

Lock by market:
- F5: 1W 1L, win rate 50.0%, -0.13u
- F5_ML: 2W 0L, win rate 100.0%, +1.50u
- F5_Total: 1W 0L, win rate 100.0%, +0.91u
- Hits: 1W 0L, win rate 100.0%, +0.50u
- K: 7W 4L, win rate 63.6%, +1.65u
- ML: 4W 5L, win rate 44.4%, -2.75u
- Over: 0W 1L, win rate 0.0%, -1.00u
- RL: 3W 0L, win rate 100.0%, +3.13u
- Total: 2W 1L, win rate 66.7%, +0.82u
- TotalBases: 1W 0L, win rate 100.0%, +0.91u
- Under: 1W 1L, win rate 50.0%, -0.09u

Because the trailing 14d Lock win rate (58.6%) is under the 80 percent floor, the guard is cap active. The 11:30 AM run will cap A tier publication and demote any A tier candidate missing four or more of the seven quality gates until the rolling 14d Lock win rate recovers to 85 percent.

## Section 4 — Top Three Losses

- Guardians ML -120 to -110 (ML) — Favored side buried early in a 8 run blowout; Boston Red Sox 9, Cleveland Guardians 1. Category STARTER_REGRESSION. Final Boston Red Sox 9 @ Cleveland Guardians 1.
- Under 8 (Total) — Under was badly off as bats erupted for 19 total runs. Category MODEL_ERROR. Final Minnesota Twins 9 @ Pittsburgh Pirates 10.
- F5 Under 4.5 (F5_Total) — Under was badly off as bats erupted for 15 F5 runs. Category MODEL_ERROR. Final Minnesota Twins 9 @ Pittsburgh Pirates 10.

## Section 5 — Rule Memory Status

Permanent rules (never expire): 6.
- [3x, last 2026-05-25] Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot over
- [3x, last 2026-05-25] Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs l
- [3x, last 2026-05-25] Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never 
- [3x, last 2026-05-25] Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park ad
- [5x, last 2026-05-30] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K ov
- [5x, last 2026-05-30] Down weight setups exposed to VARIANCE until the pattern clears.

Rules promoted to permanent today: 0.
Rules that aged out today: 0.
New rules created today: 3 (pattern source, 7 day trial window).
- [1/3, exp 2026-06-08] Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.
- [1/3, exp 2026-06-08] Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 cons
- [1/3, exp 2026-06-08] Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts re
- [1/3, exp 2026-06-08] Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs i
- [1/3, exp 2026-06-08] Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but 
- [1/3, exp 2026-06-11] Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per sta
- [1/3, exp 2026-06-06] Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough
- [1/3, exp 2026-06-06] Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullp
- [1/3, exp 2026-06-06] Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing

Total active rules in memory: 6 permanent + 9 trial.

## Section 6 — Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
6. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
7. Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.
8. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
9. Down weight setups exposed to VARIANCE until the pattern clears. *
10. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
11. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
12. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.

## Section 7 — Lifetime and Recent 14 Day KPIs

Lifetime: 1046 picks, 520W 424L, win rate 55.1%, +26.85u, ROI 0.3%.
Recent 14d: 370 picks, 184W 158L, win rate 53.8%, -2.83u, ROI -0.0%.

## Section 8 — Data Notes

Git sync via sparse clone succeeded; picks_log pulled from origin (workspace mount was EDEADLK locked, so all work ran from the clone). All 15 boxscores and linescores resolved. Weathers K prop confirmed from boxscore (10 K, over 5.5 wins). F5 Under 4.5 graded from linescore (15 first 5 runs). No schema parse warnings.
