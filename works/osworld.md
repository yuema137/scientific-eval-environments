# OSWorld (2024)

## Overview

OSWorld is a scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across Ubuntu, Windows, and macOS. It provides 369 real computer tasks spanning web and desktop applications, OS file I/O, and multi-application workflows.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2404.07972>
- **Code:** <https://github.com/xlang-ai/OSWorld>

## Summary

OSWorld addresses the limitation that existing benchmarks either lack an interactive environment or are confined to specific applications or domains, failing to reflect the diversity of real-world computer use. It introduces a first-of-its-kind scalable, real computer environment for multimodal agents that supports task setup, execution-based evaluation, and interactive learning across multiple operating systems. Across 369 real computer tasks, humans accomplish over 72.36% while the best model achieves only 12.24%.

## Tasks

369 real computer tasks involving real web and desktop applications, OS file I/O, and multi-application workflows.

## Domains

Open-ended real computer use across operating systems: Ubuntu, Windows, and macOS.

## Evaluation

- Each task includes a detailed initial-state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation.
- Reported: humans accomplish over 72.36% of tasks; the best model achieves 12.24%.

## Typical Duration

Open-ended, multi-application workflows per task. Per-task step/time budget: TODO(reference) — not stated in the abstract.

## Main Contribution

A scalable real-computer environment for multimodal agents with per-task setup and execution-based reward scripts, enabling reproducible open-ended evaluation across operating systems.

## Key Design Ideas

- Real operating-system environments (Ubuntu, Windows, macOS) rather than app-specific sandboxes.
- Per-task initial-state setup plus custom execution-based evaluation scripts for reproducibility.
- Open-ended, multi-application task workflows.
- Supports interactive learning as well as evaluation.

## Strengths

- Reflects real, diverse computer use rather than a single application domain.
- Execution-based per-task scripts give reproducible, objective grading.
- Large human-model gap (72.36% vs. 12.24%) signals substantial headroom.

## Limitations

- Repository note: Per-task duration and step budgets are not stated in the abstract and are marked `TODO(reference)`.

## Related Works

- [WebArena](./webarena.md) — Also an interactive, execution-evaluated environment, but limited to web sites rather than whole operating systems.
- [GAIA](./gaia.md) — Also evaluates general assistant capability, but via answer correctness rather than execution inside a computer environment.
