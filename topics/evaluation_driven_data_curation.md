# Evaluation-Driven Data Curation

> **English** | [简体中文](../zh/topics/evaluation_driven_data_curation.md) · [← All topics](./README.md)

## Start Here

Most training papers choose data first and report evaluation at the end. In that workflow, the score describes the finished model but does not decide what data should come next.

Here the score closes the loop. A curation policy selects 10,000 examples, the fixed recipe trains a model, held-out evaluation exposes weak behavior, and the next policy changes the mixture or filters. Evaluation is therefore a control signal for data selection. A paper that merely tries several datasets and reports the best result is not automatically in this topic; the feedback must actually change the curation process.

## Definition

Evaluation-driven data curation uses downstream results to choose the next training data. The system may select, generate, filter, weight, reorder, or remix examples, but the defining step is the return path: evaluation changes the next data decision.

## Motivation

Nearly every training paper reports a final score. That alone does not close a loop. Here, a data policy builds a training set, a fixed recipe produces a model, held-out evaluation exposes a weakness, and the policy changes what it selects next. Requiring that feedback path keeps ordinary dataset comparisons and general data-centric ML outside the topic.

## Existing Approaches

- **Closed-loop policy research.** [Curation-Bench](../works/curation-bench.md) fixes the model, training recipe, and evaluation suite while agents iteratively modify executable selection policies.
- **Process-score filtering.** [SkillCoach](../works/skillcoach.md) uses validated skill-use rubrics to select supervised fine-tuning trajectories, outperforming outcome-only filtering in its reported study.
- **Broader post-training search.** [PostTrainBench](../works/posttrainbench.md) allows agents to change data as one part of an evaluator-driven post-training strategy, while auditing contamination.

## Comparison

| Work | Data intervention | Evaluation signal | Iteration | Controls |
|---|---|---|---|---|
| Curation-Bench | Executable selection policy and selected subset | Downstream VLM benchmark suite | Up to 10 rounds | Fixed model and recipe |
| SkillCoach | Filter agent trajectories for SFT | Validated process rubric + task verifier | Offline selection and retraining | Same task families and base model |
| PostTrainBench | Data sourcing, generation, filtering, formatting | Target benchmark score | Open-ended within 10 hours | Fixed base model, evaluator, GPU budget |

## Open Questions

- How can a loop distinguish genuine generalization from repeated-evaluator overfitting?
- What evaluation budget is needed to compare noisy data policies reliably?
- How should process quality, downstream accuracy, diversity, cost, and safety trade off?
- Can learned curation policies transfer across models, modalities, and domains?
- What audit trail is sufficient to detect direct and indirect contamination?

## Related Works

- [Curation-Bench](../works/curation-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [PostTrainBench](../works/posttrainbench.md)
