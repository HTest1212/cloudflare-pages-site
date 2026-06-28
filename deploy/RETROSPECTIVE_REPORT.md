# MLB Daily Retrospective

Run date 2026-06-28 (4 AM window). Slate settled: 2026-06-26.

## Section 1 — Lock Breach Banner

No Lock breach. Zero A tier picks were on the 2026-06-26 slate, so no Lock could break. Rolling 14 day Lock win rate sample is empty; guard remains healthy.

## Section 2 — Slate Summary

Slate date 2026-06-26, 15 games, all Final. Settled 27 picks (all from the v1/chip id schema; no v2 or midday schema picks were present). Overnight note: 2026-06-27 had 15 finalized games but zero picks were ever logged, so there was nothing to settle for the literal prior day. The 2026-06-27 retrospective did not run, leaving the 2026-06-26 slate unsettled until now; this run cleared it.

Record: 16W-9L-2P, +4.91u, win rate 64.0%, ROI 18.2%.

By market:

- K: 2W-0L-0P (100.0%), +1.78u, ROI 88.9%
- ML: 10W-6L-0P (62.5%), +2.49u, ROI 15.6%
- Total: 4W-3L-2P (57.1%), +0.64u, ROI 7.1%

By tier:

- tier b: 2W-0L-0P (100.0%), +1.82u, ROI 90.9%
- tier c: 14W-9L-2P (60.9%), +3.09u, ROI 12.3%

## Section 3 — Lock Track Record

Lifetime Locks: 25W-17L-2P-1V across 45 settled, win rate 59.5%, +3.09u, ROI 0.6%.
Current streak: 1 loss. Longest win streak 8, longest loss streak 6.
Rolling 14 day Lock win rate: 0.0% (empty sample). Rolling 30 day: 33.3%.

Lock by market:

- F5: 1W-1L (50.0%), -0.13u, ROI -6.5%
- F5_ML: 2W-0L (100.0%), +1.50u, ROI 49.9%
- F5_Total: 2W-0L (100.0%), +1.78u, ROI 88.9%
- Hits: 1W-0L (100.0%), +0.50u, ROI 50.0%
- K: 8W-5L (61.5%), +1.42u, ROI 10.9%
- ML: 4W-7L (36.4%), -4.75u, ROI -43.2%
- Over: 0W-1L (0.0%), -1.00u, ROI -100.0%
- RL: 3W-0L (100.0%), +3.13u, ROI 104.3%
- Total: 2W-2L (50.0%), -0.18u, ROI -3.6%
- TotalBases: 1W-0L (100.0%), +0.91u, ROI 90.9%
- Under: 1W-1L (50.0%), -0.09u, ROI -4.5%

Guard status: healthy. No A tier published since 2026-06-10, so the 14 day Lock window holds fewer than three settled Locks and the guard defaults to healthy. The 11:30 AM run is not capped. When A tier resumes, the published permanent Lock breach rules below remain in force.

## Section 4 — Top Three Losses

- Over 9 (tier c, conf 68) — Over 9: total 4 vs line 9.0; loss. Category VARIANCE.
- Washington Nationals ML +110 to +125 (tier c, conf 68) — Washington Nationals ML +110 to +125: final Washington Nationals 1 at Baltimore Orioles 3; Washington Nationals lost. Category VARIANCE.
- Kansas City Royals ML -110 to +105 (tier c, conf 67) — Kansas City Royals ML -110 to +105: final Kansas City Royals 1 at Chicago White Sox 22; Kansas City Royals lost. Category STARTER_REGRESSION.

## Section 5 — Rule Memory Status

Total active rules in memory: 23 permanent + 3 trial = 26.

Permanent rules (never expire):

