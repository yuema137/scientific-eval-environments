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

## Related Works

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
