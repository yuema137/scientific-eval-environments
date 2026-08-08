# Scientific Evaluation Environments

> **English** | [简体中文](./zh/README.md)

An open knowledge base documenting the design space of **scientific evaluation environments** for AI agents — benchmarks, evaluation methodology, evaluation frameworks, trajectory evaluation, resource-aware evaluation, and scientific workflows.

This repository is **not** a benchmark implementation. It is a reference manual, intended to remain useful to anyone working on scientific evaluation regardless of what tools or benchmarks they build.

---

## Repository Structure

```
scientific-eval-environments/
├── README.md              # This file
├── AGENT.md               # Repository constitution — read before contributing
├── CLAUDE.md              # Quick reference for the constitution
├── works/                 # One Markdown card per work (factual references)
│   ├── README.md          # Card template and rules
│   └── ...                # 73 cards, flat, kebab-case — one file per work
├── topics/                # Literature-review pages, one per canonical topic
│   ├── README.md          # Topic page template and rules
│   ├── credit_assignment.md
│   ├── long_horizon_evaluation.md
│   ├── resource_aware_evaluation.md
│   ├── scientific_agents.md
│   ├── skill_hierarchy.md
│   ├── survey.md
│   └── trajectory_evaluation.md
├── domains/               # Index pages, one per science/engineering domain
│   ├── README.md          # Domain page template and rules
│   └── ...                # 19 domain pages, snake_case — one file per domain
└── zh/                    # Chinese mirror (synced after every English batch)
    ├── README.md
    ├── works/
    ├── topics/
    └── domains/
```

The repository has **two knowledge layers plus one index layer**:

- **`works/`** — flat directory, one Markdown page per work. Cards are factual references. "Works" is broader than "benchmarks": the layer holds cards for benchmarks, evaluation methodologies, evaluation frameworks (diagnostic overlays, trace-analysis systems, ground-truth generation toolkits), evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly.
- **`topics/`** — literature-review pages, each covering one canonical evaluation direction. Each topic owns its own comparison table and its own dimensions. There is **no global comparison matrix**.
- **`domains/`** — index pages aggregating works by the **science or engineering domain they evaluate in**. This is an orthogonal axis to topics: topics group by evaluation *methodology*, domains by *field*. Each domain page carries a scope note, a comparison table with fixed columns (scientific problem, task form & scale, domain verification — identical on every domain page), and a linked work list; methodology synthesis stays in topic pages. Works without a science or engineering domain (web/UI agents, computer use, evaluation methodology, surveys) do not appear in the domain index.

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. That mapping is expressed twice — in the card's `Topics` block and in each topic page's `Related Works` section — and the two sides are kept in sync as a maintenance discipline.

---

## Canonical Topic Taxonomy

Topics are organized around this fixed set:

| # | Topic | File |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | [`long_horizon_evaluation.md`](./topics/long_horizon_evaluation.md) |
| II | Scientific Agent Benchmarks | [`scientific_agents.md`](./topics/scientific_agents.md) |
| III | Trajectory Evaluation | [`trajectory_evaluation.md`](./topics/trajectory_evaluation.md) |
| IV | Skill Hierarchy | [`skill_hierarchy.md`](./topics/skill_hierarchy.md) |
| V | Credit Assignment | [`credit_assignment.md`](./topics/credit_assignment.md) |
| VI | Resource-aware Evaluation | [`resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md) |
| VII | Survey | [`survey.md`](./topics/survey.md) |

Skill Hierarchy and Credit Assignment are independent topics.

---

## Canonical Domain Taxonomy

Domains are organized around a fixed set of 19 science and engineering fields in two groups (full table with fold rules in [`AGENT.md`](./AGENT.md)):

- **Science:** Physics, Astronomy, Mathematics, Chemistry, Biology, Neuroscience & Cognitive Science, Medicine & Health, Earth Science, Environmental Science, Materials Science, Computer Science, AI & Machine Learning Research.
- **Engineering:** Mechanical & Aerospace, Electrical, Energy Systems, Chemical, Civil & Structural, Robotics, Software & Systems.

Narrower fields fold into canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, …), and a work may appear in several domains. UI and computer-use environments are not science or engineering domains.

---

## How to Read This Repository

Topics are the primary entry point. If you are new to a research direction, start there:

```
Topic  →  Representative works  →  Original papers
```

If you arrive with a field rather than a methodology in mind, start from the domain index instead:

```
Domain  →  Works evaluated in that domain  →  Original papers
```

- Want to understand **how trajectories are scored**? Read [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md).
- Want to understand **how resource consumption enters evaluation**? Read [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md).
- Want to know **what exists for physics or fluid dynamics**? Read [`domains/physics.md`](./domains/physics.md) or [`domains/mechanical_aerospace_engineering.md`](./domains/mechanical_aerospace_engineering.md).
- Want the facts about a specific work? Read its card in [`works/`](./works/).

---

## Filename Conventions

- **Evaluation-direction topics** use the `_evaluation.md` suffix: `trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader topics** keep natural names: `scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`.
- **Work cards** use kebab-case matching the work's canonical name: `agentboard.md`, `t-eval.md`, `long-horizon-terminal-bench.md`.
- **Domain pages** use snake_case matching the domain name: `materials_science.md`, `software_systems_engineering.md`.

---

## Contributing

Before making changes, read [`AGENT.md`](./AGENT.md). It defines the constitution:

- Two-level reference validation. *Link validation* (title, URL, project, venue, year) and *content validation* (statistics, task counts, metrics — from the **original paper or official project only**, never secondary sources). Unverifiable content becomes `TODO(reference)`.
- Objective only — no "our benchmark" / "our approach" / positioning language.
- Repository Notes are conservative. Any observation not stated by the paper is prefixed `Repository note:`, and speculative critique / opinion / extrapolation is not allowed.
- Template stability — do not churn the work-card template; new evaluation dimensions extend topic pages, not card fields.
- English canonical, Chinese mirrored under `zh/`, synced after every English batch — not deferred.

Layer-specific rules live in [`works/README.md`](./works/README.md), [`topics/README.md`](./topics/README.md), and [`domains/README.md`](./domains/README.md).

---

## Bilingual Documentation

English is the canonical source. Chinese pages mirror the English tree under `zh/` (`zh/works/`, `zh/topics/`, `zh/domains/`) and are synchronized after every English batch.

---

## Scope

**In scope:** scientific evaluation environments, benchmark landscape, evaluation methodology, evaluation frameworks, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design, and evaluation-focused RL work on agents (reward design, credit-assignment methods, off-policy evaluation of agent trajectories).

**Out of scope (for now):** pure RL algorithm development, policy optimization and training procedures, agent implementation, multi-agent systems, memory systems.

The RL cutline is judged by the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

---

## Status

All seven canonical topic pages are written, and card coverage has grown well past the initial reference list:

- **73 cards** in `works/` — benchmarks, evaluation frameworks and methodologies, and reference papers (surveys and position papers). Each card notes its type explicitly; the flat directory itself is the authoritative list.
- **7 topic pages** — full literature reviews with topic-specific comparison tables and open questions. Current Related-Works coverage per topic: Scientific Agent Benchmarks (24), Trajectory Evaluation (20), General Long-Horizon Agent Benchmarks (17), Credit Assignment (13), Skill Hierarchy (7), Resource-aware Evaluation (7), Survey (4).
- **19 domain pages** — an index of works by science/engineering domain, with the largest coverage currently in Biology, Mathematics, Physics, and Software & Systems Engineering.
- **Chinese mirrors** under `zh/` kept in sync per the bilingual cadence.
