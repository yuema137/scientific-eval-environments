# REFLECT / RoboFail (2023)

> **English** | [简体中文](../zh/works/robofail.md)

## Overview

REFLECT queries an LLM for robot failure explanation over a hierarchical summary of multisensory robot experiences, and its explanations guide a language-based planner to correct the failure; the paired RoboFail dataset provides tasks and failure scenarios for evaluating this failure-reasoning loop in simulation and the real world.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2306.15724>
- **Code:** <https://github.com/columbia-ai-robotics/reflect>
- **Project:** <https://robot-reflect.github.io/>
- **Venue:** CoRL 2023

## Summary

REFLECT converts a robot's raw multisensory record — vision, audio, proprioception — into a hierarchical experience summary an LLM can reason over, then runs a progressive failure-explanation algorithm to localize and explain what went wrong. The explanation is not the end product: it conditions a correction planner that produces an executable recovery plan. RoboFail supplies the evaluation substrate of tasks with injected failure scenarios, evaluated in both simulation and the real world.

## Tasks

Failure-explanation and correction episodes over robot task executions with a variety of tasks and failure scenarios (RoboFail); post-hoc explanation plus interactive correction replanning. Dataset size figures are TODO(reference) — not stated in the abstract or project page.

## Domains

Robotics — robot manipulation failure analysis over multisensory execution records, evaluated in simulation and on real-world robot tasks.

## Evaluation

- Quality of failure explanations and success of correction planning guided by them; specific metric names are not stated in the abstract or project page.
- **Reported.** REFLECT generates informative failure explanations that assist successful correction planning.

## Typical Duration

Post-hoc analysis over a completed (failed) execution, followed by a correction episode.

## Main Contribution

Establishing robot-failure explanation as an LLM reasoning task with a closed loop to recovery — the founding formulation the later failure-analysis benchmarks build on.

## Key Design Ideas

- Hierarchical experience summarization compresses multisensory streams into LLM-consumable structure.
- Progressive explanation narrows from summary level to the failure step.
- Explanations are graded by their downstream utility: does the correction plan work?

## Strengths

- Venue-verified early formulation; RoboFail became a reference evaluation set for successor systems.
- Covers both simulation and real-world executions.

## Limitations

- Repository note: the paper's primary contribution is the REFLECT framework; RoboFail is its paired dataset, and this card covers the dataset/benchmark side. No RoboFail size figures are verifiable from allowed sources — counts are TODO(reference).
- Repository note: card compiled from the arXiv abstract and official project materials (August 2026).

## Related Works

- [AHA](./aha.md) — Also robot-manipulation failure reasoning, scaled up via procedural failure generation.
- [RoboFAC](./robofac.md) — Also failure analysis and correction, at 78K-QA scale with a specialized model.
- [TRAJDEBUG](./trajdebug.md) — Also error localization in agent trajectories, for software agents.
