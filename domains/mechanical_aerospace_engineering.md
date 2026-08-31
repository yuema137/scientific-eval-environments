# Mechanical & Aerospace Engineering

> **English** | [简体中文](../zh/domains/mechanical_aerospace_engineering.md) · [← All domains](./README.md)

## Scope

Mechanical and aerospace engineering. Computational fluid dynamics and thermal transport fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| CFDLLMBench | 2025 | Computational fluid dynamics at three depths: graduate-level knowledge (CFDQuery), numerical solution of stated PDEs in Python (CFDCodeBench), and end-to-end OpenFOAM case configuration and execution (FoamBench). | 240 tasks: 90 expert-curated multiple-choice questions, 24 PDE-solver coding problems, and 126 OpenFOAM cases (110 tutorial-derived + 16 expert-crafted to be unlike any tutorial). | Execution plus banded normalized error (NMSE) against reference solutions and an explicit convergence check under mesh and time-step refinement; any valid numerical method is accepted. | [→](../works/cfdllmbench.md) |
| Terminal-Bench Science | 2026 | Mechanical Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| SimBench | 2024 | Generate digital twins for multibody dynamics, FEA, vehicle dynamics, robotic dynamics, and sensor simulation in the Chrono simulator. | 102 demonstration tasks over 34 physical systems (official repository), built through multi-turn dialogue; 33+ LLMs compared. | LLM-judge scoring with predefined rules and human-in-the-loop guidance. | [→](../works/simbench.md) |
| FEM-Bench | 2025 | Write finite-element functions and unit tests for computational-mechanics problems — forces, deformation, constraints. | 33 graduate-course-aligned tasks over two tracks, five attempts per model-task pair. | Objective verification; Average Joint Success Rate for test writing. | [→](../works/fem-bench.md) |
| RealPDEBench | 2026 | Predict fluid and thermal engineering systems — fluid–structure interaction, cylinder and foil flows, and combustion — from real-world measurements paired with numerical simulations. | Five real-world measured datasets with paired simulations and three sim-vs-real tasks; evaluates scientific ML surrogate models rather than LLM agents. | Eight data-oriented and physics-oriented metrics over ten baselines. | [→](../works/realpdebench.md) |
| FEABench | 2025 | Solve multiphysics engineering problems end to end with finite element analysis by operating COMSOL Multiphysics through its API. | Natural-language problem descriptions; the agentic setting iterates API calls against software feedback. | Evaluation over generated API calls and computed answers; executability of API calls as a headline metric. | [→](../works/feabench.md) |
| MooseBench | 2026 | Generate multiphysics finite-element simulation code (MOOSE) that solves the intended physics, not merely code that runs. | 220 cases with PDE-level mathematical ground truth. | Intent Fidelity Score via deterministic PDE reconstruction; 39–40% of cases stay runnable-but-wrong under execution-only repair. | [→](../works/moosebench.md) |
| SciConvBench | 2026 | Clarify ill-posed simulation requests; fluid mechanics and solid mechanics are two of its four computational-science domains. | Multi-turn disambiguation and inconsistency-resolution dialogues over a structured task ontology. | Rubric scoring of clarification behavior, conversational grounding, and final-specification fidelity. | [→](../works/sciconvbench.md) |
| AInsteinBench | 2025 | Resolve maintainer-PR tasks in production scientific repositories; fluid dynamics is among its six codebases. | Repository-level coding-agent tasks in executable environments. | Test-driven verification with expert-reviewed curation. | [→](../works/ainsteinbench.md) |
| ERI Benchmark | 2026 | Mechanical and aerospace engineering, two of the benchmark's nine covered fields, spanning thermodynamics, fluid mechanics, heat transfer, machine design, dynamics and vibrations, manufacturing and HVAC, plus aerodynamics, flight mechanics, propulsion, aerospace structures, and orbital mechanics. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item; aerospace engineering is among the hardest fields for every model scored. | [→](../works/eri-benchmark.md) |
| SoM-1K | 2025 | Strength of materials as the solid-mechanics foundation the paper states is shared across civil, mechanical, aerospace and materials engineering — axial loading of bars, torsion of shafts, bending, and integrated problems combining static analysis with vibration, impact and rigid-body motion. | 1,065 annotated problems (bending 630, axial 201, torsion of shafts 137, frames 54, integrated 43; 148 statically indeterminate) drawn from university textbooks and mechanics competitions, each pairing a statement, a schematic, an expert-verified Description of the Image and a worked solution; 8 models over 3 prompting strategies. | Manual grading of every response by mechanics educators, awarding a point only when the reasoning sequence is valid and the final answer correct, over a majority vote of five samples; best result 56.6%. | [→](../works/som-1k.md) |
| EngDesign | 2025 | Mechanical systems design, together with the solid-mechanics content shared with the benchmark's Structure Design area, posed as design specifications with goals, constraints and performance requirements rather than questions with reference answers. | Mechanical Systems (7 tasks) and Structure Design (13) within 101 design tasks carrying 473 gradable items across nine engineering areas; 12 chat and reasoning models, with an iterative protocol allowing up to 10 simulator-feedback rounds. | Structured model output executed by a per-task evaluation script driving the domain's own tools — MATLAB, finite element analysis, topology-optimisation solvers — returning a binary pass/fail, a 0–100 partial-credit score and an evaluation log. | [→](../works/engdesign.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the mechanical and aerospace engineering subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`FLU` fluid mechanics & aerodynamics · `CFD` computational fluid dynamics & flow solvers · `THERM` thermodynamics, heat transfer & combustion · `SOL` solid mechanics & strength of materials · `FEA` finite element analysis & computational structural mechanics · `MULTI` multiphysics simulation & coupled-field analysis · `DYN` dynamics, vibrations & multibody systems, including vehicle dynamics · `MECH` machine design & mechanical systems · `AERO` aerospace: aerodynamics, flight mechanics, propulsion & orbital mechanics · `GEN` curriculum-wide or unspecified, no single subfield

**Two scores, not one.** The columns split into **coverage** — what the evaluation setup puts under test — and **rigor** — how far you can trust what it reports. They are summed separately because they pull against each other: a benchmark can put everything under test and verify none of it carefully, and a deliberately narrow one can be the most trustworthy thing on the page. Rows are ordered by `Cov`, highest first, and by `Rig` within equal coverage; remaining ties keep Comparison-table order. Coverage leads because it is the axis a reader scans for — *does this benchmark even put my problem under test* — and `Rig` then says how far to trust what it reports.

### Coverage (`Cov`, max 7)

Yes/no, ordered by rarity — the properties fewest works have come first, so the left of the group is where the field is thin. A property nearly every work satisfies does not earn a column: *writing and running code* was dropped on that ground.

- **Net** — network or live external retrieval permitted; a supplied fixed corpus does not count.
- **E2E** — end-to-end research: a question or goal only, with no source paper, reference implementation, or step-by-step specification supplied, and the agent drives the whole investigation.
- **Cost** — budget or resource cost is a scored or priced dimension, not merely a step cap.
- **MM** — multimodal content is load-bearing, either required as input or scored as an output artifact.
- **Repro** — grounded in a specific published result the agent must match or recover.
- **Real** — real experimental or observational data, as opposed to synthetic or simulated (a digital twin is simulated).
- **Inter** — interactive: the agent takes multiple actions against an environment, tool, or simulator and gets feedback that shapes the next one.

### Rigor (`Rig`, max 13)

- **Human** — a measured human-expert baseline or human reference performance anchors the scale. `◐` where the anchor is a published result or expert reference implementation rather than a measured human run.
- **Rubric** — an expert-authored rubric or official marking scheme with named criteria or weights; a continuous automatic metric is not a rubric.
- **Contam** — a deliberate mechanism makes the answer unmemorizable: post-cutoff sourcing, unpublished or newly authored problems, counterfactual alteration, on-demand generation, or screened leakage. Withholding a published paper at evaluation time is `◐` — it does not remove that paper from a pretraining corpus.
- **Verif** `0`–`3` — how far the score can be trusted without trusting a model. `0` scored only by an LLM judge or rubric, with no validation of that scorer · `1` judge or rubric scoring whose agreement with human experts is measured and reported · `2` deterministic checks alongside judge or rubric scoring · `3` fully deterministic — execution, tests, numerical comparison to a reference, symbolic checking, or a proof kernel, with no judge in the loop. This replaces a plain yes/no *deterministic verification* column, which 85% of works satisfied and which therefore separated nothing; as a ladder it separates a great deal. A separate `Judge` column was dropped as near-redundant with `Verif` < 2.
- **Scale** `0`–`3` — items evaluated **in this domain**: `0` fewer than 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 or more · `?` the source does not give a per-domain count. This counts items, not effort: 30 paper-reproduction tasks are far more work than 3,000 exam questions, and the column cannot see that.
- **Fail** `0`–`4` — how deep the failure analysis goes, because "reports a failure analysis" spans everything from a single remark to a controlled experiment. `0` nothing beyond headline scores · `1` narrative remarks on where models fall short, no classes named · `2` named error classes or illustrative case studies, but no counts or shares · `3` a quantified failure account: a taxonomy with per-class counts or shares, or measured breakdowns isolating specific failure conditions · `4` level 3 plus a controlled experiment or ablation built to test *why* the failures occur.

### Reading the two scores

Yes/no columns score `✔` 1, `◐` 0.5, `✘` 0, `?` 0; graded columns contribute their number, with `?` scoring 0. `Domain` does not score.

Three cautions. A `?` costs exactly what a `✘` costs, so both scores are floors on what a work *demonstrably* does, not verdicts on it. Neither score is a quality ranking: high `Cov` with low `Rig` describes a benchmark that reaches for everything and pins down little, while low `Cov` with high `Rig` describes one that measures a narrow thing carefully — and which of those is the right design depends entirely on the question being asked. And `Cov` is a property of the *evaluation setup*, not of the science: a work can sit at the bottom of this table and still be the most important paper in its subfield.

For multi-domain suites the row describes this domain's slice, as in the Comparison table.
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CFDLLMBench | CFD, THERM | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ◐ | 3 | 2 | 3 | **9** |
| EngDesign | MECH, SOL | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✔ | ✘ | 3 | 1 | 3 | **8** |
| SoM-1K | SOL | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ◐ | ✘ | 3 | 3 | 4 | **10.5** |
| MooseBench | MULTI, FEA | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| SimBench | DYN, FEA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✔ | ✘ | 2 | 2 | 1 | **6.5** |
| SciConvBench | FLU, SOL | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✔ | ◐ | 1 | ? | 3 | **5.5** |
| AInsteinBench | CFD | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| FEABench | MULTI, FEA | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 2 | ? | 3 | **5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| RealPDEBench | FLU, THERM | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| ERI Benchmark | GEN, AERO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✔ | 2 | 3 | 3 | **10** |
| FEM-Bench | FEA, SOL | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ◐ | ✘ | ◐ | 3 | 1 | 2 | **7** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [SciConvBench](../works/sciconvbench.md)
- [MooseBench](../works/moosebench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [RealPDEBench](../works/realpdebench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [FEM-Bench](../works/fem-bench.md)
- [SoM-1K](../works/som-1k.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [EngDesign](../works/engdesign.md)
- [FEABench](../works/feabench.md)
- [SimBench](../works/simbench.md)
