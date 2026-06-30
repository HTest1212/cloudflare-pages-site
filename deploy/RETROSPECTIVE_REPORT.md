# MLB Daily Retrospective — 2026-06-29

Generated 2026-06-30 (America/New_York). Settlement window: 2026-06-29 slate, 13 games, all Final.

## SECTION 1 — LOCK BREACH BANNER

No Lock breach. Zero A tier picks were live on the 2026-06-29 slate, so no Lock could break. Rolling 14d Lock win rate remains an empty sample. Guard status: healthy.

## SECTION 2 — SLATE SUMMARY

Slate date 2026-06-29, 13 games, all reached Final.

HARD ERROR: zero picks were logged for 2026-06-29. The picks_log pulled from origin contains no entries dated 2026-06-29 and no entries referencing any of yesterday's 13 gamePks. The most recent committed picks are dated 2026-06-28. This means the 11:30 AM publish or commit step did not land picks for the 2026-06-29 slate. Nothing was settled for yesterday as a result.

Pick count by schema: v2 = 0, v1 = 0, midday = 0. Overall settled record for 2026-06-29: 0 wins, 0 losses, 0 pushes, 0 voids.

Record by market: none (no picks). Record by tier: none (no picks).

Final scores for reference (away at home): White Sox 8 at Orioles 2, Pirates 11 at Phillies 7, Tigers 7 at Yankees 3, Mets 1 at Blue Jays 2, Nationals 3 at Red Sox 6, Rangers 6 at Guardians 3, Reds 3 at Brewers 5, Padres 2 at Cubs 3, Twins 5 at Astros 4, Marlins 10 at Rockies 7, Dodgers 9 at Athletics 4, Angels 2 at Mariners 6, Giants 4 at Diamondbacks 5.

## SECTION 3 — LOCK TRACK RECORD

Lifetime Lock record: 25 wins, 17 losses, 2 pushes, 1 void across 45 settled A tier picks. Win rate 0.5952. Units plus 3.09 on a flat 1u model. ROI 0.0701. Current streak: 1 loss. Longest win streak 8, longest loss streak 6. Rolling 14d Lock win rate: empty sample (no A tier published since 2026-06-10, which now sits outside the 14d window). Rolling 30d Lock win rate: 0.3333 on 6 settled Locks.

Lock by market (settled): ML 4 and 7 (win rate 0.3636, minus 4.75u), K 8 and 5 (0.6154, plus 1.42u), Total 3 and 4 (0.4286, minus 1.27u), RL 3 and 0 (1.000, plus 3.13u), F5_ML 2 and 0 (1.000, plus 1.50u), F5_Total 2 and 0 (1.000, plus 1.78u), F5 1 and 1 (0.500), Hits 1 and 0 (1.000), TotalBases 1 and 0 (1.000). The A tier ML book is the lone negative market and the clear drag on Lock ROI.

Guard status: healthy. Because fewer than three Locks have settled inside the trailing 14 days, the guard defaults to healthy and the 11:30 AM run faces no A tier cap today. The standing permanent Lock rules below still apply as hard filters.

## SECTION 4 — TOP THREE LOSSES WITH DIAGNOSES

No losses occurred on 2026-06-29 because no picks were live. The three most recent Lock losses on record, all from 2026-06-10, are retained for context:

1. Dodgers ML minus 150 to minus 170 — BULLPEN_FATIGUE. Ohtani left after 6.2 with the lead but the Los Angeles bullpen surrendered Pittsburgh runs in the seventh and eighth to flip the game.
2. Coors Over 11.5 — BAD_PARK_READ. Only 5 combined runs scored as both starters held despite the altitude, heat, and wind out thesis.
3. Cubs ML minus 125 to minus 140 — VARIANCE. Lost 2 to 3 at Coors as Chicago bats never solved the altitude and the model overweighted the opposing starter edge.

## SECTION 5 — RULE MEMORY STATUS

