# AI4AI-Bench (2026)

> **English** | [简体中文](../zh/works/ai4ai-bench.md)

> **First appeared:** 2026-08-20 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.20318)

## Overview

AI4AI-Bench tests whether a coding agent can improve how an AI system learns, rather than only tune the run around an unchanged method. Across ten frozen research repositories, the agent returns a source-code patch; a separate clean execution then trains or constructs the model and scores it with a fixed evaluator the agent could not query during development.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.20318>
- **Project:** <https://lab.einsia.ai/ai4ai/>
- **Code:** <https://github.com/Einsia/AI4AI-Bench>
- **Venue:** arXiv preprint (2026)

## Summary

Each task supplies a real research codebase, its starting model or assets, and a cheap proxy metric. The agent gets four hours on one B300 to diagnose the training dynamics, edit the repository, and test candidate ideas, but only its source patch crosses into the sealed stage; the patched code is rerun from a clean start for up to twelve hours and scored against the repository's original method under identical conditions. The evaluation therefore separates a reproducible algorithm change from lucky checkpoints or state carried over from exploration, while a second analysis classifies whether the patch changed how the run was operated or how the model learned.

## Tasks

Ten repositories cover ten algorithm families: OpenR1 supervised fine-tuning, RAGEN multi-turn agentic RL, OPD on-policy distillation, BTRM Bradley–Terry reward modeling, DPO preference optimization, DDPO diffusion RL, NPO machine unlearning, DiGress discrete graph diffusion, Model Soup weight averaging, and OWL one-shot pruning. Eight tasks train a model from initialization; weight averaging and pruning execute once under the same verification ceiling.

## Domains

AI and machine-learning research, spanning language-model post-training, reinforcement learning, reward modeling, diffusion models, unlearning, graph generation, model merging, and pruning.

## Evaluation

Each task keeps its native deterministic metric, including LiveCodeBench, held-out solve rate, AIME 2024/2025, RewardBench, IFEval, aesthetic score, unlearning balanced score, graph test negative log-likelihood, ImageNet-V2 accuracy, and WikiText-2 perplexity. A monotone progress mapping places them on a shared scale: `0` is an uninformative model, `0.1` is the original repository method rerun under the same budget, and `1.0` is the task optimum. The study evaluates 29 model–harness–effort configurations across all ten tasks (290 cells); the mean mapped score is 0.166, the best system average is 0.250, and 124 cells fall below the original-method baseline.

For diagnosis, a separate language model reads 263 classifiable code diffs and assigns non-exclusive change families. Of these submissions, 141 change only run-side choices such as duration, hyperparameters, checkpoint selection, or trainable capacity; 122 touch the loss, supervision, update rule, or data. The latter group averages 0.226 against 0.126 for run-side-only changes. Varying reasoning effort raises the share reaching the learning side from 8% to 64%, but the authors state that the comparison is not randomized and therefore does not identify a causal effect of making an algorithmic change.

## Typical Duration

Four hours of agent exploration on one NVIDIA B300 per task, followed by up to twelve hours of clean-start formal execution; the two non-training tasks use twelve hours only as a verification ceiling.

## Main Contribution

A benchmark that isolates algorithmic design inside AI research automation by holding hardware, starting assets, execution budget, and final evaluation fixed, then checking both whether the submitted patch improves the model and which layer of the learning procedure it changes.

## Key Design Ideas

- Make source code the only artifact transferred from exploration into formal evaluation.
- Rerun the original and modified algorithms from the same starting point under the same hardware, budget, evaluator, and evaluation asset.
- Keep a cheap proxy available during development while withholding the metric that determines the final score.
- Normalize heterogeneous task metrics around an uninformative point, the shipped algorithm, and the task optimum.
- Read submitted diffs to distinguish operational tuning from changes to the learning procedure.

## Strengths

- Covers ten distinct algorithm families instead of repeating one post-training recipe.
- The clean-start replay makes a score attributable to the submitted source rather than exploration checkpoints or cached state.
- Reports both outcome and intervention type, exposing why a superficially successful AI-research run may not demonstrate algorithm design.
- Releases task environments, evaluators, and scored submissions for replay and later longitudinal comparison.
- Reports exploration cost and controlled reasoning-effort sweeps alongside performance.

## Limitations

- The suite contains ten expensive tasks on one hardware class, so coverage is broad by algorithm family but small by instance count.
- There is no human-expert baseline; the original repository algorithm anchors the scale but does not locate human research performance.
- The source-patch change families are assigned by a language model, and the paper does not report human validation of those labels.
- The proxy/final boundary prevents direct final-metric querying, but the paper notes that some proxies draw from the same corpus as final evaluation; it guarantees separation of access and timing, not sample disjointness.
- The public repository supports self-hosted evaluation but currently states that it does not provide a blind evaluation service, so third-party runs do not automatically reproduce the paper's evaluator-access boundary.

## Related Works

- [PostTrainBench](./posttrainbench.md) — opens post-training end to end, including data and initialization choices, while AI4AI-Bench isolates training-algorithm design.
- [RE-Bench](./re-bench.md) — evaluates open-ended AI R&D under time budgets with human comparison, but does not isolate the learning-rule layer.
- [Curation-Bench](./curation-bench.md) — fixes the training recipe and makes data-policy improvement the intervention instead.
- [AutoWorldModel-Bench](./autoworldmodel-bench.md) — asks agents to improve world models with an open method space and a held-out evaluator.
- [Beyond Final Scores](./beyond-final-scores.md) — separates long-horizon improvement outcomes from the processes and shortcuts that produced them.
