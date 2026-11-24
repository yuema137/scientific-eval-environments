# Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents (2026)

> **English** | [简体中文](../zh/works/trace2tower.md)

> **First appeared:** 2026-09-04 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.05261)

## Overview

Trace2Tower turns an LLM agent's past trajectories into a three-level skill library (action skills, procedure skills, strategy skills) and uses each trajectory's success or failure label to decide which behavioral patterns enter the library. Earlier experience-reuse methods retrieve whole trajectories or write flat skill summaries; here the outcome labels weight the transition graph from which skills are extracted, and later edits to the library are accepted only if a paired comparison on task outcomes does not reject them. The paper tests the change by giving the induced skills to a fixed "Skill User" model on ALFWorld and WebShop and comparing success, step count, invalid actions, and context size against no-skill, expert-written, and other skill-induction baselines.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities


N/A — Skill-induction method evaluated on general embodied household (ALFWorld) and web-shopping (WebShop) tasks; no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2609.05261>
- **Code:** <https://github.com/FudanSELab/Trace2Tower>
- **Venue:** arXiv preprint, September 2026

## Summary

A Skill Author model (GPT-5.4) segments each raw trajectory into canonical events, then builds a graph whose edges are observed event transitions. Each edge combines semantic compatibility, transition frequency, and outcome evidence, computed separately over successful and failed trajectories; a trajectory counts as successful when its primary benchmark score is at least 0.999. A contrastive transform keeps edge weight that success supports and suppresses weight concentrated in failures, and spectral clustering of the resulting graph yields procedure skills; maximal paths over procedures supported by successful edges become strategy skills. At deployment the Skill User retrieves skills under a token budget, ranking them by smoothed success reliability. The evidence is limited to two simulated household and web-shopping environments with a 20-step horizon.

## Tasks

N/A — method paper; it introduces no new task suite. Experiments use existing benchmarks:

- **ALFWorld:** all 134 solvable `valid_unseen` tasks across six task families. Skills are induced from 1,240 No-Skill trajectories over 310 training tasks (4 rollouts per task).
- **WebShop:** a fixed 100-task test manifest. Skills are induced from 400 trajectories over 100 training tasks.

## Domains

General embodied household interaction (ALFWorld) and web shopping (WebShop); no canonical science or engineering domain is evaluated.

## Evaluation

The Skill User (DeepSeek-V4-Flash by default, temperature 0, at most 512 output tokens) acts in the environment with retrieved skills in its context, under a 20-step horizon. One ALFWorld episode is scored by the environment's completion indicator; the run also records steps, invalid actions, input tokens, and characters of skill context. WebShop episodes report exact success (official reward at least 0.999), reward, and invalid actions. Results are mean ± SD over three runs.

Reported main results (Trace2Tower Full):

- **ALFWorld:** 87.31 ± 0.75% success, 10.35 steps, 0.26 invalid actions, 44,651 input tokens, 3,623 skill characters. Comparison rows: No-Skill 46.27%, Expert-Crafted 71.39%, Trace2Skill (+Combined) 61.44%, SkillX 78.61%, ExpeL 81.59%. The High-only variant (strategy skills only) reaches 84.83% with 1,966 skill characters.
- **WebShop:** 50.67 ± 2.89% exact success, reward 0.7115, 0.27 invalid actions; SkillX 49.33%, ExpeL 48.00%, Expert-Crafted 48.00%, No-Skill 40.67%.
- Relative to SkillX on ALFWorld, the paper reports 30.5% fewer input tokens and 63.9% less skill context.

Ablations on ALFWorld (single 134-task evaluation each): removing transition evidence gives 70.15%, removing outcome evidence 73.88%, removing the contrastive transform 73.88%. Verifier-guided refinement raises pooled success on two held-out ALFWorld sets of 120 tasks each from 80.42% (frozen tower) to 84.58% (TF-IDF Pareto selection) or 83.75% (embedding selection), using 10,000 paired bootstrap resamples. Cross-model transfer: with the Flash user, a GPT-5.4-authored tower reaches 88.06% against 65.67% for a Flash-authored tower; with DeepSeek-V4-Pro as user, 85.82% against 79.10% (p = 0.150, not significant).

## Typical Duration

Episodes are capped at 20 steps; the full method averages 10.35 steps on ALFWorld. Wall-clock time and induction cost are `TODO(reference)`.

## Main Contribution

A transition-aware, outcome-contrastive way to induce a multi-level skill hierarchy from execution traces, with a refinement stage that edits the hierarchy only when paired task outcomes support the edit.

## Key Design Ideas

- Edge affinity is the geometric mean of semantic compatibility, transition probability, and outcome evidence, computed separately for successful and failed trajectories, with no learned mixing weights.
- The contrastive transform `Ā_uv = (A⁺_uv)² / (A⁺_uv + A⁻_uv)` keeps success-supported transitions and down-weights failure-prone shortcuts without a tuned threshold.
- Spectral clustering with an eigengap rule chooses the number of procedure skills per connected component.
- Three skill levels: canonical events (action), spectral clusters (procedure), and success-supported procedure paths (strategy).
- Four refinement operators (Split, Merge, Promote, Downweight) are filtered by Pareto non-dominance over semantic relevance, structural relevance, and feedback evidence, then gated by paired outcomes; rejected updates roll back.
- Retrieval maximizes `Σ log(1 + ζ·ϱ)` under a token budget, where `ϱ = (n⁺+1)/(n+2)` is a skill's smoothed success reliability.

## Strengths

- Ablations isolate the contribution of transition evidence, outcome evidence, and the contrastive transform (paper, ALFWorld).
- Reports context cost (input tokens, skill characters) alongside success, so gains can be weighed against prompt size (paper).
- Compares skill levels directly: High-only versus Full on both benchmarks (paper).

## Limitations

- The paper states that representation quality is sensitive to the Skill Author model; the Flash-authored tower is 22.39 points below the GPT-5.4-authored tower with the Flash user.
- Structural ablations are single evaluations without run-to-run variance (paper).
- The paper does not specify the metric, threshold, or significance level of the paired bootstrap gate, nor does it define the shared task manifest used for refinement.
- The exact embedding model identifier was not recoverable from the source records (paper).
- Repository note: evaluation covers two simulated general-agent environments; no scientific or engineering task is tested.

## Related Works

- [SkillEvolBench](./skillevolbench.md) — benchmarks the same step this method performs: distilling episodic trajectories into reusable skills.
- [SkillLearnBench](./skilllearnbench.md) — scores automatically generated skills, the output type Trace2Tower produces.
- [HiPER](./hiper.md) — also separates high-level and low-level agent decisions on ALFWorld and WebShop, but through RL training rather than trace-derived skills.
