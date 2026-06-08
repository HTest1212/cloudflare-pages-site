# Daily Retrospective — 2026-06-07

Settled at 2026-06-08 (4am run). No Lock breaches. Guard status: WARNING.

## Section 1 — Lock Breach Banner

No Lock lost on 2026-06-07. Zero A tier picks were settled this date, so there is no breach to report. The dedicated Lock guard logic still ran in full.

## Section 2 — Slate Summary

Slate date 2026-06-07. Total games on schedule: 15, all Final.

Pick count by schema: v2 = 0, v1 = 0, midday = 0. Combined published picks for 2026-06-07 = 0.

Overall settled record for the date: 0 wins, 0 losses, 0 pushes, 0 voids. Units 0.00.

No picks were generated or published for this slate even though all 15 games finalized. This is flagged here per protocol as a hard data note (see Section 8). It is not a settlement failure. The picks_log contains no entries dated 2026-06-07, so there was nothing to settle. The same was true for 2026-06-06. The pick pipeline resumed for 2026-06-08 with 26 picks now queued for today's run.

Because the date carried zero picks, there is no record breakdown by market or tier for 2026-06-07.

## Section 3 — Lock Track Record

Lifetime Lock KPIs across all A tier picks:

Record 23 wins, 13 losses, 2 pushes, 1 void over 39 settled Locks. Win rate 0.6389. Units +5.45. ROI 0.0102. Current streak: 5 wins. Longest win streak 8, longest loss streak 6.

Rolling 14 day Lock win rate: 0.8333 (5 wins, 1 loss over 6 Locks). Rolling 30 day Lock win rate: 0.6389.

By market (Locks only):

RL 3 and 0, win rate 1.000, units +3.13. F5_ML 2 and 0, win rate 1.000, units +1.50. K 7 and 4, win rate 0.6364, units +1.65. Total 2 and 1, win rate 0.6667, units +0.82. F5_Total 1 and 0, units +0.91. TotalBases 1 and 0, units +0.91. Hits 1 and 0, units +0.50. ML 4 and 5, win rate 0.4444, units -2.75. F5 1 and 1, units -0.13. Under 1 and 1, units -0.09. Over 0 and 1, units -1.00.

Guard status: WARNING. The rolling 14 day Lock win rate of 0.8333 sits between the 0.80 cap line and the 0.90 healthy line. No hard cap is active. The 11:30 AM run is not forced to demote A tier candidates, but it should treat the warning as a reason to hold the line on quality and avoid stacking correlated Locks. If the next Lock loss drops the 14 day rate below 0.80 the guard will move to cap_active and the cap rule becomes non negotiable.

The guard improved this cycle. The prior run carried cap_active. As older losses rolled out of the 14 day window and recent Locks went 5 of 6, the rolling rate climbed back above 0.80 and the cap lifted to a warning.

## Section 4 — Top Three Losses With Diagnoses

None. Zero picks were settled on 2026-06-07, so there are no losses to diagnose for this date.

## Section 5 — Rule Memory Status

Carryover logic ran in full despite the zero pick day. With no losses to validate against, no trial rules advanced and none were promoted. No rules aged out because every surviving trial rule still sits inside its expiry window.

Permanent rules (never expire), 10 total:

- (manual, validated 3) Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. First learned 2026-05-20.
- (manual, validated 3) Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA and Giants offense ranks top 10 NL in runs last 14 days. First learned 2026-05-20.
- (manual, validated 3) Cap A-tier exposure at 2 picks per game maximum; never stack F5 Under plus ML plus Total all A-tier on the same game. First learned 2026-05-20.
- (manual, validated 3) Never issue A-tier ML when the team ranks bottom third in runs scored last 7 days regardless of park. First learned 2026-05-20.
- (pattern, validated 6) Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over. First learned 2026-05-28.
- (pattern, validated 8) Down weight setups exposed to VARIANCE until the pattern clears. First learned 2026-05-29.
- (pattern, validated 5) Cap total bet exposure per slate; correlated under and favorite clusters amplify variance. First learned 2026-05-30.
- (pattern, validated 4) Demote any ML favorite whose starter lacks two consecutive quality starts in the last three outings. First learned 2026-05-30.
- (pattern, validated 3) Tighten under totals: no under when both lineups rank top 12 in runs per game over the trailing 14 days. First learned 2026-05-30.
- (pattern, validated 4) Avoid K Over chips when the starter carries blowout or short leash risk; require a projected floor of 6 innings. First learned 2026-06-01.