Permanent rules (never expire): 26 active, all at times_validated 3 or higher. Highlights include the Coors road ML cap (times_validated 4, last validated 2026-06-28), the K over six innings clearance rule (times_validated 4, last validated 2026-06-14), the VARIANCE down weight pattern (times_validated 19, last validated 2026-06-28), and the correlated exposure cap (times_validated 13, last validated 2026-06-28).

Rules promoted to permanent today: none.

Trial rules still accumulating evidence: none. Every rule in memory has already reached permanent status.

Rules that aged out today: none.

New rules created today: none. No losses were available to validate a rule or seed a new one.

Total rules in active memory: 26 permanent plus 0 trial.

## SECTION 6 — ADJUSTMENTS FOR TODAY

Priority order. All entries are permanent rules (marked with a star). No Lock guard cap is active.

1. * Do not Lock a road ML favorite at Coors on opponent starter ERA alone; altitude variance caps these at B until the offense shows top tier road form.
2. * Do not Lock a K over at 6.5 or higher unless the starter cleared six innings in three of his last four starts; pull A tier on any short leash arm.
3. * Do not Lock a road ML favorite whose starter projects under seven innings unless a rested high leverage reliever is confirmed.
4. * Never Lock a Coors Over above 11 on wind blowing out alone; require both starters at a 5.00 or worse ERA and confirmed heavy bullpen usage.
5. * Down weight setups exposed to VARIANCE until the pattern clears.
6. * Cap total bet exposure per slate; a cluster of correlated under and favorite plays amplifies variance on rough nights.
7. * Down weight setups exposed to VARIANCE; require an extra confirming signal before grading above C.
8. * Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake.
9. * Two of three K Over 6.5 losses came from starters pulled before 6 innings in lopsided games; avoid K Over chips when the starter carries a short leash.
10. * Down weight setups exposed to STARTER_REGRESSION; require an extra confirming signal before grading above C.
11. * Demote any ML favorite whose starter lacks two consecutive quality starts in last three outings; require bullpen rest confirmation.
12. * Tighten under totals: do not publish an under when both lineups rank top 12 in runs per game over the trailing 14 days.

## SECTION 7 — LIFETIME AND RECENT 14 DAY KPIs

All figures on a flat 1u model. The stake field on 77 historical outcomes from 2026-05-23 was contaminated at 100 instead of 1.0, so totalStake is computed as the non void settled count per the schema default; profit values were already on the correct 1u scale and were left untouched.

Lifetime: 852 wins, 681 losses, 43 pushes, 161 voids across 1737 settled picks. Win rate 0.5558. Units plus 51.44. ROI 0.0326.

Recent 30 days: 318 wins, 245 losses, 14 pushes, 84 voids. Win rate 0.5648. Units plus 24.40. ROI 0.0423.

Recent 14 days: 167 wins, 133 losses, 7 pushes, 6 voids. Win rate 0.5567. Units plus 11.06. ROI 0.0360.

Recent 7 days: 98 wins, 77 losses, 6 pushes, 6 voids. Win rate 0.5600. Units plus 8.36. ROI 0.0462.

## SECTION 8 — DATA NOTES

Git sync: sparse clone from origin succeeded. picks_log.json was copied into the working folder. Local outcomes_log.json could not be read because the workspace mount returned Resource deadlock avoided, the known mount lock condition. The origin outcomes_log was used as the authoritative base, deduplicated by id from 1847 to 1831 entries.

Schema parse: picks_log carries all three schemas; none matched yesterday's date or gamePks, confirming the empty slate is a publish gap and not a parse failure.

Box scores: not pulled because there were no picks to settle. All 13 games were confirmed Final from the schedule feed.

Stake field contamination handled as described in Section 7. winRate and roi are stored as decimals. Validation gate passed with zero errors before push.

Action item carried into the monitoring list: investigate why no picks were committed for the 2026-06-29 slate.
