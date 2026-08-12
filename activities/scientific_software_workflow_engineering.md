# Scientific Software & Workflow Engineering

> **English** | [简体中文](../zh/activities/scientific_software_workflow_engineering.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on producing, repairing, integrating, or executing scientific and engineering software or workflows as a substantive capability — scientific code generation, numerical-algorithm implementation, repository engineering, pipeline construction, and hardware-description or formal-specification code.

## Scope

Covers scientific **and** engineering software or workflow artifacts — including HDL/RTL, formal models, numerical solvers, and scientific pipelines — where software correctness is central to the evaluation. It excludes general-purpose application or web software engineering, and incidental helper-scripting done in service of another activity.

## Task Patterns

**HDL/RTL generation and hardware verification.** A cluster of works targets hardware-description and formal-hardware code. [RTLLM](../works/rtllm.md) and [VerilogEval](../works/verilogeval.md) generate design/RTL Verilog from natural language graded by simulation; [RTL-Repo](../works/rtl-repo.md) extends this to repository-scale cross-file Verilog completion, [VHDL-Eval](../works/vhdl-eval.md) to VHDL, and [HLS-Eval](../works/hls-eval.md) to high-level synthesis. [CVDP](../works/cvdp.md) consolidates RTL generation, debugging, and verification across 783 problems. Verification-focused works produce assertions and testbenches: [AssertionBench](../works/assertionbench.md) generates SystemVerilog assertions against formally verified ground truth, and [FVEval](../works/fveval.md) decomposes formal verification into NL2SVA and Design2SVA sub-tasks checked by Cadence Jasper.

**PDE/numerical-solver and simulation-code generation.** Many works ask the agent to write numerical code or simulation input decks. [CodePDE](../works/codepde.md), [PDEAgent-Bench](../works/pdeagent-bench.md), and [PDE-Controller](../works/pde-controller.md) target PDE solvers; [FEM-Bench](../works/fem-bench.md) and [FEABench](../works/feabench.md) cover finite-element code; [CFDLLMBench](../works/cfdllmbench.md) spans CFD knowledge, Python solvers, and OpenFOAM cases; [MooseBench](../works/moosebench.md) reconstructs the PDE encoded in MOOSE input files; and [SimBench](../works/simbench.md) builds Chrono digital twins. [CRAFTS](../works/crafts.md) extends this to chemical-process flowsheeting, emitting typed intermediate representations that must clear deterministic IDAES/Pyomo gates before an executable model is constructed. Domain-simulation workflow execution appears in [VASPBench](../works/vaspbench.md), [MDArena](../works/mdarena.md), and [Collider-Bench](../works/collider-bench.md).

**Scientific-repository engineering and research reproduction.** These works have agents operate on real codebases and papers. [AInsteinBench](../works/ainsteinbench.md) ports the SWE-bench maintainer-PR paradigm to six production scientific repos; [SUPER](../works/super.md) and [ML-Bench](../works/ml-bench.md) test setting up and executing real research repositories. Paper-reproduction works include [PaperBench](../works/paperbench.md), [EXP-Bench](../works/exp-bench.md), [PRBench](../works/prbench.md), [QMP-Bench](../works/qmp-bench.md), [NatureBench](../works/naturebench.md), and [gwBenchmarks](../works/gwbenchmarks.md).

**ML-research code implementation and ML engineering.** A large group frames ML research/engineering itself as the coded artifact. [MLAgentBench](../works/mlagentbench.md), [MLE-bench](../works/mle-bench.md), [MLE-Dojo](../works/mle-dojo.md), [MLRC-Bench](../works/mlrc-bench.md), [RE-Bench](../works/re-bench.md), and [DevAI](../works/devai.md) task agents with training models, optimizing code, or proposing novel methods against baselines and leaderboards. [ResearchCodeBench](../works/researchcodebench.md) implements novel contributions from recent papers, and [SciCode](../works/scicode.md) covers scientist-curated research coding across natural-science subfields.

**Bioinformatics/data-science pipelines and cross-domain workflows.** Pipeline-construction and data-science coding works include [GenoTEX](../works/genotex.md), [BioAgent Bench](../works/bioagent-bench.md), [MedAgentGym](../works/medagentgym.md), [BioXArena](../works/bioxarena.md), [DA-Code](../works/da-code.md), [ScienceAgentBench](../works/scienceagentbench.md), and [MatTools](../works/mattools.md) (pymatgen). Formal-specification code is represented by [SysMoBench](../works/sysmobench.md) (TLA+ models). Broader containerized scientific-computing harnesses are [Terminal-Bench Science](../works/terminal-bench-science.md) and the structural-engineering workbench [StructureClaw](../works/structureclaw.md).

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| ML-Bench | 2023 | Repository-level ML code from task descriptions | 9,641 tasks over 18 GitHub repos; text-to-code + Linux-sandbox agent | Pass@5 / autonomous execution success rate | [card](../works/ml-bench.md) |
| MLAgentBench | 2023 | ML experimentation code improving a metric | 13 tasks; ReAct agent reads/writes files, runs experiments | Measured improvement over starter-code baseline | [card](../works/mlagentbench.md) |
| RTLLM | 2023 | Design RTL (Verilog) from natural language | 29 hand-crafted designs (v2.0: 50); static generation | Syntax, functionality, and design-quality pass | [card](../works/rtllm.md) |
| VerilogEval | 2023 | Verilog RTL from problem/spec descriptions | 156 HDLBits problems; static generation | Simulation-checked functional correctness (pass@k) | [card](../works/verilogeval.md) |
| AssertionBench | 2024 | SystemVerilog assertions for hardware designs | 100 OpenCores Verilog designs; static generation | Fraction of functionally correct assertions | [card](../works/assertionbench.md) |
| DA-Code | 2024 | Data-science wrangling/analytics code | Agentic tasks in Docker sandbox | Execution-grounded accuracy (best 30.5%) | [card](../works/da-code.md) |
| DevAI / Agent-as-a-Judge | 2024 | AI/ML development projects from requirements | 55 tasks, 365 hierarchical requirements; agentic | Step-wise requirement satisfaction (Agent-as-a-Judge) | [card](../works/devai.md) |
| FVEval | 2024 | SystemVerilog assertions/testbenches for verification | Three sub-tasks (NL2SVA-Machine/Human, Design2SVA) | Formal-tool (Cadence Jasper) validation | [card](../works/fveval.md) |
| GenoTEX | 2024 | Gene-expression analysis pipeline code | 1,384 gene-trait problems over 911 datasets; agentic | Match to expert-curated reference pipelines/results | [card](../works/genotex.md) |
| MLE-bench | 2024 | End-to-end ML engineering solutions | 75 Kaggle competitions; agent in scaffold | Kaggle medal thresholds vs leaderboard | [card](../works/mle-bench.md) |
| RE-Bench | 2024 | ML research-engineering code/kernels | 7 open-ended environments; agents vs 61 experts | Score vs reference under 2/8/32h budgets | [card](../works/re-bench.md) |
| RTL-Repo | 2024 | Repository-scale Verilog completion | 4,000+ samples with full-repo context; static | Edit similarity / exact match | [card](../works/rtl-repo.md) |
| SciCode | 2024 | Scientist-curated research code | 80 main problems, 338 subproblems, 16 subfields | Pass against gold solutions and test cases | [card](../works/scicode.md) |
| ScienceAgentBench | 2024 | Self-contained scientific-workflow Python programs | 102 tasks from 44 papers, four disciplines | Program/execution-result correctness and cost | [card](../works/scienceagentbench.md) |
| SimBench | 2024 | Chrono multi-physics digital-twin code | 102 tasks over 34 systems; multi-turn | LLM-judge score under rules + human guidance | [card](../works/simbench.md) |
| SUPER | 2024 | Setting up and executing research repos | 45 end-to-end + 152 sub + 602 auto problems; agentic | End-to-end success (best 16.3%) | [card](../works/super.md) |
| VHDL-Eval | 2024 | VHDL code generation | 202 problems with self-verifying testbenches; static | Testbench-verified functional correctness | [card](../works/vhdl-eval.md) |
| AInsteinBench | 2025 | Scientific-repository PR resolution | Maintainer-PR tasks in 6 production sci repos; agentic | Test-driven verification in executable envs | [card](../works/ainsteinbench.md) |
| CFDLLMBench | 2025 | CFD knowledge, Python solvers, OpenFOAM cases | 240 tasks in three tiers (CFDQuery/Code/Foam) | Executability, numerical error, convergence | [card](../works/cfdllmbench.md) |
| CodePDE | 2025 | PDE-solver code generation | Representative PDE problems with iterative refinement | Solver numerical accuracy on PDE problems | [card](../works/codepde.md) |
| CVDP | 2025 | RTL design, debugging, and verification code | 783 problems, 13 categories; agentic + non-agentic | pass@1 (best <=34% on code generation) | [card](../works/cvdp.md) |
| EXP-Bench | 2025 | End-to-end AI research experiment code | 461 tasks from 51 papers, incomplete starter code | Design/implementation/execution correctness (subtasks) | [card](../works/exp-bench.md) |
| FEABench | 2025 | FEA solution by driving COMSOL via API | Multiphysics NL problems; agentic API iteration | Executable API calls / correct computed answer | [card](../works/feabench.md) |
| FEM-Bench | 2025 | FEM functions and unit tests | 33 function-writing tasks + test track; 5 attempts | Objective verification / joint success rate | [card](../works/fem-bench.md) |
| HLS-Eval | 2025 | High-level-synthesis code and optimization edits | 94 designs, two tasks; framework-harnessed | Parse/compile/run/synthesize on Vitis HLS (pass@k) | [card](../works/hls-eval.md) |
| MatTools | 2025 | pymatgen tool comprehension and Python code | 69,225 QA pairs + 49 tasks (138 subtasks); execution | Correct executed materials-property answers | [card](../works/mattools.md) |
| MedAgentGym | 2025 | Biomedical data-science coding | 72,413 instances, 129 categories; sandbox w/ feedback | Verifiable ground-truth success (RL-trainable) | [card](../works/medagentgym.md) |
| MLE-Dojo | 2025 | ML-engineering solutions in interactive gym | 200+ Kaggle challenges; structured feedback loop | Iterative improvement / long-horizon quality | [card](../works/mle-dojo.md) |
| MLRC-Bench | 2025 | Novel ML research methods implemented | 7 competition tasks; scaffolded agent | Fraction of baseline-to-human gap closed (best 9.3%) | [card](../works/mlrc-bench.md) |
| PaperBench | 2025 | Replicate AI papers from scratch | 20 ICML papers, 8,316 rubric subtasks; agentic | Rubric-graded replication score (LLM judge) | [card](../works/paperbench.md) |
| PDE-Controller | 2025 | STL autoformalization + PDE-control programs | Heat/wave systems; human cases + 2M synthetic | Reasoning/autoformalization/synthesis metrics; utility gain | [card](../works/pde-controller.md) |
| ResearchCodeBench | 2025 | Implement novel ML-paper contributions as code | 212 challenges from 20 recent papers; static | Correct executable implementation (best 37.3%) | [card](../works/researchcodebench.md) |
| SysMoBench | 2025 | TLA+ formal system models + TLC config | 11 concurrent/distributed artifacts, 175-5,360 SLOC | Syntax/runtime/conformance/invariant checks (automated) | [card](../works/sysmobench.md) |
| AutoDFT / VASPBench | 2026 | Autonomous DFT (VASP) workflow execution | 34 tasks, 9 calculation types; closed-loop agent | Task-level success + property accuracy (94.1%) | [card](../works/vaspbench.md) |
| BioAgent Bench | 2026 | End-to-end bioinformatics pipelines | Curated RNA-seq/variant-calling/metagenomics; agentic | LLM-graded pipeline progress + outcome validity | [card](../works/bioagent-bench.md) |
| BioXArena | 2026 | Multi-modal biomedical ML models | 76 tasks, 9 domains; 2h single-GPU environment | Hidden-label biology-aware score (0-1) | [card](../works/bioxarena.md) |
| Collider-Bench | 2026 | LHC analysis reproduction (simulation pipeline) | 10 CMS SUSY tasks; containerized public stack | Histogram fidelity vs hidden reference yields | [card](../works/collider-bench.md) |
| CRAFTS | 2026 | Executable IDAES/Pyomo chemical-process simulation models | OpenIDAES-450; 82 frozen held-out cases, typed IRs, deterministic gates | Workflow Success 91.5% + unit/stream/connection macro-F1 | [card](../works/crafts.md) |
| gwBenchmarks | 2026 | Gravitational-wave modeling/surrogate code | 8 high-precision tasks; >10^8 core-hours data | External-framework score at near 1e-4 error | [card](../works/gwbenchmarks.md) |
| MDArena | 2026 | Molecular-dynamics workflow code | 50 containerized tasks, 29 systems, 14 protocols | Strict success rate + process partial credit | [card](../works/mdarena.md) |
| MooseBench | 2026 | MOOSE multiphysics simulation input files | 220 cases with PDE-level ground truth | Intent Fidelity Score (reconstructed PDE match) | [card](../works/moosebench.md) |
| NatureBench | 2026 | Match published SOTA scientific code | 90 tasks from Nature-family papers, six domains | Reach/exceed published SOTA under info firewall | [card](../works/naturebench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | Build a neuroscience data-to-discovery pipeline in code | 9 computational tasks (7 stages + end-to-end); Harbor-compatible | Correct stage code vs expert annotations and legacy codebases | [card](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| PDAgent-Bench | 2026 | Generate EDA-tool scripts for VLSI physical design | 210 script-gen tasks + closed-loop flow; Innovus/ICC2/OpenROAD | Execution-validated scripts (pass@1/5) | [card](../works/pdagent-bench.md) |
| PDEAgent-Bench | 2026 | PDE solver code for FEM libraries | 645 instances, 6 categories; DOLFINx/Firedrake/deal.II | Staged executability, accuracy, efficiency | [card](../works/pdeagent-bench.md) |
| PRBench | 2026 | Reproduce physics research from papers | 30 expert-curated tasks, 11 subfields; sandbox | Quantitative match to publication (CSV rubric) | [card](../works/prbench.md) |
| QMP-Bench | 2026 | Quantum many-body simulation code | 100 end-to-end tasks from 21 journals | Coding correctness + physical validity | [card](../works/qmp-bench.md) |
| SciVisAgentBench | 2026 | Generate executable scientific-visualization code | 108 cases; ParaView/napari/MD/topology via CLI/MCP/Python | Image metrics + code checkers + rule-based verifiers | [card](../works/scivisagentbench.md) |
| StructureClaw | 2026 | Structural-engineering workflow (model to solver to checks) | 150 scenarios; artifact workbench w/ OpenSees | Model-match + numerical agreement vs frozen refs | [card](../works/structureclaw.md) |
| Terminal-Bench Science | 2026 | Containerized scientific-computing workflows | 8 tasks across 5 domains (target 100+); agentic | pytest deterministic programmatic verification | [card](../works/terminal-bench-science.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [PDAgent-Bench](../works/pdagent-bench.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [ML-Bench](../works/ml-bench.md)
- [MLAgentBench](../works/mlagentbench.md)
- [RTLLM](../works/rtllm.md)
- [VerilogEval](../works/verilogeval.md)
- [AssertionBench](../works/assertionbench.md)
- [DA-Code](../works/da-code.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)
- [FVEval](../works/fveval.md)
- [GenoTEX](../works/genotex.md)
- [MLE-bench](../works/mle-bench.md)
- [RE-Bench](../works/re-bench.md)
- [RTL-Repo](../works/rtl-repo.md)
- [SciCode](../works/scicode.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [SimBench](../works/simbench.md)
- [SUPER](../works/super.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [AInsteinBench](../works/ainsteinbench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [CodePDE](../works/codepde.md)
- [CVDP](../works/cvdp.md)
- [EXP-Bench](../works/exp-bench.md)
- [FEABench](../works/feabench.md)
- [FEM-Bench](../works/fem-bench.md)
- [HLS-Eval](../works/hls-eval.md)
- [MatTools](../works/mattools.md)
- [MedAgentGym](../works/medagentgym.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [PaperBench](../works/paperbench.md)
- [PDE-Controller](../works/pde-controller.md)
- [ResearchCodeBench](../works/researchcodebench.md)
- [SysMoBench](../works/sysmobench.md)
- [AutoDFT / VASPBench](../works/vaspbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [BioXArena](../works/bioxarena.md)
- [Collider-Bench](../works/collider-bench.md)
- [gwBenchmarks](../works/gwbenchmarks.md)
- [MDArena](../works/mdarena.md)
- [MooseBench](../works/moosebench.md)
- [NatureBench](../works/naturebench.md)
- [PDEAgent-Bench](../works/pdeagent-bench.md)
- [PRBench](../works/prbench.md)
- [QMP-Bench](../works/qmp-bench.md)
- [StructureClaw](../works/structureclaw.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [CRAFTS](../works/crafts.md)
