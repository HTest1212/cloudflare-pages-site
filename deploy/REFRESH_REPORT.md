# MLB Dashboard Refresh Report

Window: early afternoon (2:08 PM)
Run timestamp (UTC): 2026-06-25T20:55Z
Commit: fbee4a00c9cc1ec4ed5a8c7e01b89bf0430316a8
Push status: success, Cloudflare Pages auto deploy verified live

## Slate
Slate date: 2026-06-25
Game count: 9 (2 Final closed, 1 Live, 6 Preview)

IMPORTANT DATA NOTE: The schedule hydrate endpoint returned a stale 2026-06-24
slate (16 Final games) whenever any hydrate token was attached. The clean no hydrate
query returned the true 9 game 2026-06-25 bucket, and probable pitchers plus lineups
were pulled per game from the v1.1 live feed endpoint, which was not poisoned. All
cards are built from the verified 2026-06-25 data.

## API data quality
Pitchers: 14 confirmed via live feed and people stats endpoint, 0 TBD on active games.
Notable small samples flagged: Troy Melton (31.2 IP, 5 GS), Matthew Boyd (24 IP, 5 GS),
Tatsuya Imai (41 IP rookie). All triggered STARTER_REGRESSION downweighting.
Weather: 6 of 6 outdoor parks fetched successfully from Open Meteo (DET, WSH, TOR, NYM, BOS, STL).

## Per game summary
824258 HOU @ DET | C 62 | proj 3.7 - 4.4 | 6 picks | chips: Under 9, Tigers ML, Imai K over 5.5
822717 PHI @ WSH | B 78 | proj 5.0 - 3.4 | 6 picks | chips: Phillies ML, Sanchez K over 5.5, Phillies F5 ML
822797 TEX @ TOR | B 73 | proj 3.4 - 3.9 | 7 picks | chips: Under 8.5, Gausman K over 5.5, Blue Jays ML
823612 CHC @ NYM | C 60 | proj 4.7 - 4.0 | 6 picks | chips: Cubs ML, Over 8.5, Peralta K over 5.5
824747 NYY @ BOS | B 78 | proj 5.0 - 3.5 | 6 picks | chips: Yankees ML, Schlittler K over 5.5, Yankees F5 ML
823042 AZ @ STL | B 70 | proj 4.3 - 4.9 | 6 picks | chips: Cardinals ML, Over 9, Cardinals F5 ML
823209 ATH @ SF | C 58 Live | proj 3.6 - 3.8 | 6 picks | locked chip: Under 8 (scoreless early, tracking)
822961 KC @ TB | Final, Tampa Bay won 13 to 2
823366 SEA @ PIT | Final, Pittsburgh won 5 to 1

## Overlay rebuilds
odds_overlay.json: 7 active and live games (moneyline, total, runline)
statcast_overlay.json: 7 games, ERA based xFIP and FIP estimates per pitcher
picks_log.json: 18 primary chips appended for the 6 Preview games, total 1020 entries, idempotent upsert

## Learnings adjustments applied
Top tier held to B (park, umpire, framing overlays absent).
VARIANCE downweight active, extra confirming signal required above C.
STARTER_REGRESSION downweight applied to Melton, Boyd, Imai.
Under blocked when both lineups top 12 in trailing runs: enforced on PHI @ WSH and AZ @ STL.
Projected lineup cap (B plus): applied to HOU @ DET away, CHC @ NYM both, AZ @ STL away.
Road ML favorite under seven innings cleared only with rested high leverage pen: NYY @ BOS passed (Bednar, Cruz rested).
No A tier published, Lock posture conservative.

## Errors and fallbacks
Stale hydrate slate detected and bypassed (see data note above).
Original /tmp clone was root owned and read only; rebuilt a self owned clone at /tmp/cf_work for the write and push.
No other errors. Schema gate passed (9 games), all four render functions intact, zero hyphens in writeup text.
