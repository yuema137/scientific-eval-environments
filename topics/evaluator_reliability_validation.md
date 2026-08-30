# Evaluator Reliability & Validation

> **English** | [简体中文](../zh/topics/evaluator_reliability_validation.md) · [← All topics](./README.md)

## Start Here

An evaluator is another measurement system, not an oracle. If an LLM judge gives a trajectory 8/10, the important next question is whether that score agrees with experts, ranks better runs above worse ones, and stays stable when wording or candidate order changes.

Take 100 expert-labeled trajectories, score them with the judge, then separate false passes from false failures and test a swapped presentation order. This evaluates the evaluator before using it to rank agents or supply rewards. High agreement on this set still does not guarantee reliability after the agent changes its behavior to exploit the judge.

## Definition

An evaluator turns an agent run into a score, ranking, or reward. It may be a deterministic verifier, an expert rubric, a reward model, an LLM judge, or a combination of them. This topic tests whether that mechanism gives the right verdict, expresses uncertainty honestly, survives irrelevant changes, and remains suitable for the decision that consumes its output.

## Motivation

A score inherits the evaluator's mistakes. A judge can agree with experts on easy examples yet reverse a ranking when answer order changes, reward verbosity, or fail on trajectories unlike its validation set. Before its scores guide a leaderboard or training loop, the evaluator needs its own expert ground truth, calibration checks, and adversarial failure tests.

## Existing Approaches

- **Expert-labeled trajectory benchmarks.** [AgentRewardBench](../works/agentrewardbench.md) and [MobileJudgeBench](../works/mobilejudgebench.md) compare automatic trajectory judges with expert outcomes across web and mobile agents.
- **Pairwise preference validation.** [Plan-RewardBench](../works/plan-rewardbench.md) controls candidate order and asks evaluators to distinguish preferred tool-use trajectories from confusable negatives.
- **Skill-aware judging.** [SkillTV-Bench](../works/skilltv-bench.md) tests whether judges can verify trajectories whose correctness depends on task-specific skill knowledge.
- **Hybrid verification.** [AgentLens](../works/agentlens.md) combines formal checks with multiple judge dimensions and evidence-linked reviews.
- **Domain calibration.** [AstroVisBench](../works/astrovisbench.md), [PSE-Bench](../works/pse-bench.md), and [FIRE-Bench](../works/fire-bench.md) report human agreement for judges used on scientific outputs.

## Comparison

| Work | Evaluator under test | Ground truth | Reliability signal | Downstream validation |
|---|---|---|---|---|
| AgentRewardBench | LLM and rule-based web-agent evaluators | Expert trajectory labels | Precision, recall, agreement across benchmarks | Agent evaluation |
| MobileJudgeBench | Six mobile-agent judge methods × five backends | 931 human-labeled trajectories | Classification metrics, ranking correlation, rate error | Agent ranking and on-policy reward |
| Plan-RewardBench | Reward models and LLM judges | Validated pairwise preferences | Order-swapped pairwise accuracy | No |
| SkillTV-Bench | LLM-as-a-Judge and Agent-as-a-Judge | Skill-aware trajectory labels | Judge accuracy and best-of-N selection | Trajectory selection |
| AgentLens | Hybrid judge plus formal verifier | Executable checks and review evidence | Multi-dimensional quality index | Coding-agent diagnosis |
| AstroVisBench | Multimodal visualization judges | Professional astronomer annotations | Rank correlation and inter-annotator agreement | Judge selection |

## Open Questions

- Which judge metrics predict ranking fidelity, reward usefulness, and deployment decisions?
- How should evaluator uncertainty propagate into benchmark leaderboards and statistical comparisons?
- How can verifier coverage and false-negative surfaces be measured when no complete oracle exists?
- When do pairwise, pointwise, rubric, and deterministic evaluators fail differently?
- How should benchmarks defend evaluators against reward hacking, style bias, contamination, and adaptive optimization?

## Related Works

- [AgentRewardBench](../works/agentrewardbench.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [AgentLens](../works/agentlens.md)
- [AstroVisBench](../works/astrovisbench.md)
- [PSE-Bench](../works/pse-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
