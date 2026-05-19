#!/bin/bash
# ============================================================
# MLB Dashboard — Push + Deploy
# Double-click in Finder to run.
# Pushes to GitHub. GitHub Actions auto-deploys to Cloudflare Pages.
# ============================================================
set -euo pipefail

WORK_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$WORK_DIR/deploy/push_deploy.log"
mkdir -p "$WORK_DIR/deploy"
exec > >(tee -a "$LOG") 2>&1

echo ""
echo "=== MLB Dashboard Push + Deploy  $(date '+%Y-%m-%d %H:%M:%S %Z') ==="
echo "Working dir: $WORK_DIR"
cd "$WORK_DIR"

# ── Step 1: Run today's inject script if present ─────────────────────────────
INJECT=$(ls -t inject_*.py 2>/dev/null | head -1 || true)
if [ -n "$INJECT" ]; then
  echo ""
  echo "Step 1: Running $INJECT ..."
  python3 "$INJECT" && echo "  Inject OK" || { echo "  ERROR: inject failed"; exit 1; }
else
  echo "Step 1: No inject script found — using current index.html"
fi

# ── Step 2: Get GitHub token ─────────────────────────────────────────────────
GITHUB_TOKEN=""

# Try .env file first
if [ -f "$WORK_DIR/.env" ]; then
  GITHUB_TOKEN=$(grep -E '^GITHUB_TOKEN=' "$WORK_DIR/.env" | head -1 | cut -d= -f2- | tr -d '"'"'" || true)
fi

# Fallback: built-in token (rotates via rotate-github-pat task)
if [ -z "$GITHUB_TOKEN" ]; then
  GITHUB_TOKEN=""  # set via .env GITHUB_TOKEN
fi

# ── Step 3: Git commit and push ───────────────────────────────────────────────
echo ""
echo "Step 2: Git push to origin/main ..."

git config user.email "tathoughtleaders@gmail.com" 2>/dev/null || true
git config user.name "Claude MLB Bot" 2>/dev/null || true
git remote set-url origin "https://HTest1212:${GITHUB_TOKEN}@github.com/HTest1212/cloudflare-pages-site.git"

git add index.html picks_log.json \
  outcomes_log.json learnings.json bet_record_summary.json \
  retrospective_history.json locks_log.json \
  deploy/RETROSPECTIVE_REPORT.md 2>/dev/null || true

if git diff --cached --quiet 2>/dev/null; then
  echo "  No staged changes — files already match HEAD. Forcing a push anyway."
  git commit --allow-empty -m "Deploy ping $(date '+%Y-%m-%d %H:%M')"
else
  FILE_DATE=$(python3 -c "
import re
with open('index.html') as f: c = f.read()
m = re.search(r'\"runDate\":\s*\"([^\"]+)\"', c)
print(m.group(1) if m else 'unknown')
" 2>/dev/null || echo "unknown")
  git commit -m "Auto deploy $(date '+%Y-%m-%d %H:%M') runDate $FILE_DATE"
  echo "  Committed runDate=$FILE_DATE"
fi

git pull --rebase "https://HTest1212:${GITHUB_TOKEN}@github.com/HTest1212/cloudflare-pages-site.git" main 2>&1 | tail -3 || true
git push "https://HTest1212:${GITHUB_TOKEN}@github.com/HTest1212/cloudflare-pages-site.git" main 2>&1
echo "  Push OK"

# ── Step 4: Wait for GitHub Actions to deploy to Cloudflare Pages ────────────
echo ""
echo "Step 3: Waiting 90 seconds for GitHub Actions deploy ..."
sleep 90

echo ""
echo "Step 4: Verifying live site ..."
LIVE_DATE=$(curl -sf "https://mlb-betting-dashboard-v2.pages.dev" 2>/dev/null \
  | python3 -c "
import sys, re
c = sys.stdin.read()
m = re.search(r'\"runDate\":\s*\"([^\"]+)\"', c)
print(m.group(1) if m else 'not found')
" 2>/dev/null || echo "fetch failed")

LOCAL_DATE=$(python3 -c "
import re
with open('index.html') as f: c = f.read()
m = re.search(r'\"runDate\":\s*\"([^\"]+)\"', c)
print(m.group(1) if m else 'unknown')
" 2>/dev/null || echo "unknown")

echo "  Local index.html runDate: $LOCAL_DATE"
echo "  Live site runDate:        $LIVE_DATE"

if [ "$LIVE_DATE" = "$LOCAL_DATE" ]; then
  echo "  VERIFIED: live site matches local"
else
  echo "  Note: site may still be propagating. Check https://mlb-betting-dashboard-v2.pages.dev in 60s"
fi

echo ""
echo "=== DONE ==="
echo "    Live: https://mlb-betting-dashboard-v2.pages.dev"
echo "    Log:  $LOG"
