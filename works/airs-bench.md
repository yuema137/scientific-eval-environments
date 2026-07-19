# AIRS-Bench (2026)

## Overview

AIRS-Bench (AI Research Science Benchmark) is a suite of 20 frontier research-science tasks for LLM agents, covering the full research lifecycle across language modeling, mathematics, bioinformatics, and time-series forecasting — with no baseline code provided.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.06855>

## Summary

AIRS-Bench evaluates agentic capabilities across the full research lifecycle rather than isolated coding subtasks. Tasks span four scientific domains and are set up without providing baseline code, so agents must design and execute end-to-end research workflows.

## Tasks

20 tasks.

## Domains

Language modeling, mathematics, bioinformatics, time-series forecasting.

## Evaluation

Agentic capability across the full research lifecycle. Baseline references are drawn from human performance (per abstract).

## Typical Duration

TODO(reference): abstract does not state per-task duration.

## Main Contribution

A frontier research-science benchmark that removes baseline code and requires agents to construct end-to-end research workflows from scratch across a small but diverse suite of tasks.

## Key Design Ideas

- No baseline code provided — agents design workflows from scratch.
- Full research-lifecycle coverage rather than isolated modeling or evaluation subtasks.
- Multi-domain breadth in a compact 20-task suite.

## Strengths

- Removing baseline code stresses genuine agent-driven research design.
- Compact but multi-domain — allows focused evaluation across research subfields.

## Limitations

- Repository note: 20 tasks — small task pool relative to typical benchmarks.

## Related Works

- [NatureBench](./naturebench.md) — Also research-science, but anchored on published Nature-family SOTA.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also research-science workflows, but with executable containerized verification.
