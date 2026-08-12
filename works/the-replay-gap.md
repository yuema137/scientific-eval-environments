# The Replay Gap (2026)

> **English** | [简体中文](../zh/works/the-replay-gap.md)

## Overview

An evaluation-methodology study showing that the standard way of scoring per-step model routing/switching in multi-step LLM agents — replaying a logged trajectory and substituting another model's recorded outputs — measures a counterfactual world that does not occur, and proposing branching (counterfactual) rollouts with matched same-model control forks as the sound alternative.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


N/A — Evaluation-methodology study of per-step agentic model routing; SWE-bench software repair is only the experimental substrate, not an evaluated scientific/research task.

## Links

- **Paper:** https://arxiv.org/abs/2608.08239
- **Code:** https://github.com/AshrithaG/replay-gap
- **Dataset:** https://huggingface.co/datasets/ashritha0907/replay-gap-trajectories
- **Venue:** Conference on Language Modeling (COLM) 2026

## Summary

LLM routers aim to serve each request with the cheapest adequate model and are increasingly applied per step inside multi-step agents, yet agentic routers are commonly evaluated like single-turn routers: by replaying logged trajectories and swapping in another model's recorded outputs while assuming the rest of the trajectory is unchanged. This work tests that assumption directly with branching rollouts — forking live SWE-bench agent trajectories at controlled points, rebuilding the environment, and continuing each fork with a different model — and compares swaps against matched same-model control forks that isolate sampling and replay noise. Across six paired runs (~900 rollouts), model swaps diverge from their matched control floors by large margins and rewrite the majority of subsequent actions, and a log-stitching replay evaluator mispredicts every success-relevant outcome. The authors conclude that replay-based benchmarks "score the wrong world" for agentic routing and release their harness and trajectory data.

## Tasks

Not a task benchmark; a methodology/measurement study built on an existing benchmark. The substrate is SWE-bench Verified software-repair instances run with the mini-SWE-agent scaffold (a bash-only ReAct loop), under a 50-step budget and a 28k-token context, using the official per-instance Docker images. The experiment comprises six paired runs (forward/reverse switching directions across three difficulty tiers), ~900 total rollouts spanning 717 scored branch pairs, with 30 instances per run pair and 359 same-model control forks. Base trajectories are forked at controlled depths (reported at 30% and 70% of trajectory length): a "control fork" continues with the same model to isolate sampling and environment-replay noise, while a "swap arm" continues with the alternative model to measure the routing counterfactual. Models: a small model (Qwen3-4B-Instruct, FP8-quantized) and a large model (Qwen3-14B, AWQ-quantized), served via vLLM on a single 24GB GPU at temperature 0.

## Domains

Software & Systems — the testbed is SWE-bench Verified software-repair tasks executed in per-instance Docker environments. Repository note: the paper's contribution is an evaluation-methodology critique of agentic model routing; software engineering is the experimental substrate rather than the object of study.

## Evaluation

Divergence between a fork and its base/control is measured with normalized edit distance over post-fork action sequences, plus the fraction of post-fork actions rewritten, the fraction of forks diverging at the first post-fork action, and the fraction of replayed states that remain valid. Multiplicity-corrected 95% confidence intervals are used to test whether swap effects exceed matched control floors. Task success uses the SWE-bench outcome (instance solved/unsolved), and "outcome flips" between swap and control are tracked. A log-stitching replay evaluator is compared against live rollouts by patch similarity to the patch the switch actually produces.

## Typical Duration

Per rollout: up to a 50-step agent budget with a 28k-token context window; models served at temperature 0 on a single 24GB GPU. The full study comprises ~900 rollouts across six paired runs. Exact wall-clock time per rollout: `TODO(reference)`.

## Main Contribution

The paper argues that static/replay evaluation of per-step model switching in agents is unsound because a swapped model changes the downstream trajectory, so log-stitching scores a world that never runs. It introduces branching counterfactual rollouts with matched same-model control forks to attribute divergence to the swap (versus sampling and replay noise), and it quantifies the resulting "replay gap," showing replay mispredicts success-relevant outcomes.

## Key Design Ideas

- **Branching rollouts.** Execute a base trajectory to completion, then re-fork at controlled depths in fresh containers, replaying pre-fork actions before continuing.
- **Matched control forks.** Same-model continuations that isolate sampling nondeterminism and environment-replay drift, giving a per-condition noise floor for attribution.
- **Swap arms vs. control floors.** Swap-induced divergence is judged as the excess over its matched control floor, with multiplicity-corrected confidence intervals.
- **Direct replay-evaluator audit.** A log-stitching replay evaluator is scored against live branching outcomes by patch similarity and by success-relevant outcome calls.
- **Noise-floor audit of "determinism."** Temperature-0 determinism is checked per serving stack (FP8 vs. AWQ quantization) rather than assumed.

## Strengths

- Tests the replay assumption empirically with a live, environment-rebuilding harness rather than argument alone, and isolates the swap effect with same-model controls (six paired runs, ~900 rollouts, 359 control forks).
- Swaps exceed their matched control floors by +0.25 to +0.66 normalized edit distance (multiplicity-corrected CIs exclude zero) and rewrite 61–94% of post-fork actions; 74–77% of early swaps diverge at the first post-fork action versus 6–35% of controls, leaving only ~3% of replayed states valid for early forks.
- All five observed outcome flips occur in swap arms (upgrades rescuing unsolved instances, a downgrade losing the sole solve) and zero occur across 359 control forks, tying the methodological point to success-relevant consequences.
- Direct evaluator audit: the replay evaluator's predicted patch has 0.00–0.11 similarity to the patch the switch actually produces and mispredicts every success-relevant call.
- Surfaces a serving-stack confound: FP8-served controls diverge on over 90% of forks at temperature 0 while AWQ-served controls diverge far less, showing "determinism" is configuration-dependent.
- Releases the harness (GitHub) and trajectory dataset (HuggingFace) for reuse.

## Limitations

- Repository note: the study uses a single agent scaffold (mini-SWE-agent) and one benchmark (SWE-bench Verified) with two specific quantized models (Qwen3-4B FP8, Qwen3-14B AWQ), so the magnitude of the replay gap on other scaffolds, tasks, or model pairs is not established by this evidence.
- Repository note: forks are taken at two controlled depths (≈30% and 70%) at temperature 0; behavior at other depths, sampling temperatures, or step/token budgets is outside the reported settings.
- Repository note: divergence is measured largely by action-sequence edit distance and patch similarity; these are proxies for behavioral difference and do not by themselves quantify downstream cost or utility of routing.

## Related Works

- [SWE-bench](./swe-bench.md) — the software-repair benchmark whose Verified subset is the experimental substrate for the branching-rollout study.
