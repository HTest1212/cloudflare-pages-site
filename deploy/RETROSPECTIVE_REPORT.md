# MLB Daily Retrospective — 2026-06-21

Settled 2026-06-22 08:00 UTC. No Lock breach. No A tier picks were published yesterday (Lock guard cap remained active).

## Section 1 — Lock Breach Banner

None. Zero A tier picks were on the board for 2026-06-21, so no Lock could break.

## Section 2 — Slate Summary

Slate date 2026-06-21. 15 games scheduled, 14 Final, 1 postponed (Blue Jays at Cubs, Wrigley, inclement weather, rescheduled to 2026-08-06).

All 10 settled picks landed on a single game: New York Mets at Philadelphia Phillies (Citizens Bank Park), final Phillies 6, Mets 2. Wheeler went 5.2 innings, 7 strikeouts, 2 earned runs, 3 walks, and took the win.

Schema breakdown: v2 0, v1 10, midday 0.

Overall record: 7 wins, 3 losses, 0 pushes. Units +2.13. Win rate 70 percent, ROI 21.3 percent.

By market: ML 2-0, F5_ML 1-0, K 2-0, Team_Total 1-0, Total 1-0, NRFI 0-1, F5_Total 0-1, Outs 0-1.

By tier: B 5-0, C 2-2, watch 0-1.

The card was heavily correlated on the Phillies side. The winners were the straight Phillies bets (moneyline, F5 moneyline, Wheeler strikeouts, team total over, game under 8.5). The three losers were the low scoring side bets that contradicted the same card's own offense read: NRFI and F5 Under both died when Philadelphia put up 5 runs in the first two innings, and the Wheeler outs over 17.5 missed by a single out when he was pulled with two away in the sixth.

## Section 3 — Lock Track Record

Lifetime Locks: 25 wins, 17 losses, 2 pushes, 1 void. Win rate 59.5 percent. Units +3.09. ROI 0.6 percent.

Current streak: 1 loss. Longest win streak 8. Longest loss streak 6.

Rolling 14 day Lock win rate: 33.3 percent (6 settled). Rolling 30 day: 54.5 percent (22 settled).

Lock by market: ML 4-7 for -4.75u is the clear leak, RL 3-0 for +3.13u and F5 markets are carrying the book. K props 8-5.

Guard status: cap_active. Rolling 14 day sits at 33.3 percent, far under the 80 percent floor. The 11:30 AM run will treat the A tier cap as non-negotiable: A tier publication is suspended until the rolling 14 day Lock win rate recovers to 85 percent, and any A tier candidate missing 4 or more of the seven confirmation signals (confidence above 80, recent form positive, lineup confirmed, weather favorable, bullpen rested, no key injury, no umpire flag) is demoted. The ML leak is the priority: the permanent breach rules now block road ML favorites with short starters and Coors ML on opponent ERA alone.

## Section 4 — Top Three Losses With Diagnoses

1. F5 Under 4.5 (C, -100). Seven runs scored through five. MODEL_ERROR. The under directly contradicted the same card's team total over lean on a starter the notes called very hittable. Stacking a first five under with a team total over on the same offense is self defeating.

2. NRFI (C, -125). Philadelphia scored 2 in the bottom first off Peterson. MODEL_ERROR. Same contradiction as above: the card argued Peterson was hittable and the Phillies bats had room, then bet against a first inning run anyway.

3. Wheeler over 17.5 outs (watch, -120). 17 outs, missed by one. VARIANCE. Strong line but pulled with two outs in the sixth. Outs props on starters who get lifted in the sixth stay coin flips and belong on the watch tier, which is where this correctly sat.

## Section 5 — Rule Memory Status

Permanent rules (never expire): 23 in force, including 9 manual or overlay rules and 14 earned pattern and breach rules. Highest conviction: VARIANCE down weight (validated 17), correlated total exposure cap (11), trailing five start strikeout floor (10), K Over six inning requirement (9).

Rules promoted to permanent today: 1 milestone. "Do not publish three correlated positions such as moneyline, a duplicate moneyline and the run line on the same heavy favorite; cap single game exposure at two positions so one cold offensive game cannot compound into a three unit MODEL_ERROR loss." Validated for the third time by yesterday's two MODEL_ERROR losses on the over-stacked Phillies card. This rule is now permanent and is exactly the lesson of yesterday's slate.

Trial rules still accumulating evidence: 1. Coors Over above 11 on wind alone (lock_breach, validated 2 of 3, expires 2026-06-28).

Rules that aged out today: none.

New rules created today: none. The two MODEL_ERROR losses share a category but only reached frequency 2, below the frequency 3 threshold for a fresh pattern rule. The existing correlated positions rule already covers the failure mode and was promoted instead.

Total rules in active memory: 23 permanent plus 1 trial.

## Section 6 — Adjustments For Today (priority order, permanent marked with a star)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14 day Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. * Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in recent starts.
3. * Do not Lock a road ML favorite whose starter projects under seven innings unless the bullpen edge is confirmed.
4. * Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude overrides the matchup.
5. Never Lock a Coors Over above 11 on wind blowing out alone; require both starters to confirm (trial).
6. * Down weight setups exposed to VARIANCE until the pattern clears.
7. * Cap total bet exposure per slate; a cluster of correlated under and favorite plays compounds risk.
8. * Require the pitcher trailing five start strikeout rate to exceed the posted K line floor.
9. * Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; require a tight game script.
10. * Down weight setups exposed to VARIANCE; require an extra confirming signal before publishing.
11. * Demote any ML favorite whose starter lacks two consecutive quality starts in the last five.
12. * Tighten under totals: do not publish an under when both lineups rank top 12 in runs.

## Section 7 — Lifetime And Recent 14 Day KPIs

Lifetime: 726 wins, 578 losses, 37 pushes, 155 voids. Win rate 55.7 percent. Units +44.53. ROI 0.5 percent.

Recent 14 day: 134 wins, 105 losses, 7 pushes, 18 voids. Win rate 56.1 percent. Units +5.91. ROI 2.4 percent.

## Section 8 — Data Notes

Git sync: fresh self owned clone from origin succeeded after the standard /tmp leftover and workspace mount lock were bypassed; the prior repo_retro was owned by another user and a new clone was used for all reads and the push. Working folder .env and picks_log were unreadable through the mount (Resource deadlock avoided), so the origin committed picks_log.json was used as the source of truth.

Boxscores: all 14 Final games pulled cleanly. get_mlb_game_scoring_plays returned an attribute error and was not needed; linescore plus a boxscore subagent supplied every settlement input.

Schema parse: all 10 picks were Schema B (string id, not v2). No parse warnings. Idempotent upsert removed 0 prior 2026-06-21 outcomes (first settlement of this date) and appended 10.