Rules promoted to permanent today: none.

Trial rules still accumulating evidence, 6 total:

- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier F5 Under when the run suppressor is park and weather only; require starter ERA below 3.50 and opposing lineup bottom 5 NL in runs.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier ML on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier ML against a starter with ERA above 4.50 who has allowed 2 or fewer runs in 2 of his last 3 starts.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier Over when the visiting starter has ERA above 6.00 but the bullpen ERA is below 3.80.
- (lock_breach, 1 of 3, expires 2026-06-11) Do not publish A tier pitcher K over at a line of 7.0 or higher unless the season strikeouts per start beats the line by at least 1.5.

Rules that aged out today: none.

New rules created today: none.

Total rules in active memory: 10 permanent plus 6 trial = 16.

## Section 6 — Adjustments For Today (priority order)

No Lock guard cap is active, so the guard rule is not prepended. Order below runs permanent breach style and pattern rules first, then trial rules. Permanent rules are marked with a star.

1. Do not publish A tier F5 Under when the run suppressor is park and weather only; require starter ERA below 3.50 and opposing lineup bottom 5 NL in runs.
2. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and 3 consecutive quality starts.
3. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts.
4. Do not publish A tier ML against a starter with ERA above 4.50 who has allowed 2 or fewer runs in 2 of his last 3 starts.
5. Do not publish A tier Over when the visiting starter has ERA above 6.00 but the bullpen ERA is below 3.80.
6. Do not publish A tier pitcher K over at 7.0 or higher unless season strikeouts per start beats the line by 1.5.
7. * Down weight setups exposed to VARIANCE until the pattern clears.
8. * Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over.
9. * Cap total bet exposure per slate; correlated under and favorite clusters amplify variance.
10. * Demote any ML favorite whose starter lacks two consecutive quality starts in the last three outings.
11. * Avoid K Over chips when the starter carries blowout or short leash risk; require a 6 inning floor.
12. * Tighten under totals: no under when both lineups rank top 12 in runs per game over the trailing 14 days.

## Section 7 — Lifetime and Recent 14 Day KPIs

Lifetime: 589 wins, 469 losses, 30 pushes, 111 voids over 1199 settled picks. Win rate 0.5567. Units +40.47. ROI 0.0046.

Recent 7 day: 51 wins, 28 losses, 1 push, 33 voids. Win rate 0.6456. Units +15.22. ROI 0.1903.

Recent 14 day: 116 wins, 100 losses, 1 push, 53 voids. Win rate 0.5370. Units -1.55. ROI -0.0072.

Recent 30 day: 410 wins, 348 losses, 21 pushes, 90 voids. Win rate 0.5409. Units -3.26. ROI -0.0004.

The recent 7 day window is strong on both win rate and ROI. The 14 and 30 day windows sit near breakeven, dragged by the rough stretch at the start of June that is now rolling out of the shorter windows.

## Section 8 — Data Notes

Git sync: sparse clone from origin succeeded. Latest origin commit at pull was the 1130am 2026-06-08 refresh. picks_log.json was copied from origin into the working folder. The authoritative lifetime outcomes_log.json (1309 entries through 2026-06-05) was used as the settlement base because the local working copy was stale and unparseable; no overnight outcome data was lost since the local copy predated origin.

Zero pick day: picks_log.json contains no entries dated 2026-06-07 (and none for 2026-06-06). All 15 scheduled games finalized. Per protocol this is logged as a hard data note. No settlements were produced and the outcomes log count is unchanged at 1309.

Schema parse: no warnings. All five output files validated as well formed JSON. KPI invariants held in every window (win rate at or below 1.0, absolute ROI below 2.0).

Mount note: direct writes to the working folder hit the known Resource deadlock on the mount. Output files were written to a scratch path, then staged into the origin clone for commit and copied into the working folder through the file tool.
