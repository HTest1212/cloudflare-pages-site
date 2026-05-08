# Daily Retrospective — 2026-05-06
_Generated 2026-05-08T07:11:56Z_
## Slate Summary
Total games on slate: 15
Picks logged: 73
Record: 30 W, 34 L, 2 P, 7 V
Units: +2.27, ROI: +3.54%, Win rate (decided): 46.9%

## By Market
- F5_ML: 6-8-1 (V:0), units +0.50, ROI +3.57%
- Hits: 5-4-0 (V:6), units +1.70, ROI +18.89%
- K: 4-9-0 (V:1), units -4.45, ROI -34.23%
- ML: 6-8-0 (V:0), units +0.62, ROI +4.43%
- RL: 2-0-0 (V:0), units +2.15, ROI +107.50%
- Total: 7-5-1 (V:0), units +1.75, ROI +14.55%

## By Tier
- B: 12-20-1 (V:0), units -4.28, ROI -13.38%
- C: 4-4-0 (V:1), units +0.46, ROI +5.73%
- watch: 14-10-1 (V:6), units +6.09, ROI +25.37%

## Top 3 Losses
- **20260506-824198-K-2** — K | Glasnow K over 7.5 (conf 84, tier B)
  - Final: 12-2
  - Diagnosis: Pulled early after 1.0 IP, 1 ER — couldn't accumulate Ks.
  - Category: **STARTER_REGRESSION**
- **20260506-823550-ML-1** — ML | Yankees ML 160 to 180 (conf 84, tier B)
  - Final: 6-1
  - Diagnosis: Starter regression drove the loss; chosen side outpitched on the day. Final TEX 6 - NYY 1.
  - Category: **STARTER_REGRESSION**
- **20260506-823550-K-2** — K | Warren K over 7.5 (conf 84, tier B)
  - Final: 6-1
  - Diagnosis: Got rocked: 6 ER, 7 K in 4.0 IP, hook came early.
  - Category: **STARTER_REGRESSION**

## Patterns Identified
- **STARTER_OVERRATED** (x9): Pitcher K overs went 4-9 with ROI -34.23%, model overestimated K thresholds across the slate.
  - Rule: Cap pitcher K thresholds 0.5 below market average and require 6+ projected innings before taking K over.
- **MODEL_ERROR** (x20): B tier (high confidence) ROI -13.38% underperformed watch tier (25.37%); confidence calibration is inverted on this slate.
  - Rule: Apply 5 point confidence haircut to B tier picks until 7 day rolling B tier ROI returns to positive.
- **LINEUP_CHANGE** (x6): 6 hitter props voided due to player not in lineup (likely scratched, IL, or roster mismatch).
  - Rule: Confirm hitter is on active roster within 2 hours of first pitch before publishing Hits chips; haircut confidence by 10 if pulled from projected lineup.
- **STARTER_OVERRATED** (x8): F5 ML lost 8 times — chosen starters trailed at the 5 inning mark too often.
  - Rule: Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- **STARTER_REGRESSION** (x8): 8 losses tagged STARTER_REGRESSION, including blowup outings under 5 IP.
  - Rule: Cap starter side confidence at 60 when the most recent start had 5 plus ER in 5 or fewer IP.
- **MISSED_NEWS** (x6): Multiple Hits voids stem from 11:30 AM publish using projected lineups that did not match the actual lineup card.
  - Rule: Add a lineup confirmation gate: publish Hits chips only after the official lineup post hits at first pitch minus 2 hours.

## Adjustments For Today
- Cap pitcher K thresholds 0.5 below market average and require 6+ projected innings before taking K over.
- Apply 5 point confidence haircut to B tier picks until 7 day rolling B tier ROI returns to positive.
- Confirm hitter is on active roster within 2 hours of first pitch before publishing Hits chips; haircut confidence by 10 if pulled from projected lineup.
- Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- Cap starter side confidence at 60 when the most recent start had 5 plus ER in 5 or fewer IP.
- Add a lineup confirmation gate: publish Hits chips only after the official lineup post hits at first pitch minus 2 hours.

## Loss Category Breakdown
- STARTER_OVERRATED: 12
- VARIANCE: 10
- STARTER_REGRESSION: 8
- BAD_PARK_READ: 4

## Lifetime KPIs (single day so far)
- Picks: 73
- Units: +2.27
- ROI: +3.54%
- Win rate: 46.9%

## Notes
- The 2026-05-07 slate had no picks logged in picks_log.json; this retrospective settles 2026-05-06 picks that the previous run missed.
- 6 hitter Hits chips voided due to projected lineup mismatch with the official card.
- Mookie Betts, Lars Nootbaar, Ronald Acuña Jr., Jazz Chisholm Jr., Pete Alonso, and Luis Robert Jr. were all named in picks but did not appear in their team boxscores.
