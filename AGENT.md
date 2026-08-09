# Repository Constitution

You are the long-term maintainer of this repository.

This repository is **NOT** a benchmark implementation.

It is an **open knowledge base documenting scientific evaluation environments** — the design space of how AI agents are evaluated on scientific and long-horizon tasks.

Its purpose is to organize existing knowledge about:

- scientific benchmarks
- evaluation methodologies and metrics
- evaluation frameworks and diagnostic protocols
- trajectory evaluation
- resource-aware evaluation
- scientific workflows
- evaluation-focused RL work on agents
- benchmark design

The repository must remain **objective**. It must **not** contain discussion about any future benchmark the maintainers are working on. It should stand as a useful, standalone reference for anyone working on scientific evaluation.

---

## Repository Organization

The repository has **four knowledge layers**: works (facts about individual projects), plus **three co-equal aggregation axes** over them — topics (the **methodology axis**), domains (the **field axis**), and activities (the **research-activity / task axis**). No axis is subordinate to the others.

- **Topic** — the evaluation or research *theme* a work relates to (why / how we evaluate).
- **Domain** — the scientific or engineering *field* a work is grounded in (where the task lives).
- **Activity** — the substantive scientific or research *task* the evaluated agent or system performs (what the agent does).

### Layer 1 — Works

Directory: `works/`

- **Flat directory.** Every documented work lives directly under `works/` as a single Markdown file — no per-category sub-folders. Each work appears in exactly one place.
- **Filenames** use kebab-case matching the work's canonical name: `agentboard.md`, `t-eval.md`, `long-horizon-terminal-bench.md`.
- Cards are **factual references**. They answer *"What is this work?"* — not *"How does it compare to everything else?"* Synthesis belongs in topic pages, not cards.
- Cards must be **lightweight**. Do not let a card grow into a literature review.

**"Works" is broader than "benchmarks."** The directory holds cards for benchmarks, evaluation methodologies, evaluation frameworks (diagnostic overlays, trace-analysis systems, ground-truth generation toolkits), evaluation-focused RL contributions, surveys, and position papers. Non-benchmark works keep the same card structure — sections that do not apply are filled with `N/A` and a short note (e.g., `N/A — survey paper`).

**Card template:**

- Overview
- **Topics** *(metadata block — bulleted list of topic pages this work belongs to)*
- **Activities** *(metadata block — bulleted list of activity pages, or an explicit `N/A — <reason>`)*
- Links
- Summary
- Tasks
- Domains
- Evaluation
- Typical Duration
- Main Contribution
- Key Design Ideas
- Strengths
- Limitations
- Related Works

The `Topics` block is not just navigation for readers — it is the **internal index** used to keep topic pages in sync. When a new topic page is added, its `Topics` entry on each relevant card is how a maintainer finds the cards to link. When a card is updated, its `Topics` block tells the maintainer which topic pages may need synchronization. The `Activities` block works the same way for the activity axis (see Layer 4): it is the reverse index that keeps activity pages in sync, and it is **mandatory on every card** — applicable works link one or more canonical activities, and genuinely non-applicable works carry an explicit `N/A — <reason>`.

**Do NOT include** sections such as:

- Gap to Our Work
- Comparison with Our Framework
- Our Positioning
- Any other section that positions a work against a maintainer's own project

**Template stability.** Once the card template is established, avoid changing its structure. Consistency across cards is more valuable than optimizing individual pages. New evaluation dimensions should extend **topic pages**, not card fields. The `Activities` block was a deliberate, one-time schema extension adding a core navigation axis (mirroring `Topics`); it does not license further casual additions. Activities are controlled navigation metadata drawn from a fixed taxonomy — not a place for topic-specific evaluation dimensions.

**Repository Notes discipline.** Any observation that is not stated by the paper or official project must be prefixed `Repository note:`. Repository Notes must be conservative:

- Allowed: maintenance observations, factual synthesis across multiple papers, repository-specific organizational notes, observations that are direct consequences of what the paper describes.
- Not allowed: speculative critique, opinion about the field, extrapolations from the paper's results to settings the paper does not evaluate, judgment calls about what the authors *should* have done.

If an observation cannot be reasonably supported by the cited literature, it should not appear as a Repository Note.

### Layer 2 — Topics

Directory: `topics/`

Each topic summarizes one important evaluation direction and acts as a **literature review**.

**Canonical topic taxonomy.** The repository organizes topics around this fixed set:

| # | Topic | File |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | `long_horizon_evaluation.md` |
| II | Scientific Agent Benchmarks | `scientific_agents.md` |
| III | Trajectory Evaluation | `trajectory_evaluation.md` |
| IV | Skill Hierarchy | `skill_hierarchy.md` |
| V | Credit Assignment | `credit_assignment.md` |
| VI | Resource-aware Evaluation | `resource_aware_evaluation.md` |
| VII | Survey | `survey.md` |

