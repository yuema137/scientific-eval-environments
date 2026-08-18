

# Scientific Evaluation Environments

> **English** | [简体中文](./zh/README.md)

An open knowledge base on **how AI agents are evaluated on scientific and long-horizon tasks**. It documents the design space — benchmarks, evaluation methodologies, evaluation frameworks, trajectory and resource-aware evaluation, scientific workflows, and evaluation-focused RL work on agents.

Each piece of work has a concise, factual reference card. Cards are organized along three independent axes: **topics** (the evaluation methodology), **domains** (the scientific field), and **activities** (what the evaluated agent actually does). Start from whichever question you arrive with, follow the links to representative works, and go on to the original papers.

This is a reference, not a benchmark implementation — it aims to stay useful to anyone working on scientific evaluation, whatever tools they build.

---

## A Living Knowledge Base

Scientific Evaluation Environments is continuously maintained rather than periodically released. An automated update agent scans public sources every three days for new work, integrates relevant additions into the knowledge base, and proposes updates through pull requests for human review.

---

## Start Exploring

- **[Browse by Topic](./topics/README.md)** — explore research themes in scientific-agent and agent-evaluation methodology.
- **[Browse by Domain](./domains/README.md)** — explore evaluation work within a scientific or engineering field.
- **[Browse by Research Activity](./activities/README.md)** — explore works by what the evaluated agent or system actually does.
- **[Browse All Works](./works/README.md)** — the complete collection of indexed work cards.

The three axes are co-equal entry points over the same cards:

```
Topic     →  Representative works            →  Original papers   (why / how we evaluate)
Domain    →  Works evaluated in that domain  →  Original papers   (where the task lives)
Activity  →  Works performing that task      →  Original papers   (what the agent does)
```

A work may appear under several topics, domains, and activities — each is a different lens on the same work, not an exclusive bucket.

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
| [Physics](./domains/physics.md) | 47 |
| [Chemistry](./domains/chemistry.md) | 38 |
| [Biology](./domains/biology.md) | 38 |
| [Materials Science](./domains/materials_science.md) | 28 |
| [AI & Machine Learning Research](./domains/ai_ml_research.md) | 24 |
| [Mathematics](./domains/mathematics.md) | 19 |
| [Medicine & Health](./domains/medicine_health.md) | 22 |
| [Neuroscience & Cognitive Science](./domains/neuroscience_cognitive_science.md) | 12 |
| [Astronomy](./domains/astronomy.md) | 34 |
| [Earth Science](./domains/earth_science.md) | 12 |
| [Computer Science](./domains/computer_science.md) | 7 |
| [Environmental Science](./domains/environmental_science.md) | 6 |

**Engineering**

| Domain | Works |
|---|--:|
| [Electrical Engineering](./domains/electrical_engineering.md) | 18 |
| [Robotics](./domains/robotics.md) | 18 |
| [Software & Systems Engineering](./domains/software_systems_engineering.md) | 18 |
| [Mechanical & Aerospace Engineering](./domains/mechanical_aerospace_engineering.md) | 12 |
| [Energy Systems](./domains/energy_systems.md) | 5 |
| [Civil & Structural Engineering](./domains/civil_structural_engineering.md) | 30 |
| [Chemical Engineering](./domains/chemical_engineering.md) | 12 |

Narrower fields fold into these canonical domains (bioinformatics → Biology, GIS → Earth Science, psychology → Neuroscience & Cognitive Science, …), and a work may appear in several domains. Web/UI agents, computer use, and pure evaluation methodology are not science or engineering domains and do not appear here.

---

## Browse by Research Activity

Activities are the **task axis**: what the evaluated agent or system actually does, independent of field or evaluation method. A work may perform several activities; works that evaluate no scientific or research task (surveys, pure methodology, general-purpose benchmarks) carry an explicit `N/A` and appear on no activity page. Full index in [`activities/`](./activities/README.md).

