# DSAgentBench (2026)

> **English** | [简体中文](../zh/works/dsagentbench.md)

> **First appeared:** 2026-08-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.10366)

## Overview

DSAgentBench is a benchmark that evaluates whether agents can automate complete end-to-end data-science workflows inside real computer environments, requiring coordinated use of tools such as notebooks, IDEs, terminals, browsers, and databases.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.10366
- **Venue:** arXiv preprint (submitted 11 Aug 2026)

## Summary

DSAgentBench targets long-horizon, real-world data-science practice that spans data wrangling, exploration, modeling, visualization, and validation. The authors state it is the first benchmark to evaluate whether agents can automate full data-science workflows inside real computer environments, in contrast to prior benchmarks that lack real-computer interaction and do not test complete end-to-end workflows. Each task requires grounding decisions in intermediate outputs and coordinating multiple tools, and is paired with a deterministic evaluator. Experiments across 15 closed- and open-source models reveal a large capability gap between current agentic systems and real data-science workflows.

## Tasks

275 diverse tasks covering the entire data-science life-cycle (data wrangling, exploration, modeling, visualization, and validation). Each task requires grounding decisions in intermediate outputs and coordinated use of tools such as notebooks, IDEs, terminals, browsers, and databases within real operating environments. Detailed task-construction methodology and per-stage task breakdown: TODO(reference).

## Domains

General data-science workflows conducted within real computer/operating environments (notebooks, IDEs, terminals, browsers, databases). The abstract does not enumerate specific scientific or application domains for the individual tasks; per-domain composition: TODO(reference).

## Evaluation

Each task includes a deterministic evaluator that verifies analytical correctness, visual outputs, and model performance, rather than checking code-only execution. Reported results: across 15 closed- and open-source models, the strongest agent, Claude-4.6-Sonnet, achieves 56.70% task success, while all open-source agents remain below 1%; reported failure modes include tool orchestration, OS grounding, and multi-step reasoning. Full metric definitions and per-model results: TODO(reference).

## Typical Duration

Described by the authors as long-horizon, multi-stage, multi-tool workflows. Concrete trajectory length, wall-clock time, or token budget per task: TODO(reference).

## Main Contribution

The authors present DSAgentBench as the first benchmark to evaluate whether agents can automate full end-to-end data-science workflows inside real computer environments, capturing the multi-stage, multi-tool nature of data-science practice that prior benchmarks omit, and pairing tasks with deterministic evaluators of analytical correctness, visual outputs, and model performance.

## Key Design Ideas

- Execution inside real computer environments with coordinated use of notebooks, IDEs, terminals, browsers, and databases, rather than isolated code snippets.
- Coverage of the entire data-science life-cycle: data wrangling, exploration, modeling, visualization, and validation.
- Tasks that require grounding decisions in intermediate outputs and multi-step tool orchestration.
- Deterministic evaluators that verify analytical correctness, visual outputs, and model performance instead of code-only execution.

## Strengths

- Evaluates complete, long-horizon data-science workflows in realistic computing environments rather than single-step or code-only tasks (abstract).
- Deterministic evaluation of analytical correctness, visual outputs, and model performance provides objective scoring beyond execution success (abstract).
- Broad empirical study spanning 15 closed- and open-source models (abstract).

## Limitations

- Repository note: The abstract does not specify the distribution of tasks across data-science life-cycle stages or application domains, task-construction provenance, or the exact evaluator metrics; these require the full paper to verify.
- Repository note: Reported evaluation names a model ("Claude-4.6-Sonnet") whose identifier is not verifiable against the primary source beyond the abstract text; the full model list and configuration require the full paper.

## Related Works

- [DSBench](./dsbench.md) — earlier data-science-agent benchmark on data analysis and modeling tasks; DSAgentBench extends the setting to full end-to-end workflows in real computer environments.
