# AutoWorldModel-Bench (2026)

> **English** | [简体中文](../zh/works/autoworldmodel-bench.md)

> **First appeared:** 2026-07-20 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.11216)

## Overview

AutoWorldModel-Bench is a closed-loop benchmark in which a frontier coding agent is handed a working world model and a fixed compute budget and asked to make it better, with no improvement direction specified in advance. Eight game environments share a unified structured-state representation that strips out perception, isolating dynamics modeling and keeping each training run short enough for many iterations inside a session.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.11216>
- **Project:** <https://electronicarts.github.io/AutoWorldModelBench/> (CC BY-NC-ND 4.0)
- **Venue:** arXiv preprint (submitted July 2026; v2 August 2026).

## Summary

The authors argue that world modeling is a good testbed for autonomous research precisely because it is unsettled: architectures, training objectives and state representations interact in complicated ways and no recipe dominates across environments, so there is no specification to code to. That distinguishes it from the engineering-to-spec tasks that dominate current agent benchmarks. The benchmark supplies a single-file base world model — one of four architectures — and asks the agent to improve it however it sees fit, whether by changing the architecture, the loss, the hyperparameters or the training procedure. All eight games expose ground-truth entity state through a shared tensor format, so the agent never confronts pixels and the measured quantity is transition modeling over known entities. Runs are short by design, allowing minutes-per-run iteration inside a bounded session. Beyond the aggregate improvement rates, the paper audits *what kind* of edit won each session, finding that in the overwhelming majority the winning change was substantive rather than a hyperparameter tweak.

## Tasks

**Eight game environments** — Snake, Frogger, Pong, Breakout, Asteroids, Platformer, Kong and Racer — under a unified entity-component-system snapshot representation. Each frame carries an entity registry (**N × 34** dimensions), entity state (**N × 23**), player action (**7D**), game state (**17D**) and a terminal flag.

The provided base is one of four single-file, agent-modifiable architectures: **RSSM/Dreamer, AR-Transformer, D3PM, or MaskGIT**. The agent's task is to autonomously improve that base under a fixed compute budget, free to modify architecture, loss, hyperparameters or training procedure. The full grid is **64 sessions** — 2 agents × 8 games × 4 bases.

## Domains

**AI & Machine Learning Research.** The evaluated object is a learned world model and the agent's work is machine-learning research — architecture, loss and training-procedure changes measured by held-out predictive accuracy. The game environments are a substrate for generating dynamics, not a domain of study in themselves, so no other canonical domain is assigned.

## Evaluation

The test metric is a composite of **Position L1** over mutable entity positions and **Alive F1**, evaluated at horizons **h ∈ {1, 10, 20}** and combined as **0.1 · composite₁ + 0.2 · composite₁₀ + 0.7 · composite₂₀** — weighting long-horizon rollout fidelity most heavily. Δ is the session-best improvement over the base on the **held-out test split**.

Across **64 sessions**, Codex-5.4 and Claude Opus 4.6 improve on the base in all but one session. **33 of 64** achieve a substantial gain (**Δ ≥ +0.10**); the remainder are smaller but positive. Mean test-score lift is **+0.196**, median **+0.115**. On a separate scenario suite, improvements appear in **56 of 64** sessions at mean **+0.170**. Gains concentrate at long horizons — mean **+0.205** at h₁₀ and **+0.215** at h₂₀ against only **+0.056** at h₁.

The head-to-head between the two agents splits **19–13 in favour of Codex-5.4**, which the paper reports as not statistically significant (**Wilcoxon p = 0.15**).

An edit-type audit finds that in **91% of sessions** the winning change was a substantive modification to the model or training rather than a hyperparameter tweak.

## Typical Duration

**A 6-hour session on a single H100 GPU**, with a **10-minute wall-clock cap on each individual training run**. The short per-run cap is what makes minutes-per-run iteration possible within the session budget.

## Main Contribution

An open-ended research benchmark where the improvement direction is deliberately unspecified, made tractable by removing perception from the problem and capping individual runs at ten minutes — plus the accompanying audit showing that in 91% of sessions the winning edit was substantive rather than a hyperparameter tweak, which is the paper's evidence that agents are doing research rather than search.

## Key Design Ideas

- The task is defined by an objective without a specification, which is the property the authors use to separate it from engineering-to-spec agent benchmarks.
- Ground-truth structured state from the game engine removes perception entirely, so a failure is attributable to dynamics modeling rather than to representation learning.
- A 10-minute cap per training run — rather than a cap on the number of runs — converts the compute budget into iteration count, rewarding agents that test many hypotheses.
- Four distinct base architectures per game prevent the benchmark from measuring skill at improving one particular model family.
- The composite metric weights the 20-step horizon at 0.7, so gains must come from rollout fidelity rather than from one-step prediction that several bases already do well.
- Auditing whether the winning edit was substantive or a hyperparameter tweak is a direct check on the benchmark's own claim to measure research rather than tuning.
- A separate scenario suite provides a second, differently constructed measurement of the same improvements.

## Strengths

- Scoring is fully automatic against a held-out split with no judge in the loop.
- The edit-type audit tests the benchmark's central claim rather than assuming it, and reports a specific rate (91%).
- Removing perception is a deliberate narrowing that makes the measured quantity clean, and the authors state the cost of that choice explicitly.
- Both the aggregate (33 of 64 at Δ ≥ +0.10) and the distribution (mean +0.196, median +0.115) are reported, so the skew is visible.
- The head-to-head between agents is reported with a significance test and correctly described as inconclusive, rather than presented as a ranking.
- Per-horizon decomposition shows where the gains come from, making the h₁ versus h₂₀ asymmetry legible.

## Limitations

- The authors note the comparison covers model *and* harness together, so it does not isolate model quality.
- Explicit structured state from the game engine limits the benchmark to transition modeling over known entities, and the state is exact — no sensor noise, missing values or measurement error.
- One-step prediction is already strong for many bases, so headroom is concentrated at long horizons by construction.
- Per-cell magnitudes carry seed sensitivity, and the authors report that magnitude varies on some cells, especially for strong bases.
- Environments are games rather than scientific systems, so the dynamics being modeled are authored rather than natural.
- The CC BY-NC-ND license is non-commercial and prohibits derivatives, which restricts reuse relative to a permissively licensed benchmark.

## Related Works

- [Beyond Final Scores](./beyond-final-scores.md) — Also has agents improve a provided artifact under a wall-clock budget in AI R&D, adding deterministic process metrics and a novelty audit.
- [MLE-bench](./mle-bench.md) — Machine-learning engineering under compute budget, with the improvement direction largely fixed by a Kaggle-style objective.
- [PACE-Bench](./pace-bench.md) — Also starts the agent from a working artifact under a bounded budget, requiring repair after an environment change rather than open-ended improvement.
- [Replica](./replica.md) — Research capability measured against a published result rather than against an agent's own starting artifact.
