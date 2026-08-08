# PhySciBench (2026)

> **English** | [简体中文](../zh/works/physcibench.md)

## Overview

PhySciBench is a benchmark of 200 expert-curated deep-research questions in the physical sciences, balanced between physics and chemistry across six task categories reflecting real scientific workflows. The accompanying DelveAgent framework is agent-construction work adjacent to this repository's evaluation focus.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.18648>
- **Venue:** arXiv preprint (physics.comp-ph), 2026

## Summary

The paper identifies three deficiencies in existing deep-research systems on physical-science questions — fragility in extended reasoning chains, limited knowledge transfer across steps, and a lack of physics-grounded self-verification — and introduces PhySciBench to measure them: 200 expert-curated questions balanced between physics and chemistry in six task categories. It also develops DelveAgent (adaptive planning loop, dual-granularity memory, hierarchical physics-grounded reflection).

## Tasks

200 expert-curated questions, balanced between physics and chemistry, organized into six task categories reflecting real-world scientific workflows.

## Domains

Physical sciences: physics and chemistry.

## Evaluation

- Accuracy-based evaluation comparing state-of-the-art models and agent systems.
- **Reported.** The Gemini Deep Research baseline reaches 33.5% accuracy; DelveAgent improves by up to 7.5 percentage points at roughly one-third of the strongest baseline's inference cost.

## Typical Duration

Deep-research workflows with extended reasoning chains; per-question budgets are TODO(reference).

## Main Contribution

An expert-curated physical-science deep-research benchmark that makes reasoning-chain fragility, cross-step knowledge transfer, and physics-grounded self-verification measurable.

## Key Design Ideas

- Six task categories mirror real scientific workflows rather than exam formats.
- Physics/chemistry balance keeps the benchmark from collapsing into one field.
- Cost is reported alongside accuracy for the proposed agent.

## Strengths

- Targets a diagnosed failure profile (fragile chains, poor transfer, no physical self-verification) rather than generic difficulty.
- Baseline accuracy of 33.5% leaves substantial headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- Repository note: DelveAgent, the paper's second contribution, is agent implementation and out of this repository's scope; the card documents the benchmark.

## Related Works

- [PRBench](./prbench.md) — Also expert-curated physics evaluation, via end-to-end paper reproduction rather than deep-research questions.
- [DeepResearch Bench](./deepresearch-bench.md) — Also evaluates deep-research systems, scoring general-demand reports rather than physical-science questions.
- [TRACE](./trace.md) — Also evaluates deep-research agents, scoring whole trajectories rather than final answers.
