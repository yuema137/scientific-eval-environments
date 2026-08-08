# Mechanical & Aerospace Engineering

> **English** | [简体中文](../zh/domains/mechanical_aerospace_engineering.md) · [← All domains](./README.md)

## Scope

Mechanical and aerospace engineering. Computational fluid dynamics and thermal transport fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| CFDLLMBench | 2025 | Computational fluid dynamics at three depths: graduate-level knowledge (CFDQuery), numerical solution of stated PDEs in Python (CFDCodeBench), and end-to-end OpenFOAM case configuration and execution (FoamBench). | 240 tasks: 90 expert-curated multiple-choice questions, 24 PDE-solver coding problems, and 126 OpenFOAM cases (110 tutorial-derived + 16 expert-crafted to be unlike any tutorial). | Execution plus banded normalized error (NMSE) against reference solutions and an explicit convergence check under mesh and time-step refinement; any valid numerical method is accepted. | [→](../works/cfdllmbench.md) |
| Terminal-Bench Science | 2026 | Mechanical Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |

## Related Works

- [CFDLLMBench](../works/cfdllmbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
