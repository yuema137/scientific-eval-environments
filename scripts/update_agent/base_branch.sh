#!/usr/bin/env bash
# Check out the single rolling automated-update branch so a run accumulates on top of any prior
# unmerged batch (spec §14) rather than basing on main and dropping yesterday's pending work.
# Untracked files (e.g. runtime/) survive the switch.
set -euo pipefail
ROLLING="auto/knowledge-update"
git fetch origin "$ROLLING" 2>/dev/null || true
if git rev-parse --verify "origin/$ROLLING" >/dev/null 2>&1; then
  git checkout -B "$ROLLING" "origin/$ROLLING"
  echo "based on existing rolling branch $ROLLING"
else
  git checkout -B "$ROLLING"
  echo "created rolling branch $ROLLING from base"
fi
