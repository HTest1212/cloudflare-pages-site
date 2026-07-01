# MLB Daily Retrospective — 2026-06-30

Generated 2026-07-01T14:07:28Z. Settlement window: 2026-06-30 America/New_York slate.

## Section 1 — Lock Breach Banner

No Lock lost yesterday. No breach to report.

## Section 2 — Slate Summary

Yesterday's slate: 2026-06-30, 15 games, all Final.

HARD ERROR: picks_log.json contained zero picks dated 2026-06-30 across all three schemas (v2, v1, midday). The most recent picks in the log are dated 2026-06-28, with gaps on 06-27, 06-29 and 06-30. No 11:30 AM slate was committed for yesterday, so there was nothing to settle. This is the second consecutive empty retrospective (the 06-30 run settling 06-29 was also empty).

Pick count by schema: v2 0, v1 0, midday 0. Yesterday record: 0W 0L 0P 0 voids, 0.00u.

## Section 3 — Lock Track Record

Lifetime Locks: 25W 17L 2P 1 voids across 45 settled picks.
Units +3.0865 on 44u staked. Win rate 59.5%. ROI 7.0%.
Current streak: 1 loss. Longest win streak 8, longest loss streak 6.
Rolling 14d Lock win rate: 0% (fewer than 3 Lock outcomes in the 14 day window, insufficient sample). Rolling 30d: 33.3%.

Lock by market:

- K: 8W 5L, win rate 61.5%, +1.42u, ROI 10.9%
- ML: 4W 7L, win rate 36.4%, -4.75u, ROI -43.2%
- Total: 2W 2L, win rate 50.0%, -0.18u, ROI -3.6%
- RL: 3W 0L, win rate 100.0%, +3.13u, ROI 104.3%
- F5_ML: 2W 0L, win rate 100.0%, +1.50u, ROI 49.9%
- F5_Total: 2W 0L, win rate 100.0%, +1.78u, ROI 88.9%
- F5: 1W 1L, win rate 50.0%, -0.13u, ROI -6.5%
- Under: 1W 1L, win rate 50.0%, -0.09u, ROI -4.5%
- Hits: 1W 0L, win rate 100.0%, +0.50u, ROI 50.0%
- Over: 0W 1L, win rate 0.0%, -1.00u, ROI -100.0%
- TotalBases: 1W 0L, win rate 100.0%, +0.91u, ROI 90.9%

Guard status: healthy. No Lock outcomes have settled since 2026-06-10, so the guard sits on insufficient sample and the 11:30 AM run faces no A tier cap today.

## Section 4 — Top Three Losses With Diagnoses

No losses settled yesterday. Most recent Lock losses on record, for reference:

- 2026-06-10 Dodgers ML -150 to -170 (ML, BULLPEN_FATIGUE): Dodgers ML lost; Ohtani left after 6.2 with the lead but the Los Angeles bullpen surrendered Pittsburgh runs in the seventh and eighth to flip a one run game.
- 2026-06-10 Over 11.5 (Total, BAD_PARK_READ): Coors Over lost; only 5 combined runs scored as both starters held despite the altitude, heat, and wind out thesis.
- 2026-06-10 Cubs ML -125 to -140 (ML, VARIANCE): Cubs ML lost 2 to 3 at Coors; Chicago bats never solved the altitude despite the Lorenzen edge and the model overweighted the opposing starter ERA.

## Section 5 — Rule Memory Status

