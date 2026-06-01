# MLB Daily Retrospective — 2026-05-31

No Lock breach. Zero A tier picks were published yesterday under the active Lock guard, so no Lock could miss.

## Section 2 — Slate Summary

Slate date 2026-05-31, 15 games, all Final.

Settled 26 picks plus 4 watch only voids. Record 14W 12L 0P, net +0.18u, win rate 53.8%, ROI 0.7%.

All 30 logged entries came from the 11:30 AM midday run (schema with id field). No v1 or standalone v2 picks were present.

By market:

| Market | Picks | W | L | Win rate | Units |
| --- | --- | --- | --- | --- | --- |
| ML | 19 | 12 | 7 | 63.2% | +3.44 |
| K | 1 | 0 | 1 | 0.0% | -1.00 |
| Total | 2 | 1 | 1 | 50.0% | -0.09 |
| F5_ML | 4 | 1 | 3 | 25.0% | -2.17 |

By tier:

| Tier | Picks | W | L | Win rate | Units |
| --- | --- | --- | --- | --- | --- |
| B | 15 | 7 | 8 | 46.7% | -2.20 |
| C | 11 | 7 | 4 | 63.6% | +2.38 |

## Section 3 — Lock Track Record

Lifetime Locks: 38 settled, 23W 13L 2P, net +5.45u, win rate 63.9%, ROI 1.0%.

Current streak: 5 win. Longest win streak 8, longest loss streak 6.

Rolling 14d Lock win rate 58.6%, rolling 30d 63.9%.

Guard status: cap_active.

The 11:30 AM run will keep A tier publication capped until the rolling 14d Lock win rate recovers to 85 percent. Any A tier candidate missing 4 or more health checks (model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire flag) is demoted.

Lock by market:

| Market | Picks | W | L | Win rate | Units |
| --- | --- | --- | --- | --- | --- |
| ML | 9 | 4 | 5 | 44.4% | -2.75 |
| Under | 2 | 1 | 1 | 50.0% | -0.09 |
| F5 | 2 | 1 | 1 | 50.0% | -0.13 |
| Over | 1 | 0 | 1 | 0.0% | -1.00 |
| F5_Total | 1 | 1 | 0 | 100.0% | +0.91 |
| TotalBases | 1 | 1 | 0 | 100.0% | +0.91 |
| K | 11 | 7 | 4 | 63.6% | +1.65 |
| RL | 3 | 3 | 0 | 100.0% | +3.13 |
| Total | 4 | 2 | 1 | 66.7% | +0.82 |
| F5_ML | 3 | 2 | 0 | 100.0% | +1.50 |
| Hits | 2 | 1 | 0 | 100.0% | +0.50 |

## Section 4 — Top Three Losses

Astros ML -118 to -106 (ML, tier B) — Brewers 2 Astros 0. Category MODEL_ERROR. Model published both Astros ML and Brewers ML on the same game; the Brewers side won and the Astros side lost, a self conflicting output.

Astros F5 ML -120 to -130 (F5_ML, tier B) — Brewers 2 Astros 0. Category MODEL_ERROR. Same self conflicting MIL HOU exposure; Astros were shut out through five as Misiorowski rolled.

Cubs ML -118 to -106 (ML, tier B) — Cubs 1 Cardinals 5. Category STARTER_REGRESSION. Cubs starter was tagged early as St Louis put up two in the first and three in the third, game out of reach.

Note on process: the midday run published both Astros ML and Brewers ML on Milwaukee at Houston, and logged Braves ML twice on Cincinnati across two gamePks. Both are self conflicting or duplicate outputs that should be blocked before publication.

## Section 5 — Rule Memory Status

Permanent rules (6, never expire):

- [manual] validated 3x, first learned 2026-05-20: Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park c

- [manual] validated 3x, first learned 2026-05-20: Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL

- [manual] validated 3x, first learned 2026-05-20: Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 B

- [manual] validated 3x, first learned 2026-05-20: Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless 

- [pattern] validated 5x, first learned 2026-05-28: Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, an

- [pattern] validated 6x, first learned 2026-05-29: Down weight setups exposed to VARIANCE until the pattern clears.

Rules promoted to permanent today: none.

Trial rules accumulating evidence (9):

- [lock_breach] 1 of 3, expires 2026-06-08: Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ER

- [lock_breach] 1 of 3, expires 2026-06-08: Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at le

- [lock_breach] 1 of 3, expires 2026-06-08: Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5

- [lock_breach] 1 of 3, expires 2026-06-08: Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fe

- [lock_breach] 1 of 3, expires 2026-06-08: Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above

- [lock_breach] 1 of 3, expires 2026-06-11: Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeou

- [pattern] 2 of 3, expires 2026-06-07: Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies varianc

- [pattern] 2 of 3, expires 2026-06-07: Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; req

- [pattern] 2 of 3, expires 2026-06-07: Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over th

Rules aged out today: none.

New rules created today: none. Yesterday's VARIANCE and STARTER_REGRESSION patterns matched existing rules, which were revalidated rather than duplicated.

Total active memory: 6 permanent + 9 trial.

## Section 6 — Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.

2. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.

3. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.

4. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.

5. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.

6. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.

7. Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.

8. Down weight setups exposed to VARIANCE until the pattern clears. *

9. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *

10. Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge. *

11. Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met. *

12. Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game. *

(* marks a permanent rule.)

## Section 7 — Lifetime and Recent 14 Day KPIs

Lifetime: 1109 picks, 534W 436L 29P, net +27.03u, win rate 55.0%, ROI 0.3%.

Recent 14 days: 471 picks, 190W 164L, net -3.26u, win rate 53.7%, ROI -0.0%.

## Section 8 — Data Notes

Git sync: origin sparse clone succeeded; picks_log.json pulled from origin (30 picks for the date). A stale prior clone at /tmp/repo_retro was owned by another user and unusable, so a fresh clone directory was used.

Six picks referenced shifted gamePks (824190, 823054, 824513, 823132, 823622, 824431) that did not exist on the official schedule; each was matched to its real game by team matchup and settled against the correct box score.

All 15 box scores and linescores retrieved cleanly. Misiorowski K prop settled from the boxscore pitching line (8 K in 7 innings).

Working folder writes are blocked by the mount deadlock; outputs were built in the origin clone and pushed, and mirrored locally via the file write fallback.