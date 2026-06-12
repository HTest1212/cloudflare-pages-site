# DAILY RETROSPECTIVE — 2026-06-11
Generated 2026-06-12 by the 4 AM retrospective.

## SECTION 2 — SLATE SUMMARY
Slate date 2026-06-11, 8 scheduled games, 7 played to Final, 1 postponed by rain (Braves at White Sox, no picks attached). All 10 picks came from the overnight v3 card schema (label, price, tier fields); zero v2, zero v1, zero midday schema picks. Every pick gamePk verified against the official 06-11 schedule, no stale slate duplicates, no voids.

Overall record: 4W 6L 0P, minus 2.72 units on 10 staked.

By market: F5 ML 1W 1L. ML 1W 2L. K 1W 1L. Total 0W 1L. TeamTotal 1W 0L. YRFI 0W 1L.
By tier: B 3W 3L (minus 0.49u). C 1W 3L (minus 2.23u).

## SECTION 3 — LOCK TRACK RECORD
No A tier Locks were published on the 06-11 slate, so the Lock book did not move.

Lifetime: 45 settled, 25W 17L 2P 1V, plus 3.09 units, 59.5 percent win rate, 7.2 percent ROI.
Current streak: loss 1. Longest win streak 8, longest loss streak 4.
Rolling 14 day win rate: 33.3 percent (2W 4L). Rolling 30 day: 55.6 percent.

Guard status: CAP ACTIVE. The 11:30 AM run must treat the A tier cap as non negotiable: demote any A tier candidate missing 4 or more of model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag. The cap lifts when rolling 14 day recovers to 0.85.

## SECTION 4 — TOP THREE LOSSES WITH DIAGNOSES
1. Mariners ML minus 110 (B 76). Woo was charged seven earned runs in five innings and the 1.00 WHIP edge evaporated against Baltimore. STARTER_REGRESSION. This also sank the correlated Woo K Over 5.5 (4 strikeouts).
2. Twins ML minus 105 (B 74). Minnesota was shut out while Detroit hung eleven runs; the comparable starters read collapsed on both sides, and the correlated Under 8 died with it. STARTER_REGRESSION.
3. Royals F5 ML minus 110 (C 67). Wacha trailed three to nothing through three innings; the command and length thesis failed immediately. STARTER_OVERRATED.

The slate pattern is unmistakable: four of six losses came from trusting a low WHIP label without a recent form check, and the damage was doubled by stacking two picks on the same starter in two games.

## SECTION 5 — RULE MEMORY STATUS
Permanent rules (never expire), 10 total:
- 4 manual A tier guardrails, times validated 3, learned 2026-05-25 (Oracle unders, Giants ML, A tier game stacking cap, bottom third offense ML ban).
- Down weight setups exposed to VARIANCE until the pattern clears — times validated 10, validated again today.
- Require trailing 5 start strikeout rate to exceed the posted K line — times validated 8, validated again today.
- Cap total bet exposure per slate, correlated unders and favorites amplify variance — times validated 7, validated again today.
- Two of three K Over 6.5 losses came from starters pulled early in lopsided games — times validated 6, validated again today (Woo, 5 innings, lopsided).
- Demote ML favorites lacking two consecutive quality starts — times validated 5, validated again today.
- Tighten under totals when both lineups rank top 12 — times validated 4, validated today.

Rules promoted to permanent today: none.

Trial rules still accumulating evidence, 9 total:
- Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts — 2 of 3, validated today, expires 2026-06-25.
- Do not publish A tier K over at 7.0 plus without 1.5 strikeouts of cushion — 1 of 3, expires 2026-06-11 (final day, ages out tomorrow).
- Three Lock breach rules from 06-10 (road ML favorite bullpen rule, Coors Over rule, Coors road ML rule) — each 1 of 3, expire 2026-06-24.
- Down weight VARIANCE setups, require extra signal above C — 2 of 3, validated today, expires 2026-06-18.
- Down weight STARTER_REGRESSION setups, require extra signal above C — 2 of 3, validated today, expires 2026-06-18.
- Down weight BAD_PARK_READ setups — 1 of 3, expires 2026-06-17.
- NEW: A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter — 1 of 3, expires 2026-06-18.

Rules that aged out today: none.
New rules created today: 1 (the sub 1.10 WHIP form check rule, source pattern).
Total rules in active memory: 10 permanent + 9 trial.

## SECTION 6 — ADJUSTMENTS FOR TODAY (priority order, capped at 12)
1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. * Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate.
3. * Never issue Giants ML as A-tier unless SF starter has sub 3.20 ERA and the offense ranks top 10 NL last 14 days.
4. * Cap A-tier exposure at 2 picks per game maximum; never stack F5 Under plus ML plus Total on one game.
5. * Never issue A-tier ML on a team with bottom third run production last 7 days.
6. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts (2 of 3).
7. Do not publish A tier K over at 7.0 plus without 1.5 strikeouts per start of cushion (1 of 3, expiring).
8. Do not Lock a road ML favorite whose starter projects under seven innings without a rested high leverage reliever (1 of 3).
9. Never Lock a Coors Over above 11 on wind alone (1 of 3).
10. Do not Lock a road ML favorite at Coors on opponent starter ERA alone (1 of 3).
11. * Down weight setups exposed to VARIANCE until the pattern clears (validated 10 times).
12. * Require the trailing 5 start strikeout rate to exceed the posted K line before publishing a K over; cap stake at half a unit above season average.

Starred rules are permanent. The new WHIP form check rule and remaining trial pattern rules live in carryover memory but fell below the 12 rule cap.

## SECTION 7 — LIFETIME AND RECENT 14 DAY KPIs
Lifetime: 1301 settled picks, 626W 503L 35P 137V, 55.4 percent win rate where decided, plus 35.84 units, plus 0.4 percent ROI.
Recent 14 days: 282 settled, 117W 95L 6P 64V, 55.2 percent win rate, plus 2.09 units, plus 1.0 percent ROI. Full market and tier breakdowns live in bet_record_summary.json windows.recent14.
Yesterday: 10 picks, 4W 6L, 40.0 percent, minus 2.72 units, minus 27.2 percent ROI.

## SECTION 8 — DATA NOTES
Git sync: origin sparse clone succeeded on a fresh path (/tmp dirs from prior runs persist read only; the run clones to a timestamped directory). picks_log.json pulled from origin; outcomes_log.json and locks_log.json deliberately never copied from origin.
Workspace mount: all six output JSON files in the local working folder are deadlocked (EDEADLK in sandbox, EPERM via host file tools), the known mount lock condition. The run therefore built every output from the origin clone, which was verified current through 2026-06-10, and pushed directly. Local working folder copies could not be refreshed this run; the repo and live dashboard are authoritative.
Boxscore MCP: passing a fields filter to get_mlb_boxscore breaks its pydantic validation (701 errors); full payload calls work. Starter lines for Woo and Christian Scott were extracted via subagent and cross verified against statsapi.
All 7 played games had complete linescores and boxscores. One game postponed (824589, rescheduled 2026-08-20), no picks affected.
