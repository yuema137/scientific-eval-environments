# Monthly Report Automation

On the first day of each month, this automation summarizes cards that first reached `main` during the previous calendar month. It opens a bilingual report PR for human review and never merges it.

## Data flow

```text
first-parent history of main
  -> cards added during YYYY-MM
  -> manifest with First appeared, status, Topics, Domains, and card evidence
  -> canonical English synthesis
  -> Chinese translation with restrained Dongbei-explainer logic
  -> independent Chinese naturalness review
  -> deterministic completeness/link/parity validation
  -> review-only PR
```

The assignment rule and the date stamp answer different questions:

- The main-branch addition month decides which report contains the card.
- `First appeared` records when the work itself first became publicly accessible.
- Matching months produce `New release` / `当月新发布`; all other dates produce `Backfill` / `历史补录`.

The initial archive is bootstrapped separately: existing cards with public first appearances from January 2024 onward are grouped by that first-appearance month. Cards from 2023 or earlier receive no historical monthly report. This exception does not change the rule for future incremental reports.

## Editorial balance

The narrative is selective, but `Complete Monthly Index` is exhaustive. The writer expands only story lines, Topics, and Domains that carry a real monthly development. Each work receives one primary narrative treatment; cross-links expose other taxonomy membership without repeating its summary.

English and Chinese use the same explanatory logic: identify the older path, show which step changed, connect the evidence to the insight, and state the boundary. Only Chinese uses restrained, broadly understandable Northeastern conversational rhythm. Dialect performance, obscure vocabulary, jokes, and persona imitation are prohibited.

## Commands

```bash
python3 scripts/monthly_report.py prepare --month 2026-08
python3 scripts/monthly_report.py generate --month 2026-08
python3 scripts/monthly_report.py validate --month 2026-08
python3 scripts/monthly_report.py validate-all
python3 scripts/monthly_report.py index
```

`generate` requires `CLAUDE_CODE_OAUTH_TOKEN` and fails when a report already exists unless `--force` is supplied. The scheduled workflow runs at 06:17 America/Los_Angeles on day 1, after the regular knowledge-update wake-up window.
