# Chemistry

> **English** | [简体中文](../zh/domains/chemistry.md) · [← All domains](./README.md)

## Scope

Chemistry as the science, including computational chemistry and molecular design. Chemical process engineering belongs to Chemical Engineering.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| ScienceAgentBench | 2024 | Computational Chemistry tasks — 20 of its 102 — extracted from peer-reviewed data-driven discovery workflows. | Each task requires generating a self-contained Python program reproducing an analysis from a real publication. | Valid execution plus task-specific hand-written success checkers against expert-annotated references (e.g., metric thresholds); figure outputs judged by GPT-4o. | [→](../works/scienceagentbench.md) |
| NatureBench | 2026 | Match the published state of the art of Nature-family Molecular Design studies — 11 of its 90 tasks — given the target algorithm's inputs but none of its operations or outputs. | Code-agent tasks built by a review-gated pipeline with an information firewall; ~3.7 primary metrics per task. | SOTA-normalized relative gap g on each paper's own primary metric; Match-SOTA (g ≥ 0) and Surpass-SOTA (g > 0.1) rates, with a judge flagging shortcut runs. | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | Chemistry tasks within the Physical Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Chemistry is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| MDArena | 2026 | Run realistic computational-chemistry workflows over molecular dynamics: trajectory analysis, system preparation, alchemical free-energy calculations, and enhanced sampling. | 50 containerized tasks sourced from active research projects, spanning 29 molecular systems and 14 research protocols. | Strict-Pass@1 as the headline metric, with correctness and process-reward metrics crediting partial progress. | [→](../works/mdarena.md) |
| PhySciBench | 2026 | Answer expert-curated deep-research questions on the chemistry side of a physics/chemistry-balanced set, targeting fragile reasoning chains, limited cross-step knowledge transfer, and missing self-verification. | 200 expert-curated questions balanced between physics and chemistry, organized into six task categories reflecting real-world scientific workflows. | Accuracy-based evaluation comparing state-of-the-art models and agent systems, with cost reported alongside accuracy. | [→](../works/physcibench.md) |
| MetaSyn | 2026 | Conduct protocol-faithful systematic review and meta-analysis; chemistry is among the subjects its 422 expert-curated meta-analyses span. | Multi-stage systematic-review workflows: identify the eligible studies for a research question with structured PI/ECO criteria within a shared PubMed-anchored corpus containing ineligible distractors. | Study identification against the original expert reviewers' included set, with stage-wise evaluation locating failures along the meta-analysis pipeline. | [→](../works/metasyn.md) |
| SciCode | 2024 | Write research code for scientist-curated problems; chemistry is among the five main domains its 16 natural-science subfields span. | 80 main problems decomposed into 338 subproblems mixing knowledge recall, reasoning, and code synthesis. | Execution against scientist-annotated gold-standard solutions and test cases. | [→](../works/scicode.md) |
| SMDD-Bench | 2026 | Solve medicinal-chemistry design problems — 2D pharmacophore identification, scaffold hopping, lead optimization, fragment assembly — against protein targets. | 502 guaranteed-solvable multi-turn tasks over 102 targets under a limited oracle-call budget. | Solve rate over guaranteed-solvable instances; best frontier model 40.2%. | [→](../works/smdd-bench.md) |
| AInsteinBench | 2025 | Resolve maintainer-PR tasks in production scientific repositories; quantum chemistry and cheminformatics are among its six codebases. | Repository-level coding-agent tasks in executable environments. | Test-driven verification with expert-reviewed curation. | [→](../works/ainsteinbench.md) |
| ChemBench | 2024 | Measure chemical knowledge and reasoning against the expertise of human chemists. | 2,700+ curated question–answer pairs; static QA without tools. | Automated framework scoring with a recruited chemist baseline and confidence analysis. | [→](../works/chembench.md) |
| ChemEval | 2024 | Assess the chemical capabilities research professionals need, from literature understanding to advanced chemical knowledge. | 42 tasks across 4 progressive levels and 12 dimensions, from open-source data and expert-crafted material. | Zero- and few-shot evaluation with curated demonstrations and prompts. | [→](../works/chemeval.md) |
| ChemCoTBench | 2025 | Solve molecular property optimization and reaction prediction as step-by-step chemical operations. | 1,495 samples across 22 tasks posed as modular add/delete/substitute workflows. | Structured evaluation over annotated operation workflows with a reasoning taxonomy. | [→](../works/chemcotbench.md) |
| MolecularIQ | 2026 | Reason over molecular graphs — the structure that determines molecular properties. | Symbolically verifiable structure-reasoning tasks; static evaluation. | Symbolic verification against the molecular graph; failures localized to specific structures. | [→](../works/moleculariq.md) |
| ChemIQ | 2025 | Answer core organic-chemistry questions, including NMR structure elucidation, without tools. | 816 constructed-response short-answer questions in 8 categories. | Judge-free programmatic checking: exact match, OPSIN-parsed IUPAC, canonical SMILES. | [→](../works/chemiq.md) |
| FGBench | 2025 | Attribute molecular property differences to specific functional groups. | 625K generated problems over 245 functional groups; 7K curated benchmark subset. | Regression and classification scoring against dataset labels. | [→](../works/fgbench.md) |
| QCBench | 2025 | Perform quantitative calculations across analytical, bio/organic, general, inorganic, physical, polymer, and quantum chemistry. | 350 problems in 7 subfields and 3 difficulty tiers, built to defeat heuristic shortcuts. | Tiered accuracy on stepwise numerical calculation across 24 LLMs. | [→](../works/qcbench.md) |
| MolPuzzle | 2024 | Elucidate molecular structures from IR, MS, ¹H-NMR, and ¹³C-NMR spectra. | 200 instances in 3 stages (understanding, spectrum interpretation, construction); 23,678 examples. | Exact-match accuracy on final structures plus per-stage scores, with a human baseline. | [→](../works/molpuzzle.md) |
| MolQuest | 2026 | Elucidate structures by planning experiments and integrating heterogeneous spectra. | Multi-turn interactive episodes with model-initiated experimental steps. | Accuracy of final structures; SOTA ≈50%, most models below 30%. | [→](../works/molquest.md) |
| Speak-to-Structure (TOMG-Bench) | 2024 | Generate, edit, and optimize molecules from open-domain natural-language instructions. | Three task families (MolEdit, MolOpt, MolCustom); 5,000 samples per subtask in the original release. | One-to-many instruction-satisfaction checking rather than single-reference match. | [→](../works/tomg-bench.md) |
| MolLangBench | 2025 | Recognize, edit, and generate molecular structures through language, over strings, images, and graphs. | Three task families; recognition auto-constructed, editing and generation expert-annotated. | Per-task accuracy; GPT-5 at 86.2% / 85.5% / 43.0% on recognition / editing / generation. | [→](../works/mollangbench.md) |
| FukuyamaBench | 2026 | Deduce full elementary-step mechanisms for organic reactions. | Hierarchical mechanism-reasoning problems derived from Fukuyama's Advanced Organic Reaction Mechanism book. | Exact pathway match; best reported 8.3% (fine-tuned Qwen3-30B-A3B) vs. 5.1% (FlowER). | [→](../works/fukuyamabench.md) |
| ChemCensor / CREED | 2026 | Evaluate single-step retrosynthesis where many precursor sets are chemically valid. | Plausibility-based benchmarking framework plus millions of validated reaction records. | ChemCensor chemical-plausibility metric replacing exact-match Top-K. | [→](../works/chemcensor.md) |
| MOOSE-Chem | 2024 | Rediscover the hypotheses of recent high-impact chemistry papers. | 51 post-January-2024 papers annotated by PhD chemists; retrieve–compose–rank pipeline. | Similarity to annotated ground-truth hypotheses under a pre-2024 knowledge-cutoff control. | [→](../works/moose-chem.md) |
| ChemX | 2025 | Extract structured chemical data from scientific documents on nanomaterials and small molecules. | 10 manually curated, expert-validated datasets; agentic document extraction. | Extraction quality against domain-expert-validated records. | [→](../works/chemx.md) |
| ChemCost | 2026 | Price a chemical reaction: ground identities, retrieve quotes, select packs, compute cost. | 1,427 evaluable reactions over a frozen snapshot of 2,261 chemicals and 230,775 supplier quotes. | Judge-free exact ground truth with stage-level diagnosis; best agents 50.6% within 25% relative error. | [→](../works/chemcost.md) |
| onepot-Bench 0 | 2026 | Predict reaction outcomes and catalyst selections, plus cheminformatics literacy and refusal behavior. | Proprietary three-part suite (ChemAbacus, SynthRefusal, SynthBench) on private lab-generated data. | Per-suite scoring against private experimental ground truth. | [→](../works/onepot-bench.md) |
| MaCBench | 2024 | Do the visual work of chemistry research: read instruments, extract data, interpret experimental results. | Multimodal (image + text) tasks in three aspects; static vision-language evaluation. | Accuracy via the ChemBench pipeline; near-perfect extraction, limited cross-modal inference. | [→](../works/macbench.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of chemistry data — one of its seven application domains — translating natural-language intent into executable visualization operations, including molecular-dynamics tooling. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | Interleaved web-browsing-plus-computation questions in the biochemistry domain (folding into Chemistry) — multi-hop identification of chemical entities and retrieval of quantitative properties from sources such as PubChem, ChEMBL, and RCSB PDB, followed by domain-specific computation. | Answer-first questions synthesized from knowledge-graph chains requiring multi-hop identification, quantitative-property retrieval, and multi-step computation; spans five domains (biochemistry, geophysical, financial, security, history), of which biochemistry is one. | Execution-based: gold answers computed by executing parameterized code over knowledge-graph values, scored within ~2% relative tolerance; two-stage difficulty cascade; 76% human-validated validity. | [→](../works/drbencher.md) |
| Science Edge Evaluation (SEE) | 2026 | Evidence-bounded scientific reasoning over real chemistry experimental data — spectra (IR, NMR, mass spectrometry), X-ray diffraction, and related measurements — rather than concept recall; chemistry is one of its three disciplines. | 1,116 expert-curated multimodal questions (1,049 public) across three experimental disciplines (chemistry, biology, materials science) and 17 sub-fields, in multiple-choice and numerical fill-in-the-blank formats; a visual-agent setting adds web search and a code interpreter. | Answers scored against expert ground truth — exact match for multiple choice, expert tolerance for numerical answers — under a strict binary LLM-as-judge protocol (Gemini 3.1 Pro); image-ablation checking confirms each question needs its visual input. | [→](../works/science-edge-evaluation.md) |

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MDArena](../works/mdarena.md)
- [PhySciBench](../works/physcibench.md)
- [MetaSyn](../works/metasyn.md)
- [SciCode](../works/scicode.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [ChemBench](../works/chembench.md)
- [ChemEval](../works/chemeval.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [MolecularIQ](../works/moleculariq.md)
- [ChemIQ](../works/chemiq.md)
- [FGBench](../works/fgbench.md)
- [QCBench](../works/qcbench.md)
- [MolPuzzle](../works/molpuzzle.md)
- [MolQuest](../works/molquest.md)
- [Speak-to-Structure (TOMG-Bench)](../works/tomg-bench.md)
- [MolLangBench](../works/mollangbench.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [MOOSE-Chem](../works/moose-chem.md)
- [ChemX](../works/chemx.md)
- [ChemCost](../works/chemcost.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [MaCBench](../works/macbench.md)
