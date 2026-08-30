# TempoBench (2025)

> **English** | [简体中文](../zh/works/tempobench.md)

> **First appeared:** 2025-10-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.27544)

## Overview

A formally verifiable temporal benchmark that isolates *counterfactual causal attribution* over execution trajectories, testing whether LLMs can identify which inputs were necessary for an observed output rather than merely simulating a system forward.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities


N/A — Abstract counterfactual causal-attribution reasoning diagnostic over synthetic Mealy-machine traces; a reasoning-capability probe, not a scientific/research activity.

## Links

- **Paper:** https://arxiv.org/abs/2510.27544
- **Venue:** arXiv preprint (2025; cs.AI, cs.FL)

## Summary

TempoBench is built from synthesized deterministic Mealy machines, which give an infinitely scalable corpus of trajectory-based causal-reasoning problems with controllable complexity and provably correct causal labels. It separates two abilities: forward *simulation* of an execution trace, and identification of the *minimal necessary cause* of an observed output. The authors report that frontier models simulate systems forward accurately but fall sharply when asked which inputs were necessary for an observed output — a disparity they name the SIM/MIN gap — often confusing "possible inputs" with "necessary causes." The paper also reports that fine-tuning open-source models on TempoBench data yields targeted gains on external causal benchmarks while preserving general-purpose, math, and code performance.

## Tasks

Problems are generated from synthesized deterministic **Mealy machines**, yielding an infinitely scalable corpus with controllable complexity and provably correct causal labels. The benchmark defines two task types over an execution trajectory:

- **Forward simulation (SIM)** — given a machine and an input sequence, produce the execution trace (per step: input read, output produced, resulting state).
- **Minimal necessary cause (MIN)** — identify the minimal set of input conditions that were necessary for a given observed output, which requires counterfactual reasoning over alternative inputs.

Exact corpus size, per-difficulty splits, and complexity parameters (state counts, trace lengths): `TODO(reference)`.

## Domains

N/A — the benchmark is built from abstract deterministic Mealy machines used as synthetic causal-reasoning problems; it does not evaluate a scientific or engineering field. The authors motivate it by downstream causal-inference tasks such as debugging, root-cause analysis, and task planning.

## Evaluation

Deterministic, formally verifiable scoring against provably correct labels computed from the underlying Mealy machine: simulation traces are checked step-by-step, and minimal-necessary-cause answers are checked against the causal set derived by counterfactual attribution (negating candidate input conditions and testing whether the output changes under the machine's dynamics). Reported headline results: frontier models reach **96% step accuracy** on forward simulation and fall to **32%** when asked which inputs were necessary for an observed output — the **SIM/MIN gap**. Model list and per-model breakdowns: `TODO(reference)`.

## Typical Duration

`TODO(reference)` — per-problem trajectory lengths and token budgets not verified from the primary source.

## Main Contribution

Introduced as the first formally verifiable temporal benchmark that isolates counterfactual causal attribution over execution trajectories, and used to show that LLMs categorically fall back to brute-force simulation-based reasoning when asked to reason causally — quantified by the SIM/MIN gap — establishing that identifying minimal necessary causes is a distinct capability from forward simulation.

## Key Design Ideas

- **Synthesized deterministic Mealy machines** as problem generators, giving an infinitely scalable corpus with controllable complexity.
- **Provably correct causal labels** computed directly from the machine, so causal attribution is checked against ground truth rather than a judge.
- **SIM vs. MIN separation** — forward trace simulation and minimal-necessary-cause identification are evaluated as distinct tasks, isolating counterfactual attribution.
- **The SIM/MIN gap** as a diagnostic: the drop from forward-simulation accuracy to minimal-cause accuracy exposes reliance on simulation over causal understanding.
- **Transfer via fine-tuning** — training on TempoBench data reportedly improves open-source models on external causal benchmarks while preserving general-purpose, math, and code performance.

## Strengths

- Ground-truth causal labels are computed from a formal model, avoiding dependence on human or LLM judges (per paper).
- The generative construction is described as infinitely scalable with controllable complexity, so difficulty can be tuned and the corpus extended (per paper).
- Cleanly separates forward simulation from counterfactual attribution, isolating a specific reasoning failure mode (per paper).

## Limitations

- Reported minimal-necessary-cause accuracy is low even for frontier models (≈32%), indicating counterfactual causal attribution remains largely unsolved (per paper).
- Repository note: problems are abstract Mealy-machine trajectories; the connection to real-world debugging, root-cause analysis, and task planning is a motivation stated by the authors rather than an evaluated setting.
- Repository note: several structural quantities (corpus size, evaluated model list, per-model and per-difficulty numbers) could not be verified from the primary source in this pass and are marked `TODO(reference)`.

## Related Works

- [Long-Horizon Agent Trajectory Attribution](./long-horizon-agent-trajectory-attribution.md) — also attributes an observed outcome to responsible components of a trajectory, but over LLM-agent trajectories rather than formal Mealy-machine execution traces.
- [ProcessBench](./processbench.md) — another attribution-over-reasoning benchmark, localizing the earliest erroneous step in a static solution rather than the minimal necessary cause of an output.
