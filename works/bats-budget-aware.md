# BATS / Budget Tracker (2025)

> **English** | [简体中文](../zh/works/bats-budget-aware.md)

> **First appeared:** 2025-11-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2511.17006)

## Overview

A study of what happens when tool-augmented agents are scaled under explicit tool-call budgets, motivated by the finding that simply raising the budget does not help because agents have no awareness of it. It contributes a unified cost metric that prices token and tool consumption on one scale, a lightweight Budget Tracker plug-in that makes the remaining budget visible to the agent, and BATS, a framework that adapts planning and verification to the budget that remains.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — web-search, conversational and coding agents under budget. No scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2511.17006>
- **Code:** <https://github.com/google-research/budget-aware-agent>
- **Venue:** Accepted to COLM 2026. arXiv v1 November 2025, v2 August 2026.

## Summary

Test-time scaling for tool-augmented agents differs from scaling reasoning tokens: a tool call is an action against an environment, not just more thinking. The paper's starting observation is negative — raising the tool-call budget alone does not raise performance, because the agent never learns how much it has left and plateaus. Two interventions follow. The Budget Tracker is a plug-in that injects the used and remaining budget per tool into the agent's context at each iteration, together with a policy guideline describing what to do in different budget regimes; it is deliberately minimal, and most of the paper's gain comes from it. BATS builds on that awareness with a planning module that maintains a tree-structured checklist whose breadth and depth adjust to the remaining budget, and a verification module that checks a proposed answer constraint by constraint and decides CONTINUE, PIVOT or SUCCESS conditioned on budget status, compressing the trajectory into a summary when it pivots. To compare any of this fairly, the authors formalise a single cost currency covering both tokens and tool calls, and use it to plot cost-performance scaling curves rather than accuracy at a fixed budget.

## Tasks

Primary evaluation is on web-search agents: **BrowseComp (1,266 web-browsing questions)**, **BrowseComp-ZH (289 questions)**, and **HLE-Search (a 200-question curated subset of Humanity's Last Exam)**. Appendices extend the study to conversational agents on the **τ²-bench retail subset (114 tasks)** and coding agents on **SWE-bench Verified (500 tasks)**.

Tool-call budgets are the independent variable, tested per tool at **10, 30, 50 and 100**; τ²-bench uses global budgets of 10, 30 and 50, and SWE-bench Verified uses 50, 60 and 70.

## Domains

No canonical domain is assigned. The evaluated settings are web browsing, retail dialogue and software issue resolution; HLE-Search draws on Humanity's Last Exam, but the paper reports no science-field breakdown of its 200-question subset, so no slice is identifiable and sized. The contribution is a cost-measurement and budget-awareness methodology rather than a science or engineering task suite.

## Evaluation

The unified cost metric is **`C_unified(x, π) = c_token(x, π) + Σᵢ cᵢ(x, π)·Pᵢ`** — token cost at official provider rates plus each tool's invocation count priced at **a unified rate of $0.001 per invocation** for both search-API calls and web-browsing actions. Having one currency is what lets the paper draw cost-performance scaling curves and argue about a Pareto frontier rather than comparing accuracies at nominally equal tool budgets.

Backbones are **Gemini-2.5-Flash**, **Gemini-2.5-Pro** (thinking budget 1024 tokens) and **Claude-Sonnet-4**, with Gemini-3-Flash-Preview added in an appendix.

Reported results: on **BrowseComp at budget = 100, BATS reaches 24.6% accuracy against ReAct's 12.6%**. The sharper result is the efficiency one — the **Budget Tracker alone at budget = 10 reaches 12.8%, matching ReAct's 12.6% at budget = 100**, while using **40.4% fewer search calls, 19.9% fewer browse calls and 31.3% lower overall cost**. BATS is reported to outperform a parallel majority-vote baseline across budget levels and to deliver higher accuracy at comparable or lower cost.

## Typical Duration

Budget is the evaluated variable rather than a fixed setting: per-tool call budgets of 10–100, with cost measured in the unified token-plus-tool currency above. No wall-clock budget is imposed. `TODO(reference)` — absolute wall-clock and token totals per task are not tabulated.

## Main Contribution

A single cost currency for tool-augmented agents that prices tokens and tool calls together, used to run what the authors describe as the first systematic study of budget-constrained agents — plus the finding that most of the benefit comes not from a better search strategy but from simply telling the agent how much budget it has left.

## Key Design Ideas

- The unified cost metric is the enabling move: without one currency, "more tool calls" and "more tokens" cannot be traded off and scaling curves cannot be drawn.
- The Budget Tracker is deliberately minimal — an injected used/remaining line plus a policy guideline — which makes it a clean test of whether awareness *alone* accounts for the gain.
- Budget conditioning enters at two distinct decision points: how wide and deep to plan, and whether to CONTINUE, PIVOT or SUCCEED after a candidate answer.
- Pivoting compresses the trajectory into a summary rather than discarding it, so a change of direction does not also throw away the budget already spent.
- Reporting a scaling *curve* rather than a single accuracy makes the budget-awareness effect visible as a change in slope, not just a point improvement.
- Extending to conversational and coding agents in appendices tests whether the finding is specific to web search.

## Strengths

- The headline finding is a negative result about the field's default assumption — that more budget buys more performance — and the paper leads with it.
- The efficiency comparison (matching a baseline's accuracy at one-tenth its budget) is a stronger claim shape than an accuracy gain at equal budget.
- The cost metric is written down explicitly, including the per-invocation price, so the numbers can be recomputed under different pricing.
- The simplest intervention is reported as carrying most of the gain, rather than being buried beneath the more elaborate framework.
- Code is public under a Google Research repository, and the work is peer-reviewed at COLM 2026.
- Three backbones across three benchmark families, with two further agent settings in appendices.

## Limitations

- The $0.001-per-invocation tool price is an assumed average, not a measured cost; conclusions about the Pareto frontier are sensitive to it, and real search-API and browsing costs differ.
- Cost covers tokens and tool calls only. Wall-clock time, GPU time and memory — the currencies that dominate scientific and engineering agent work — are not modelled.
- The authors note HLE-Search questions are typically shorter and contain fewer verifiable details, which limits what the verification module can contribute there.
- Absolute wall-clock and token totals per task are not tabulated (recorded above as `TODO(reference)`).
- Budget awareness is delivered by prompt injection, so the mechanism's reliability depends on instruction-following and is not enforced by the harness.
- Repository note: the primary artifact is a method plus a cost metric rather than a task suite. This card indexes it for the metric and the systematic cost-performance study, which are evaluation-methodology contributions; the BATS framework itself is a system.
- Repository note: the budget is a *given* constraint the agent must respect, not a *predicted* quantity. The paper does not estimate in advance what an action will cost, which is the gap the profile-based direction on the topic page describes.

## Related Works

- [CATP-LLM](./catp-llm.md) — Cost-aware tool planning where tool execution costs are traded against performance, learning a planning policy rather than measuring a cost currency.
- [CostBench](./costbench.md) — Budget-aware agent evaluation as a benchmark, with cost folded into the score and static-versus-dynamic robustness reported.
- [R³-Bench](./r3-bench.md) — Shared-budget allocation across a problem suite, calibrated against an oracle built from the model's own response curves.
- [AI Research Preference Models](./ai-research-preference-models.md) — The predictive counterpart: rather than telling the agent its remaining budget, it predicts what a candidate action would cost before running it.
- [SimulCost](./simulcost.md) — Cost-aware evaluation in a scientific setting, where the currency is simulation compute rather than tool calls.
