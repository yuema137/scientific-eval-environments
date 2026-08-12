# Mechanical & Aerospace Engineering

> **English** | [简体中文](../zh/domains/mechanical_aerospace_engineering.md) · [← All domains](./README.md)

## Scope

Mechanical and aerospace engineering. Computational fluid dynamics and thermal transport fold here.

## Comparison

| Work | Year | Scientific problem | Task form & scale | Domain verification | Card |
|---|---|---|---|---|---|
| CFDLLMBench | 2025 | Computational fluid dynamics at three depths: graduate-level knowledge (CFDQuery), numerical solution of stated PDEs in Python (CFDCodeBench), and end-to-end OpenFOAM case configuration and execution (FoamBench). | 240 tasks: 90 expert-curated multiple-choice questions, 24 PDE-solver coding problems, and 126 OpenFOAM cases (110 tutorial-derived + 16 expert-crafted to be unlike any tutorial). | Execution plus banded normalized error (NMSE) against reference solutions and an explicit convergence check under mesh and time-step refinement; any valid numerical method is accepted. | [→](../works/cfdllmbench.md) |
| Terminal-Bench Science | 2026 | Mechanical Engineering tasks within the Engineering Sciences track of a five-track suite of terminal-based scientific workflows. | Containerized terminal tasks (8 at launch across all five tracks, target 100+), community-contributed under a three-approval validation gate. | Deterministic pytest-based verification in containerized execution environments. | [→](../works/terminal-bench-science.md) |
| SimBench | 2024 | Generate digital twins for multibody dynamics, FEA, vehicle dynamics, robotic dynamics, and sensor simulation in the Chrono simulator. | 102 demonstration tasks over 34 physical systems (official repository), built through multi-turn dialogue; 33+ LLMs compared. | LLM-judge scoring with predefined rules and human-in-the-loop guidance. | [→](../works/simbench.md) |
| FEM-Bench | 2025 | Write finite-element functions and unit tests for computational-mechanics problems — forces, deformation, constraints. | 33 graduate-course-aligned tasks over two tracks, five attempts per model-task pair. | Objective verification; Average Joint Success Rate for test writing. | [→](../works/fem-bench.md) |
| RealPDEBench | 2026 | Predict fluid and thermal engineering systems — fluid–structure interaction, cylinder and foil flows, and combustion — from real-world measurements paired with numerical simulations. | Five real-world measured datasets with paired simulations and three sim-vs-real tasks; evaluates scientific ML surrogate models rather than LLM agents. | Eight data-oriented and physics-oriented metrics over ten baselines. | [→](../works/realpdebench.md) |
| FEABench | 2025 | Solve multiphysics engineering problems end to end with finite element analysis by operating COMSOL Multiphysics through its API. | Natural-language problem descriptions; the agentic setting iterates API calls against software feedback. | Evaluation over generated API calls and computed answers; executability of API calls as a headline metric. | [→](../works/feabench.md) |
| MooseBench | 2026 | Generate multiphysics finite-element simulation code (MOOSE) that solves the intended physics, not merely code that runs. | 220 cases with PDE-level mathematical ground truth. | Intent Fidelity Score via deterministic PDE reconstruction; 39–40% of cases stay runnable-but-wrong under execution-only repair. | [→](../works/moosebench.md) |
| SciConvBench | 2026 | Clarify ill-posed simulation requests; fluid mechanics and solid mechanics are two of its four computational-science domains. | Multi-turn disambiguation and inconsistency-resolution dialogues over a structured task ontology. | Rubric scoring of clarification behavior, conversational grounding, and final-specification fidelity. | [→](../works/sciconvbench.md) |
| AInsteinBench | 2025 | Resolve maintainer-PR tasks in production scientific repositories; fluid dynamics is among its six codebases. | Repository-level coding-agent tasks in executable environments. | Test-driven verification with expert-reviewed curation. | [→](../works/ainsteinbench.md) |
| ERI Benchmark | 2026 | Mechanical and aerospace engineering, two of the benchmark's nine covered fields, spanning thermodynamics, fluid mechanics, heat transfer, machine design, dynamics and vibrations, manufacturing and HVAC, plus aerodynamics, flight mechanics, propulsion, aerospace structures, and orbital mechanics. | 57,750 instruction–response records generated over a controlled field × subdomain × intent × difficulty cross-product (1,155 cells, 50 pairs per cell), with per-field means reported separately. | Automatic checks for refusals, missing final answers, and machine-parsable constraint violations, beneath rubric scoring by a three-provider judge panel (Claude Haiku 4.5, GPT-4.1 Mini, Mistral Small 3) averaged per item; aerospace engineering is among the hardest fields for every model scored. | [→](../works/eri-benchmark.md) |

## Related Works

- [CFDLLMBench](../works/cfdllmbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [SimBench](../works/simbench.md)
- [FEM-Bench](../works/fem-bench.md)
- [RealPDEBench](../works/realpdebench.md)
- [FEABench](../works/feabench.md)
- [MooseBench](../works/moosebench.md)
- [SciConvBench](../works/sciconvbench.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [ERI Benchmark](../works/eri-benchmark.md)
