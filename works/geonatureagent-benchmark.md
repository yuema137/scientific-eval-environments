# GeoNatureAgent Benchmark (2026)

> **English** | [简体中文](../zh/works/geonatureagent-benchmark.md)

> **First appeared:** 2026-06-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.12821)

## Overview

GeoNatureAgent Benchmark is a benchmark for evaluating LLM agents on environmental geospatial analysis conducted through structured tool calls to a production-style API. It comprises 93 tasks across 18 categories, run against an open, self-hostable API that serves three environmental indicators across Spain and Portugal through 16 tools.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12821>
- **Code:** <https://github.com/gabrielireland/GeoNatureAgent_Benchmark>

## Summary

GeoNatureAgent Benchmark argues that environmental scientists spend disproportionate effort on data wrangling and that no existing benchmark evaluates agents operating through structured tool calling against real geospatial APIs. The authors present it as the first benchmark for environmental analysis agents that operate via structured tool calls to a production-style geospatial API, and demonstrate extensibility by integrating BigEarthNet V2 land cover for Portugal alongside the Spanish CO2 and erosion indicators. Across seven LLMs under three temperature-1.0 seeds, Claude Sonnet 4 leads at 60.8% ± 0.8%, the cost-accuracy Pareto frontier is occupied mostly by open-weight models, and close-value comparison tasks sit at 0% for every model.

## Tasks

93 tasks across 18 categories covering municipality analysis, multi-turn conversation, spatial reasoning, cross-indicator synthesis, error handling and recovery, ranking, comparison, multilingual understanding, habitat analysis, and task rejection; error-handling tasks are deliberately unsolvable to test graceful decline. By category (Table 1): Tool selection 21, Cross-indicator 8, Interpretation 7, Habitat analysis 7, and 14 further categories of 1–6 tasks each. Each task specifies a natural-language query (optionally with multi-turn history), expected tool calls, must-contain / must-not-contain strings, a maximum-rounds budget, a cost budget, and domain-expert ground truth; beyond this per-task specification, the paper does not describe how tasks were authored.

## Domains

Environmental geospatial analysis over Spain and Portugal: CO2 absorption suitability (categorical, Spain), gully erosion probability (continuous), and BigEarthNet V2 land cover (categorical, Portugal).

## Evaluation

- **Binary per-case pass.** Eight mechanistic checks per case, with no LLM-as-judge: every expected tool called, every expected action generated, required keywords present, forbidden keywords absent, numeric values within tolerance (default ±2 percentage points), a chart produced when required, and the round budget respected; the cost check is logged but excluded from the binary capability score.
- **Partial-credit diagnostics.** Check score (the fraction of individual checks passed per case), tool F1, keyword coverage, and cost utilization complement the binary metric.
- **Error taxonomy.** Each failure is attributed to its first failing check in a fixed priority order: missing tool, missing chart, wrong data, rounds exceeded, missing keyword, forbidden keyword.
- **Reported.** Across Claude Sonnet 4, DeepSeek V3.2, GLM-5, Gemini 2.5 Pro, Qwen3-235B, GPT-OSS-120B, and Llama 4 Scout: Claude Sonnet 4 leads at 60.8% ± 0.8% ($0.127/case); DeepSeek V3.2 reaches 56.3% ± 3.1% at $0.011/case — 93% of Claude's capability at 11× lower cost — with no other model above 51%; close-value comparison tasks sit at 0% for every model, and accuracies run 25–35 points below general-purpose GIS benchmarks. No human baseline is reported.

## Typical Duration

Runs are capped at 10 agent-loop turns and 4,096 output tokens per model call; each task carries a per-case cost budget defaulting to $0.10, logged but not gated. No wall-clock limit is stated.

## Main Contribution

A benchmark evaluating environmental analysis agents through structured tool calls to a production-style, self-hostable geospatial API, with capability and per-case cost reported as orthogonal axes.

## Key Design Ideas

- Structured tool calling against a real, self-hostable geospatial API of 16 tools (12 principal operations plus 4 auxiliary), rather than code generation or a simulated environment.
- Machine-checkable task specifications — expected tool calls, must-contain / must-not-contain strings, numeric tolerances, round and cost budgets — enabling fully automated grading.
- Deliberately unsolvable error-handling tasks and task-rejection coverage to test graceful decline.
- Three random seeds at temperature 1.0 per model, exposing run-to-run variance in tool-use reliability.

## Strengths

- Mechanistic checks avoid LLM-judge variance while still covering multi-turn, multilingual, and cross-indicator behavior.
- Orthogonal capability and cost axes surface a Pareto frontier occupied mostly by open-weight models.
- Self-hostable API and public harness support reproduction and extension, demonstrated by integrating BigEarthNet V2 land cover for Portugal.

## Limitations

- Repository note: Coverage is two countries and three environmental indicators — transfer of the task suite to other regions, indicator types, or APIs is demonstrated only by the single BigEarthNet V2 extension.
- Repository note: Several of the 18 categories hold very few tasks (Comparison 2, Ranking 2, Temporal change 1), so per-category findings — including the 0% on close-value comparisons — rest on small samples.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also evaluates agents on real scientific data-analysis tasks including geographical information science, but unifies output to a self-contained Python program scored by execution rather than structured tool calls against a live API.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also grades scientific workflows with deterministic programmatic checks, but via pytest in containers across five domains rather than tool-call and keyword checks against a geospatial API.
- [SimulCost](./simulcost.md) — Also treats cost as a first-class axis of scientific-agent evaluation, but prices simulation time and experimental resources in physics parameter tuning rather than per-case dollar cost of API-driven analysis.