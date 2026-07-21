# Scientific Evaluation Environments

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
│   ├── README.md
│   ├── agent-evaluation-survey.md
│   ├── agentatlas.md
│   ├── agentboard.md
│   ├── agents-last-exam.md
│   ├── airs-bench.md
│   ├── costbench.md
│   ├── enconda-bench.md
│   ├── fintrace.md
│   ├── from-chatbot-to-digital-colleague.md
│   ├── gate.md
│   ├── insights-generator.md
│   ├── long-horizon-terminal-bench.md
│   ├── medhelm.md
│   ├── naturebench.md
│   ├── simulcost.md
│   ├── t-eval.md
│   ├── terminal-bench-science.md
│   ├── trace.md
│   ├── traxgen.md
│   └── uniclawbench.md
├── topics/                # Literature-review pages, one per canonical topic
│   ├── README.md
│   ├── credit_assignment.md
│   ├── long_horizon_evaluation.md
│   ├── resource_aware_evaluation.md
│   ├── scientific_agents.md
│   ├── skill_hierarchy.md
│   ├── survey.md
│   └── trajectory_evaluation.md
└── zh/                    # Chinese mirror (synced after every English batch)
    ├── README.md
    ├── works/
    └── topics/
```

The repository has **only two knowledge layers**:

- **`works/`** — flat directory, one Markdown page per work. Cards are factual references. "Works" is broader than "benchmarks": the layer holds cards for benchmarks, evaluation methodologies, evaluation frameworks (diagnostic overlays, trace-analysis systems, ground-truth generation toolkits), evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly.
- **`topics/`** — literature-review pages, each covering one canonical evaluation direction. Each topic owns its own comparison table and its own dimensions. There is **no global comparison matrix**.

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

## How to Read This Repository

Topics are the primary entry point. If you are new to a research direction, start there:

```
Topic  →  Representative works  →  Original papers
```

- Want to understand **how trajectories are scored**? Read [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md).
- Want to understand **how resource consumption enters evaluation**? Read [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md).
- Want the facts about a specific work? Read its card in [`works/`](./works/).

---

## Filename Conventions

- **Evaluation-direction topics** use the `_evaluation.md` suffix: `trajectory_evaluation.md`, `resource_aware_evaluation.md`, `long_horizon_evaluation.md`.
- **Broader topics** keep natural names: `scientific_agents.md`, `skill_hierarchy.md`, `credit_assignment.md`, `survey.md`.
- **Work cards** use kebab-case matching the work's canonical name: `agentboard.md`, `t-eval.md`, `long-horizon-terminal-bench.md`.

---

## Contributing

Before making changes, read [`AGENT.md`](./AGENT.md). It defines the constitution:

- Two-level reference validation. *Link validation* (title, URL, project, venue, year) and *content validation* (statistics, task counts, metrics — from the **original paper or official project only**, never secondary sources). Unverifiable content becomes `TODO(reference)`.
- Objective only — no "our benchmark" / "our approach" / positioning language.
- Repository Notes are conservative. Any observation not stated by the paper is prefixed `Repository note:`, and speculative critique / opinion / extrapolation is not allowed.
- Template stability — do not churn the work-card template; new evaluation dimensions extend topic pages, not card fields.
- English canonical, Chinese mirrored under `zh/`, synced after every English batch — not deferred.

Layer-specific rules live in [`works/README.md`](./works/README.md) and [`topics/README.md`](./topics/README.md).

---

## Bilingual Documentation

English is the canonical source. Chinese pages mirror the English tree under `zh/` (`zh/works/`, `zh/topics/`) and are synchronized after every English batch.

---

## Scope

**In scope:** scientific evaluation environments, benchmark landscape, evaluation methodology, evaluation frameworks, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design, and evaluation-focused RL work on agents (reward design, credit-assignment methods, off-policy evaluation of agent trajectories).

**Out of scope (for now):** pure RL algorithm development, policy optimization and training procedures, agent implementation, multi-agent systems, memory systems.

The RL cutline is judged by the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

---

## Status

Full coverage of the initial reference list. All seven canonical topic pages are written:

- **24 cards** in `works/`:
  - **Benchmark cards (16)**: AgentBoard, Agents' Last Exam, AIRS-Bench, CATP-LLM / OpenCATP, CostBench, Enconda-bench, FinTrace, Long-Horizon-Terminal-Bench, MedHELM, NatureBench, ScienceAgentBench, SimulCost, T-Eval, Terminal-Bench Science, TRACE, UniClawBench.
  - **Framework / methodology cards (3)**: AgentAtlas (audit protocol), Insights Generator (corpus-level trace diagnostics), Traxgen (deterministic ground-truth trajectory generation toolkit).
  - **Reference-paper cards (4)**: *Survey on Evaluation of LLM-based Agents* (Yehudai et al., 2025), *Evaluation and Benchmarking of LLM Agents: A Survey* (Mohammadi et al., 2025), *A Survey on Large Language Model based Autonomous Agents* (Wang et al., 2023), *From Chatbot to Digital Colleague* (Zhang et al., 2026).
  - **Included with an explicit scope caveat (1)**: GATE — actual paper is about tool making, not skill-hierarchy evaluation as the initial reference list suggested; card carries a repository-note flagging this.
- **7 topic pages** — full literature reviews with topic-specific comparison tables and open questions.
- **Chinese mirrors** kept in sync per bilingual cadence.
