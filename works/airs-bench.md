# AIRS-Bench (2026)

> **English** | [简体中文](../zh/works/airs-bench.md)

## Overview

AIRS-Bench (AI Research Science Benchmark) is a suite of 20 frontier research-science tasks for LLM agents, covering the full research lifecycle across language modeling, mathematics, bioinformatics, and time-series forecasting — with no baseline code provided.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.06855>

## Summary

AIRS-Bench evaluates agentic capabilities across the full research lifecycle rather than isolated coding subtasks. Tasks span four scientific domains and are set up without providing baseline code, so agents must design and execute end-to-end research workflows.

## Tasks

20 tasks.

## Domains

Language modeling, mathematics, bioinformatics, time-series forecasting.

## Evaluation

- **Execution-based, outcome-only.** Although tasks are framed around the full research lifecycle, grading is on the final artifact: the agent submits a `.csv` of predictions on the held-out test split, scored by a task-specific `evaluate.py` against test labels — no LLM judge, no workflow rubric, no baseline code provided.
- **Normalized Score (NS).** Per task, NS = [φ(s) − φ(s_min)] / [φ(s_sota) − φ(s_min)], where s_min is the worst score observed across seeds/agents and s_sota is the literature SOTA; 0 = worst observed, 1 = human SOTA, > 1 = exceeds SOTA. A "march of nines" transform φ(s) = −log₁₀|s − s_opt| (s_opt = theoretical optimum) log-scales gains near the ceiling so they count meaningfully.
- **Valid Submission Rate (VSR)** — fraction of runs producing an executable, scoreable submission.
- **Elo** — Bradley–Terry ratings over pairwise agent-score comparisons.
- **Reported:** average normalized score ≈ 24.1%; mean valid submission rate ≈ 55.1%; only ~1.58% of submissions exceed SOTA. On a per-task-average basis, agents beat human SOTA on 4 of 20 tasks (16 unbeaten), and human SOTA outranks every agent on Elo.

## Typical Duration

Each run lasts 24 hours with access to one H-200 GPU, and each task is launched at least 10 times ("seeds"). Classified by the authors as a high-compute benchmark (> 1 hour per task); some tasks are noted as compute- or time-limited.

## Main Contribution

A frontier research-science benchmark that removes baseline code and requires agents to construct end-to-end research workflows from scratch across a small but diverse suite of tasks.

## Key Design Ideas

- No baseline code provided — agents design workflows from scratch.
- Full research-lifecycle coverage rather than isolated modeling or evaluation subtasks.
- Multi-domain breadth in a compact 20-task suite.
- Normalized Score with a "march of nines" log transform, so improvements near the performance ceiling remain meaningful; complemented by Valid Submission Rate and Elo.

## Strengths

- Removing baseline code stresses genuine agent-driven research design.
- Compact but multi-domain — allows focused evaluation across research subfields.

## Limitations

- Repository note: 20 tasks — small task pool relative to typical benchmarks.
- Repository note: Although framed around the full research lifecycle, scoring is outcome-only (a predictions `.csv` vs. held-out labels); ideation and iterative refinement are not directly graded.

## Related Works

- [NatureBench](./naturebench.md) — Also research-science, but anchored on published Nature-family SOTA.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also research-science workflows, but with executable containerized verification.
