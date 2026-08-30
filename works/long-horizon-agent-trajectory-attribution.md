# Long-Horizon Agent Trajectory Attribution (2026)

> **English** | [简体中文](../zh/works/long-horizon-agent-trajectory-attribution.md)

> **First appeared:** 2026-08-07 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.06909)

## Overview

A benchmark and fine-grained annotation framework for *trajectory attribution* — identifying which component of a long-horizon LLM-agent trajectory (user instructions, tool calls, observations, memory, etc.) is primarily responsible for an observed outcome such as a task-aligned action, an unsafe action, or a safety refusal.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities


N/A — Trajectory-attribution / diagnosis methodology over arbitrary agent trajectories (AgentDojo, Agent3Sigma); operates on trajectories, not a scientific/research task.

## Links

- **Paper:** https://arxiv.org/abs/2608.06909
- **Code:** https://github.com/chenjing-2024/agent-trajectory-attribution
- **Venue:** arXiv preprint (2026)

## Summary

Existing agent benchmarks mainly evaluate behavioral outcomes and offer limited support for fine-grained attribution analysis. This work introduces the task of trajectory attribution and builds a benchmark plus annotation framework for it. Heterogeneous agent trajectories are organized under a unified component schema, and each trajectory is annotated with its primary attribution component together with attack and execution chains where applicable. The benchmark is instantiated with trajectories drawn from AgentDojo and from the Stage and Canary settings of Agent3Sigma, and defines two evaluation tasks with reference baselines. The authors also release a reusable annotation skill so that trajectories from new agent models can be standardized and annotated under the same attribution framework.

## Tasks

The benchmark comprises **1,351 annotated trajectories**.

By source:
- AgentDojo: 640 trajectories
- Agent3Sigma (Stage setting): 495 trajectories
- Agent3Sigma (Canary setting): 216 trajectories

By outcome category:
- Task-aligned actions: 409 (30.3%)
- Unsafe actions: 532 (39.4%)
- Safety refusals: 410 (30.3%)

Trajectories are organized under a unified component schema in which each component has a *role* (system, user, assistant, or tool) and *content* (user instructions, reasoning traces, tool calls, tool observations, retrieved memory, and final actions); tool calls and their observations are treated as composite units. Each trajectory is annotated with its primary attribution component, and with attack and execution chains where applicable.

Two evaluation tasks are defined:
- **Primary attribution localization** — identify the annotated root-cause component.
- **Attribution-chain recovery** — recover additional components beyond the primary cause that form the attribution chain.

## Domains

N/A — the benchmark evaluates general LLM-agent trajectories (tool-using agents from AgentDojo and the Agent3Sigma safety settings) rather than a scientific or engineering field.

## Evaluation

The two tasks are scored with ranking metrics: primary attribution localization uses **Hit@1** and **Mean Reciprocal Rank (MRR)**; attribution-chain recovery uses **Recall@K** and **Mean Average Precision (MAP)**.

Two reference baselines are provided:
- **Incremental (trajectory contribution)** — scores components by the likelihood change as the trajectory unfolds.
- **Leave-One-Out (component-level perturbation)** — estimates a component's importance by the effect of removing it.

Reported micro-averaged results across all targets: Incremental — Hit@1 = 0.369, MRR = 0.616; Leave-One-Out — Hit@1 = 0.537, MRR = 0.713. The paper notes substantial performance differences across attribution settings (local, long-range, and structured-chain attribution), giving an initial characterization of the benchmark's difficulty.

## Typical Duration

Reported mean trajectory lengths range from 6.58 to 21.69 components, with the longest trajectories reaching up to 97 components. The attribution distance (separation between the primary component and the target) averages 2.41–3.93 components, with maxima up to 23 components.

## Main Contribution

Introduces trajectory attribution as an evaluation task for long-horizon LLM agents, and provides a unified component schema, a fine-grained annotation framework, a benchmark of 1,351 annotated trajectories, two evaluation tasks with reference baselines, and a reusable annotation skill for extending the benchmark to trajectories from new agent models.

## Key Design Ideas

- **Unified component schema** that represents heterogeneous agent trajectories (instructions, tool calls/observations, memory, configuration, skill context) with role/content fields, treating tool call–observation pairs as composite units.
- **Primary-component annotation plus attack and execution chains**, distinguishing a single root cause from the broader chain of contributing components.
- **Two attribution tasks** (localization and chain recovery) scored with ranking metrics (Hit@1, MRR, Recall@K, MAP).
- **Perturbation- and likelihood-based baselines** (incremental contribution and leave-one-out) as reference attribution methods.
- **Coverage of diverse attribution settings** — local, long-range, and structured-chain attribution across task-aligned, unsafe, and refusal outcomes.
- **Reusable annotation skill** operationalizing the construction protocol so new agent-model trajectories can be standardized and annotated consistently.

## Strengths

- Provides fine-grained, component-level attribution annotations that go beyond outcome-only agent benchmarks (per paper).
- Spans multiple trajectory sources and outcome types (task-aligned, unsafe, safety refusals), enabling attribution analysis across both benign and safety-relevant behaviors (per paper).
- Ships an extensible annotation protocol/skill intended to standardize trajectories generated by new agent models (per paper).

## Limitations

- Reference baselines show substantial performance gaps across attribution settings, indicating attribution — especially long-range and structured-chain cases — remains challenging (per paper).
- Repository note: the benchmark is instantiated from two upstream sources (AgentDojo and Agent3Sigma) and centers on tool-use safety/security trajectories; coverage of other agent settings depends on future use of the released annotation skill.

## Related Works

- [MLE-Dojo](./mle-dojo.md) — another agent evaluation environment, but focused on machine-learning engineering tasks rather than trajectory-level attribution.
