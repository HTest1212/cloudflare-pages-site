# MLB Betting Retrospective Report
**Slate Date:** 2026-05-17 | **Generated:** 2026-05-18 04:00 UTC

---

## Slate Summary

15 games on the board (all Final). 14 picks logged via midday 11:30 AM run (Schema C). No v1 or v2 algorithm picks found for this date.

**Pick count by schema:** v2 = 0, v1 = 0, midday = 14

---

## Yesterday Record: 6W-8L | -3.18 units | Win Rate 42.86% | ROI -22.73%

### By Market

| Market | W | L | Units | Win Rate |
|--------|---|---|-------|----------|
| ML     | 4 | 7 | -3.63 | 36.4%    |
| Total  | 2 | 0 | +1.82 | 100%     |
| K      | 0 | 2 | -2.00 | 0%       |

### By Tier

| Tier | W | L | Units | Win Rate |
|------|---|---|-------|----------|
| b    | 4 | 2 | -0.12 | 66.7%    |
| c    | 2 | 6 | -3.06 | 25.0%    |

---

## Top Three Losses with Diagnoses

### 1. ATH ML -115 to -130 (gamePk 825006)
**Final:** SF 10, OAK 1 | **Category:** MODEL_ERROR

Picked the Athletics at home expecting Webb to be neutralized by the wind and their home record. Instead Webb was dominant and SF ran up 10 runs. Backing an underdog vs an elite ace in a large sample is a negative expected value spot regardless of home field. Narrative did not hold.

### 2. WSH ML +110 to +125 (gamePk 822738)
**Final:** BAL 7, WSH 3 | **Category:** MODEL_ERROR

Faded Baltimore on the road but they scored 7 and WSH was blown out. The road struggles edge on BAL was not confirmed by recent road splits. This was a narrative based fade rather than a data driven one.

### 3. STL ML -150 to -165 (gamePk 823058)
**Final:** KC 2, STL 0 | **Category:** VARIANCE

STL was shut out at home by Kansas City. Mikolas groundball profile was expected to suppress runs while the offense generated enough support. KC held STL scoreless in a 2 to 0 game which is a low probability outcome despite the rationale being directionally sound.

---

## Patterns Identified

### VARIANCE (5 losses)
Close single run losses on NYY ML, CHC ML, STL ML, MIL ML, and near miss on Skenes K (7 actual vs 7.5 line). The model reads were directionally sound on most of these but the variance went negative on every close call.

**Rule:** On days with 3 or more variance losses in single run games, reduce ML stake by 20% and shift to run lines for top tier picks.

### MODEL_ERROR (2 losses)
ATH ML and WSH ML both reflected overconfidence in narrative spots without confirming recent splits. The model backed an underdog vs an elite starter (Webb) and faded a road team without verifying recent form.

**Rule:** Downgrade plus money picks on road underdog ML when opponent is at home with 0.500 or better record; require stronger spot than narrative alone.

### STARTER REGRESSION (1 loss)
Gausman K over 6.5 missed by 1.5 strikeouts. Pitcher park and wind in were expected to suppress offense and generate easy Ks but Gausman only worked 6 innings with 5 Ks. Comerica and 15 mph in wind suppressed his K volume rather than boosting it.

**Rule:** Require at least 28% K rate season average before taking K prop over lines; bump line threshold by 0.5 in first 3 months.

---

## Adjustments for Today (2026-05-18)

1. NYY ML lean at Citi was wrong; NYM home field plus uncertainty on starter should have been a pass.
2. CHC ML lost to CWS 9 to 8; avoid laying heavy juice on NL teams in crosstown games with wind blowing out.
3. WSH plus money miss; BAL road struggles did not translate, confirm recent road splits before fading.
4. STL ML at home lost to KC shutout; Mikolas groundball profile did not generate strikeouts or runs.
5. ATH ML loss to SF 10 to 1; Webb ace differential was too steep, avoid backing underdogs vs elite starters.
6. MIL ML narrow miss 5 to 4; injuries to Buxton and Larnach did not guarantee MIL cover.
7. Gausman K under 6.5 missed by 1.5 strikeouts; TOR pitcher park suppresses K volume for finesse types.
8. Skenes K missed by 0.5 on 7.5 line; consider 7.0 line threshold for high strikeout aces.
9. Winning angle: aces plus pitcher parks for totals (PHI at PIT Under 7.5 nailed it, 6 runs total).
10. Winning angle: large underdog plus money on road teams at altitude or offense friendly parks (ARI at COL).
11. Grade C tier picks went 2W 6L; tighten grade C standards or reduce to one C pick per slate.
12. Grade B tier picks went 4W 2L; maintain current criteria for B tier picks.

---

## Lifetime KPIs

| Metric     | Value     |
|------------|-----------|
| Record     | 336W-266L |
| Units      | +29.68    |
| Win Rate   | 55.81%    |
| ROI        | +4.76%    |
| Total Stake | 623.0    |

## Recent 14 Day KPIs

| Metric     | Value     |
|------------|-----------|
| Record     | 336W-266L |
| Units      | +29.68    |
| Win Rate   | 55.81%    |
| ROI        | +4.76%    |

*Note: Recent 14 window equals lifetime window as all logged picks fall within the 14 day lookback.*

---

## Data Notes

- Git clone succeeded without PAT (public repo); picks_log.json pulled fresh from origin.
- All 15 scheduled games finalized before this run.
- Schema C midday format used for all 14 picks; no id, gameId, or type fields present. Stable IDs generated using {date}-{game-normalized}-{market}-mid pattern.
- Skenes K data: 7 Ks in 5.0 IP (vs 7.5 line, loss by 0.5).
- Gausman K data: 5 Ks in 6.0 IP (vs 6.5 line, loss by 1.5).
- No picks found for gamePks: 824436 (CIN@CLE), 824192 (TEX@HOU), 823138 (SD@SEA), 824358 not settled via picks (ARI@COL was picked via ARI ML).
