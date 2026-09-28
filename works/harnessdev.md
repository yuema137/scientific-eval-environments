# HarnessDev (2026)

> **English** | [简体中文](../zh/works/harnessdev.md)

> **First appeared:** 2026-09-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.01437)

## Overview

HarnessDev evaluates whether a model can build reusable agent execution software and improve it from feedback. The submitted artifact is a harness, which is frozen before an executor model uses it on downstream tasks.

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2609.01437>
- **Full text:** <https://arxiv.org/html/2609.01437v1>
- **Project:** <https://self-developing-agents.github.io/>
- **Venue:** arXiv preprint (2026)

## Summary

Creation starts from a runnable seed without a solving policy and 1–3 development cases. Evolution starts from the created harness and exposes designated execution feedback. Separating the creator from the executor allows the same artifact to be tested with its authoring model or a common runtime model.

## Tasks

Six creator models; four task families; 2,207 unique downstream instances: SWE-bench Pro public (731), Terminal-Bench 2.1 (89), MLE-bench (75), EQ-Bench3 (46), and BrowseComp (1,266). Evolution evaluates code harnesses, using 100 SWE-Pro tasks and 89 Terminal-Bench tasks for feedback, with 630 separate SWE-Pro tasks withheld. Feedback instances are not additional benchmark items.

## Domains

Software engineering, machine-learning experimentation, writing, and information search. The scientific slice uses MLE-bench’s model-training competitions and submission grading; the other task families are not scientific research evaluations.

## Evaluation

- Frozen harnesses receive benchmark-native scores: task success, competition medals, writing rubrics, or retrieval accuracy.
- Self-Eval uses the creator as executor; Unified-Eval fixes the executor. Evolution reports feedback-set and hidden-set changes separately.
- Code credit depends on repository diffs or final environment state, not self-reported success. Source and trajectory audits found no prohibited scoring route among reported runs.
- Report total and mean executor tokens; creator development tokens are excluded.
- Created harnesses approach writing references and exceed ML-experimentation references in self-evaluation, but lag in coding and search. Improvements vary across revisions and shrink on unseen tasks or different executors.

## Typical Duration

MLE-bench allows 10 hours per task, including a 30-minute grader reserve; Evolution coding tasks allow two hours. Both use a 500-step cap.

## Main Contribution

Makes construction and continued maintenance of a persistent harness the evaluation target.

## Key Design Ideas

A policy-free seed, separate creator/executor roles, frozen artifacts, and hidden downstream checks distinguish development feedback from generalization.

## Strengths

Records executable artifacts and traces, measures token costs, and tests whether improvements survive changing the executor.

## Limitations

Evolution covers coding only. Reported efficiency excludes development costs. Human-engineered reference scores are partly taken from published reports rather than matched local reruns. Held-out means hidden from the development loop, not necessarily absent from model pretraining.

## Related Works

- [Evo-Bench](./evo-bench.md) — Evaluates improvements to a shared seed harness.
- [EvoHarnessBench](./evoharnessbench.md) — Tests adaptation and retention as available capabilities expand.
- [MLE-bench](./mle-bench.md) — Supplies the machine-learning competition tasks.
