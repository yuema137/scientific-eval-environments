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
│   └── ...                # 222 cards, flat, kebab-case — one file per work
├── topics/                # Literature-review pages, one per canonical topic
│   ├── README.md          # Topic page template and rules
│   ├── credit_assignment.md
│   ├── long_horizon_evaluation.md
│   ├── resource_aware_evaluation.md
│   ├── scientific_agents.md
│   ├── skill_hierarchy.md
│   ├── survey.md
│   └── trajectory_evaluation.md
├── domains/               # Field-axis reference pages, one per canonical domain
│   ├── README.md          # Domain page template and rules
│   └── ...                # 19 domain pages, snake_case — one file per domain
└── zh/                    # Chinese mirror (synced after every English batch)
    ├── README.md
    ├── works/
    ├── topics/
    └── domains/
```

The repository has **three knowledge layers** — works, plus two co-equal aggregation axes over them:

- **`works/`** — flat directory, one Markdown page per work. Cards are factual references. "Works" is broader than "benchmarks": the layer holds cards for benchmarks, evaluation methodologies, evaluation frameworks (diagnostic overlays, trace-analysis systems, ground-truth generation toolkits), evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly.
- **`topics/`** — literature-review pages, each covering one canonical evaluation direction. Each topic owns its own comparison table and its own dimensions. There is **no global comparison matrix**.
- **`domains/`** — reference pages aggregating works by the **science or engineering domain they evaluate in**. This is the **field axis**, orthogonal and equal in standing to topics: topics group by evaluation *methodology*, domains by *field*. Each domain page carries a scope note, a comparison table with fixed columns (scientific problem, task form & scale, domain verification — identical on every domain page), and a linked work list; methodology synthesis stays in topic pages. Works without a science or engineering domain (web/UI agents, computer use, evaluation methodology, surveys) do not appear in the domain layer.

**Topics are not mutually exclusive.** A work may naturally belong to multiple topics, because each topic represents a different literature perspective rather than a unique category. You can move in either direction: each card's `Topics` block links up to its topics, and each topic page's `Related Works` links down to its cards.

---

## Canonical Topic Taxonomy

Topics are organized around this fixed set:

| # | Topic | File |
|---|---|---|
| I | [General Long-Horizon Agent Benchmarks](./topics/long_horizon_evaluation.md) | `long_horizon_evaluation.md` |
| II | [Scientific Agent Benchmarks](./topics/scientific_agents.md) | `scientific_agents.md` |
| III | [Trajectory Evaluation](./topics/trajectory_evaluation.md) | `trajectory_evaluation.md` |
| IV | [Skill Hierarchy](./topics/skill_hierarchy.md) | `skill_hierarchy.md` |
| V | [Credit Assignment](./topics/credit_assignment.md) | `credit_assignment.md` |
| VI | [Resource-aware Evaluation](./topics/resource_aware_evaluation.md) | `resource_aware_evaluation.md` |
| VII | [Survey](./topics/survey.md) | `survey.md` |

Skill Hierarchy and Credit Assignment are independent topics.

---

## Canonical Domain Taxonomy

Domains are organized around this fixed set of 19 science and engineering fields:

| Group | Domain | File |
|---|---|---|
| Science | [Physics](./domains/physics.md) | `physics.md` |
| Science | [Astronomy](./domains/astronomy.md) | `astronomy.md` |
| Science | [Mathematics](./domains/mathematics.md) | `mathematics.md` |
| Science | [Chemistry](./domains/chemistry.md) | `chemistry.md` |
| Science | [Biology](./domains/biology.md) | `biology.md` |
| Science | [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | `neuroscience_cognitive_science.md` |
| Science | [Medicine & Health](./domains/medicine_health.md) | `medicine_health.md` |
| Science | [Earth Science](./domains/earth_science.md) | `earth_science.md` |
| Science | [Environmental Science](./domains/environmental_science.md) | `environmental_science.md` |
| Science | [Materials Science](./domains/materials_science.md) | `materials_science.md` |
| Science | [Computer Science](./domains/computer_science.md) | `computer_science.md` |
| Science | [AI & Machine Learning Research](./domains/ai_ml_research.md) | `ai_ml_research.md` |
| Engineering | [Mechanical & Aerospace Engineering](./domains/mechanical_aerospace_engineering.md) | `mechanical_aerospace_engineering.md` |
| Engineering | [Electrical Engineering](./domains/electrical_engineering.md) | `electrical_engineering.md` |
| Engineering | [Energy Systems](./domains/energy_systems.md) | `energy_systems.md` |
| Engineering | [Chemical Engineering](./domains/chemical_engineering.md) | `chemical_engineering.md` |
| Engineering | [Civil & Structural Engineering](./domains/civil_structural_engineering.md) | `civil_structural_engineering.md` |
| Engineering | [Robotics](./domains/robotics.md) | `robotics.md` |
| Engineering | [Software & Systems Engineering](./domains/software_systems_engineering.md) | `software_systems_engineering.md` |

Narrower fields fold into canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, …), and a work may appear in several domains. UI and computer-use environments are not science or engineering domains. Per-domain work counts and the full rules live in [`domains/README.md`](./domains/README.md) and [`AGENT.md`](./AGENT.md).

---

## How to Read This Repository

There are two co-equal entry points, one per axis. If you arrive with a methodology question, start from topics; if you arrive with a field in mind, start from domains:

```
Topic   →  Representative works            →  Original papers
Domain  →  Works evaluated in that domain  →  Original papers
```

- Want to understand **how trajectories are scored**? Read [`topics/trajectory_evaluation.md`](./topics/trajectory_evaluation.md).
- Want to understand **how resource consumption enters evaluation**? Read [`topics/resource_aware_evaluation.md`](./topics/resource_aware_evaluation.md).
- Want to know **what exists for physics or fluid dynamics**? Read [`domains/physics.md`](./domains/physics.md) or [`domains/mechanical_aerospace_engineering.md`](./domains/mechanical_aerospace_engineering.md).
- Want the facts about a specific work? Read its card in [`works/`](./works/).

---

## Languages

Every page is available in English and Chinese. Use the language switcher at the top of any page (**English** | 简体中文); the Chinese mirror lives under [`zh/`](./zh/README.md).

---

## Contributing

Contributions are welcome. All contributor and maintainer rules — reference validation, page templates, taxonomies, and the bilingual sync cadence — live in [`AGENT.md`](./AGENT.md) (the constitution) and [`CLAUDE.md`](./CLAUDE.md) (its quick reference), with layer-specific rules in each directory's README.

---

## Scope

**In scope:** scientific evaluation environments, benchmark landscape, evaluation methodology, evaluation frameworks, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design, and evaluation-focused RL work on agents (reward design, credit-assignment methods, off-policy evaluation of agent trajectories).

**Out of scope (for now):** pure RL algorithm development, policy optimization and training procedures, agent implementation, multi-agent systems, memory systems.

The RL cutline is judged by the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

---

## Status

All seven canonical topic pages are written, and card coverage has grown well past the initial reference list:

- **222 cards** in `works/` — benchmarks, evaluation frameworks and methodologies, and reference papers (surveys and position papers). Each card notes its type explicitly; the flat directory itself is the authoritative list.
- **7 topic pages** — full literature reviews with topic-specific comparison tables and open questions. Current Related-Works coverage per topic: Scientific Agent Benchmarks (24), Trajectory Evaluation (20), General Long-Horizon Agent Benchmarks (17), Credit Assignment (13), Skill Hierarchy (7), Resource-aware Evaluation (7), Survey (4).
- **19 domain pages** — field-axis reference pages, each with a fixed-column comparison table (scientific problem, task form & scale, domain verification per work); largest coverage currently in Biology, Mathematics, Physics, and Software & Systems Engineering.
- **Chinese mirrors** under `zh/` kept in sync per the bilingual cadence.
