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
| Model Discovery Agent | 2026 | Discover an enzyme-kinetic rate law by choosing informative combinations of seven controllable chemical conditions. | 36 interactive ChemBench/ActiveSciBench-Chem tasks (12 mechanism families × 3 tiers), evaluated at two seeds and up to 60 designed experiments. | Held-out reaction-rate error on 1,000 novel conditions plus SymPy-based mathematical equivalence to the true rate law. | [→](../works/model-discovery-agent.md) |
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
| ChemEBench | 2025 | Molecular chemistry at the benchmark's L2 level: SMILES-to-IUPAC name translation, molecule naming from textual descriptions, molecular property prediction, and reaction prediction. | One of three progressive levels inside a suite of 15 dimensions and 101 distinct tasks; static single-response items, with 14 models compared. | Accuracy on objective items; subjective short-answer and calculation items graded 0–5 for completeness and clarity, with the reasoning chain checked step by step. | [→](../works/chemebench.md) |
| Imaging-101 | 2026 | Chemistry and materials computational imaging — one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| SciVQR | 2026 | Multimodal scientific reasoning in chemistry, one of six top-level scored subjects. | 3,254 image-paired competition and exam questions across six subjects and 54 subfields (2,545 multiple-choice, 709 free-form; easy/medium/hard tiers); 15 multimodal models zero-shot, with and without CoT. Per-subject item counts are not published. | Zero-shot accuracy reported per subject, plus a five-dimension rubric (faithfulness, informativeness, redundancy, hallucination, missing steps) scoring the generated reasoning against expert-authored solution traces. | [→](../works/scivqr.md) |
| HiSciBench | 2025 | Chemistry across the hierarchy: literature question answering over chemistry papers, plus data-driven discovery in which the model writes and executes Python analysis code. | 1,116 chemistry instances within 8,735 — 200 general scientific QA, 886 monolingual literature QA, 10 review topics and 20 data-driven discovery tasks; 18 models evaluated. | Level-appropriate metrics: accuracy at the QA levels, word-level accuracy for literature OCR, BLEU for translation, at the review level an LLM-judge 1–5 rubric over Coverage, Structure, Relevance, Synthesis and Critical Analysis plus citation verifiability, metadata accuracy, faithfulness and recency, and at the discovery level an execution-based Success Rate zeroed when the generated program fails to execute. | [→](../works/hiscibench.md) |
| MolClaw | 2026 | Computational drug-molecule chemistry: property filtering over RDKit descriptors, binding-affinity comparison, molecular docking and virtual screening, functional-group modification, and physicochemical property optimization toward QED, LogP and LogS targets. | MolBench in three tiers — screening (50 property-filtering, 37 binding-affinity, 25 docking items), optimization (39 functional-group items plus a property-optimization subtask whose count is `TODO(reference)`), and three end-to-end discovery challenges requiring 8 to 50+ sequential tool invocations; items sourced from CARA/ChEMBL, ACNet and ChemCoTBench. | Accuracy for property filtering and binding-affinity comparison, Hits@3 for docking screening, operational accuracy and property deltas with success rate for optimization, and task-specific weighted rubrics for the end-to-end tier (rubric weights and judge identity `TODO(reference)`). | [→](../works/molclaw.md) |
| CASCADE | 2025 | Chemistry research tasks in SciSkillBench: retrieving, processing and analysing chemical data and running computations through specialized chemistry toolkits and simulation codes. | 116 materials-science and chemistry tasks — 76 data-oriented and 40 computation-oriented, split again into 58 Level 0 tasks naming the key functions and 58 Level 1 tasks giving only a high-level objective; three repetitions per configuration over 16,008 experiment runs. | Outcome-based automated scoring: the agent's processed output is compared against the ground-truth answer within a predefined tolerance threshold, reported as success rate (GPT-5 DeepSolver 93.26% against 35.36% for the Native configuration). | [→](../works/cascade.md) |
| OntoLearner | 2026 | Construct ontology structure for chemistry — one of the 22 domains its ontology collection spans, with a chemistry dataset published on the official hub — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the chemistry subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`ORG` organic chemistry & reaction mechanisms · `ANAL` analytical chemistry & spectroscopy · `SYN` synthesis planning & retrosynthesis · `QC` quantum & electronic-structure chemistry · `MD` molecular dynamics & biomolecular simulation · `CHEMINF` cheminformatics & molecular representation · `MOLDES` molecular design & generation · `MED` medicinal chemistry & drug discovery · `BIOCHEM` biochemistry & chemical biology · `NANO` nanomaterials & materials chemistry · `GEN` curriculum-wide or unspecified, no single subfield

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
| ScienceAgentBench | CHEMINF | ◐ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✔ | 2 | 1 | 2 | **7.5** |
| Imaging-101 | ANAL, NANO | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| PhySciBench | GEN | ◐ | ◐ | ◐ | ✔ | ✘ | ✔ | ✔ | **4.5** | ✘ | ✔ | ✘ | 2 | 2 | 1 | **6** |
| MolQuest | ANAL | ? | ◐ | ✔ | ✘ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| NatureBench | MOLDES | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 2 | 1 | 2 | **7** |
| MetaSyn | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 2 | ? | 3 | **6** |
| SciVisAgentBench | MD | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| SMDD-Bench | MED | ✘ | ✘ | ✔ | ◐ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 2 | 2 | **8** |
| MolClaw | MED, MOLDES | ✔ | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | **3** | ✘ | ✔ | ✘ | 2 | 2 | 2 | **7** |
| Science Edge Evaluation (SEE) | ANAL | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ◐ | 2 | ? | 4 | **6.5** |
| DrBencher | BIOCHEM | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | 1 | 1 | **6** |
| CASCADE | CHEMINF, NANO | ✔ | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
| Model Discovery Agent | GEN | ✘ | ✔ | ✔ | ✘ | ✘ | ✘ | ✔ | **3** | ✘ | ✘ | ✘ | 3 | 1 | 4 | **8** |
| ChemCost | SYN | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | **2.5** | ✔ | ✘ | ✘ | 3 | 3 | 4 | **11** |
| ChemX | NANO, MED | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **2.5** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| MDArena | MD, BIOCHEM | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ◐ | ✔ | ✘ | 2 | 1 | 2 | **6.5** |
| MOOSE-Chem | GEN | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✘ | **2.5** | ◐ | ◐ | ✔ | 1 | 1 | 2 | **6** |
| MaCBench | ANAL, NANO | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✘ | ◐ | 2 | ? | 4 | **6.5** |
| HiSciBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| MolLangBench | CHEMINF, MOLDES | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| ChemCensor / CREED | SYN | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ◐ | ✘ | ✔ | 3 | 3 | 2 | **9.5** |
| MolPuzzle | ANAL, ORG | ✘ | ✘ | ✘ | ✔ | ✘ | ? | ✘ | **1** | ✔ | ✘ | ✘ | 3 | 3 | 2 | **9** |
| SciVQR | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| AInsteinBench | QC, CHEMINF | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| onepot-Bench 0 | SYN, CHEMINF | ? | ✘ | ? | ? | ✘ | ✔ | ✘ | **1** | ? | ? | ✔ | 2 | ? | 0 | **3** |
| ChemBench | GEN | ◐ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0.5** | ✔ | ✘ | ◐ | 2 | 3 | 2 | **8.5** |
| FGBench | CHEMINF | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ✘ | ✘ | ✘ | 3 | 3 | 1 | **7** |
| MolecularIQ | CHEMINF | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| ChemIQ | ORG, ANAL | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 4 | **9.5** |
| ChemEval | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✔ | 3 | 2 | 2 | **8** |
| ChemCoTBench | MOLDES, ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| Speak-to-Structure (TOMG-Bench) | MOLDES | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 3 | 1 | **7.5** |
| FukuyamaBench | ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| QCBench | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 2 | 2 | 2 | **6.5** |
| SciCode | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | ? | 0 | **3.5** |
| ChemEBench | CHEMINF, ORG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ◐ | ✘ | 2 | ? | 0 | **2.5** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: `?` records a source that does not settle the column, not an inferred absence. This matters most for `Net` and for per-domain `Scale` in multi-domain suites, where papers often report only a total task count.

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
- [Model Discovery Agent](../works/model-discovery-agent.md)
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
- [ChemEBench](../works/chemebench.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
- [MolClaw](../works/molclaw.md)
- [CASCADE](../works/cascade.md)
- [OntoLearner](../works/ontolearner.md)
