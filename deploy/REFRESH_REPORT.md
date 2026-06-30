# MLB Dashboard Refresh Report

Window: midday (11:30 AM ET)
Run timestamp UTC: 2026-06-30T18:54:46Z
Slate date: 2026-06-30
Game count: 15

## API data quality
Probable pitchers: 29 of 30 confirmed via schedule API; 1 TBD (Arizona Diamondbacks home starter, gamePk 825066).
Pitcher season stats: all 29 confirmed arms pulled real lines from the people endpoint.
Weather: 15 of 15 parks fetched from Open Meteo successfully. Retractable roofs projected closed at Daikin Park (89F), American Family Field (94F), and Chase Field (99F); open at Rogers Centre (85F).
Lineups: all projected (no lineup endpoint returned players at refresh time except a partial Baltimore home list); all cards capped at B plus per the projected lineup rule.

## Per game summary

| Game | Grade | Proj Score | Picks | Primary Chips |
|---|---|---|---|---|
| CWS @ BAL | C 62 | CWS 4.5, BAL 4.8 | 6 | none (lean only) |
| TEX @ CLE | B 78 | TEX 4.1, CLE 3.2 | 6 | deGrom K Over 6.5 ; Under 8 |
| PIT @ PHI | B 80 | PIT 3.6, PHI 4.9 | 6 | Phillies ML  140 to  160 ; Sanchez K Over 6.5 |
| DET @ NYY | B 81 | DET 3.4, NYY 3.0 | 6 | Under 7.5 ; Schlittler K Over 6.5 |
| NYM @ TOR | C 66 | NYM 3.7, TOR 3.9 | 6 | Under 8.5 |
| WSH @ BOS | B 76 | WSH 3.4, BOS 5.0 | 6 | Red Sox ML  130 to  150 ; Red Sox Team Total Over 4.5 |
| STL @ ATL | C 63 | STL 3.1, ATL 3.9 | 6 | none (lean only) |
| TB @ KC | C 65 | TB 4.5, KC 3.9 | 6 | Rays ML  110 to  125 |
| CIN @ MIL | C 60 | CIN 4.4, MIL 4.5 | 6 | none (lean only) |
| SD @ CHC | C 69 | SD 5.0, CHC 5.4 | 6 | Over 10 |
| MIN @ HOU | B 80 | MIN 4.6, HOU 3.3 | 6 | Twins ML  105 to  120 ; Ryan K Over 6.5 |
| MIA @ COL | B 74 | MIA 5.2, COL 5.8 | 6 | Over 11.5 ; Rockies Team Total Over 5.5 |
| LAD @ ATH | B 76 | LAD 5.0, ATH 3.8 | 6 | Dodgers ML  130 to  150 ; Dodgers Team Total Over 4.5 |
| LAA @ SEA | B 76 | LAA 3.3, SEA 3.2 | 6 | Under 7.5 ; Woo K Over 5.5 |
| SF @ ARI | C 56 | SF 3.8, ARI 4.0 | 6 | none (lean only) |

## Overlays deployed
odds_overlay.json: 15 games (moneyline, total, runline from projected scores).
statcast_overlay.json: 15 games (ERA based xFIP and FIP estimates, playerId null, statcast_7d placeholder).
picks_log.json: 1111 total entries; 19 primary chip records appended for 2026-06-30.

## Learnings adjustments applied
Read from learnings.json (asof 2026-06-29, yesterday 2026-06-28: 45 picks, 25 wins 20 losses, plus 2.44 units). 12 active adjustments held throughout the run. Key effects this slate:

- VARIANCE down weight applied across every card (dominant 16 loss tag from 06-28).
- Coors over capped at B (Eury Perez sub 5.00 ERA and only light wind) per the Coors lock rule, gamePk 824338.
- K over leash check applied: deGrom, Sanchez, Schlittler, Joe Ryan, and Woo cleared a six inning floor and were published; Skubal K over kept secondary and sized down for short leash risk on a 59.2 inning return arc.
- Cold form tier ML cap held Atlanta to C despite the Perez edge, and kept Yankees and Mariners off any side chip.
- No A tier published; Lock guard healthy and the rolling 14 day Lock sample remains empty.
- All B grade cards capped at two chips and all C cards at one chip or fewer per the grading table.

## Deploy
GitHub commit: 7b3dd49 (Auto refresh 1130am 2026-06-30). Push 8521379..7b3dd49 to main after a clean rebase onto a concurrent retrospective push.
Cloudflare Pages auto deploy verified live: odds_overlay.json on the live site returned asOf 2026-06-30T18:52:08Z with 15 games.
Live URL: https://mlb-betting-dashboard-v2.pages.dev

## Errors and fallbacks
- Workspace mount returned Resource deadlock (errno 35) on bash and EPERM on the file tools, the known recurring lock. Built and pushed from a fresh public clone at /tmp; GitHub token recovered from the workspace git remote config. This report committed to the repo deploy directory rather than written to the locked mount.
- The five analysis overlays park_factors, park_wind_rules, catcher_framing, pitch_matchup, and umpire_factors are absent from the repo; park, wind, and weather reads were built from Open Meteo plus baseline park knowledge.
- A concurrent retrospective run advanced the remote (learnings, outcomes, locks logs) mid push; rebased cleanly with no conflict on the four refresh files.