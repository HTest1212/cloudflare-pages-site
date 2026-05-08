# Daily Retrospective — 2026-05-07

asof: 2026-05-08 (idempotent re-run)

## Yesterday's slate

Date: 2026-05-07 (Thursday). Total games on the schedule: 10. All 10 finals.

Final scores:
- TEX 2 @ NYY 9
- MIN 5 @ WSH 7
- CLE 8 @ KC 5
- CIN 3 @ CHC 8
- NYM 2 @ COL 6
- PIT 4 @ ARI 2
- OAK 12 @ PHI 1
- BAL 3 @ MIA 4
- TB 8 @ BOS 4
- STL 2 @ SD 1

## Yesterday's picks: record

52 picks settled.

| Bucket | Picks | W | L | P | V | Units | Win % | ROI |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| All | 52 | 30 | 16 | 2 | 4 | 12.99 | 65.22 | 27.05 |

By market:
- F5_ML: 10 picks, 6 W, 2 L, 2 P, 0 V, +5.08 u, ROI 50.80
- Hits: 10 picks, 5 W, 1 L, 0 P, 4 V, +3.55 u, ROI 59.09
- K: 10 picks, 3 W, 7 L, 0 P, 0 V, -4.50 u, ROI -45.00
- ML: 11 picks, 6 W, 5 L, 0 P, 0 V, +0.26 u, ROI 2.35
- RL: 1 pick, 1 W, 0 L, 0 P, 0 V, +1.42 u, ROI 142.00
- Total: 10 picks, 9 W, 1 L, 0 P, 0 V, +7.18 u, ROI 71.82

By tier:
- B: 18 picks, 12 W, 6 L, +4.56 u, ROI 25.34
- C: 9 picks, 4 W, 5 L, -1.44 u, ROI -15.99
- watch: 25 picks, 14 W, 5 L, 2 P, 4 V, +9.86 u, ROI 46.97

## Top three losses

1. Padres ML at minus 145 to minus 160 (B tier, conf 84). SD lost 2 to 1; the bats never produced against the Cardinals despite the home favorite read. Category VARIANCE.

2. Michael King strikeouts over 6.5 (B tier, conf 84). King went 6.0 IP with 6 K and 1 ER, one short of the line on a usage limited night. Category STARTER_OVERRATED.

3. Max Meyer strikeouts over 6.5 (B tier, conf 80). Meyer pulled at 5.0 IP with 5 K and 2 ER, well short of 6.5. Category STARTER_OVERRATED.

## Patterns identified

1. STARTER_OVERRATED on the K market. The K book went 3 wins and 7 losses for ROI minus 45. Six losses tagged STARTER_OVERRATED. Adjustment rule: cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.

2. STARTER_OVERRATED on F5 ML. Two F5 ML losses where the chosen starter trailed at the 5 inning mark. Rule: cap F5 ML confidence at 60 when the opposing starter has K rate above 25 percent or recent ERA under 3.50.

3. LINEUP_CHANGE void leakage. Four hitter props voided yesterday because the player was not in the lineup or was mapped to the wrong gamePk (Suzuki DNP, Devers absent, Chisholm wrong game, Doyle DNP). Rule: verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.

4. MODEL_ERROR — B tier rebound. B tier ROI 25.34 today (W12 L6). Rule: lift the 5 point B tier confidence haircut once 7 day rolling B tier ROI is back above plus 5 percent.

5. MISSED_NEWS — wrong gamePk mappings on Hits. Devers and Chisholm Hits chips referenced wrong games. Rule: validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.

6. BAD_PARK_READ — Coors F5 visiting team. Coors F5 ML on the visitor lost again as the Rockies bats got going late. Rule: do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage.

## Adjustments for today

1. Cap pitcher K thresholds 0.5 below market average and require projected 6 plus innings AND a recent start with 7 plus Ks before taking K over.
2. Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
3. Verify the picked hitter is on the actual gamePk roster within 90 minutes of first pitch; do not publish Hits chips before lineup confirmation.
4. Lift the 5 point B tier confidence haircut once 7 day rolling B tier ROI is back above plus 5 percent.
5. Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.
6. Do not take F5 ML on the visiting team at Coors when the home pitcher has a track record of escaping the first 5 with limited damage.
7. Cap pitcher K thresholds 0.5 below market average and require 6 plus projected innings before taking K over.
8. Confirm hitter is on active roster within 2 hours of first pitch before publishing Hits chips; haircut confidence by 10 if pulled from projected lineup.
9. Cap starter side confidence at 60 when the most recent start had 5 plus ER in 5 or fewer IP.
10. Add a lineup confirmation gate: publish Hits chips only after the official lineup post hits at first pitch minus 2 hours.

## Lifetime KPIs (settled through 2026-05-07)

| Window | Picks | W | L | P | V | Units | Win % | ROI |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Lifetime | 125 | 60 | 50 | 4 | 11 | 15.25 | 54.55 | 13.38 |
| Recent 14 | 125 | 60 | 50 | 4 | 11 | 15.25 | 54.55 | 13.38 |
| Recent 30 | 125 | 60 | 50 | 4 | 11 | 15.25 | 54.55 | 13.38 |

Recent 14 and 30 day windows currently equal lifetime because only two settled days exist in the ledger (May 6 and May 7); both fall inside both windows. The numbers will diverge naturally as history grows past 14 days.

By market lifetime:
- F5_ML: 25 picks, ROI 22.32
- Hits: 25 picks, ROI 34.97
- K: 24 picks, ROI minus 38.91
- ML: 25 picks, ROI 3.51
- RL: 3 picks, ROI 119.00
- Total: 23 picks, ROI 38.81

By tier lifetime:
- B: 51 picks, ROI 0.55
- C: 18 picks, ROI minus 5.77
- watch: 56 picks, ROI 34.68

## Notes on data state

This is an idempotent re run of the morning retrospective. The earlier run today (asof 07:23:59 UTC) had already settled the May 7 slate. picks_log no longer contains May 7 entries (only May 6 carry over picks remain), so this re run sourced settlements from outcomes_log directly rather than re settling from picks_log. Output content matches the prior run; only timestamps were refreshed. retrospective_history was updated in place rather than appending a duplicate May 7 entry.

No data gaps for the slate itself: all 10 May 7 games reached Final, all 52 picks have a result tag, and all final scores reconcile against the live MLB schedule pulled this run.
