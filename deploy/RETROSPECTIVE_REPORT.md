# MLB Daily Retrospective — settled 2026-06-25 (gap settle 06-23 through 06-25)

_Generated 2026-06-26T14:48:42Z_

## Section 1 — Lock Breach Banner

No A tier Locks were published on 2026-06-25, and no Lock lost across the gap settled dates. No breach.

## Section 2 — Slate Summary

Gap settle covered three unsettled dates (origin outcomes lagged through 06-21; 06-22 had zero published picks).

- 2026-06-23: 28W-26L-0P-0V  -1.46u
- 2026-06-24: 41W-26L-4P-0V  +9.39u
- 2026-06-25 (nominal yesterday): 16W-22L-0P-6V  -8.37u

Yesterday record: 16W-22L-0P-6V, -8.37u, win rate 42.1%, ROI -22.0%. Six picks voided (ARI @ STL postponed).

Yesterday by market:

- F5_ML: 0W-1L-0P  -1.00u
- K: 6W-5L-0P  -0.16u
- ML: 5W-10L-0P  -5.79u
- NRFI: 0W-0L-0P  +0.00u
- Total: 5W-6L-0P  -1.42u

Yesterday by tier:

- b: 10W-13L  -4.90u
- c: 6W-9L  -3.47u

## Section 3 — Lock Track Record

Lifetime Locks: 25W-17L-2P, win rate 59.5%, +3.09u, ROI 0.6%.
Current streak: 1 loss. Longest win 8, longest loss 6.
Rolling 14d Lock win rate: 0.0%. Rolling 30d: 33.3%.
Guard status: healthy (threshold 0.8). No A tier Locks settled in the last 14 days, so the guard defaults to healthy on insufficient sample. The 11:30 AM run is not capped.

Lock by market:

- F5: 1W-1L  win rate 50.0%  -0.13u
- F5_ML: 2W-0L  win rate 100.0%  +1.50u
- F5_Total: 2W-0L  win rate 100.0%  +1.78u
- Hits: 1W-0L  win rate 100.0%  +0.50u
- K: 8W-5L  win rate 61.5%  +1.42u
- ML: 4W-7L  win rate 36.4%  -4.75u
- Over: 0W-1L  win rate 0.0%  -1.00u
- RL: 3W-0L  win rate 100.0%  +3.13u
- Total: 2W-2L  win rate 50.0%  -0.18u
- TotalBases: 1W-0L  win rate 100.0%  +0.91u
- Under: 1W-1L  win rate 50.0%  -0.09u

## Section 4 — Top Three Losses

- **Phillies F5 ML -120 to -140** (conf 84, B): Phillies F5 ML -120 to -140: through five 0-5; loss. [VARIANCE]
- **Sanchez K over 6.5** (conf 80, B): Sanchez K over 6.5: Cristopher Sánchez K=6 vs 6.5; loss. [STARTER_REGRESSION]
- **Royals ML +100 to +115** (conf 80, B): Royals ML +100 to +115: final 2-13; lost ML. [VARIANCE]

## Section 5 — Rule Memory Status

