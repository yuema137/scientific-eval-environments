# VeRO / VeRO-Bench (2026)

## Overview

VeRO (Versioning, Rewards, and Observations) is an outer harness for benchmarking coding agents on *agent harness optimization* — iteratively improving a target agent by editing and evaluating its code — providing versioned snapshots, budget-controlled evaluation, and structured execution traces. VeRO-Bench is the accompanying benchmark suite of target agents, tasks, and reference evaluation procedures.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.22480>
- **Code:** <https://github.com/scaleapi/vero>
- **Venue:** ICML 2026

## Summary

VeRO frames agent optimization as an open-ended coding task and asks how well coding agents, acting as *optimizers*, can improve *target agent harnesses* as arbitrary programs — a setting the paper distinguishes from prompt-optimization frameworks that treat the underlying workflow as fixed. Because harnesses interleave deterministic code with stochastic LLM completions, and because uncontrolled optimization risks evaluation contamination and unrestricted budget usage, VeRO enforces six requirements: versioning (every modification is an auto-committed Git snapshot), budget enforcement, permission control (no access to held-out test data or evaluation infrastructure), reproducible execution (uv-pinned packages, isolated environments), structured tracing, and a standardized observation interface. The optimization objective is *lift* — expected improvement over the baseline agent on held-out data — subject to a hard evaluation-call budget n_E ≤ B.

## Tasks

The benchmark study evaluates optimizers on five target-agent tasks spanning math reasoning (MATH), tool use (TAU-Bench Retail), multi-step reasoning (GAIA), factual QA (SimpleQA), and science QA (GPQA), each with train/validation/test splits and hand-crafted task-specific target agents (GPT-4.1 mini as the fixed target model). The main protocol compares 8 optimizer configurations across the 5 tasks over N = 3 iterations each (120 experiments, budget B = 8): Claude Code variants (Pure, VeRO Tools), VeRO-Agent variants (Default, Orchestrator under three optimizer models, Resources-Only), and GEPA as an external baseline. Case studies add a minimal-vs-sophisticated agent pair (Pawn / Knight) on GAIA and a long-horizon coding study optimizing the Terminus-KIRA harness on TerminalBench-2 (89 terminal tasks).

## Domains

Agent harness optimization over general agentic task suites: math, tool use, multi-step QA, factual and science QA, and terminal-based coding.

## Evaluation

- **Lift over baseline** — maximum accuracy gain over the initial agent across iterations, evaluated on held-out data — plus variance across iterations (optimization stability) and mean inference runtime per sample.
- **Budget-controlled evaluation:** each evaluation request checks out a specific commit, runs the gated Evaluator, stores results, and decrements the budget; requests beyond n_E ≤ B are blocked, so no optimizer gains advantage through extra compute. TerminalBench-2 budgets are defined in samples rather than full passes because one full evaluation of the 89-task suite with Claude Haiku 4.5 costs about $180.
- Reported results: with the target model held fixed, the full VeRO harness yields an average best score of 0.61 vs. a 0.50 baseline; Claude Code without VeRO tools reaches 0.53, and adding VeRO tools alone 0.55. The external baseline GEPA (0.54) matches VeRO's Resources-Only variant (0.54), both below VeRO-Agent Default. Gains are strongly task-dependent — tool-use-oriented tasks (GAIA, Retail, SimpleQA) improve consistently while reasoning-heavy tasks (GPQA, MATH) barely move, and a budget ablation over B ∈ {2, 4, 8, 16, 32} shows the reasoning-task plateau is not a budget artifact. On TerminalBench-2, the best optimizer run lifts pass rate from 30.3% (27/89) to 37.1% (33/89), and one run cuts the crash rate from 46.1% to 30.3% without changing pass rate.

## Typical Duration

Iterative optimization loops of up to B evaluation calls (B = 8 in the main study), each involving code inspection, modification, and a budget-gated evaluation of the target agent on training samples.

## Main Contribution

Casting agent optimization as a benchmarkable capability of coding agents: a controlled protocol (versioning, budget enforcement, permission control, reproducible execution, structured tracing, standardized observations) plus a standardized suite that together allow optimizers to be compared under identical resource and information conditions.

## Key Design Ideas

- Evaluation calls as the scarce resource: each scoring of the target agent is treated as an expensive black-box query, decremented from a hard budget.
- Git-worktree versioning with auto-commit hooks makes every modification an immutable, diffable trajectory step, enabling rollback and post-hoc analysis.
- Permission control programmatically walls off held-out test data, evaluation infrastructure, and model checkpoint changes, preventing trivial or contaminated wins.
- A standardized observation interface fixes what traces, history, and statistics every optimizer sees, so comparisons isolate the optimizer rather than its information access.
- Optimization-trajectory interpretability: commit histories are tagged by change type, showing that optimizers default to prompt modifications (over 50% of phases after the first) and that change diversity collapses after early phases.

## Strengths

- Makes the evaluation-cost budget an enforced, gated protocol element rather than an honor-system convention.
- Coding-agent-agnostic: any optimizer that consumes the exposed interfaces and preserves commit-level traceability can be benchmarked.
- Empirical findings beyond a leaderboard: optimization headroom inversely correlates with target-agent sophistication, instruction templates trade variance against peak performance, and single-task gains do not reliably generalize (one commit gained +5.75 points on GAIA while regressing −17.8 on SimpleQA).
- Robustness study checks whether optimized harnesses transfer when the target model is swapped, finding gains persist within a model family but can regress out-of-family.

## Limitations

The paper's own limitations note that the budget is specified in evaluation calls rather than tokens or API cost, introducing variance; that budget-allocation strategies across independent sessions are not compared; that human baselines for the target agents are absent; and that public-API instability and potential reward hacking via leaked ground truth are not controlled.

## Related Works

- [Harness-Bench](./harness-bench.md) — Also makes the agent harness a first-class evaluation object, but measures how fixed harness configurations affect performance across models, whereas VeRO evaluates agents that *edit* harnesses.
- [SWE-bench](./swe-bench.md) — Execution-graded coding-agent benchmark whose Docker-based reproducibility VeRO explicitly mirrors with uv-pinned, Git-versioned target packages; SWE-bench measures task completion while VeRO measures improving other agents.
