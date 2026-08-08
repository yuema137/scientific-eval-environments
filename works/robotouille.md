# Robotouille (2025)

> **English** | [简体中文](../zh/works/robotouille.md)

## Overview

Robotouille is an asynchronous planning benchmark for LLM agents: long-horizon cooking tasks where progress requires managing overlapping actions and interruptions — ReAct with GPT-4o achieves 47% on synchronous tasks but only 11% on asynchronous ones.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.05227>
- **Code:** <https://github.com/portal-cornell/robotouille>
- **Project:** <https://portal-cornell.github.io/robotouille/>
- **Venue:** ICLR 2025 (per the official repository and OpenReview; arXiv metadata carries no venue)

## Summary

Most planning benchmarks let an agent do one thing at a time. Robotouille's cooking environment does not: dishes require starting long-running actions (frying, boiling), doing other work while they complete, and reacting to interruptions. The benchmark ships 30 long-horizon scenarios across synchronous, asynchronous, and multi-agent settings, each backed by 10 tasks with 10 procedurally generated instances (official repository). The synchronous-to-asynchronous drop — 47% to 11% for ReAct (GPT-4o) — isolates time-overlap handling as a distinct, unsolved capability, and the paper attributes failures to weak long-horizon feedback incorporation and lack of self-auditing.

## Tasks

30 long-horizon planning scenarios (synchronous, asynchronous, multi-agent), each a curated dataset of 10 tasks × 10 procedurally generated instances; the LLM agent plans and acts in the cooking simulator. Simulation only.

## Domains

Simulated cooking environment — outside the repository's science/engineering domain axis; documented for its evaluation methodology.

## Evaluation

- Task success rate per setting (synchronous / asynchronous / multi-agent), with failure-mode analysis.
- **Reported.** ReAct (GPT-4o): 47% synchronous vs. 11% asynchronous; smaller models near zero on asynchronous tasks.

## Typical Duration

Long-horizon episodes with concurrent, temporally overlapping actions.

## Main Contribution

Isolating asynchrony as the measured variable: identical planning machinery loses three-quarters of its success rate the moment actions overlap in time.

## Key Design Ideas

- Long-running actions with completion delays make time management, not just ordering, the challenge.
- Procedural instance generation gives each scenario statistical depth.
- Matched synchronous/asynchronous task sets turn the comparison into a controlled experiment.

## Strengths

- The cleanest published isolation of asynchronous-planning weakness in LLM agents.
- Fully public stack with procedural generation for contamination resistance.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the ICLR 2025 venue is stated by the repository and OpenReview, not arXiv metadata. Scenario counts come from the repository.
- Simulation-only; the "robot" is abstract — no physical platform.

## Related Works

- [Gaia2](./gaia2.md) — Also injects temporal events and asynchrony into agent evaluation, in a mobile-environment setting.
- [LoTa-Bench](./lota-bench.md) — Also execution-scored LLM planning, in the synchronous regime.
- [PARTNR](./partnr.md) — Also coordination under concurrency, with human partners rather than parallel actions.
