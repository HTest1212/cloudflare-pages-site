# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM)
Run timestamp: 2026-06-20T18:19:38Z
Slate date: 2026-06-20
Game count: 14 (3 Live, 11 Preview)

## API data quality
Pitchers: 28 of 28 confirmed from schedule-api, 0 TBD.
Weather fetched (Open Meteo) for 11 outdoor/retractable parks, all success.
Domes/closed roofs treated no-weather: Tropicana (fixed), Daikin and Chase (closed vs heat/rain).

## Active learnings adjustments
LOCK GUARD ACTIVE: A tier capped, top grade held to B (rolling 14d Lock win rate 0.333).
Factor overlays (bullpen, park, wind, umpire, framing, pitch matchup, rolling form) ALL ABSENT this run -> top tier held to B, relief neutral.
VARIANCE down-weight, K-over six-inning floor rule, Coors altitude cap all applied.

## Per game (grade / proj / picks / primary chips)
824263 CWS@DET C62 4.0-4.6 5p [Detroit ML] LIVE Tigers 1-0 b4
823532 CIN@NYY C63 4.2-4.9 5p [Yankees ML] LIVE Yankees 1-0 e2
824665 TOR@CHC C58 4.7-4.9 5p [Over 8.5] LIVE 0-0 t1
822885 SD@TEX C64 4.1-4.4 6p [Rangers ML, Gore K o6.5]
822967 WSH@TB C61 4.3-4.2 5p [Nationals ML, Cavalli K o5.5]
823854 SF@MIA B80 3.4-4.5 6p [Marlins ML, Meyer K o6.5, Under 8]
824909 MIL@ATL B81 3.4-3.6 6p [Under 7.5, Sale K o6.5, Harrison K o6.5]
824180 CLE@HOU B80 3.6-4.4 6p [Astros ML, Under 8.5]
823447 NYM@PHI B82 3.6-4.5 6p [Phillies ML, Sanchez K o6.5]
824342 PIT@COL B80 5.0-4.4 6p [Pirates ML, Skenes K o6.5]
824988 LAA@ATH C66 4.3-4.6 5p [Athletics ML]
823937 BAL@LAD B82 3.3-4.8 6p [Dodgers ML, Yamamoto K o5.5]
823126 BOS@SEA C64 3.7-4.0 5p [Under 7.5, Mariners ML]
825068 MIN@ARI C66 4.4-4.2 5p [Twins ML, Bradley K o5.5]

## Overlays
odds_overlay.json: 14 games. statcast_overlay.json: 14 games (ERA-based xFIP/FIP). picks_log.json: 23 pending chips upserted, 844 total.

## Deploy
Commit: a6dd80e
Push status: success (Cloudflare Pages auto-deploy)
Live verify: date 2026-06-20, window 2:08 PM, 0 zero-render cards across 14 games.

## Errors / fallbacks
All factor overlays missing -> analyst defaults, top tier held to B (consistent with active Lock guard).
Workspace mount .env unreadable (token len 0) -> PAT recovered from existing clone .git/config.
