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

## Related Works

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
