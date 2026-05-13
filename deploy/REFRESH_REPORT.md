# MLB Dashboard Refresh Report

Window: midday (11:30 AM)
Run timestamp UTC: 2026-05-13T01:00:08Z
Slate date: 2026-05-12

## Slate summary
Total games: 15
In progress: 13
Pre Game: 2
Final or Postponed: 0

## Live games (verdicts locked)
- Angels at Guardians (824442) — Live T9, CLE 3, LAA 2
- Yankees at Orioles (824843) — Live T9, NYY 7, BAL 2
- Nationals at Reds (824521) — Live B7, WAS 7, CIN 2
- Rockies at Pirates (823385) — Live B8, PIT 3, COL 0
- Phillies at Red Sox (824764) — Live T9, PHI 2, BOS 1
- Rays at Blue Jays (822817) — Live B6, TB 4, TOR 0
- Tigers at Mets (823632) — Live M6, NYM 3, DET 2
- Cubs at Braves (824927) — Live B6, ATL 5, CHC 2
- Royals at White Sox (824604) — Live B5, KC 2, CWS 1
- Marlins at Twins (823712) — Live T6, MIN 3, MIA 0
- Padres at Brewers (823790) — Live M5, MIL 6, SD 2
- Diamondbacks at Rangers (822903) — Live M4, TEX 2, ARI 1
- Mariners at Astros (824197) — Live B3, SEA 2, HOU 1

## Pre Game cards
- Cardinals at Athletics (825011)
- Giants at Dodgers (823951)

## Spotlight pick
- ROC at PIR | ML Pirates ML -195 to -215  | tier B | conf 82
  reasoning: Skenes elite vs Rockies bats at a pitcher park is the cleanest pitching edge on the slate.

## ML coverage
ML primary chips: 14
F5 ML primary chips: 1
Hits primary chips: 15
Under primary chips: 1
Over primary chips: 5
K primary chips: 4
Watch List ML leans: 1
Watch List F5 ML leans: 14
Watch List Hits leans: 13

## Adjustments applied today
- (2 cards) Avoid Under total picks at Toronto, Coors, Dodger Stadium, and any park factor 105+ when both lineups carry 15 day OPS above .770.
- (0 cards) Do not stack Over leans when both starters carry season ERA under 3.50 even with hitter friendly conditions.
- (0 cards) Cap F5 Under confidence when opposing starter has allowed 4+ ER in any of last 3 starts OR park HR factor exceeds 105.
- (0 cards) Drop ML confidence by 5 when laying -140 or worse and opposing starter has K9 above 9 with sub 3.50 ERA in last 30 days.
- (0 cards) Skip NRFI leans when home starter has allowed 1+ ER in first inning in 3 of last 5 starts.
- (0 cards) Cap Hits over 0.5 props to confirmed lineup leadoff/2 hole hitters with at least 4 expected at bats and recent 7 day batting average over 0.260.
- (0 cards) Validate every Hitter prop pick by checking the player ID against the gamePk team roster from the MLB API before publishing.
- (0 cards) Tighten Hits prop selection to hitters with rolling 14 day OBP above .340 and project a strong matchup, since 0.5 hits at minus 115 needs more than narrative.
- (0 cards) Cap F5 ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- (1 cards) Do not lay more than minus 175 on F5 ML when chosen starter has a single previous start with at least 3 ER allowed in last 14 days.
- (3 cards) Cap F5 ML and ML confidence at 60 when opposing starter has K rate above 25 percent or recent ERA under 3.50.
- (0 cards) Lower ML confidence by 5 when home dog price beats plus 110 and starter ERA delta vs opposing starter is under 1.00.

## What was refreshed
- 13 live game cards: status set to live, inning and score note appended, morning verdicts locked in place
- 2 pre game cards (Cardinals at Athletics, Giants at Dodgers): cards preserved from morning run, status retained
- lastUpdated stamp refreshed
- window field set to midday (11:30 AM)

## API reachability
- statsapi.mlb.com: reachable, returned schedule and linescores for all 15 games
- api.open-meteo.com: not called this run (pre game cards preserved; weather already captured this morning)

## Validation
- Inline script node --check: PASS (both scripts)
- CLAUDE_DAILY_ANALYSIS parsed as valid JSON: PASS

## Notes
- Run executed late vs the scheduled 11:30 AM window because of trigger timing.
- Default behavior preserved: morning verdicts locked, no rewriting of live cards.
- picks_log.json: 81 entries already recorded for 2026-05-12 from the morning run, no new appends needed.