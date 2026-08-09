# BAGEN (2026)

> **English** | [简体中文](../zh/works/bagen.md)

## Overview

BAGEN is an evaluation benchmark that tests whether LLM agents are budget-aware — able to estimate mid-execution how much of their resource budget remains and whether the task is still finishable — treating budget as an active control signal rather than a passive, post-hoc cost metric. It evaluates five frontier agents across four environments and formalizes budget-awareness as progressive interval estimation, in which the agent predicts an upper and lower bound on its remaining budget at every turn.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — evaluates an agent meta-property (cost, safety, or robustness), not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2606.00198>
- **Project:** <https://ragen-ai.github.io/bagen/>
- **Code:** <https://github.com/mll-lab-nu/BAGEN>

## Summary

BAGEN argues that agent cost is today measured only after execution, so agents never treat budget as something to reason about while a task is still running. It defines budget along two axes — internal budget from the model's own token generation and external, multi-dimensional budget from actions in the environment — and recasts budget-awareness as progressive interval estimation scored by a rollout-replay protocol. Across four environments and five frontier agents it finds that task success correlates only weakly with budget-awareness (r = 0.35) and that frontier models are consistently over-optimistic, yet the signal is trainable, with early stopping saving 28–64% of tokens on failed runs.

## Tasks

Four environments supply the tasks: Sokoban box-pushing on an 8×8 grid, Search-R1 multi-hop retrieval, SWE-bench GitHub-issue resolution, and Warehouse, a supply-chain environment curated from real enterprise data. The first three probe internal token budgets, while Warehouse probes external, multi-resource budgets over time, storage occupancy, and cumulative cost. BAGEN generates 128 rollouts per model on Sokoban, Search-R1, and Warehouse and 64 on SWE-bench, and a rollout-replay protocol turns each non-terminal turn into one estimation sample, yielding 2,000–3,000 samples per model-task pair.

## Domains

Interactive planning puzzles, multi-hop question answering, software-issue resolution, and supply-chain operations.

## Evaluation

- **Feasibility Macro-F1.** Binary prediction of whether a task is still finishable, computed over the full trajectory (all-turn) or the first turn only (first-turn).
- **Fail-F1.** Restricted to tasks that ultimately fail, measuring how early the agent detects an impossible run.
- **Interval Score.** Combines coverage — whether the realized budget falls inside the predicted lower and upper bound — with tightness, which penalizes intervals that are needlessly wide.
- **Reported.** Across GPT-5.2 Instant, Claude Opus 4.7, Claude Sonnet 4.6, Gemini 3.1 Pro, and Qwen3-235B, task success correlates with budget-awareness at only r = 0.35 and the models are consistently over-optimistic; early stopping saves 28–64% of tokens on failed trajectories while lowering overall success by only 1.6–4.2 percentage points; supervised fine-tuning raises a trained Qwen-7B's feasibility accuracy from 25.5% to about 90%, though interval coverage climbs only from 10.5% to at most 47% after SFT+RL.

## Typical Duration

Per-task budgets are capped per environment: 2,500 tokens on Sokoban, 3,500 tokens on Search-R1, 160 turns on SWE-bench, and a multi-resource ceiling over time, storage occupancy, and cost on Warehouse. Budget exhaustion is the horizon — a task ends when its cap is reached or the agent halts.

## Main Contribution

A benchmark that reframes agent resource use as an online prediction problem — progressive interval estimation of remaining internal and external budget — and shows the resulting budget-awareness signal to be only weakly correlated with task success yet trainable enough to drive early stopping.

## Key Design Ideas

- Budget split into internal budget (fresh tokens from the model's own reasoning) and external, D-dimensional budget (the cost actions commit in the environment).
- Budget-awareness formalized as progressive interval estimation: at each turn, predict a lower and upper bound on remaining budget, or declare the task impossible.
- A rollout-replay protocol that scores every non-terminal turn of pre-collected trajectories as an independent estimation sample.
- Trainable budget control via supervised fine-tuning on interval targets followed by GRPO reinforcement learning that rewards tight-but-covering intervals.

## Strengths

- Turns cost from a post-hoc statistic into a per-turn control signal, so an agent can in principle stop before spending budget on an unwinnable task.
- Spans both internal token budgets and external multi-resource action budgets (time, storage, cost) rather than measuring tokens alone.
- Rollout-replay scoring decouples budget estimation from policy quality, isolating awareness as a capability measurable across five frontier models.

## Limitations

- Repository note: Interval calibration stays weak — coverage reaches only 47% even after SFT+RL — so the predicted budget bounds are not yet reliable.
- Repository note: The trainability results come from a single open model (Qwen-7B); the five frontier agents are evaluated zero-shot and not themselves fine-tuned for budget-awareness.

## Related Works

- [CostBench](./costbench.md) — Also treats resource cost as a first-class evaluation target, but scores the cost-optimality of a completed tool-use plan rather than the agent's per-turn forecast of its own remaining budget.
- [SimulCost](./simulcost.md) — Also prices non-token resources, but charges physics-simulation time and experimental cost the agent must ration rather than asking it to predict budget-exhaustion intervals and halt early.
- [CATP-LLM](./catp-llm.md) — Also targets cost-aware agent behavior, but is a tool-planning method optimizing a performance-cost trade-off rather than a benchmark probing whether agents can estimate remaining budget mid-execution.