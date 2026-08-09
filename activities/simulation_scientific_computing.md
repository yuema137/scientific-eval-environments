# Simulation & Scientific Computing

> **English** | [简体中文](../zh/activities/simulation_scientific_computing.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on computationally solving scientific systems — constructing, configuring, executing, debugging, or reasoning through numerical simulations and scientific-computing tasks.

## Scope

Includes PDE and finite-element solving, molecular dynamics, Monte Carlo, DFT, multiphysics simulators, and simulator or digital-twin construction. It is **not** assigned merely because a benchmark internally uses a simulator; the evaluated agent must substantially construct, configure, execute, debug, or reason through the simulation.

## Task Patterns

A large cluster frames scientific computing as **PDE-solver code generation**, where the solver — not the solution field — is the graded artifact. [CodePDE](../works/codepde.md) established the evaluation axes for LLM-generated numerical solvers; [PDEAgent-Bench](../works/pdeagent-bench.md) scales this to 645 instances across three FEM libraries (DOLFINx, Firedrake, deal.II) with a staged executability-accuracy-efficiency ladder; and [CFDLLMBench](../works/cfdllmbench.md) adds a three-tier CFD suite pairing PDE-solving Python code with graduate knowledge and OpenFOAM operation. [FEM-Bench](../works/fem-bench.md) grounds finite-element code generation at course-level granularity, while [MooseBench](../works/moosebench.md) exposes the comprehension-generation gap by deterministically reconstructing the PDE encoded in MOOSE input files to catch simulations that run but solve the wrong physics.

Another cluster drives **real domain simulators end to end**, treating professional software as the evaluation surface. [FEABench](../works/feabench.md) operates COMSOL Multiphysics through its API; [SimBench](../works/simbench.md) builds Chrono digital twins over multi-turn dialogue; [VASPBench](../works/vaspbench.md) plans, runs, and repairs VASP DFT calculations in a closed loop; [StructureClaw](../works/structureclaw.md) drives OpenSees-backed structural-analysis workbenches; and [PowerAgentBench-SS](../works/poweragentbench-ss.md) has agents call power-grid simulators for N-2 contingency screening. [HydroAgent](../works/hydroagent.md) iteratively calibrates the operational CREST hydrologic model, and [SimulCost](../works/simulcost.md) benchmarks cost-aware parameter tuning across 13 physics simulators.

A third cluster targets **reproducing published research end to end** via specialized simulation toolchains: [AutoMat](../works/automat.md) reproduces computational-materials-science claims (DFT, MD, dislocation dynamics); [Collider-Bench](../works/collider-bench.md) recasts LHC searches through the public MadGraph/Pythia/Delphes stack; [QMP-Bench](../works/qmp-bench.md) covers end-to-end quantum many-body simulations; and [MDArena](../works/mdarena.md) packages authentic molecular-dynamics workflows into containerized tasks. [Terminal-Bench Science](../works/terminal-bench-science.md) generalizes containerized scientific-computing workflows across five natural-science domains.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| SimBench | 2024 | Multi-turn digital-twin generation for Chrono multi-physics simulator | 102 tasks / 34 systems, 33+ LLMs, 3000+ dialogues | LLM-judge scores under predefined rules with human-in-loop | [card](../works/simbench.md) |
| CFDLLMBench | 2025 | Three-tier CFD: knowledge, PDE Python solvers, OpenFOAM cases | 240 tasks (90 MCQ, 24 code, 126 OpenFOAM cases) | Executability, relative error, numerical convergence | [card](../works/cfdllmbench.md) |
| CodePDE | 2025 | LLM-generated PDE numerical solvers with iterative refinement | Representative PDE problems (counts TODO) | Solver accuracy on representative PDE problems | [card](../works/codepde.md) |
| FEABench | 2025 | Driving COMSOL Multiphysics via API to solve FEA problems | NL multiphysics problems, agentic API loop (counts TODO) | Correct answer; 88% executable API-call rate | [card](../works/feabench.md) |
| FEM-Bench | 2025 | FEM/computational-mechanics function-writing plus unit-test writing | 33 function tasks + test track, 5 attempts each | Objective verification; joint success rate | [card](../works/fem-bench.md) |
| AutoDFT / VASPBench | 2026 | Autonomous VASP DFT calculations, plan-run-repair closed loop | 34 tasks across 9 DFT calculation types | 94.1% task success; reliable property predictions | [card](../works/vaspbench.md) |
| AutoMat | 2026 | Reproducing computational-materials claims end to end on HPC | 85 SME-curated claims, three reproduction types | Evidence supporting/undermining claim; 54.1% success | [card](../works/automat.md) |
| Collider-Bench | 2026 | Recasting LHC SUSY searches via public simulation stack | 10 simulation tasks from four CMS searches | Histogram fidelity vs hidden yields; LLM provenance judge | [card](../works/collider-bench.md) |
| HydroAgent | 2026 | Calibrating operational CREST hydrologic model, re-simulate loop | 4 held-out gauges (329-40,792 km2), best-of-20 rounds | Nash-Sutcliffe Efficiency vs human-expert reference | [card](../works/hydroagent.md) |
| MDArena | 2026 | Realistic molecular-dynamics research workflows | 50 containerized tasks, 29 systems, 14 protocols | Strict success rate plus process-level partial credit | [card](../works/mdarena.md) |
| MooseBench | 2026 | MOOSE multiphysics input-file generation with PDE ground truth | 220 cases, each with intended PDE contract | Intent Fidelity Score via deterministic PDE reconstruction | [card](../works/moosebench.md) |
| PDEAgent-Bench | 2026 | PDE solver-code generation for three FEM libraries | 645 instances, 6 categories, 11 families (DOLFINx/Firedrake/deal.II) | Staged executability, accuracy, efficiency checks | [card](../works/pdeagent-bench.md) |
| PowerAgentBench-SS | 2026 | Agentic steady-state grid studies with simulator calls | IEEE 39-bus variants, DC thermal N-2 contingency search | Hidden evaluator recomputes validity; multi-metric scoring | [card](../works/poweragentbench-ss.md) |
| QMP-Bench | 2026 | End-to-end quantum many-body simulation reproduction | 100 research tasks from 21 high-impact journals | Coding correctness plus physical validity | [card](../works/qmp-bench.md) |
| SimulCost | 2026 | Cost-aware physics-simulation parameter tuning | 2,947 single-round + 1,931 multi-round tasks, 13 simulators | Performance under simulation-time/resource budget constraints | [card](../works/simulcost.md) |
| StructureClaw | 2026 | Operating structural-engineering workbench with solver backends | 150 scenarios: standard, interactive, multimodal reconstruction | Model matching + numerical agreement vs frozen references | [card](../works/structureclaw.md) |
| Terminal-Bench Science | 2026 | Containerized natural-science computational workflows | 8 tasks across 5 domains (target 100+) | Deterministic pytest-based programmatic verification | [card](../works/terminal-bench-science.md) |

## Related Works

- [SimBench](../works/simbench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [CodePDE](../works/codepde.md)
- [FEABench](../works/feabench.md)
- [FEM-Bench](../works/fem-bench.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [AutoMat](../works/automat.md)
- [Collider-Bench](../works/collider-bench.md)
- [HydroAgent](../works/hydroagent.md)
- [MDArena](../works/mdarena.md)
- [MooseBench](../works/moosebench.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [PowerAgentBench-SS](../works/poweragentbench-ss.md)
- [QMP-Bench](../works/qmp-bench.md)
- [SimulCost](../works/simulcost.md)
- [StructureClaw](../works/structureclaw.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
