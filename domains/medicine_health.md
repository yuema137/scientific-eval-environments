# Medicine & Health

> **English** | [简体中文](../zh/domains/medicine_health.md) · [← All domains](./README.md)

## Scope

Clinical and biomedical-application evaluation: medical tasks, drug discovery, EHR modeling, biomedical modeling.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| MedHELM | 2025 | Medical and clinical language tasks under a clinician-validated taxonomy of 5 categories and 22 subcategories — from clinical note generation to administration and workflow. | 121 tasks aggregated across 35 benchmarks (17 existing + 18 newly formulated), developed with 29 clinicians. | LLM-jury evaluation with measured clinician agreement (ICC = 0.47), reported to outperform ROUGE-L and BERTScore baselines. | [→](../works/medhelm.md) |
| SciAgentArena | 2026 | Computational drug discovery and EHR modeling among its five biomedical research fields — e.g., hERG toxicity prediction and FHIR query construction. | ~200 tasks in four categories (Data Analysis, Optimization, Discovery, Validity) in an interactive, agent-agnostic environment. | Per-domain stepwise verification: expert-designed binary criteria, action-level F1 for EHR tasks, and task-native metrics such as AUROC averaged over independent runs; no LLM judge. | [→](../works/sciagentarena.md) |
| NatureBench | 2026 | Match the published state of the art of Nature-family Biomedical Modeling studies — 14 of its 90 tasks — given the target algorithm's inputs but none of its operations or outputs. | Code-agent tasks built by a review-gated pipeline with an information firewall; ~3.7 primary metrics per task. | SOTA-normalized relative gap g on each paper's own primary metric; Match-SOTA (g ≥ 0) and Surpass-SOTA (g > 0.1) rates, with a judge flagging shortcut runs. | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | Medicine tasks within the Life Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| MetaSyn | 2026 | Conduct protocol-faithful systematic review and meta-analysis; medical science is among the subjects its 422 expert-curated meta-analyses span. | Multi-stage systematic-review workflows: identify the eligible studies for a research question with structured PI/ECO criteria within a shared PubMed-anchored corpus containing ineligible distractors. | Study identification against the original expert reviewers' included set, with stage-wise evaluation locating failures along the meta-analysis pipeline. | [→](../works/metasyn.md) |
| CORE-Bench | 2024 | Reproduce published computational results from each paper's own code and data; medicine is one of its three disciplines. | 270 tasks from 90 papers at three difficulty levels, in language-only and vision-language forms. | Accuracy of reproduced results, checked by a fast, parallelizable evaluation harness. | [→](../works/core-bench.md) |
| MedAgentGym | 2025 | Solve code-centric biomedical data-science tasks, including EHR-derived scenarios (MIMIC-III, eICU per the official repository). | 72,413 task instances across 129 categories from 12 real scenarios, in executable sandboxes with interactive feedback. | Verifiable ground-truth annotations checked in sandboxes; 29 LLMs benchmarked. | [→](../works/medagentgym.md) |
| SMDD-Bench | 2026 | Design small-molecule drugs against protein targets: pharmacophores, interaction points, scaffold hopping, lead optimization, fragment assembly. | 502 guaranteed-solvable multi-turn tasks over 102 protein targets, under a limited oracle-call budget. | Solve rate over guaranteed-solvable instances; best frontier model 40.2%. | [→](../works/smdd-bench.md) |
| MedBrowseComp | 2025 | Retrieve and reconcile multi-hop medical facts across live sources: trials, primary studies, regulatory records, patents, cost data. | 1,000+ physician-curated questions in deep-research and computer-use splits (50/605/484 per the official dataset). | Gold-answer checking over live retrieval. | [→](../works/medbrowsecomp.md) |
| AgentClinic | 2024 | Diagnose patients through sequential dialogue, multimodal data collection under incomplete information, and tool use. | Simulated clinical encounters across nine specialties and seven languages, with patient, measurement, and moderator agents. | Diagnostic accuracy with bias perturbations and patient-centric metrics; supported by real EHRs and a clinical reader study. | [→](../works/agentclinic.md) |
| MedAgentBench | 2025 | Execute physician-written clinical tasks against production-standard EHR interfaces. | 300 patient-specific tasks in 10 categories over 100 realistic profiles (700K+ data elements) in a FHIR-compliant environment. | Programmatic success-rate checking against reference solutions; best model 69.67%. | [→](../works/medagentbench.md) |
| SDBench | 2025 | Reach diagnoses by iteratively querying a gatekeeper for findings and ordering costed tests. | 304 NEJM-CPC cases as sequential encounters; physician cohort baseline (21 clinicians, 20% mean accuracy). | Diagnostic accuracy scored jointly with the cost of visits and tests. | [→](../works/sdbench.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of medical-science data — one of its seven application domains — translating natural-language intent into executable visualization operations over volumetric and multimodal medical data. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |
| Fisher-R1 / P-Bench | 2026 | Statistically valid hypothesis testing on real medical/biostatistics datasets (Vanderbilt Biostatistics teaching materials, R-package datasets) — medicine is one of its three fields — covering both randomized experiments and observational studies. | 425 open-ended hypothesis-testing tasks (Easy 203 / Hard 222) spanning economics, biology, and medicine; each gives only a hypothesis and a dataset and requires selecting a statistical test, computing a p-value, and drawing a reject/fail-to-reject conclusion. Per-domain counts not stated in the card. | Ground-truth p-values, test statistics, and decisions read off a logged run of canonical reference code; scored as Raw (decision match) and Strict (decision plus p-value closeness within 0.5 z-score units), pass@1 and pass@3. | [→](../works/fisher-r1.md) |
| MiraMind | 2025 | Evidence-constrained mental-health / psychiatric clinical reasoning — diagnosis, intervention selection, and psychiatry question answering — where the warranted specificity, certainty, and severity of judgments is itself evaluated (folds into Medicine & Health). | Six task families over 13 datasets (appraisal, diagnosis, intervention, multi-step psychiatry QA, abstraction, verification) spanning informal user narratives, counseling dialogues, psychiatric board-style QA, and Cochrane review abstracts; 20 LLMs. | Per-family outcome metrics (Micro-F1, Jaccard, expert-scoring-point recall, Macro-F1) plus an LLM-as-judge trajectory rubric (usability, logical structure, informational contribution) validated on 100 human-annotated trajectories. | [→](../works/miramind.md) |
| Imaging-101 | 2026 | Medical computational imaging — one of its six named domains — recovering hidden signals from indirect, noisy measurements through a full reconstruction pipeline. | 57 paper-grounded tasks across six domains, each canonicalized into preprocessing → forward physics modeling → inverse solver → visualization and evaluated on planning, function-level and end-to-end tracks; per-domain task counts are `TODO(reference)`. | End-to-end reconstructions executed and scored against per-task `metrics.json` acceptance thresholds using normalized cross-correlation and NRMSE; function-level work checked by paired pytest suites synthesized from captured reference input/output. | [→](../works/imaging-101.md) |
| MolClaw | 2026 | Computational drug discovery: virtual screening and binding-affinity reasoning against protein targets, molecular editing, and structure-guided lead optimization of a named drug molecule (Erlotinib). | MolBench in three tiers — screening (50 property-filtering, 37 binding-affinity, 25 docking items), optimization (39 functional-group items plus a property-optimization subtask whose count is `TODO(reference)`), and three end-to-end discovery challenges requiring 8 to 50+ sequential tool invocations, with the lead-optimization challenge running up to fifteen rounds. | Accuracy for property filtering and binding-affinity comparison, Hits@3 for docking screening, operational accuracy and property deltas with success rate for optimization, and task-specific weighted rubrics for the end-to-end tier; the authors state all end-to-end results are purely computational, with wet-lab validation still required. | [→](../works/molclaw.md) |
| RubricsTree | 2026 | Consumer and clinical personal-health question answering — medical explanation, interpretation of user health and wearable-sensor metrics, advice and action planning, and symptom handling — judged for clinical correctness rather than style. | N/A as a task suite: a judging framework built on over 100 atomic, clinically verifiable Boolean rubrics in a hierarchical DAG, curated from roughly 4,000 real user queries. Meta-evaluation uses 532 real-world queries across four scenarios with controlled perturbations; downstream optimization is measured on HealthBench-Hard (362 queries). | Agreement with a physician-led expert panel measured by ICC₃ (0.876) and Cohen's κ (0.787) against 0.291 and 0.431 for a principle-based baseline, plus oracle-perturbation tests checking that contextually degraded responses are penalized. | [→](../works/rubricstree.md) |
| BiomedSQL | 2025 | Answer clinical-translation questions over drug gene targets, indications, licensing status and dosages, supplying the implicit criteria — which trial phase counts as approved, which direction of effect answers the question — that the natural-language question never states. | 68,000 question / SQL query / answer triples over a ten-table BigQuery database ranging from a few hundred rows to 72.2M, templated from 40 expert-authored seed queries; models scored on a representative 546-question test set labelled across nine biomedical reasoning categories. | Execution Accuracy as the headline metric (the executed query output must match the gold execution result exactly), with Jaccard partial credit and syntax error rate alongside, against a measured baseline of two biomedical analysts at 90.0% EX. | [→](../works/biomedsql.md) |
| OntoLearner | 2026 | Construct ontology structure for medicine — one of the 22 domains its ontology collection spans, with a medicine dataset published on the official hub — by typing terms, recovering the is-a hierarchy between types, and extracting non-taxonomic relations. | 180 machine-readable ontologies across 22 domains with pipeline-ready train/dev/test splits for three ontology-learning tasks; 22 retrieval models and 12 LLMs evaluated in single-shot structured prediction rather than an agentic setting. | Precision, recall and F1 computed by normalized pair-level and triple-level matching against the gold ontology structure; per-domain and per-model scores are `TODO(reference)` in the card, the paper's results section not being retrievable. | [→](../works/ontolearner.md) |
| Apodex Discovery | 2026 | Drug repurposing and reformulation. | An executable biomedical environment supplying tools and data to a frontier backbone, compared against the same backbone closed-book. | Mean normalized prediction score over the closed-book control: +2.5 points for GPT-5.5 and +7.6 points for GPT-5.6-sol. | [→](../works/apodex-discovery.md) |
| Agents Catching Agents | 2026 | Whether committees of clinical decision-support agents adopt shortcut cues that a benchmark rewards but a clinician would ignore. | Seven cohorts over six public datasets — MedQA-USMLE, MedMCQA, MIMIC-CXR reports, NIH ChestX-ray14, MIMIC-CXR-JPG, CheXpert and SUPPORT2 — with a three-agent shared blackboard. | Adoption rate against the isolated-condition flip rate (5–16% solo against 38% with two asserting peers); three oversight detectors scored on precision, recall and false-positive rate. | [→](../works/agents-catching-agents.md) |

## Capability Matrix

A checklist view of the same works: what each one does and does not put under evaluation. It answers a different question from the Comparison table above — not *what science is being tested* but *what an evaluation setup covers and leaves out*.

**Marks.** `✔` present · `✘` explicitly absent · `◐` partial, optional, or true of only part of the suite · `?` not stated in the card or the primary source. `?` means the source is silent, not that the answer is no; it is a standing verification backlog, never a default. `Domain`, `Verif`, `Scale` and `Fail` are not yes/no columns — see below.

**`Domain`** names the medicine and health subfields the work actually evaluates in, taken from the card's `## Domains` prose. This vocabulary is specific to this page — each domain page defines its own, since one domain's subfields have nothing to say to another's.

`CLIN` clinical medicine & diagnosis · `PSY` psychiatry & mental health · `IMG` medical imaging & radiology · `EHR` electronic health records & clinical informatics · `DRUG` drug discovery & medicinal chemistry · `PHARM` pharmacology, regulation & drug approval · `EPI` epidemiology & clinical evidence synthesis · `BSTAT` biostatistics & clinical data analysis · `BMOD` biomedical modeling & computational biomedicine · `PH` personal & consumer health · `HPOL` health policy, economics & care administration · `KR` biomedical knowledge representation & terminology · `GEN` curriculum-wide or unspecified, no single subfield

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
| CORE-Bench | GEN | ✘ | ✘ | ✔ | ✔ | ✔ | ✔ | ✔ | **5** | ✘ | ✘ | ✘ | 3 | 1 | 3 | **7** |
| Imaging-101 | IMG | ? | ◐ | ◐ | ✔ | ✔ | ✔ | ✔ | **5** | ◐ | ✔ | ✘ | 2 | ? | 3 | **6.5** |
| AgentClinic | CLIN, EHR | ✔ | ✔ | ✘ | ◐ | ✘ | ✔ | ✔ | **4.5** | ✘ | ✘ | ✘ | 0 | 3 | 3 | **6** |
| MedBrowseComp | PHARM, HPOL | ✔ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **4** | ✘ | ✘ | ✔ | 1 | 3 | 3 | **8** |
| SDBench | CLIN, HPOL | ✘ | ✔ | ✔ | ✘ | ✘ | ✔ | ✔ | **4** | ✔ | ✔ | ✔ | 1 | 2 | 1 | **7** |
| SciAgentArena | DRUG, EHR | ? | ◐ | ◐ | ✔ | ✘ | ◐ | ✔ | **3.5** | ◐ | ✔ | ✘ | 3 | 1 | 3 | **8.5** |
| Apodex Discovery | DRUG | ? | ✔ | ◐ | ? | ✘ | ✔ | ✔ | **3.5** | ✘ | ✔ | ◐ | 2 | 0 | 3 | **6.5** |
| NatureBench | BMOD | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | **3.5** | ◐ | ✘ | ◐ | 2 | 1 | 2 | **6** |
| SciVisAgentBench | IMG | ? | ✘ | ◐ | ✔ | ✘ | ✔ | ✔ | **3.5** | ✘ | ✘ | ✘ | 2 | ? | 1 | **3** |
| MetaSyn | EPI | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ◐ | **3** | ◐ | ✘ | ◐ | 2 | 2 | 3 | **8** |
| MedAgentGym | EHR, BMOD | ? | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | **2.5** | ? | ✘ | ✔ | 3 | 3 | 4 | **11** |
| Agents Catching Agents | CLIN, IMG | ✘ | ✘ | ✘ | ✔ | ✘ | ✔ | ◐ | **2.5** | ✘ | ✘ | ✘ | 3 | 2 | 4 | **9** |
| Fisher-R1 / P-Bench | BSTAT | ✘ | ✘ | ✘ | ✘ | ◐ | ✔ | ✔ | **2.5** | ◐ | ✘ | ✔ | 3 | ? | 2 | **6.5** |
| MolClaw | DRUG | ? | ◐ | ✘ | ✘ | ✘ | ◐ | ✔ | **2** | ✘ | ✔ | ✘ | 2 | 2 | 3 | **8** |
| SMDD-Bench | DRUG | ✘ | ✘ | ◐ | ✘ | ✘ | ◐ | ✔ | **2** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| MedAgentBench | EHR | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ | **2** | ✘ | ✘ | ◐ | 3 | 2 | 2 | **7.5** |
| BiomedSQL | PHARM | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ◐ | **1.5** | ✔ | ✘ | ✘ | 2 | 2 | 4 | **9** |
| MedHELM | CLIN, EHR, HPOL | ? | ✘ | ◐ | ✘ | ✘ | ✔ | ✘ | **1.5** | ✘ | ✔ | ◐ | 2 | 2 | 1 | **6.5** |
| MiraMind | PSY | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| RubricsTree | PH, CLIN | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✔ | ✘ | 1 | 2 | 3 | **7** |
| OntoLearner | KR | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | ? | 1 | **4** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
Repository note: two rows sit outside the agent setting the other columns assume. RealPDEBench evaluates scientific ML surrogate models rather than agents, so its task-setup marks describe an offline training-and-evaluation protocol. SciVQR is static multimodal question answering with no agent, tool use, or environment interaction.

Repository note: two columns carry nearly all the unknowns. `Net` is `?` on 35 of the 47 rows, which is why it leads the coverage group — almost no work here demonstrably grants live retrieval, and most do not say; the full text of eleven of those thirty-five was read for this column and not one states it either way. `Scale` is `?` on 12 rows, every one a multi-domain suite that reports a total task count but no per-domain breakdown. Both columns record that silence rather than resolving it by inference, and in both cases the silence costs the work real score. Two further cells remain `?`: SciCode and Terminal-Bench Science on `Real`.

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [MiraMind](../works/miramind.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [MedHELM](../works/medhelm.md)
- [SciAgentArena](../works/sciagentarena.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MetaSyn](../works/metasyn.md)
- [CORE-Bench](../works/core-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [SMDD-Bench](../works/smdd-bench.md)
- [MedBrowseComp](../works/medbrowsecomp.md)
- [AgentClinic](../works/agentclinic.md)
- [MedAgentBench](../works/medagentbench.md)
- [SDBench](../works/sdbench.md)
- [Imaging-101](../works/imaging-101.md)
- [MolClaw](../works/molclaw.md)
- [RubricsTree](../works/rubricstree.md)
- [BiomedSQL](../works/biomedsql.md)
- [OntoLearner](../works/ontolearner.md)
- [Apodex Discovery](../works/apodex-discovery.md)
- [Agents Catching Agents](../works/agents-catching-agents.md)
