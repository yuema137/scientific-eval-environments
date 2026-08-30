# MobileJudgeBench (2026)

> **English** | [简体中文](../zh/works/mobilejudgebench.md)

> **First appeared:** 2026-08-11 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.11434)

## Overview

MobileJudgeBench evaluates automatic judges for mobile-agent trajectories against 931 human-labeled trajectories spanning six benchmarks, four agent models, 289 tasks, and 68 apps.

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — evaluator-validation benchmark over general mobile-agent trajectories.

## Links

- **Paper:** <https://arxiv.org/abs/2608.11434>
- **Venue:** arXiv preprint (2026)

## Summary

The benchmark compares six judge methods across five LLM backends, using human success labels as ground truth. It reports trajectory-level classification metrics and tests whether those metrics predict two downstream uses: reproducing human agent rankings and serving as reward signals for on-policy training. A simple sampled-screenshot baseline is competitive with purpose-built pipelines; the best configuration reaches 90.9% accuracy, and balanced accuracy correlates with agent-ranking fidelity at Spearman ρ = 0.87.

## Tasks

931 trajectories from SPA-Bench, AndroidWorld, AndroidLab, AndroidArena, A3, and B-MoCA, covering 289 tasks and 68 apps. Each trajectory contains screenshots and actions from one of four mobile-agent models.

## Domains

Mobile GUI agents and app interaction; no canonical scientific or engineering domain.

## Evaluation

Accuracy, balanced accuracy, precision, recall, and F1 against adjudicated human success labels, plus agent-level ranking correlation and success-rate estimation error. Each trajectory is independently labeled by two to four of nine annotators; pairwise agreement is 88.4%. Meta-correlation and downstream RL experiments test whether benchmark metrics predict practical judge utility.

## Typical Duration

Offline judging of recorded trajectories; no environment execution budget is defined for the judge.

## Main Contribution

A judge benchmark that validates not only human agreement but whether judge-quality metrics predict reliable agent comparison and useful training rewards.

## Key Design Ideas

- Cross six benchmarks, multiple agents, and 68 apps rather than validating on one environment.
- Compare judge method and backbone as separate sources of variance.
- Connect offline judge metrics to ranking fidelity and on-policy training outcomes.
- Analyze conservative and permissive failure profiles through precision and recall.

## Strengths

- Human labels provide an external reference for every trajectory.
- Downstream validation tests whether judge metrics matter beyond the benchmark itself.
- The simple baseline exposes when pipeline complexity adds no reliability.

## Limitations

- The corpus is limited to mobile GUI agents.
- Success is binary, so partial completion and process quality are not directly represented.
- On-policy validation covers one training setting and does not establish universal reward-model behavior.

## Related Works

- [AgentRewardBench](./agentrewardbench.md) — validates web-agent trajectory evaluators against expert labels.
- [Plan-RewardBench](./plan-rewardbench.md) — tests evaluator preference accuracy on paired tool-use trajectories.
- [SkillTV-Bench](./skilltv-bench.md) — validates judges in skill-augmented trajectory settings.
