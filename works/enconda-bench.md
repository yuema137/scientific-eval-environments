# Enconda-bench (2025)

## Overview

Enconda-bench (Environment Configuration Diagnosis Benchmark) evaluates software-engineering agents at the process level on environment configuration — a bottleneck where end-to-end build/test benchmarks obscure where and why agents fail.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.25694>

## Summary

Enconda-bench provides process-level trajectory assessment of software-engineering agents during environment setup. Rather than only scoring end-to-end build or test success, it evaluates fine-grained capabilities — planning, error diagnosis, repair, and execution — across the configuration process. Task instances are automatically constructed by injecting realistic README errors and validated in Docker.

## Tasks

Automatically constructed task instances built by injecting realistic README errors and validated in Docker. Exact task count: TODO(reference).

## Domains

Environment configuration for software-engineering agents.

## Evaluation

Process-level trajectory assessment across four capability subprocesses:

- Planning
- Error diagnosis
- Repair
- Execution

Validated in Docker containers. Reported: agents can localize errors but struggle to translate feedback into effective corrections.

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
