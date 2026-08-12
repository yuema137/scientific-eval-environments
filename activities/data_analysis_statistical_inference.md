# Data Analysis & Statistical Inference

> **English** | [简体中文](../zh/activities/data_analysis_statistical_inference.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on extracting scientific conclusions from data — preprocessing, exploratory and statistical analysis, estimation, hypothesis testing, fitting, uncertainty quantification, and interpretation of results.

## Scope

Includes bioinformatics and omics analysis, statistical inference over scientific datasets, and structured analysis pipelines where analysing data is the central scientific activity. It is **not** assigned because a benchmark merely computes evaluation statistics, and is distinguished from Modeling & Prediction, whose core deliverable is a predictive model rather than a conclusion drawn from observed data.

## Task Patterns

A large cluster targets **single-cell and omics data analysis**. [BAISBench](../works/baisbench.md), [scBench](../works/scbench.md), [scBench-Long](../works/scbench-long.md), and [SpatialBench](../works/spatialbench.md) evaluate agents on recovering biological results from single-cell or spatial transcriptomic data, mostly via deterministic snapshot-based grading. [BixBench](../works/bixbench.md) and [HeurekaBench](../works/heurekabench.md) recast published notebook analyses into open-ended exploratory tasks, while [GenoTEX](../works/genotex.md), [BioAgent Bench](../works/bioagent-bench.md), and [GeneBench-Pro](../works/genebench-pro.md) span gene-expression pipelines, RNA-seq/variant-calling workflows, and simulation-grounded multistage genomic statistics. [MedAgentGym](../works/medagentgym.md) and [SciAgentArena](../works/sciagentarena.md) extend this into biomedical data science and cross-scale biomedical research.

A second cluster covers **general data-science and documentation-intensive analysis**. [BLADE](../works/blade.md), [DA-Code](../works/da-code.md), [DSBench](../works/dsbench.md), and [ScienceAgentBench](../works/scienceagentbench.md) benchmark open-ended wrangling, analytics, and statistical modeling against expert or publication-derived ground truth, and [AstaBench](../works/astabench.md) bundles a data-analysis category into a broader research suite. [LongDA](../works/longda.md) makes long-document navigation over U.S. federal survey data the central bottleneck, and [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md) tests environmental geospatial analysis through structured tool calls to a production API.

A third cluster frames analysis as **budgeted measurement and physics-grounded fitting**: [Gravity-Bench-v1](../works/gravity-bench.md), [MaD Physics](../works/mad-physics.md), [SciGym](../works/scigym.md), and [Stargazer](../works/stargazer.md) require agents to plan data collection under cost budgets and infer laws, mechanisms, or orbital models from collected/simulated data. [EXP-Bench](../works/exp-bench.md) extends this to end-to-end AI research experimentation.

A final cluster addresses **neuroscience and behavioral signal analysis**: [BrainBench (EEG)](../works/brainbench-eeg.md) evaluates instruction-conditioned EEG analysis and reporting, and [Rodent-Bench](../works/rodent-bench.md) tests multimodal annotation of long rodent-behavior video.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| BLADE | 2024 | Open-ended data-driven scientific analysis graded on analytical choices | 12 datasets with research questions from literature | Match expert data-scientist ground-truth analyses | [card](../works/blade.md) |
| DA-Code | 2024 | Agentic data-science code generation | Wrangling/analytics tasks in Docker sandbox | Execution-verified accuracy (best LLM 30.5%) | [card](../works/da-code.md) |
| DSBench | 2024 | Data-analysis and modeling on realistic multimodal tasks | 540 tasks (466 analysis + 74 modeling), multi-table | Solve tasks (best agent 34.12% analysis) | [card](../works/dsbench.md) |
| GenoTEX | 2024 | Gene-trait association gene-expression analysis | 1,384 problems over 911 datasets, full pipeline | Match bioinformatician-curated reference code/results | [card](../works/genotex.md) |
| ScienceAgentBench | 2024 | Individual data-driven scientific-workflow tasks | 102 tasks from 44 papers, four disciplines | Self-contained Python program, execution scored | [card](../works/scienceagentbench.md) |
| AstaBench | 2025 | Holistic scientific research incl. data analysis | 2,400+ problems across 11 benchmarks | Cost-controlled scoring vs standardized baselines | [card](../works/astabench.md) |
| BAISBench | 2025 | Omics-driven single-cell biological discovery | 15 datasets annotation + 193 discovery MCQs | Correct cell types and study conclusions vs human baseline | [card](../works/baisbench.md) |
| BixBench | 2025 | Exploratory computational-biology data analysis | 50+ scenarios, | 300 questions, Jupyter container | [card](../works/bixbench.md) |
| EXP-Bench | 2025 | End-to-end AI research experimentation | 461 tasks from 51 papers, 12,737 subtasks | Design/implement/execute/analyze (0.5% full) | [card](../works/exp-bench.md) |
| Gravity-Bench-v1 | 2025 | Budgeted observation and gravitational-physics inference | Simulated two-body systems, OOD variants | Characterize concealed physics vs reference solutions | [card](../works/gravity-bench.md) |
| MedAgentGym | 2025 | Code-centric biomedical data-science reasoning | 72,413 instances, 129 categories, sandboxed | Verifiable ground-truth pass; also RL training | [card](../works/medagentgym.md) |
| SciGym | 2025 | Iterative experiment design over hidden SBML systems | 137 small systems evaluated, 350 released | Submit hypothesized mechanism vs ground-truth system | [card](../works/scigym.md) |
| SpatialBench | 2025 | Spatial-biology analysis from data snapshot | 146 problems, five technologies, seven categories | Deterministic recovery of key biological result | [card](../works/spatialbench.md) |
| BioAgent Bench | 2026 | End-to-end bioinformatics pipeline execution | RNA-seq/variant-calling/metagenomics, perturbation probes | LLM-graded output artifacts and step reasoning | [card](../works/bioagent-bench.md) |
| BrainBench | 2026 | Instruction-conditioned EEG understanding and analysis | Four subsets, 17 datasets, CodeAct/agentic | Scientifically grounded report across output dimensions | [card](../works/brainbench-eeg.md) |
| DSAgentBench | 2026 | Automate full data-science analysis workflows | 275 tasks in real computer envs (notebooks, terminals, browsers, DBs) | Deterministic checks of analytical correctness (best 56.7%) | [card](../works/dsagentbench.md) |
| Fisher-R1 / P-Bench | 2026 | Select test, compute p-value, draw valid inference | 425 hypothesis-testing tasks; economics, biology, medicine | Reject/fail-to-reject match plus p-value closeness (Raw/Strict) | [card](../works/fisher-r1.md) |
| GeneBench-Pro | 2026 | Multistage statistical genomics analysis | 129 problems on simulated data-generating processes | Binary pass on decision-relevant number (best 28.7%) | [card](../works/genebench-pro.md) |
| GeoNatureAgent Benchmark | 2026 | Environmental geospatial analysis via tool calls | 93 tasks, 18 categories, self-hostable API | Expected tool calls and must-contain answers (best 60.8%) | [card](../works/geonatureagent-benchmark.md) |
| HeurekaBench | 2026 | Exploratory end-to-end research over published studies | 50 open + 50 MCQ from 41 insights, single-cell | Data-driven answers verified vs reported findings | [card](../works/heurekabench.md) |
| LongDA | 2026 | Documentation-intensive survey data analysis | 505 queries, 17 U.S. surveys, | 263k-token docs | [card](../works/longda.md) |
| MaD Physics | 2026 | Budgeted measurement and physical-law inference | Three simulated environments, altered-physics variants | Infer law to predict future system state | [card](../works/mad-physics.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | Behavior classification and statistical comparison of fly data | 9-task fly-optogenetics pipeline; ~47 GB data | Stage outputs vs expert annotations (e.g., Mann–Whitney U) | [card](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| Rodent-Bench | 2026 | Multimodal rodent-behavior video annotation | Long recordings (10-35 min), multiple paradigms | Temporal segmentation/classification (second-wise accuracy, F1) | [card](../works/rodent-bench.md) |
| scBench | 2026 | Single scRNA-seq analysis step from snapshot | 394 problems, six platforms, seven categories | Deterministic recovery of key biological result (29-53%) | [card](../works/scbench.md) |
| scBench-Long | 2026 | Long-horizon single-cell discovery from near-raw data | 21 evaluations, no prescribed method | Recover study conclusions, deterministic grading (25.4%) | [card](../works/scbench-long.md) |
| SciAgentArena | 2026 | Real biomedical research across scales |  | 200 tasks, five fields, stepwise verification | [card](../works/sciagentarena.md) |
| SciVisAgentBench | 2026 | Scientific data analysis and visualization for insight | 108 expert cases, seven science domains; multi-platform tools | Outcome-centric image metrics plus deterministic verifiers | [card](../works/scivisagentbench.md) |
| Stargazer | 2026 | Iterative physics-grounded RV model fitting | 120 tasks (100 synthetic + 20 real archival) | Per-criterion pass on Keplerian fits (Easy 80%, real 0%) | [card](../works/stargazer.md) |

## Related Works

- [SciVisAgentBench](../works/scivisagentbench.md)
- [Fisher-R1 / P-Bench](../works/fisher-r1.md)
- [DSAgentBench](../works/dsagentbench.md)
- [A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md)
- [BLADE](../works/blade.md)
- [DA-Code](../works/da-code.md)
- [DSBench](../works/dsbench.md)
- [GenoTEX](../works/genotex.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [AstaBench](../works/astabench.md)
- [BAISBench](../works/baisbench.md)
- [BixBench](../works/bixbench.md)
- [EXP-Bench](../works/exp-bench.md)
- [Gravity-Bench-v1](../works/gravity-bench.md)
- [MedAgentGym](../works/medagentgym.md)
- [SciGym](../works/scigym.md)
- [SpatialBench](../works/spatialbench.md)
- [BioAgent Bench](../works/bioagent-bench.md)
- [BrainBench](../works/brainbench-eeg.md)
- [GeneBench-Pro](../works/genebench-pro.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [HeurekaBench](../works/heurekabench.md)
- [LongDA](../works/longda.md)
- [MaD Physics](../works/mad-physics.md)
- [Rodent-Bench](../works/rodent-bench.md)
- [scBench](../works/scbench.md)
- [scBench-Long](../works/scbench-long.md)
- [SciAgentArena](../works/sciagentarena.md)
- [Stargazer](../works/stargazer.md)
