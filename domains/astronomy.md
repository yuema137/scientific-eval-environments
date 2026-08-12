# Astronomy

> **English** | [简体中文](../zh/domains/astronomy.md) · [← All domains](./README.md)

## Scope

Astronomy and astrophysics, including inference from observational data.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| Stargazer | 2026 | Infer exoplanet systems from radial-velocity time series: propose the number of planets and orbital parameters that explain the observed stellar signal, iterating on per-criterion feedback. | 120 model-fitting tasks — 100 synthetic across three difficulty tiers plus 20 real archival systems from the NASA Exoplanet Archive and VizieR, spanning one to seven planets. | Four simultaneous physical criteria: residual RMS ≤ 1.5× measurement uncertainty, positive ΔBIC vs. a constant null model, Hungarian-matched planet recovery ≥ 0.8, and exact planet count. | [→](../works/stargazer.md) |
| Terminal-Bench Science | 2026 | Astronomy tasks within the Physical Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | Re-discover the findings of a hidden published paper from a task description, related literature, and raw data — Astronomy is one of its ten domains (40 tasks total). | End-to-end autonomous research tasks, each grounded in a real publication kept hidden during evaluation; the agent produces a final research report. | Reference-Anchored Discovery Score (0–100; 50 = reference-level evidence) against expert-curated multimodal rubrics anchored to the hidden paper's artifacts, judged by GPT-5.1. | [→](../works/researchclawbench.md) |
| gwBenchmarks | 2026 | Model gravitational-wave sources at the precision the science requires: waveform surrogates from numerical relativity, black-hole orbital dynamics, merger remnants, template banks. | 8 tasks over data representing more than 10⁸ core-hours of compute; 12 coding agents evaluated. | External pre-defined evaluation framework with per-task physics metrics against a ≲10⁻⁴ relative-error domain requirement. | [→](../works/gwbenchmarks.md) |
| ReplicationBench | 2025 | Replicate the core contributions of astrophysics research papers: experimental setup, derivations, data analysis, and codebase. | 111 replication tasks spanning 20 papers (official repository), co-developed with the original authors and run in computational sandboxes. | Objective per-task scoring of faithfulness to the original methods and correctness of the results. | [→](../works/replicationbench.md) |
| SciVisAgentBench | 2026 | Scientific visualization and data analysis of astronomy data — one of its seven application domains — translating natural-language intent into executable visualization operations over scalar/vector/tensor and time-varying fields. | 108 expert-crafted SciVis cases across seven science domains and 15 visualization-operation categories, run over platforms such as ParaView and napari via CLIs, MCP servers, and Python APIs. | Multimodal outcome-centric pipeline combining an MLLM judge (reported Claude-Opus-4.6; Pearson 0.808 with human ratings) with deterministic evaluators — image metrics (PSNR, SSIM, LPIPS), code checkers, and rule-based/case-specific verifiers. | [→](../works/scivisagentbench.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [Stargazer](../works/stargazer.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [ReplicationBench](../works/replicationbench.md)
