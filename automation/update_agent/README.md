# Daily Update Agent

A deterministic GitHub Actions orchestrator + Claude Code semantic workers that keeps this
knowledge base current: it discovers newly released evaluation and evaluation-driven-improvement work, including methods that make action or decision abstraction an explicit object of evaluation and optimization, writes verified English
work cards, integrates them into every canonical axis, mirrors and independently reviews the
Chinese translation, validates everything, and **opens a pull request for human review — it
never auto-merges.**

English writing, Chinese translation, and Chinese naturalness review all follow [`../../EXPLANATION_STYLE.md`](../../EXPLANATION_STYLE.md). The pipeline preserves causal structure, concrete traces, and boundaries instead of treating translation as sentence-by-sentence word substitution.

> **`auto/updater-state` is durable updater state. Do not delete it in branch cleanups.** It holds
> only `watermark.json`, the end of the last successful production run's search window, which
> drives the next discovery window. If it is missing, every production run fails as
> **needs_attention** until a maintainer runs the recovery described under
> [Discovery window, watermark and backfills](#discovery-window-watermark-and-backfills). It was
> deleted once during a stale-branch cleanup on 2026-10-22.

Every accepted card also records a sourced `First appeared` date: the earliest verifiable day when the work itself became publicly accessible, regardless of later publication. Workers compare preprint/submission, official project/data/software release, publisher/proceedings, DOI, and official-repository records; venue facts remain separate in `Links`. Repository addition is permitted only as an explicitly labeled last resort. After the Chinese mirror exists, `python3 scripts/backfill_first_appeared.py --index-only` regenerates the bilingual chronological indexes without another network request.

## Five phases (ordered; a later phase never starts if an earlier one failed)

```
Phase 1  Discovery        arXiv + OpenReview + HuggingFace + GitHub metadata, every Topic/Domain/Activity + global queries
Phase 2  Cards            deep primary-source review; write factual English cards; reject aggressively
Phase 3  English axes     Topic / Domain / Activity specialists + deterministic integration + date-index/count refresh
Phase 4  Chinese mirror   translate every changed English page (English is canonical)
Phase 5  Chinese review   independent editor rewrites literal/awkward Chinese
Final gate               machine-readable; PR is impossible unless all five phases pass
```

The deterministic integration step keeps every Topic, Domain, and Activity `Related Works` index ordered by the cards' `First appeared` dates, newest first; same-day ties use title A–Z. Axis comparison tables retain their own methodology-specific ordering.

Each GitHub Actions job is one phase (`discovery → english → chinese → review → finalize`);
state passes between jobs as `runtime/` artifacts. Every phase writes `runtime/state/<phase>.json`,
and `scripts/update_agent/phase_state.py` computes `ready_for_pr` — the only thing that lets the
finalize job open a PR.

## Schedule & concurrency

- Wakes **daily at 00:17 America/Los_Angeles** (native `timezone:` cron; GitHub adjusts for DST),
  but the discovery job's due-check only performs a full update when **≥ 72h** have passed since the
  last successful run (`watermark.min_interval_hours`). The effective cadence is therefore ~3 days,
  decoupled from the calendar month. Enabled 2026-08-18; before that the `schedule:` block was
  commented out pending a first legitimate PR, so every earlier run was `workflow_dispatch`.
- GitHub disables scheduled workflows on repositories with **60 days of no activity**; any push
  re-arms them. If the cadence silently stops, check this first.
- The catch-up guard allows a backlog of up to 60 days. A longer outage fails visibly rather than
  silently skipping old records; after a successful recovery, the durable watermark advances and
  the normal 72-hour cadence resumes.
- The watermark advances only when the whole run succeeds (a PR or a genuine no-op). A failure in
  any later phase therefore holds discovery at the old watermark, and the next run re-covers the
  same window plus the new days.
- `workflow_dispatch` supports manual modes (below). Scheduled runs are always `full`.
- Concurrency group `daily-knowledge-update`, `cancel-in-progress: false` — a running production
  update is never interrupted by the next trigger.

## Manual modes (`workflow_dispatch` → `mode`)

| Mode | What it does | Claude? | Writes repo? | PR? |
|---|---|---|---|---|
| `validators-only` | pytest suite + repo validators + count check | no | no | no |
| `discovery-smoke` | bounded live discovery (1 axis item/kind), no deep review | no | no | no |
| `auth-smoke` | tiny `claude -p` reads AGENT.md, returns a marker | yes | no | no |
| `fixture-e2e-smoke` | full 5 phases on ONE synthetic candidate in an isolated temp workspace | yes | no (temp only) | no |
| `full` | production run | yes | rolling branch | yes (never merged) |

`full` also takes two optional inputs, `window_start` and `window_end`. See the next section.

## Discovery window, watermark and backfills

A regular `full` run searches `watermark - overlap_hours → now`, where the watermark is read from
`auto/updater-state:watermark.json`. `run_phase.py discover` reports the outcome as `basis` in the
job summary and in `coverage.json` → `search_window`.

- **State absent.** If the branch or file is missing or unreadable, the run fails as
  **needs_attention** and the summary says why. It no longer falls back to the 3-day
  `lookback_days`; that fallback silently skipped 10-11..10-23 after the branch was deleted.
- **Manual window override.** Dispatch the workflow with `mode=full` and `window_start`
  (`YYYY-MM-DD`, UTC), optionally with `window_end` (inclusive; empty means now). Discovery
  searches exactly that range. The span is limited to `watermark.max_catchup_days`. Backfill a long
  gap in smaller ranges, for example 7 days per run, because the deep-review cap is per run. An
  invalid override fails as needs_attention.
- **Override runs and the watermark.** An override run never advances an existing watermark, so a
  backfill can never move the schedule backwards. It seeds the watermark at its window end **only
  when none exists**. That is the bootstrap path for a first run, or for recovery after the branch
  was deleted.
- **Regular runs** advance only forward. A window end at or before the current watermark is
  ignored, and an unreadable current watermark blocks the advance. `run_phase.py advance-watermark`
  re-reads the current value at advance time and writes its decision to the job summary.

Recovery after the state branch was deleted: dispatch `full` with `window_start` set to the first
day not known to be covered, and `window_end` empty. On success the watermark is seeded at "now",
and the schedule resumes from there. To backfill older gaps in smaller ranges, run those first:
the first successful override seeds the watermark at its window end. The next scheduled run then
covers everything from that point to now, provided that span is within `max_catchup_days`. Further
override runs leave the watermark alone.

## Sources & search

Adapters (`sources.py`): `ArxivOAISource`, `OpenReviewSource`, `HuggingFaceSource`, `GitHubSource`
— **metadata only** (Phase 1 never downloads papers or clones repos). Add a source = add one
`Source` subclass. Adapters receive the window end as well as the start; HuggingFace, OpenReview
and GitHub use it as an upper bound, so a bounded backfill does not fan out to today.

**arXiv (OAI-PMH).** `discover._harvest_arxiv` harvests the window in `arxiv_oai.chunk_days`
chunks (one day by default). Each chunk has its own `max_pages` budget, and `max_total_pages` caps
the whole run. One page cap used to be shared by the whole window, and in 2026-09/10 a 60-day
harvest stopped at datestamp 09-18 without covering the rest. Now a chunk that hits its cap,
errors, or is skipped for lack of budget marks the source `suspicious_empty`, which blocks the
watermark advance. The summary names the last complete day (`complete_through`). If every chunk
fails, the source is a `failure`. Harvested records then pass two filters before `raw_hits.json`:

- *Revision filter.* The OAI datestamp is the time of the last metadata change, and on
  `oaipmh.arxiv.org` `<created>` can be the latest version's date. For example, 2312.10986 shows
  `created=2026-10-23`. Each record therefore gets a first-submission estimate. The new-style id's
  YYMM fixes the v1 month, and `<created>` refines it only when it falls in that month. A record
  whose estimate is older than the window start minus `revision_grace_days` is a revision of an
  older paper, and it is dropped. Records with an unparseable id are kept.
- *Local taxonomy gate* (`_local_match`, unchanged): a concrete benchmark/eval noun plus an
  agent/LLM signal.

Both drops are saved: `phase1/arxiv_revisions_dropped.json` holds the revisions the gate would have
matched, and `phase1/arxiv_local_unmatched.json` holds compact records (id, title, dates,
categories) of new work the gate rejected. The counts are in `coverage.json` → `arxiv_harvest`.

**OpenReview** is relevance-ranked with no server-side date window (see the adapter comment), so a
short window can be empty. If it returns 0 records across every query over a window of at least
`openreview.zero_hit_min_window_days`, the summary shows a **WARNING** line, and the warning is
recorded in `coverage.json` → `source_warnings`. The warning does not block the run or hold the
watermark, because arXiv is the primary recency source. The 0-hit runs of 2026-10-27 were checked
live: the endpoint, `source=forum` and the date parsing all work, but the newest result in the
relevance top-100 was two weeks old.

`HuggingFaceSource` uses one endpoint in two modes: the **curated daily-papers feed**
(`?date=`, harvested one calendar day at a time across the **whole** discovery window and memoized
per window, so cost is ~one request per day regardless of taxonomy size; `huggingface.max_days` is
only a guard set above the longest valid window, and if it ever binds, or a day is unreachable, the
skipped days appear as a summary warning) unioned with a **term search**
(`?q=`, date-filtered client-side). Its ids ARE arXiv ids, so records merge with the arXiv record
for the same work — heavy overlap is expected and dedup collapses it. Its value is the papers the
date-windowed arXiv harvest ranks past, including work promoted to the feed days after posting:
the daily harvest deliberately does **not** date-filter, so late-promoted papers survive.
It is **not** in `validate_discovery`'s mandatory set — the feed is legitimately empty on weekends
and arXiv remains the primary recency source, so a HuggingFace outage must not block a run.
Search profiles live in `automation/update_agent/search_profiles/{domains,topics,activities,global}.yaml`
and are calibrated per axis item; `validators.py profiles` fails if a taxonomy item lacks coverage.
The canonical taxonomy is read from the repo (topic/domain/activity page titles) — never hard-coded.

## Phase-1 precision triage

Discovery is high-recall then **progressively discriminative** — noise is removed *after* retrieval, not by narrowing the search:

```
raw hits
  → deterministic source-aware prefilter   (prefilter.py; arXiv/OR/HF need eval+agent/science signal;
                                             GitHub needs a benchmark/environment noun + not a
                                             noise repo: awesome-*/skills/templates/MCP/SDK/apps)
  → cross-source merge + existing/pending dedup  (deduplicate.py; repo↔paper via linked arXiv id,
                                             HF↔arXiv via shared arXiv id,
                                             arXiv↔OR↔HF via fuzzy title + shared author — never title-only)
  → metadata relevance scorer               (relevance.py + relevance-scorer agent; Claude, metadata
                                             only, batched; deep_review / uncertain / reject_low_relevance;
                                             "a paper evaluating its own method" ≠ "an agent-evaluation
                                             contribution")
  → ranked admission                        (all deep_review + highest-confidence uncertain while under
                                             the cap; a scorer failure fails OPEN to 'uncertain', never a
                                             silent reject)
  → deep-review budget                     (top max_deep_review_candidates by confidence are admitted;
                                             the overflow goes to deferred_by_budget.json. It does not
                                             fail the run and is not carried into later runs)
```

Every stage's kept/rejected sets and reasons are preserved as workflow artifacts
(`arxiv_revisions_dropped.json`, `arxiv_local_unmatched.json`, `prefilter_rejected.json`,
`merged_candidates.json`, `relevance.json`, `deferred_by_budget.json`, `candidates.json`), so the
next audit can compute recall and precision by stage. None are committed to the knowledge base.

## Deduplication & pending-PR awareness

`inventory.py` builds an identity index of existing cards (arXiv ID → OpenReview ID → DOI →
GitHub URL → normalized title). `deduplicate.py` merges cross-source hits into one candidate,
drops works already in the repo, and drops works already staged on the open automated-update
branch. There is a single **rolling PR** on branch `auto/knowledge-update`; each successful run
accumulates onto it, and new changes only become visible after that run passes the final gate.

When the rolling PR is open, its branch is merged with current `main` before workers run; a conflict stops the update. When the last rolling PR is merged and its head still matches the remote branch, the next batch starts with current `main` content and retains the old branch only as merge ancestry, allowing a normal fast-forward push even after a squash merge. An unmatched branch tip or a failed PR-state lookup blocks reuse rather than discarding unreviewed changes. Merge updater code fixes into `main` before a production recovery run, because workers execute from this canonical base.

## Configuration (`config.yaml`)

`watermark` (overlap, catch-up limit, cadence), `arxiv_oai` (chunking, page budgets, revision
grace), `huggingface.max_days`, `openreview.zero_hit_min_window_days`, per-source limits, smoke
sampling (`smoke.lookback_days`), retry/backoff, Claude model/turn bounds, and the runaway-cost
limits: `max_deep_review_candidates`, `max_parallel_{card,translation,review}_workers`.
`lookback_days` is not used by production `full` runs. If Phase 1 ranks more candidates for deep
review than `max_deep_review_candidates`, `relevance.admit` admits the top N by confidence and
writes the rest to `deferred_by_budget.json`. The run does not fail, and deferred candidates are not
retried automatically.

## Claude workers (`automation/update_agent/agents/`)

`work-card-writer`, `topic-axis-updater`, `domain-axis-updater`, `activity-axis-updater`,
`chinese-mirror-translator`, `chinese-naturalness-reviewer`, `final-update-auditor`. All are
invoked headless via `run_claude_worker.py` (`claude -p --output-format json`, bounded turns,
**Bash/code-execution never allowed**). Structured JSON decisions only — no prose grepping.

## Security

- `CLAUDE_CODE_OAUTH_TOKEN` is consumed only as a GitHub secret env var; never logged/committed.
- No `pull_request`/`pull_request_target` trigger — a fork can never run this secret-bearing workflow.
  Pull requests are gated instead by `.github/workflows/knowledge-base-validation.yml`, a separate
  secret-free workflow (`contents: read`, no token, repository-local Python only). That is where a
  `pull_request` trigger belongs; do not add one here to "make PRs validated".
- Every paper/README/abstract/webpage is **untrusted data**; agent prompts forbid obeying embedded
  instructions, running external code, cloning/executing candidate repos, or leaking secrets.
- Least-privilege: top-level `contents: read`; only `finalize` has `contents: write` + `pull-requests: write`.
- Counts are auto-derived (`scripts/update_counts.py`).

## Failure behavior & debugging

A failed phase blocks the PR, uploads `runtime/` artifacts, and writes a job summary. The
watermark does not advance, so the next run re-covers the same window. A failed **scheduled** run also opens a
tracking issue titled "Daily Knowledge Update is failing", or comments on it while it is open;
close the issue once the cause is fixed. The auth smoke prints the Claude CLI's own failure
fields, so an expired token and an exhausted usage limit are distinguishable in the log. To debug: open the failed run, download the
`runtime`/`stage-*` artifacts, and inspect `state/*.json` and the phase manifests.

## Tests

- `tests/update_agent/` — deterministic unit/fixture tests (inventory, dedup, phase gate,
  profile coverage, axis/bilingual validators, empty-run, failure-injection, discovery coverage
  (chunked harvest, revision filter, missing state, window override, zero-hit warnings), and the
  repo-wide sweeps + Chinese-card conventions in `test_repo_wide_validators.py`).
- Live smokes: `discovery-smoke` (sources), `auth-smoke` (token), `fixture-e2e-smoke` (5 phases).

## Disable / enable

Cadence is set by `watermark.min_interval_hours` (72h) in `config.yaml` and the daily workflow
`schedule`. Per-run token cost is bounded by `limits.max_deep_review_candidates`.

Disable: GitHub → Actions → “Daily Knowledge Update” → **⋯ → Disable workflow** (or delete the
schedule block). Re-enable from the same menu. Tune cost via `config.yaml` limits.

## One-time maintainer setup

1. Repository secret **`CLAUDE_CODE_OAUTH_TOKEN`** (Settings → Secrets and variables → Actions).
2. **Settings → Actions → General → Workflow permissions → enable "Allow GitHub Actions to create
   and approve pull requests"** (lets the `finalize` job open the automated PR; it still never merges).