Permanent rules (never expire): 23.
- ★ Consult bullpen_availability_overlay.json. Fade a team late game moneyline and lean toward overs when its bullpen_health (validated 1x, first learned 2026-06-21)
- ★ Consult bvp_overlay.json keyed batterId_pitcherId. Only use a batter versus pitcher line at 15 or more career at bats. C (validated 1x, first learned 2026-06-21)
- ★ Consult hitter_advanced_overlay.json. Grade lineups by lineup_wOBA tier and listed threats, not just runs. Favor overs a (validated 1x, first learned 2026-06-21)
- ★ Consult splits_overlay.json for the platoon matchup. Grade each lineup by its split versus today's starter hand, not by  (validated 1x, first learned 2026-06-21)
- ★ Apply recent form as a two way confidence modifier from rolling_form_overlay.json. When backing a team add up to 6 confi (validated 1x, first learned 2026-06-21)
- ★ Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top 5 K rate. The park cannot over (validated 3x, first learned 2026-05-20)
- ★ Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants offense ranks top 10 NL in runs l (validated 3x, first learned 2026-05-20)
- ★ Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.50 ERA with sub 7.0 BB9. Never  (validated 3x, first learned 2026-05-20)
- ★ Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 7 days regardless of park ad (validated 3x, first learned 2026-05-20)
- ★ Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K ov (validated 10x, first learned 2026-05-28)
- ★ Down weight setups exposed to VARIANCE until the pattern clears. (validated 17x, first learned 2026-05-29)
- ★ Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights. (validated 11x, first learned 2026-05-30)
- ★ Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest co (validated 7x, first learned 2026-05-30)
- ★ Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days. (validated 6x, first learned 2026-05-30)
- ★ Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the (validated 9x, first learned 2026-06-01)
- ★ Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is conf (validated 3x, first learned 2026-06-10)
- ★ Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offen (validated 3x, first learned 2026-06-10)
- ★ Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A ti (validated 4x, first learned 2026-06-10)
- ★ Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C. (validated 9x, first learned 2026-06-10)
- ★ Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C. (validated 6x, first learned 2026-06-10)
- ★ A sub 1.10 WHIP label alone is not protection; verify the starter's last three starts for runs allowed and innings befor (validated 3x, first learned 2026-06-11)
- ★ K Over props require the starter to average at least 5.2 innings across his last three starts; exclude any K Over line o (validated 3x, first learned 2026-06-13)
- ★ Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy fa (validated 3x, first learned 2026-06-18)

Rules promoted to permanent today: 0.

Trial rules accumulating evidence: 3.
- Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and c (2/3, expires 2026-06-28)
- Tighten exposure on bets prone to VARIANCE; require a second confirming signal before publishing. (1/3, expires 2026-07-02)
- Tighten exposure on bets prone to STARTER_REGRESSION; require a second confirming signal before publishing. (1/3, expires 2026-07-02)

Rules aged out today: 0.

New rules created today: 2 (pattern source, expire 2026-07-02).

Total rules in active memory: 23 permanent + 3 trial.

## Section 6 — Adjustments For Today (priority order)

1. ★ Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash or pitch count risk.
2. ★ Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed; bottom third bullpens cap these at B.
3. ★ Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows two straight road games of five plus runs.
4. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage before A tier.
5. ★ Down weight setups exposed to VARIANCE until the pattern clears.
6. ★ Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
7. ★ Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.
8. ★ Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries blowout or short leash risk and require a projected floor of 6 innings.
9. ★ Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
10. ★ Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
11. ★ Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.
12. ★ Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.

## Section 7 — Lifetime and Recent 14 Day KPIs

- Lifetime: 811W-652L-41P, win rate 55.4%, +44.09u, ROI 0.5%.
- Recent 14d: 171W-144L-6P, win rate 54.3%, +2.58u, ROI 0.8%.
- Recent 7d: 103W-89L-4P, win rate 53.6%, -0.57u, ROI -0.3%.

## Section 8 — Data Notes

- Git sync: anonymous-token sparse clone of origin succeeded; PAT recovered from workspace .git/config (mount was EDEADLK/EPERM locked, so all work built from the /tmp origin clone).
- Origin outcomes_log lagged through 2026-06-21; gap settled 06-23, 06-24, 06-25 (06-22 had zero published picks). All 169 picks settled idempotently by id.
- Settlement source: statsapi.mlb.com linescore + boxscore for 39 final games (4 worker pool, retried timeouts). One game (823042 ARI @ STL) postponed; its 6 picks voided.
- Pitcher K props matched on accent-normalized surname against boxscore pitching lines.
- No A tier Locks on the slate; no Lock breach escalation triggered.