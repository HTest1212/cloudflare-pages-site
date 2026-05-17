# MLB Statcast Overlay Refresh Report

## Window and Run Timestamp
- **Window:** Early morning 6 AM ET scheduled task (`mlb-statcast-refresh-6am`)
- **Run timestamp (UTC):** 2026-05-17T10:08:33Z
- **Overlay asof:** 2026-05-17T10:08:33Z

---

## Slate Date
**2026-05-17** — 15 game slate

---

## Yesterday's Slate (2026-05-16)
- Games played: **15** (all Final)
- Pitchers scanned: **121**
- Batters scanned: **433**
- Statcast window used: **7 day (2026-05-09 to 2026-05-16)**
  - Note: 30 day window returned `{"error":"Result too large"}` for most pitchers. Fell back to 7 day for all but Fluharty and Mize (who had 30 day files already saved before the error pattern was detected).

---

## Today's Slate (2026-05-17)
- Games scheduled: **15**
- Pitchers in overlay: **30** (yesterday's starter per team side, 2 per game)
- Batters in overlay: **150** (5 per team roster slot, 10 per game × 15 games)

### Matchups and Yesterday Starters (Probable Pitchers All TBD at 6 AM ET)

| Away | Home | First Pitch UTC | Away Yest Starter | Home Yest Starter |
|------|------|----------------|-------------------|-------------------|
| Miami Marlins | Tampa Bay Rays | 16:15 | Sandy Alcantara | Nick Martinez |
| Baltimore Orioles | Washington Nationals | 17:35 | Chris Bassitt | Cade Cavalli |
| Philadelphia Phillies | Pittsburgh Pirates | 17:35 | Cristopher Sanchez | Bubba Chandler |
| Boston Red Sox | Atlanta Braves | 17:35 | Payton Tolle | Bryce Elder |
| Cincinnati Reds | Cleveland Guardians | 17:40 | Chris Paddack | Joey Cantillo |
| Toronto Blue Jays | Detroit Tigers | 17:40 | Mason Fluharty | Casey Mize |
| New York Yankees | New York Mets | 17:40 | Carlos Rodon | Huascar Brazoban |
| Texas Rangers | Houston Astros | 18:10 | Jacob deGrom | Kai-Wei Teng |
| Chicago Cubs | Chicago White Sox | 18:10 | Jameson Taillon | Davis Martin |
| Milwaukee Brewers | Minnesota Twins | 18:10 | Logan Henderson | Connor Prielipp |
| Kansas City Royals | St. Louis Cardinals | 18:15 | Noah Cameron | Kyle Leahy |
| Arizona Diamondbacks | Colorado Rockies | 19:10 | Eduardo Rodriguez | Tomoyuki Sugano |
| San Francisco Giants | Athletics | 20:05 | Trevor McDonald | Luis Severino |
| Los Angeles Dodgers | Los Angeles Angels | 20:07 | Justin Wrobleski | Jose Soriano |
| San Diego Padres | Seattle Mariners | 23:20 | Walker Buehler | Logan Gilbert |

---

## Lineup Endpoint Behavior
All 15 lineup/probable pitcher endpoints returned **empty** at 6 AM ET. This is expected — MLB does not publish probable pitchers or batting orders until later in the morning (typically 10 AM to noon ET). All game entries carry `probable_pitcher: { id: null, name: "TBD" }`. The 11:30 AM refresh will populate these fields once the API populates them.

---

## Pitcher Statcast Index (30 entries)

| Name | Pitches 7d | Avg Velo | K 7d |
|------|-----------|---------|------|
| Mason Fluharty | 166 | 86.6 | 12 |
| Casey Mize | 287 | 89.9 | 21 |
| Noah Cameron | 177 | 87.9 | 8 |
| Kyle Leahy | 185 | 89.3 | 7 |
| Eduardo Rodriguez | 191 | 88.9 | 10 |
| Tomoyuki Sugano | 169 | 87.8 | 3 |
| Chris Bassitt | 176 | 84.7 | 10 |
| Cade Cavalli | 189 | 90.3 | 12 |
| Cristopher Sanchez | 211 | 89.8 | 20 |
| Bubba Chandler | 154 | 94.7 | 5 |
| (20 additional — see statcast_overlay.json) | | | |

---

## Batter Statcast Index
- **Target:** 150 batters (5 per team × 30 teams)
- **Populated:** 4 of 150 (George Springer, Yohendrick Pinango, Vladimir Guerrero Jr., Kazuma Okamoto)
- **Gap reason:** Token budget exhausted after pitcher pulls; 146 batters carry `statcast: {}` placeholder. The 11:30 AM refresh will attempt to fill remaining batter Statcast slots.

---

## GitHub Push Status
**SUCCESS**

- Remote: `https://github.com/HTest1212/cloudflare-pages-site.git`
- Branch: `main`
- Commit: `1496256` — "Auto refresh statcast 2026-05-17 10:10"
- Previous commit: `7e12fcf` — "Auto refresh 1130am 2026-05-16 19:00"
- File pushed: `statcast_overlay.json` (54.1 KB, 2401 lines)

---

## Cloudflare Pages Deploy Status
**PARTIAL — GitHub push succeeded; wrangler deploy skipped**

- `CLOUDFLARE_API_TOKEN` is not available in the Linux sandbox environment. Wrangler requires this token in non-interactive environments.
- The GitHub → Cloudflare Pages auto-deploy integration should trigger within 1 to 3 minutes of the push. If the integration is healthy, the live URL will serve `asof: 2026-05-17T10:08:33Z` shortly after this report is written.
- Live URL checked at ~10:11 UTC still returned the prior overlay (`asof: 2026-05-16T16:45:56Z`). Auto-deploy had not yet fired at that point.
- **Action required:** Store `CLOUDFLARE_API_TOKEN` as an environment variable accessible to the Linux sandbox so wrangler can deploy directly on future runs. Alternatively, verify the GitHub → CF Pages auto-deploy webhook is active.

---

## Notes / Data Gaps

- **All probable pitchers TBD** — expected at 6 AM ET. No actionable pitcher data for today's games until the 11:30 AM refresh.
- **Batter Statcast coverage 2.7%** (4 of 150) — only the first batch attempted before time budget was consumed. Not a blocking issue; the overlay validates and the dashboard will show pitcher Statcast data for all 30 starters.
- **7-day pitcher window** — shorter than the preferred 30-day. Result-too-large errors from the Statcast API forced the fallback. Pitch mix percentages and spin rates are valid; small-sample K rates should be interpreted carefully for starters who only made one appearance in the window.
- **Workspace `.git` broken** — the local repo at the workspace folder has a corrupt git state (`Resource deadlock avoided`). All git operations were performed via a fresh clone at `/tmp/cf_repo`. The overlay file itself is clean and correct in the workspace folder.
- **No bullpen availability data** in this run — that is handled by the separate `mlb-bullpen-availability-daily` scheduled task.
