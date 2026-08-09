# EcoAgent-Bench (2026)

> **English** | [简体中文](../zh/works/ecoagent-bench.md)

## Overview

EcoAgent-Bench is a benchmark for economic decision-making in budget-constrained LLM agents: every task specifies priced actions and an explicit budget, and agents are scored on whether their decisions are economically sound rather than merely task-completing.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — evaluates an agent meta-property (cost, safety, or robustness), not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2608.05519>
- **Venue:** arXiv preprint, 2026

## Summary

EcoAgent-Bench comprises 304 real-derived tasks in five families adapted from GAIA, HotpotQA, and MuSiQue, testing four decision types: avoiding unnecessary escalation, escalating when needed, selecting model tiers, and stopping on unsupported premises. An economic-consistency score compares performance on upgrade-oriented versus save-oriented task groups, exposing one-sided policies that always spend or always save.

## Tasks

304 real-derived tasks across five families adapted from GAIA, HotpotQA, and MuSiQue; every task specifies priced actions and an explicit budget, and targets one of four decision types (avoid unnecessary escalation, escalate when needed, select model tier, stop on unsupported premises).

## Domains

Question answering across multiple knowledge domains (adapted from existing QA benchmarks); no single science domain.

## Evaluation

- Micro-averaged accuracy and strict success rates.
- **Economic-consistency score** contrasting upgrade-oriented and save-oriented task groups, so a policy that always escalates (or never does) cannot score well.
- Seven LLM agents evaluated in tool-API and workspace-CLI settings, plus four scripted oracle controls.
- **Reported.** Tool-API agents reach only 3.9–24.0% micro strict success and at most 7.3% economic consistency; a budget sweep moves GPT-5.4's escalation rate from 0% to only 3%.

## Typical Duration

Budgeted QA episodes with priced actions; per-task budgets are task-specified.

## Main Contribution

Makes the economic soundness of agent decisions — not just task success under a cap — the measured object, via paired task groups that expose one-sided spending policies.

## Key Design Ideas

- Priced actions plus explicit budgets turn every step into an economic decision.
- Upgrade/save paired groups make economic consistency measurable and ungameable by a constant policy.
- Scripted oracle controls bound what a rational policy could achieve.

## Strengths

- Shows agents are nearly insensitive to budget changes (escalation rate 0% → 3% across a sweep).
- Strict success and economic consistency reveal that current agents fail both.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CostBench](./costbench.md) — Also evaluates cost-optimal agent decision-making, over dynamically priced travel planning.
- [BAGEN](./bagen.md) — Also makes budget an online decision signal, via per-turn budget-interval prediction.
- [CATP-LLM](./catp-llm.md) — Also prices actions for cost-aware planning, over tool-execution plans.
