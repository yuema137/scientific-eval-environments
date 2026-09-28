#!/usr/bin/env bash
# Reuse pending work only while its PR is open; a merged PR's branch is historical state.
set -euo pipefail
ROLLING="auto/knowledge-update"
git fetch origin main
REMOTE_REF="refs/remotes/origin/$ROLLING"
REMOTE_SHA="$(git ls-remote --heads origin "refs/heads/$ROLLING" | cut -f1)"
if [ -z "$REMOTE_SHA" ]; then
  git checkout -B "$ROLLING" origin/main
  echo "created $ROLLING from current main"
  exit 0
fi
git fetch origin "refs/heads/$ROLLING:$REMOTE_REF"
# Fail on API errors instead of mistaking inaccessible PR state for an empty queue.
OPEN_PR="$(gh pr list --head "$ROLLING" --base main --state open --json number --jq '.[0].number')"
if [ -n "$OPEN_PR" ] && [ "$OPEN_PR" != null ]; then
  git checkout -B "$ROLLING" "$REMOTE_REF"
  # Keep pending additions, but never run old scripts against a newer main silently.
  git -c user.name=github-actions\[bot\] -c user.email=41898282+github-actions\[bot\]@users.noreply.github.com \
    merge --no-edit origin/main
  echo "preserved pending PR #$OPEN_PR and integrated current main"
else
  MERGED_HEAD="$(gh pr list --head "$ROLLING" --base main --state merged --limit 1 --json headRefOid --jq '.[0].headRefOid')"
  if [ "$MERGED_HEAD" != "$REMOTE_SHA" ]; then
    echo "::error::Rolling branch has no open PR and its tip is not a verified merged PR; inspect it before reuse."
    exit 1
  fi
  git checkout -B "$ROLLING" origin/main
  # The old tip was already reviewed and merged (possibly squashed). Preserve only its ancestry
  # so publication remains a normal fast-forward push; retain main's exact content.
  git -c user.name=github-actions\[bot\] -c user.email=41898282+github-actions\[bot\]@users.noreply.github.com \
    merge -s ours --no-edit "$REMOTE_REF"
  echo "started from current main; retained ancestry of the already-merged rolling PR"
fi
