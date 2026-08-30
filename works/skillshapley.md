# SkillShapley (2026)

> **English** | [简体中文](../zh/works/skillshapley.md)

> **First appeared:** 2026-08-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.13173)

## Overview

SkillShapley is a step-level attribution framework for agent skills: it models the contribution of each step inside a skill as a Shapley value and estimates those values under a boundary-adaptive sampling scheme designed for discretized benchmark rewards.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — attribution methodology; no scientific or research activity is itself the evaluated object.

## Links

- **Paper:** <https://arxiv.org/abs/2608.13173>
- **Venue:** arXiv preprint, 2026

## Summary

Agent skills are procedural instructions that let a language agent carry out long tasks such as document processing or coding, and they are written either by hand or distilled from execution traces — in both cases with little evidence about which of their steps actually matter. SkillShapley formulates skill-step attribution as Shapley-value contribution estimation over coalitions of steps, then estimates those values in two phases motivated by two empirical observations: benchmark rewards are discretized and therefore produce sharp performance cliffs, and interactions between steps are largely additive rather than synergistic. A warmup phase builds a cache with broad stratum coverage and identifies which strata remain uncertain; an adaptive phase then repeatedly evaluates the single most informative unevaluated configuration, scored by how many high-priority one-flip edges it forms with configurations already cached.

## Tasks

N/A — attribution method, not a task suite. Skills are drawn from SkillsBench, which formalizes agent skills as structured procedural knowledge and supplies curated skills with deterministic verifiers across diverse tasks. Three skills are analyzed in the experiments: `offer-letter-generator`, `manufacturing-fjsp-optimization`, and `dialogue-parser`.

## Domains

No canonical science or engineering domain. The evaluated skills cover document generation, flexible job-shop scheduling optimization, and dialogue graph parsing — general-purpose agent procedures rather than tasks in a science or engineering field, and the object of evaluation is the attribution estimator rather than the skills' subject matter.

## Evaluation

- **Mean absolute error against exact Shapley values**, measuring how closely the estimator recovers the ground-truth attribution under a fixed evaluation budget.
- **Removal validation curves**, testing whether removing steps in the order the estimator ranks them degrades skill performance as predicted.
- Baselines: individual scores, Leave-One-Out, random removal, LeastCore, Monte Carlo Shapley, quasi-Monte Carlo Shapley, paired Monte Carlo Shapley, and size-*k*-truncated Shapley.
- **Reported.** Under a budget of 99 unique configurations, the boundary-adaptive first phase yields 206 reusable one-flip marginal edges, whereas Monte Carlo permutation sampling yields 130 permutation marginal observations of which only 115 are unique. Further headline magnitudes are TODO(reference).

## Typical Duration

N/A — post-hoc valuation over completed skill executions; cost is reported as a budget of unique skill configurations evaluated rather than as wall-clock or token spend.

## Main Contribution

Brings Shapley-value credit assignment down to the individual *step* of an agent skill, and adapts the sampling strategy to the structure that agentic benchmarks actually exhibit — cliff-shaped discrete rewards and near-additive step interactions — rather than assuming a smooth, strongly interacting value function.

## Key Design Ideas

- Skill-step attribution is posed as coalitional value estimation over subsets of steps, so a step's worth is defined by its marginal effect across many contexts rather than by a single ablation.
- The two empirical premises — discretized rewards producing sharp cliffs, and largely additive step interactions — are used to justify concentrating the sampling budget near informative boundaries instead of sampling permutations uniformly.
- Sampling reuses evaluated configurations: each new configuration is chosen for the number of high-priority one-flip edges it forms with the cache, so a single expensive rollout contributes several marginal observations.
- Validation is two-sided: agreement with exact Shapley values where they can be computed, and a behavioral removal test where they cannot.

## Strengths

- Attribution is at step granularity, finer than skill-level or unit-level valuation, and directly actionable for skill authoring and pruning.
- Sample efficiency is measured against exact Shapley values, so the estimator's approximation quality is a reported quantity rather than an assumption.
- The comparison set includes both classical data-valuation estimators and Shapley variance-reduction methods, not only naive leave-one-out.

## Limitations

- The experiments cover three skills; the paper does not establish that the additive-interaction premise holds across skill families more broadly.
- The additivity and cliff assumptions are motivating empirical observations rather than guarantees, so the adaptive sampler's advantage may not transfer to benchmarks with dense or strongly synergistic rewards.
- No code release is stated in the paper.
- Repository note: card compiled from the arXiv v1 full text (August 2026); no peer-reviewed version was located at the time of writing.
- Repository note: attribution is measured against the verifier of the host benchmark, so a step judged low-value is low-value *for that verifier* and not necessarily for the underlying task.

## Related Works

- [SkillSV](./skillsv.md) — The closest sibling: also Shapley valuation of a skill's internals, but over compiled units, dependencies, and hierarchy rather than over individual steps.
- [Skill-Use](./skill-use.md) — Also treats skills as first-class evaluation objects, scoring the agent's use of a skill rather than the worth of the skill's parts.
- [QVal](./qval.md) — Also makes a step-level credit signal the object of evaluation rather than the agent.
- [BACKROOMBench](./backroombench.md) — Also establishes skill influence by counterfactual intervention, at the level of the whole skill rather than its steps.
- [GATE](./gate.md) — Also analyzes structured skill/tool artifacts, through graph-based tool evolution rather than credit valuation.
