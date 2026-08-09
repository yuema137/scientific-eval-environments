# CaP-X (2026)

> **English** | [简体中文](../zh/works/cap-x.md)

## Overview

CaP-X benchmarks and improves coding agents for robot manipulation: agents control robots by synthesizing and executing programs that compose perception and control primitives, evaluated in CaP-Bench across levels of abstraction, interaction, and perceptual grounding — 12 frontier models show performance that improves with human-crafted abstractions and degrades as those priors are removed.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2603.22435>
- **Project:** <https://capgym.github.io>
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

CaP-X packages the Code-as-Policies paradigm into a measurable framework with four parts: CaP-Gym (the interactive environment), CaP-Bench (the benchmark), and two methods — training-free CaP-Agent0 and CaP-RL with verifiable rewards. The benchmark core holds 7 manipulation tasks (from cube lifting to two-arm handover), extended by 30 LIBERO-PRO and 2 BEHAVIOR tasks, within a 187-task CaP-Gym suite (paper body). Coding agents work multi-turn with structured execution feedback and visual differencing. Across 12 models the consistent trend is dependence on designer scaffolding: success falls as human-crafted abstraction layers are stripped away. Human experts average 88.5% single-turn success on the low-level tier; the paired methods recover human-level reliability on several tasks in simulation and on real Franka Panda and AgiBot G1 embodiments.

## Tasks

Interactive code-synthesis episodes: the agent writes Python programs over perception/control primitives, executes them, and revises from feedback; benchmark evaluation in simulation (Robosuite, LIBERO-PRO, BEHAVIOR) with 100 trials per task per tier; the paired methods additionally run on real robots.

## Domains

Robotics — robot-manipulation control via agent-written programs, benchmarked in simulation with sim-to-real transfer of the paired methods to physical Franka Panda and AgiBot G1 platforms.

## Evaluation

- Success rate over 100 trials per task and tier; zero-shot pass@1; comparison against human expert-written programs under identical environments (human 88.5% average on the low-level-primitive tier).
- **Reported.** Performance improves with human-crafted abstractions and degrades as priors are removed (abstract); project page: frontier models >30% zero-shot; CaP-RL lifts Qwen2.5-Coder from 20% to 72%.

## Typical Duration

Multi-turn synthesize-execute-revise episodes per manipulation task.

## Main Contribution

Measuring the scaffolding dependence of coding-agent robotics: tiered abstraction levels quantify how much of current "LLMs can control robots" rests on human-designed primitives.

## Key Design Ideas

- Abstraction tiers make designer priors an experimental variable rather than a hidden constant.
- Structured execution feedback and visual differencing give the agent the observability a roboticist would have.
- Human expert-written programs anchor the ceiling under identical conditions.

## Strengths

- The tier design yields a causal-style finding about scaffolding, not just a leaderboard.
- Covers 12 current frontier and open models with real-robot transfer of the paired methods.

## Limitations

- Repository note: card compiled from the arXiv abstract, paper body, and official project page (August 2026); no venue is verifiable (the HTML shows ICML formatting, which indicates submission, not acceptance). Benchmark and methods are co-primary contributions; task counts come from the paper body. The exact code-repository URL is not verifiable from fetched sources.

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — Also LLMs producing executable robot behavior, through dialog and waypoints rather than programs.
- [ManipBench](./manipbench.md) — Also low-level manipulation competence, measured as static reasoning rather than executed code.
- [BadRobot](./badrobot.md) — Also evaluates Code-as-Policies-style embodied stacks, adversarially.
