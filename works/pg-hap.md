# PG-HAP: Policy-Guided Stepwise Action Planning for Controllable LLM Reasoning (2026)

> **English** | [简体中文](../zh/works/pg-hap.md)

## Overview

PG-HAP trains a lightweight policy to select high-level reasoning actions step by step while keeping the executor LLM fully frozen.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — general mathematical and commonsense reasoning methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://aclanthology.org/2026.findings-acl.2024/>
- **Code:** <https://github.com/john1226966735/PG-HAP>
- **Venue:** Findings of ACL 2026

## Summary

The planner chooses among Analysis, Decomposition, Continue/Direct Reasoning, Knowledge Recall, Code Generation, Code Refinement, Verification, and Final Answer. An action-dependency mask blocks invalid or redundant transitions, while an action-diversity reward discourages collapse to one template. Because Qwen2.5 executor models remain frozen, performance changes isolate the learned high-level policy more cleanly than end-to-end tuning.

## Tasks

Five mathematical and commonsense reasoning benchmarks, including MATH, GSM8K, SVAMP, CommonsenseQA, and StrategyQA, evaluated with frozen 3B and 7B executors; supplementary experiments use Qwen3-8B.

## Domains

General language-model reasoning; not tied to a canonical scientific or engineering domain.

## Evaluation

Answer accuracy, action-sequence distributions, structural redundancy, sequence collapse, and ablations of dependency masking and diversity reward.

## Typical Duration

No fixed per-example time or token budget is reported.

## Main Contribution

A controlled planner–executor experiment showing that improving high-level action selection alone can improve reasoning without changing the executor model.

## Key Design Ideas

- Freeze the executor and train only a small action-selection policy.
- Enforce legal transitions and reward population-level sequence diversity.

## Strengths

- The frozen executor provides unusually clean attribution to the planner.
- Explicit action traces expose redundancy and collapse that final accuracy hides.

## Limitations

- The action set and legal-transition graph are hand-designed.
- Reduced template collapse on five benchmarks does not establish broad OOD strategy transfer.
- The planner optimizes terminal correctness; ground truth for whether an intermediate action was the best choice is unavailable.

## Related Works

- [MetaAct-RL](./metaact-rl.md) — jointly trains meta-action behavior inside the reasoning model.
- [HiPER](./hiper.md) — applies a planner–executor hierarchy to interactive environment actions.