| Activity | What it covers | Works |
|---|---|--:|
| [Scientific Problem Solving & Reasoning](./activities/scientific_problem_solving_reasoning.md) | Scientific QA, derivations, proofs, quantitative and multimodal problem solving, diagnostic reasoning | 94 |
| [Scientific Software & Workflow Engineering](./activities/scientific_software_workflow_engineering.md) | Scientific/engineering code, repository and pipeline engineering, HDL and formal-spec code | 71 |
| [Data Analysis & Statistical Inference](./activities/data_analysis_statistical_inference.md) | Statistical analysis and inference, bioinformatics/omics analysis, data interpretation | 43 |
| [Experiment Design & Scientific Discovery](./activities/experiment_design_discovery.md) | Experiment and observation planning, hypothesis generation, law discovery | 22 |
| [Simulation & Scientific Computing](./activities/simulation_scientific_computing.md) | Numerical simulation, PDE/FEM, MD/DFT, running and building scientific simulators | 35 |
| [Modeling & Prediction](./activities/modeling_prediction.md) | Predictive and surrogate modelling, property prediction, forecasting | 21 |
| [Optimization & Engineering Design](./activities/optimization_engineering_design.md) | Parameter and controller tuning, engineering/inverse design, materials and molecular design | 26 |
| [Literature Search & Evidence Synthesis](./activities/literature_evidence_synthesis.md) | Literature retrieval, systematic review, evidence synthesis, literature-grounded extraction | 23 |
| [Research Reproduction & Replication](./activities/research_reproduction_replication.md) | Reproducing published analyses, results, and methods; matching reported findings | 11 |
| [End-to-End Research](./activities/end_to_end_research.md) | Multi-stage research lifecycle across several major phases | 6 |
| [Laboratory & Instrument Control](./activities/laboratory_instrument_control.md) | Instrument, microscope, and beamline control; lab automation; behaviour-defined control code | 3 |

---

## Scope

**In scope:** scientific evaluation environments, the benchmark landscape, evaluation methodology, evaluation frameworks, scientific workflows, trajectory evaluation, resource-aware evaluation, benchmark design, and evaluation-focused RL work on agents (reward design, credit-assignment methods, off-policy evaluation of agent trajectories).

**Out of scope (for now):** pure RL algorithm development, policy optimization and training procedures, agent implementation, multi-agent systems, memory systems.

The RL cutline is judged by the paper's primary contribution: if it advances *how agents are evaluated*, it belongs here; if it advances *how agents are trained*, it does not.

"Works" is broader than "benchmarks": the collection holds cards for benchmarks, evaluation methodologies, evaluation frameworks, evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly. The collection currently holds **364 work cards**, **7 topic pages**, **19 domain pages**, and **11 activity pages**, each mirrored in Chinese under [`zh/`](./zh/README.md).

---

## Repository Structure

The knowledge base has **four layers**: the works layer, plus three co-equal aggregation axes over it.

| Directory | Role |
|---|---|
| [`works/`](./works/README.md) | One factual reference card per work. Flat, kebab-case, one Markdown file each. |
| [`topics/`](./topics/README.md) | Literature-review pages — the methodology axis. Each topic owns its own comparison table; there is no global matrix. |
| [`domains/`](./domains/README.md) | Field-axis reference pages, one per canonical science or engineering domain, with a fixed-column comparison table. |
| [`activities/`](./activities/README.md) | Task-axis reference pages, one per canonical research activity, with Definition, Scope, task patterns, and a comparison table. |
| [`zh/`](./zh/README.md) | Chinese mirror of every page, synced after each English batch. |

Two navigational conventions keep the axes in sync: each card's `Topics` block links up to its topics, and each topic page's `Related Works` links back down to its cards. The domain mapping is maintained one-way on the domain pages. Root-level [`AGENT.md`](./AGENT.md) is the repository constitution and [`CLAUDE.md`](./CLAUDE.md) is its quick reference; each directory's own `README.md` documents its page template and rules.

---

## Contributing

Contributions are welcome. Automated updates complement, rather than replace, community contributions; missing or newly relevant work can still be proposed manually. All contributor and maintainer rules — reference validation, page templates, the canonical taxonomies, and the bilingual sync cadence — live in [`AGENT.md`](./AGENT.md) (the constitution) and [`CLAUDE.md`](./CLAUDE.md) (its quick reference), with layer-specific rules in each directory's README. Every page is available in English and Chinese; use the language switcher at the top of any page.
