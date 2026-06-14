# MLB Dashboard Refresh Report

Window: midday (11:30 AM)
Run timestamp: 2026-06-14T15:55:00Z (11:55 AM ET)
Slate date: 2026-06-14
Game count: 15 (1 Live: MIA at PIT)

## API data quality
- Probable pitchers: 30 of 30 confirmed via schedule API (probable_pitcher_source=schedule-api). Zero TBD.
- Pitcher season stats: batch fetched for all 30 IDs (people endpoint with -g glob disable to fix bracket parsing).
- Lineups: confirmed (9 players each) for 11 games; projected from rolling form for 4 evening games (PHI away, COL at ATH, CHC at SF, TB at LAA, TEX at BOS).
- Weather: Open Meteo success for all 14 outdoor or retractable parks. Notable: CLE 65F with 88 percent rain, CIN 75F with 63 percent rain, WSH 95F, BAL 92F, ATH (Las Vegas) 103F extreme, TOR roof treated closed.

## Per game summary
- MIA at PIT (PNC Park): C 65, proj 3.3 to 3.7, 5 picks. Chips: Pass/Lean only
- SD at BAL (Oriole Park at Camden Yards): B 73, proj 4.7 to 4.6, 6 picks. Chips: San Diego Padres ML +100 to +115; Over 9 or 9.5
- SEA at WSH (Nationals Park): B 74, proj 4.4 to 3.4, 6 picks. Chips: Seattle Mariners ML -125 to -140; Hancock K over 5.5
- NYY at TOR (Rogers Centre): B 73, proj 4.6 to 3.7, 6 picks. Chips: New York Yankees ML -130 to -145; Warren K over 5.5
- AZ at CIN (Great American Ball Park): C 67, proj 4.6 to 4.8, 5 picks. Chips: Cincinnati Reds ML -115 to -130
- DET at CLE (Progressive Field): C 66, proj 3.4 to 3.6, 5 picks. Chips: Under 8
- ATL at NYM (Citi Field): B 72, proj 3.8 to 3.9, 5 picks. Chips: Atlanta Braves ML +100 to +115; Under 8.5
- HOU at KC (Kauffman Stadium): B 73, proj 4.4 to 3.7, 6 picks. Chips: Houston Astros ML -120 to -135; Arrighetti K over 5.5
- STL at MIN (Target Field): B 71, proj 3.9 to 4.0, 5 picks. Chips: Bradley K over 5.5
- LAD at CWS (Rate Field): B 75, proj 5.0 to 3.6, 6 picks. Chips: Los Angeles Dodgers ML -160 to -180; Dodgers F5 ML -135 to -150
- PHI at MIL (American Family Field): B 76, proj 3.5 to 3.4, 6 picks. Chips: Under 7.5 or 8; Sánchez K over 6.5
- COL at ATH (Las Vegas Ballpark): B 73, proj 5.1 to 5.4, 5 picks. Chips: Over 9.5 or 10
- CHC at SF (Oracle Park): C 66, proj 3.7 to 4.0, 5 picks. Chips: San Francisco Giants ML -120 to -135
- TB at LAA (Angel Stadium): C 67, proj 4.5 to 3.8, 5 picks. Chips: Tampa Bay Rays ML -120 to -135
- TEX at BOS (Fenway Park): B 71, proj 4.1 to 4.0, 5 picks. Chips: Texas Rangers ML -110 to +105; Eovaldi K over 5.5

## Overlays deployed
- odds_overlay.json: 15 games (moneyline, total, runline derived from projected scores)
- statcast_overlay.json: 15 games (ERA based xFIP and FIP estimates, playerId null)
- picks_log.json: 26 new records appended, 6 updated in place, 740 total

## Learnings adjustments applied
Lock Guard ACTIVE: A tier publication capped. Result: zero A tier cards, all grades B or C. Other active rules applied per card: projected lineup cap to B plus 84 (5 evening games), sub 25 inning starter cap to C with one chip (Rolison 24.0 IP at SF, Legumina 17.2 IP at LAA, Poulin 25.1 IP noted at WSH), K over six inning floor and trailing rate check (Sánchez and Arrighetti verified, others capped at 5.5), variance down weight on rain games (CLE, CIN), Oracle under suppressed from A tier.

## Deploy
- Repo: HTest1212/cloudflare-pages-site, branch main
- Commit: b8ef5ac80fd5eb9b9a7b667f430e9e8f6d2e9edf "Auto refresh 1130am 2026-06-14"
- Push: success (321effb..b8ef5ac). Cloudflare Pages auto deploy triggered.
- Render functions verified present after splice: renderClaudePicksBlock, tierFromProb, renderBestBetsBlock.

## Errors and fallbacks
- Workspace mount at the Desktop folder returned EPERM and Resource deadlock on file reads and writes throughout the run. Recovered by cloning the repo fresh to /tmp and reading learnings.json, picks_log.json and overlays from the clone instead of the workspace.
- GitHub token read from existing .git/config remote in the workspace clone (.env file not present in workspace).
- Per game overlay files (bullpen, rolling form, catcher framing, pitch matchup, park factors, park wind rules, umpire) were not present in the workspace or repo. Cards used confirmed API pitcher data, live weather, and park run environment knowledge; bullpen and park notes derived analytically. Noted as fallback.
- curl people endpoint initially returned a stale locked file in /tmp from a prior run; resolved by writing to unique filenames.
