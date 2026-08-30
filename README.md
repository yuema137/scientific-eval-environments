

# Scientific Evaluation Environments

> **English** | [简体中文](./zh/README.md)

This repository tracks how scientific and engineering AI agents are evaluated, and how those results feed back into development.

The key idea is simple: a score should do more than say whether an agent won or lost. It should help someone decide what to change next. If a research agent fails to reproduce a paper, the useful question is whether the plan was wrong, a tool call failed, the verifier missed an error, or the system ran out of budget. Those diagnoses lead to different repairs.

The repository follows that loop:

```text
task → agent run → evaluation → diagnosis → intervention → new evaluation
```

One work card records what a paper or project actually contributes. Three independent indexes let readers approach that card from different questions: **topic** asks what evaluation problem it addresses, **domain** asks where the task lives, and **activity** asks what the agent does. Topic pages connect the cards into a literature map and explain where the methods differ.

This is a reference, not a benchmark implementation. The [Explanation Style Guide](./EXPLANATION_STYLE.md) governs the prose: name the actor, show the old path and the changed step, trace a real example when useful, and state the nearest limitation.

---

## A Living Knowledge Base

The collection changes as the field changes. Every three days, an update agent searches public sources for new work. It drafts cards and index updates, but does not publish them directly. Each batch arrives as a pull request so a person can check the sources, taxonomy, prose, and Chinese mirror before merge.

---

## Start Exploring

- **[Browse by Topic](./topics/README.md)** — start from an evaluation problem, see how one example changes, then compare the literature.
- **[Browse by Domain](./domains/README.md)** — find evaluation work within a scientific or engineering field.
- **[Browse by Research Activity](./activities/README.md)** — find works by the task the evaluated agent or system performs.
- **[Browse All Works](./works/README.md)** — open the complete collection of factual work cards.
- **[Browse Works by First Appearance](./WORKS_BY_DATE.md)** — view the collection from newest to oldest initial public appearance.
- **[Read Monthly Reports](./monthly/README.md)** — follow what entered the knowledge base each month and what changed across the literature.

Choose the entry point that matches the question you already have:

```
Topic     →  Representative works            →  Original papers   (what / how / how evaluation is used)
Domain    →  Works evaluated in that domain  →  Original papers   (where the task lives)
Activity  →  Works performing that task      →  Original papers   (what the agent does)
```

These are not competing classifications. A benchmark for a chemistry agent may belong to several topics, one domain, and several activities at the same time. Each link answers a different question about the same work.

---

## Browse by Topic

A topic starts with an evaluation problem. Some topics ask what behavior to measure, such as planning or long-horizon work. Others ask whether the measurement itself is trustworthy, or how its feedback changes skills, harnesses, data, and post-training. Each topic page explains that problem, groups the main approaches, and compares them using dimensions that fit the problem. See [`topics/`](./topics/README.md) for the full index.

| Topic | What you'll find |
|---|---|
| [General Long-Horizon Agent Benchmarks](./topics/long_horizon_evaluation.md) | Benchmarks whose tasks need many sequential decisions, tool calls, or turns — where failures accumulate and intermediate state matters. |
| [Scientific Agent Benchmarks](./topics/scientific_agents.md) | Agents on tasks drawn from real scientific research and practice, judged against published or expert-defined outcomes. |
| [Planning & Decision-Making Evaluation](./topics/planning_decision_evaluation.md) | Whether an agent selects a sound plan or next action from the current state, goals, constraints, tools, and evidence, and replans appropriately after feedback. |
| [Hierarchical Decision Abstraction](./topics/hierarchical_decision_abstraction.md) | How agent behavior should be represented, evaluated, and optimized across goals, strategies, subgoals, semantic actions, primitive actions, and control signals. |
| [Trajectory Evaluation](./topics/trajectory_evaluation.md) | Methods that score the whole sequence of actions and intermediate states, not just the final answer. |
| [Skill Hierarchy](./topics/skill_hierarchy.md) | Decomposing a complex capability into narrower subskills, each scored separately. |
| [Credit Assignment](./topics/credit_assignment.md) | Attributing a trajectory's success or failure to specific steps or subgoals — dense rewards, partial credit, per-step scoring. |
| [Resource-aware Evaluation](./topics/resource_aware_evaluation.md) | Treating tokens, fees, wall-clock time, or compute as part of what the benchmark measures — sometimes as an explicit objective. |
| [Evaluator Reliability & Validation](./topics/evaluator_reliability_validation.md) | Validating judges, reward models, rubrics, and verifiers against human or deterministic ground truth and downstream use. |
| [Benchmark Design, Validity & Contamination](./topics/benchmark_design_validity_contamination.md) | Task construction, verifier rigor, contamination resistance, dynamic evaluation, and ecological validity. |
| [Skill Learning & Evolution](./topics/skill_learning_evolution.md) | Turning experience and evaluation feedback into reusable skills, then testing transfer and failure modes. |
| [Agent Harnesses & Scaffolding](./topics/agent_harnesses_scaffolding.md) | Measuring, attributing, and optimizing the control structures surrounding a model. |
| [Evaluation-Driven Data Curation](./topics/evaluation_driven_data_curation.md) | Revising selection, generation, filtering, or mixture policies from downstream evaluation feedback. |
| [Evaluation-Driven Post-Training](./topics/evaluation_driven_post_training.md) | Using evaluation as an objective, feedback signal, or experimental environment for model and agent improvement. |
| [Survey](./topics/survey.md) | Surveys and position papers on agent evaluation — an index of references rather than a task suite. |

