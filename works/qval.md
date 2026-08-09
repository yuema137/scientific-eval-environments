# QVal (2026)

> **English** | [简体中文](../zh/works/qval.md)

## Overview

QVal is a training-free evaluation methodology and testbed that scores dense supervision signals by how well they order an agent's candidate actions according to the Q-values of a strong reference policy. It is instantiated as QVal-v1.0, which benchmarks 21 dense supervision methods from seven methodological families across four environments and six open-weight model backbones.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.32034>
- **Project:** <https://q-val.com>
- **Code:** <https://github.com/bethgelab/qval>

## Summary

QVal addresses the common practice of evaluating dense supervision methods by the downstream performance of a training pipeline that integrates them, which the authors argue is expensive, conflates supervision quality with training-engineering confounders, and leaves methodological families requiring distinct training setups incomparable. Given a state-action pair, QVal measures whether a method's score is Q-aligned — whether it orders actions as the Q-values of a strong reference policy do — so that signals can be compared before any training run. QVal-v1.0 covers 21 dense supervision methods, seven methodological families, four environments and six open-weight model backbones in over 1.2K evaluation experiments, and finds that simple prompting baselines consistently outperform recent dense supervision methods from the literature.

## Tasks

21 dense supervision methods across seven methodological families — ranking, direct, intrinsic scoring, self-distillation, pre-trained, embedding, and code — are the units under test, scored over labelled state-action pairs collected from four environments. States are sampled from a range in the middle of each collected trajectory, excluding very early and very late states, and each state is paired with four candidate actions: the trajectory's own action plus three sampled alternatives. Per-environment sample sizes are tabulated in an appendix rather than stated in the main text.

## Domains

Goal-directed navigation, embodied reasoning, browser-based computer use, and terminal-based problem solving — FrozenLake, ALFWorld, OpenApps, and TerminalBench, of which TerminalBench is text-only and the rest supply both textual and visual observations.

## Evaluation

- **Q-alignment.** A method's score is Q-aligned when it is a strictly increasing transform of the reference Q-value, so that it orders the candidate actions at a state exactly as the reference values do.
- **Spearman's ρ.** The primary metric, reported both globally and per state then averaged across states; Kendall's τ is reported in an appendix.
- **Reference values.** The reference policy is environment-specific: scripted optimal policies for FrozenLake and OpenApps, an expert planner for ALFWorld, and Max-Value Monte-Carlo rollouts with k = 16 using GPT-5.5 for TerminalBench, where an optimal policy is intractable to find. To label a point, the environment is restored to the recorded state, the first continuation step is forced to the dataset action, and the reference policy is then followed to record the discounted return.
- **Robustness checks.** Text-vs-image observations, Q-value vs. state-value targets, and GPT-5.5 vs. Claude Opus 4.7 as the Monte-Carlo backbone for the TerminalBench labels, which produce closely matching method correlations.
- **Reported.** Ranking and direct prompting achieve the highest degree of Q-alignment across environments and backbones; within a family, more elaborate variants do not reliably improve Q-alignment; and direct-prompting methods stay positive everywhere, including TerminalBench. Numeric correlation values are carried in the figures rather than stated in the main text.

## Typical Duration

Offline scoring over a fixed set of labelled state-action pairs, with no training run required. Not stated: no wall-clock, step, or token budget for a QVal run is given, and no cost figure is reported.

## Main Contribution

A training-free methodology that evaluates dense supervision methods by their Q-alignment — how well their scores rank intermediate actions against reference values — so that a question which previously required a training run becomes a cheap offline evaluation.

## Key Design Ideas

- Q-alignment as the evaluation target: a signal is judged by whether it orders candidate actions as reference Q-values do, not by the downstream performance of a training pipeline.
- Environment-specific reference policies: scripted optimal policies for FrozenLake and OpenApps, an expert planner for ALFWorld, and Max-Value Monte-Carlo rollouts with GPT-5.5 for TerminalBench.
- Labelling by environment restoration — replay to the recorded state, force the dataset action, then follow the reference policy and record the discounted return.
- A fixed backbone and an identical supplied context across methods — task description, environment dynamics, reward specification, and state and action space descriptions — so that differences in Q-alignment reflect the scoring method rather than the model.

## Strengths

- Separating signal quality from training-pipeline engineering lets methodological families that need different training setups be compared on common ground.
- A single score per state-action pair is the whole interface a new method must satisfy, which keeps the testbed cheap to extend to further methods and environments.
- Holding the backbone and the supplied context fixed across methods isolates the scoring signal from the underlying model's competence.

## Limitations

- Repository note: The paper's own discussion states that signal quality is not the only component affecting the effectiveness of RL post-training and is not isolated from the rest of the pipeline, so a high Q-alignment score does not on its own establish that a signal will improve a training run.
- Repository note: Numeric Spearman and Kendall values are carried in figures and the appendix rather than in the main text, and per-environment sample sizes sit in an appendix table — the headline findings are therefore recorded here qualitatively rather than as numbers.

## Related Works

- [AgentBoard](./agentboard.md) — Also assigns credit below end-task success, but from human-annotated subgoal progress within an agent benchmark rather than from reference Q-values used to rank external scoring methods.
- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Also produces dense intermediate reward on long-horizon tasks, but by grading subtasks the benchmark itself defines rather than by judging third-party supervision methods.
- [TRACE](./trace.md) — Also treats intermediate trajectory content as a first-class evaluation object, but scores a whole deep-research trajectory with a hierarchical utility function rather than ranking candidate actions at a single state.
