# Evaluation-Driven Post-Training

> **English** | [简体中文](../zh/topics/evaluation_driven_post_training.md) · [← All topics](./README.md)

## Start Here

Evaluation is often treated as the last page of a training run: train first, score once, publish the table. This topic studies the opposite arrangement. The evaluator sits inside development and helps choose the next data, reward, fine-tuning method, or model update.

For example, an agent fine-tunes a base model, runs a held-out suite, sees that function calling improved while medical reasoning regressed, and changes the next training mixture. That is an evaluation-driven loop. It also creates a risk: repeated access can turn improvement into benchmark overfitting or reward hacking, so held-out tests and contamination audits remain part of the method.

## Definition

Evaluation-driven post-training puts an evaluator inside the improvement loop. A developer or agent uses its results to choose data, rewards, fine-tuning settings, preference updates, or reinforcement-learning experiments, then evaluates the changed model again.

## Motivation

The useful signal is not just whether the final model is better. It is which measured weakness caused the next intervention and whether that intervention fixed the weakness without breaking something else. Ordinary papers that train once and report benchmark numbers remain outside this topic. Evaluation must influence what the system selects, optimizes, or tries next.

## Existing Approaches

- **Autonomous post-training R&D.** [PostTrainBench](../works/posttrainbench.md) gives CLI agents a base model, evaluator, and fixed GPU-time budget, then scores the submitted model.
- **Data-policy optimization.** [Curation-Bench](../works/curation-bench.md) narrows intervention to data selection under a fixed model and recipe.
- **Evaluation-derived supervision.** [SkillCoach](../works/skillcoach.md) turns a validated process rubric into a trajectory filter for supervised fine-tuning.
- **Judge utility as training reward.** [MobileJudgeBench](../works/mobilejudgebench.md) tests whether offline judge metrics predict downstream on-policy reward usefulness.

## Comparison

| Work | Improved object | Allowed intervention | Evaluation role | Guard against gaming |
|---|---|---|---|---|
| PostTrainBench | Base language model | Data, SFT, adapters, RL, hyperparameters | Repeated feedback and final objective | Rules, held-out evaluator, contamination audit |
| Curation-Bench | Data policy and trained VLM | Selection policy | Per-iteration downstream feedback | Fixed model, recipe, and suite |
| SkillCoach | Agent model via SFT | Trajectory selection | Process-quality filter | Validation-gated rubric evolution |
| MobileJudgeBench | Mobile agent via RL | Reward evaluator choice | Judge as on-policy reward | Human-grounded judge benchmark |

## Open Questions

- When does repeated evaluator access produce learning, benchmark overfitting, or reward hacking?
- How should evaluation calls, compute, data, and wall-clock time be budgeted jointly?
- Which diagnostic signals lead to useful interventions rather than local score chasing?
- How can improvements be tested on held-out tasks without denying agents enough feedback to learn?
- What provenance and auditing are needed when agents autonomously source data and modify training code?

## Related Works

- [PostTrainBench](../works/posttrainbench.md)
- [Curation-Bench](../works/curation-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [MA-RLHF](../works/ma-rlhf.md)
- [CoLA](../works/cola.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
