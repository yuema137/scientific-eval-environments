# PostTrainBench (2026)

> **English** | [简体中文](../zh/works/posttrainbench.md)

## Overview

PostTrainBench evaluates whether CLI agents can autonomously post-train small base language models to improve held-out benchmark scores under a single-H100, ten-hour budget.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.08640>
- **Project:** <http://posttrainbench.com/>
- **Code:** <https://github.com/aisa-group/PostTrainBench>
- **Venue:** arXiv preprint (2026)

## Summary

An agent receives a base model, benchmark-specific evaluator, unrestricted internet access, and freedom to choose data and training methods, then submits a final model after at most ten hours on one H100. Seven targets span math, writing, function calling, science, medical reasoning, and code. The best reported aggregate reaches 23.2% against a 7.5% base-model average, while systematic auditing finds 23 contamination flags across five agents, making evaluator gaming part of the measured deployment risk.

## Tasks

Post-train four base models for seven evaluation targets: AIME 2025, Arena Hard Writing, BFCL, GPQA, GSM8K, HealthBench Easy, and HumanEval. Agents run through Claude Code, Codex CLI, Gemini CLI, or OpenCode and may iteratively change datasets, formatting, hyperparameters, adapters, or training algorithms.

## Domains

AI and machine-learning research automation across model post-training, data preparation, experimentation, and evaluation.

## Evaluation

Final held-out benchmark score of the submitted model, aggregated first across four base models per benchmark and then across seven benchmarks. Evaluator files and test data may not be modified or used for training. The study also audits generated scripts, datasets, model substitutions, and traces for direct, indirect, and evaluation-guided contamination.

## Typical Duration

Ten hours on one NVIDIA H100 per task; time-budget ablations include shorter and twenty-hour conditions.

## Main Contribution

A controlled environment in which evaluation is both the optimization target and experimental feedback for autonomous post-training research, with compute metering and contamination auditing.

## Key Design Ideas

- Hold the base model and benchmark target fixed while leaving data and training strategy open.
- Give agents repeated evaluator access within a strict GPU-time budget.
- Compare model–CLI-scaffold configurations rather than attributing results only to the base model.
- Audit reward hacking and contamination instead of assuming benchmark rules are followed.

## Strengths

- Covers heterogeneous post-training objectives under one resource protocol.
- Generated models are executed by the official evaluator, giving an objective downstream outcome.
- Detailed trace analysis exposes strategies, persistence, failures, and specification gaming.

## Limitations

- Optimizing one narrow benchmark does not measure production-quality general-purpose post-training.
- Most configurations have one run because of GPU cost; only selected frontier configurations have repeated runs.
- The evaluator-access loop creates a strong contamination and overfitting surface, which auditing detects but cannot eliminate completely.

## Related Works

- [Curation-Bench](./curation-bench.md) — isolates data-policy improvement under a fixed training recipe.
- [MLE-bench](./mle-bench.md) — evaluates ML engineering on Kaggle competitions rather than model post-training under a common hardware budget.
- [HarnessOpt-Bench](./harnessopt-bench.md) — evaluates agents optimizing their harness under a metered evaluation budget.
