# Enconda-bench (2025)

> **English** | [简体中文](../zh/works/enconda-bench.md)

## Overview

Enconda-bench (Environment Configuration Diagnosis Benchmark) evaluates software-engineering agents at the process level on environment configuration — a bottleneck where end-to-end build/test benchmarks obscure where and why agents fail.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.25694>

## Summary

Enconda-bench provides process-level trajectory assessment of software-engineering agents during environment setup. Rather than only scoring end-to-end build or test success, it evaluates fine-grained capabilities — planning, error diagnosis, repair, and execution — across the configuration process. Task instances are automatically constructed by injecting realistic README errors and validated in Docker.

## Tasks

4,201 erroneous-README tasks (9,471 injected errors in total) across 323 source repositories, each pinned to a fixed commit. Construction funnel: 1,772 two-error READMEs → 1,230 Docker-validated (LLM–human agreement 98.5%) → split and merged into 4,201 READMEs carrying 1–10+ errors, stratified into difficulty levels 1–10.

## Domains

Environment configuration for software-engineering agents.

## Evaluation

Process-level scoring across four capabilities (the paper's Planning, Perception, Feedback, Action), reported as separate metric groups rather than one composite score:

- **Perception (error diagnosis)** — predicted error types (from six canonical categories) are matched against the gold set; reported as **Precision / Recall / F1**, since a README may contain multiple errors.
- **Feedback (repair)** — each predicted **error description** and **fix suggestion** is matched to gold and judged by GPT-4.1-mini for consistency, giving two **accuracy** scores.
- **Planning + Action (execution)** — the extracted shell script runs in a Docker container on a fixed commit, scored by **Pass@1**: a pass requires the environment to build, the test files to execute, and the process to exit normally.

**Error-injection validation.** An injected error counts as effective only if setup fails with it and proceeds once it is repaired; a deliberately weak model (GPT-4.1-mini) generates and runs the setup script so that a stronger model cannot implicitly auto-fix errors and undermine validity — followed by LLM filtering and human validation (98.5% agreement).

Reported (best configuration, Repo2Run + Claude-4): error-type F1 = 60.6, description accuracy = 52.2, fix accuracy = 47.3, Pass@1 = 22.9. The gap between fix accuracy (47.3) and Pass@1 (22.9) is the paper's evidence that agents can localize errors but struggle to translate feedback into working corrections.

## Typical Duration

Multi-step configuration workflows; specific duration not stated in the abstract.

## Main Contribution

A process-level trajectory evaluation of software-engineering agents on environment configuration, with automatic task construction via realistic error injection.

## Key Design Ideas

- Process-level evaluation across four capability subprocesses (planning / diagnosis / repair / execution).
- Automatic task construction via error injection into real README files.
- Docker-based deterministic validation.

## Strengths

- Automatic task construction scales without heavy manual annotation.
- Docker execution provides deterministic verification.
- Process decomposition surfaces where agents fail (diagnosis vs. repair vs. execution).

## Limitations

- Repository note: Scoped to environment configuration — does not evaluate other software-engineering activities such as code authoring or architectural design.

## Related Works

- [T-Eval](./t-eval.md) — Also decomposes evaluation into capability subprocesses, but for tool use rather than environment configuration.
- [AgentBoard](./agentboard.md) — Also process-level trajectory evaluation, via annotated subgoals rather than error-injection-constructed tasks.
