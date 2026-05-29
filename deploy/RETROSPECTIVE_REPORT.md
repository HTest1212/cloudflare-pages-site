# MLB Daily Retrospective — 2026-05-28 (settled 2026-05-29)

## LOCK BREACH
**LOCK BREACH — Ohtani K over 7.5 | 2026-05-27**  
Diagnosis: Ohtani struck out 7 over 6 strong innings but the 7.5 line left zero cushion and he missed by one.  
New rule: Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.  
Rolling 14d Lock win rate: 58.6%  
Guard status: cap_active

Note: this Lock loss occurred on the 05-27 slate, which had not been settled by the prior retrospective. It was settled in this run as part of a gap fill and is treated as a fresh breach so the Lock never misses silently.

## Slate Summary

Two slates were settled this run. 05-27 carried 15 games and 38 logged picks (23 actionable primary, 15 conditional watch list items settled void). 05-28 carried 6 games and 9 firm picks. 05-26 published no picks.

05-27 actionable record: 11 W and 12 L, -2.7 units.
05-28 record: 5 W and 4 L, +0.05 units.

05-28 by market:
- ML: 3 W and 1 L, win rate 75.0%, +1.31 units
- K: 2 W and 2 L, win rate 50.0%, -0.26 units
- Total: 0 W and 1 L, win rate 0.0%, -1.0 units

05-27 actionable by tier: A tier 5 W and 1 L, B tier 5 W and 10 L, C tier 1 W and 1 L. 05-28 by tier: B tier 4 W and 4 L, C tier 1 W and 0 L. No A tier picks were published on 05-28.

## Lock Track Record

Lifetime Locks: 23 W and 13 L, win rate 63.9%, -82.21 units, ROI -15.4%.
Current streak: 4 win. Longest win streak 8, longest loss streak 6.
Rolling 14d Lock win rate: 58.6%. Rolling 30d: 63.9%.

Lock by market:
- F5_ML: 2 W and 0 L, win rate 100.0%, +1.5 units
- TotalBases: 1 W and 0 L, win rate 100.0%, +0.91 units
- ML: 4 W and 5 L, win rate 44.4%, -30.08 units
- Hits: 1 W and 0 L, win rate 100.0%, +0.5 units
- K: 7 W and 4 L, win rate 63.6%, +71.24 units
- RL: 3 W and 0 L, win rate 100.0%, +3.13 units
- Total: 2 W and 1 L, win rate 66.7%, -8.18 units
- F5: 1 W and 1 L, win rate 50.0%, -13.04 units
- Under: 1 W and 1 L, win rate 50.0%, -9.09 units
- Over: 0 W and 1 L, win rate 0.0%, -100.0 units
- F5_Total: 1 W and 0 L, win rate 100.0%, +0.91 units

Guard status: **cap_active**. The rolling 14d Lock win rate of 58.6% sits below the 80% floor, so the guard stays active. The 11:30 AM run must cap A tier publication and demote any A candidate missing 4 or more of the confirmation signals until the rolling 14d rate recovers to 85%.

## Top Three Losses With Diagnoses

- **Ohtani K over 7.5 (A tier Lock, 05-27)**: Ohtani struck out 7 over 6 strong innings; the 7.5 line left zero cushion and he missed by one. A line above the pitcher delivery on a non dominant start is the lesson.
- **Under 7 at Rate Field, MIN at CWS (B tier, 05-27)**: Seventeen combined runs in a 15 to 2 blowout obliterated the under, a full miss on the run environment read.
- **Pirates ML (B tier, 05-28)**: Pittsburgh lost 7 to 2 even though Skenes struck out 10; the offense and bullpen failed behind a dominant start, so the ML read was undone by support, not the starter.

## Rule Memory Status

