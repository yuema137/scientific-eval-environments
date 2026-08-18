# Beyond Final Scores (2026)

> **English** | [简体中文](../zh/works/beyond-final-scores.md)

## Overview

A systematic evaluation of seven frontier models on 36 long-horizon AI research and development tasks, built around the argument that final scores reveal neither where progress is gained or lost nor whether accumulated experience improves later decisions. It contributes a framework of deterministic rule-based process metrics over within-run behaviour, plus controlled counterfactual comparisons that isolate experience reuse within and across tasks.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.13417>
- **Code:** `TODO(reference)` — the paper does not state a release location for the framework or the task set.
- **Venue:** arXiv preprint (August 2026).

## Summary

The tasks come from AutoLab: each provides an objective, a correct but deliberately suboptimal starting artifact, an expert-written reference solution, a wall-clock budget and an automated verifier, and the agent's job is to improve the artifact iteratively. On top of that substrate the authors build two instruments. The first is a set of three rule-based metric families computed deterministically from verifier outcomes and recorded trajectory signals rather than from LLM judgments, characterising how an agent frames solutions, whether it reliably executes them, and how it responds to feedback. The second is a pair of counterfactual experiments on experience: within a run, the agent's accumulated context is erased at a mid-run branch point while the solution is preserved, and the next commit is compared against the unerased branch; across runs, lessons extracted from solved source tasks are supplied or withheld on held-out targets. The conclusion is that current agents behave like engineering optimizers rather than autonomous researchers — competent at formulating and implementing practical solutions, but highly variable across runs, mostly adapting established techniques, and rarely producing genuine methodological novelty.

## Tasks

**36 tasks from AutoLab** in four families: **Model Development (7)**, **System Optimization (15)**, **Puzzle & Challenge (10)** and **CUDA (4)**. Each provides an objective, a correct but suboptimal starting artifact, an expert-written reference solution, an automated verifier and a wall-clock budget of **2–12 hours**. Scores are normalised to **[0, 1]**, with verifier feedback available at each evaluated checkpoint. Total evaluation is **756 rollouts** (36 tasks × 7 models × 3 rollouts).

## Domains

**AI & Machine Learning Research.** The task families are model development, system optimization, CUDA kernel work and algorithmic challenges — the artifact being improved is a machine-learning model or the system code around it, and the verifier measures its performance. No science co-domain is assigned; the work evaluates research-and-development capability on AI artifacts rather than on any natural-science problem.

## Evaluation

Overall performance is reported as **avg@3 / best@3**: Opus-4.7 **0.739 / 0.790**, GLM-5.2 **0.682 / 0.757**, GPT-5.5 **0.663 / 0.772**, Gemini-3.1-Pro **0.652 / 0.750**, Kimi-K2.7-Code **0.587 / 0.729**, LongCat-2.0 **0.572 / 0.674**, DeepSeek-V4-Pro **0.502 / 0.668**. The seven models were evaluated June–July 2026 through provider APIs available at that time. The reliability finding falls directly out of these two columns: the strongest-to-weakest gap is **0.237 on avg@3 but only 0.122 on best@3**, so much of the apparent capability difference is run-to-run variance rather than ceiling.

Three deterministic metric families characterise within-run behaviour. **C1 Solution Framing** uses the running best verifier score as a proxy for whether pursued directions reach a strong solution quickly, mapped to a common horizon so that both height and earliness are rewarded and later failures cannot erase prior discoveries. **C2 Execution** gates on whether the artifact runs and is correct, discounting successful delivery by prior code-related build failures under a bound. **C3 Feedback Control** combines retention (final versus highest step score) with recovery (amount recovered and number of transitions), penalising hidden trial-and-error. For Opus-4.7 these read **0.612 / 0.967 / 0.920**.

Experience reuse is measured counterfactually. **Intra-task**: erasing accumulated context, disk notes and code comments at a mid-run branch point while preserving the solution, then comparing the first commit after the branch. Intra-task experience generally helps, with mean gains from **+0.0362 (Opus-4.7) to +0.1454 (LongCat-2.0)** — weaker models depend on it more. **Inter-task**: lessons extracted from four solved source tasks (one per category) are supplied or withheld on **19 target tasks, 32 retained for analysis**. Here initial performance does not predict improvement: the weakest baseline model, **DeepSeek-V4-Pro, gains most (+0.093 avg@3)** while the stronger **Gemini-3.1-Pro declines (−0.017 avg@3)**, and self-generated lessons beat cross-model transfer.

