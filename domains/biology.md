# Biology

> **English** | [简体中文](../zh/domains/biology.md) · [← All domains](./README.md)

## Scope

Life-science evaluation from molecular to population scale. Bioinformatics, genomics, and single-cell biology fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Aviary | 2024 | Molecular cloning (DNA-construct manipulation) and protein engineering: propose stabilizing mutations on real proteins; plus scientific-literature research (LitQA2). | POMDP environments with terminal rewards: SeqQA (500 train / ~140 test cloning questions), Protein Stability (mutation proposals on 40 proteins from the megascale stability dataset), LitQA2 (248 questions). | SeqQA / LitQA2 by multiple-choice accuracy; protein tasks pass iff the proposed mutation's Rosetta ΔΔG < 0 (stabilizing). | [→](../works/aviary.md) |
| HeurekaBench | 2026 | Answer open-ended single-cell biology research questions — derived from 41 validated insights in 13 Nature and Cell papers — by autonomously designing and executing multi-step analyses on the studies' datasets. | 50 open-ended + 50 multiple-choice questions (Lite subset: 22 + 18 restricted to datasets under 750 MB), produced by a semi-automated insight-to-question pipeline. | Ground truth is the published finding; open-ended answers scored 1–5 by a G-Eval GPT-4o judge over atomic-fact overlap, multiple choice by accuracy. | [→](../works/heurekabench.md) |
| GeneBench-Pro | 2026 | Multistage statistical analyses in genomics, quantitative biology, and translational biomedicine, with 3–13 inferential forks per problem where a plausible wrong choice changes the downstream answer. | 129 problems built on constructively simulated data-generating processes with fully known causal structure, deliberately avoiding textbook examples. | Binary grading against recoverable targets with exact-match rules and numeric tolerances; no partial credit; 10 independent attempts per model–problem pair. | [→](../works/genebench-pro.md) |
| SciAgentArena | 2026 | Real biomedical research scenarios across single-cell omics, spatial omics, computational drug discovery, EHR modeling, and genetics. | ~200 tasks in four categories (Data Analysis, Optimization, Discovery, Validity) in an interactive, agent-agnostic environment; Validity tasks include deliberately infeasible requests. | Per-domain stepwise verification — expert-designed binary criteria, action-level F1, and task-native metrics (AUROC, Jaccard, correlation) — execution- and expert-criteria-based, no LLM judge. | [→](../works/sciagentarena.md) |
| ScienceAgentBench | 2024 | Bioinformatics tasks — 27 of its 102 — extracted from peer-reviewed data-driven discovery workflows. | Each task requires generating a self-contained Python program reproducing an analysis from a real publication. | Valid execution plus task-specific hand-written success checkers against expert-annotated references; figure outputs judged by GPT-4o. | [→](../works/scienceagentbench.md) |
| NatureBench | 2026 | Match the published state of the art of Nature-family Cellular Omics (31) and Protein Biology (16) studies — 47 of its 90 tasks — given the target algorithm's inputs but none of its operations or outputs. | Code-agent tasks built by a review-gated pipeline with an information firewall; ~3.7 primary metrics per task. | SOTA-normalized relative gap g on each paper's own primary metric; Match-SOTA (g ≥ 0) and Surpass-SOTA (g > 0.1) rates, with a judge flagging shortcut runs. | [→](../works/naturebench.md) |
| AIRS-Bench | 2026 | Frontier research-science tasks in bioinformatics, one of its four fields, covering the full research lifecycle with no baseline code provided. | 20 tasks total across the suite; the agent submits held-out test-split predictions as a CSV. | Execution-based, outcome-only scoring by task-specific evaluators; SOTA-normalized score with a 'march of nines' transform near the ceiling. | [→](../works/airs-bench.md) |
| AstaBench | 2025 | Biology-domain benchmarks within its 11-benchmark scientific-research suite — e.g., data-driven discovery in DiscoveryBench — alongside CS-weighted literature, code, and discovery tasks. | 2,400+ problems across 11 benchmarks with a standard, reproducible tool environment; 57 agents scored. | Per-benchmark metrics from exact match to LLM-judged hypothesis matching, reported with time-invariant dollar-cost accounting and score-vs-cost Pareto frontiers. | [→](../works/astabench.md) |
| Terminal-Bench Science | 2026 | Biology tasks within the Life Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Life is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| MDArena | 2026 | Run realistic biomolecular-simulation workflows — including membrane-protein systems — covering trajectory analysis, system preparation, free-energy calculations, and enhanced sampling. | 50 containerized tasks sourced from active research projects, spanning 29 molecular systems and 14 research protocols. | Strict-Pass@1 as the headline metric, with correctness and process-reward metrics crediting partial progress. | [→](../works/mdarena.md) |
| SciCode | 2024 | Write research code for scientist-curated problems; biology is among the five main domains its 16 natural-science subfields span. | 80 main problems decomposed into 338 subproblems mixing knowledge recall, reasoning, and code synthesis. | Execution against scientist-annotated gold-standard solutions and test cases. | [→](../works/scicode.md) |
| GenoTEX | 2024 | Automate gene expression analysis for gene-trait association: dataset selection, preprocessing, and statistical analysis to computational-genomics standards. | 1,384 analysis problems over 911 datasets (official repository); multi-step code-writing pipelines with self-correction. | Comparison against expert-curated annotations, reference code, and results from bioinformaticians. | [→](../works/genotex.md) |
| BixBench | 2025 | Perform exploratory computational-biology data analysis drawn from real published notebook analyses. | 50+ scenarios with ~300 open-answer questions (abstract; current repository lists 205 questions), run as multi-step agent trajectories with containerized execution. | LLM-graded open answers plus exact-match multiple choice; majority vote over replicas. | [→](../works/bixbench.md) |
| BioAgent Bench | 2026 | Complete end-to-end bioinformatics pipelines: RNA-seq, variant calling, metagenomics, and related workflows. | Manually curated pipeline tasks completed from prompts to concrete output artifacts, across multiple agent harnesses. | LLM grader over output artifacts for progress and validity; perturbation robustness suite (corrupted inputs, decoys, prompt bloat). | [→](../works/bioagent-bench.md) |
| scBench | 2026 | Perform single-cell RNA-seq analysis steps that recover known biological results. | 394 verifiable problems across six sequencing platforms and seven task categories, each from a pre-step data snapshot. | Deterministic grader on recovery of a key biological result; accuracy. | [→](../works/scbench.md) |
| scBench-Long | 2026 | Recover the published scientific conclusions of real single-cell studies from raw or near-raw data, with no prescribed methods. | 21 long-horizon evaluations over scRNA/TCR, RNA+ATAC, cross-species, and immune-repertoire data; 1,068 completed trajectories. | Controlled answer vocabularies with deterministic grading and trajectory rubrics. | [→](../works/scbench-long.md) |
| SpatialBench | 2025 | Analyze real spatial-biology data to recover known biological results. | 146 verifiable problems across five spatial technologies and seven task categories, from pre-step snapshots. | Deterministic grader on recovery of a key biological result; accuracy. | [→](../works/spatialbench.md) |
| BAISBench | 2025 | Annotate cell types and answer discovery questions grounded in the conclusions of published single-cell studies. | 15 expert-labeled annotation datasets plus 193 MCQs from 41 published studies; human baseline from six graduate-level bioinformaticians. | Hierarchical cell-type-tree annotation scoring plus MCQ correctness against published conclusions. | [→](../works/baisbench.md) |
| BioXArena | 2026 | Build and train predictive models on biomedical data across nine domains from sequence modeling to biomedical imaging. | 76 end-to-end ML tasks in a standardized 2-hour single-GPU environment; agents submit predictions on private test samples. | Hidden labels with held-out graders and biology-aware metrics normalized to 0–1. | [→](../works/bioxarena.md) |
| BioProBench | 2025 | Understand, order, correct, generate, and reason over biological wet-lab protocols. | 523,784 task instances from 22,413 human-written protocols across five task types; static evaluation. | Task-specific metrics including step recall/precision, Kendall's tau, exact match, and BLEU. | [→](../works/bioprobench.md) |
| SciGym | 2025 | Design experiments iteratively to uncover the mechanism of hidden systems-biology models. | Sequential experiment-design episodes over hidden SBML-encoded systems; 137 evaluated, 350 released. | Recovered models compared against hidden ground-truth SBML systems. | [→](../works/scigym.md) |
| LAB-Bench | 2024 | Exercise the practical capabilities of biology research: literature, figures, databases, protocols, DNA/protein sequences, and cloning. | 2,400+ multiple-choice questions in eight categories / 30 subtasks; static, tool-use optional. | MCQ scoring against human expert biology researchers. | [→](../works/lab-bench.md) |
| LABBench2 | 2026 | The same biology-research capabilities under realistic contexts: PDFs, images, and bioinformatics files. | Nearly 1,900 tasks across hardened subtask families including patents, source quality, and clinical trials. | Accuracy via the released harness; −26% to −46% model-specific drops versus LAB-Bench. | [→](../works/labbench2.md) |
| BioKGBench | 2024 | Verify scientific claims and interrogate biomedical knowledge graphs to locate factual errors. | 2,000+ atomic instances (claim verification, KGQA) plus 225 annotated agentic KGCheck instances over UniProt, STRING, Reactome, DisGeNET. | Atomic-task correctness plus agent-level KGCheck scoring; 90+ real database errors surfaced. | [→](../works/biokgbench.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of biology data — one of its seven application domains — translating natural-language intent into executable visualization operations, including napari-based bioimage tooling. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | Interleaved web-browsing-plus-computation questions in the biochemistry domain (folding into Biology) — multi-hop identification of biomolecular entities and retrieval of quantitative properties from sources such as UniProt, RCSB PDB, and PubChem, then domain-specific computation. | Answer-first questions synthesized from knowledge-graph chains requiring multi-hop identification, quantitative-property retrieval, and multi-step computation; spans five domains (biochemistry, geophysical, financial, security, history), of which biochemistry is one. | Execution-based: gold answers computed by executing parameterized code over knowledge-graph values, scored within ~2% relative tolerance; two-stage difficulty cascade; 76% human-validated validity. | [→](../works/drbencher.md) |
| Science Edge Evaluation (SEE) | 2026 | Evidence-bounded reasoning over real biology experimental data — bioactivity measurements, Cryo-EM structures, Western blot and gel-electrophoresis images, and microscopy — rather than concept recall; biology is one of its three disciplines. | 1,116 expert-curated multimodal questions (1,049 public) across three experimental disciplines (chemistry, biology, materials science) and 17 sub-fields, in multiple-choice and numerical fill-in-the-blank formats; a visual-agent setting adds web search and a code interpreter. | Answers scored against expert ground truth — exact match for multiple choice, expert tolerance for numerical answers — under a strict binary LLM-as-judge protocol (Gemini 3.1 Pro); image-ablation checking confirms each question needs its visual input. | [→](../works/science-edge-evaluation.md) |
| Fisher-R1 / P-Bench | 2026 | Statistically valid hypothesis testing on real biology datasets (from peer-reviewed papers with data on cBioPortal) — biology is one of its three fields — testing whether an agent's reported p-value is valid given the data's assumptions. | 425 open-ended hypothesis-testing tasks (Easy 203 / Hard 222) spanning economics, biology, and medicine; each gives only a hypothesis and a dataset and requires selecting a statistical test, computing a p-value, and drawing a reject/fail-to-reject conclusion. Per-domain counts not stated in the card. | Ground-truth p-values, test statistics, and decisions read off a logged run of canonical reference code; scored as Raw (decision match) and Strict (decision plus p-value closeness within 0.5 z-score units), pass@1 and pass@3. | [→](../works/fisher-r1.md) |
| ScienceBoard | 2025 | Structural and molecular biology work driven through UCSF ChimeraX — one of the six professional applications instantiating its domains. | 169 human-curated computer-use tasks in a single Ubuntu virtual machine: 38 GUI-only, 33 CLI-only, 98 hybrid GUI+CLI; per-application task counts are not published. | Programmatic checking of key intermediate input/output and of the final virtual-machine state through templates supporting exact match, range-based assessment and numerical tolerance; biochemistry is among the highest-scoring domains (up to 62.07% for GPT-5). | [→](../works/scienceboard.md) |
| Imaging-101 | 2026 | Biological computational imaging — one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| SciVQR | 2026 | Multimodal scientific reasoning in biology, one of six top-level scored subjects. | 3,254 image-paired competition and exam questions across six subjects and 54 subfields (2,545 multiple-choice, 709 free-form; easy/medium/hard tiers); 15 multimodal models zero-shot, with and without CoT. Per-subject item counts are not published. | Zero-shot accuracy reported per subject, plus a five-dimension rubric (faithfulness, informativeness, redundancy, hallucination, missing steps) scoring the generated reasoning against expert-authored solution traces. | [→](../works/scivqr.md) |
| HiSciBench | 2025 | Biology across the hierarchy: literature parsing, translation and question answering over arXiv biology papers, plus data-driven discovery in which the model writes and executes Python analysis code. | 2,324 biology instances within 8,735 — 200 general scientific QA, 45 literature OCR, 45 translation, 1,952 monolingual literature QA, 45 cross-lingual literature QA, 10 review topics and 27 data-driven discovery tasks; 18 models evaluated. | Level-appropriate metrics: accuracy at the QA levels, word-level accuracy for literature OCR, BLEU for translation, at the review level an LLM-judge 1–5 rubric over Coverage, Structure, Relevance, Synthesis and Critical Analysis plus citation verifiability, metadata accuracy, faithfulness and recency, and at the discovery level an execution-based Success Rate zeroed when the generated program fails to execute. | [→](../works/hiscibench.md) |
| FlyAOC | 2026 | Curate Drosophila melanogaster gene annotations end to end: given only a gene symbol, search and read the primary literature and emit ontology-grounded Gene Ontology function terms, expression patterns, and historical synonyms. | 100 benchmark genes posed as open-ended curation tasks over a fixed corpus of 16,898 full-text papers (reported as more than 140 million words from PubMed Central), with 7,397 expert-curated FlyBase annotations as ground truth across three annotation types. | Semantic recall@k against the FlyBase curation record — Wang similarity over the Gene Ontology directed acyclic graph for GO and expression terms (k = 20 and k = 10), case-insensitive exact match for synonyms — micro-averaged recall reported as the primary metric. | [→](../works/flyaoc.md) |
| Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes | 2026 | Produce Entity-Quality phenotype annotations for comparative vertebrate morphology, linking free-text character-state descriptions to terms in the UBERON, PATO, BSPO and GO ontologies. | The Dahdul et al. (2018) biocuration Gold Standard — 203 characters (463 character states) from seven phylogenetic studies, with scoring restricted to characters 51–203 (344 states); five frontier LLMs run as agentic curators in a self-contained workspace holding the source PDF, the human annotation guide, the ontologies, and a validation script. | Four ontology-based semantic-similarity metrics carried over unchanged from the original study (SimJ, NIC, partial precision, partial recall), scored against the Gold Standard and compared with three trained human biocurators and the Semantic CharaParser NLP baseline. | [→](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md) |
| BiomedSQL | 2025 | Answer human-genomics questions over GWAS summary statistics, SMR causal-inference results, allele frequencies and gene–pathway associations for neurodegenerative disease, supplying the statistical-genetics conventions — genome-wide significance thresholds, effect directionality — that the question never states. | 68,000 question / SQL query / answer triples over a ten-table BigQuery database ranging from a few hundred rows to 72.2M, templated from 40 expert-authored seed queries; models scored on a representative 546-question test set. | Execution Accuracy as the headline metric (the executed query output must match the gold execution result exactly), with Jaccard partial credit and syntax error rate alongside, against a measured baseline of two biomedical analysts at 90.0% EX. | [→](../works/biomedsql.md) |
| OntoLearner | 2026 | Construct ontology structure for biology and life sciences — one of the 22 domains its ontology collection spans — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |
| Apodex Discovery | 2026 | Adeno-associated virus capsid design across viability prediction, tropism prediction, structure prediction and generative design. | One of 20 executable environments, each supplying tools, data, budgets and a hidden verifier behind a fixed episode interface. | Task-specific experimental fitness measures against the published state of the art, which the system exceeded by 7% across all four tasks. | [→](../works/apodex-discovery.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the biology subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`GENOM` genomics, genetics & statistical genetics · `SCB` single-cell biology & transcriptomics · `SPAT` spatial biology & spatial transcriptomics · `MOLB` molecular & cell biology, cloning & biochemistry · `PROT` protein science & engineering · `STRB` structural biology & biomolecular simulation · `BIOINF` bioinformatics & computational biology · `SYSB` systems biology & mechanistic modeling · `IMM` immunology · `ECOEV` ecology, evolution & organismal biology · `DRUG` drug discovery & pharmacology · `IMG` bioimaging & microscopy · `PROTO` wet-lab protocols & experimental methods · `CURA` biocuration, ontologies & biological knowledge bases · `GEN` curriculum-wide or unspecified, no single subfield

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
| Imaging-101 | IMG | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| AIRS-Bench | BIOINF | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | ✔ | **5** | ◐ | ✘ | ✘ | 3 | 0 | 1 | **4.5** |
| FlyAOC | GENOM, CURA | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✘ | ✘ | 3 | 2 | 4 | **9.5** |
| scBench | SCB | ✔ | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **4.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| ScienceAgentBench | BIOINF | ✘ | ✘ | ✔ | ◐ | ✔ | ✔ | ✔ | **4.5** | ◐ | ✔ | ✔ | 2 | 1 | 2 | **7.5** |
| Apodex Discovery | PROT | ? | ◐ | ◐ | ✘ | ✔ | ✔ | ✔ | **4** | ◐ | ✔ | ◐ | 2 | 0 | 3 | **7** |
| AstaBench | GEN | ◐ | ✘ | ✔ | ✘ | ◐ | ✔ | ✔ | **4** | ✘ | ◐ | ◐ | 2 | ? | 2 | **5** |
| BioXArena | GEN | ✘ | ◐ | ✘ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 3 | 1 | 3 | **9** |
| SpatialBench | SPAT | ? | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| scBench-Long | SCB, IMM | ? | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✔ | ◐ | 2 | 1 | 3 | **7.5** |
| HeurekaBench | SCB | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | 2 | 3 | **7** |
| NatureBench | SCB, PROT | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✔ | 2 | 1 | 2 | **7** |
| Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes | ECOEV, CURA | ✘ | ✘ | ◐ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| Fisher-R1 / P-Bench | GENOM | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ✘ | ✘ | 3 | ? | 2 | **5.5** |
| BixBench | BIOINF | ? | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | 2 | 1 | **5** |
| SciVisAgentBench | IMG | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| SciAgentArena | SCB, SPAT, GENOM, DRUG | ? | ◐ | ◐ | ✘ | ✘ | ✔ | ✔ | **3** | ◐ | ✔ | ✘ | 3 | 2 | 3 | **9.5** |
| GenoTEX | GENOM, BIOINF | ✘ | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | 3 | 2 | **9** |
| LABBench2 | GEN | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| ScienceBoard | STRB | ? | ✘ | ✘ | ✔ | ✘ | ✔ | ✔ | **3** | ✔ | ✘ | ✘ | 3 | ? | 3 | **7** |
| Science Edge Evaluation (SEE) | STRB, IMG | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **3** | ✘ | ✘ | ✔ | 2 | ? | 3 | **6** |
| DrBencher | MOLB | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ✘ | ✔ | 3 | ? | 1 | **5** |
| BioAgent Bench | BIOINF, GENOM | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **3** | ✘ | ◐ | ✘ | 0 | 0 | 3 | **3.5** |
| LAB-Bench | GEN | ◐ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2.5** | ✔ | ✘ | ✔ | 3 | 3 | 1 | **9** |
| Aviary | MOLB, PROT | ✘ | ✘ | ✔ | ✘ | ✘ | ◐ | ✔ | **2.5** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| MDArena | STRB | ✔ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **2.5** | ✘ | ✔ | ✘ | 2 | 1 | 3 | **7** |
| HiSciBench | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ✘ | **2** | ✘ | ✔ | ✘ | 2 | 3 | 3 | **9** |
| SciGym | SYSB | ✘ | ✔ | ✘ | ✘ | ✘ | ✘ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 2 | 3 | **8** |
| BioKGBench | CURA | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| BAISBench | SCB | ? | ✘ | ✘ | ✘ | ✔ | ✔ | ✘ | **2** | ✔ | ✘ | ✘ | 3 | 2 | 1 | **7** |
| GeneBench-Pro | GENOM | ✘ | ◐ | ✘ | ✘ | ✘ | ✘ | ✔ | **1.5** | ✘ | ✘ | ✔ | 3 | 2 | 3 | **9** |
| BiomedSQL | GENOM | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✔ | ✘ | ✘ | 2 | 2 | 4 | **9** |
| BioProBench | PROTO | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 3 | 3 | **9** |
| SciVQR | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✔ | ✘ | 2 | ? | 3 | **6** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| SciCode | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
| OntoLearner | CURA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | ? | 3 | **6** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [Science Edge Evaluation (SEE)](../works/science-edge-evaluation.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [Aviary](../works/aviary.md)
- [HeurekaBench](../works/heurekabench.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [SciAgentArena](../works/sciagentarena.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [AstaBench](../works/astabench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [MDArena](../works/mdarena.md)
- [SciCode](../works/scicode.md)
- [GenoTEX](../works/genotex.md)
- [BixBench](../works/bixbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SpatialBench](../works/spatialbench.md)
- [BAISBench](../works/baisbench.md)
- [BioXArena](../works/bioxarena.md)
- [BioProBench](../works/bioprobench.md)
- [SciGym](../works/scigym.md)
- [LAB-Bench](../works/lab-bench.md)
- [LABBench2](../works/labbench2.md)
- [BioKGBench](../works/biokgbench.md)
- [ScienceBoard](../works/scienceboard.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
- [FlyAOC](../works/flyaoc.md)
- [Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes](../works/frontier-llm-based-agents-can-overcome-the-ontolog.md)
- [BiomedSQL](../works/biomedsql.md)
- [OntoLearner](../works/ontolearner.md)
- [Apodex Discovery](../works/apodex-discovery.md)
