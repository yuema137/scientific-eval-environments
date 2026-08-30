# Daily Update Agent

A deterministic GitHub Actions orchestrator + Claude Code semantic workers that keeps this
knowledge base current: it discovers newly released evaluation and evaluation-driven-improvement work, writes verified English
work cards, integrates them into every canonical axis, mirrors and independently reviews the
Chinese translation, validates everything, and **opens a pull request for human review — it
never auto-merges.**

## Five phases (ordered; a later phase never starts if an earlier one failed)

```
Phase 1  Discovery        arXiv + OpenReview + HuggingFace + GitHub metadata, every Topic/Domain/Activity + global queries
Phase 2  Cards            deep primary-source review; write factual English cards; reject aggressively
Phase 3  English axes     Topic / Domain / Activity specialists + deterministic integration + count refresh
Phase 4  Chinese mirror   translate every changed English page (English is canonical)
Phase 5  Chinese review   independent editor rewrites literal/awkward Chinese
Final gate               machine-readable; PR is impossible unless all five phases pass
```

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

## Sources & search

Adapters (`sources.py`): `ArxivOAISource`, `OpenReviewSource`, `HuggingFaceSource`, `GitHubSource`
— **metadata only** (Phase 1 never downloads papers or clones repos). Add a source = add one
`Source` subclass.

`HuggingFaceSource` uses one endpoint in two modes: the **curated daily-papers feed**
(`?date=`, harvested one calendar day at a time across the discovery window and memoized per
window, so cost is ~one request per day regardless of taxonomy size) unioned with a **term search**
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
  → deep-review safety cap                  (unchanged; if genuine deep_review still exceeds the cap the
                                             run is needs_attention — the cap is never raised to force green)
```

Every stage's kept/rejected sets and reasons are preserved as workflow artifacts
(`prefilter_rejected.json`, `merged_candidates.json`, `relevance.json`, `candidates.json`), so the
next audit can compute precision by stage. None are committed to the knowledge base.

## Deduplication & pending-PR awareness

`inventory.py` builds an identity index of existing cards (arXiv ID → OpenReview ID → DOI →
GitHub URL → normalized title). `deduplicate.py` merges cross-source hits into one candidate,
drops works already in the repo, and drops works already staged on the open automated-update
branch. There is a single **rolling PR** on branch `auto/knowledge-update`; each successful run
accumulates onto it, and new changes only become visible after that run passes the final gate.

## Configuration (`config.yaml`)

`lookback_days` (overlapping window; dedup, not a 1-day cutoff, prevents repeats), per-source
limits, smoke sampling, retry/backoff, Claude model/turn bounds, and the runaway-cost limits:
`max_deep_review_candidates`, `max_parallel_{card,translation,review}_workers`. If Phase 1 yields
more deep-review candidates than the max, the run fails as **needs_attention** and preserves the
full candidate artifact — it never silently truncates.

## Claude workers (`automation/update_agent/agents/`)

`work-card-writer`, `topic-axis-updater`, `domain-axis-updater`, `activity-axis-updater`,
`chinese-mirror-translator`, `chinese-naturalness-reviewer`, `final-update-auditor`. All are
invoked headless via `run_claude_worker.py` (`claude -p --output-format json`, bounded turns,
**Bash/code-execution never allowed**). Structured JSON decisions only — no prose grepping.

## Security

- `CLAUDE_CODE_OAUTH_TOKEN` is consumed only as a GitHub secret env var; never logged/committed.
- No `pull_request`/`pull_request_target` trigger — a fork can never run this secret-bearing workflow.
- Every paper/README/abstract/webpage is **untrusted data**; agent prompts forbid obeying embedded
  instructions, running external code, cloning/executing candidate repos, or leaking secrets.
- Least-privilege: top-level `contents: read`; only `finalize` has `contents: write` + `pull-requests: write`.
- Counts are auto-derived (`scripts/update_counts.py`).

## Failure behavior & debugging

A failed phase blocks the PR, uploads `runtime/` artifacts, and writes a job summary. The
overlapping lookback lets the next day's run recover. To debug: open the failed run, download the
`runtime`/`stage-*` artifacts, and inspect `state/*.json` and the phase manifests.

## Tests

- `tests/update_agent/` — deterministic unit/fixture tests (inventory, dedup, phase gate,
  profile coverage, axis/bilingual validators, empty-run, failure-injection).
- Live smokes: `discovery-smoke` (sources), `auth-smoke` (token), `fixture-e2e-smoke` (5 phases).

## Disable / enable

Cadence/lookback are in `config.yaml` (`lookback_days: 3`) and the workflow `schedule` (every 3 days) — both chosen to bound per-run token cost.

Disable: GitHub → Actions → “Daily Knowledge Update” → **⋯ → Disable workflow** (or delete the
schedule block). Re-enable from the same menu. Tune cost via `config.yaml` limits.

## One-time maintainer setup

1. Repository secret **`CLAUDE_CODE_OAUTH_TOKEN`** (Settings → Secrets and variables → Actions).
2. **Settings → Actions → General → Workflow permissions → enable "Allow GitHub Actions to create
   and approve pull requests"** (lets the `finalize` job open the automated PR; it still never merges).
