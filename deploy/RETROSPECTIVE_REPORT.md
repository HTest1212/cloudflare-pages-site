# MLB Daily Retrospective Report
Slate date 2026 06 03 . Settled 2026 06 04 08:12 UTC

## Section 2 Slate Summary
Yesterday's slate carried 15 final games. The model logged 27 picks, all from the morning v2 engine, with zero v1 or midday entries.
Overall record 20 wins, 6 losses, 1 push for +9.73 units at a 76.9 percent win rate and 36.0 percent ROI.

Record by market:

- ML: 5W 2L 0P
- F5_ML: 5W 1L 1P
- Total: 5W 2L 0P
- K: 5W 1L 0P

Record by tier: B tier went 18 and 5 with one push, C tier went 2 and 1. No A tier Locks were published yesterday because the Lock guard is active.

## Section 3 Lock Track Record
Lifetime Locks: 23 wins, 13 losses, 2 pushes, 1 void across 39 settled picks. Units +5.45, win rate 63.9 percent, ROI 1.0 percent. Current streak 4 win. Longest win streak 8, longest loss streak 6. Rolling 14 day Lock win rate 61.9 percent, rolling 30 day 63.9 percent.

Lock record by market:

- F5_ML: 2W 0L, win rate 100.0 percent, units +1.50
- TotalBases: 1W 0L, win rate 100.0 percent, units +0.91
- ML: 4W 5L, win rate 44.4 percent, units -2.75
- Hits: 1W 0L, win rate 100.0 percent, units +0.50
- K: 7W 4L, win rate 63.6 percent, units +1.65
- RL: 3W 0L, win rate 100.0 percent, units +3.13
- Total: 2W 1L, win rate 66.7 percent, units +0.82
- F5: 1W 1L, win rate 50.0 percent, units -0.13
- Under: 1W 1L, win rate 50.0 percent, units -0.09
- Over: 0W 1L, win rate 0.0 percent, units -1.00
- F5_Total: 1W 0L, win rate 100.0 percent, units +0.91

Guard status: cap_active. The rolling 14 day Lock win rate of 61.9 percent sits below the 0.80 floor, so the guard is capping A tier publication. The 11:30 AM run will hold the cap and demote any A tier candidate that misses four or more of the seven quality gates until the rolling 14 day Lock win rate recovers to 0.85. No Locks have been published since 2026 05 27, which is why no new Lock data entered the window yesterday.

## Section 4 Top Three Losses With Diagnoses
- Under 6.4 (Total, B tier): Projected sub 6.4 runs but Daikin Park turned into a 20 run slugfest as both staffs were hammered. Category BAD_PARK_READ. Final PIT 9, HOU 11.
- Twins ML (ML, B tier): Twins were shut out 8 to 0 as Bradley gave up 4 earned in 4.2 and Fedde silenced the bats. Category STARTER_REGRESSION. Final CWS 8, MIN 0.
- Twins F5 ML (F5_ML, B tier): Twins trailed 4 to 0 after five, the F5 was gone early behind a leaky start. Category STARTER_REGRESSION. Final CWS 8, MIN 0.

## Section 5 Rule Memory Status
Permanent rules (never expire):

- [8x, last 2026-06-03] Down weight setups exposed to VARIANCE until the pattern clears.
- [6x, last 2026-06-02] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- [4x, last 2026-06-02] Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- [3x, last 2026-05-25] Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- [3x, last 2026-05-25] Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- [3x, last 2026-05-25] Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- [3x, last 2026-05-25] Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- [3x, last 2026-06-03] Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- [3x, last 2026-06-01] Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- [3x, last 2026-06-03] Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.

Rules promoted to permanent today (milestone):

- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.

Trial rules still accumulating evidence:

- [1 of 3, 5 days left, lock_breach] Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
- [1 of 3, 5 days left, lock_breach] Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
- [1 of 3, 5 days left, lock_breach] Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
- [1 of 3, 5 days left, lock_breach] Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
- [1 of 3, 5 days left, lock_breach] Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
- [1 of 3, 8 days left, lock_breach] Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.

Rules that aged out today: none.

New rules created today: none. The three variance losses were already covered by the standing variance downweight rule, and starter regression logged only two losses, one short of a new pattern threshold.

Total rules in active memory: 10 permanent plus 6 trial.

## Section 6 Adjustments For Today
In priority order. Permanent rules marked with a star.

- LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
- Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
- Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
- Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
- Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
- Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
- Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.
- Down weight setups exposed to VARIANCE until the pattern clears. *
- Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
- Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
- Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *

## Section 7 Lifetime And Recent 14 Day KPIs
Lifetime: 572W 462L 30P, units +32.52, win rate 55.3 percent, ROI 0.4 percent across 1168 settled picks.
Recent 14 day: 179W 152L 6P, units -1.69, win rate 54.1 percent.

## Section 8 Data Notes
Git sync via sparse clone of origin succeeded. picks_log.json pulled fresh from main; outcomes were upserted by id so prior entries were preserved. All 15 boxscores and linescores finalized cleanly. Three full boxscores were fetched to disk and parsed for strikeout props (Ohtani 6, Bradley 5, Meyer 7). The workspace mount returned a resource deadlock, so the run executed against the origin clone in temp and pushed from there, consistent with the documented recovery path.