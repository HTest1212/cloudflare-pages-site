# MLB Daily Retrospective — 2026-06-13

Settled 2026-06-14 (4 AM run). No Lock breach: zero A tier picks were published for 2026-06-13.

## Section 2 — Slate Summary

Slate date 2026-06-13, 15 games, all Final. All 63 logged picks used the v1 string id schema (no v2 ids, no midday no id picks present for this date). Overall record 33 wins, 29 losses, 1 push, for negative 0.50 units on a coin flip slate.

The story of the night was a market split. Totals carried the card while strikeout props collapsed.

Record by market:

- Total: 14 and 4, plus 8.97 units, win rate 0.778
- K (pitcher strikeouts): 5 and 13, minus 8.85 units, win rate 0.278
- ML: 10 and 10, minus 1.99 units, win rate 0.500
- F5 Total: 1 and 2 with 1 push, minus 1.11 units
- F5 ML: 1 and 0, plus 0.77 units
- YRFI: 2 and 0, plus 1.70 units

Record by tier:

- B tier: 13 and 13 with 1 push, minus 2.53 units
- C tier: 20 and 16, plus 2.03 units

## Section 3 — Lock Track Record

No A tier picks settled for 2026-06-13, so the lifetime Lock ledger is unchanged from the prior run.

Lifetime Locks: 45 picks, 25 wins, 17 losses, 2 pushes, 1 void. Win rate 0.595, plus 3.09 units, ROI 0.006. Current streak: 1 loss. Longest win streak 8, longest loss streak 6. Rolling 14 day Lock win rate 0.333 (6 settled Locks in window). Rolling 30 day Lock win rate 0.543.

Lock record by market: RL 3 and 0, F5 ML 2 and 0, Hits 1 and 0, TotalBases 1 and 0, F5 Total 3 and 1, K 8 and 5, Total 3 and 4, ML 4 and 7.

Guard status: cap_active. The rolling 14 day Lock win rate sits at 0.333, well under the 0.80 floor. The 11:30 AM run will enforce the Lock guard: A tier publication is capped until the rolling 14 day Lock win rate recovers to 0.85, and any A tier candidate missing four or more of the seven confirming signals (model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag) is demoted. The ML and Total Lock markets are the soft spots driving the cap.

## Section 4 — Top Three Losses With Diagnoses

1. Tigers ML (confidence 84, B tier). Detroit lost 1 to 3 at Cleveland. Skubal gave Detroit a real edge on paper but the Tigers bats produced a single run. Category VARIANCE: a coin flip favorite that did not convert.

2. Skubal K over 6.5 (confidence 84, B tier). Skubal struck out only 4 over 4.2 innings and was pulled early in a tight game. Category STARTER_REGRESSION. This is the exact failure mode the K Over guard targets, a high line attached to a starter who never reached the sixth.

3. deGrom K over 7 (confidence 80, B tier). deGrom went a clean 6 innings but recorded just 5 strikeouts against Boston. Category VARIANCE: full outing, low whiff total, line set too high relative to realized swing and miss.

Honest read: the strikeout book was the single point of failure. Five wins against thirteen losses on K props erased what Totals earned. Four of the K losers (Skubal, Cameron, Nola, Bachar) were pulled before completing five innings, confirming the short leash risk the rule memory already flags.

## Section 5 — Rule Memory Status

Total active rules in memory: 13 permanent and 6 trial, 19 in all.

Rules promoted to permanent today (milestones):

- Lock breach: "Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk." Validated to 3 by today's Skubal and deGrom K Over losses.
- Pattern: "Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C." Validated to 3 by today's short start cluster.

Permanent rules (never expire), with times validated:

- Down weight setups exposed to VARIANCE until the pattern clears (12)
- Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over (9)
- Cap total bet exposure per slate; correlated under and favorite plays amplify variance (9)
- Two of three K Over 6.5 losses came from starters pulled before 6 innings; avoid K Over chips on short leash arms (7)
- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings (6)
- Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game (5)
- Do not Lock a K over at 6.5 or higher unless the starter cleared six in three of last four (3, promoted today)
- Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal (3, promoted today)
- Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C (3)
- Four manual A tier guardrails (Oracle under, Giants ML, A tier cap 2 per game, ML bottom third offense), each at 3

Trial rules still accumulating evidence:

- Do not Lock a road ML favorite whose starter projects under seven innings (2 of 3, validated today, expires 2026-06-27)
- Do not Lock a K over without a sub 1.10 WHIP and confirmed recent form (2 of 3, validated today, expires 2026-06-20)
- Never Lock a Coors Over above 11 on wind alone (1 of 3, expires 2026-06-24)
- Do not Lock a road ML favorite at Coors on opponent starter ERA alone (1 of 3, expires 2026-06-24)
- Down weight setups exposed to BAD_PARK_READ; require an extra confirming signal (1 of 3, expires 2026-06-17)
- K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early (new today, 1 of 3, expires 2026-06-20)

Rules that aged out today: none.

New rules created today: 1 (the K Over innings and favorite filter above, source pattern).

## Section 6 — Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: cap A tier publication until rolling 14d Lock win rate recovers to 0.85; demote any A tier candidate missing 4 or more of the seven confirming signals.
2. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. (star, permanent)
3. Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed.
4. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA.
5. Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B.
6. Down weight setups exposed to VARIANCE until the pattern clears. (star, permanent)
7. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over. (star, permanent)
8. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance. (star, permanent)
9. Two of three K Over 6.5 losses came from starters pulled before 6 innings; avoid K Over chips on short leash arms. (star, permanent)
10. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings. (star, permanent)
11. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game. (star, permanent)
12. Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. (star, permanent)

The newly generated K Over filter and the remaining trial rules sit below the 12 rule cap and remain in persistent memory for tomorrow.

## Section 7 — Lifetime And Recent 14 Day KPIs

Recent 14 day: 307 settled picks, 139 wins, 101 losses, 7 pushes, 60 voids, plus 13.98 units, win rate 0.579, ROI 0.057.

Recent 30 day: 721 settled picks, 343 wins, 279 losses, plus 8.15 units, win rate 0.551, ROI 0.001.

Lifetime: 1383 settled picks, 673 wins, 537 losses, 36 pushes, plus 41.01 units, win rate 0.556, ROI 0.005.

## Section 8 — Data Notes

Git sync: sparse clone of origin succeeded; the standard /tmp/repo_retro path was blocked by a stale clone owned by another user and by mount lock errors, so the working clone was built under the session home directory instead. All settlement was computed against this fresh origin pull.

Box scores and line scores: all 15 games returned Final cleanly. Starter strikeout lines were extracted by subagents from full box scores (no fields parameter passed). No openers were detected; every named starting pitcher was the actual game starter. The Miami starter was confirmed as Lake Bachar (a short 2.0 inning outing, not an opener per gamesStarted).

Settlement edge cases: F5 Under 4 at Fenway (Rangers at Red Sox) finished exactly 4 runs through five and settled as a push. F5 line parsing was corrected to ignore the numeral inside the token "F5".

Carryover matching: lock breach rules were validated against today's losses by market and category. The K Over 6.5 lock breach rule matched today's K market STARTER_REGRESSION losses and the road ML favorite rule matched today's ML VARIANCE losses. Coors specific rules did not match (no Coors game on the slate). Pattern rules were validated by loss category. These inference choices are noted for transparency since carryover entries store rule text and source rather than structured market and category fields.
