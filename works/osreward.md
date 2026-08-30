# OSReward (2026)

> **English** | [简体中文](../zh/works/osreward.md)

> **First appeared:** 2026-07-30 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.28609)

## Overview

OSReward is a standardized benchmark for evaluating cross-platform computer-use reward models — vision-language judges of computer-using agent trajectories — released together with the OS-Shepherd-100K corpus of reasoning-annotated trajectory judgments and trained OS-Shepherd reward models (9B and 35B).

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.28609>
- **Venue:** arXiv preprint (work in progress), 2026

## Summary

OSReward establishes ground-truth verdicts through multi-stage human annotation of trajectories from diverse agent backbones across platforms, and identifies systematic leniency bias in state-of-the-art model judges. It ships three variants — the main benchmark, OSReward-Hard for difficult cases, and OSReward-Multi for fine-grained efficiency and alignment scoring — plus OS-Shepherd-100K and open reward models that match commercial judges at 30–60× lower cost.

## Tasks

Diverse computer-use agent trajectories across platforms, human-annotated in multiple stages; the main benchmark plus OSReward-Hard and OSReward-Multi variants. Exact instance counts are TODO(reference).

## Domains

Cross-platform computer-use trajectories (evaluated as reward-model input, not as a science domain).

## Evaluation

- Reward-model verdicts scored against multi-stage human-annotated ground truth.
- OSReward-Hard isolates difficult judgments; OSReward-Multi scores fine-grained efficiency and alignment dimensions.
- **Reported.** State-of-the-art models exhibit systematic leniency bias; OS-Shepherd models (9B, 35B) match frontier commercial judges at 30–60× lower cost.

## Typical Duration

N/A — post-hoc judgment of recorded trajectories.

## Main Contribution

Institutes a standardized, human-anchored evaluation for computer-use reward models and demonstrates that open, small judges can match commercial ones at a fraction of the cost.

## Key Design Ideas

- Ground truth by multi-stage human annotation across heterogeneous agent backbones, so the judge is tested off-distribution.
- A Hard split and a multi-dimension split separate difficulty from granularity.
- A 100K reasoning-annotated judgment corpus makes judge training reproducible.

## Strengths

- Directly measures and names the leniency bias of current VLM judges.
- Cost-matched comparison shows commercial-judge quality is attainable at 30–60× lower cost.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- The authors mark the work as in progress.

## Related Works

- [CUARewardBench](./cuarewardbench.md) — Also benchmarks computer-use reward models against expert labels; OSReward adds cross-platform standardization and trained open judges.
- [AgentRewardBench](./agentrewardbench.md) — Also measures trajectory-judge reliability against ground truth, for web agents.
- [ToolPRMBench](./toolprmbench.md) — Also benchmarks step-level reward models, for tool-use decision steps.
