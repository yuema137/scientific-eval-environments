# LoopsBench (2026)

> **English** | [简体中文](../zh/works/loopsbench.md)

> **First appeared:** 2026-07-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.00267)

## Overview

LoopsBench is a long-horizon benchmark for evaluating coding agents on "loop engineering" — sustained, multi-step software development — where each task is a dependency DAG over separately testable development units with source-evidenced prerequisite edges.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General-purpose software-engineering (long-horizon 'loop engineering') benchmark across generic repos; excluded as general application software engineering.

## Links

- **Paper:** https://arxiv.org/abs/2608.00267
- **Project:** https://loopsbench.ai
- **Code:** https://github.com/microsoft/Loopsbench
- **Venue:** arXiv preprint (2026)

## Summary

LoopsBench targets the shift in coding-agent infrastructure from harness engineering toward loop engineering, arguing that existing benchmarks center on localized tasks or end-state outcomes and give limited insight into sustained execution. Each task is modeled as a dependency DAG whose nodes are separately testable development units connected by source-evidenced prerequisite edges. A flow-aware runtime releases tests along the "ready frontier" as prerequisites are satisfied and retains completed nodes as regression obligations, so an agent must both make forward progress and avoid breaking earlier work. The authors evaluate frontier coding agents paired with widely used loop implementations.

## Tasks

112 tasks drawn from authentic sources, spanning 8 programming languages and 9 domains, comprising more than 5,300 development units with executable tests. Each task is a dependency DAG over separately testable development units, with prerequisite edges recovered from source evidence.

## Domains

Software development across 8 programming languages and 9 domains (specific domain names: `TODO(reference)`). The benchmark evaluates coding agents on sustained software-engineering work.

## Evaluation

Execution-based scoring via a flow-aware runtime: tests are released along the ready frontier as prerequisites are completed, and completed nodes are retained as regression obligations so that regressions are detected. Per the official repository, verification is Docker-backed with verifiers that distinguish incomplete, partial, and complete solutions, and each task carries an oracle run used by maintainers to verify it before publication. Analyses additionally compare recorded agent plans against the source-recovered prerequisite DAG.

## Typical Duration

`TODO(reference)` — the paper frames tasks as long-horizon/sustained execution but a specific per-task trajectory length, wall-clock time, or token budget is not extracted here.

## Main Contribution

A long-horizon benchmark for loop engineering in coding-agent evaluation, structured as source-evidenced dependency DAGs of separately testable development units with a flow-aware runtime that releases tests along the ready frontier and treats completed nodes as regression obligations.

## Key Design Ideas

- Task = dependency DAG over separately testable development units, with prerequisite edges evidenced from source.
- Flow-aware runtime that releases tests along the "ready frontier" as prerequisites are satisfied.
- Completed nodes retained as regression obligations, exposing regressions during sustained execution.
- Evaluation of frontier coding agents paired with widely used loop implementations (e.g., outer-continuation loops).
- Comparison of recorded agent plans against the source-recovered prerequisite DAG.

## Strengths

- Large-scale executable substrate: 112 tasks and more than 5,300 development units with executable tests (paper).
- Breadth across 8 programming languages and 9 domains (paper).
- Explicitly measures regression during long-horizon execution rather than only end-state outcomes (paper).
- Open-sourced benchmark data and code under the MIT license, with Docker-backed verification and adapters for multiple agents/loops (official repository).

## Limitations

- The strongest evaluated configuration (Opus-4.7 with Claude Code and outer continuation) resolves 25.00% of tasks, indicating substantial headroom (paper).
- Recorded plans recover only part of the source-recovered prerequisite DAG, and regression events remain visible across the evaluated loop profiles (paper).
- Repository note: the specific names of the 9 domains and the per-task duration/budget are not extracted here and are marked `TODO(reference)`.

## Related Works

- [SWE-bench Pro-Max](./swe-bench-promax.md) — another long-horizon coding-agent benchmark emphasizing execution-based evaluation of software tasks.
