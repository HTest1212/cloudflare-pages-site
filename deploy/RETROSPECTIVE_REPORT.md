# MLB Betting Retrospective — 2026-05-18

---

## SECTION 2 — SLATE SUMMARY

**Date:** 2026-05-18  
**Games on slate:** Full slate (15 picks across 11+ games)  
**Pick schemas:** Schema C midday only (15 picks)  
**Overall record:** 8W-6L-1V | +0.61u | Win rate 57.1% | ROI +4.35%

| Market | Picks | W | L | V | Units | Win% |
|--------|-------|---|---|---|-------|------|
| ML | 8 | 5 | 3 | 0 | +0.88 | 62.5% |
| Total | 5 | 3 | 2 | 0 | +0.73 | 60.0% |
| K | 2 | 0 | 1 | 1 | -1.00 | 0.0% |

| Tier | Picks | W | L | V | Units |
|------|-------|---|---|---|-------|
| B | 10 | 5 | 4 | 1 | -0.27 |
| C | 5 | 3 | 2 | 0 | +0.88 |

---

## SECTION 3 — LOCK TRACK RECORD

**Guard status:** HEALTHY  
**Lifetime Lock (A tier) picks:** 0  
**Rolling 14d Lock win rate:** N/A (no A tier picks published yet)  
**Self-tightening guard:** Inactive — threshold at 80%. No cap in effect.

*No Lock picks have been published yet. The guard system is primed and will activate on the first A tier pick.*

---

## SECTION 4 — TOP 3 LOSSES WITH DIAGNOSES

**1. ATL ML -165 → LOSS (MIA 12, ATL 0)**  
Category: MODEL_ERROR  
Picked ATL behind Strider vs weak MIA offense, expected a pitcher dominated contest at Truist. MIA exploded for 12 runs — complete game blowout. Road Coors-style outlier output against a pitcher the model overrated. Thesis: wrong on both run suppression and lineup activation. Do not publish ML favorites above -150 without confirming recent opponent hard-contact rate.

**2. CHC ML -150 and Imanaga K over 7.5 → LOSS/STARTER_REGRESSION (MIL 9, CHC 3)**  
Category: MODEL_ERROR / STARTER_REGRESSION  
Imanaga at home vs Sproat looked dominant on paper. Actual line: 2 Ks, 8 ER in 4.1 innings. The K prop missed by 5.5 strikeouts — the single largest K line miss of the run. Imanaga's elevated hard-contact rate in recent starts was the signal the model missed. Both the ML and K prop stemmed from the same faulty pitcher confidence. Lesson: one corrupted pitcher reading cascades into two losing picks.

**3. PHI (Wheeler) K over 7.5 → VOID (Wheeler scratched)**  
Category: LINEUP_CHANGE  
Wheeler was announced as the starter at pick time but was scratched before first pitch, replaced by Andrew Painter. The K prop was correctly voided. No financial damage but this is a process gap — any K prop must be confirmed within 90 minutes of first pitch. This will become a loss rather than a void if a substitute starter is counted.

---

## SECTION 5 — PATTERNS IDENTIFIED

**Pattern 1: MODEL_ERROR (3 losses)**  
ATL ML, CHC ML, BOS@KC Over — all three were confident theses that collapsed due to incorrect assumptions about either starter quality or run environment.  
Rule generated: Require recency-weighted splits (last 7 starts) before publishing any ML favorite at or above -150 odds. Confirm hard-contact rates trending in the right direction.

**Pattern 2: STARTER SCRATCH (1 void, risk of future loss)**  
Wheeler scratched on K prop. One void this time but represents a repeatable exposure.  
Rule generated: All K props and starter-dependent ML picks must be re-confirmed within 90 minutes of first pitch. If starter is replaced, cancel or void immediately.

**Pattern 3: PARK CONTEXT MISS (1 loss)**  
TEX@COL Under 9.5 — Coors game total ran to 13 despite 44 degree temperature. Cold weather normally suppresses Coors offense but did not here.  
Rule generated: Coors Under plays require a 3-year historical over rate check at the specific line before publishing. Never take Under at Coors below 11 without confirming extreme suppression conditions (sub-35F and heavy rain forecast).

---

## SECTION 6 — ADJUSTMENTS FOR TODAY

1. Never publish a B tier ML favorite on a road game without confirming the starter is active and recent opponent contact rates
2. Do not ride ML of a team whose starter is posting elevated hard-contact rates last 3 starts
3. Confirm starter identity within 90 minutes of publishing any K prop or game result pick
4. Coors field totals require historical over rate check before taking Under at any line below 11
5. Avoid backing road favorite teams with negative recent form even at short odds
6. Verify recent scoring pace of both teams before publishing an Over in a pitcher matchup with neither team a consistent scorer
7. Winning angle: SD Under with Petco and elite starters (LAD@SD totaled 1 run) — continue targeting low-run games at pitcher parks
8. Winning angle: NYM@WSH Over delivered 23 runs — warm weather plus thin bullpens is a reliable Over signal
9. Grade B picks: 5W-4L-1V on the day. CHC ML and ATL ML were avoidable with better confirmation steps
10. Grade C picks: 3W-2L. CLE ML +112 hit. Continue publishing plus-money C picks with strong matchup edges

---

## SECTION 7 — LIFETIME AND RECENT KPIs

**Lifetime (system launched ~May 7):**  
344W-272L-22P-53V | +30.29u | Win rate 55.84% | ROI +4.75% | Total stake 638u

**Recent 7 days:**  
77W-72L-10P-18V | -11.65u | Win rate 51.68% | ROI -7.33% | Total stake 159u

> **Note:** Recent 7 day performance is materially weaker than lifetime average. Win rate has dropped ~4 points and ROI swung negative. This pattern warrants reducing stake on lower confidence picks until the win rate recovers above 54%.

**By market (lifetime):**  
See bet_record_summary.json for full breakdown.

---

## SECTION 8 — DATA NOTES

- All 15 picks were Schema C midday format. No v1 or v2 algorithm picks on this date.
- Wheeler K prop settled as VOID (LINEUP_CHANGE) — Painter started, Wheeler scratched.
- recent14 window equals lifetime because system launched 2026-05-07; all data falls within 14 days.
- recent7 ROI of -7.33% is a meaningful warning signal. Monitor closely over next 3 days.
- No boxscore data gaps. All 15 gamePks resolved cleanly from MLB Stats API.
- locks_log.json initialized with 0 entries — no A tier picks have been published.
- Git PAT sourced from .env GITHUB_TOKEN (primary source).