Two further findings bear on validity: after manual review only **three solutions (1.2%)** retain genuine novelty, while **16 (6.3%)** exploit evaluation-specific shortcuts. Harness substitution raises avg@3 by **0.019–0.055** but moves best@3 by at most **0.035** for any model.

## Typical Duration

**2–12 hours wall-clock per task**, inherited from AutoLab. Mean inference cost per task varies by roughly an order of magnitude across models: **Opus $89.9**, **GLM-5.2 $33.0**, **GPT-5.5 $16.5**, **DeepSeek-V4-Pro $4.3**, **LongCat-2.0 $3.9**. The full evaluation cost approximately **one hundred thousand U.S. dollars** in model inference. CUDA tasks are the most token-expensive category on average.

## Main Contribution

Process metrics for long-horizon agent runs that are computed deterministically from verifier outcomes and trajectory signals rather than from a judge, combined with counterfactual erasure experiments that turn "does experience help?" into a measured quantity — yielding the twin findings that the strongest-to-weakest model gap halves when measured at best@3 instead of avg@3, and that a model's baseline strength does not predict how much it gains from experience.

## Key Design Ideas

- Every process metric is computed from verifier outcomes and recorded execution signals, so the evaluation of the evaluation does not depend on an LLM judge.
- C1 maps running best score to a common horizon, which credits reaching a good solution *early* rather than only reaching it.
- C2 discounts successful delivery by prior build failures, so an agent that arrives via many broken intermediate states is not scored as equal to one that does not.
- C3 separates retention from recovery, distinguishing an agent that loses its own best work from one that recovers after a setback.
- Intra-task experience is measured by erasing context at a branch point while preserving the solution — isolating accumulated knowledge from accumulated progress, which a simple with/without-memory comparison would conflate.
- Reporting avg@3 alongside best@3 makes run-to-run variance a first-class result rather than noise to be averaged away.
- Manual review of the highest-scoring solutions checks whether high scores reflect novelty or shortcut exploitation, auditing the benchmark's own construct validity.

## Strengths

- Deterministic process metrics are reproducible in a way judge-based process scoring is not, and the paper is explicit that they are proxies rather than exhaustive definitions.
- The avg@3 versus best@3 contrast is a genuinely load-bearing result: it reframes much of the model ranking as reliability rather than capability.
- The counterfactual erasure design isolates experience reuse rather than inferring it from correlations across runs.
- The novelty audit (1.2% genuinely novel, 6.3% shortcut-exploiting) is a finding against the benchmark's own headline scores, and it is reported.
- Per-model inference cost is tabulated, so the roughly 20× spread between Opus and LongCat is visible next to the performance spread.
- Harness effects are measured separately, showing that harness choice moves avg@3 more than best@3 — consistent with the reliability framing.

## Limitations

- No release location is stated for the framework or task set, so neither the metrics nor the tasks are currently reusable (recorded above as `TODO(reference)`).
- C1–C3 are explicitly proxies grounded in verifier scores and execution signals; they cannot capture unrealized ideas or latent reasoning, and C3's recovery term is weakly determined when a trajectory contains few regressions.
- The experience-reuse estimates depend on the chosen erasure point, the selected source–target pairs, and how transferred experience is represented, and do not cover all accumulation mechanisms that would arise in longer deployments.
- Conclusions are tied to the AutoLab task distribution, budgets, verifiers and execution environment under a shared Claude Code harness; the authors state absolute scores and some relative rankings may change elsewhere.
- Cost figures depend on provider pricing and token accounting at evaluation time and are not stable quantities.
- Repository note: the task set is AutoLab's, not this paper's. The contribution carded here is the measurement framework layered on top of it.

## Related Works

- [AutoResearchEval](./autoresearcheval.md) — The same "go beyond final scores" argument for end-to-end research, using a calibrated agent-as-a-judge over trajectories where this work uses deterministic rules.
- [MLE-bench](./mle-bench.md) — Machine-learning engineering under budget, scored on final leaderboard position without process decomposition.
- [AutoWorldModel-Bench](./autoworldmodel-bench.md) — Also has agents improve a provided artifact under a fixed compute budget, in world modeling, and also audits whether wins are substantive or hyperparameter tweaks.
- [CostBench](./costbench.md) — Budget-aware agent evaluation, where cost is part of the score rather than reported alongside it.
- [R³-Bench](./r3-bench.md) — Also separates demonstrated competence from realized performance under resource pressure, using shared budgets across a problem suite.
