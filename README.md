# Scientific Evaluation Environments

An open knowledge base documenting the design space of **scientific evaluation environments** for AI agents — benchmarks, evaluation methodology, trajectory evaluation, resource-aware evaluation, and scientific workflows.

This repository is **not** a benchmark implementation. It is a reference manual, intended to remain useful to anyone working on scientific evaluation regardless of what tools or benchmarks they build.

---

## Repository Structure

```
scientific-eval-environments/
├── README.md              # This file
├── AGENT.md               # Repository constitution — read before contributing
├── CLAUDE.md              # Quick reference for the constitution
├── benchmarks/            # One Markdown card per benchmark (factual references)
│   ├── README.md          # Card template + card-writing rules
│   ├── agentboard.md
│   ├── costbench.md
│   └── t-eval.md
├── topics/                # Literature-review pages, one per canonical topic
│   ├── README.md          # Topic template + filename conventions
│   ├── resource_aware_evaluation.md
│   └── trajectory_evaluation.md
└── zh/                    # Chinese mirror (synced after every English batch)
    ├── README.md
    ├── benchmarks/
    └── topics/
```

The repository has **only two knowledge layers**:

- **`benchmarks/`** — flat directory, one Markdown page per benchmark. Cards are factual: what the benchmark is, what it evaluates, how it scores. No synthesis, no positioning.
- **`topics/`** — literature-review pages, each covering one canonical evaluation direction. Each topic owns its own comparison table and its own dimensions. There is **no global benchmark matrix**.

**Topics are not mutually exclusive.** A benchmark may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. That mapping is expressed twice — in the card's `Topics` block and in each topic page's `Related Benchmarks` section — and the two sides are kept in sync as a maintenance discipline.

---

## Canonical Topic Taxonomy

Topics are organized around this fixed set:

| # | Topic | File |
|---|---|---|
| I | General Long-Horizon Agent Benchmarks | [`long_horizon_evaluation.md`](./topics/long_horizon_evaluation.md) *(pending)* |
| II | Scientific Agent Benchmarks | [`scientific_agents.md`](./topics/scientific_agents.md) *(pending)* |
| III | Trajectory Evaluation | [`trajectory_evaluation.md`](./topics/trajectory_evaluation.md) |
| IV | Skill Hierarchy | [`skill_hierarchy.md`](./topics/skill_hierarchy.md) *(pending)* |
| V | Credit Assignment | [`credit_assignment.md`](./topics/credit_assignment.md) *(pending)* |
| VI | Resource-aware Evaluation | [`resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md) |
| VII | Survey | [`survey.md`](./topics/survey.md) *(pending)* |

Skill Hierarchy and Credit Assignment are independent topics.

---

## How to Read This Repository

Topics are the primary entry point. If you are new to a research direction, start there:

```
Topic  →  Representative benchmarks  →  Original papers
```

- Want to understand **how trajectories are scored**? Read [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md) and follow the links.
- Want to understand **how resource consumption enters evaluation**? Read [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md).
- Want the facts about a specific benchmark? Read its card in [`benchmarks/`](./benchmarks/).

---

## Filename Conventions

- **Evaluation-direction topics** use the `_evaluation.md` suffix: `trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader topics** keep natural names: `scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`.
- **Benchmark cards** use kebab-case matching the benchmark's canonical name: `agentboard.md`, `t-eval.md`, `costbench.md`.

---

## Contributing

Before making changes, read [`AGENT.md`](./AGENT.md). It defines the constitution:

- Two-level reference validation. *Link validation* (title, URL, project, venue, year) and *content validation* (benchmark statistics, task counts, metrics — from the **original paper or official project only**, never secondary sources). Unverifiable content becomes `TODO(reference)`.
- Objective only — no "our benchmark" / "our approach" / positioning language.
- Repository Notes are conservative. Any observation not stated by the paper is prefixed `Repository note:`, and speculative critique / opinion / extrapolation is not allowed.
- Template stability — do not churn the benchmark-card template; new evaluation dimensions extend topic pages, not card fields.
- English canonical, Chinese mirrored under `zh/`, synced after every English batch — not deferred.

Layer-specific rules live in [`benchmarks/README.md`](./benchmarks/README.md) and [`topics/README.md`](./topics/README.md).

---

## Bilingual Documentation

English is the canonical source. Chinese pages mirror the English tree under `zh/` (`zh/benchmarks/`, `zh/topics/`) and are synchronized after every English batch.

---

## Scope

**In scope:** scientific evaluation environments, benchmark landscape, evaluation methodology, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design.

**Out of scope (for now):** RL training and algorithms, policy optimization, agent implementation, multi-agent systems, memory systems.

---

## Status

Early build. The layer structure and canonical topic taxonomy are in place. A first set of examples is written: 3 benchmark cards (AgentBoard, T-Eval, CostBench) and 2 topic pages (Trajectory Evaluation, Resource-aware Evaluation). Chinese mirrors are kept in sync. Coverage of the remaining 5 canonical topics and the broader benchmark landscape will grow batch by batch, with references verified against the primary source at every step.
