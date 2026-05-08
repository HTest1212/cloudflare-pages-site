# Daily Retrospective Report  2026 05 07

Generated: 2026-05-08T07:24:34Z

## Slate Summary

Yesterday slate date: 2026-05-07. Total games settled: 10.

Pick count: 52. Record: 30 W, 16 L, 2 P, 4 V. Units: +12.99. Win rate: 65.22%. ROI: 27.05%.

## By Market

| Market | Picks | W | L | P | V | Units | Win % | ROI |
|--------|------:|--:|--:|--:|--:|------:|------:|----:|
| F5_ML | 10 | 6 | 2 | 2 | 0 | +5.08 | 75.0% | 50.8% |
| Hits | 10 | 5 | 1 | 0 | 4 | +3.55 | 83.33% | 59.09% |
| K | 10 | 3 | 7 | 0 | 0 | -4.50 | 30.0% | -45.0% |
| ML | 11 | 6 | 5 | 0 | 0 | +0.26 | 54.55% | 2.35% |
| RL | 1 | 1 | 0 | 0 | 0 | +1.42 | 100.0% | 142.0% |
| Total | 10 | 9 | 1 | 0 | 0 | +7.18 | 90.0% | 71.82% |

## By Tier

| Tier | Picks | W | L | P | V | Units | Win % | ROI |
|------|------:|--:|--:|--:|--:|------:|------:|----:|
| B | 18 | 12 | 6 | 0 | 0 | +4.56 | 66.67% | 25.34% |
| C | 9 | 4 | 5 | 0 | 0 | -1.44 | 44.44% | -15.99% |
| watch | 25 | 14 | 5 | 2 | 4 | +9.86 | 73.68% | 46.97% |

## Loss Categories

- VARIANCE: 7
- STARTER_OVERRATED: 7
- STARTER_REGRESSION: 2

## Top 3 Losses

### 1. 20260507-823306-ML-1 . ML . Padres ML minus 145 to minus 160

Tier B, confidence 84. Final score: away 2, home 1. Result: loss, profit -1.00u.

Diagnosis: SD lost 2-1; offense did not produce as projected.

Category: VARIANCE.

### 2. 20260507-823306-K-3 . K . King K over 6.5

Tier B, confidence 84. Final score: away 2, home 1. Result: loss, profit -1.00u.

Diagnosis: Michael King: 6.0 IP, 6 K, 1 ER (line over 6.5).

Category: STARTER_OVERRATED.

### 3. 20260507-823870-K-3 . K . Meyer K over 6.5

Tier B, confidence 80. Final score: away 3, home 4. Result: loss, profit -1.00u.

Diagnosis: Max Meyer: 5.0 IP, 5 K, 2 ER (line over 6.5).

Category: STARTER_OVERRATED.

## Patterns Identified

### STARTER_OVERRATED . frequency 6

K market went 3-7 ROI -45.0%; chosen starters fell short of K thresholds 6 times. Pattern continues from yesterday.

Rule: Cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.

### STARTER_OVERRATED . frequency 2

F5 ML lost 2 times; chosen starters trailed at the 5 inning mark.

Rule: Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.

### LINEUP_CHANGE . frequency 4

4 hitter props voided due to player not in lineup or assigned to the wrong gamePk (Suzuki DNP, Devers absent, Chisholm wrong game, Doyle DNP).

Rule: Verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.

### MODEL_ERROR . frequency 18

B tier ROI rebounded to 25.34% (W12 L6); confidence calibration looks healthier today.

Rule: Lift the 5 point B tier confidence haircut once 7 day rolling B tier ROI is back above plus 5 percent (today's B tier delivered).

### MISSED_NEWS . frequency 2

Hits chips referenced players not on the gamePk roster (Devers, Chisholm). Pick generation is mapping the wrong batter to the wrong game.

Rule: Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.

### BAD_PARK_READ . frequency 1

Coors F5 ML lost again; cold weather Coors model kept undershooting how late the home offense lights up.

Rule: Do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage; Coors edges accumulate after the 5th.

## Adjustments for Today (the 11:30 AM run will apply these)

- Cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.
- Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- Verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.
- Lift the 5 point B tier confidence haircut once 7 day rolling B tier ROI is back above plus 5 percent (today's B tier delivered).
- Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.
- Do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage; Coors edges accumulate after the 5th.
- Cap pitcher K thresholds 0.5 below market average and require 6+ projected innings before taking K over.
- Confirm hitter is on active roster within 2 hours of first pitch before publishing Hits chips; haircut confidence by 10 if pulled from projected lineup.
- Cap starter side confidence at 60 when the most recent start had 5 plus ER in 5 or fewer IP.
- Add a lineup confirmation gate: publish Hits chips only after the official lineup post hits at first pitch minus 2 hours.

## Monitoring List

- K market: today 3 wins, 7 losses (-45.0% ROI). Trend after two days of overrated K props is stabilizing; track 3 more days before lifting the confidence haircut.
- Hitter Hits voids: 4 today (Suzuki, Devers, Chisholm, Doyle). Pre publish lineup gate is still leaking.
- Coors F5 ML on visiting team: lost again. Reconsider F5 ML edges at Coors specifically.

## Lifetime KPIs

Picks 125, wins 60, losses 50, pushes 4, voids 11. Units +15.25. Win rate 54.55%. ROI 13.38%.

## Recent 14 Day KPIs

Picks 125, wins 60, losses 50. Units +15.25. ROI 13.38%.

## Data Gaps and Notes

- 4 voids logged: 2 LINEUP_CHANGE (Seiya Suzuki and Brenton Doyle did not bat), 2 MISSED_NEWS (Devers and Chisholm Hits chips referenced players not on the actual gamePk roster).
- 2 F5 ML pushes logged where the F5 score was tied (STL/SD 1-1 and TB/BOS 3-3).
- All 10 games reached Final status; no postponements or live games on yesterday's slate.
