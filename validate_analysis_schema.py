#!/usr/bin/env python3
"""
Deploy gate for the MLB dashboard 11:30 AM refresh.

Parses CLAUDE_DAILY_ANALYSIS out of index.html and asserts that every game card
exposes the EXACT fields the page renderer (buildDeepAnalysis in index.html) reads.
The renderer fails silently to defaults (0/100, 0.0 - 0.0, "No strong edges") when a
field name does not match, so a card can look populated while grade, score and verdict
are dead. This script reproduces the renderer's field resolution and fails the deploy
if any graded card would render a zero grade, zero score, or empty verdict.

Usage:  python3 validate_analysis_schema.py /path/to/index.html
Exit 0 = pass, exit 1 = one or more cards would render broken. Print every failure.
"""
import sys, json, re

def extract(src):
    m = "const CLAUDE_DAILY_ANALYSIS = "
    i = src.find(m)
    if i < 0:
        raise SystemExit("FAIL: CLAUDE_DAILY_ANALYSIS not found in index.html")
    start = src.find("{", i)
    depth = 0
    for j in range(start, len(src)):
        c = src[j]
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return json.loads(src[start:j+1])
    raise SystemExit("FAIL: could not brace-match CLAUDE_DAILY_ANALYSIS")

def num(x):
    try:
        f = float(x)
        return f if f == f else None  # reject NaN
    except Exception:
        return None

def resolve_score(c):
    g = c.get("grade") or {}
    s = num(g.get("score"))
    if s is None:
        s = num((c.get("confidence") or {}).get("score"))
    return s

def resolve_letter(c):
    g = c.get("grade") or {}
    l = g.get("letter") or (c.get("confidence") or {}).get("letter")
    return l

def resolve_proj(c):
    v = c.get("verdict") or {}
    a, h = num(v.get("projAway")), num(v.get("projHome"))
    if a is None or h is None:
        ps = c.get("projected_score")
        if isinstance(ps, str):
            mm = re.search(r"(\d+(?:\.\d+)?)\s*[\.•·—\-]\s*(\d+(?:\.\d+)?)", ps)
            if mm: a, h = num(mm.group(1)), num(mm.group(2))
        elif isinstance(ps, dict):
            a, h = num(ps.get("away")), num(ps.get("home"))
    return a, h

def resolve_verdict_text(c):
    v = c.get("verdict") or {}
    return (v.get("text") or v.get("prose") or "").strip()

def resolve_chips(c):
    v = c.get("verdict") or {}
    ch = v.get("chips")
    if ch is None: ch = v.get("bets")
    return ch

def main():
    if len(sys.argv) < 2:
        raise SystemExit("usage: validate_analysis_schema.py <index.html>")
    path = sys.argv[1]
    src = open(path).read()

    # render functions must survive the splice
    for fn in ["renderClaudePicksBlock", "tierFromProb", "renderBestBetsBlock", "buildDeepAnalysis"]:
        if fn not in src:
            raise SystemExit("FAIL: render function missing after splice -> " + fn)

    a = extract(src)
    fails = []
    if not a.get("date"):
        fails.append("top level: missing `date` (card only renders when date === today)")

    games = a.get("games") or {}
    if not games:
        fails.append("top level: games object is empty")

    ACTIVE = {"preview", "scheduled", "pre-game", "pregame", "warmup", ""}
    for pk, c in games.items():
        status = str(c.get("status", "")).lower()
        # closed games legitimately carry no writeup
        if status in {"final", "postponed", "completed early", "game over"}:
            continue
        score = resolve_score(c)
        if score is None or score <= 0:
            fails.append(f"{pk}: grade score resolves to {score} (need grade.score or confidence.score > 0)")
        letter = resolve_letter(c)
        if not letter or str(letter).strip() in {"", "—", "-"}:
            fails.append(f"{pk}: grade letter resolves to {letter!r} (need grade.letter or confidence.letter)")
        pa, ph = resolve_proj(c)
        if pa is None or ph is None or (pa <= 0 and ph <= 0):
            fails.append(f"{pk}: projected score resolves to {pa} - {ph} (need verdict.projAway/projHome or projected_score)")
        vt = resolve_verdict_text(c)
        if not vt:
            fails.append(f"{pk}: verdict text empty (need verdict.text or verdict.prose)")
        chips = resolve_chips(c)
        if chips is None:
            fails.append(f"{pk}: verdict.chips missing (need verdict.chips array, may be [] for Pass)")
        paras = c.get("paragraphs")
        if not isinstance(paras, list) or len(paras) < 4:
            fails.append(f"{pk}: paragraphs has {0 if not isinstance(paras,list) else len(paras)} entries (need >= 4)")
        picks = c.get("picks")
        if not isinstance(picks, list) or len(picks) < 5:
            fails.append(f"{pk}: picks has {0 if not isinstance(picks,list) else len(picks)} entries (need >= 5)")

    if fails:
        print("SCHEMA GATE FAILED ({} issue(s)):".format(len(fails)))
        for f in fails:
            print("  - " + f)
        sys.exit(1)
    print("SCHEMA GATE PASSED: {} games, all renderer fields resolve.".format(len(games)))
    sys.exit(0)

if __name__ == "__main__":
    main()