Skill Hierarchy and Credit Assignment are **two independent topics**. Do not merge them.

Adding a new canonical topic is a structural decision that requires updating this table.

**Filename convention within the taxonomy:**

- Evaluation-direction topics use the `_evaluation.md` suffix (`trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`).
- Broader topics use natural names (`scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`).

**Topic page template:**

- **Definition** — concise definition of the topic.
- **Motivation** — why this topic matters.
- **Existing Approaches** — representative work.
- **Comparison** — comparison table(s) using dimensions specific to this topic.
- **Open Questions** — current challenges and future directions.
- **Related Works** — links to work cards in `works/`.

There is **no global comparison matrix**. Each topic owns its own comparison dimensions.

### Layer 3 — Domains

Directory: `domains/`

Domains aggregate works by the **science or engineering domain they evaluate in** — an orthogonal axis to topics, which aggregate by evaluation methodology, and **equal to topics in importance**. A CFD benchmark and a proof-verification benchmark may share a topic (e.g., Skill Hierarchy) while living in different domains (Mechanical & Aerospace Engineering vs. Mathematics).

Domain pages are **factual reference pages, not literature reviews** — co-equal with topic pages as an entry point, different in kind. Each carries a comparison table with **fixed, domain-oriented columns identical on every domain page** — unlike topic tables, which choose their own dimensions. The table describes what science each work tackles, in enough detail for a reader from that field; methodology synthesis, topic-specific comparison dimensions, and open questions stay in topic pages.

**Canonical domain taxonomy.** The repository organizes domains around this fixed set:

| Group | Domain | File |
|---|---|---|
| Science | Physics | `physics.md` |
| Science | Astronomy | `astronomy.md` |
| Science | Mathematics | `mathematics.md` |
| Science | Chemistry | `chemistry.md` |
| Science | Biology | `biology.md` |
| Science | Neuroscience & Cognitive Science | `neuroscience_cognitive_science.md` |
| Science | Medicine & Health | `medicine_health.md` |
| Science | Earth Science | `earth_science.md` |
| Science | Environmental Science | `environmental_science.md` |
| Science | Materials Science | `materials_science.md` |
| Science | Computer Science | `computer_science.md` |
| Science | AI & Machine Learning Research | `ai_ml_research.md` |
| Engineering | Mechanical & Aerospace Engineering | `mechanical_aerospace_engineering.md` |
| Engineering | Electrical Engineering | `electrical_engineering.md` |
| Engineering | Energy Systems | `energy_systems.md` |
| Engineering | Chemical Engineering | `chemical_engineering.md` |
| Engineering | Civil & Structural Engineering | `civil_structural_engineering.md` |
| Engineering | Robotics | `robotics.md` |
| Engineering | Software & Systems Engineering | `software_systems_engineering.md` |

Adding a new canonical domain is a structural decision that requires updating this table. Domain filenames use snake_case matching the domain name.

**Domain page template:**

- **Scope** — one or two sentences: what counts, including fold rules.
- **Comparison** — a factual table with the fixed columns `Work | Year | Scientific problem | Task form & scale | Domain verification | Card`. *Scientific problem* states what science question the work actually tackles, in enough detail for a domain expert; *Task form & scale* states what the agent concretely does and how many tasks fall in this domain; *Domain verification* states how scientific correctness is checked (numerical error vs. reference, expert labels, execution, physical criteria, LLM judge, …). For multi-domain suites, the row is slanted to this domain's slice. Every cell must be verifiable from the work's card.
- **Related Works** — bare links to the work cards (the mapping list). A domain with no documented works yet states so explicitly.

**Rules:**

- **Folds, not new domains.** Narrower fields fold into canonical domains: bioinformatics / genomics / single-cell → Biology; particle / nuclear / quantum physics → Physics; GIS / geospatial → Earth Science; ecology → Environmental Science; psychology → Neuroscience & Cognitive Science; formal verification of software → Software & Systems Engineering.
- **A work may belong to multiple domains.** Multi-domain suites (e.g., a benchmark spanning ten scientific fields) appear in every domain they cover.
- **No catch-all.** Works with no science or engineering domain — web/UI agents, computer use, generic tool use, evaluation methodology, surveys — simply do not appear in the domain index. UI and computer-use environments are **not** science or engineering domains, even when technically demanding.
- **One-way mapping, maintained on domain pages only.** Unlike the redundant Topics mapping, cards are **not** modified for the domain axis: the card template stays stable, and the card's existing `## Domains` prose section is the evidence for domain assignment. When a card's `## Domains` section changes, check the domain pages for needed updates.
- **Assignment must be verifiable.** A work is placed in a domain only if its card's `## Domains` section (backed by the paper) names that domain or a field that folds into it. If a paper says "5 engineering categories" without naming them, the work is not force-assigned — it waits until the categories are verified.

