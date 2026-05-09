# MLB Daily Retrospective Report

As of: 2026-05-09T09:35:20Z

## Slate: 2026-05-08 (156 picks across 15 games)

Yesterday: picks 156, W 86 L 63 P 4 V 3, units 16.10, winRate 57.7%, ROI 10.5%

### By market (yesterday)
- **F5_ML**: picks 34, W 13 L 17 P 4 V 0, units -4.94, winRate 43.3%, ROI -14.5%
- **Hits**: picks 30, W 16 L 11 P 0 V 3, units 3.55, winRate 59.3%, ROI 13.1%
- **ML**: picks 48, W 25 L 23 P 0 V 0, units 0.40, winRate 52.1%, ROI 0.8%
- **Total**: picks 44, W 32 L 12 P 0 V 0, units 17.09, winRate 72.7%, ROI 38.8%

### By tier (yesterday)
- **Tier B**: picks 41, W 27 L 14 P 0 V 0, units 10.23, winRate 65.8%, ROI 24.9%
- **Tier C**: picks 5, W 3 L 2 P 0 V 0, units 1.23, winRate 60.0%, ROI 24.6%
- **Tier watch**: picks 110, W 56 L 47 P 4 V 3, units 4.64, winRate 54.4%, ROI 4.3%

## Top losses (highest confidence first)
- `20260508-823466-TOTAL-2` (Total, tier B, conf 84): Under 7.5  ->  Total landed 16, blew through Under 7.5; offense outpaced model.
- `20260508-823957-ML-1` (ML, tier B, conf 84): Braves ML -111 to -91  ->  Braves lost 3 to 1; opposing offense outproduced ours.
- `20260508-823957-ML-W1` (ML, tier watch, conf 84): Braves ML -111 to -91 lean  ->  Braves lost 3 to 1; opposing offense outproduced ours.
- `20260508-824522-F5ML-3` (F5_ML, tier B, conf 84): Reds F5 ML -102 to -72  ->  Reds trailed F5 2 to 0; starter underperformed or opposing starter dominated.
- `20260508-824522-ML-1` (ML, tier B, conf 84): Reds ML -142 to -122  ->  Reds lost 10 to 0; opposing offense outproduced ours.

## Patterns identified
- **STARTER_OVERRATED** (x17): 17 losses tagged STARTER_OVERRATED, concentrated on F5_ML; chosen starters trailed at the F5 mark or fell short of K thresholds.
  - Rule: Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- **STARTER_REGRESSION** (x16): 16 losses tagged STARTER_REGRESSION, mostly on ML where chosen starters got hit harder than projected.
  - Rule: Cap starter side confidence at 60 when the chosen starter has logged a recent outing of 5+ ER in 5 or fewer IP, or when his last two starts allowed 4+ runs each.

## Adjustments for today
- Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- Cap starter side confidence at 60 when the chosen starter has logged a recent outing of 5+ ER in 5 or fewer IP, or when his last two starts allowed 4+ runs each.
- Cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.
- Verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.
- Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.
- Do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage; Coors edges accumulate after the 5th.

## Lifetime KPIs
picks 208, W 116 L 79 P 6 V 7, units 29.08, winRate 59.5%, ROI 14.5%

### Lifetime by market
- **F5_ML**: picks 44, W 19 L 19 P 6 V 0, units 0.14, winRate 50.0%, ROI 0.3%
- **Hits**: picks 40, W 21 L 12 P 0 V 7, units 7.09, winRate 63.6%, ROI 21.5%
- **K**: picks 10, W 3 L 7 P 0 V 0, units -4.50, winRate 30.0%, ROI -45.0%
- **ML**: picks 59, W 31 L 28 P 0 V 0, units 0.66, winRate 52.5%, ROI 1.1%
- **RL**: picks 1, W 1 L 0 P 0 V 0, units 1.42, winRate 100.0%, ROI 142.0%
- **Total**: picks 54, W 41 L 13 P 0 V 0, units 24.27, winRate 75.9%, ROI 45.0%

### Lifetime by tier
- **Tier B**: picks 59, W 39 L 20 P 0 V 0, units 14.79, winRate 66.1%, ROI 25.1%
- **Tier C**: picks 14, W 7 L 7 P 0 V 0, units -0.21, winRate 50.0%, ROI -1.5%
- **Tier watch**: picks 135, W 70 L 52 P 6 V 7, units 14.50, winRate 57.4%, ROI 11.3%

## Recent 14 day KPIs
picks 208, W 116 L 79 P 6 V 7, units 29.08, winRate 59.5%, ROI 14.5%

## Notes on data gaps
- 3 picks voided due to lineup mismatches:
  - `20260508-823957-Hits-watch`: Ronald Acuna Jr. did not appear in the game (likely scratched/IL/wrong roster).
  - `20260508-824443-Hits-W3`: Chase DeLauter did not appear in the game (likely scratched/IL/wrong roster).
  - `20260508-824607-Hits-watch`: Luis Robert Jr. did not appear in the game (likely scratched/IL/wrong roster).

## Settled date list (lifetime)
- 2026-05-07
- 2026-05-08