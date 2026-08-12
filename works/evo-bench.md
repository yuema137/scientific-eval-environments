# Evo-Bench (2026)

> **English** | [简体中文](../zh/works/evo-bench.md)

## Overview

Evo-Bench is a benchmark that evaluates a language model's intrinsic ability to autonomously improve its own agent harness — the editable scaffolding that governs how the model reasons and interacts with tools — across Search, Office, and General agent domains.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General-purpose agent harness-self-improvement benchmark over Search/Office/General settings; no scientific or engineering task evaluated.

## Links

- **Paper:** https://arxiv.org/abs/2608.09096
- **Venue:** arXiv preprint (2026)

## Summary

Evo-Bench targets "harness evolution": rather than solving a fixed task, the model iteratively edits an operating harness that controls how a policy interacts with tasks, and is scored on how much the evolved harness improves downstream performance. The benchmark is constructed through a harness-guided pipeline that first identifies tasks genuinely sensitive to harness quality, then applies sensitivity-aware stratified splitting into a validation suite and an evaluation suite to isolate harness-improving skill from base-model strength and task-specific overfitting. The seed harness the model starts from is a minimal CodeAct loop with only shell execution and answer completion. Tasks are drawn from five source benchmarks spanning three domains: Search, Office, and General.

## Tasks

608 tasks in total, split into a validation suite of 160 tasks (32 per source benchmark) and an evaluation suite of 448 tasks. The evaluation suite comprises 128 BrowseComp, 128 HLE, 64 GDPval, 64 APEX-Agents, and 64 Claw-Eval tasks. The five source benchmarks map to three domains: Search (BrowseComp, HLE), Office (GDPval, APEX-Agents), and General (Claw-Eval).

Construction (harness-guided framework):
- **Stage 1 — auxiliary harness generation.** 320 auxiliary tasks (128 search, 128 office, 64 general) are used to run independent harness evolution with four frontier models, from which 12 representative harnesses are selected via a diversity-aware procedure.
- **Stage 2 — harness-guided task selection.** 2,329 candidate tasks are evaluated under the 12 auxiliary harnesses; each task's "harness sensitivity" is computed as the correlation between task-level scores and overall harness quality. Tasks with non-positive sensitivity are filtered out, and stratified selection preserves the difficulty distribution.

## Domains

The benchmark spans three agent domains — Search (web browsing / information seeking), Office (document and workflow tasks), and General. These are general-purpose agent settings; no specific natural-science or engineering field is evaluated. Repository note: because the evaluated domains are Search / Office / General agent tasks rather than a science or engineering field, no canonical scientific or engineering domain is assigned.

## Evaluation

Each model acts as an "evolver" that iteratively edits its harness; the resulting harness is applied to the held-out evaluation suite and scored. Reported metrics include the **Overall Score** (performance on the evaluation suite), per-domain scores (Search, Office, General), and an **Anytime Validation Score**, defined as the average best-so-far validation performance over the evolution budget. Evolved harnesses are compared against a human-engineered ("Artificial Harness") baseline and the CodeAct seed baseline.

Headline results (overall score): the top model reaches 46.3 (a +16.6 gain over its seed), a second model reaches 45.8 (+16.1), the human-engineered baseline is 47.5, and the CodeAct seed baseline is 29.7. Nine frontier and open-weight models are evaluated: GPT-5.6 Sol, Claude Opus 4.8, GLM-5.2, Qwen3.7-Max, Minimax-M3, Deepseek V4 Pro, Kimi K2.7 Code (frontier), and Qwen3.6-27b, Gemma-4-31B (open-weight). Repository note: model-name strings are transcribed as reported in the primary source and are not independently corroborated here.

## Typical Duration

Each harness-evolution run is bounded by 20 iterations, 1,000 evolver steps, and 48 hours. Policy rollouts during evolution are capped at 300 steps and one hour.

## Main Contribution

The authors present Evo-Bench as the first benchmark designed to evaluate models' intrinsic harness-evolving capabilities, together with a harness-guided construction framework (auxiliary-task evolution plus sensitivity-aware stratified splitting) intended to isolate harness-improvement skill from base-model strength and task-specific overfitting.

## Key Design Ideas

- Frames evaluation around **harness self-improvement** rather than static task solving: the scored artifact is the harness the model edits, starting from a minimal CodeAct seed.
- **Harness-sensitivity filtering** retains only tasks whose scores correlate with overall harness quality, so measured gains reflect harness changes rather than raw capability.
- **Sensitivity-aware stratified splitting** into validation and evaluation suites to support cross-suite generalization and limit overfitting.
- **Anytime Validation Score** captures the best-so-far trajectory across the evolution budget rather than only the final harness.
- Bounded evolution budget (20 iterations / 1,000 steps / 48 hours) with capped policy rollouts (300 steps / 1 hour).

## Strengths

- Isolates a specific capability (harness improvement) from base-model strength through its construction pipeline and sensitivity filtering.
- Spans three distinct agent domains and five source benchmarks, evaluating both frontier and open-weight models.
- Reports trajectory-aware behavior (anytime validation, temporal anomalies such as early saturation) rather than only a final score.

## Limitations

- Authors report that autonomous evolution struggles on Office tasks that demand highly specific processing workflows, and note temporal anomalies such as early saturation.
- Evolved harnesses approach but do not exceed the human-engineered baseline overall (best 46.3 vs. 47.5).
- Repository note: several evaluation numbers and model-name strings were obtained via automated extraction from the primary source; task-count arithmetic is internally consistent (32×5 = 160; 128+128+64+64+64 = 448; 160+448 = 608), but individual result values should be reconfirmed against the paper before citation.

## Related Works

- [UniClawBench](./uniclawbench.md) — Claw-Eval, one of Evo-Bench's General-domain source benchmarks, comes from the same Claw evaluation line.
- [GAIA](./gaia.md) — another general-purpose long-horizon agent benchmark spanning browsing and tool use.
- [Frontier-Eng](./frontier-eng.md) — also frames the horizon as an iterative propose-evaluate optimization trajectory under a fixed budget.
