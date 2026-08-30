# R³-Bench (2026)

> **English** | [简体中文](../zh/works/r3-bench.md)

> **First appeared:** 2026-08-17 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.16033)

## Overview

R³-Bench evaluates resource-rational reasoning: a model faces a suite of six problems that must share one budget, so success depends on allocating effort across problems rather than solving each in isolation. Its distinguishing move is to calibrate suite performance against the same model's demonstrated single-problem competence, using matched response curves to build an offline empirical oracle over observed successes.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.16033>
- **Code:** <https://github.com/NineAbyss/R-3-Bench>
- **Data:** <https://huggingface.co/datasets/R-3-Bench/R-3-Bench>
- **Venue:** arXiv preprint (August 2026).

## Summary

Resource rationality, borrowed from cognitive science, asks how an agent should allocate limited computation to maximise expected value. The authors observe that most reasoning and agent benchmarks hand out independent per-task budgets, and that the shared-budget studies which do exist never calibrate suite performance against what the same model demonstrably can do on those same problems alone. R³-Bench supplies that missing reference. Every problem is first run in isolation across a grid of budget levels, five runs per level, producing an empirical response curve — the observed success rate as a function of budget. A knapsack solver then picks one budget level per problem, including the option of allocating zero, subject to the shared constraint, maximising expected correct answers. The result is not a policy an agent could execute; it is an offline diagnostic that says what the model's own demonstrated competence would have been worth under perfect allocation. The gap between that oracle and the model's actual contest score is the paper's central quantity, and it is large and near-universal.

## Tasks

**50 suites per domain** across three domains, each suite holding **six problems** stratified as **3 Easy, 2 Medium, 1 Hard** — difficulty assigned by average output length from DeepSeek V4 Pro, GLM-5.2 and GPT-5.5. Sources are **Omni-MATH and MathNet** for mathematics (**300 problems**), **LiveCodeBench Pro** for competitive programming (**300 problems**), and **Reasoning Gym** for abstract reasoning (**300 problems**).

Two settings are evaluated. In the **tool-free** setting the model completes freely without tools or shell access and the budget is output tokens (`max_tokens`). In the **agentic** setting a tool-using agent works in a **Terminus-2** shell environment with code execution and the budget is counted tool actions; bookkeeping commands (`focus_problem`, `shelve_problem`) are logged separately as free steps.

Budgets are model-calibrated as relative pressure levels **ρ ∈ {0.2, 0.8}** against each model's own unbudgeted baseline — ρ = 0.2 being strong pressure and ρ = 0.8 moderate.

## Domains

**Mathematics** and **Computer Science.** Both slices are identifiable and sized: 300 mathematics problems from Omni-MATH and MathNet, and 300 competitive-programming problems from LiveCodeBench Pro. The third domain, abstract reasoning from Reasoning Gym, is a synthetic reasoning substrate rather than a scientific field and earns no domain assignment.

## Evaluation

The primary table has **72 cells** (6 models × 2 settings × 3 domains × 2 pressure levels). The **oracle matches or exceeds the contest score in all 72 cells and is strictly higher in 71** — a near-universal gap between demonstrated single-problem competence and what the model realises under a shared budget.

Two further comparisons narrow the interpretation. **Equal-allocation replay** — simply dividing the budget evenly and replaying — beats the model's own contest performance for **4 of 6 models** at ρ = 0.8, so the shortfall is not merely a failure to find a clever allocation. In a three-model diagnostic under strong agentic pressure (DeepSeek-V4-Pro, GLM-5.2, Hy-3), **at least one fixed scheduler exceeds the contest mean in 6 of 9 cells**, but no policy dominates across domains.

Trajectory diagnostics report limited strategy updating and pressure-dependent failure patterns.

The six flagship models are **DeepSeek-V4-Pro, Qwen3.7-Max, GLM-5.2, Hy-3, GPT-5.5 and Claude-Opus-4.8**; appendix results extend to eight models with DeepSeek-V4-Chat and DeepSeek-V4-Reasoner.

## Typical Duration

Budget is the evaluated variable rather than a fixed setting. In the tool-free setting it is output tokens capped at ρ × the model's unbudgeted baseline; in the agentic setting it is counted tool actions under the same relative scaling. Response-curve construction runs each problem in isolation over a fixed budget grid at **five runs per level**.

## Main Contribution

A shared-budget evaluation that supplies its own reference point: by measuring each problem's response curve in isolation first, it can state what a model's demonstrated competence would have yielded under optimal allocation, and thereby report the shortfall as a calibrated gap rather than as an unanchored score.

## Key Design Ideas

- The oracle is built from *observed* successes on a budget grid rather than from an assumed scaling law, so it is empirically grounded and never exceeds what the model actually did somewhere.
- Allowing the knapsack solver to allocate zero to a problem makes triage — deciding not to attempt something — an explicit part of optimal play.
- Budgets are calibrated per model against that model's own unbudgeted baseline, so ρ = 0.2 means comparable pressure across models of very different verbosity.
- Suite composition is fixed at 3 Easy / 2 Medium / 1 Hard, so every suite poses the same allocation problem shape and results aggregate meaningfully.
- Difficulty is assigned by measured output length across three models rather than by human labelling, making stratification reproducible.
- Equal-allocation replay is included as a deliberately unintelligent control: if it beats the model, the failure is in allocation behaviour rather than in the difficulty of the allocation problem.
- Bookkeeping commands are logged as free steps so the agentic budget measures problem-solving actions rather than penalising the act of organising work.

## Strengths

- The oracle turns "the model underperformed" into a quantified, per-cell shortfall against the model's own demonstrated ability, which an absolute score cannot express.
- The gap is near-universal (71 of 72 cells strictly), so the finding does not rest on a favourable subset.
- Equal-allocation replay is a strong sanity check, and the paper reports that this trivial policy beats four of six models — a result unflattering to the models and central to the argument.
- Per-model budget calibration avoids the common artifact where a fixed token cap penalises verbose models.
- Both tool-free and agentic settings are run, so the finding is not an artifact of one interaction mode.
- The authors state plainly that no scheduler dominates across domains, resisting the temptation to present a fix.
- Code and dataset are both public.

## Limitations

- The response-curve oracle has offline access to every problem's complete empirical response curve, so it is a diagnostic upper bound and explicitly not a deployable policy.
- Equal-allocation replay becomes uninformative under severe budget pressure, where the per-problem share can be extremely small.
- The online scheduler study covers only three models, and the target-in-suite context-stress diagnostic only two models across 12 cells.
- Human annotation of failure causes excludes cases with insufficient evidence, so the reported failure distribution is conditioned on legibility.
- Abstract reasoning from Reasoning Gym is synthetic, and mathematics and competitive programming are drawn from existing benchmarks, so contamination risk is inherited from those sources and is not addressed in what is reported here.
- Repository note: the evaluation is of models under budget rather than of scientific research capability; the mathematics and competitive-programming slices are what connect it to this repository's domain axis.

## Related Works

- [SimulCost](./simulcost.md) — Cost-aware evaluation where compute spent is scored against accuracy achieved, on simulation parameter tuning rather than across a shared problem suite.
- [CostBench](./costbench.md) — Budget-aware agent evaluation with cost folded into the score, without a per-problem competence reference.
- [Gravity-Bench-v1](./gravity-bench.md) — Physics discovery where observation budget is part of the scoring, making budget allocation part of the scientific task itself.
- [Beyond Final Scores](./beyond-final-scores.md) — Also separates demonstrated capability from realized performance, using avg@3 versus best@3 rather than an allocation oracle.
