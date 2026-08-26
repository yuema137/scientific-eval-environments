# Materials Science

> **English** | [简体中文](../zh/domains/materials_science.md) · [← All domains](./README.md)

## Scope

Materials characterization and computational materials science, spanning physical instruments and simulation.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| AFMBench | 2025 | Operate a real atomic force microscope — calibration, feature detection, mechanical-property measurement, graphene layer counting, indenter detection — from experimental design through results analysis. | 100 expert-curated tasks on a Nanosurf DriveAFM via a Python API; 69% multi-tool, stratified by complexity and functional domain, three trials per model–task pair. | Physical execution on real hardware; per-domain task completion rate plus a named failure taxonomy (e.g., 'sleepwalking' — unauthorized actions beyond instructions). | [→](../works/afmbench.md) |
| AutoMat | 2026 | Reproduce claims from computational materials science papers end to end, across Stat/ML methods, Density Functional Theory, Molecular Dynamics, and Discrete Dislocation Dynamics. | 85 SME-curated claim-reproduction tasks in three types (from-paper, from-artifact reproduction, from-artifact interpretation), run in a resource-controlled HPC-style environment. | An artifact-navigating LLM evaluator agent scores 1–5 against hidden SME reproduction procedures (success = ≥4), calibrated at quadratic-weighted kappa 0.69 against blind SME scoring. | [→](../works/automat.md) |
| Terminal-Bench Science | 2026 | Materials Science tasks within the Physical Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Material is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | Control microscopes and materials-characterization instruments through agentic workflows, testing whether benchmark scores generalize to unseen tasks. | 53 benchmark tests across 105 agent configurations (graph topology × five LLMs × RAG/context parameters); 1,949 runs with full trace logging. | Trace-logged benchmark tests with latency, token, cost, and failure-mode comparison; generalization probed via surrogate prediction on unseen tasks. | [→](../works/agentic-microscopy-benchmarks.md) |
| SciCode | 2024 | Write research code for scientist-curated problems; materials science is among the five main domains its 16 natural-science subfields span. | 80 main problems decomposed into 338 subproblems mixing knowledge recall, reasoning, and code synthesis. | Execution against scientist-annotated gold-standard solutions and test cases. | [→](../works/scicode.md) |
| SciConvBench | 2026 | Clarify ill-posed simulation requests; materials science is one of its four computational-science domains. | Multi-turn disambiguation and inconsistency-resolution dialogues over a structured task ontology. | Rubric scoring of clarification behavior, conversational grounding, and final-specification fidelity. | [→](../works/sciconvbench.md) |
| ChemX | 2025 | Extract structured data from nanomaterials literature — nanozymes, nanomagnetic materials — alongside small-molecule datasets. | 10 manually curated, expert-validated extraction datasets; agentic document processing. | Extraction quality against domain-expert-validated records. | [→](../works/chemx.md) |
| MaCBench | 2024 | Do the visual work of materials research: read instruments and lab scenes, extract data, interpret experimental results. | Multimodal (image + text) tasks in three aspects — data extraction, experimental understanding, results interpretation. | Accuracy via the ChemBench pipeline; near-perfect extraction but limited spatial and cross-modal reasoning. | [→](../works/macbench.md) |
| MaScQA | 2023 | Answer materials-science and metallurgy exam questions across 14 topics. | 650 GATE-derived questions in four types; static QA under zero-shot and chain-of-thought prompting. | Accuracy with a conceptual-vs-computational error taxonomy; GPT-4 ~62%. | [→](../works/mascqa.md) |
| MatSciBench | 2025 | Reason through college-level problems spanning the essential materials subdisciplines. | 1,340 problems (946 with reference solutions, 315 with images); static text and multimodal QA. | Accuracy on text and image questions; DeepSeek-R1 75.22% / GPT-5 53.02%. | [→](../works/matscibench.md) |
| LLM4Mat-Bench | 2024 | Predict materials properties from text encodings of crystals. | ~1.9M structures, 45 properties, 3 modalities (composition/CIF/text); static prediction. | MAD:MAE for regression, AUC for classification; generative LLMs near-random. | [→](../works/llm4mat-bench.md) |
| MatText | 2024 | Predict crystal properties from text representations, versus geometry-aware models. | 9 text representations, model scales up to 70B, datasets up to 2M structures; static prediction. | Regression error vs. GNN baselines; documents the "GNN-LM wall." | [→](../works/mattext.md) |
| AtomWorld | 2025 | Construct and modify crystalline atomic structures under standard modelling operations. | 10 fundamental actions across 4 modelling categories; statically verifiable. | Verifiable structure checks; rotation success below 12%. | [→](../works/atomworld.md) |
| OpenXRD | 2025 | Answer X-ray diffraction and crystallography questions. | 217 expert-curated questions, closed- and open-book; 74 LLMs/MLLMs. | Accuracy comparing expert-curated vs. AI-generated context at matched tokens. | [→](../works/openxrd.md) |
| MatVQA | 2025 | Reason visually over materials microscopy and diffraction imagery. | 1,325 questions across 4 structure-property-performance tasks; 17 MLLMs; shortcuts removed. | Accuracy on real materials imagery with textual-shortcut removal. | [→](../works/matvqa.md) |
| MatCha | 2025 | Understand materials characterization across the research workflow. | 1,500 questions across 4 stages and 21 tasks over real characterization imagery. | Accuracy with a human-expert baseline; few-shot and CoT do not close the gap. | [→](../works/matcha.md) |
| MatQnA | 2025 | Interpret data from ten mainstream characterization methods (XPS, XRD, SEM, TEM…). | Multiple-choice and subjective QA over real characterization data; multimodal. | Objective accuracy (~90% for frontier MLLMs) plus subjective evaluation. | [→](../works/matqna.md) |
| MatViX | 2024 | Extract structured data — compositions and property curves — from visually rich articles. | 324 full-length articles → 1,688 expert-curated JSON; zero-shot VLM extraction. | F1 for compositions; Curve Similarity and Curve Alignment scores for curves. | [→](../works/matvix.md) |
| MatTools | 2025 | Understand and program materials-science tools (pymatgen) to compute properties. | 69,225 comprehension QA + 49 real tasks (138 subtasks) requiring Python code. | Comprehension accuracy plus execution-verified code generation. | [→](../works/mattools.md) |
| AutoDFT / VASPBench | 2026 | Autonomously plan, run, and repair density-functional-theory (VASP) calculations. | 34 tasks across 9 DFT calculation types; closed-loop multi-agent execution. | Task-level success (94.1% with GPT-5.2) plus property accuracy vs. databases. | [→](../works/vaspbench.md) |
| AlchemyBench | 2025 | Plan inorganic materials synthesis: precursors, equipment, procedure, characterization. | End-to-end prediction over 17,000 expert-verified synthesis recipes; static. | Expert-agreement-validated LLM-as-a-Judge over free-form predictions. | [→](../works/alchemybench.md) |
| Materials Hypothesis Generation | 2025 | Generate materials-discovery hypotheses under explicit goals and constraints. | Hypothesis generation over a dataset curated from recent publications. | A scalable metric emulating a materials scientist's critical assessment. | [→](../works/materials-hypothesis.md) |
| Science Edge Evaluation (SEE) | 2026 | Evidence-bounded reasoning over real materials-characterization data — SEM/TEM/AFM microscopy, X-ray diffraction patterns, and thermal-analysis curves — rather than concept recall; materials science is one of its three disciplines. | 1,116 expert-curated multimodal questions (1,049 public) across three experimental disciplines (chemistry, biology, materials science) and 17 sub-fields, in multiple-choice and numerical fill-in-the-blank formats; a visual-agent setting adds web search and a code interpreter. | Answers scored against expert ground truth — exact match for multiple choice, expert tolerance for numerical answers — under a strict binary LLM-as-judge protocol (Gemini 3.1 Pro); image-ablation checking confirms each question needs its visual input. | [→](../works/science-edge-evaluation.md) |
| ERI Benchmark | 2026 | Materials engineering as one of nine covered fields, with six subdomains: structure of materials, mechanical properties, phase diagrams, failure analysis, polymers and composites, and corrosion. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item. | [→](../works/eri-benchmark.md) |
| Imaging-101 | 2026 | Materials computational imaging — grouped with chemistry as one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| CASCADE | 2025 | Materials-science research tasks in SciSkillBench: retrieving and processing materials data and running simulations through specialized materials toolkits, with the paper filed under cond-mat.mtrl-sci. | 116 materials-science and chemistry tasks — 76 data-oriented and 40 computation-oriented, split again into 58 Level 0 tasks naming the key functions and 58 Level 1 tasks giving only a high-level objective; three repetitions per configuration over 16,008 experiment runs. | Outcome-based automated scoring: the agent's processed output is compared against the ground-truth answer within a predefined tolerance threshold, reported as success rate (GPT-5 DeepSolver 93.26% against 35.36% for the Native configuration). | [→](../works/cascade.md) |
| OntoLearner | 2026 | Construct ontology structure for materials science and engineering — one of the 22 domains its ontology collection spans, with a materials dataset published on the official hub — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the materials science subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`STRUCT` crystal structure & crystallography, including diffraction analysis · `CHAR` materials characterization, microscopy & spectroscopy · `INSTR` instrument operation & self-driving laboratories · `COMP` computational materials science (DFT, molecular dynamics, mesoscale simulation) · `INFO` materials informatics, data curation & property prediction · `SYN` synthesis & processing · `NANO` nanomaterials · `POLY` polymers, soft matter & composites · `METAL` metallurgy & alloys · `MECH` mechanical behavior of materials · `THERMO` thermodynamics & phase diagrams · `CORR` corrosion, degradation & failure analysis · `DISC` materials discovery & design · `GEN` curriculum-wide or unspecified, no single subfield

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
| ResearchClawBench | GEN | ✔ | ✔ | ◐ | ✔ | ✔ | ✔ | ✔ | **6.5** | ◐ | ✔ | ◐ | 0 | ? | 3 | **5** |
| Imaging-101 | CHAR, COMP | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| Agentic Self-Driving Microscopy Benchmarks | INSTR, CHAR | ✘ | ✘ | ✔ | ◐ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| AFMBench | INSTR, CHAR | ? | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✘ | 0 | 2 | 4 | **6** |
| Science Edge Evaluation (SEE) | CHAR, STRUCT | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ◐ | 2 | ? | 3 | **5.5** |
| AutoMat | COMP, INFO | ? | ✘ | ✘ | ◐ | ✔ | ✘ | ✔ | **2.5** | ◐ | ✔ | ✘ | 1 | 1 | 3 | **6.5** |
| MatCha | CHAR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✔ | ✘ | ◐ | 3 | 3 | 4 | **11.5** |
| ChemX | NANO, INFO | ? | ✘ | ✘ | ◐ | ✘ | ✔ | ◐ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MatVQA | CHAR, STRUCT | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MatViX | POLY, INFO | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| AlchemyBench | SYN | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ◐ | ✔ | ✔ | 1 | 3 | 1 | **7.5** |
| MatQnA | CHAR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| MaCBench | CHAR, INSTR | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ✘ | 2 | ? | 4 | **6** |
| CASCADE | COMP, INFO | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| Materials Hypothesis Generation | DISC | ✘ | ◐ | ✘ | ✘ | ✔ | ✘ | ✘ | **1.5** | ◐ | ✔ | ✔ | 1 | 1 | 1 | **5.5** |
| AutoDFT / VASPBench | COMP | ? | ✘ | ✘ | ✘ | ◐ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 1 | 1 | **5** |
| MatTools | COMP, INFO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| SciConvBench | COMP | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✔ | ◐ | 1 | ? | 3 | **5.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| MatSciBench | GEN | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ◐ | 2 | 3 | 3 | **8.5** |
| MatText | INFO, STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 4 | **10** |
| AtomWorld | STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 2 | **9** |
| ERI Benchmark | STRUCT, MECH, THERMO, POLY, CORR | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| MaScQA | GEN, METAL | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| LLM4Mat-Bench | INFO, STRUCT | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| OpenXRD | STRUCT, CHAR | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| SciCode | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | INFO | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [AFMBench](../works/afmbench.md)
- [AutoMat](../works/automat.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [SciCode](../works/scicode.md)
- [SciConvBench](../works/sciconvbench.md)
- [ChemX](../works/chemx.md)
- [MaCBench](../works/macbench.md)
- [MaScQA](../works/mascqa.md)
- [MatSciBench](../works/matscibench.md)
- [LLM4Mat-Bench](../works/llm4mat-bench.md)
- [MatText](../works/mattext.md)
- [AtomWorld](../works/atomworld.md)
- [OpenXRD](../works/openxrd.md)
- [MatVQA](../works/matvqa.md)
- [MatCha](../works/matcha.md)
- [MatQnA](../works/matqna.md)
- [MatViX](../works/matvix.md)
- [MatTools](../works/mattools.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [AlchemyBench](../works/alchemybench.md)
- [Materials Hypothesis Generation](../works/materials-hypothesis.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [Imaging-101](../works/imaging-101.md)
- [CASCADE](../works/cascade.md)
- [OntoLearner](../works/ontolearner.md)
