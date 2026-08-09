# LoTa-Bench (2024)

> **English** | [简体中文](../zh/works/lota-bench.md)

## Overview

LoTa-Bench benchmarks language-oriented task planners for embodied agents with fully automated scoring: LLM-generated plans are executed in simulators and graded on goal satisfaction, over two dataset-simulator pairs — ALFRED on AI2-THOR and an extended Watch-And-Help on VirtualHome.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2402.08178>
- **Code:** <https://github.com/lbaa2022/LLMTaskPlanning>
- **Venue:** ICLR 2024

## Summary

Before LoTa-Bench, comparing LLM task planners meant human plan inspection. LoTa-Bench closes the loop: the LLM proposes a skill sequence for a home-service instruction, the simulator executes it, and success is measured automatically against goal conditions — enabling systematic sweeps over model choice and prompt design across two independent dataset-simulator stacks.

## Tasks

Home-service task-planning episodes on two pairs: ALFRED instructions in AI2-THOR and extended Watch-And-Help instructions in VirtualHome; the LLM plans over a skill library and plans run in simulation. Task counts are TODO(reference) — not stated in the abstract.

## Domains

Embodied household simulation — outside the repository's science/engineering domain axis; documented for its evaluation methodology.

## Evaluation

- Automated execution-based scoring: plans run in the simulator and are graded on goal satisfaction, replacing human plan inspection.
- **Reported.** No headline numbers in the abstract; the paper sweeps multiple LLMs and prompt configurations.

## Typical Duration

Single planning episode per instruction, executed to completion in simulation.

## Main Contribution

Making LLM task-planner comparison automatic and reproducible — execution-verified benchmarking where prior practice was qualitative inspection.

## Key Design Ideas

- Two independent simulator stacks guard conclusions against simulator idiosyncrasies.
- Skill-library planning isolates the language-to-plan step from low-level control.
- Automated goal checking makes prompt/model ablations cheap enough to run at scale.

## Strengths

- An early, venue-verified standard for execution-based LLM planner evaluation.
- The two-stack design became a template for later embodied benchmarks.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); task and model counts await full-paper validation.
- Simulation-only; no physical robot platform.

## Related Works

- [Embodied Agent Interface](./embodied-agent-interface.md) — Also LLM embodied decision-making evaluation, decomposed into modules with an error taxonomy.
- [EmbodiedBench](./embodiedbench.md) — Also multi-environment embodied evaluation, extended to vision-driven MLLM agents.
- [Robotouille](./robotouille.md) — Also LLM planning evaluation, stressing asynchronous overlapping tasks.
