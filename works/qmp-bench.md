# QMP-Bench (2026)

> **English** | [简体中文](../zh/works/qmp-bench.md)

## Overview

QMP-Bench is a benchmark of 100 research-level, end-to-end quantum many-body simulation tasks extracted from 21 high-impact journals. The accompanying PhysVEC multi-agent framework is agent-construction work adjacent to this repository's evaluation focus (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.00149>
- **Venue:** arXiv preprint (physics.comp-ph), 2026

## Summary

QMP-Bench asks whether AI systems can reproduce physical results from published quantum many-body research: each of its 100 tasks is an end-to-end simulation problem extracted from 21 high-impact journals, requiring both correct code and physically valid results. The paper pairs the benchmark with PhysVEC, a multi-agent framework that enforces self-verification and error correction through programming and scientific verifiers, yielding interpretable evidence and error correction at each step; PhysVEC is reported to significantly outperform existing LLM baselines on QMP-Bench with favorable inference-time scaling.

## Tasks

100 research-level, end-to-end quantum many-body simulation tasks extracted from 21 high-impact journals.

## Domains

Quantum many-body physics and its computational simulation methods.

## Evaluation

- Programming verifiers for coding correctness and scientific verifiers for principle-based physical validity.
- **Reported.** PhysVEC significantly outperforms existing LLM baselines across QMP-Bench scenarios with favorable inference-time scaling; numeric figures are TODO(reference).

## Typical Duration

End-to-end simulation workflows per task; per-task budgets are TODO(reference).

## Main Contribution

Anchors agent evaluation to published quantum many-body results, with verification split into coding correctness and principle-based physical validity rather than a single pass signal.

## Key Design Ideas

- Tasks are extracted from published journal results, so ground truth is what the literature actually established.
- Dual verifiers separate "the code runs correctly" from "the physics is valid."
- Stepwise verification yields interpretable evidence rather than only a terminal verdict.

## Strengths

- Research-level task provenance across 21 journals.
- The verifier split localizes failures between software and physics.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code or dataset release is verifiable from the paper's arXiv page.
- Repository note: PhysVEC, the paper's second contribution, is agent implementation and out of this repository's scope; the card documents the benchmark.

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — Also expert-level condensed-matter/quantum many-body evaluation, via 50 machine-graded theory problems rather than end-to-end simulations.
- [PRBench](./prbench.md) — Also reproduces published physics research end to end, across 11 subfields with expert rubrics.
- [MDArena](./mdarena.md) — Also containerized, research-derived simulation workflows, in molecular dynamics rather than quantum many-body physics.
