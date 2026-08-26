# CLAUDE.md

The maintainer constitution is canonical in [`AGENT.md`](./AGENT.md). Read it before making changes.

## Layer model

There are **three co-equal aggregation axes** over the works layer: topics (methodology), domains (field), and activities (research task).

- **`works/`** — flat directory, one Markdown file per work. Factual references only.
  Template: Overview, **Topics** (metadata block), **Activities** (metadata block), Links, Summary, Tasks, Domains, Evaluation, Typical Duration, Main Contribution, Key Design Ideas, Strengths, Limitations, Related Works. **No** "Gap to Our Work" or positioning sections.
- **`topics/`** — literature reviews. Each topic owns its own comparison table. No global matrix.
- **`domains/`** — the **field axis**, a full knowledge layer co-equal with topics. Pages hold Scope + a Comparison table with fixed columns (`Work | Year | Scientific problem | Task form & scale | Domain verification | Card`, identical on every domain page, every cell verifiable from the card) + a Capability Matrix (fixed columns `Domain | Net | E2E | Cost | MM | Repro | Real | Rubric | Judge | Inter | Fail`; yes/no columns take `✔`/`✘`/`◐`/`?` and are ordered rarest-first, `Domain` carries per-page subfield abbreviations, `Fail` is graded `0`–`4`; built from the card and then the paper, never from the Comparison row; `?` is a verification backlog, not a `✘`; updated **incrementally**, one row per new card, never re-derived wholesale) + bare Related Works links. No methodology synthesis or open questions — those stay in topics.
- **`activities/`** — the **research-activity / task axis** (what the agent actually does), a full knowledge layer co-equal with topics and domains. Pages hold Definition + Scope + a Task-Patterns synthesis + a Comparison table with fixed columns (`Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card`) + bare Related Works links.

"Works" is broader than "benchmarks" — the layer holds cards for benchmarks, methodologies, evaluation frameworks, surveys, position papers, and evaluation-focused RL contributions on agents. Non-benchmark works fill inapplicable sections with `N/A` and a short note.

**Navigation flows Topic → Work → Paper, Domain → Work → Paper, and Activity → Work → Paper.** Topics (methodology axis), domains (field axis), and activities (task axis) are three co-equal primary entry points; cards are references linked from all three.

**Topics and activities are not mutually exclusive.** A work may belong to multiple topics and multiple activities — each is a different perspective, not a unique category. Cross-membership is the intended pattern, not an exception.

A work card lists its topics in the `Topics` block and its activities in the `Activities` block; each topic/activity page lists its works in `Related Works`. These redundant mappings are the internal index for keeping the layers in sync. The `Activities` block is **mandatory on every card**: applicable works link one or more canonical activities; genuinely non-applicable works (surveys, pure methodology, general-purpose or safety/resource probes) carry an explicit `N/A — <reason>` and appear on no activity page. Assign activities conservatively (typically 1–3), from evidence in the card, never from title keywords.

## Canonical topic taxonomy (fixed)

| # | Topic | File |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | `long_horizon_evaluation.md` |
| II | Scientific Agent Benchmarks | `scientific_agents.md` |
| III | Trajectory Evaluation | `trajectory_evaluation.md` |
| IV | Skill Hierarchy | `skill_hierarchy.md` |
| V | Credit Assignment | `credit_assignment.md` |
| VI | Resource-aware Evaluation | `resource_aware_evaluation.md` |
| VII | Survey | `survey.md` |

Skill Hierarchy and Credit Assignment are independent topics — do not merge.

## Canonical domain taxonomy (fixed)

19 domains in two groups; full table in `AGENT.md`.

- **Science:** Physics, Astronomy, Mathematics, Chemistry, Biology, Neuroscience & Cognitive Science, Medicine & Health, Earth Science, Environmental Science, Materials Science, Computer Science, AI & Machine Learning Research.
- **Engineering:** Mechanical & Aerospace, Electrical, Energy Systems, Chemical, Civil & Structural, Robotics, Software & Systems.

Domain rules: narrower fields **fold** into canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, …); a work may belong to multiple domains; **no catch-all** — works without a science/engineering domain (web/UI agents, computer use, methodology, surveys) do not appear; mapping is **one-way, maintained on domain pages only** — cards are never modified for the domain axis, and a card's `## Domains` prose is the assignment evidence; unverifiable domain membership is not assigned.

## Canonical activity taxonomy (fixed)

