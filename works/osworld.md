# OSWorld (2024)

> **English** | [简体中文](../zh/works/osworld.md)

> **First appeared:** 2024-04-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2404.07972)

## Overview

OSWorld is a scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across Ubuntu, Windows, and macOS. It provides 369 real computer tasks spanning web and desktop applications, OS file I/O, and multi-application workflows.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2404.07972>
- **Code:** <https://github.com/xlang-ai/OSWorld>

## Summary

OSWorld addresses the limitation that existing benchmarks either lack an interactive environment or are confined to specific applications or domains, failing to reflect the diversity of real-world computer use. It introduces a first-of-its-kind scalable, real computer environment for multimodal agents that supports task setup, execution-based evaluation, and interactive learning across multiple operating systems. Across 369 real computer tasks, humans accomplish over 72.36% while the best model achieves only 12.24%.

## Tasks

369 real computer tasks. By category: OS 24, Office (Calc/Impress/Writer) 117, Daily (Chrome/VLC/Thunderbird) 78, Professional (VS Code/GIMP) 49, and multi-app Workflow 101 (27.4%). 30 tasks are infeasible (the agent must correctly predict failure); the suite spans 302 distinct initial states.

## Domains

Open-ended real computer use across operating systems: Ubuntu, Windows, and macOS.

## Evaluation

- **Execution-based reward R ∈ [0, 1].** A per-task reward is awarded at the final step — 1, or a positive decimal for partial achievement, or a positive value for correctly predicting an infeasible task; 0 otherwise — so scoring is not strictly binary, though most tasks are pass/fail. The reported metric is Success Rate, the mean R over the suite.
- **A per-task JSON config drives four phases:** (1) initial-state setup (VM snapshot, file download, opening apps — tasks deliberately start at intermediate states, not a clean boot); (2) post-processing (e.g., activating a window, saving files); (3) getters that extract the artifacts to check (files, cookies, accessibility-tree elements, or live values via crawlers); (4) evaluator functions comparing the retrieved state to gold — e.g., `compare_table` over spreadsheet ranges, `is_cookie_deleted`, `check_a11y_tree`. There are 134 unique, hand-authored evaluation functions (~2 hours per task).
- **Reported (Table 5).** The best model, GPT-4 with accessibility-tree input, reaches 12.24% overall (OS 20.83%, Office 3.58%, Daily 25.64%, Professional 26.53%, Workflow 2.97%) vs. 72.36% for humans; multi-app Workflow tasks are the hardest (2.97%).

## Typical Duration

Capped at 15 interaction steps and a 30-minute wall-clock limit per task. Human operators take a median of ~112 seconds per task, though some tasks run to 900 seconds or more.

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

- Repository note: The execution-based reward is defined on [0, 1] (allowing partial credit), but results are reported as a single Success Rate; per-task partial-credit values are not broken out.

## Related Works

- [WebArena](./webarena.md) — Also an interactive, execution-evaluated environment, but limited to web sites rather than whole operating systems.
- [GAIA](./gaia.md) — Also evaluates general assistant capability, but via answer correctness rather than execution inside a computer environment.
