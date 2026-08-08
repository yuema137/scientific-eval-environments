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

## Related Works

- [AFMBench](../works/afmbench.md)
- [AutoMat](../works/automat.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
