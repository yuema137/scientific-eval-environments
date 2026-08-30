#!/usr/bin/env bash
# Commit a validated bilingual monthly report and open a review-only PR.
set -euo pipefail

MONTH="${1:?usage: publish_monthly_report.sh YYYY-MM}"
BRANCH="auto/monthly-report-${MONTH}"
TITLE="Monthly knowledge report: ${MONTH}"
BODY_FILE="runtime/monthly-report/pr-body.md"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add monthly zh/monthly

if git diff --cached --quiet; then
  echo "No monthly-report changes to publish."
  exit 0
fi

mkdir -p "$(dirname "$BODY_FILE")"
python3 - "$MONTH" "$BODY_FILE" <<'PY'
import sys
month, path = sys.argv[1:]
body = """## Summary

- publish the bilingual monthly knowledge report for {month}
- synthesize the month's main literature shifts while retaining a complete card index
- distinguish works first released that month from older works backfilled into the repository
- run adversarial editorial review before deterministic validation so structural contradictions are fixed in the generated prose

## Validation

- monthly inclusion completeness and release/backfill classification
- English/Chinese work-set parity
- local card, Topic, and Domain links
- explicit enumeration consistency in narrative sections
- Chinese naturalness and dialect-safety constraints

This pull request was generated automatically for human review. It will not be merged automatically.
""".format(month=month)
open(path, "w").write(body)
PY

git commit -m "Add ${MONTH} monthly knowledge report"
git push --force-with-lease origin "HEAD:${BRANCH}"

PR_NUMBER="$(gh pr list --head "$BRANCH" --state open --json number --jq '.[0].number' 2>/dev/null || true)"
if [ -n "${PR_NUMBER:-}" ] && [ "$PR_NUMBER" != "null" ]; then
  gh pr edit "$PR_NUMBER" --body-file "$BODY_FILE" || true
  echo "Updated monthly report PR #${PR_NUMBER}"
else
  gh pr create --base main --head "$BRANCH" --title "$TITLE" --body-file "$BODY_FILE"
fi