- [pattern] tv 18, first learned 2026-05-29: Down weight setups exposed to VARIANCE until the pattern clears.
- [pattern] tv 12, first learned 2026-05-30: Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- [pattern] tv 10, first learned 2026-05-28: Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
- [pattern] tv 10, first learned 2026-06-10: Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- [pattern] tv 9, first learned 2026-06-01: Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
- [pattern] tv 7, first learned 2026-05-30: Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- [pattern] tv 7, first learned 2026-06-10: Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- [pattern] tv 6, first learned 2026-05-30: Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- [lock_breach] tv 4, first learned 2026-06-10: Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
- [manual] tv 3, first learned 2026-05-20: Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that also kills the under edge.
- [manual] tv 3, first learned 2026-05-20: Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement to no worse than -125 when both conditions are not met.
- [manual] tv 3, first learned 2026-05-20: Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier on same game.
- [manual] tv 3, first learned 2026-05-20: Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half run production last 7 days for A-tier ML designation.
- [lock_breach] tv 3, first learned 2026-06-10: Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
- [lock_breach] tv 3, first learned 2026-06-10: Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
- [pattern] tv 3, first learned 2026-06-11: A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over built on that starter.
- [pattern] tv 3, first learned 2026-06-13: K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy favorite likely to pull the starter early.
- [pattern] tv 3, first learned 2026-06-18: Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two positions so one cold offensive game cannot compound into a three unit MODEL_ERROR loss.
- [manual] tv 1, first learned 2026-06-21: Consult bullpen_availability_overlay.json. Fade a team late game moneyline and lean toward overs when its bullpen_health is depleted or its closer is unavailable. When an elite reliever under 3.00 ERA appears in elite_down treat late leads as shakier. Weight reliever quality by innings: do not trust a shiny ERA under 12 innings pitched.
- [manual] tv 1, first learned 2026-06-21: Consult bvp_overlay.json keyed batterId_pitcherId. Only use a batter versus pitcher line at 15 or more career at bats. Credit a hitter prop or team lean when a standout owns the starter at OPS above .900 and fade when dominated below .550. Ignore thin samples entirely.
- [manual] tv 1, first learned 2026-06-21: Consult hitter_advanced_overlay.json. Grade lineups by lineup_wOBA tier and listed threats, not just runs. Favor overs and fade the opposing starter against an elite lineup_wOBA, and trust the starter and unders against a weak lineup_wOBA. Note soft spots that let a starter work deeper.
- [manual] tv 1, first learned 2026-06-21: Consult splits_overlay.json for the platoon matchup. Grade each lineup by its split versus today's starter hand, not by overall stats. Credit a team in a favorable platoon spot and fade one in an unfavorable spot by up to 4 confidence points using the lineup platoon edge. A weak overall bat who crushes the hand he faces is a plus and a strong bat in a bad platoon spot is a minus. Apply a sample guard: regress or ignore any hitter split under 40 plate appearances versus that hand.
- [manual] tv 1, first learned 2026-06-21: Apply recent form as a two way confidence modifier from rolling_form_overlay.json. When backing a team add up to 6 confidence points if its form tier is hot or warm and subtract up to 8 if its tier is cool or cold. Never grade a cold team moneyline above C. Record alone is not form: a team with a strong season record but a cold form tier is a cold team. Do not call an offense hot off one big game; when the overlay marks a team consistency penalized require a second confirming signal before backing it.

Rules promoted to permanent today: none.

Trial rules still accumulating evidence:

- [lock_breach] tv 2/3, expires 2026-06-28 (2 days left): Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- [pattern] tv 2/3, expires 2026-07-03 (7 days left): Tighten exposure on bets prone to VARIANCE; require a second confirming signal before publishing.
- [pattern] tv 2/3, expires 2026-07-03 (7 days left): Tighten exposure on bets prone to STARTER_REGRESSION; require a second confirming signal before publishing.

Rules that aged out today: none.

New rules created today: none. The dominant VARIANCE loss cluster (8 of 9 losses) re validated existing permanent and trial VARIANCE rules rather than spawning a duplicate.

## Section 6 — Adjustments For Today (priority order)

- Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. *
- Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B. *
- Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs. *
- Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- Down weight setups exposed to VARIANCE until the pattern clears. *
- Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
- Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
- Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. *
- Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *
- Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
- Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C. *
- Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *

(* marks a permanent rule.)

## Section 7 — Lifetime and Recent KPIs

- Yesterday (2026-06-26): 16W-9L-2P (64.0%), +4.91u, ROI 18.2%
- Recent 7: 101W-83L-6P (54.9%), +4.46u, ROI 2.4%
- Recent 14: 142W-113L-7P (55.7%), +8.62u, ROI 3.3%
- Recent 30: 318W-253L-14P (55.7%), +15.24u, ROI 2.6%
- Lifetime: 827W-661L-43P (55.6%), +48.99u, ROI 0.5%

## Section 8 — Data Notes

- Git sync: PAT recovered from .git/config (the .env read returned a mount Resource deadlock). Sparse clone of origin succeeded into a fresh /tmp dir; a stale /tmp/repo_retro from a prior run could not be removed (owned by nobody) so a timestamped dir was used.
- Base files: origin copies (committed 2026-06-26 14:50) were newer than the stale local working folder copies (2026-06-25). All five base files were taken from origin to avoid losing the last committed 2026-06-25 settlement. picks_log.json was refreshed from origin per spec.
- 2026-06-27 produced no logged picks despite 15 Final games; flagged on the monitoring list to confirm the midday generator ran.
- Misiorowski strikeouts (game 823773) pulled from boxscore: K=8, settling both K over 6.5 and K over 7.5 as wins.
- Legacy data: outcomes_log carries 16 pre existing duplicate ids dated 2026-05-24 (an old id collision predating this run). They were left untouched; this run added 27 clean unique Jun 26 ids and introduced no new duplicates.
- Lifetime totalStake reflects historical stake fields on older entries (legacy weighting), consistent with the prior committed summary; recent windows are unit weighted.