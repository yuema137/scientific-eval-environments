# HiPER: Hierarchical Reinforcement Learning with Explicit Credit Assignment for Large Language Model Agents (2026)

> **English** | [简体中文](../zh/works/hiper.md)

## Overview

HiPER factorizes an interactive LLM-agent policy into a high-level subgoal planner and a low-level executor, then assigns reinforcement-learning credit at both levels.

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — evaluated on general household and web-shopping agent tasks rather than a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2602.16165>
- **Venue:** arXiv preprint, 2026

## Summary

Flat agent RL operates at one time scale and propagates sparse terminal reward through long action sequences. HiPER instead lets a high-level policy propose a subgoal that the executor carries out over several environment actions. Hierarchical Advantage Estimation aggregates returns within each subgoal and coordinates planner and executor updates; the paper proves an unbiased estimator with lower variance than flat GAE under its assumptions.

## Tasks

Interactive text-agent tasks in ALFWorld and WebShop with Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct.

## Domains

General embodied household and web interaction; no canonical scientific or engineering domain.

## Evaluation

Task success, training stability and efficiency, performance by horizon, and ablations of hierarchical policy and advantage estimation. The reported 7B results reach 97.4% on ALFWorld and 83.3% on WebShop.

## Typical Duration

Variable multi-turn episodes; no single wall-clock duration is specified.

## Main Contribution

An explicit connection between temporal action abstraction and level-specific credit assignment in multi-turn LLM-agent post-training.

## Key Design Ideas

- Let each high-level subgoal span several low-level actions.
- Aggregate returns within subgoal segments and update both policies coherently.

## Strengths

- Directly evaluates long-horizon interactive agents rather than static reasoning only.
- Provides theoretical and empirical analyses of the credit estimator.

## Limitations

- Evaluation covers two simulated general-agent environments.
- Subgoal quality is mainly inferred from terminal task success rather than independently annotated.
- Planner/executor separation introduces an interface whose own grounding errors require separate diagnosis.

## Related Works

- [PG-HAP](./pg-hap.md) — trains a high-level reasoning-action planner with a frozen executor.
- [MA-RLHF](./ma-rlhf.md) — coarsens token-level actions without an explicit planner–executor split.
