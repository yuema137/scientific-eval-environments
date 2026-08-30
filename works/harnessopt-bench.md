# HarnessOpt-Bench (2026)

> **English** | [简体中文](../zh/works/harnessopt-bench.md)

## Overview

HarnessOpt-Bench is a benchmark measuring how well frontier LLMs perform automated harness optimization — iteratively improving the prompts, tools, control flow, and orchestration code surrounding LLMs — under a fixed target-evaluation budget inside a trusted execution environment.

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.06301>
- **Venue:** arXiv preprint, 2026

## Summary

Each optimizer model receives a seed harness, evaluation feedback, and a fixed budget of target evaluations, and is scored by its normalized gain over the seed on a held-out test partition. A trusted execution environment enforces evaluation boundaries, meters resource use, and preserves candidate versions for audit. Across 4 downstream tasks, 5 frontier optimizer models, and 111 scored runs, the paper reports that optimizer models separate more than the coding harnesses they act through, and that gains vary substantially across tasks and seed regimes.

## Tasks

4 downstream tasks; 5 frontier LLMs evaluated as optimizers; 111 scored runs in total. Each run starts from a seed harness with evaluation feedback under a fixed target-evaluation budget.

## Domains

Agentic-system harness optimization; no single science domain.

## Evaluation

- **Normalized gain over the seed harness** on a held-out test partition.
- A trusted execution environment enforces evaluation boundaries, meters resource use, and preserves candidate versions for audit.
- **Reported.** Optimizer models separate more than the coding harnesses they act through; gains vary substantially across tasks and seed regimes.

## Typical Duration

Iterative optimize-evaluate loops bounded by a fixed target-evaluation budget.

## Main Contribution

Benchmarks the LLM as harness optimizer under audited, budget-limited evaluation, showing the optimizer model matters more than the harness it operates through.

## Key Design Ideas

- The evaluation budget is the scarce resource; optimization ability is measured per evaluation spent.
- Held-out test partitions separate true harness improvement from overfitting to the feedback signal.
- TEE-enforced metering makes resource use and candidate history auditable.

## Strengths

- Directly measures a capability (self-improving scaffolding) that other benchmarks only imply.
- Audit-preserving infrastructure guards against optimization-by-leakage.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- The abstract reports no absolute performance figures; per-task numbers are TODO(reference).

## Related Works

- [VeRO / VeRO-Bench](./vero.md) — Also benchmarks agents optimizing agents under a hard evaluation-call budget; HarnessOpt-Bench adds TEE-audited execution and held-out gain scoring.
- [Harness-Bench](./harness-bench.md) — Also isolates the harness as the studied variable, by fixing tasks and varying harnesses rather than optimizing them.
- [GATE](./gate.md) — Also studies the evolution of agent scaffolding components, for tool graphs rather than whole harnesses.
