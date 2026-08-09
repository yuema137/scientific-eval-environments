# Scientific Evaluation Environments

> **English** | [简体中文](./zh/README.md)

An open knowledge base on **how AI agents are evaluated on scientific and long-horizon tasks**. It documents the design space — benchmarks, evaluation methodologies, evaluation frameworks, trajectory and resource-aware evaluation, scientific workflows, and evaluation-focused RL work on agents.

Each piece of work has a concise, factual reference card. Cards are organized along two independent axes: **topics** (the evaluation methodology) and **domains** (the scientific field). Start from whichever question you arrive with, follow the links to representative works, and go on to the original papers.

This is a reference, not a benchmark implementation — it aims to stay useful to anyone working on scientific evaluation, whatever tools they build.

---

## Start Exploring

- **[Browse by Topic](./topics/README.md)** — explore research themes in scientific-agent and agent-evaluation methodology.
- **[Browse by Domain](./domains/README.md)** — explore evaluation work within a scientific or engineering field.
- **[Browse All Works](./works/README.md)** — the complete collection of indexed work cards.

The two axes are co-equal entry points over the same cards:

```
Topic   →  Representative works            →  Original papers
Domain  →  Works evaluated in that domain  →  Original papers
```

A work may appear under several topics and several domains — each is a different lens on the same work, not an exclusive bucket.

---

## Browse by Topic

Topics are the **methodology axis**: how agents are evaluated. Each page is a literature review with its own comparison table. See [`topics/`](./topics/README.md) for the full index.

| Topic | What you'll find |
|---|---|
| [General Long-Horizon Agent Benchmarks](./topics/long_horizon_evaluation.md) | Benchmarks whose tasks need many sequential decisions, tool calls, or turns — where failures accumulate and intermediate state matters. |
| [Scientific Agent Benchmarks](./topics/scientific_agents.md) | Agents on tasks drawn from real scientific research and practice, judged against published or expert-defined outcomes. |
| [Trajectory Evaluation](./topics/trajectory_evaluation.md) | Methods that score the whole sequence of actions and intermediate states, not just the final answer. |
| [Skill Hierarchy](./topics/skill_hierarchy.md) | Decomposing a complex capability into narrower subskills, each scored separately. |
| [Credit Assignment](./topics/credit_assignment.md) | Attributing a trajectory's success or failure to specific steps or subgoals — dense rewards, partial credit, per-step scoring. |
| [Resource-aware Evaluation](./topics/resource_aware_evaluation.md) | Treating tokens, fees, wall-clock time, or compute as part of what the benchmark measures — sometimes as an explicit objective. |
| [Survey](./topics/survey.md) | Surveys and position papers on agent evaluation — an index of references rather than a task suite. |

---

## Browse by Domain

Domains are the **field axis**: the science or engineering discipline a work evaluates in, co-equal with topics. Work counts show current coverage; the authoritative index and per-page tables live in [`domains/`](./domains/README.md).

**Sciences**

| Domain | Works |
|---|--:|
| [Physics](./domains/physics.md) | 35 |
| [Chemistry](./domains/chemistry.md) | 28 |
| [Biology](./domains/biology.md) | 25 |
| [Materials Science](./domains/materials_science.md) | 23 |
| [AI & Machine Learning Research](./domains/ai_ml_research.md) | 21 |
| [Mathematics](./domains/mathematics.md) | 12 |
| [Medicine & Health](./domains/medicine_health.md) | 12 |
| [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | 10 |
| [Astronomy](./domains/astronomy.md) | 5 |
| [Earth Science](./domains/earth_science.md) | 5 |
| [Computer Science](./domains/computer_science.md) | 4 |
| [Environmental Science](./domains/environmental_science.md) | 2 |

**Engineering**

| Domain | Works |
|---|--:|
| [Electrical Engineering](./domains/electrical_engineering.md) | 15 |
| [Robotics](./domains/robotics.md) | 14 |
| [Software & Systems Engineering](./domains/software_systems_engineering.md) | 11 |
| [Mechanical & Aerospace Engineering](./domains/mechanical_aerospace_engineering.md) | 9 |
| [Energy Systems](./domains/energy_systems.md) | 3 |
| [Civil & Structural Engineering](./domains/civil_structural_engineering.md) | 2 |
| [Chemical Engineering](./domains/chemical_engineering.md) | 1 |

Narrower fields fold into these canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, …), and a work may appear in several domains. Web/UI agents, computer use, and pure evaluation methodology are not science or engineering domains and do not appear here.

---

## Scope

**In scope:** scientific evaluation environments, the benchmark landscape, evaluation methodology, evaluation frameworks, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design, and evaluation-focused RL work on agents (reward design, credit-assignment methods, off-policy evaluation of agent trajectories).

**Out of scope (for now):** pure RL algorithm development, policy optimization and training procedures, agent implementation, multi-agent systems, memory systems.

The RL cutline is judged by the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

"Works" is broader than "benchmarks": the collection holds cards for benchmarks, evaluation methodologies, evaluation frameworks, evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly. The collection currently holds **238 work cards**, **7 topic pages**, and **19 domain pages**, each mirrored in Chinese under [`zh/`](./zh/README.md).

---

## Repository Structure

The knowledge base has **three layers**: the works layer, plus two co-equal aggregation axes over it.

| Directory | Role |
|---|---|
| [`works/`](./works/README.md) | One factual reference card per work. Flat, kebab-case, one Markdown file each. |
| [`topics/`](./topics/README.md) | Literature-review pages — the methodology axis. Each topic owns its own comparison table; there is no global matrix. |
| [`domains/`](./domains/README.md) | Field-axis reference pages, one per canonical science or engineering domain, with a fixed-column comparison table. |
| [`zh/`](./zh/README.md) | Chinese mirror of every page, synced after each English batch. |

Two navigational conventions keep the axes in sync: each card's `Topics` block links up to its topics, and each topic page's `Related Works` links back down to its cards. The domain mapping is maintained one-way on the domain pages. Root-level [`AGENT.md`](./AGENT.md) is the repository constitution and [`CLAUDE.md`](./CLAUDE.md) is its quick reference; each directory's own `README.md` documents its page template and rules.

---

## Contributing

Contributions are welcome. All contributor and maintainer rules — reference validation, page templates, the canonical taxonomies, and the bilingual sync cadence — live in [`AGENT.md`](./AGENT.md) (the constitution) and [`CLAUDE.md`](./CLAUDE.md) (its quick reference), with layer-specific rules in each directory's README. Every page is available in English and Chinese; use the language switcher at the top of any page.
