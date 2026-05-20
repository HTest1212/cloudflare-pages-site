# MLB Dashboard Refresh Report — 2026-05-18

**Run:** 11:30 AM ET automated refresh
**Commit:** 89b94c5
**Deploy:** Cloudflare Pages CI triggered on push to main — verified live

---

## Games Analyzed: 14

| Game | Grade | Score | Primary Chip |
|------|-------|-------|--------------|
| ATL@MIA | B | 80 | ATL ML -155 to -175 |
| TEX@COL | B | 78 | Under 9.5 or 10 |
| LAD@SD | B | 78 | Under 7 or 7.5 |
| BAL@TB | B | 76 | TB ML -175 to -195 |
| CIN@PHI | B | 75 | Wheeler K over 7.5 |
| MIL@CHC | B | 74 | CHC ML -140 to -160 + Imanaga K over 7.5 |
| TOR@NYY | B | 73 | NYY ML -145 to -165 |
| CLE@DET | C | 65 | CLE ML +105 to +120 |
| ATH@LAA | C | 62 | ATH ML -120 to -135 |
| SF@ARI | C | 62 | ARI ML -125 to -140 |
| HOU@MIN | C | 60 | MIN ML -115 to -130 |
| CWS@SEA | C | 60 | Under 7 or 7.5 |
| BOS@KC | C | 58 | Over 8 or 8.5 |
| NYM@WSH | C | 58 | Over 8.5 |

**Total picks logged:** 15 (8 grade B, 7 grade C)

---

## Key Changes from Prior Build

**TEX@COL — Major Flip (Over 12 to Under 9.5 or 10)**
Weather data showed 44 degrees F, 7 mph north wind blowing IN from CF, and 40% rain risk.
This entirely cancels the Coors altitude effect. Prior build incorrectly used 70 degrees dry Denver.
This is the most important correction in this refresh cycle.

**CWS@SEA — Upgraded from Pass to C/60**
WNW wind at 4.8 mph blowing in from CF confirmed at 64 degrees F at a pitcher park (factor 96, HR 92).
Under 7 or 7.5 now earns a chip.

**BOS@KC — Upgraded from Pass to C/58**
14.9 mph wind at 79 degrees F with two non elite starters.
Over 8 or 8.5 earns a weather driven chip.

**NYM@WSH — Upgraded from D/50 to C/58**
92.9 degrees F extreme heat with south out wind at neutral Nationals Park.
Over 8.5 earns a weather lean.

**ATL@MIA — Starter corrected to Strider (prior build referenced Sale)**

**CIN@PHI — Weather updated to actual 89.5 degrees F (prior build had 72 degrees)**
Wheeler K over 7.5 chip unchanged; projected score bumped to 4.5 and 4.8.

---

## Learning Adjustments Applied (from 2026-05-14)

1. Require confirmed lineup check before logging hitter props: No hitter props in any primary chip row; all 14 games projected at 11:30 AM.
2. Limit to two markets per game: No card exceeds 2 chips.
3. Reduce Altuve props when recent H/AB below .200: Not applicable today.

---

## Data Sources
- MLB schedule and rosters: mlb-api-mcp
- Weather: Open Meteo API via curl at 11:30 AM ET for all 11 outdoor parks
- Domes: TB Tropicana, MIA loanDepot, ARI Chase Field

---

## Deploy Verification
- Live URL: https://mlb-betting-dashboard-v2.pages.dev
- Coors flip chip confirmed live (4 occurrences of "Under 9.5 or 10")
- lastUpdated: 2026-05-18
- picks_log.json: 15 new picks appended (29 total on file)
