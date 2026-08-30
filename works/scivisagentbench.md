# SciVisAgentBench (2026)

> **English** | [简体中文](../zh/works/scivisagentbench.md)

> **First appeared:** 2026-03-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2603.29139)

## Overview

SciVisAgentBench is a benchmark for evaluating agents that translate natural-language intent into executable scientific data-analysis and visualization (SciVis) tasks across multi-step, realistic analysis settings.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities


- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2603.29139
- **Project:** https://scivisagentbench.github.io/
- **Code:** https://github.com/KuangshiAi/SciVisAgentBench
- **Venue:** IEEE Transactions on Visualization and Computer Graphics (IEEE VIS 2026), per the official project page

## Summary

SciVisAgentBench is a comprehensive, extensible benchmark for evaluating scientific visualization agents in realistic, multi-step analysis settings. It is grounded in a structured taxonomy spanning four dimensions — application domain, data type, complexity level, and visualization operation — and pairs the task suite with a multimodal, outcome-centric evaluation pipeline that combines LLM-based judging with deterministic evaluators. The authors also run a validity study with SciVis experts to examine agreement between human and LLM judges, and report initial baselines for representative SciVis agents and general-purpose coding agents. It is framed as a "living benchmark" for systematic comparison and failure-mode diagnosis.

## Tasks

108 expert-crafted cases covering diverse SciVis scenarios. Cases are organized by a four-dimension taxonomy:

- **Application domain:** astronomy, medical science, biology, physics, earth system science, mathematics, chemistry.
- **Data type:** scalar, vector, and tensor fields; multivariate and time-varying data.
- **Complexity level:** operations (basic procedures), tasks (structured operation sequences), and workflows (multi-stage interrelated tasks).
- **Visualization operations:** 15 categories, including color & opacity mapping, data sampling & resolution control, field computation, volume rendering, and scientific insight derivation.

The benchmark spans multiple visualization platforms/tools (e.g., ParaView, napari-based bioimage tools, molecular-dynamics tooling, and topology tools) and supports different interaction paradigms (CLIs, MCP protocols, Python APIs). Repository note: the official project page reports a split of 74 task-level and 34 workflow-level cases; the paper's three-level complexity taxonomy (operations/tasks/workflows) is not fully reconciled with this two-way split in the sources consulted.

## Domains

Scientific visualization across astronomy, medical science, biology, physics, earth system science, mathematics, and chemistry.

## Evaluation

A multimodal, outcome-centric evaluation pipeline that combines LLM-based (multimodal LLM) judging with deterministic evaluators:

- **Image-based metrics:** PSNR, SSIM, LPIPS, with scaled variants that account for task completion rates and multi-viewpoint rendering.
- **Code checkers:** script verification and execution for code-generated solutions.
- **Rule-based verifiers:** deterministic assessment of discrete outputs.
- **Case-specific evaluators:** custom scripts (e.g., topology tasks, coordinate verification, visualization-state validation).

A validity study with 12 SciVis experts examines human–LLM judge agreement. Reported figures include Krippendorff's α of 0.719 among humans (outliers removed) and a Pearson correlation of 0.808 between the LLM judge (reported as Claude-Opus-4.6) and human ratings, with a judge stability score of 0.975.

## Typical Duration

TODO(reference) — the sources consulted do not state a per-case trajectory length, wall-clock time, or token budget, though token usage is compared across agents (e.g., token-efficiency comparisons).

## Main Contribution

A principled, reproducible, and extensible benchmark for evaluating scientific data-analysis and visualization agents, combining a structured four-dimension taxonomy of 108 expert-crafted cases with a multimodal outcome-centric evaluation pipeline and a human–LLM judge validity study, establishing initial baselines and revealing capability gaps.

## Key Design Ideas

- Structured four-dimension taxonomy (application domain, data type, complexity level, visualization operation) organizing 108 cases.
- Multimodal outcome-centric evaluation combining an LLM/MLLM judge with deterministic evaluators (image metrics, code checkers, rule-based verifiers, case-specific evaluators).
- Image-metric scaling that accounts for task completion rates and multiple rendering viewpoints.
- Human–LLM judge alignment study to justify LLM-based judging.
- Platform- and paradigm-agnostic harness supporting CLIs, MCP servers, and Python APIs, with YAML-configured cases.
- Framed as a "living" / extensible benchmark.

## Strengths

- Broad coverage across multiple science domains, data types, and 15 visualization-operation categories (paper).
- Combines subjective LLM judging with deterministic, execution- and image-based verifiers rather than relying on a single scoring mode (paper).
- Includes an explicit human–LLM judge validity study with reported agreement statistics (paper).
- Evaluates both specialized SciVis agents and general-purpose coding agents (paper).

## Limitations

- Evaluated baselines include both specialized SciVis agents (ChatVis, ParaView-MCP, GMX-VMD-MCP, BioImage-Agent, TopoPilot) and general-purpose coding agents (Claude Code, Codex); reported results indicate general-purpose coding agents outperform specialized agents on most task suites, while some specialized agents are more token-efficient (paper).
- Repository note: several reported numbers (per-case duration/token budgets, exact task/workflow split) are not fully specified in the sources consulted and are marked `TODO(reference)` or as project-page figures.

## Related Works

- TODO(reference) — related SciVis / agent-evaluation works to be linked once corresponding cards exist.
