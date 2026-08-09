#!/usr/bin/env bash
# Finalize: commit the batch onto the rolling branch (already checked out) and open/update ONE
# pull request. NEVER merges. Runs only when the deterministic final gate passed.
set -euo pipefail

ROLLING="auto/knowledge-update"
TITLE="Automated knowledge update"
LABEL="automated-update"
BODY_FILE="runtime/pr_body.md"

git config user.name  "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

# Stage ONLY publishable knowledge-base paths — never runtime/, scripts/, workflows, transcripts.
git add works zh topics domains activities README.md 2>/dev/null || true

if git diff --cached --quiet; then
  echo "No knowledge-base changes to commit; not opening/updating a PR."
  exit 0
fi

DATE="$(date -u +%Y-%m-%d)"
git commit -q -m "auto(update): knowledge batch ${DATE}

Verified English work cards added, English knowledge axes integrated, Chinese mirror
synchronized and independently reviewed. Opened for human review — never auto-merged."
git push origin "HEAD:$ROLLING"

gh label create "$LABEL" --color 1f6feb --description "Automated daily knowledge update" 2>/dev/null || true
PR_NUM="$(gh pr list --head "$ROLLING" --state open --json number --jq '.[0].number' 2>/dev/null || true)"
if [ -n "${PR_NUM:-}" ] && [ "${PR_NUM}" != "null" ]; then
  gh pr edit "$PR_NUM" --body-file "$BODY_FILE" || true
  echo "Updated existing automated PR #$PR_NUM"
else
  gh pr create --base main --head "$ROLLING" --title "$TITLE" --body-file "$BODY_FILE" --label "$LABEL"
  echo "Opened automated PR from $ROLLING"
fi
