# Scientific Software & Workflow Engineering

> **English** | [简体中文](../zh/activities/scientific_software_workflow_engineering.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on producing, repairing, integrating, or executing scientific and engineering software or workflows as a substantive capability — scientific code generation, numerical-algorithm implementation, repository engineering, pipeline construction, and hardware-description or formal-specification code.

## Scope

Covers scientific **and** engineering software or workflow artifacts — including HDL/RTL, formal models, numerical solvers, and scientific pipelines — where software correctness is central to the evaluation. It excludes general-purpose application or web software engineering, and incidental helper-scripting done in service of another activity.

## Task Patterns

**HDL/RTL generation and hardware verification.** A cluster of works targets hardware-description and formal-hardware code. [RTLLM](../works/rtllm.md) and [VerilogEval](../works/verilogeval.md) generate design/RTL Verilog from natural language graded by simulation; [RTL-Repo](../works/rtl-repo.md) extends this to repository-scale cross-file Verilog completion, [VHDL-Eval](../works/vhdl-eval.md) to VHDL, and [HLS-Eval](../works/hls-eval.md) to high-level synthesis. [CVDP](../works/cvdp.md) consolidates RTL generation, debugging, and verification across 783 problems. Verification-focused works produce assertions and testbenches: [AssertionBench](../works/assertionbench.md) generates SystemVerilog assertions against formally verified ground truth, and [FVEval](../works/fveval.md) decomposes formal verification into NL2SVA and Design2SVA sub-tasks checked by Cadence Jasper.

**PDE/numerical-solver and simulation-code generation.** Many works ask the agent to write numerical code or simulation input decks. [CodePDE](../works/codepde.md), [PDEAgent-Bench](../works/pdeagent-bench.md), and [PDE-Controller](../works/pde-controller.md) target PDE solvers; [FEM-Bench](../works/fem-bench.md) and [FEABench](../works/feabench.md) cover finite-element code; [CFDLLMBench](../works/cfdllmbench.md) spans CFD knowledge, Python solvers, and OpenFOAM cases; [MooseBench](../works/moosebench.md) reconstructs the PDE encoded in MOOSE input files; and [SimBench](../works/simbench.md) builds Chrono digital twins. [CRAFTS](../works/crafts.md) extends this to chemical-process flowsheeting, emitting typed intermediate representations that must clear deterministic IDAES/Pyomo gates before an executable model is constructed. Domain-simulation workflow execution appears in [VASPBench](../works/vaspbench.md), [MDArena](../works/mdarena.md), and [Collider-Bench](../works/collider-bench.md). A civil-engineering strand generates whole structural models as code: OpenSeesPy in [the beam agent study](../works/a-large-language-model-empowered-agent-for-reliabl.md), [a 2D frame multi-agent system](../works/a-lightweight-large-language-model-based-multi-age.md), [an OpenSeesPy-backed analysis framework](../works/integrating-large-language-models-for-automated-st.md) and [AutoBM](../works/autobm.md); SAP2000 scripts exceeding a thousand lines in [a 3D frame pipeline](../works/agentic-large-language-models-for-automated-struct.md); reliability solver code in [a multi-agent reliability framework](../works/automating-structural-reliability-analysis-with-a.md); and EPyT/EPANET functions in [LLM-EPANET](../works/llm-epanet.md).

**Scientific-repository engineering and research reproduction.** These works have agents operate on real codebases and papers. [AInsteinBench](../works/ainsteinbench.md) ports the SWE-bench maintainer-PR paradigm to six production scientific repos; [SUPER](../works/super.md) and [ML-Bench](../works/ml-bench.md) test setting up and executing real research repositories. Paper-reproduction works include [PaperBench](../works/paperbench.md), [EXP-Bench](../works/exp-bench.md), [PRBench](../works/prbench.md), [QMP-Bench](../works/qmp-bench.md), [NatureBench](../works/naturebench.md), and [gwBenchmarks](../works/gwbenchmarks.md).

**ML-research code implementation and ML engineering.** A large group frames ML research/engineering itself as the coded artifact. [MLAgentBench](../works/mlagentbench.md), [MLE-bench](../works/mle-bench.md), [MLE-Dojo](../works/mle-dojo.md), [MLRC-Bench](../works/mlrc-bench.md), [RE-Bench](../works/re-bench.md), and [DevAI](../works/devai.md) task agents with training models, optimizing code, or proposing novel methods against baselines and leaderboards. [ResearchCodeBench](../works/researchcodebench.md) implements novel contributions from recent papers, and [SciCode](../works/scicode.md) covers scientist-curated research coding across natural-science subfields.

**Bioinformatics/data-science pipelines and cross-domain workflows.** Pipeline-construction and data-science coding works include [GenoTEX](../works/genotex.md), [BioAgent Bench](../works/bioagent-bench.md), [MedAgentGym](../works/medagentgym.md), [BioXArena](../works/bioxarena.md), [DA-Code](../works/da-code.md), [ScienceAgentBench](../works/scienceagentbench.md), and [MatTools](../works/mattools.md) (pymatgen). Formal-specification code is represented by [SysMoBench](../works/sysmobench.md) (TLA+ models). Broader containerized scientific-computing harnesses are [Terminal-Bench Science](../works/terminal-bench-science.md) and the structural-engineering workbench [StructureClaw](../works/structureclaw.md). Engineering-document production is represented by [DrafterBench](../works/drafterbench.md), whose 46-function drafting toolchain makes the recorded operation chain, rather than the rendered drawing, the scored artifact. Two works move the interface itself: [ScienceBoard](../works/scienceboard.md) drives six professional scientific desktop applications through GUI and CLI inside an instrumented Ubuntu VM, and [ALeRCE Text-to-SQL](../works/alerce-text-to-sql.md) makes the artifact an executable query against a 25-table astronomical alert-broker schema whose domain semantics, not SQL syntax, are what agents get wrong — the same shape as [BiomedSQL](../works/biomedsql.md), where the query must additionally supply the significance thresholds, effect directions and trial-phase filters the question leaves unstated. Instrument- and library-specific analysis code forms a related strand: [gammapyGPT](../works/gammapygpt.md) targets a thinly documented, actively developed gamma-ray library where model priors are weakest, [AstroVisBench](../works/astrovisbench.md) separates processing code from the plot that must carry the scientific insight, and [Imaging-101](../works/imaging-101.md) canonicalizes 57 paper-grounded computational-imaging tasks into a fixed preprocessing / forward-physics / inverse-solver / visualization pipeline so failures can be attributed to a stage.

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
| AstroVisBench | 2025 | Astronomy processing and visualization code from notebook stages | 432 + 432 tasks from 110 Astro Data Lab and STScI notebooks | Variable-recall score plus VLM error category on the produced plot | [card](../works/astrovisbench.md) |
| BiomedSQL | 2025 | Executable SQL over a harmonized biomedical BigQuery knowledge base | 546-question test set from 68,000 triples; 10 tables up to 72.2M rows; BMSQL refinement loop | Execution Accuracy on gold results (best 62.6%, expert baseline 90.0%) plus syntax error rate | [card](../works/biomedsql.md) |
| CFDLLMBench | 2025 | CFD knowledge, Python solvers, OpenFOAM cases | 240 tasks in three tiers (CFDQuery/Code/Foam) | Executability, numerical error, convergence | [card](../works/cfdllmbench.md) |
| CodePDE | 2025 | PDE-solver code generation | Representative PDE problems with iterative refinement | Solver numerical accuracy on PDE problems | [card](../works/codepde.md) |
| Cosmological Model-Building with CLASS | 2025 | Patching a 43,000-line C Boltzmann-solver codebase | Containerized CLASS 3.3.0; patch-based submission, three staged tasks | Patch compiles and reproduces reference observables numerically | [card](../works/an-llm-driven-framework-for-cosmological-model-bui.md) |
| CVDP | 2025 | RTL design, debugging, and verification code | 783 problems, 13 categories; agentic + non-agentic | pass@1 (best <=34% on code generation) | [card](../works/cvdp.md) |
| DrafterBench | 2025 | Technical-drawing revision through a custom drafting toolchain | 1,920 tasks, 12 revision types, 46 PyMuPDF/OpenCV/Reportlab functions | Code executability (30 pts) plus operation-chain target completeness | [card](../works/drafterbench.md) |
| EXP-Bench | 2025 | End-to-end AI research experiment code | 461 tasks from 51 papers, incomplete starter code | Design/implementation/execution correctness (subtasks) | [card](../works/exp-bench.md) |
| FEABench | 2025 | FEA solution by driving COMSOL via API | Multiphysics NL problems; agentic API iteration | Executable API calls / correct computed answer | [card](../works/feabench.md) |
| FEM-Bench | 2025 | FEM functions and unit tests | 33 function-writing tasks + test track; 5 attempts | Objective verification / joint success rate | [card](../works/fem-bench.md) |
| gammapyGPT | 2025 | Gammapy analysis scripts written, executed and repaired in a loop | 4 tasks in a stripped environment with a data pointer and time limit | Validated numerical output, logged with the attempt index that passed | [card](../works/gammapygpt.md) |
| HLS-Eval | 2025 | High-level-synthesis code and optimization edits | 94 designs, two tasks; framework-harnessed | Parse/compile/run/synthesize on Vitis HLS (pass@k) | [card](../works/hls-eval.md) |
| Integrating LLMs for Automated Structural Analysis | 2025 | OpenSeesPy and OpsVis scripts from structural word problems | 20 problems; best-of-3 model comparison and 5-run stability study | Complete executable code with correct internal forces (GPT-4o 100%) | [card](../works/integrating-large-language-models-for-automated-st.md) |
| Lightweight Multi-Agent System for 2D Frame Analysis | 2025 | OpenSeesPy frame code via a JSON topology intermediate representation | 20 frame problems, 5 agents, 10 trials each, tool-based validation agent | Proportion of correctly generated codes (over 80% on most problems) | [card](../works/a-lightweight-large-language-model-based-multi-age.md) |
| LLM-EPANET | 2025 | EPyT/EPANET Python functions with retrieval and self-debugging | 69 queries, 3 networks, up to 5 retries, 60 s sandbox timeout | Result equivalence to hand-written reference scripts (56-81%) | [card](../works/llm-epanet.md) |
| MatTools | 2025 | pymatgen tool comprehension and Python code | 69,225 QA pairs + 49 tasks (138 subtasks); execution | Correct executed materials-property answers | [card](../works/mattools.md) |
| MedAgentGym | 2025 | Biomedical data-science coding | 72,413 instances, 129 categories; sandbox w/ feedback | Verifiable ground-truth success (RL-trainable) | [card](../works/medagentgym.md) |
| MLE-Dojo | 2025 | ML-engineering solutions in interactive gym | 200+ Kaggle challenges; structured feedback loop | Iterative improvement / long-horizon quality | [card](../works/mle-dojo.md) |
| MLRC-Bench | 2025 | Novel ML research methods implemented | 7 competition tasks; scaffolded agent | Fraction of baseline-to-human gap closed (best 9.3%) | [card](../works/mlrc-bench.md) |
| PaperBench | 2025 | Replicate AI papers from scratch | 20 ICML papers, 8,316 rubric subtasks; agentic | Rubric-graded replication score (LLM judge) | [card](../works/paperbench.md) |
| PDE-Controller | 2025 | STL autoformalization + PDE-control programs | Heat/wave systems; human cases + 2M synthetic | Reasoning/autoformalization/synthesis metrics; utility gain | [card](../works/pde-controller.md) |
| ResearchCodeBench | 2025 | Implement novel ML-paper contributions as code | 212 challenges from 20 recent papers; static | Correct executable implementation (best 37.3%) | [card](../works/researchcodebench.md) |
| ScienceBoard | 2025 | Operating professional scientific desktop applications | 169 tasks over six applications in an Ubuntu VM; GUI and CLI channels | Binary success from intermediate I/O and final VM state (best 24.20%) | [card](../works/scienceboard.md) |
| SysMoBench | 2025 | TLA+ formal system models + TLC config | 11 concurrent/distributed artifacts, 175-5,360 SLOC | Syntax/runtime/conformance/invariant checks (automated) | [card](../works/sysmobench.md) |
| Agentic LLMs for 3D Frame Structural Analysis | 2026 | SAP2000 scripts exceeding a thousand lines, generated floor by floor | 10 irregular 3D frames, 10 trials each, checkpointed regeneration | Executable script whose computed responses match a reference within 1% | [card](../works/agentic-large-language-models-for-automated-struct.md) |
| ALeRCE Text-to-SQL | 2026 | Generating executable SQL against an alert-broker schema | 110 astronomer-authored NL/SQL pairs; 25 tables, 304 columns | Perfect Match on executed rows and columns, split by difficulty tier | [card](../works/alerce-text-to-sql.md) |
| AutoBM / BMEval | 2026 | OpenSeesPy building-model programs of roughly 600 lines | 128 tasks, sandboxed execution, 16 models, 5 perturbed evaluations | Pass@k with period-agreement and compliance-verdict variants | [card](../works/autobm.md) |
| AutoDFT / VASPBench | 2026 | Autonomous DFT (VASP) workflow execution | 34 tasks, 9 calculation types; closed-loop agent | Task-level success + property accuracy (94.1%) | [card](../works/vaspbench.md) |
| Automating Structural Reliability Analysis | 2026 | Reliability solver code passed between typed data contracts | 20 problems; Code Engineer emits code, non-LLM Runner parses the results | Executable code returning parseable beta and P_f on all 20 problems | [card](../works/automating-structural-reliability-analysis-with-a.md) |
| BioAgent Bench | 2026 | End-to-end bioinformatics pipelines | Curated RNA-seq/variant-calling/metagenomics; agentic | LLM-graded pipeline progress + outcome validity | [card](../works/bioagent-bench.md) |
| BioXArena | 2026 | Multi-modal biomedical ML models | 76 tasks, 9 domains; 2h single-GPU environment | Hidden-label biology-aware score (0-1) | [card](../works/bioxarena.md) |
| Collider-Bench | 2026 | LHC analysis reproduction (simulation pipeline) | 10 CMS SUSY tasks; containerized public stack | Histogram fidelity vs hidden reference yields | [card](../works/collider-bench.md) |
| CRAFTS | 2026 | Executable IDAES/Pyomo chemical-process simulation models | OpenIDAES-450; 82 frozen held-out cases, typed IRs, deterministic gates | Workflow Success 91.5% + unit/stream/connection macro-F1 | [card](../works/crafts.md) |
| Einstein Telescope Agentic AI Comparison | 2026 | Executing a seven-stage gravitational-wave pipeline from a written spec | One exp.md specification, two agents, identical server, data and libraries | Specification thresholds met, plus counted restarts and silent deviations | [card](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| gwBenchmarks | 2026 | Gravitational-wave modeling/surrogate code | 8 high-precision tasks; >10^8 core-hours data | External-framework score at near 1e-4 error | [card](../works/gwbenchmarks.md) |
| Imaging-101 | 2026 | Building four-stage computational-imaging reconstruction pipelines | 57 paper-grounded tasks; planning, unit-test and end-to-end tracks | pytest module pass plus NCC/NRMSE thresholds (end-to-end best 17/57) | [card](../works/imaging-101.md) |
| LLM-Empowered Agent for Structural Analysis | 2026 | OpenSeesPy code generation with automatic execution and visualization | 8 beam problems, 500 runs each, five-component prompt ablation | Reliability above 0.990; collapses to 0.000 without the complete example | [card](../works/a-large-language-model-empowered-agent-for-reliabl.md) |
| LQCDMaster | 2026 | PyQUDA measurement scripts, job-submission artifacts and execution logs | 70 LQCD tasks; deterministic Wick-contraction tool plus three expert-annotated skills | Executable workflow reproducing the expert reference at machine precision (90.0% Matched) | [card](../works/lqcdmaster.md) |
| MDArena | 2026 | Molecular-dynamics workflow code | 50 containerized tasks, 29 systems, 14 protocols | Strict success rate + process partial credit | [card](../works/mdarena.md) |
| MooseBench | 2026 | MOOSE multiphysics simulation input files | 220 cases with PDE-level ground truth | Intent Fidelity Score (reconstructed PDE match) | [card](../works/moosebench.md) |
| NatureBench | 2026 | Match published SOTA scientific code | 90 tasks from Nature-family papers, six domains | Reach/exceed published SOTA under info firewall | [card](../works/naturebench.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | Build a neuroscience data-to-discovery pipeline in code | 9 computational tasks (7 stages + end-to-end); Harbor-compatible | Correct stage code vs expert annotations and legacy codebases | [card](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| PDAgent-Bench | 2026 | Generate EDA-tool scripts for VLSI physical design | 210 script-gen tasks + closed-loop flow; Innovus/ICC2/OpenROAD | Execution-validated scripts (pass@1/5) | [card](../works/pdagent-bench.md) |
| PDEAgent-Bench | 2026 | PDE solver code for FEM libraries | 645 instances, 6 categories; DOLFINx/Firedrake/deal.II | Staged executability, accuracy, efficiency | [card](../works/pdeagent-bench.md) |
| PRBench | 2026 | Reproduce physics research from papers | 30 expert-curated tasks, 11 subfields; sandbox | Quantitative match to publication (CSV rubric) | [card](../works/prbench.md) |
| QMP-Bench | 2026 | Quantum many-body simulation code | 100 end-to-end tasks from 21 journals | Coding correctness + physical validity | [card](../works/qmp-bench.md) |
| Quantifying Reproducibility of Astrophysical Methods | 2026 | Reconstructing a published analysis pipeline as executable Python | One method at three nested text-information levels; five models | Hierarchy of Scientific Validity 0-3, with V >= 2 the stated threshold | [card](../works/quantifying-the-reproducibility-of-astrophysical-m.md) |
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
- [DrafterBench](../works/drafterbench.md)
- [Integrating Large Language Models for Automated Structural Analysis](../works/integrating-large-language-models-for-automated-st.md)
- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](../works/a-lightweight-large-language-model-based-multi-age.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Agentic Large Language Models for Automated Structural Analysis of 3D Frame Systems](../works/agentic-large-language-models-for-automated-struct.md)
- [AutoBM / BMEval](../works/autobm.md)
- [Automating Structural Reliability Analysis with a Multi-Agent Large Language Model Framework](../works/automating-structural-reliability-analysis-with-a.md)
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](../works/a-large-language-model-empowered-agent-for-reliabl.md)
- [AstroVisBench](../works/astrovisbench.md)
- [An LLM-driven framework for cosmological model-building and exploration](../works/an-llm-driven-framework-for-cosmological-model-bui.md)
- [gammapyGPT](../works/gammapygpt.md)
- [ScienceBoard](../works/scienceboard.md)
- [ALeRCE Text-to-SQL](../works/alerce-text-to-sql.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [Imaging-101](../works/imaging-101.md)
- [Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory](../works/quantifying-the-reproducibility-of-astrophysical-m.md)
- [BiomedSQL](../works/biomedsql.md)
- [LQCDMaster](../works/lqcdmaster.md)
