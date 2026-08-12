# Simulation & Scientific Computing

> **English** | [简体中文](../zh/activities/simulation_scientific_computing.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on computationally solving scientific systems — constructing, configuring, executing, debugging, or reasoning through numerical simulations and scientific-computing tasks.

## Scope

Includes PDE and finite-element solving, molecular dynamics, Monte Carlo, DFT, multiphysics simulators, and simulator or digital-twin construction. It is **not** assigned merely because a benchmark internally uses a simulator; the evaluated agent must substantially construct, configure, execute, debug, or reason through the simulation.

## Task Patterns

A large cluster frames scientific computing as **PDE-solver code generation**, where the solver — not the solution field — is the graded artifact. [CodePDE](../works/codepde.md) established the evaluation axes for LLM-generated numerical solvers; [PDEAgent-Bench](../works/pdeagent-bench.md) scales this to 645 instances across three FEM libraries (DOLFINx, Firedrake, deal.II) with a staged executability-accuracy-efficiency ladder; and [CFDLLMBench](../works/cfdllmbench.md) adds a three-tier CFD suite pairing PDE-solving Python code with graduate knowledge and OpenFOAM operation. [FEM-Bench](../works/fem-bench.md) grounds finite-element code generation at course-level granularity, while [MooseBench](../works/moosebench.md) exposes the comprehension-generation gap by deterministically reconstructing the PDE encoded in MOOSE input files to catch simulations that run but solve the wrong physics.

Another cluster drives **real domain simulators end to end**, treating professional software as the evaluation surface. [FEABench](../works/feabench.md) operates COMSOL Multiphysics through its API; [SimBench](../works/simbench.md) builds Chrono digital twins over multi-turn dialogue; [VASPBench](../works/vaspbench.md) plans, runs, and repairs VASP DFT calculations in a closed loop; [StructureClaw](../works/structureclaw.md) drives OpenSees-backed structural-analysis workbenches; and [PowerAgentBench-SS](../works/poweragentbench-ss.md) has agents call power-grid simulators for N-2 contingency screening. [HydroAgent](../works/hydroagent.md) iteratively calibrates the operational CREST hydrologic model, and [SimulCost](../works/simulcost.md) benchmarks cost-aware parameter tuning across 13 physics simulators.

A third cluster is **chemical-process flowsheeting**, where the graded artifact is a process simulation that actually converges. [Simona](../works/simona.md) scores conversion of written process descriptions into flowsheets by Simulation Convergence Rate; [CRAFTS](../works/crafts.md) constructs executable IDAES/Pyomo models behind deterministic promotion gates covering degrees-of-freedom closure, initialization, and solver termination; and the Parameter dimension of [CeProBench](../works/ceprobench.md) executes candidate operating parameters in Aspen Plus so thermodynamic feasibility, not text similarity, decides the score.

A fourth cluster targets **reproducing published research end to end** via specialized simulation toolchains: [AutoMat](../works/automat.md) reproduces computational-materials-science claims (DFT, MD, dislocation dynamics); [Collider-Bench](../works/collider-bench.md) recasts LHC searches through the public MadGraph/Pythia/Delphes stack; [QMP-Bench](../works/qmp-bench.md) covers end-to-end quantum many-body simulations; and [MDArena](../works/mdarena.md) packages authentic molecular-dynamics workflows into containerized tasks. [Terminal-Bench Science](../works/terminal-bench-science.md) generalizes containerized scientific-computing workflows across five natural-science domains.

A fifth cluster runs **structural analysis against a civil-engineering solver**, where a natural-language description of a structure must become a solver model whose computed response is then checked. The lineage escalates in structural complexity: [the reliability-and-robustness agent study](../works/a-large-language-model-empowered-agent-for-reliabl.md) on statically determinate beams, [a lightweight five-agent system](../works/a-lightweight-large-language-model-based-multi-age.md) on multi-bay 2D frames, and [an agentic pipeline for 3D frame systems](../works/agentic-large-language-models-for-automated-struct.md) that requires every monitored response to fall within 1% of a hand-built SAP2000 reference. [Integrating LLMs for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md) and [the MCP-mediated static-analysis dataset](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) reach the same OpenSeesPy target through a prompting framework and a tool server respectively, [AutoBM](../works/autobm.md) validates generated building models by their fundamental period, and [MASSE](../works/masse.md) embeds the model-and-solve step inside a full consulting workflow. Two works move the simulated object off the building frame: [Automating Structural Reliability Analysis](../works/automating-structural-reliability-analysis-with-a.md) runs FORM, Monte Carlo and subset simulation for component reliability, and [LLM-EPANET](../works/llm-epanet.md) executes hydraulic and water-quality simulations of water distribution networks.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| SimBench | 2024 | Multi-turn digital-twin generation for Chrono multi-physics simulator | 102 tasks / 34 systems, 33+ LLMs, 3000+ dialogues | LLM-judge scores under predefined rules with human-in-loop | [card](../works/simbench.md) |
| Building Static Analysis with LLMs and MCP | 2025 | Configuring and running OpenSeesPy through a Model Context Protocol server | 4 reinforced-concrete frames, 16 analyses, GPT-only vs GPT+MCP control | Relative error vs ETABS reference (GPT+MCP below 1.427%) | [card](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md) |
| CFDLLMBench | 2025 | Three-tier CFD: knowledge, PDE Python solvers, OpenFOAM cases | 240 tasks (90 MCQ, 24 code, 126 OpenFOAM cases) | Executability, relative error, numerical convergence | [card](../works/cfdllmbench.md) |
| CodePDE | 2025 | LLM-generated PDE numerical solvers with iterative refinement | Representative PDE problems (counts TODO) | Solver accuracy on representative PDE problems | [card](../works/codepde.md) |
| FEABench | 2025 | Driving COMSOL Multiphysics via API to solve FEA problems | NL multiphysics problems, agentic API loop (counts TODO) | Correct answer; 88% executable API-call rate | [card](../works/feabench.md) |
| FEM-Bench | 2025 | FEM/computational-mechanics function-writing plus unit-test writing | 33 function tasks + test track, 5 attempts each | Objective verification; joint success rate | [card](../works/fem-bench.md) |
| Integrating LLMs for Automated Structural Analysis | 2025 | Driving OpenSeesPy and OpsVis from structural word problems | 20 hand-curated 2D-frame problems; best-of-3 and 5-run stability protocols | Correct deformations and internal forces (GPT-4o 100% best-of-3) | [card](../works/integrating-large-language-models-for-automated-st.md) |
| Lightweight Multi-Agent System for 2D Frame Analysis | 2025 | Building OpenSeesPy finite-element models of multi-bay 2D frames | 20 frame problems, five specialized agents, 10 trials each | Proportion of correctly generated models (over 80% on most problems) | [card](../works/a-lightweight-large-language-model-based-multi-age.md) |
| LLM-EPANET | 2025 | Generating and executing EPANET water-distribution simulations | 69 queries over 3 networks, 5 complexity tiers, sandboxed self-debug loop | Value equivalence to hand-written reference scripts (56-81%) | [card](../works/llm-epanet.md) |
| MASSE | 2025 | Building and solving OpenSeesPy models inside a structural consulting workflow | 100 racking-system problems, 4 rubric-scored benchmarks, 10 trials each | GPT-5 judge rubric scores per agent role (SAAB 96.6 best) | [card](../works/masse.md) |
| Agentic LLMs for 3D Frame Structural Analysis | 2026 | Producing executable SAP2000 models of irregular 3D frame systems | 10 irregular 3D frames (voids, setbacks, L/U/cross plans), 10 trials each | All monitored responses within 1% of a hand-built SAP2000 model (90% avg) | [card](../works/agentic-large-language-models-for-automated-struct.md) |
| AutoBM / BMEval | 2026 | Generating executable OpenSeesPy building models validated by modal analysis | 128 expert-validated tasks, sandboxed execution, 16 models | Pass@k_strict: clean execution, period within tolerance, compliance verdict | [card](../works/autobm.md) |
| AutoDFT / VASPBench | 2026 | Autonomous VASP DFT calculations, plan-run-repair closed loop | 34 tasks across 9 DFT calculation types | 94.1% task success; reliable property predictions | [card](../works/vaspbench.md) |
| AutoMat | 2026 | Reproducing computational-materials claims end to end on HPC | 85 SME-curated claims, three reproduction types | Evidence supporting/undermining claim; 54.1% success | [card](../works/automat.md) |
| Automating Structural Reliability Analysis | 2026 | Generating and running FORM, Monte Carlo and subset-simulation solvers | 20 held-out reliability problems, deterministic non-LLM runner | Reliability index within 0.1 of validated-solver reference on all 20 | [card](../works/automating-structural-reliability-analysis-with-a.md) |
| CeProBench | 2026 | Closed-loop refinement of operating parameters executed in Aspen Plus | 20 high-fidelity Aspen Plus files, 91 adjustable parameters, 65 objectives | Aspen-validated feasibility; yield/purity/cost and convergence iterations | [card](../works/ceprobench.md) |
| Collider-Bench | 2026 | Recasting LHC SUSY searches via public simulation stack | 10 simulation tasks from four CMS searches | Histogram fidelity vs hidden yields; LLM provenance judge | [card](../works/collider-bench.md) |
| CRAFTS | 2026 | Building executable IDAES/Pyomo process-simulation models from requests and PFDs | OpenIDAES-450, 82 frozen held-out cases, deterministic IDAES/Pyomo gates | Workflow Success 91.5% plus unit/stream/connection macro-F1 | [card](../works/crafts.md) |
| HydroAgent | 2026 | Calibrating operational CREST hydrologic model, re-simulate loop | 4 held-out gauges (329-40,792 km2), best-of-20 rounds | Nash-Sutcliffe Efficiency vs human-expert reference | [card](../works/hydroagent.md) |
| LLM-Empowered Agent for Structural Analysis | 2026 | Generating and auto-executing OpenSeesPy beam models with OpsVis rendering | 8 beam problems plus 3 extended tasks, 500 runs each | Reliability above 0.990 and robustness above 0.996 | [card](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| MDArena | 2026 | Realistic molecular-dynamics research workflows | 50 containerized tasks, 29 systems, 14 protocols | Strict success rate plus process-level partial credit | [card](../works/mdarena.md) |
| MooseBench | 2026 | MOOSE multiphysics input-file generation with PDE ground truth | 220 cases, each with intended PDE contract | Intent Fidelity Score via deterministic PDE reconstruction | [card](../works/moosebench.md) |
| PDEAgent-Bench | 2026 | PDE solver-code generation for three FEM libraries | 645 instances, 6 categories, 11 families (DOLFINx/Firedrake/deal.II) | Staged executability, accuracy, efficiency checks | [card](../works/pdeagent-bench.md) |
| PowerAgentBench-SS | 2026 | Agentic steady-state grid studies with simulator calls | IEEE 39-bus variants, DC thermal N-2 contingency search | Hidden evaluator recomputes validity; multi-metric scoring | [card](../works/poweragentbench-ss.md) |
| QMP-Bench | 2026 | End-to-end quantum many-body simulation reproduction | 100 research tasks from 21 high-impact journals | Coding correctness plus physical validity | [card](../works/qmp-bench.md) |
| Simona | 2026 | Turning written process descriptions into converging simulation flowsheets | 1,000 expert-written descriptions; simulator driven over HTTP APIs | Simulation Convergence Rate (80.3%) and design time | [card](../works/simona.md) |
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
- [CeProBench](../works/ceprobench.md)
- [CRAFTS](../works/crafts.md)
- [Simona](../works/simona.md)
- [Toward Responsible AI in High-Stakes Domains: A Dataset for Building Static Analysis with LLMs in Structural Engineering](../works/toward-responsible-ai-in-high-stakes-domains-a-dat.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [MASSE](../works/masse.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [AutoBM / BMEval](../works/autobm.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
