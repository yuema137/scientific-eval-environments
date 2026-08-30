# PTA-GRPO: Plan Then Action, High-Level Planning Guidance Reinforcement Learning for LLM Reasoning (2025)

> **English** | [简体中文](../zh/works/pta-grpo.md)

## Overview

PTA-GRPO distills compact high-level guidance from chain-of-thought traces, then jointly optimizes plan quality and fine-grained reasoning with reinforcement learning.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — general mathematical reasoning methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2510.01833>
- **Venue:** arXiv preprint, 2025

## Summary

The first stage summarizes detailed solution traces into an analytic plan and uses plan–reasoning pairs for supervised fine-tuning. The second stage adds a guidance-aware GRPO objective that rewards both the final answer and the quality of the high-level plan. The hierarchy is therefore plan followed by token-level reasoning, rather than independent modules acting at different environment time scales.

## Tasks

Mathematical reasoning evaluated across ten benchmarks; primary tables include MATH-500, AIME 2024, AIME 2025, and AMC 2023 across Qwen and Llama model families.

## Domains

General mathematical reasoning and language-model post-training; not mapped to the Mathematics domain because the work studies a generic reasoning method rather than mathematical research activity.

## Evaluation

Answer accuracy across reasoning benchmarks, plan-quality reward, cross-model consistency, and ablations of supervised plan guidance and the RL objective.

## Typical Duration

No fixed per-problem time or token budget is reported.

## Main Contribution

Treating compact global guidance and detailed local reasoning as separately supervised levels inside one post-training objective.

## Key Design Ideas

- Distill detailed chains into compact analytic guidance.
- Optimize guidance quality jointly with final correctness under GRPO.

## Strengths

- Broad cross-model and cross-benchmark evaluation.
- Ablations separate plan supervision from the guidance-aware RL stage.

## Limitations

- Plans are distilled from solution traces and may encode dataset-specific templates.
- Plan quality depends on a learned reward rather than executable plan validity.
- Experiments emphasize mathematical IID benchmarks rather than interactive or compositional transfer.

## Related Works

- [PG-HAP](./pg-hap.md) — selects the next action online instead of committing to one plan before reasoning.
- [MetaAct-RL](./metaact-rl.md) — represents a trajectory as repeated semantic reasoning actions.
