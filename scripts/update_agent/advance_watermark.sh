#!/usr/bin/env bash
# Advance the durable discovery watermark on the dedicated `auto/updater-state` branch, using git
# plumbing (no checkout/worktree): the branch holds ONLY watermark.json. Called on production
# success (a legitimate PR, or a successful no-op). Failed runs never call this.
set -euo pipefail
TS="${1:?ISO timestamp required}"
BR="auto/updater-state"

git config user.name  "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git fetch origin "$BR" 2>/dev/null || true

BLOB="$(printf '{"last_success":"%s"}\n' "$TS" | git hash-object -w --stdin)"
TREE="$(printf '100644 blob %s\twatermark.json\n' "$BLOB" | git mktree)"
if git rev-parse --verify "origin/$BR" >/dev/null 2>&1; then
  COMMIT="$(git commit-tree "$TREE" -p "origin/$BR" -m "watermark: $TS")"
else
  COMMIT="$(git commit-tree "$TREE" -m "watermark: $TS")"   # first time: orphan commit, file only
fi
git push origin "$COMMIT:refs/heads/$BR"
echo "watermark advanced to $TS on $BR"
