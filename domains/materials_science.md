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
