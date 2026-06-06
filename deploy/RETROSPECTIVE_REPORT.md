# MLB Daily Retrospective — 2026-06-05

_Settled 31 picks. No A tier Locks were published (Lock guard cap_active), so there is no Lock breach today._

## Section 2 — Slate Summary

Yesterday's slate: 15 games, all Final.

Record: **17 W, 7 L, 0 P, 7 V** | units **+7.95** | win rate **70.8%** | ROI **33.1%**.

Pick schemas: all 31 picks used the v1 string id schema (no v2, no midday). 24 actionable, 7 watch entries voided.

By tier: B 16 W 6 L, C 1 W 1 L.

By market (W-L): ML 4-5, K 1-1, Total 4-0, F5_Total 2-1, RL 1-0, Team Total 1-0, YRFI 2-0, F5_ML 2-0

## Section 3 — Lock Track Record

Lifetime Locks: **23 W, 13 L, 2 P, 1 V** | units **+5.45** | win rate **63.9%** | ROI **14.3%**.

Current streak: **5 win**. Longest win streak 8, longest loss streak 6.

Rolling 14 day Lock win rate: **62.5%** (n=16). Rolling 30 day: **63.9%**.

By market (Locks): Total 2-1 (66.7%), F5_Total 1-0 (100.0%), RL 3-0 (100.0%), K 7-4 (63.6%), F5 1-1 (50.0%), ML 4-5 (44.4%), Under 1-1 (50.0%), Over 0-1 (0.0%), F5_ML 2-0 (100.0%), Hits 1-0 (100.0%), TotalBases 1-0 (100.0%)

**Guard status: cap_active.** Rolling 14 day Lock win rate 62.5% sits below the 0.80 floor, so the cap stays active. The 11:30 AM run will publish no A tier card and will demote any A tier candidate that misses 4 or more of the seven readiness checks until the 14 day rate recovers to 0.85.

## Section 4 — Top Three Losses

1. **Cubs ML -125 to -140** (ML, SF 18, CHC 3) — STARTER_REGRESSION. The Cubs were routed 3 to 18, the platoon and wind edge erased by a starter meltdown.
2. **Blue Jays ML -145 to -160** (ML, BAL 13, TOR 3) — STARTER_REGRESSION. Toronto was buried 3 to 13, the projected best arm Yesavage did not deliver.
3. **F5 Under 4.5** (F5_Total, PIT 3, ATL 6) — VARIANCE. Nine runs crossed in the first five at Truist, the low walk projection busted early.

## Section 5 — Rule Memory Status

Permanent rules (never expire): **10**.
- (pattern, validated 8x, last 2026-06-03) Down weight setups exposed to VARIANCE until the pattern clears.
- (pattern, validated 6x, last 2026-06-02) Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- (pattern, validated 5x, last 2026-06-05) Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- (pattern, validated 4x, last 2026-06-05) Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- (pattern, validated 4x, last 2026-06-05) Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- (manual, validated 3x, last 2026-05-25) Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- (manual, validated 3x, last 2026-05-25) Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- (manual, validated 3x, last 2026-05-25) Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- (manual, validated 3x, last 2026-05-25) Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- (pattern, validated 3x, last 2026-06-01) Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.

Rules promoted to permanent today: **0** — none.

Trial rules still accumulating evidence: **6**.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
- (lock_breach, 1 of 3, expires 2026-06-08) Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
- (lock_breach, 1 of 3, expires 2026-06-11) Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.

Rules that aged out today: **0** — none.

New rules created today: **0** — none. Both of yesterday's loss patterns (VARIANCE and STARTER_REGRESSION) already map to permanent rules, so no duplicates were added.

Total rules in active memory: **10 permanent + 6 trial = 16**.

## Section 6 — Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
6. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
7. Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.
8. Down weight setups exposed to VARIANCE until the pattern clears. *(permanent)*
9. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *(permanent)*
10. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *(permanent)*
11. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *(permanent)*
12. Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *(permanent)*

## Section 7 — Lifetime and Recent 14 Day KPIs

Recent 14 day (all picks): 152 W, 128 L, 4 P | units +1.80 | win rate 54.3% | ROI 0.6%.

Lifetime (all picks): 589 W, 469 L, 30 P | units +40.47 | win rate 55.7% | ROI 3.7%.

## Section 8 — Data Notes

Git sync: sparse clone of origin succeeded (public read). The `.github_pat` and `.env` files were not found in the working folder, so the push uses the token resolved at deploy time. The workspace folder mount returned a Resource deadlock under bash, so all processing ran inside the origin clone at /tmp/repo_retro per the documented mount lock workaround.

Box scores: all 15 finals retrieved. F5, YRFI and F5 ML settled from linescores; Messick (4 K, 5.2 IP) and Woo (7 K, 6.1 IP) settled from full box scores.

Schema notes: 7 conditional Watch entries voided per standard convention. Market keys normalized (F5 to F5_Total, F5 ML to F5_ML). Team Total retained as a distinct market.
