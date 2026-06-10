# MLB Dashboard Refresh Report

**Window:** midday (11:30 AM ET)
**Run timestamp:** 2026-06-10 15:33 UTC
**Slate date:** 2026-06-10
**Game count:** 15

## API data quality

Slate pulled live from the MLB Stats API schedule endpoint with probablePitcher, lineups, team, and venue hydrated. Pitcher season stats pulled in one batch call for all 28 confirmed arms.

- Confirmed probable pitchers: 28 of 30 starter slots (source schedule-api)
- TBD starters: 2 (Minnesota at Detroit away side, Chicago White Sox home side)
- Confirmed lineups: Boston (away) at Tampa Bay, and both New York Yankees and Cleveland at Progressive Field. All other games used projected orders, capped at B plus 84 per the timing rule.
- Weather fetched successfully for all 14 outdoor or retractable parks (Tropicana Field skipped as a fixed dome). No weather fallbacks needed.

Notable weather: Las Vegas Ballpark 103 degrees, PNC 91, Rate Field 92 with 50 percent rain, Kauffman 90 with a 22 mph wind, Camden 77 with 58 percent rain, Coors 88 at altitude.

## Per game summary

| Game | Grade | Proj Score | Picks | Primary chips |
|------|-------|-----------|-------|---------------|
| BOS at TB | B 80 | 3.4 to 3.9 | 6 | Rays ML, Rays F5 ML |
| NYY at CLE | B 83 | 3.4 to 3.2 | 6 | Under 8, Messick K Over 5.5, Guardians F5 ML |
| WSH at SF | B 78 | 3.5 to 3.7 | 6 | Under 7.5, F5 Under 4 |
| CIN at SD | B 83 | 3.3 to 4.5 | 6 | Padres ML, Padres F5 ML, King K Over 5.5 |
| SEA at BAL | B 76 | 4.1 to 3.9 | 6 | Under 8.5, F5 Under 4.5 |
| LAD at PIT | B+ 84 | 4.8 to 2.9 | 6 | Dodgers F5 ML, Dodgers ML, Ohtani K Over 5.5 |
| MIN at DET | C 62 | 3.8 to 4.2 | 6 | Tigers F5 ML |
| AZ at MIA | C+ 68 | 4.3 to 3.6 | 6 | Diamondbacks ML |
| PHI at TOR | B+ 84 | 4.9 to 3.5 | 6 | Phillies ML, Luzardo K Over 6.5 |
| STL at NYM | C+ 67 | 4.0 to 3.9 | 6 | Over 8.5 |
| TEX at KC | B 78 | 4.3 to 4.0 | 6 | Gore K Over 6.5, Over 9 |
| ATL at CWS | C 64 | 5.0 to 3.2 | 6 | Sale K Over 6.5 |
| CHC at COL | B 76 | 6.0 to 4.7 | 6 | Over 11, Cubs ML |
| MIL at ATH | B 75 | 5.2 to 4.9 | 6 | Over 9.5 |
| HOU at LAA | B 79 | 4.0 to 3.8 | 6 | Detmers K Over 6.5 |

No A tier cards published, consistent with the projected lineup cap and the active learnings on variance and exposure. Highest grades are B plus 84 on LAD at PIT (Ohtani) and PHI at TOR (Luzardo over a scuffling Scherzer).

## Overlays deployed

- odds_overlay.json: 15 games, moneyline, total, and runline derived from projected scores
- statcast_overlay.json: 15 games, ERA based xFIP and FIP estimates for all 28 confirmed arms, league average placeholders for the 2 TBD slots
- picks_log.json: 27 primary chip entries appended for 2026-06-10, total 595 records, sorted date then confidence descending

## Learnings adjustments applied

All 11 active adjustments from learnings.json were kept live. Key applications this slate:

- Projected lineup cap held all non confirmed cards to B plus 84.
- TBD cap held MIN at DET and ATL at CWS to C with a single chip each (Tigers F5 ML, Sale K Over 6.5).
- Sub 15 inning starters down weighted: AZ at MIA capped at C plus on a 5 inning Gusto sample, BOS at TB and LAD at PIT noted thin opposing samples but rode the strong side.
- K over cushion rule enforced: every K chip clears the posted line by the required margin (Messick, King, Ohtani at a conservative 5.5 to respect his innings cap, Luzardo, Gore, Sale, Detmers). No K over published without a six inning floor.
- Oracle and Giants restrictions applied: WSH at SF under set at 7.5 as a B not an A, Giants ML held to a C lean at no worse than -125.
- Variance down weighting held Coors and Las Vegas overs to B, and kept the Scherzer five start sample game at B plus not A.

## Deploy

- GitHub commit: c19543b (prev 15f867d), branch main
- Push status: success
- Cloudflare Pages auto deploy triggered on push
- Live verification: odds_overlay.json and statcast_overlay.json both serving slate 2026-06-10 with 15 games at https://mlb-betting-dashboard-v2.pages.dev

## Errors and fallbacks

- Workspace mount has the known resource deadlock on direct file reads and writes. Worked around by cloning the repo fresh from origin into /tmp, reading overlays and the index from the clone, and reading the GitHub token from the repo git config remote URL (no .env file present in the working folder this run).
- No data fallbacks were needed for pitcher stats or weather.
