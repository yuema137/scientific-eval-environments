# CLAUDE.md

The maintainer constitution is canonical in [`AGENT.md`](./AGENT.md). Read it before making changes.

## Layer model

- **`works/`** — flat directory, one Markdown file per work. Factual references only.
  Template: Overview, **Topics** (metadata block), Links, Summary, Tasks, Domains, Evaluation, Typical Duration, Main Contribution, Key Design Ideas, Strengths, Limitations, Related Works. **No** "Gap to Our Work" or positioning sections.
- **`topics/`** — literature reviews. Each topic owns its own comparison table. No global matrix.
- **`domains/`** — factual index by science/engineering domain (orthogonal to topics, which index by methodology). Pages hold Scope + a Comparison table with fixed columns (`Work | Year | Scientific problem | Task form & scale | Domain verification | Card`, identical on every domain page, every cell verifiable from the card) + bare Related Works links. No methodology synthesis or open questions — those stay in topics.

"Works" is broader than "benchmarks" — the layer holds cards for benchmarks, methodologies, evaluation frameworks, surveys, position papers, and evaluation-focused RL contributions on agents. Non-benchmark works fill inapplicable sections with `N/A` and a short note.

**Navigation flows Topic → Work → Paper.** Topics are the primary entry point; cards are references linked from topics.

**Topics are not mutually exclusive.** A work may belong to multiple topics — each topic is a different literature perspective, not a unique category. Cross-topic membership is the intended pattern, not an exception.

A work card lists its topics in the `Topics` block; each topic page lists its works in `Related Works`. This redundant mapping is the internal index for keeping the two layers in sync.

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

## Working rules

- **Two-level reference validation.**
  - *Link validation*: title, URL, project, venue, year.
  - *Content validation*: statistics, task counts, metrics, reported numbers, settings — from the **original paper or official project only**, never secondary sources. Unverifiable content becomes `TODO(reference)`.
- **English is canonical.** Chinese mirrors under `zh/` (`zh/works/`, `zh/topics/`, `zh/domains/`) sync after every English batch — not deferred.
- **Objective only.** No "our benchmark" / "our approach" / positioning language anywhere in `works/` or `topics/`.
- **Link, do not copy.** Prefer cross-references over duplicating content.
- **Card template is stable.** Do not churn its structure. New evaluation dimensions extend topic pages, not card fields.
- **Repository Notes are conservative.** Prefix any non-paper observation with `Repository note:`. Allowed: maintenance observations, cross-paper synthesis, direct consequences of what the paper describes. Not allowed: speculative critique, opinion, extrapolation to settings the paper does not evaluate.

## Scope

Evaluation-focused RL work on agents is **in scope** (reward design for agents, credit-assignment methods, off-policy evaluation of agent trajectories). Pure RL algorithm / training / policy optimization is **out of scope**. Judge by the paper's primary contribution: does it advance *how agents are evaluated* or *how agents are trained*?

## Files not part of the published repository

- `initial_doc.md` — the maintainer's private input material. **Not** repository content. Extract verifiable facts from it into topic and card pages; discard positioning language.

Scope, bilingual rules, and long-term goal are defined in `AGENT.md`.
