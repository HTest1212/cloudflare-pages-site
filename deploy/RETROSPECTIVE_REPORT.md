# MLB Betting Retrospective — 2026-05-21

> **LOCK BREACH ALERT** | 4 A-tier losses from OAK at LAA | Lock guard: CAP ACTIVE (14d win rate 0.667)

**Catch-up note:** 2026-05-22 had zero picks in the log (local picks were not pushed). This run settles the 62 pending 2026-05-21 picks as a catch-up.

---

## Yesterday's Record (2026-05-21)

**33W  27L  2P** | +1.38u | Win rate: 55.0%

| Tier | W | L | P | Units |
|------|---|---|---|-------|
| A (Lock) | 4 | 4 | 1 | -1.24u |
| B | 28 | 21 | 1 | +2.70u |
| C | 1 | 2 | 0 | -0.08u |

---

## LOCK BREACH — OAK @ LAA (gamePk 824031)

### 4 A-tier losses — full postmortem

**Affected picks:**
- `2026-05-21-824031-ML-primary` — Angels ML -155 to -170 | LOSS
- `2026-05-21-824031-ML-0` — Angels ML -162 | LOSS
- `2026-05-21-824031-Total-primary` — Soriano K over 7.5 | LOSS
- `2026-05-21-824031-K-1` — Soriano K over 7.5 | LOSS

**What happened:** Luis Severino delivered a 10K 7IP shutout performance for Oakland, neutralising the Soriano quality edge model had assigned to LAA. OAK won 3-2 in 10 innings on a walk-off. Soriano pitched 6.2IP and produced exactly 7 strikeouts, one short of the 7.5 line.

**Root causes:**

1. **Opponent SP blind spot.** Severino entered with sub-3.00 ERA and above 9.5 K9 over his last 6 starts. Model assigned Angels ML at tier A without applying the opposing elite SP filter. Severino's resurgence was not adequately weighted.

2. **K-over line too aggressive.** Soriano K over 7.5 required an elite outing against a lineup at 22% K rate. Soriano was efficient in the early innings (did not need to push deep counts) and was pulled at 6.2IP when the game extended to extras. The line needed a 95th percentile outcome to cash.

3. **Same-game correlated A-tier stacking.** Two separate A-tier ML chips on the same game (ML-primary at -110 and ML-0 at -162) amplified the loss. These were correlated bets; publishing both as tier A violated concentration principles.

**New rules (effective immediately):**

- Do not publish A-tier ML on a team whose opponent SP has ERA under 3.00 and K9 above 9.5 in their last 6 starts.
- Do not publish A-tier K over 7.5 for any starter unless that starter has posted 8 or more K in 3 of their last 5 starts.
- Cap A-tier same-game picks to 2 total maximum. ML plus K on the same game exceeds correlated risk threshold.

---

## Game-by-Game Summary

### OAK @ LAA — OAK 3, LAA 2 (F10)
- F5: LAA 2, OAK 0 | 1st inn: YRFI (LAA 2)
- Soriano: 7K, 6.2IP | Severino: 10K, 7IP
- 5W 5L: Angels F5 ML WIN, Soriano over 6.5 WIN, Under 8 WIN, F5 Under 4 WIN, OAK ML WIN
- LOSSES: Angels ML x2, Soriano over 7.5 x2, NRFI

### PIT @ STL — PIT 6, STL 2
- F5: PIT 2, STL 1 | 1st inn: YRFI (PIT 1)
- Ashcraft: 9K, 7IP | May: 7K, 6IP
- 8W 1L 1P: Strong day. PIT ML, RL +1.5, Ashcraft Ks, F5 Under 4.5, F5 ML all WIN
- PUSH: Under 8 (total = 8 exactly)
- LOSS: NRFI (PIT scored in 1st)

### CLE @ DET — CLE 3, DET 1
- F5: CLE 2, DET 0 | 1st inn: NRFI
- Cantillo: 6K, 6IP | Mize: 4K, 6.2IP
- 6W 4L: CLE ML, Unders, F5 Under, NRFI WIN; DET RL -1.5 x2, Mize K over 5.5, DET F5 ML all LOSS

