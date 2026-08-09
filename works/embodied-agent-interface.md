# Embodied Agent Interface (2024)

> **English** | [简体中文](../zh/works/embodied-agent-interface.md)

## Overview

Embodied Agent Interface (EAI) benchmarks LLMs for embodied decision making by decomposing the problem into four modules — goal interpretation, subgoal decomposition, action sequencing, and transition modeling — and scoring each against simulator states in VirtualHome and BEHAVIOR with a fine-grained error taxonomy.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2410.07166>
- **Code:** <https://github.com/embodied-agent-eval/embodied-agent-eval>
- **Project:** <https://embodied-agent-interface.github.io/>
- **Dataset:** <https://huggingface.co/datasets/Inevitablevalor/EmbodiedAgentInterface>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks Track (oral), 2024

## Summary

Instead of scoring an embodied agent only on end-task success, EAI standardizes the interface to each decision-making module an LLM might implement and evaluates them separately: interpreting goals, decomposing subgoals, sequencing actions, and modeling transitions. Errors are broken down into types — hallucination errors, affordance errors, and various planning errors — so failures localize to a module and a cause. Per the official project page, the suite covers VirtualHome (26 task categories, 338 instructions) and BEHAVIOR (100 task categories), with 18 LLMs evaluated over 338 trajectories.

## Tasks

Module-level evaluation over VirtualHome and BEHAVIOR tasks: each LLM output is checked against simulator states per module rather than run as a free agent loop; 338 trajectories with roughly 4,420 steps (official project page).

## Domains

Embodied household simulation — outside the repository's science/engineering domain axis; documented for its evaluation methodology.

## Evaluation

- Fine-grained metrics per module with a typed error taxonomy: hallucination errors, affordance errors, and multiple planning-error types, all checked against simulator state.
- **Reported.** No headline numbers in the abstract; 18 LLMs evaluated per the project page.

## Typical Duration

Per-module queries over recorded task trajectories; not a free-running episode.

## Main Contribution

The ability-decomposed alternative to end-to-end embodied scoring: a standardized interface that turns "the agent failed" into "which module failed, with which error type."

## Key Design Ideas

- Four-module decomposition mirrors the architecture of most LLM embodied stacks, so scores transfer to system design.
- Typed errors (hallucination vs. affordance vs. planning) separate knowledge failures from grounding failures.
- Simulator-state checking keeps module grading objective without an LLM judge.

## Strengths

- Venue-verified oral with full public stack; the de facto reference for modular embodied-LLM evaluation.
- The error taxonomy transfers to any embodied pipeline, not just the two simulators used.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); scale figures come from the project page, not the abstract.
- Module-decomposed rather than closed-loop: interactions between modules are outside the measured object.

## Related Works

- [LoTa-Bench](./lota-bench.md) — Also LLM embodied planning evaluation, scored end-to-end by executed goal satisfaction.
- [TRAJDEBUG](./trajdebug.md) — Also typed error analysis over agent trajectories, for tool-use and coding agents.
- [EmbodiedBench](./embodiedbench.md) — Also capability-decomposed embodied evaluation, for vision-driven MLLM agents.
