# FormalRewardBench (2026)

> **English** | [简体中文](../zh/works/formalrewardbench.md)

## Overview

FormalRewardBench is a benchmark that evaluates reward models on their ability to prefer a correct Lean 4 proof over an incorrect one. It consists of 250 preference pairs in which a formally verified proof is paired with an incorrect variant produced by one of five expert-curated error injection strategies.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.10141>
- **Code:** <https://github.com/GGLAB-KU/formal_rewardbench>

## Summary

FormalRewardBench addresses the sparse credit assignment problem in reinforcement learning with verifiable rewards, where a proof attempt that makes substantial progress but fails at the final step receives the same zero reward as a completely wrong approach. The authors argue that this sparsity motivates learned reward models able to judge proof quality beyond binary verification, but that comparing such reward models normally requires expensive RL training ablations. They introduce FormalRewardBench as the first benchmark for evaluating reward models in formal theorem proving with Lean 4, and run it over frontier LLMs, judge LLMs, general-purpose LLMs, and specialized theorem proving models.

## Tasks

250 preference pairs, 50 sampled from each of five error injection strategies: minimal single-point variations, natural language justification, Python code injection, forced LLM mistakes, and verbose incorrect proofs. Theorem statements come from MiniF2F, a set of 488 olympiad-level problems formalized in Lean 4 and drawn from AMC, AIME, and IMO competitions. Correct proofs are sourced from DeepSeek-Prover-V2-671B, incorrect variants are generated with Claude Opus 4.5 as the prompting model, and candidates pass syntactic, type-check-failure, and triviality filters before sampling.

## Domains

Formal mathematics in Lean 4: olympiad-level algebra, number theory, and combinatorics.

## Evaluation

- **Pointwise accuracy.** The model scores each proof independently; a sample counts as correct when the score given to the correct proof exceeds the score given to the incorrect one.
- **Pairwise accuracy (position-consistent).** The model compares the two proofs directly, and a sample counts as correct only when the judgment is correct under both presentation orderings.
- **Position bias analysis.** Accuracy is reported separately for the correct-proof-first and correct-proof-second orderings, alongside consistency and agreement rates.
- **Per-strategy breakdown.** Pairwise accuracy is reported for each of the five error injection strategies, exposing a difficulty gradient with Python code injection easiest and verbose incorrect proofs and forced LLM mistakes hardest.
- **Reported.** Claude Opus 4.5 leads at 70.1% pointwise and 59.8% pairwise; the strongest specialized prover, Gödel-Prover-V2-32B, reaches 24.4% pairwise, and DeepSeek-Prover-V2-7B reaches 13.7% pointwise and 9.4% pairwise. The best model reaches 60% on verbose incorrect proofs and 50% on forced LLM mistakes. The authors report that most models perform at or below the random baseline.

## Typical Duration

Single-turn preference judgments over complete proofs; there is no interactive horizon or multi-step rollout. Not stated: no per-item wall-clock, step, or token budget is given.

## Main Contribution

A benchmark of 250 Lean 4 preference pairs built by expert-curated error injection, allowing reward models for formal theorem proving to be compared directly without expensive RL training ablations.

## Key Design Ideas

- Controlled difficulty through synthetic error injection into formally verified correct proofs.
- Five error injection strategies targeting distinct reward-model weaknesses: minimal single-point variations, natural language justification, Python code injection, forced LLM mistakes, and verbose incorrect proofs.
- Objective preference labels from Lean's type checker for the strategies that route through Lean — the correct proof passes it and the incorrect variant fails it.
- Paired pointwise and pairwise protocols, with pairwise accuracy requiring a consistent judgment across both presentation orderings.

## Strengths

- Type-checker-derived labels give deterministic ground truth without human preference annotation.
- Error strategies are kept separate, so per-category results localize which failure mode a reward model is vulnerable to.
- Covering frontier, judge, general-purpose, and prover-specialized models under one protocol exposes a generation–evaluation gap that evaluating a single model family would not reveal.

## Limitations

- Repository note: Judgments are whole-proof and single-turn — the paper states that it does not consider process-level or step-by-step evaluation, so credit is assigned to a complete proof rather than to individual tactic steps.
- Repository note: Labels rest primarily on automatic verification, with the authors manually inspecting 50 of the 250 pairs; all pairs are MiniF2F problems in Lean 4, so transfer to other proof assistants is not evaluated.

## Related Works

- [AgentBoard](./agentboard.md) — Also motivated by the coarseness of a single binary outcome, but credits annotated subgoals inside a trajectory rather than scoring a complete proof as one unit.
- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Also targets sparse binary end-task reward, but supplies dense partial credit through graded subtasks rather than benchmarking the reward models that would supply a denser signal.
- [TRACE](./trace.md) — Also puts a learned judge at the core of scoring, but uses the judge as the instrument for grading trajectories rather than making the judge the subject under evaluation.
