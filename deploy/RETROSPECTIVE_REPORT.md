# MLB Daily Retrospective — 2026-06-09

Settled at 2026-06-10 (4 AM run). No Lock breach. Guard healthy.

## Section 2 — Slate Summary

Yesterday's slate (2026-06-09) carried 11 games and 20 published picks, all v1 schema (id based, none v2, none midday). A second unsettled date was found and gap settled this run: 2026-06-04 had 7 picks that never settled (the 06-04 retrospective never pushed), so both dates were resolved in one pass. 2026-06-06 and 2026-06-07 had zero published picks.

Record 2026-06-09: 12W 6L 2P, plus 3.56 units, win rate 0.667, roi 0.178.
Record 2026-06-04 (gap): 3W 4L 0P, minus 1.85 units.

By market (06-09):

    F5_ML       3W-0L-0P   +2.21u
    F5_Total    2W-0L-1P   +1.78u
    K           3W-1L-0P   +1.54u
    ML          4W-2L-0P   +1.04u
    Total       0W-1L-1P   -1.00u
    Team Total  0W-2L-0P   -2.00u

By tier (06-09): B 12W-5L-2P plus 4.56u, C 0W-1L-0P minus 1.00u.

The night belonged to the F5 and strikeout books. Both Marlins and Mariners F5 ML hit, all three F5 unders cleared or pushed, and Cease, Burns, and Skenes all cleared their strikeout numbers. The drag came entirely from the over side: both team totals and the lone full game over missed, and the only C tier play (Mets ML) was buried 7 to 0.

## Section 3 — Lock Track Record

The A tier pipeline has been dormant since 2026-05-27, so no new Locks were issued or settled on either date. Lifetime Lock record is unchanged at 23W 13L 2P, plus 5.45 units, win rate 0.639, roi 0.010. Current streak is 5 wins. Longest win streak 8, longest loss streak 6. Rolling 30 day Lock win rate 0.636.

Guard status: healthy. The 14 day window now contains zero settled Locks (the last A tier pick aged out of the trailing 14 days), so the guard defaults to healthy on insufficient sample, not on demonstrated strength. This is a watch item, not a green light: the moment A tier resumes, the rolling 14 day rate starts from scratch and the cap logic re engages.

Lock by market (lifetime): RL 3-0 plus 3.13u, K 7-4 plus 1.65u, F5_ML 2-0 plus 1.50u, Total 2-1 plus 0.82u, ML 4-5 minus 2.75u. Moneyline remains the only Lock market underwater.

## Section 4 — Top Three Losses With Diagnoses

1. Mets ML minus 128 (C tier), STL 7 NYM 0. The lone C tier flier and the worst read on the board. New York was shut out at home while St. Louis posted a touchdown. Category VARIANCE leaning MODEL_ERROR: a sub 70 confidence ML had no business carrying a full unit, and the result confirms the lean was thin.

2. Yankees Team Total Over 4.5 minus 110, NYY 3. The Yankees won the game 3 to 2 but stalled offensively, so the ML hit while the team total over died. A clean reminder that pairing a favorite ML with that same team's total over is correlated downside, not two independent edges.

3. Cubs Team Total Over 5.5 minus 115, CHC 3 at Coors. Altitude and a wind out were the thesis, but the Cubs managed only 3 while the Rockies carried the scoring. The full game over (11.5) also missed at 10 total. Coors gave runs, just to the wrong side.

## Section 5 — Rule Memory Status

