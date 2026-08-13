# AstroVisBench (2025)

> **English** | [简体中文](../zh/works/astrovisbench.md)

## Overview

AstroVisBench is a code benchmark for scientific computing and visualization in astronomy: a model must implement an astronomy-specific data-processing workflow and then produce the plot that conveys the intended scientific insight. Visualizations are graded by a VLM-as-a-judge pipeline validated against annotations by five professional astronomers.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.20538>
- **Project:** <https://astrovisbench.github.io/>
- **Code:** <https://github.com/SebaJoe/AstroVisBench>
- **Data:** <https://huggingface.co/datasets/sebajoe/AstroVisBench>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track

## Summary

AstroVisBench targets a step of scientific work that most code benchmarks skip: whether the artifact a model produces actually communicates the right scientific result. Each instance is split into three stages — setup, processing, visualization — derived from real astronomy tutorial notebooks; the model is given the setup stage and must write the processing code, and separately must write the visualization code. Processing output is scored by comparing the resulting in-memory variables against the ground-truth ones, and visualization output is scored by a vision-language judge that classifies the generated plot against the reference plot as No Error, Minor Error, or Major Error. Evaluation of eight contemporary models shows a large gap relative to research-assistant usefulness: the strongest model reaches "No Error" on only a small minority of visualization tasks.

## Tasks

432 processing tasks and 432 visualization tasks, extracted from 110 Jupyter notebooks. Notebooks were drawn from two curated astronomy tutorial collections — the Astro Data Lab and the Space Telescope Science Institute. The authors selected notebooks whose final cell produces a visualization, extracted cell dependencies, and split each instance into setup, processing, and visualization stages.

## Domains

Astronomy: the workflows are astronomy-specific data processing and plotting over astronomical survey and mission data from the Astro Data Lab and STScI tutorial corpora, and the correctness judgment is about whether the scientific insight in the plot is right. Secondary co-domain is Computer Science / Software & Systems, since the task form is code generation and execution in a Python scientific-computing environment.

## Evaluation

- **Processing stage.** Generated code is executed and its resulting variables compared with the ground-truth variables via a Variable Inspection Score, `VIscore = |V_M ∩ V_G| / |V_G|`, i.e. recall of the ground-truth key variables. Execution crashes are reported separately as a crash rate.
- **Visualization stage.** A vision-language judge compares the generated plot with the reference plot and assigns one of three error categories: No Error, Minor Error, Major Error. Reported metrics include the fraction of crash-free visualization runs, a VisFail rate for responses producing the wrong number of visualizations, and the CorrectV / MiE / MaE breakdown.
- **Judge validation.** Five professional astronomers, all holding a doctorate in astronomy, astrophysics or physics, annotated 135 visualization pairs (270 visualizations). Inter-annotator agreement on error category was Fleiss' κ = 0.53, with pairwise Spearman's ρ = 0.69 on the 30 tasks annotated by all five. Among candidate judges, Claude 3.5 Sonnet correlated best with the expert annotations at ρ = 0.822 and was adopted as the judge.
- **Reported.** Eight models were evaluated — Gemini 2.5 Pro, Claude 3.7 Sonnet, Claude 4.0 Opus, o3-mini, GPT-4o, QwQ, Qwen-2.5, Llama-4 Maverick. Gemini 2.5 Pro was strongest, with a 30.8% crash rate on processing tasks, VIscore 0.600, and on visualization tasks only 15.7% "No Error" against 28.5% major errors.

## Typical Duration

Not reported as a per-task time or token budget. The paper specifies the harness instead: execution on two 56-core Intel Xeon MAX 9480 CPUs with 128 GB RAM total, and roughly 100 GB of storage per model evaluation (about 50 GB for the execution environment and 50 GB for pickled objects). Generation used a 1,024-token cap for Claude 3.7 Sonnet, which only 10 of 864 responses reached.

## Main Contribution

The first benchmark that jointly evaluates astronomy-specific scientific computing and the visualization of its results, together with an LLM/VLM-as-a-judge evaluation of visualization correctness that is validated against professional-astronomer annotation.

## Key Design Ideas

- Three-stage decomposition of real tutorial notebooks (setup / processing / visualization) so that the two capabilities can be scored independently while keeping realistic context.
- Variable-level scoring for the processing stage, checking the data products in memory rather than string-matching the code or the printed output.
- Visualization graded on scientific correctness with a graded error taxonomy (No Error / Minor / Major) instead of pixel or structural similarity.
- Judge selection driven by measured correlation with a five-astronomer annotation panel, rather than assumed.
- Public leaderboard and released execution environments, including a ground-truth cache to make re-running cheaper.

## Strengths

- Grounded in curated professional astronomy tutorial notebooks, so the workflows reflect real archive and mission data practice rather than synthetic exercises.
- The visualization judge is empirically calibrated against domain experts, and the agreement statistics are reported rather than asserted.
- Separating processing from visualization isolates two failure modes that end-to-end code benchmarks conflate.

## Limitations

- Inter-annotator agreement among the five astronomers is only moderate (Fleiss' κ = 0.53), which bounds how sharply the visualization metric can discriminate.
- Repository note: `VIscore` measures recall of ground-truth variables and does not penalize spurious extra variables, so it rewards partially correct workflows that also produce incorrect intermediate products.
- Repository note: the benchmark scores single-shot code generation per stage, not an iterative agent loop with tool feedback, so it measures workflow authoring rather than long-horizon autonomous investigation.
- Repository note: the harness has a substantial storage footprint (about 100 GB per model evaluation), which raises the cost of independent replication.

## Related Works

- [SciVisAgentBench](./scivisagentbench.md) — Also scores agents on scientific visualization with an LLM-judge plus deterministic evaluators, but across general SciVis domains rather than astronomy notebooks specifically.
- [Stargazer](./stargazer.md) — Also an astronomy evaluation with executable ground truth, but an iterative model-fitting environment rather than staged code and plot generation.
- [ScienceAgentBench](./scienceagentbench.md) — Also grades generated data-analysis programs against expert-validated references across scientific disciplines, without the visualization-correctness judge.
- [SciCode](./scicode.md) — Also a scientific code-generation benchmark built from research workflows, scored by execution rather than by visual scientific correctness.