11 activities; full table and per-activity rules in `AGENT.md` and [`activities/README.md`](./activities/README.md).

Literature Search & Evidence Synthesis (`literature_evidence_synthesis`), Scientific Problem Solving & Reasoning (`scientific_problem_solving_reasoning`), Data Analysis & Statistical Inference (`data_analysis_statistical_inference`), Modeling & Prediction (`modeling_prediction`), Simulation & Scientific Computing (`simulation_scientific_computing`), Experiment Design & Scientific Discovery (`experiment_design_discovery`), Laboratory & Instrument Control (`laboratory_instrument_control`), Optimization & Engineering Design (`optimization_engineering_design`), Scientific Software & Workflow Engineering (`scientific_software_workflow_engineering`), Research Reproduction & Replication (`research_reproduction_replication`), End-to-End Research (`end_to_end_research`).

Activity rules: **multi-label**, assigned conservatively (typically 1–3, only when a meaningful evaluated component); **two-way** card↔page reverse index like topics (card `## Activities` ⇆ page `Related Works`, agree exactly); **mandatory block** on every card, with explicit `N/A — <reason>` for works that evaluate no scientific/research task; **canonical labels only**, evidence-based (not title keywords); do not confuse activities with topics, domains, verifier types, or work types.

## Working rules

- **Two-level reference validation.**
  - *Link validation*: title, URL, project, venue, year.
  - *Content validation*: statistics, task counts, metrics, reported numbers, settings — from the **original paper or official project only**, never secondary sources. Unverifiable content becomes `TODO(reference)`.
  - *Retrieval*: for literature and domain-backfill research, prefer **WebFetch** for public HTTP(S) retrieval. Do not use `curl` or `wget` when WebFetch can retrieve the source. Domain-scoped shell rules are fragile (argument order, redirects, variables), so network access is governed by `WebFetch(domain:…)` allow rules instead; a new publisher domain is approved once, then remembered.
- **English is canonical.** Chinese mirrors under `zh/` (`zh/works/`, `zh/topics/`, `zh/domains/`, `zh/activities/`) sync after every English batch — not deferred. Every card's `## Activities` block mirrors on the Chinese card under `## 研究活动` with the fixed Chinese activity labels. Translations must be **natural Chinese, not word-for-word** (面包屑-style literalisms are defects); after every sync, re-read the changed zh pages as a Chinese reader and fix stilted phrasing — the naturalness review is part of the sync step.
- **Objective only.** No "our benchmark" / "our approach" / positioning language anywhere in `works/` or `topics/`.
- **Link, do not copy.** Prefer cross-references over duplicating content.
- **Card template is stable.** Do not churn its structure. New evaluation dimensions extend topic pages, not card fields.
- **Filenames.** Cards kebab-case (`t-eval.md`); topics natural names or `_evaluation` suffix; domains snake_case (`materials_science.md`).
- **Repository Notes are conservative.** Prefix any non-paper observation with `Repository note:`. Allowed: maintenance observations, cross-paper synthesis, direct consequences of what the paper describes. Not allowed: speculative critique, opinion, extrapolation to settings the paper does not evaluate.
- **Counts are auto-derived.** All topic/domain/activity work counts, membership totals, and the root-README card/page totals come from `scripts/update_counts.py` (reads the reverse indexes). Run `python scripts/update_counts.py` after adding/removing/re-mapping cards; `--check` flags drift without writing. Never hand-edit a count cell.

## Scope

Evaluation-focused RL work on agents is **in scope** (reward design for agents, credit-assignment methods, off-policy evaluation of agent trajectories). Pure RL algorithm / training / policy optimization is **out of scope**. Judge by the paper's primary contribution: does it advance *how agents are evaluated* or *how agents are trained*?

## Automated daily updater

A GitHub Actions + Claude Code pipeline (`.github/workflows/daily-knowledge-update.yml`, `automation/update_agent/`, `scripts/update_agent/`) discovers new work daily and opens a rolling PR. Durable rules: automated additions meet the same evidence/scope bar as human ones; the English gate must pass before Chinese sync; the Chinese naturalness review is mandatory and independent; the automation opens/updates one PR but **never merges**. Mechanics: `automation/update_agent/README.md`.

## Files not part of the published repository

- `initial_doc.md` — the maintainer's private input material. **Not** repository content. Extract verifiable facts from it into topic and card pages; discard positioning language.

Scope, bilingual rules, and long-term goal are defined in `AGENT.md`.
