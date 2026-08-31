# Chemical Engineering

> **English** | [简体中文](../zh/domains/chemical_engineering.md) · [← All domains](./README.md)

## Scope

Chemical process engineering — the design, simulation, optimization, operation, and safety of chemical processes and plants — as distinct from Chemistry the science. Works on this page evaluate process flowsheeting and simulator-grounded design (Aspen Plus, IDAES/Pyomo), operating-parameter optimization, process control and supervisory fault recovery, process-safety analysis such as HAZOP and P&ID validation, and chemical-engineering knowledge and calculation across mass and energy balances, thermodynamics, transport phenomena, reaction kinetics, and separation processes. Molecular, reaction, and materials-level questions belong to Chemistry; a work belongs here when its evaluated objective is a process or plant decision, and a work whose evaluation genuinely spans both is listed on both pages.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | Chemical Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| CeProBench | 2026 | Chemical process development across three declared pillars — knowledge (process routes, catalysts, separation techniques), concept (process flow diagram parsing, completion, and design), and parameter (operating-parameter optimization). | Six task classes spanning 243 questions and 235 specific tasks, built from 70 technical documents (4,406 entities / 4,967 relations), 113 competition-derived PFDs (986 equipment units, 1,172 connections), and 20 Aspen Plus parameter files (91 adjustable parameters, 65 objectives). | Parameter tasks scored by executing candidate settings in Aspen Plus, which validates chemical and thermodynamic feasibility; knowledge and concept tasks scored against expert graph annotations via entity F1, MEC/MED, and equipment and connection accuracy. | [→](../works/ceprobench.md) |
| Simona | 2026 | Convert a written chemical process description into a simulation flowsheet — unit-operation topology plus operating configuration — that runs to convergence. | 1,000 process descriptions authored by chemical engineering experts, varied along unit-operation difficulty and description detail. | Simulation Convergence Rate (converged designs over total requirements) established by execution in the authors' process simulator over HTTP APIs, reported with design time against LLM, multi-agent, and human-expert baselines. | [→](../works/simona.md) |
| CRAFTS | 2026 | Automated construction of executable IDAES/Pyomo process-simulation models: unit-operation selection, topology construction, property-package assignment, specification closure, initialization, recycle handling, and solver diagnosis. | OpenIDAES-450 — 450 user-facing requests paired with executable IDAES models and execution records, of which 82 are frozen as the held-out test split. | Staged Workflow Success contract enforced by deterministic IDAES/Pyomo promotion gates (port compatibility, degrees-of-freedom closure, initialization, accepted solver termination), plus macro-F1 on unit records, stream records, and directed connections. | [→](../works/crafts.md) |
| A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents | 2026 | Supervisory fault recovery in process plants: returning a modular batch mixing unit and a continuous stirred-tank reactor to safe operation after pump failure and degradation, main-line clogging, leakage, heat-exchanger fouling, and cooling-valve saturation. | Two openly released executable Python environments with typed configurable fault injection and pluggable recovery/validation interfaces; parameterised scenario generators rather than a fixed task list or split. | Per-action validation rather than a task score: a symbolic validator checks state reachability and actuator existence against plant structure, and a simulation-based validator rolls the action forward in a digital twin and accepts only bounded unsafe exposure. | [→](../works/ctrl-alt-recover.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | Safe admission of LLM reasoning into industrial process control, evaluated on chemical plant scenarios — three derived from the Tennessee Eastman Process plus a polymerization reactor and a dryer. | Five process-plant scenarios spanning continuous and batch operation, an error-injection set of 43 crafted proposals, an N = 50 repeated-run robustness study, and a B0–B3 context ablation ladder. | Deterministic graph traversal over the plant P&ID checks each proposed control action for tag existence, actuatability, fail-state consistency, and downstream impact; validator recall measured against the injected error set. | [→](../works/aae-framework.md) |
| Can Large Language Models Automate the HAZOP Process Without Human Intervention? | 2026 | Hazard and Operability analysis in the process industries: producing a complete HAZOP worksheet — deviations, causes, consequences, safeguards — from a piping and instrumentation diagram. | One identical P&ID and one standardized prompt per model, with four multimodal LLMs each generating a full worksheet without human intervention. | Comparison against an expert-prepared reference worksheet along two separated axes: similarity (F1, all four models above 86%) and cost per worksheet, versus semantic scenario validity (0.19–0.37) and safeguard diversity. | [→](../works/can-large-language-models-automate-the-hazop-proce.md) |
| PSE-Bench | 2026 | Process systems engineering consultation across four domains: process modeling and simulation, process optimization, machine learning for chemical processes, and process design and systems engineering (HAZOP, LOPA, plantwide control, FEED). | 200 open-ended questions, 50 per domain, answered single-turn and zero-shot, released with ground truths and per-question rubrics. | Five independent LLM judges score each response against a seven-element rubric, combined into a composite of ROUGE-1, ROUGE-L, cosine similarity, and rubric element coverage, and checked against three domain experts (rs = 0.416, ICC = 0.793, +0.85 leniency offset). | [→](../works/pse-bench.md) |
| ChemEBench | 2025 | Chemical-engineering capability from foundational knowledge through applied professional skill — reactor and separation equipment, distillation and extraction, heat exchangers, process and plant safety, process economics, and plant engineering construction. | Three progressive levels covering 15 dimensions and 101 distinct tasks, in objective (multiple choice, fill-in-the-blank, true/false) and subjective (short answer, calculation) formats; 14 models compared. | Accuracy on objective items; subjective items graded 0–5 for completeness and clarity, with the reasoning chain checked step by step for factual, logical, computational, and knowledge errors. | [→](../works/chemebench.md) |
| PEOA | 2024 | Chemical and process engineering problem-solving: mass and energy balances, thermodynamics, heat transfer, reaction kinetics, fluid mechanics, separation processes, and process control. | Two datasets compiled from scholarly sources under a 70/15/15 split — ChemProc (7,000+ chemical-engineering QA pairs) and the supporting MathComp (8,500+ modeling and numerical-methods pairs) — each item solved as a multi-step tool-integrated trajectory. | Stage-decomposed tool-learning scoring: task planning against gold-standard plans, tool selection by Recall@K / NDCG@K / COMP@K against a ground-truth tool set, tool calling by parameter-extraction correctness and error handling, and response generation by BLEU, ROUGE-L, and exact match. | [→](../works/peoa.md) |
| Using Large Language Models for Solving Thermodynamic Problems | 2025 | Chemical-engineering thermodynamics: closed and open systems, single and multi-step changes of state, cyclic processes, and processes involving liquids as well as gases. | 22 purpose-written problems (13 simple, 9 advanced), each fully specified in text with a unique numerical solution and presented three times to each of five models. | Trained human experts grade in the manner of academic exam marking, awarding 0.5 points per correctly executed solution step (stated uncertainty typically ±0.5), with means reported separately for the simple and advanced subsets and consistency measured across repetitions. | [→](../works/llm-thermodynamics.md) |
| ERI Benchmark | 2026 | Chemical engineering as one of nine covered fields, with six subdomains: mass and energy balances, chemical thermodynamics, reaction engineering, separation processes, process control, and transport phenomena. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell); the chemical-engineering slice covers 126 cells, roughly 6,300 records, and is scored separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item, with means reported per field. | [→](../works/eri-benchmark.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the chemical engineering subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`BAL` mass & energy balances · `THERMO` thermodynamics & phase equilibria · `TRANS` transport phenomena & fluid mechanics · `HEAT` heat transfer & exchanger design · `SEP` separation processes · `RXN` reaction engineering & catalysis · `FLOW` process flowsheeting & simulation · `OPT` process optimization · `CTRL` process control & plant operations · `SAFE` process safety & hazard analysis · `DES` process & plant design · `ECON` process economics · `GEN` curriculum-wide or unspecified, no single subfield

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
| CeProBench | FLOW, OPT, DES | ✔ | ✘ | ◐ | ✔ | ✘ | ◐ | ◐ | **3.5** | ✘ | ✔ | ✘ | 2 | 2 | 2 | **7** |
| Can Large Language Models Automate the HAZOP Process Without Human Intervention? | SAFE | ✘ | ✘ | ✔ | ✔ | ✘ | ◐ | ✘ | **2.5** | ◐ | ✘ | ✘ | 2 | 0 | 3 | **5.5** |
| CRAFTS | FLOW | ? | ✘ | ✘ | ✔ | ✘ | ✘ | ✔ | **2** | ◐ | ✘ | ◐ | 3 | 1 | 3 | **8** |
| Terminal-Bench Science | GEN | ? | ✘ | ? | ? | ◐ | ◐ | ✔ | **2** | ✘ | ✘ | ✔ | 3 | 0 | 0 | **4** |
| Simona | FLOW, DES | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✔ | ✔ | ✔ | 2 | 3 | 2 | **10** |
| PEOA | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ◐ | ✘ | 2 | 3 | 3 | **9** |
| A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents | CTRL, SAFE | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ◐ | 3 | ? | 0 | **3.5** |
| Autonomous Action Execution (AAE) Framework | CTRL, SAFE | ? | ✘ | ? | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ◐ | ✘ | 3 | 1 | 4 | **8.5** |
| ERI Benchmark | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| PSE-Bench | FLOW, OPT, DES | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✘ | 1 | 2 | 3 | **7** |
| Using Large Language Models for Solving Thermodynamic Problems | THERMO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 1 | 1 | 3 | **6.5** |
| ChemEBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✘ | 2 | ? | 1 | **4** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [CRAFTS](../works/crafts.md)
- [A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents](../works/ctrl-alt-recover.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [PSE-Bench](../works/pse-bench.md)
- [CeProBench](../works/ceprobench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [Simona](../works/simona.md)
- [Can Large Language Models Automate the HAZOP Process Without Human Intervention?](../works/can-large-language-models-automate-the-hazop-proce.md)
- [ChemEBench](../works/chemebench.md)
- [Using Large Language Models for Solving Thermodynamic Problems](../works/llm-thermodynamics.md)
- [PEOA](../works/peoa.md)