### Layer 4 — Activities

Directory: `activities/`

Activities aggregate works by the **substantive scientific or research task the evaluated agent performs** — the *what does the agent do* axis, orthogonal to topics (how/why we evaluate) and domains (what field). A physics benchmark (domain: Physics) might evaluate *Scientific Problem Solving & Reasoning*, while a physics-law-discovery benchmark in the same domain evaluates *Experiment Design & Scientific Discovery*.

Activity pages are **reference pages with light synthesis** — co-equal with topic and domain pages as an entry point. Each carries a Definition, a Scope note, a Task-Patterns synthesis of how the activity appears across the corpus, a fixed-column Comparison table, and a Related Works reverse index. Detailed evaluation-methodology synthesis stays in topics; field-specific scientific verification stays in domains.

**Canonical activity taxonomy.** The repository organizes activities around this fixed set of 11:

| # | Activity | File |
|---|---|---|
| 1 | Literature Search & Evidence Synthesis | `literature_evidence_synthesis.md` |
| 2 | Scientific Problem Solving & Reasoning | `scientific_problem_solving_reasoning.md` |
| 3 | Data Analysis & Statistical Inference | `data_analysis_statistical_inference.md` |
| 4 | Modeling & Prediction | `modeling_prediction.md` |
| 5 | Simulation & Scientific Computing | `simulation_scientific_computing.md` |
| 6 | Experiment Design & Scientific Discovery | `experiment_design_discovery.md` |
| 7 | Laboratory & Instrument Control | `laboratory_instrument_control.md` |
| 8 | Optimization & Engineering Design | `optimization_engineering_design.md` |
| 9 | Scientific Software & Workflow Engineering | `scientific_software_workflow_engineering.md` |
| 10 | Research Reproduction & Replication | `research_reproduction_replication.md` |
| 11 | End-to-End Research | `end_to_end_research.md` |

Adding, renaming, splitting, or removing a canonical activity is a structural decision that requires updating this table. Activity filenames use snake_case. Per-activity definitions and scope live on each page and in [`activities/README.md`](./activities/README.md).

**Activity page template:**

- **Definition** — one concise paragraph defining the activity.
- **Scope** — what belongs here and the key boundary cases.
- **Task Patterns** — synthesis of how the activity appears across the corpus, linking work cards.
- **Comparison** — a factual table with the fixed columns `Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card`. *Activity instantiation* states what the work asks the agent to do with respect to **this** activity (not a whole-benchmark summary). Every cell must be verifiable from the work's card.
- **Related Works** — bare links to the work cards (the reverse-index mapping list).

**Rules:**

- **Multi-label, assigned conservatively.** Activities are not mutually exclusive; a work may appear on several activity pages. But an activity is listed only when it is a **meaningful evaluated component** — if removing it would materially change what capability the benchmark measures. Incidental tool use is not enough. Typical cards carry one to three activities; four or more is rare and must reflect a genuinely broad or end-to-end task.
- **Two-way reverse index.** Unlike domains, the activity mapping is redundant like topics: every activity on a card's `## Activities` block must appear in that activity page's `Related Works` (and Comparison table), and vice versa. The two sides must agree exactly — no table-only entries, no duplicates, no broken links.
- **Not every work has an activity.** Surveys, position papers, pure evaluation methodologies and diagnostic/reward frameworks over arbitrary trajectories, general-purpose web/UI/computer-use and coding-assistant benchmarks, and safety/robustness/resource-awareness probes do not evaluate a scientific/research activity. Their cards carry an explicit `## Activities` block reading `N/A — <reason>` and appear on no activity page. Use `N/A` only when the axis genuinely does not apply — never because classification is hard.
- **Canonical labels only, evidence-based.** Cards draw solely from the taxonomy above. Classification is based on the actual task the card describes (`Overview`, `Tasks`, `Summary`, `Main Contribution`, `Domains`, `Key Design Ideas`), falling back to the verified primary source — never on title keywords. Do not confuse activities with topics (Trajectory Evaluation, Credit Assignment…), domains (Physics, Robotics…), verifier types (LLM judge, execution-based…), or work types (benchmark, survey…).

---

## Relationship Between the Layers

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. Do not force a work into a single topic to "keep things tidy" — cross-topic membership is the intended pattern, not an exception.

