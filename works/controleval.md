# ControlAgent / ControlEval (2024)

> **English** | [简体中文](../zh/works/controleval.md)

## Overview

ControlEval is a benchmark of 500 control-system design tasks with varied design goals, released with ControlAgent — a multi-agent LLM system (central, task-specific, and Python-computation agents) that automates control design by iteratively tuning controller parameters and beats both LLM baselines and traditional toolbox-plus-human baselines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.19811>
- **Code:** <https://github.com/ControlAgent/ControlAgent>
- **Venue:** arXiv preprint (eess.SY), 2024

## Summary

Control-system design is iterative: propose a controller, check settling time and phase margin, retune. ControlAgent automates that loop with collaborative LLM agents — a central agent, task-specific design agents, and a Python computation agent — plus a history/feedback module. It is evaluated on ControlEval, a dataset of 500 control tasks spanning first- and second-order stable/unstable systems, systems with time delay, and higher-order systems, each with specific design goals (settling time, phase-margin robustness). ControlAgent maintains high success rates across system types and outperforms LLM-only and toolbox-plus-human baselines.

## Tasks

500 control-system design tasks (ControlEval) across first/second-order stable and unstable systems, time-delay systems, and higher-order systems, each with specific design criteria; the agents iteratively tune controllers — agentic, not static QA.

## Domains

Electrical Engineering — control-systems design: controller synthesis and tuning to meet stability and performance specifications.

## Evaluation

- Average Success Rate (ASR) and agent success rate (AgSR) against design criteria, versus LLM-based and traditional toolbox-plus-human baselines.
- **Reported.** ControlAgent maintains high success rates across system types (e.g., second-best result at 97.2% on first-order-with-delay), beating the baselines.

## Typical Duration

Iterative multi-agent design episodes per control task, with feedback-driven retuning.

## Main Contribution

Automating control-system design end to end with cooperating LLM agents — and a 500-task benchmark (ControlEval) that scores designs against real control specifications rather than free-form answers.

## Key Design Ideas

- A Python computation agent grounds the LLMs in actual control-theoretic calculation.
- The history/feedback module encodes the iterative retune loop control engineers use.
- ControlEval's task taxonomy spans the canonical system classes with graded difficulty.

## Strengths

- Beats toolbox-plus-human baselines, a strong bar in a mature engineering discipline.
- ControlEval's 500 specification-graded tasks make control design objectively scorable.

## Limitations

- Repository note: the paper's primary contribution is the ControlAgent framework; ControlEval is its paired benchmark, and this card centers the benchmark. The ControlEval dataset lives inside the ControlAgent repository (no separate release); no venue is stated in arXiv metadata.

## Related Works

- [AnalogXpert](./analogxpert.md) — Also an LLM agent for an electrical-design task, on analog circuit topology synthesis.
- [ElecBench](./elecbench.md) — Also an electrical-domain decision benchmark, on power-grid dispatch.
- [Frontier-Eng](./frontier-eng.md) — Also iterative engineering optimization under a simulator, across broader engineering tasks.
