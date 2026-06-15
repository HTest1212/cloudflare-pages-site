# MLB Daily Retrospective Report
Slate date 2026-06-14. Settled at 2026-06-15T04:39:08Z.

## Section 1 — Lock Breach Banner
No A tier Locks were published yesterday. The Lock Guard remained cap_active through the slate, so the 11:30 AM run did not release any A tier picks. Zero Lock losses to report.

## Section 2 — Slate Summary
Slate date 2026-06-14, 15 scheduled games. One game (Tigers at Guardians, 824424) was postponed and its picks voided.
Pick schema counts: all 41 picks use the current labeled schema (v2 style). Actionable settled: 23. Watch leans logged as void for tracking: 16. Postponed voids: 2.
Overall settled record: 12W 11L 0P, -0.63 units, win rate 52.2 percent, ROI -2.8 percent.

By market (yesterday):
  F5_ML: 1W 0L 0P | win rate 100.0 percent | +0.71u
  K: 3W 3L 0P | win rate 50.0 percent | -0.46u
  ML: 5W 6L 0P | win rate 45.5 percent | -1.66u
  Total: 3W 2L 0P | win rate 60.0 percent | +0.77u

By tier (yesterday):
  B: 9W 9L | win rate 50.0 percent | -1.14u
  C: 3W 2L | win rate 60.0 percent | +0.51u

## Section 3 — Lock Track Record
Lifetime Locks: 25W 17L 2P 1V, win rate 59.5 percent, +3.09 units, ROI 0.6 percent.
Current streak: 1 win. Longest win streak 8, longest loss streak 6.
Rolling 14 day Lock win rate: 33.3 percent. Rolling 30 day: 54.3 percent.

Lock by market:
  F5: 1W 1L | win rate 50.0 percent | -0.13u
  F5_ML: 2W 0L | win rate 100.0 percent | +1.50u
  F5_Total: 2W 0L | win rate 100.0 percent | +1.78u
  Hits: 1W 0L | win rate 100.0 percent | +0.50u
  K: 8W 5L | win rate 61.5 percent | +1.42u
  ML: 4W 7L | win rate 36.4 percent | -4.75u
  Over: 0W 1L | win rate 0.0 percent | -1.00u
  RL: 3W 0L | win rate 100.0 percent | +3.13u
  Total: 2W 2L | win rate 50.0 percent | -0.18u
  TotalBases: 1W 0L | win rate 100.0 percent | +0.91u
  Under: 1W 1L | win rate 50.0 percent | -0.09u

Guard status: cap_active. The rolling 14 day Lock win rate of 33.3 percent sits below the 80 percent floor, so the guard stays active. The 11:30 AM run will continue to cap A tier publication until the rolling 14 day Lock win rate recovers to 85 percent, demoting any A tier candidate that misses four or more confirming signals.

## Section 4 — Top Three Losses With Diagnoses
1. Warren K over 5.5 (K, B, c73) — Warren struck out just 1 over 4 innings, far short of 5.5. Category STARTER_REGRESSION.
2. Seattle Mariners ML -125 to -140 (ML, B, c74) — Hancock was knocked out after 4 innings allowing 6 earned; Mariners lost 1 to 10. Category STARTER_REGRESSION.
3. Hancock K over 5.5 (K, B, c74) — Hancock managed only 2 strikeouts in 4 innings before exiting, well short of 5.5. Category STARTER_REGRESSION.

## Section 5 — Rule Memory Status
Permanent rules (never expire): 15.
  [pattern] validated 13x, first learned 2026-05-29, last validated 2026-06-14: Down weight setups exposed to VARIANCE until the pattern clears.
  [pattern] validated 10x, first learned 2026-05-28, last validated 2026-06-14: Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
  [pattern] validated 10x, first learned 2026-05-30, last validated 2026-06-14: Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
  [pattern] validated 8x, first learned 2026-06-01, last validated 2026-06-14: Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
  [pattern] validated 7x, first learned 2026-05-30, last validated 2026-06-14: Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
  [pattern] validated 6x, first learned 2026-05-30, last validated 2026-06-14: Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
  [pattern] validated 5x, first learned 2026-06-10, last validated 2026-06-14: Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
  [lock_breach] validated 4x, first learned 2026-06-10, last validated 2026-06-14: Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
  [pattern] validated 4x, first learned 2026-06-10, last validated 2026-06-14: Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
  [manual] validated 3x, first learned 2026-05-20, last validated 2026-05-25: Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
  [manual] validated 3x, first learned 2026-05-20, last validated 2026-05-25: Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
  [manual] validated 3x, first learned 2026-05-20, last validated 2026-05-25: Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
  [manual] validated 3x, first learned 2026-05-20, last validated 2026-05-25: Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
  [lock_breach] validated 3x, first learned 2026-06-10, last validated 2026-06-14: Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
  [pattern] validated 3x, first learned 2026-06-11, last validated 2026-06-14: A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.

Rules promoted to permanent today (milestones):
  PROMOTED: Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
  PROMOTED: A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.

Trial rules still accumulating evidence:
  [lock_breach] 2 of 3, expires 2026-06-28: Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
  [lock_breach] 2 of 3, expires 2026-06-28: Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
  [pattern] 2 of 3, expires 2026-06-21: K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.
  [pattern] 1 of 3, expires 2026-06-17: Down weight setups exposed to BAD_PARK_READ; require an extra confirming signal before grading above C.

Rules that aged out today: 0.
New rules created today: 0 (yesterday's loss patterns matched existing rules and were folded in as validations rather than duplicated).
Total rules in active memory: 15 permanent + 4 trial = 19.

## Section 6 — Adjustments For Today (priority order)
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

(* marks a permanent rule.)

## Section 7 — Lifetime And Recent 14 Day KPIs
Lifetime: 685W 548L 36P, win rate 55.6 percent, +40.37 units, ROI 0.5 percent on 8828 units staked.
Recent 14 days: 147W 107L 7P, win rate 57.9 percent, +15.13 units, ROI 5.8 percent.

## Section 8 — Data Notes
Git sync: origin clone succeeded; picks_log pulled from origin. Workspace mount was read locked (EDEADLK), so all computation and writes were performed in the origin clone at /tmp/repo_retro and pushed from there per the established playbook.
Box scores: all 14 played games returned Final box scores and linescores via statsapi. Tigers at Guardians (824424) was postponed to September; its two actionable picks plus two Watch notes were voided.
Schema: all 41 picks parsed under the labeled schema (id, label, price, away, home, market, tier, confidence). No parse warnings.
Pattern category mapping note: pattern carryover rules were validated against yesterday's loss categories by keyword (VARIANCE and STARTER_REGRESSION both present), promoting the road ML favorite breach rule and the sub 1.10 WHIP pattern rule to permanent.