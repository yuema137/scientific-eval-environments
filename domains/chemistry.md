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

## Related Works

- [ScienceAgentBench](../works/scienceagentbench.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
