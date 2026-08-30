# Simona (2026)

> **English** | [简体中文](../zh/works/simona.md)

> **First appeared:** 2026-01-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2601.06776)

## Overview

Simona is a dataset of 1,000 expert-written chemical process descriptions, introduced as the evaluation set for a multi-agent LLM workflow that converts natural-language process descriptions into executable, converging process-simulation flowsheets. Systems are scored by Simulation Convergence Rate and design time against LLM, multi-agent, and human-expert baselines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.06776>

## Summary

The paper targets the step between a process flow diagram and a working simulation: converting a described process into a configured flowsheet that actually converges inside a simulator, which the authors characterize as a labor-intensive, parameter-heavy manual task. The proposed system uses four specialized agents — semantic interpretation, topology development, configuration tuning, and outcome assessment — augmented with an Enhanced Monte Carlo Tree Search to stabilize semantic parsing and configuration generation, and interacts repeatedly with a process simulator over HTTP APIs. Evaluation is conducted on Simona, a self-constructed corpus of process descriptions, with convergence rate and design time as the headline metrics.

## Tasks

Each task presents a written chemical process description; the system must produce a simulation flowsheet — topology plus unit-operation configuration — that runs to convergence in the process simulator. The paper states: "Our experiments are conducted on a self-constructed dataset called Simona, consisting of 1000 process descriptions carefully designed by chemical engineering experts." Descriptions vary along two axes: the difficulty of the unit operations involved (mixers, distillation columns, and others, i.e. the nodes of a flowsheet) and the level of detail given in the description.

## Domains

Chemical Engineering. The evaluated objective is process simulation and flowsheet design — selecting and connecting unit operations such as mixers and distillation columns and tuning their operating configuration until the flowsheet converges — which is squarely process systems engineering rather than chemistry. No co-domain is assigned: the tasks concern process topology and simulator configuration, not molecular or reaction-level chemistry.

## Evaluation

The primary metric is the Simulation Convergence Rate (SCR), "defined as the ratio of successfully converged process designs to total requirements," reported alongside design time in seconds. Designs are additionally scored on five dimensions: economic feasibility, environmental sustainability, process safety, technical feasibility, and topological rationality. Simulation is performed by an in-house tool — "For chemical process simulation, we integrate with our self-developed chemical process simulation software through HTTP APIs" — rather than a commercial package.

Reported results: the proposed method reaches 80.3% SCR, against GPT-4o at 23.4% SCR / 86.13 s, MetaGPT at 49.2% SCR / 612.33 s, and expert manual design at 100% SCR / 8,301.91 s. The abstract summarizes this as a 31.1% improvement in simulation success rate over baselines and an 89.0% reduction in design duration relative to manual expert work. GPT-4o is the primary backbone evaluated, with a comparison against Claude Sonnet 4.

## Typical Duration

Design time per process description is reported directly as an efficiency metric: 86.13 s for the GPT-4o baseline, 612.33 s for MetaGPT, and 8,301.91 s for expert manual design, with the proposed method reported as 89.0% faster than the manual baseline. Token budgets and agent step counts are not reported.

## Main Contribution

In the authors' framing, the contribution is an end-to-end multi-agent system that closes the gap from written process descriptions to computationally confirmed simulation setups, combining four role-specialized agents with Enhanced Monte Carlo Tree Search for reliable semantic parsing and configuration generation, together with the Simona description corpus and the convergence-based evaluation used to demonstrate it.

## Key Design Ideas

- Convergence-based scoring: a design counts only if the resulting flowsheet actually converges in the simulator, making the metric execution-verified rather than similarity-based.
- Role decomposition into four agents — semantic interpretation, topology development, configuration tuning, and outcome assessment — mirroring the manual flowsheeting workflow.
- Enhanced Monte Carlo Tree Search over the configuration space, with an ablation over the number of child nodes per expansion (2, 3, 4, and 5).
- Simulator access through HTTP APIs, allowing repeated agent-simulator interaction loops instead of one-shot generation.
- A human-expert baseline included in the comparison table, providing an upper reference point (100% SCR) for both quality and time.
- Task variation deliberately spans both unit-operation difficulty and description detail level, separating parsing difficulty from engineering difficulty.

## Strengths

- Success is execution-verified: a design counts only when the flowsheet converges in the simulator, so the metric cannot be satisfied by output that merely looks like a plausible flowsheet.
- At 1,000 expert-written process descriptions, the corpus is substantially larger than the handful of case studies typical of flowsheet-generation papers.
- Task difficulty is varied along two separable axes — unit-operation complexity and description detail — so parsing difficulty can be distinguished from engineering difficulty.
- The comparison includes a human-expert baseline (100% SCR, 8,301.91 s), giving both quality and time an interpretable upper reference rather than only model-to-model contrasts.
- Design time is reported alongside convergence rate, making efficiency an explicit second axis rather than an unmeasured side effect.

## Limitations

- The paper does not state that Simona is publicly released, and gives no dataset URL or license; the corpus is described only as self-constructed.
- Simulation relies on the authors' own self-developed simulation software accessed over HTTP, so results cannot be reproduced against a standard tool such as Aspen Plus, HYSYS, or DWSIM.
- Model coverage is narrow: GPT-4o as the primary backbone with a Claude Sonnet 4 comparison.
- The five design-quality dimensions (economic feasibility, environmental sustainability, process safety, technical feasibility, topological rationality) are reported as scores without a published rubric or grader-agreement analysis in the paper.
- Repository note: the dataset is introduced as the evaluation vehicle for the authors' own system, so all reported baselines are run by the proposing authors rather than by independent submissions.

## Related Works

- [CeProBench](./ceprobench.md) — chemical-process-development benchmark whose Concept and Parameter dimensions cover the same description-to-flowsheet and parameter-configuration steps, scored through Aspen Plus.
- [FEABench](./feabench.md) — engineering benchmark where success is defined by driving a commercial simulator through its API to a valid result.
- [CFDLLMBench](./cfdllmbench.md) — simulation-configuration benchmark using execution in OpenFOAM as the success criterion.