- Work pages document **individual projects** (facts).
- Topic pages **synthesize** across works.
- A work **belongs to multiple topics**. That mapping is expressed twice, redundantly on purpose:
  - in the card's `Topics` metadata block, and
  - in each topic page's `Related Works` section.

Example mappings from the canonical taxonomy:

```
TRACE                  → trajectory_evaluation, long_horizon_evaluation
Terminal-Bench Science → scientific_agents, long_horizon_evaluation
CostBench              → resource_aware_evaluation
AgentBoard             → trajectory_evaluation, skill_hierarchy
```

**Activities work the same way.** A work's activity memberships are expressed twice, redundantly on purpose: in the card's `Activities` metadata block, and in each activity page's `Related Works` section. The one difference from topics is that activities admit an explicit `N/A` state for works that evaluate no scientific/research task.

**Topic, domain, and activity pages are the three co-equal primary entry points.** A reader who arrives with a methodology question starts from `topics/`; a reader who arrives with a field in mind starts from `domains/`; a reader who arrives asking what the agent actually does starts from `activities/`. All follow links into `works/` and from there to the original papers:

```
Topic     →  Representative works              →  Original papers
Domain    →  Works evaluated in that domain    →  Original papers
Activity  →  Works performing that task        →  Original papers
```

---

## Documentation Principles

- Documentation comes first.
- Prefer Markdown.
- Keep files reasonably small.
- Avoid duplication.
- Prefer **linking** over **copying**.

The repository should feel like a technical handbook rather than research notes.

---

## References

Zero tolerance for fabricated references.

Every claim added to the repository must be verified. There are **two distinct levels of verification**, and both are required:

### Link validation

Verify the following against the actual source:

- paper title
- URL (paper, project, code)
- venue
- publication year

### Content validation

Verify the following **from the original paper or official project only** — never from secondary sources or summaries:

- benchmark statistics
- task counts
- evaluation metrics
- reported numbers
- benchmark settings

If a statistic cannot be verified from the primary source, use `TODO(reference)` instead of guessing. **Never infer numbers from secondary sources** (blog posts, tweets, other summaries).

Preferred primary sources:

- arXiv
- OpenReview
- ACL Anthology
- Nature
- Science
- Official GitHub repositories
- Official project websites
- Workshop / conference proceedings (NeurIPS workshops, etc.)

**Correctness is always more important than completeness.**

---

## Bilingual Documentation

Maintain both English and Chinese versions.

**English is always the canonical version.**

Chinese pages mirror the English tree under `zh/` (`zh/works/`, `zh/topics/`, `zh/domains/`, `zh/activities/`). Every card's `## Activities` block is mirrored on the Chinese card under the heading `## 研究活动`, using the fixed Chinese activity labels; every English activity page has a Chinese counterpart.

**Cadence.** English and Chinese documentation must not diverge for long. The working cycle is:

1. Finish one batch of English pages.
2. Review.
3. Synchronize the corresponding Chinese pages.
4. Re-read every changed Chinese page as a Chinese reader and fix any phrasing that is stilted, ambiguous, or only makes sense with the English in mind. This naturalness review is part of the sync step, not optional polish.
5. Only then begin the next English batch.

Do not postpone Chinese translation until the whole repository is complete.

Translation rules:

- work names remain in English
- paper titles remain in English
- project names remain in English
- proper nouns remain in English
- technical terminology may remain in English where appropriate

**Natural translation, not word-for-word.** Chinese pages must read as if originally written in Chinese. Literal renderings of English idioms and metaphors are defects — e.g., a "breadcrumb" link is a 返回链接, not 面包屑. When a sentence structure works in English but reads awkwardly in Chinese, restructure the sentence; fidelity is to the meaning, never to the word order.

---

## Scope

**In scope:**

- Scientific evaluation environments
- Benchmark landscape
- Evaluation methodology and metrics
- Evaluation frameworks and diagnostic protocols
- Scientific workflows
- Trajectory evaluation
- Resource-aware evaluation
- Benchmark design
- **Evaluation-focused RL work on agents** — reward design for agents, credit-assignment methods, off-policy evaluation of agent trajectories, and similar contributions whose focus is *evaluating* agents.

**Out of scope (for now):**

- Pure RL algorithm development
- Policy optimization and training procedures
- Agent implementation
- Multi-agent systems
- Memory systems

The distinction between in-scope and out-of-scope RL work is the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

---

## Goal

The final repository should read like a well-organized technical handbook.

- Work cards provide **factual documentation**.
- Topic pages provide **synthesis** along the methodology axis; domain pages provide **field-oriented reference** along the domain axis; activity pages provide **task-oriented reference** along the research-activity axis. The three are co-equal entry points.

Together they should give any reader a clear understanding of the current scientific evaluation landscape.