Permanent rules (never expire): 26.
- [1x, learned 2026-06-21] Consult bullpen_availability_overlay.json. Fade a team late game moneyline and lean toward overs when its bullpen_health is depleted or its closer is unavailabl
- [1x, learned 2026-06-21] Consult bvp_overlay.json keyed batterId_pitcherId. Only use a batter versus pitcher line at 15 or more career at bats. Credit a hitter prop or team lean when a 
- [1x, learned 2026-06-21] Consult hitter_advanced_overlay.json. Grade lineups by lineup_wOBA tier and listed threats, not just runs. Favor overs and fade the opposing starter against an 
- [1x, learned 2026-06-21] Consult splits_overlay.json for the platoon matchup. Grade each lineup by its split versus today's starter hand, not by overall stats. Credit a team in a favora
- [1x, learned 2026-06-21] Apply recent form as a two way confidence modifier from rolling_form_overlay.json. When backing a team add up to 6 confidence points if its form tier is hot or 
- [3x, learned 2026-05-20] Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppression that a
- [3x, learned 2026-05-20] Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice requirement 
- [3x, learned 2026-05-20] Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total all A-tier o
- [3x, learned 2026-05-20] Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: top half r
- [10x, learned 2026-05-28] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is
- [19x, learned 2026-05-29] Down weight setups exposed to VARIANCE until the pattern clears.
- [13x, learned 2026-05-30] Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
- [7x, learned 2026-05-30] Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
- [6x, learned 2026-05-30] Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
- [9x, learned 2026-06-01] Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash 
- [3x, learned 2026-06-10] Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these a
- [3x, learned 2026-06-10] Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
- [4x, learned 2026-06-10] Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five
- [4x, learned 2026-06-10] Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count ris
- [11x, learned 2026-06-10] Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
- [8x, learned 2026-06-10] Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
- [3x, learned 2026-06-11] A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings before publishing any ML, total, or K over bu
- [3x, learned 2026-06-13] K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line of 6.5 or higher when the team is a heavy
- [3x, learned 2026-06-18] Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two 
- [3x, learned 2026-06-25] Tighten exposure on bets prone to VARIANCE; require a second confirming signal before publishing.
- [3x, learned 2026-06-25] Tighten exposure on bets prone to STARTER_REGRESSION; require a second confirming signal before publishing.

Rules promoted to permanent today: none.

Trial rules still accumulating evidence: 0.

Manual rules held in memory: 9.
- Consult bullpen_availability_overlay.json. Fade a team late game moneyline and lean toward overs when its bullpen_health is depleted or its closer is 
- Consult bvp_overlay.json keyed batterId_pitcherId. Only use a batter versus pitcher line at 15 or more career at bats. Credit a hitter prop or team le
- Consult hitter_advanced_overlay.json. Grade lineups by lineup_wOBA tier and listed threats, not just runs. Favor overs and fade the opposing starter a
- Consult splits_overlay.json for the platoon matchup. Grade each lineup by its split versus today's starter hand, not by overall stats. Credit a team i
- Apply recent form as a two way confidence modifier from rolling_form_overlay.json. When backing a team add up to 6 confidence points if its form tier 
- Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot overcome elite SP offense suppress
- Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs last 14 days. Suppress juice re
- Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never stack F5 Under + ML + Total al
- Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park advantage. Minimum requirement: 

Rules that aged out today: none.

New rules created today: none (no losses to learn from).

Total rules in active memory: 26 permanent + 9 trial and manual = 26.

## Section 6 — Adjustments For Today

1. Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs. *
2. Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk. *
3. Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B. *
4. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier. *
5. Down weight setups exposed to VARIANCE until the pattern clears. *
6. Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. *
7. Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. *
8. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average. *
9. Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings. *
10. Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C. *
11. Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation. *
12. Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. *

Rules marked * are permanent.

## Section 7 — Lifetime And Recent 14 Day KPIs

- Lifetime: 852W 681L 43P, +51.44u, win rate 55.6%, ROI 3.3% (1737 settled)
- Recent 30d: 314W 240L 14P, +26.19u, win rate 56.7%, ROI 4.6% (651 settled)
- Recent 14d: 167W 133L 7P, +11.06u, win rate 55.7%, ROI 3.6% (313 settled)
- Recent 7d: 57W 51L 2P, -1.02u, win rate 52.8%, ROI -0.9% (116 settled)

## Section 8 — Data Notes

- Git sync: a stale /tmp/repo_retro clone owned by another user could not be removed, but its files were the current origin HEAD (committed 2026-06-30 18:42) and were used as the authoritative base. Local working folder copies were stale (2026-06-25) and correctly ignored.
- Base files (outcomes_log, learnings, locks_log, retrospective_history) were read from origin, which is strictly newer and more complete than the local working folder.
- HARD ERROR: zero picks logged for 2026-06-30 despite 15 Final games. Pick generation has produced nothing since 2026-06-28. The 11:30 AM slate task should be checked.
- Workspace mount writes returned Resource deadlock (EDEADLK); all outputs were written to the scratch dir and staged for git push, which is the live delivery path via Cloudflare Pages.
- outcomes_log.json unchanged (no new settlements). KPIs recomputed with today's rolling windows. totalStake computed as settled non-void count to avoid the known stake=100 contamination on 77 May 23 rows.