Permanent rules (never expire): 4
- Never issue A-tier Under 7.0 at Oracle when the opposing starter has sub 3.50 ERA and top ... (validated 3x, first learned 2026-05-20)
- Never issue Giants ML as A-tier unless SF starting pitcher has sub 3.20 ERA AND Giants off... (validated 3x, first learned 2026-05-20)
- Cap A-tier exposure at 2 picks per game maximum. F5 Under 4 requires both starters sub 3.5... (validated 3x, first learned 2026-05-20)
- Never issue A-tier ML on any team when their offense ranks bottom third in runs scored las... (validated 3x, first learned 2026-05-20)

Rules promoted to permanent today: none.

Trial rules still accumulating evidence: 7
- [lock_breach, 1 of 3, expires 2026-06-08] Do not publish A tier F5 Under when the run suppressor is park and weather only ...
- [lock_breach, 1 of 3, expires 2026-06-08] Do not publish A tier ML relying on ERA differential alone; require FIP within 0...
- [lock_breach, 1 of 3, expires 2026-06-08] Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP ...
- [lock_breach, 1 of 3, expires 2026-06-08] Do not publish A tier ML against a starter with ERA above 4.50 when that starter...
- [lock_breach, 1 of 3, expires 2026-06-08] Do not publish A tier Over when the visiting team's rotation is starting a pitch...
- [lock_breach, 1 of 3, expires 2026-06-11] Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitch...
- [pattern, 1 of 3, expires 2026-06-04] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line ...

Rules that aged out today: none.

New rules created today: 2
- [lock_breach, expires 2026-06-11] Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.
- [pattern, expires 2026-06-04] Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.

Total rules in active memory: 4 permanent + 7 trial.

## Adjustments For Today (priority order)

1. LOCK GUARD ACTIVE: Cap A tier publication until rolling 14d Lock win rate recovers to 0.85. Demote any A tier candidate missing 4 or more of: model confidence above 80, recent form positive, lineup confirmed, weather neutral or favorable, bullpen rested, no key injury, no umpire risk flag.
2. Do not publish A tier pitcher K over at a line of 7.0 or higher unless the pitcher's season strikeouts per start exceeds the posted line by at least 1.5; a strong but not dominant 7 strikeout start must still clear with cushion.
3. Do not publish A tier F5 Under when the run suppressor is park and weather only — require starter ERA below 3.50 and opposing lineup ranked bottom 5 NL in runs scored.
4. Do not publish A tier ML relying on ERA differential alone; require FIP within 0.50 of ERA and at least 3 consecutive quality starts before classifying as starter edge.
5. Do not publish A tier Under at Oracle Park when the visiting pitcher has a WHIP above 1.30 in last 5 starts regardless of wind magnitude.
6. Do not publish A tier ML against a starter with ERA above 4.50 when that starter has allowed 2 or fewer runs in 2 of his last 3 starts regardless of season ERA.
7. Do not publish A tier Over when the visiting team's rotation is starting a pitcher with an ERA above 6.00 but the bullpen ERA is below 3.80; the pen can neutralize the starter damage and suppress the run total.
8. Require the pitcher trailing 5 start strikeout rate to exceed the posted K line before publishing a K over, and cap K over stake at half a unit when the line is above the pitcher season average.

## Lifetime And Recent 14 Day KPIs

Lifetime: 488 W and 383 L, win rate 56.0%, +921.69 units, ROI 10.8%.
Recent 14 day: 158 W and 125 L, win rate 55.8%, +888.83 units, ROI 11.2%.

## Data Notes

- Git sync: sparse clone of origin succeeded. picks_log.json pulled from origin (authoritative).
- Mount access: the local working folder was unreachable this session (Resource deadlock from bash, EPERM from file tools). All inputs were read from the origin clone and all outputs were written directly into the clone for push. The local working folder copies could not be refreshed.
- Base outcomes_log from origin was current through 05-25. 05-26 had no picks. 05-27 and 05-28 were unsettled and settled here. No data was overwritten; settlement is ID based upsert.
- All 21 games across both slates were Final with complete box scores. Pitcher strikeout totals confirmed from box score pitching lines.