# MLB Dashboard Refresh Report

Window: midday (11:30 AM) late pass with fresh live data
Run timestamp: 2026-06-09 19:44:00 UTC
Slate date: 2026-06-09
Game count: 15

## Run context
This scheduled 11:30 AM task fired late in the afternoon as a duplicate invocation. The earlier 11:30 run had already deployed, so the remote carried today commits. This pass re pulled fully fresh live data at run time, rebuilt all cards and overlays, deduplicated the picks log so only this pass set remains for the slate, and deployed on top of current HEAD.

## API data quality
- Pitchers confirmed: 30 of 30, every game carries confirmed probable pitchers from the schedule API
- Pitchers TBD: 0
- Weather success: 14 of 14 outdoor and retractable parks fetched from Open Meteo; Tropicana Field skipped as a closed dome
- Supporting overlays for bullpen, rolling form, park factors, park wind, umpire, catcher framing, and pitch matchup were not present in the workspace or repo, so cards were built from confirmed pitcher stats, live weather, park knowledge, and active learnings rules

## Per game summary
- CHC at COL | B82 | proj 6.4 to 6.0 | 6 picks | chips: Over 11.5 or 12 ; Cubs Team Total Over 5.5
- SEA at BAL | B80 | proj 5.0 to 3.6 | 6 picks | chips: Mariners ML -135 to -150 ; Mariners F5 ML -130 to -145
- PHI at TOR | B80 | proj 3.3 to 3.2 | 6 picks | chips: Cease K Over 7.5 ; F5 Under 4.5
- BOS at TB | B79 | proj 3.3 to 3.4 | 6 picks | chips: Under 7 or 7.5 ; F5 Under 4
- CIN at SD | B79 | proj 4.0 to 3.0 | 6 picks | chips: Reds ML -115 to -130 ; Burns K Over 6.5
- LAD at PIT | B78 | proj 3.8 to 3.2 | 6 picks | chips: Skenes K Over 6.5 ; F5 Under 4.5
- AZ at MIA | B78 | proj 3.4 to 4.0 | 6 picks | chips: Marlins ML -120 to -135 ; Marlins F5 ML -125 to -140
- NYY at CLE | B77 | proj 4.8 to 3.5 | 6 picks | chips: Yankees ML -130 to -145 ; Yankees Team Total Over 4.5
- ATL at CWS | B77 | proj 4.6 to 3.4 | 6 picks | chips: Braves ML -140 to -155 ; Braves F5 ML -130 to -145
- MIN at DET | B74 | proj 3.9 to 3.6 | 6 picks | chips: Bradley K Over 6.5
- STL at NYM | C68 | proj 3.7 to 4.2 | 6 picks | chips: Mets ML -120 to -135
- TEX at KC | C64 | proj 3.8 to 3.6 | 6 picks | chips: Pass, no primary chip
- MIL at ATH | C63 | proj 4.4 to 4.6 | 6 picks | chips: Pass, no primary chip
- WSH at SF | C62 | proj 3.4 to 3.6 | 6 picks | chips: Pass, no primary chip
- HOU at LAA | C60 | proj 4.0 to 3.8 | 6 picks | chips: Pass, no primary chip

## Overlays deployed
- odds_overlay.json: 15 games
- statcast_overlay.json: 15 games, ERA based xFIP and FIP estimates
- picks_log.json: 20 entries for the slate, 568 total after dedupe

## Learnings adjustments applied
- LOCK GUARD ACTIVE: rolling 14d Lock win rate below 0.85, so no A tier cards were published; all cards capped at B or lower
- 11:30 AM projected lineup cap held projected lineup cards to B plus 84 maximum
- K over chips published only where season strikeouts per start exceed the posted line: Cease 7.5, Burns 6.5, Skenes 6.5, Bradley 6.5, Gilbert 5.5
- K over withheld on Gerrit Cole due to blowout and short leash risk on an 18 inning return sample
- Robert Gasser flagged under 15 innings at 13.1, triggering a one letter downgrade and a quarter Kelly cap; the over there kept off a chip
- Under totals checked against the both lineups top 12 rule; full unders softened where both offenses are capable, as at Toronto
- Per slate exposure capped given the lock guard warning; below 65 confidence games TEX at KC, HOU at LAA, WSH at SF, and MIL at ATH carry zero primary chips

## Deploy
- GitHub commit: b665a900242310a140efb6e4971d723e5360e6db
- Push status: success, 5d4b7a3 to b665a90 on main
- Cloudflare Pages auto deploy verified live at https://mlb-betting-dashboard-v2.pages.dev/index.html with generatedAt 2026-06-09T19:35:46Z and 15 cards present

## Errors and fallbacks
- Workspace folder mount has the known Resource deadlock, so all reads and writes used the cloned repo in /tmp rather than the workspace folder
- First push was rejected because the earlier 11:30 run had advanced the remote; resolved by re cloning fresh, rebuilding overlays and picks log against current HEAD, deduplicating the slate entries, and pushing a clean fast forward
- Supporting enrichment overlays were absent as noted; no starter names were invented, all 30 came from the schedule API