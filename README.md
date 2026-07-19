# Scientific Evaluation Environments

An open knowledge base documenting the design space of **scientific evaluation environments** for AI agents — benchmarks, evaluation methodology, trajectory evaluation, cost-aware evaluation, and scientific workflows.

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
└── topics/                # Literature-review pages, one per evaluation direction
    ├── README.md          # Topic template + filename conventions
    ├── cost_aware_evaluation.md
    └── trajectory_evaluation.md
```

The repository has **only two knowledge layers**:

- **`benchmarks/`** — flat directory, one Markdown page per benchmark. Cards are factual: what the benchmark is, what it evaluates, how it scores. No synthesis, no positioning.
- **`topics/`** — literature-review pages, each covering one evaluation direction. Each topic owns its own comparison table and its own dimensions. There is **no global benchmark matrix**.

A benchmark can belong to multiple topics. That mapping is expressed twice — in the card's `Topics` block and in each topic page's `Related Benchmarks` section — and the two sides are kept in sync as a maintenance discipline.

---

## How to Read This Repository

Topics are the primary entry point. If you are new to a research direction, start there:

```
Topic  →  Representative benchmarks  →  Original papers
```

- Want to understand **how trajectories are scored**? Read [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md) and follow the links.
- Want to understand **how cost enters evaluation**? Read [`topics/cost_aware_evaluation.md`](./topics/cost_aware_evaluation.md).
- Want the facts about a specific benchmark? Read its card in [`benchmarks/`](./benchmarks/).

---

## Filename Conventions

- **Evaluation-direction topics** use the `_evaluation.md` suffix so the directory is self-explanatory: `trajectory_evaluation.md`, `cost_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader topics** keep natural names: `scientific_workflows.md`, `verifier_design.md`, `llm_judges.md`.
- **Benchmark cards** use kebab-case matching the benchmark's canonical name: `agentboard.md`, `t-eval.md`, `costbench.md`.

---

## Contributing

Before making changes, read [`AGENT.md`](./AGENT.md). It defines the constitution:

- Zero fabricated references — every URL, title, venue, and year is verified before commit; unverifiable facts become `TODO`.
- Objective only — no "our benchmark" / "our approach" / positioning language.
- Facts vs. observations — anything the repository adds (not stated by the paper) is prefixed `Repository note:`.
- Template stability — do not churn the benchmark-card template; new evaluation dimensions extend topic pages, not card fields.
- English canonical, Chinese mirrored under `zh/`.

Layer-specific rules live in [`benchmarks/README.md`](./benchmarks/README.md) and [`topics/README.md`](./topics/README.md).

---

## Bilingual Documentation

English is the canonical source. Chinese pages will mirror the English tree under `zh/` (`zh/benchmarks/`, `zh/topics/`) once the English content stabilizes.

---

## Scope

**In scope:** scientific evaluation environments, benchmark landscape, evaluation methodology, scientific workflows, trajectory evaluation, cost-aware evaluation, benchmark design.

**Out of scope (for now):** RL training and algorithms, policy optimization, agent implementation, multi-agent systems, memory systems.

---

## Status

Early build. The layer structure is in place and a first set of examples is written. Coverage of the broader benchmark landscape will grow topic by topic, with references verified against the primary source at every step.
