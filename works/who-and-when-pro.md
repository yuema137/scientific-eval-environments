# Who&When Pro (2026)

> **English** | [简体中文](../zh/works/who-and-when-pro.md)

> **First appeared:** 2026-07-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.09996)

## Overview

Who&When Pro is a benchmark that measures how well LLMs attribute a failed agent trajectory to the agent, the step, and the error mode responsible for it. It contains 12,326 failed trajectories whose labels are fixed by construction: every trace replays the prefix of a successful rollout exactly, then substitutes a single injected error.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.09996>
- **Project:** <https://whowhenpro.github.io>
- **Code:** <https://github.com/whowhenpro/whowhen_pro>

## Summary

Automated failure attribution asks an LLM to read a failed agent trajectory and say where and why it went wrong, and the authors argue that as agents become more capable their failures become subtler, which makes that judgement both harder to reach and harder to label. Who&When Pro builds its traces through a strictly controlled pipeline that replays the prefix of a successful rollout exactly, substitutes one erroneous action at a sampled step, and keeps the run only if it then ends in task failure, so the injected agent and step are the only controlled change separating success from failure. The benchmark holds 12,326 failed trajectories spanning 26 source benchmarks, 9 task categories, and 3 modalities, and the strongest judge reaches 73.9% step-level accuracy on text, while error-mode macro-F1 tops out at 22.2% on text and 40.0% on video.

## Tasks

12,326 failed trajectories. They span 9 task categories drawn from 26 source benchmarks and 15 agent frameworks, cover single-agent and multi-agent settings, and range from STEM question answering and data science to GUI interaction and video understanding. Each trace begins from a successful seed rollout: a sampler selects an injection step conditioned on a target failure mode, a frontier model reads the seed context and the task and writes an adaptive injection prompt for the erroneous action, the prefix is replayed to restore agent context and environment state, and the substituted action is then rolled forward.

## Domains

Recorded agent trajectories rather than a live environment — text, image, and video traces from single-agent and multi-agent systems across 9 task categories.

## Evaluation

- **Agent.** Accuracy at naming the agent responsible for the failure, scored on multi-agent traces only.
- **Step.** Exact-match accuracy at localizing the first decisive error step in the trace.
- **Error.** Macro-F1 over the failure-mode classes, taken from a taxonomy of 18 error modes covering perception, reasoning, planning, action, verification, and coordination failures.
- **Joint.** Fraction of traces on which the agent, step, and error-mode judgements are all correct at once.
- **Reported.** Judge models from closed-source and open-weight families are scored, including GPT-5.4, Claude Sonnet 4.6, Gemini 3 Flash, Grok 4.1, GLM-5, and Qwen3.5-122B; on text traces the highest step accuracy is 73.9% (Qwen3.5-122B), the highest joint score is 25.3% (GLM-5), and error-mode macro-F1 tops out at 22.2%. Step accuracy falls from 94% on traces under 3,000 tokens to 50% on traces beyond 12,000 tokens.

## Typical Duration

Traces average 7.5 steps and reach 50 steps at most, with 1,139 words per trace and 152 words per step on average. Not stated: attribution is scored offline over recorded traces, and no per-task wall-clock, step, or token budget for the judge model is given.

## Main Contribution

A large-scale benchmark for automated failure attribution in agentic systems, built by injecting a failure only after exactly replaying a successful prefix, so that each of its 12,326 failed trajectories carries golden agent, step, and error-mode labels.

## Key Design Ideas

- Warm-started injection: the prefix of a successful seed trajectory is replayed exactly to restore agent context and environment state before the erroneous action is substituted.
- Labels that follow from the intervention: because the injected error is the only controlled change turning a successful rollout into a failed one, the responsible agent and the decisive step are given by the injection point rather than by an annotator's judgement.
- Mode-conditioned step sampling: the injection step is drawn conditioned on the target failure mode, excluding steps that already carry execution errors or where the target mode cannot naturally occur, with position preferences differing by error family.
- Post-hoc filtering: only rollouts that end in task failure are retained, and traces are discarded when the erroneous action leaks construction artifacts or when the task's correct answer is already salient in context before the injection step.

## Strengths

- Ground truth comes from a controlled intervention rather than post-hoc annotation, which removes the annotator's guess about which step actually mattered.
- Coverage runs along axes that are usually collapsed — 26 source benchmarks, 9 task categories, 15 agent frameworks, and text, image, and video traces — so attribution can be compared across modality and framework instead of within one setting.
- Splitting the judgement into agent, step, error-mode, and joint scores separates locating a failure from explaining it, and the distance between the step and error-mode results is what the evaluation turns on.

## Limitations

- Repository note: Every failure in the benchmark is introduced by deliberate injection into an otherwise successful rollout, so the distribution of failures reflects the injection pipeline and the frontier model that wrote the erroneous actions, not failures that arose on their own.
- Repository note: The linked repository marks its code and data as not yet released, so the 12,326 traces cannot currently be inspected or re-scored independently.

## Related Works

- [AgentBoard](./agentboard.md) — Also spreads credit across a trajectory instead of scoring the final outcome alone, but credits the fraction of annotated subgoals a run completes rather than isolating the single step at which the run went wrong.
- [TRACE](./trace.md) — Also treats the whole trajectory as the object being scored, but grades an agent's own run with a hierarchical utility function rather than testing how well a judge can attribute someone else's failed run to a decisive step.
- [FinTrace](./fintrace.md) — Also decomposes a trajectory into several graded judgements instead of one pass/fail bit, but scores process and output quality along fixed dimensions rather than pinning a failure to one agent, step, and error mode.
