# Monthly Report Automation

On the first day of each month, this automation summarizes cards that first reached `main` during the previous calendar month. The same workflow also supports manual refreshes for any explicit month, so maintainers can regenerate an in-progress or historical report without creating a second file for that month. It opens a bilingual report PR for human review and never merges it.

## Data flow

```text
first-parent history of main
  -> cards added during YYYY-MM
  -> manifest with First appeared, status, Topics, Domains, and card evidence
  -> canonical English synthesis
  -> Chinese translation with restrained Dongbei-explainer logic
  -> adversarial review-and-improve pass on the bilingual pair
  -> independent Chinese naturalness review
  -> deterministic completeness/link/parity/structure validation
  -> review-only PR
```

The assignment rule and the date stamp answer different questions:

- The main-branch addition month decides which report contains the card.
- `First appeared` records when the work itself first became publicly accessible.
- Matching months produce `New release` / `当月新发布`; all other dates produce `Backfill` / `历史补录`.

The initial archive is bootstrapped separately: existing cards with public first appearances from January 2024 onward are grouped by that first-appearance month. Cards from 2023 or earlier receive no historical monthly report. This exception does not change the rule for future incremental reports.

## Refresh semantics

Each month owns exactly one canonical report pair:

- `monthly/YYYY-MM.md`
- `zh/monthly/YYYY-MM.md`

Scheduled and manual runs both regenerate those same files. A later run for the same month refreshes the existing report in place and updates the same month-specific PR branch when it is still open. The automation never creates `YYYY-MM-2.md`, alternate copies, or parallel monthly-report files for the same month.

## Editorial balance

The narrative is selective, but `Complete Monthly Index` is exhaustive. The writer expands only story lines, Topics, and Domains that carry a real monthly development. Each work receives one primary narrative treatment; cross-links expose other taxonomy membership without repeating its summary.

English and Chinese use the same explanatory logic: identify the older path, show which step changed, connect the evidence to the insight, and state the boundary. Only Chinese uses restrained, broadly understandable Northeastern conversational rhythm. Dialect performance, obscure vocabulary, jokes, and persona imitation are prohibited.

The adversarial reviewer exists because monthly reports fail in ways a style prompt alone will not catch: counted structures that never reach the promised third item, category boundaries that drift mid-paragraph, conclusions that outrun the cited cards, or a topic section that sounds plausible but never cashes out its own framing. The reviewer is expected to cut or rewrite those claims, not merely comment on them.

## Commands

```bash
python3 scripts/monthly_report.py prepare --month 2026-08
python3 scripts/monthly_report.py generate --month 2026-08 --force
python3 scripts/monthly_report.py validate --month 2026-08
python3 scripts/monthly_report.py validate-all
python3 scripts/monthly_report.py index
```

Between month-end regenerations, every card that reaches `main` still needs a row in that month's `Complete Monthly Index`, or `validate-all` fails on `main` and blocks the daily updater. `sync-index` appends the missing rows (English and Chinese, domains read from the domain pages) without touching existing rows or the narrative; `check-pending` reports them without writing. Both default to the current month, and `--base REF` also counts the cards a branch adds relative to `REF`:

```bash
python3 scripts/monthly_report.py sync-index --base origin/main
python3 scripts/monthly_report.py check-pending --base origin/main
```

The daily updater runs `sync-index` before its final validation, and the pull-request gate runs `check-pending` against the PR's base, so a card PR that forgets the row fails before merge.

`generate` requires `CLAUDE_CODE_OAUTH_TOKEN`. Passing `--force` regenerates the canonical file for that month in place, which is how both scheduled reruns and manual refreshes avoid creating duplicate monthly reports. The scheduled workflow runs at 06:17 America/Los_Angeles on day 1, after the regular knowledge-update wake-up window.
