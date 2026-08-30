# RE-Bench (2024)

> **English** | [简体中文](../zh/works/re-bench.md)

> **First appeared:** 2024-11-22 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2411.15114)

## Overview

RE-Bench (Research Engineering Benchmark, v1) evaluates the frontier AI R&D capabilities of language-model agents against human experts: 7 open-ended ML research-engineering environments with reference solutions, plus data from 71 eight-hour attempts by 61 human experts — with agents outscoring humans 4x at a 2-hour budget but humans winning 2x by 32 hours.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.15114>
- **Code:** <https://github.com/metr/ai-rd-tasks>
- **Venue:** arXiv preprint (cs.LG), 2024

## Summary

RE-Bench, from METR, is built to compare agents against human experts on real AI R&D. Its 7 open-ended ML research-engineering environments — writing and optimizing code, custom kernels, fine-tuning scripts — are scored against strong reference solutions, and it ships data from 71 eight-hour attempts by 61 distinct human experts (82% achieving a non-zero score, 24% matching or exceeding the reference). The time-budget comparison is its signature result: the best AI agents score 4x higher than experts at a 2-hour budget, but humans reach 2x the top agent's score by 32 hours — and in one case an agent wrote a faster custom Triton kernel than any human expert.

## Tasks

7 open-ended ML research-engineering environments (code/kernel optimization, fine-tuning); agents and humans are scored against reference solutions under 2/8/32-hour time budgets. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — AI R&D / research engineering: optimizing code and models on open-ended research tasks.

## Evaluation

- Best-of-k scoring against reference solutions under time budgets; direct comparison to human-expert data.
- **Reported.** Agents 4x experts at 2h; humans 2x the top agent at 32h; 82% of expert attempts non-zero, 24% match/exceed the reference.

## Typical Duration

Long-horizon episodes under explicit multi-hour time budgets (2/8/32 hours).

## Main Contribution

A human-anchored, time-budgeted benchmark for frontier AI R&D — quantifying not just whether agents can do research engineering but how their speed and ceiling compare to experts across time.

## Key Design Ideas

- Open-ended optimization tasks with reference solutions measure real R&D progress.
- Large human-expert dataset (71 attempts) enables direct, calibrated comparison.
- Time-budget sweeps expose the agents-fast-but-humans-scale dynamic.

## Strengths

- One of the most rigorous human-vs-agent AI-R&D comparisons, fully open-sourced (environments, human data, trajectories).
- The time-budget finding is a widely cited capability-trajectory result.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is stated in arXiv metadata (METR is the org). The abstract states 7 environments while the repository lists 8 task families — the abstract figure is used here.

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — Also human-anchored ML research evaluation, on competition tasks.
- [MLGym](./mlgym.md) — Also open-ended AI-research tasks in a Gym environment.
- [MLAgentBench](./mlagentbench.md) — Also improve-the-metric ML experimentation, without the human-expert comparison.