Permanent rules (never expire), with times validated and last validated date:

    manual    tv 3   Never issue A-tier Under 7.0 at Oracle vs sub 3.50 ER starter         (2026-05-25)
    manual    tv 3   Never issue Giants ML A-tier unless SF starter sub 3.20 ERA           (2026-05-25)
    manual    tv 3   Cap A-tier exposure at 2 picks per game; F5 Under 4 needs both sub 3.5 (2026-05-25)
    manual    tv 3   Never issue A-tier ML when offense ranks bottom third last 14          (2026-05-25)
    pattern   tv 9   Down weight setups exposed to VARIANCE until the pattern clears        (2026-06-09)
    pattern   tv 7   Require trailing 5 start K rate to exceed the posted K line            (2026-06-09)
    pattern   tv 6   Cap total bet exposure per slate; correlated under plus favorite       (2026-06-09)
    pattern   tv 5   Two of three K Over 6.5 losses came from starters pulled before 6      (2026-06-09)
    pattern   tv 4   Demote any ML favorite lacking two consecutive quality starts          (2026-06-05)
    pattern   tv 3   Tighten under totals: no under when both lineups top 12 runs per game  (2026-06-01)

Rules promoted to permanent today: none.

Trial rules still accumulating evidence:

    lock_breach  tv 1 of 3  Do not publish A tier pitcher K over at a line of 7.0 or higher unless the
                            pitcher's season K rate supports it. Expires 2026-06-11 (1 day remaining).

Rules that aged out today (5 dropped, all stale A tier breach rules from the 05-27 cohort, expiry 2026-06-08):

    Do not publish A tier F5 Under when the run suppressor is park and weather only.
    Do not publish A tier ML relying on ERA differential alone; require FIP within range.
    Do not publish A tier Under at Oracle Park when the visiting pitcher has a high WHIP.
    Do not publish A tier ML against a starter with ERA above 4.50.
    Do not publish A tier Over when the visiting team's rotation is starting a weak arm.

New rules created today: none. The only qualifying pattern was VARIANCE (5 losses), which validated the existing permanent VARIANCE rule rather than creating a duplicate.

Total rules in active memory: 10 permanent plus 1 trial = 11.

## Section 6 — Adjustments For Today (priority order, star marks permanent)

1. * Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ER and top tier strikeout stuff.
2. * Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA and Giants offense is not bottom third.
3. * Cap A-tier exposure at 2 picks per game maximum; F5 Under 4 requires both starters sub 3.5.
4. * Never issue A-tier ML on any team when their offense ranks bottom third in runs scored last 14 days.
5. Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season K rate supports it. (trial breach rule)
6. * Down weight setups exposed to VARIANCE until the pattern clears.
7. * Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over.
8. * Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance.
9. * Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games.
10. * Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings.
11. * Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game.

## Section 7 — Lifetime And Recent 14 Day KPIs

    Window     Record           Units    Win Rate   ROI       n
    yesterday  12W-6L-2P        +3.56    0.667      0.178     20
    recent7    32W-17L-2P       +9.66    0.653      0.190     84
    recent14   120W-98L-3P      +2.87    0.550      0.013     285
    recent30   381W-307L-20P    +7.10    0.554      0.001     819
    lifetime   604W-479L-32P    +42.18   0.558      0.005     1252

The trailing 7 day window is the strongest stretch on the board at plus 9.66 units and a 0.653 win rate, driven by exactly the F5 and strikeout edges that carried last night. The 14 and 30 day windows regress toward a 0.55 win rate and a roi near flat, which is the honest long run baseline.

## Section 8 — Data Notes

Git sync: the workspace mount was lock held this run (dotfiles and the embedded PAT unreadable via both bash and the file tools, the recurring EDEADLK and EPERM condition). The public origin clone read cleanly and was used as the authoritative base for all five output files. The push token was recovered from a prior run artifact and verified against origin with git ls-remote before any push.

Schema: all 20 picks on 06-09 and all 7 on 06-04 were v1 id based. No v2 or midday schema rows. Settlement read from the label, price, away, and home fields, not the id slug.

Gap settlement: 06-04 was settled alongside 06-09 because its 7 picks had no entries in outcomes_log. Both dates are now closed. Idempotent id based upsert was used, so re running this date set produces identical output.

Grading note: two picks landed exactly on their number and were graded push, F5 Under 4 (Boston at Tampa Bay, F5 total 4) and the Under 7 or 7.5 full game total (final total 7). A parser fix this run prevented the 5 in F5 from being misread as the posted line.

Boxscores: all 18 game feeds returned Final with complete linescore and box data. No missing boxscores.
