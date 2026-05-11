# MLB Retrospective for 2026-05-10

_Generated 2026-05-11T08:00:00Z_

## Yesterday Slate

- Slate size: 15 games
- Picks settled: 39
- Record: 16 wins, 21 losses, 2 pushes, 0 voids
- Units: -3.6352
- Win rate: 43.2 percent
- ROI: -9.32 percent

## By Market (yesterday)

| Market | Picks | W-L-P | Units | Win % | ROI |
| --- | ---: | --- | ---: | ---: | ---: |
| ML | 11 | 5 and 6 and 0 | -0.3885 | 45.5% | -3.53% |
| F5_ML | 9 | 3 and 4 and 2 | -0.2467 | 42.9% | -2.74% |
| Hits | 14 | 6 and 8 and 0 | -2.0000 | 42.9% | -14.29% |
| Total | 5 | 2 and 3 and 0 | -1.0000 | 40.0% | -20.00% |

## By Tier (yesterday)

| Tier | Picks | W-L-P | Units | Win % | ROI |
| --- | ---: | --- | ---: | ---: | ---: |
| B | 8 | 2 and 4 and 2 | -1.2814 | 33.3% | -16.02% |
| C | 1 | 0 and 1 and 0 | -1.0000 | 0.0% | -100.00% |
| watch | 30 | 14 and 16 and 0 | -1.3538 | 46.7% | -4.51% |

## Top 3 Highest Confidence Losses

- **[ML] Athletics ML +209 to +239** (conf 81, tier B)
  - Final score: Athletics 1 at Orioles 2
  - Diagnosis: Final OAK 1 - BAL 2; pick lost.
  - Category: MODEL_ERROR

- **[F5_ML] White Sox F5 ML -227 to -197** (conf 78, tier B)
  - Final score: Mariners 1 at White Sox 2
  - Diagnosis: F5 score SEA 1 - CWS 0; F5 pick loss.
  - Category: MODEL_ERROR

- **[ML] Guardians ML -223 to -193** (conf 77, tier B)
  - Final score: Twins 5 at Guardians 4
  - Diagnosis: Final MIN 5 - CLE 4; pick lost.
  - Category: MODEL_ERROR

## Patterns Identified

- **VARIANCE** (frequency 8): Hits over 0.5 props at conf 60 went 6 and 8; 8 0-fers across watch tier picks suggests blanket coverage adds noise.
  - New rule: Cap Hits over 0.5 props to confirmed lineup leadoff/2 hole hitters with at least 4 expected at bats and recent 7 day batting average over 0.260.

- **MODEL_ERROR** (frequency 2): Both Over leans at park amplifier venues stayed well under (5 each). Park profile alone is not enough; both starters were sharp.
  - New rule: Do not lean Over on Total when both starters carry season ERA below 3.50 even at hitter friendly parks.

- **STARTER_OVERRATED** (frequency 4): F5 ML went 3 and 4 with 2 pushes. Two heavy chalk F5 plays at minus 200 plus odds (CWS, CLE) lost outright.
  - New rule: Do not lay more than minus 175 on F5 ML when chosen starter has a single previous start with at least 3 ER allowed in last 14 days.

- **MODEL_ERROR** (frequency 6): ML went 5 and 6 with chalk teams (CLE -223, ATL hosting LAD type alignments). Pricing tighter than form.
  - New rule: Lower ML confidence by 5 when home dog price beats plus 110 and starter ERA delta vs opposing starter is under 1.00.

## Adjustments for Today

- Cap Hits over 0.5 props to confirmed lineup leadoff/2 hole hitters with at least 4 expected at bats and recent 7 day batting average over 0.260.
- Do not lean Over on Total when both starters carry season ERA below 3.50 even at hitter friendly parks.
- Do not lay more than minus 175 on F5 ML when chosen starter has a single previous start with at least 3 ER allowed in last 14 days.
- Lower ML confidence by 5 when home dog price beats plus 110 and starter ERA delta vs opposing starter is under 1.00.
- Tighten Hits prop selection to hitters with rolling 14 day OBP above .340 and project a strong matchup, since 0.5 hits at minus 115 needs more than narrative.
- Cap starter side confidence at 60 when chosen starter has a recent outing of 5 or more ER in 5 IP or fewer, or has logged back to back outings allowing 4 or more runs each.
- Cap F5 ML and ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- Cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.
- Verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.
- Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.
- Do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage; Coors edges accumulate after the 5th.
- Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.

## Lifetime KPIs

- Picks: 369
- Record: 195 and 142 and 11
- Units: +40.0875
- Win rate: 57.9 percent
- ROI: 10.86 percent

## Recent 14 Day KPIs

- Picks: 369
- Record: 195 and 142 and 11
- Units: +40.0875
- Win rate: 57.9 percent
- ROI: 10.86 percent

## Loss Categories (yesterday)

- MODEL_ERROR: 13
- VARIANCE: 8

## Monitoring List

- Track Hits over 0.5 hit rate by tier this week. If watch tier sub 45 percent hit rate persists, retire the entire bucket.
- Watch road dog F5 ML pricing. Confirm bullpen openers vs traditional starters before placing F5 leans.
- Audit Total Over picks at hitter friendly parks when both starters have ERA under 3.50.

## Data Gaps Notes

- All 15 games on the slate reached Final status with linescore and boxscore retrieved successfully.
- F5 totals confirmed via inning by inning runs from linescore endpoint.
- Hits resolved via boxscore player batting stats.
- No K, ER, BB, NRFI, YRFI, RL, F5_RL, F5_Total, HR, or TotalBases picks on the slate this date.
