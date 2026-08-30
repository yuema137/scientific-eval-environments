# Curation-Bench (2026)

> **English** | [简体中文](../zh/works/curation-bench.md)

> **First appeared:** 2026-06-02 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.04261)

## Overview

Curation-Bench evaluates whether generalist coding agents can improve training-data curation policies through an iterative train–evaluate–revise loop with the model, training recipe, and evaluation suite held fixed.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.04261>
- **Venue:** arXiv preprint (2026)

## Summary

Agents inspect a candidate dataset, implement selection policies through a CLI, submit them to a fixed vision-language instruction-tuning pipeline, observe evaluation results, and revise for up to ten iterations. Out-of-the-box agents recover strong published selection baselines but mostly tune local variants; a scaffold requiring each iteration to cite and adapt a prior method broadens exploration and produces a policy that exceeds strong baselines using one tenth of their data budget.

## Tasks

Open-ended data-policy research for vision-language instruction tuning. Each run modifies executable curation code and repeatedly invokes the same training and downstream evaluation pipeline; the evaluated artifact is the selected data subset and policy that produced it.

## Domains

AI and machine-learning research, specifically multimodal instruction-tuning data selection.

## Evaluation

Downstream benchmark performance of the model trained on the selected data, under a fixed base model, recipe, and suite. Results are tracked across ten iterations and compared with published data-selection baselines, data budgets, and scaffold conditions; trajectory analysis classifies local tuning versus exploration of new method families.

## Typical Duration

Up to ten train–evaluate–revise iterations per run; the paper reports data-budget comparisons rather than one universal wall-clock limit.

## Main Contribution

An agent-centric benchmark that makes downstream evaluation feedback the control signal for autonomous data-curation research.

## Key Design Ideas

- Fix model, recipe, and evaluator so only the curation policy changes.
- Expose the loop through a CLI suitable for generalist coding agents.
- Compare open-ended prompting with a method-citation and adaptation scaffold.
- Evaluate both final downstream quality and the research behavior visible in trajectories.

## Strengths

- The controlled pipeline attributes gains to data policy rather than model or recipe changes.
- Multiple iterations make evaluation an active feedback signal rather than a terminal report.
- Data-budget comparisons expose efficiency as well as quality.

## Limitations

- The current instantiation covers one vision-language instruction-tuning setting.
- Expensive training loops constrain the number of repetitions and explored policies.
- Strong results under the method-guided scaffold do not establish open-ended autonomous research ability.

## Related Works

- [PostTrainBench](./posttrainbench.md) — gives agents broader freedom over data and training under a fixed evaluator and compute budget.
- [SkillCoach](./skillcoach.md) — uses process evaluation to select trajectories for supervised fine-tuning.
- [MLE-bench](./mle-bench.md) — evaluates end-to-end ML engineering through competition outcomes rather than controlled curation research.
