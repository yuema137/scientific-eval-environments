# Research Activities

> **English** | [简体中文](../zh/activities/README.md)

Reference pages for the **research-activity axis** of the repository — grouping works by *what the evaluated agent or system actually does*. Activities are a third co-equal navigation layer alongside the methodology axis in [`../topics/`](../topics/README.md) and the field axis in [`../domains/`](../domains/README.md):

```
Topic     →  Representative works  →  Original papers   (why / how we evaluate)
Domain    →  Works in that field   →  Original papers   (where the task lives)
Activity  →  Works doing that task →  Original papers   (what the agent does)
```

- **Topic** — the evaluation or research *theme* a work relates to.
- **Domain** — the scientific or engineering *field* the work is grounded in.
- **Activity** — the substantive scientific or research *task* the evaluated agent performs.

A reader who arrives asking "which benchmarks make an agent *design experiments*?" or "*reproduce* a paper?" or "*solve* a physics problem?" starts here and follows the links into [`../works/`](../works/README.md), then to the original papers.

## Canonical taxonomy

The set of activities is fixed. Adding, renaming, or removing one requires updating [`../AGENT.md`](../AGENT.md). Counts are the number of work cards currently mapped to each activity (a work may appear under several).

| Activity | What it covers | Works |
|---|---|--:|
| [Literature Search & Evidence Synthesis](./literature_evidence_synthesis.md) | Literature retrieval, study selection, systematic review, evidence synthesis, literature-grounded extraction | 23 |
| [Scientific Problem Solving & Reasoning](./scientific_problem_solving_reasoning.md) | Scientific QA, derivations, proofs, quantitative and multimodal problem solving, diagnostic reasoning | 94 |
| [Data Analysis & Statistical Inference](./data_analysis_statistical_inference.md) | Preprocessing, statistical analysis and inference, bioinformatics/omics analysis, data interpretation | 44 |
| [Modeling & Prediction](./modeling_prediction.md) | Predictive and surrogate modelling, property prediction, forecasting, model-fitting as a central artifact | 22 |
| [Simulation & Scientific Computing](./simulation_scientific_computing.md) | Numerical simulation, PDE/FEM, MD/DFT, running and building scientific simulators | 35 |
| [Experiment Design & Scientific Discovery](./experiment_design_discovery.md) | Experiment and observation planning, active measurement, hypothesis generation, law discovery | 23 |
| [Laboratory & Instrument Control](./laboratory_instrument_control.md) | Instrument, microscope, and beamline control; lab automation; behaviour-defined control code | 3 |
| [Optimization & Engineering Design](./optimization_engineering_design.md) | Parameter and controller tuning, engineering/inverse design, materials and molecular design | 26 |
| [Scientific Software & Workflow Engineering](./scientific_software_workflow_engineering.md) | Scientific/engineering code generation, repository and pipeline engineering, HDL and formal-spec code | 71 |
| [Research Reproduction & Replication](./research_reproduction_replication.md) | Reproducing published analyses, results, and methods; matching reported findings | 11 |
| [End-to-End Research](./end_to_end_research.md) | Multi-stage research lifecycle across several major phases, from formulation to reporting | 9 |

Across the corpus, 361 activity memberships are assigned over the applicable work cards.

## Activities are multi-label

Activities are **not** mutually exclusive. A work may appear on several activity pages when the benchmark genuinely evaluates several substantive activities (for example, a paper-reproduction task that also requires simulation and scientific software). Labels are assigned conservatively: an activity is listed only when it is a **meaningful evaluated component** — if removing it would materially change what capability the benchmark measures. Incidental tool use is not enough, and typical cards carry one to three activities.

## Not every work has an activity

Some works do not evaluate a scientific or research activity and therefore appear on no activity page: surveys and position papers, pure evaluation methodologies and diagnostic or reward/credit-assignment frameworks that operate on arbitrary trajectories, general-purpose web/UI/computer-use and coding-assistant benchmarks, and safety/robustness/resource-awareness probes. These cards carry an explicit `## Activities` block reading `N/A — <reason>` and are never force-assigned to an activity.

## Activity page template

Each activity page follows one structure:

```markdown
# <Activity Name>

> **English** | [简体中文](../zh/activities/<file>.md) · [← All activities](./README.md)

## Definition      — one concise paragraph defining the activity
## Scope           — what belongs here and the key boundary cases
## Task Patterns   — synthesis of how the activity appears across the corpus, linking work cards
## Comparison      — table: Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card
## Related Works   — the reverse index: bare links to every member work card
```

## Maintenance rules

- **Reverse index is two-way.** Every activity on a card's `## Activities` block must appear in that activity page's `Related Works`, and every work in a page's `Related Works` (and Comparison table) must list that activity on its card. The two sides must agree exactly — no table-only entries, no duplicates, no broken links.
- **Counts are auto-derived.** The work counts in the table above (and everywhere else in the repository) are generated from the reverse indexes by [`../scripts/update_counts.py`](../scripts/update_counts.py) — run it after any card change, and never hand-edit a count.
- **Canonical labels only.** Cards draw solely from the taxonomy above; no free-form activity tags.
- **Evidence standard.** Classification is based on the actual task the card describes (its `Overview`, `Tasks`, `Summary`, `Main Contribution`, `Domains`, `Key Design Ideas`), falling back to the verified primary source — never on title keywords.
- **No force-assignment and no `Other`.** Genuinely non-applicable works get an explicit `N/A` reason; there is no catch-all activity.
- **Division of responsibility.** Topics own evaluation-methodology synthesis and open questions; domains describe field-specific instantiation and scientific verification; activities describe task and workflow patterns; cards remain factual references. Detailed scoring methodology stays in cards, topics, and domains.
- **Bilingual mirror.** Every activity page and every card's `## Activities` block is mirrored under [`../zh/activities/`](../zh/activities/README.md) and `../zh/works/`, synced after each English change.
- **Taxonomy changes** require updating [`../AGENT.md`](../AGENT.md) and [`../CLAUDE.md`](../CLAUDE.md).