---

## Browse by Domain

Domain pages answer a narrower question: where does the evaluated work happen? A physics benchmark and a biology benchmark may use the same evaluation method but face different tools, artifacts, costs, and correctness standards. The counts below show current coverage; the maintained index and per-domain tables live in [`domains/`](./domains/README.md).

**Sciences**

| Domain | Works |
|---|--:|
| [Physics](./domains/physics.md) | 47 |
| [Chemistry](./domains/chemistry.md) | 38 |
| [Biology](./domains/biology.md) | 38 |
| [Materials Science](./domains/materials_science.md) | 28 |
| [AI & Machine Learning Research](./domains/ai_ml_research.md) | 27 |
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

Activity pages follow the work itself. Does the agent search literature, run a simulation, design an experiment, reproduce a result, or carry a project end to end? The same activity can appear in several domains and use several evaluation methods. Work that evaluates no scientific or research task, such as a survey or pure evaluation methodology, carries an explicit `N/A`. See [`activities/`](./activities/README.md) for the full index.

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
| [End-to-End Research](./activities/end_to_end_research.md) | Multi-stage research lifecycle across several major phases | 9 |
| [Laboratory & Instrument Control](./activities/laboratory_instrument_control.md) | Instrument, microscope, and beamline control; lab automation; behaviour-defined control code | 3 |

---

## Scope

Work is in scope when evaluation changes what we know or what the development loop does next. That includes benchmarks, diagnostic methods, evaluator validation, benchmark-validity research, scientific workflows, and systems that use evaluation to revise skills, harnesses, data, or post-training.

A paper is not in scope merely because it reports benchmark scores. Pure training, optimization, data, memory, or multi-agent work stays out when evaluation appears only in the final results table. The test is operational: does evaluation define the objective, supply feedback, select an intervention, diagnose a failure, or serve as the experiment environment?

"Works" is broader than "benchmarks": the collection holds cards for benchmarks, evaluation methodologies, evaluation frameworks, evaluation-focused RL contributions, surveys, and position papers. Each card notes its type explicitly. The collection currently holds **381 work cards**, **15 topic pages**, **19 domain pages**, and **11 activity pages**, each mirrored in Chinese under [`zh/`](./zh/README.md).

---

## Repository Structure

The knowledge base has **four layers**: the works layer, plus three co-equal aggregation axes over it.

| Directory | Role |
|---|---|
| [`works/`](./works/README.md) | One factual reference card per work. Flat, kebab-case, one Markdown file each. |
| [`topics/`](./topics/README.md) | Literature-review pages — the evaluation-research axis spanning measurement, diagnosis, and improvement. Each topic owns its own comparison table. |
| [`domains/`](./domains/README.md) | Field-axis reference pages, one per canonical science or engineering domain, with a fixed-column comparison table. |
| [`activities/`](./activities/README.md) | Task-axis reference pages, one per canonical research activity, with Definition, Scope, task patterns, and a comparison table. |
| [`zh/`](./zh/README.md) | Chinese mirror of every page, synced after each English batch. |

Two navigational conventions keep the axes in sync: each card's `Topics` block links up to its topics, and each topic page's `Related Works` links back down to its cards. The domain mapping is maintained one-way on the domain pages. Root-level [`AGENT.md`](./AGENT.md) is the repository constitution and [`CLAUDE.md`](./CLAUDE.md) is its quick reference; each directory's own `README.md` documents its page template and rules.

---

## Contributing

Contributions are welcome. Automated updates complement, rather than replace, community contributions; missing or newly relevant work can still be proposed manually. All contributor and maintainer rules — reference validation, page templates, the canonical taxonomies, and the bilingual sync cadence — live in [`AGENT.md`](./AGENT.md) (the constitution) and [`CLAUDE.md`](./CLAUDE.md) (its quick reference), with layer-specific rules in each directory's README. Every page is available in English and Chinese; use the language switcher at the top of any page.