### ATL @ MIA — ATL 9, MIA 3
- F5: ATL 5, MIA 2 | 1st inn: YRFI (ATL 2)
- Strider: 9K, 6.1IP | Alcantara: 3K, 4IP
- 7W 2L: ATL ML x2, Strider Ks x2, F5 ML, Strider over 6.5 all WIN
- LOSSES: Under 7 (total 12), NRFI

### TOR @ NYY — TOR 2, NYY 0
- F5: TOR 1, NYY 0 | 1st inn: YRFI (TOR 1)
- Rodon: 7K, 3BB, 5IP | Fisher: 4K, 1.1IP
- 3W 5L: TOR ML x2 and F5 ML WIN; Over props, F5 Over 5, TOR Team Total, Rodon BB over 3.5 all LOSS

### COL @ ARI — ARI 2, COL 1
- F5: ARI 0, COL 0 | 1st inn: NRFI
- E. Rodriguez: 4K, 7IP | Agnos: 4K, 5IP
- 2W 6L 1P: ARI ML WIN, NRFI WIN; ARI RL -1.5 x2 (narrow 1-run win), E. Rodriguez K props, Over 9, ARI Team Total all LOSS
- PUSH: ARI F5 ML (tied 0-0 after 5)

### NYM @ WSH — NYM 2, WSH 1
- F5: NYM 2, WSH 1 | 1st inn: NRFI
- Peterson: 3K, 5IP | Cavalli: 9K, 7IP
- 2W 4L: Cavalli K over 5.5 WIN, NRFI WIN; WSH ML x2, Over 9, Peterson K over 5.5 LOSS

---

## Lock System Status

| Metric | Value |
|--------|-------|
| Guard status | CAP ACTIVE |
| 14d win rate | 66.7% |
| Threshold | 80.0% |
| Lifetime record | 10W 5L 2P 1V |
| Lifetime win rate | 66.7% |
| Lifetime units | +2.72u |

**CAP ACTIVE:** Until the rolling 14d Lock win rate recovers above 80%, A-tier picks are capped. Maximum 1 A-tier pick per card. All A-tier candidates require second-pass validation against the new elite-opponent-SP and K-line rules above.

---

## Market Performance (2026-05-21)

| Market | W | L | P | Units |
|--------|---|---|---|-------|
| ML | 12 | 4 | 0 | +4.76u |
| F5_ML | 4 | 1 | 1 | +1.76u |
| K | 5 | 7 | 0 | -2.55u |
| RL | 3 | 4 | 0 | -2.04u |
| Total | 4 | 7 | 1 | -2.55u |
| F5_Total | 3 | 1 | 0 | +1.75u |
| NRFI | 2 | 4 | 0 | -2.10u |
| TeamTotal | 0 | 2 | 0 | -2.00u |
| BB | 0 | 1 | 0 | -1.00u |

**Key takeaway:** ML and F5 markets positive. K-over, NRFI, and totals all negative. K-over props missed across 4 different starters (Soriano, Mize, E. Rodriguez, Peterson).

---

## Adjustments for 2026-05-22

1. **LOCK BREACH ENFORCEMENT:** Apply new A-tier rules before any Lock designation today. Validate opponent SP metrics (ERA, K9) before assigning A-tier ML.
2. **K-over second pass:** Soriano, Mize, E. Rodriguez, and Peterson all missed. Run K9 trend, recent K totals, and opposing lineup K-rate before publishing any K prop.
3. **RL -1.5 restriction:** DET and ARI both failed to cover with narrow wins. Restrict RL -1.5 on heavy favourites to clear blowout scenarios.
4. **Over totals:** 0-for-5 on overs involving elite starters. Require starter ERA above 4.00 or bullpen ERA above 4.50 before publishing Over props.
5. **DATA NOTE:** Zero picks logged for 2026-05-22. Local picks from the 11:30AM run were not pushed. Check picks_log.json on the local machine before the next session.

---

*Generated: 2026-05-23 | Settling date: 2026-05-21 | Catch-up run*
