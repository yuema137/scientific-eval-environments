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

Astronomy contributes a distinct cluster of **analysis over observational archives and survey streams**. One strand vets or classifies survey detections directly from the instrument products a human reviewer sees: [AstroAlertBench](../works/astroalertbench.md) pairs broker metadata with science/reference/difference stamps for ZTF alerts, and [Spec-o3 / SpecVI-Bench](../works/spec-o3.md) has the agent re-render chosen wavelength intervals of LAMOST spectra before committing to a rare-object verdict. A second strand infers physical quantities from archival catalogs through established analysis codes — [Mephisto](../works/mephisto.md) searches over CIGALE spectral-energy-distribution models for 256 COSMOS2020 galaxies against an exhaustive-grid reference, [gammapyGPT](../works/gammapygpt.md) validates Gammapy fluxes and spectral indices numerically, [Plausible but Wrong](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) scores supernova, rotation-curve, exoplanet and lensing analyses on parameter recovery, and [the Einstein Telescope agent comparison](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) runs a full matched-filter search on simulated detector strain. [AstroVisBench](../works/astrovisbench.md) and [Imaging-101](../works/imaging-101.md) sit at the code-bearing end of the same cluster, and [VESTA / DAWN](../works/vesta-dawn.md) isolates the plot-transform-refit loop on astrophysical functional families.

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
| AstroVisBench | 2025 | Astronomy-specific data-processing workflows from notebooks | 432 processing + 432 visualization tasks from 110 notebooks | Variable-recall score plus VLM-judged plot correctness (best 15.7% error-free) | [card](../works/astrovisbench.md) |
| BAISBench | 2025 | Omics-driven single-cell biological discovery | 15 datasets annotation + 193 discovery MCQs | Correct cell types and study conclusions vs human baseline | [card](../works/baisbench.md) |
| BixBench | 2025 | Exploratory computational-biology data analysis | 50+ scenarios, | 300 questions, Jupyter container | [card](../works/bixbench.md) |
| EXP-Bench | 2025 | End-to-end AI research experimentation | 461 tasks from 51 papers, 12,737 subtasks | Design/implement/execute/analyze (0.5% full) | [card](../works/exp-bench.md) |
| gammapyGPT | 2025 | Gamma-ray observation analysis through the Gammapy library | 4 tasks on real observational data, stripped execution environment | Exact or tolerance match on observation counts, flux and spectral index | [card](../works/gammapygpt.md) |
| Gravity-Bench-v1 | 2025 | Budgeted observation and gravitational-physics inference | Simulated two-body systems, OOD variants | Characterize concealed physics vs reference solutions | [card](../works/gravity-bench.md) |
| HiSciBench | 2025 | Data-driven discovery from a supplied dataset and research problem | L5.1: 74 instances requiring Python analysis to be written and run | Execution-based success rate against task-specific criteria | [card](../works/hiscibench.md) |
| LLM-IOAA | 2025 | Olympiad data-analysis over plots, spectra and sky images | 8 data-analysis problems from the IOAA exams of 2022-2025 | Official marking-scheme partial credit (GPT-5 88.5%) | [card](../works/llm-ioaa.md) |
| MedAgentGym | 2025 | Code-centric biomedical data-science reasoning | 72,413 instances, 129 categories, sandboxed | Verifiable ground-truth pass; also RL training | [card](../works/medagentgym.md) |
| Mephisto | 2025 | Inferring galaxy physical properties from multi-band photometry | 256 COSMOS2020 galaxies plus 31 JWST Little Red Dots; CIGALE tree search | Fit reaching chi-squared below 1.2x the exhaustive-grid baseline | [card](../works/mephisto.md) |
| SciGym | 2025 | Iterative experiment design over hidden SBML systems | 137 small systems evaluated, 350 released | Submit hypothesized mechanism vs ground-truth system | [card](../works/scigym.md) |
| SpatialBench | 2025 | Spatial-biology analysis from data snapshot | 146 problems, five technologies, seven categories | Deterministic recovery of key biological result | [card](../works/spatialbench.md) |
| VLM-Verified Autonomous Discovery | 2025 | Recovering the underlying model behind a supplied dataset | 10 tasks: power spectra, spectral lines, oscillators, epidemiology | pass@1 on identifying the correct model (0.7-0.8 with VLM feedback) | [card](../works/enhancing-agentic-autonomous-scientific-discovery.md) |
| AstroAlertBench | 2026 | Vetting survey alerts from broker metadata and difference stamps | 1,500 real ZTF alerts, 300 per class, three graded stages | End-to-end 5-class accuracy (best 60.60%) vs 30.67% human ensemble | [card](../works/astroalertbench.md) |
| BioAgent Bench | 2026 | End-to-end bioinformatics pipeline execution | RNA-seq/variant-calling/metagenomics, perturbation probes | LLM-graded output artifacts and step reasoning | [card](../works/bioagent-bench.md) |
| BrainBench | 2026 | Instruction-conditioned EEG understanding and analysis | Four subsets, 17 datasets, CodeAct/agentic | Scientifically grounded report across output dimensions | [card](../works/brainbench-eeg.md) |
| DSAgentBench | 2026 | Automate full data-science analysis workflows | 275 tasks in real computer envs (notebooks, terminals, browsers, DBs) | Deterministic checks of analytical correctness (best 56.7%) | [card](../works/dsagentbench.md) |
| Einstein Telescope Agentic AI Comparison | 2026 | Executing a matched-filter gravitational-wave search end to end | One seven-stage specification, two agents, two runs, identical hardware | Detection efficiency and recovered SNR, plus counted process deviations | [card](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| Fisher-R1 / P-Bench | 2026 | Select test, compute p-value, draw valid inference | 425 hypothesis-testing tasks; economics, biology, medicine | Reject/fail-to-reject match plus p-value closeness (Raw/Strict) | [card](../works/fisher-r1.md) |
| GeneBench-Pro | 2026 | Multistage statistical genomics analysis | 129 problems on simulated data-generating processes | Binary pass on decision-relevant number (best 28.7%) | [card](../works/genebench-pro.md) |
| GeoNatureAgent Benchmark | 2026 | Environmental geospatial analysis via tool calls | 93 tasks, 18 categories, self-hostable API | Expected tool calls and must-contain answers (best 60.8%) | [card](../works/geonatureagent-benchmark.md) |
| HeurekaBench | 2026 | Exploratory end-to-end research over published studies | 50 open + 50 MCQ from 41 insights, single-cell | Data-driven answers verified vs reported findings | [card](../works/heurekabench.md) |
| Imaging-101 | 2026 | Recovering signals from indirect measurements via inverse solvers | 57 paper-grounded tasks, six domains, four-stage canonical pipeline | NCC and NRMSE against per-task thresholds (best end-to-end 17/57) | [card](../works/imaging-101.md) |
| LongDA | 2026 | Documentation-intensive survey data analysis | 505 queries, 17 U.S. surveys, | 263k-token docs | [card](../works/longda.md) |
| MaD Physics | 2026 | Budgeted measurement and physical-law inference | Three simulated environments, altered-physics variants | Infer law to predict future system state | [card](../works/mad-physics.md) |
| Neuroscience Data-to-Discovery Case Study | 2026 | Behavior classification and statistical comparison of fly data | 9-task fly-optogenetics pipeline; ~47 GB data | Stage outputs vs expert annotations (e.g., Mann–Whitney U) | [card](../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) |
| Plausible but Wrong | 2026 | Analysis of public archival astronomical catalogs | 4 research tasks: supernovae, rotation curves, exoplanets, lensing | Parameter Recovery Score plus physical-plausibility rating | [card](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| Rodent-Bench | 2026 | Multimodal rodent-behavior video annotation | Long recordings (10-35 min), multiple paradigms | Temporal segmentation/classification (second-wise accuracy, F1) | [card](../works/rodent-bench.md) |
| scBench | 2026 | Single scRNA-seq analysis step from snapshot | 394 problems, six platforms, seven categories | Deterministic recovery of key biological result (29-53%) | [card](../works/scbench.md) |
| scBench-Long | 2026 | Long-horizon single-cell discovery from near-raw data | 21 evaluations, no prescribed method | Recover study conclusions, deterministic grading (25.4%) | [card](../works/scbench-long.md) |
| SciAgentArena | 2026 | Real biomedical research across scales |  | 200 tasks, five fields, stepwise verification | [card](../works/sciagentarena.md) |
| SciVisAgentBench | 2026 | Scientific data analysis and visualization for insight | 108 expert cases, seven science domains; multi-platform tools | Outcome-centric image metrics plus deterministic verifiers | [card](../works/scivisagentbench.md) |
| Spec-o3 / SpecVI-Bench | 2026 | Vetting rare-object candidates by inspecting survey spectra | 5 tasks, 1,122 positive / 5,632 negative LAMOST test spectra | Macro accuracy and positive-class F1 (Spec-o3-7B 88.7% / 76.5%) | [card](../works/spec-o3.md) |
| Stargazer | 2026 | Iterative physics-grounded RV model fitting | 120 tasks (100 synthetic + 20 real archival) | Per-criterion pass on Keplerian fits (Easy 80%, real 0%) | [card](../works/stargazer.md) |
| VESTA / DAWN | 2026 | Iterative distribution and time-series fitting with residual inspection | 400 instances including stellar-IMF and gravitational-wave chirp splits | Jensen-Shannon divergence and ELPD-LOO against ground truth | [card](../works/vesta-dawn.md) |

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
- [AstroVisBench](../works/astrovisbench.md)
- [gammapyGPT](../works/gammapygpt.md)
- [HiSciBench](../works/hiscibench.md)
- [LLM-IOAA](../works/llm-ioaa.md)
- [Mephisto](../works/mephisto.md)
- [Enhancing Agentic Autonomous Scientific Discovery with Vision-Language Model Capabilities](../works/enhancing-agentic-autonomous-scientific-discovery.md)
- [AstroAlertBench](../works/astroalertbench.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [Imaging-101](../works/imaging-101.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [Spec-o3](../works/spec-o3.md)
- [VESTA / DAWN](../works/vesta-dawn.md)
