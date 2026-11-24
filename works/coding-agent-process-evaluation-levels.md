# What Process Evaluation of Coding Agents Actually Measures (2026)

> **English** | [简体中文](../zh/works/coding-agent-process-evaluation-levels.md)

> **First appeared:** 2026-08-24 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.22960)

## Overview

Process evaluation of coding agents usually asks one judge, often an LLM reading the whole trace, to say which step mattered. This paper argues that such a judgment mixes three questions: what the agent is likely to do next (action level), whether the run as a whole is still uncertain or recoverable (task level), and whether a particular step causally changed the outcome (step level). It gives each level its own estimator, introduces SCAE, a replay-based estimator for the step-level causal quantity, and uses these estimators on coding-agent traces to test what existing process signals actually track.

## Topics


- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities


N/A — Process-evaluation methodology for coding-agent trajectories on general software file localization (SWE-bench Verified); no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.22960>

## Summary

The authors model agent execution as a structural causal model in which each action is drawn from the policy with exogenous Gumbel decoding noise, the environment returns an observation, and the final file set is scored against the gold set. Under assumptions of context observability, exogenous decoding noise, and a replayable environment, the value of a prefix can be estimated by replaying the agent from that prefix several times and averaging the outcome; a step's contribution is the difference between the values of consecutive prefixes. When the agent's next action is nearly deterministic, replays cannot vary it, so SCAE substitutes an alternative action, executes it for real, and replays the rest. Applied to file-localization traces, the estimators show that next actions follow execution provenance, that uncertainty is concentrated at the task level, and that full-trace judges shift blame toward later steps when they can see downstream outcomes.

## Tasks

499 file-localization episodes derived from SWE-bench Verified, spanning 12 repositories (django is the largest). Each episode contains an issue, a repository snapshot, an agent trajectory, and a gold set of files to locate. Trajectories were produced by Codex CLI backed by gpt-5.5-0424-global in a read-only sandbox. Action-level analysis uses 7,616 decision points from 488 episodes; step-attribution analysis uses 190 prefixes across 38 instances.

## Domains

Software engineering: locating the files relevant to a GitHub issue in open-source Python repositories.

## Evaluation

- **Outcome.** The SCM uses containment of the gold file set; the main experiments use recall over the gold files, which the authors report moves under intervention for 98.6% of instances against 73.2% for binary success.
- **Step contribution (SCAE).** Replay m = 8 continuations from prefix τ<sub>1:t</sub> and average the outcome to get v̂<sub>t</sub>; the step effect is Δ̂<sub>t</sub> = v̂<sub>t</sub> − v̂<sub>t−1</sub>, and step effects sum to Y − E[Y | q, G]. An entropy probe over (tool, target object) buckets with 4 to 6 replays decides whether to use observational replay or the substituted-action intervention. Tool outputs are never fabricated.
- **Trace.** For one episode, if replays from the prefix ending before step t recover 40% of gold files on average and replays from the prefix ending after step t recover 55%, step t is credited with +0.15. The paper reports that none of its 190 intervention-estimated effects survive BH-FDR correction at q = 0.10, so no individual step is certified.
- **Action level.** Next-action prediction with top-k accuracy, NLL, calibration, and effective candidate count. A provenance predictor (the last tool output) reaches top-3 accuracy 0.326 on first-visit decisions, against 0.058 for a strengthened code-graph predictor.
- **Task level.** Instance identity explains ICC = 0.640 of residual replay variance, against a permutation null of 0.196; action-model entropy does not track replay variance (ρ = −0.088).
- **Judge audit.** With judge model and rubric fixed, hiding versus showing downstream steps moves the judge's verdict later in 59 of 70 episodes. The full-trace judge selects gold-touching steps 0.900 of the time against a 0.413 baseline. Judges tested: gpt-5.5, qwen3.6-plus, and qwen3-coder-plus.

## Typical Duration

The 1,901 replayed continuations used for attribution took 12.7 hours. Per-episode agent step counts are not stated in the text read for this card. TODO(reference)

## Main Contribution

A measurement framework that separates action-level prediction, task-level uncertainty, and step-level causal attribution in coding-agent process evaluation, with SCAE as a replay-based estimator of prefix-conditioned step effects. The authors conclude that current process evaluation often measures semantic relevance rather than certified causal contribution.

## Key Design Ideas

- Define the step-level target as a prefix-conditioned causal quantity, so step credit has a definition independent of any judge.
- Estimate prefix values by replaying the real agent in a replayable environment instead of asking a model to predict outcomes.
- Switch to real action substitution only when decoding entropy is too low for replays to vary the action.
- Audit judges by changing only their information set (with or without downstream steps), which isolates collider bias from judge quality.

## Strengths

- Each claim is paired with a null or baseline (permutation nulls, chance agreement, code-graph predictors) and confidence intervals.
- Preconditions are checked before use: environment replayability was 1.00 over 100 actions with 3 re-executions each, and no rollout triggered context compaction.
- The judge audit is replicated across three judge models, including a code-specialized one.

## Limitations

- Only file localization is studied, which limits external validity to other coding-agent behaviors.
- Step-level attribution is underpowered at feasible replay budgets: none of 190 intervention estimates survive FDR correction, so no episode's critical step is certified.
- Values are estimated at selected prefixes, so step contributions are segment-level approximations.
- Exogenous decoding noise and transferability of substituted actions cannot be fully verified from traces; the substituted-action branch estimates effects under a perturbed policy.
- The three-way uncertainty decomposition is validated only on a synthetic process, and only 46.2% of agent objects resolve to dependency-graph nodes.
- Repository note: No code or data link appears on the arXiv page or in the paper text read for this card.

## Related Works

- [SWE-bench](./swe-bench.md) — Source of the issues from which the file-localization episodes are derived.
- [AgentProcessBench](./agentprocessbench.md) — Scores steps with human effectiveness labels; this work asks whether such step judgments reflect causal contribution.
- [Who&When Pro](./who-and-when-pro.md) — Also targets which step is responsible for an outcome, using failure labels fixed by construction rather than replay estimates.
- [Long-Horizon Agent Trajectory Attribution](./long-horizon-agent-trajectory-attribution.md) — Also attributes outcomes to parts of an agent trajectory, but over trajectory components rather than replay-estimated step effects.
