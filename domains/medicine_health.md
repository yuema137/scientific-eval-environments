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

## Related Works

- [MedHELM](../works/medhelm.md)
- [SciAgentArena](../works/sciagentarena.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [MetaSyn](../works/metasyn.md)
