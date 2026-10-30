# Agent4Sci (2026)

> **English** | [简体中文](../zh/works/agent4sci.md)

> **First appeared:** 2026-10-20 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.28763)

## Overview

ML-engineering benchmarks usually ask an agent to reach a good score on a competition task, so the bar is a leaderboard, not the published state of the art of a scientific field. Agent4Sci starts each run from a verified reproduction of the best published model on a scientific ML benchmark and asks the agent to improve it within 12 hours on 8 H200 GPUs. A separate evaluation agent scores the submitted model on a sequestered test set, and an auditing agent checks the trajectory for gaming. The score is the relative improvement over the published best.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** [Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?](https://arxiv.org/abs/2610.28763), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.28763v1>
- **Code:** <https://github.com/maszhongming/agent4sci>
- **Data:** <https://huggingface.co/datasets/MingZhong/agent4sci>
- **Venue:** NeurIPS 2026 Evaluations & Datasets Track (per the arXiv comment)

## Summary

A benchmark is admitted only if its standardized reproduction matches the paper's headline number within a verified tolerance. The agent receives that reproduction with the training and, where available, validation data, but cannot read or evaluate on the test set; hill-climbing and evaluation run in separate containers with deterministic splits. After 12 hours, an evaluation agent runs the submitted artifact on the held-out test set, and the score is Δ% = (s − b)/|b| × 100 for higher-is-better metrics (sign reversed for lower-is-better), where b is the reproduced baseline. An auditing agent (Claude Opus 4.6 by default) reviews each trajectory for selective reporting, test-set contamination, metric manipulation, and hardcoding; half of each agent's runs are re-audited by three other model families, with human spot checks. The paper reports that most gains come from engineering techniques rather than research-level insight, and there is no human-researcher baseline.

## Tasks

20 benchmarks with 25 tasks across 11 domains, e.g. transient classification (ATAT), σ8 regression (CosmoBench), molecule retrieval from mass spectra (MassSpecGym), DMS substitution prediction (ProteinGym), full-topology power flow (PFDelta), and dead-tree segmentation (TreeFinder). Benchmarks pass a four-stage filter: a scientific-domain target, automated screening against seven criteria (data, training, baselines, evaluation, licensing), human re-verification, and review of reproducibility, task specificity, repository usability, and domain coverage. On the NeurIPS 2025 Datasets & Benchmarks track this admitted 10 of 497 candidates; the rest come from other ML venues and domain journals.

## Domains

Astronomy (ATAT, Mars-Bench), cosmology (CosmoBench), biology (SR-CACO-2 confocal super-resolution), genomics (DART-Eval), bioengineering (ESCAPE, gRNAde, MOTIVE, ProteinGym, UniSite), chemistry (CheMixHub, MassSpecGym), ecology (CarbonGlobe, TreeFinder), geography (GEO-Bench-2, GTPBD), geology (LITHOS), neuroscience (NeuroGraph), and physics (PFDelta, TIDMAD dark-matter signal denoising), using the paper's domain labels.

## Evaluation

- **Metric:** signed relative improvement over the reproduced published best, measured on the sequestered test set by a separate evaluation agent.
- **Default agents (mean Δ%):** Claude Opus 4.6 10.4%, Claude Sonnet 4.6 9.6%, Gemini 3.1 Pro 6.8%, Codex (GPT-5.4) 4.4%. The best default-agent result is positive on every benchmark, from 1.1% (ProteinGym) to 64.4% (PFDelta); the paper reports that no run was flagged for misconduct.
- **Trajectory analysis:** three recurring limitations, namely novelty miscalibration (well-known techniques presented as new ideas), resource under-utilization (idle GPUs, serialized experiments), and collapse into hyperparameter sweeps and ensembling after an early win. Hyperparameter tuning is 56% of Opus's interventions, 44% of Codex's, and 48% of Gemini's.
- **Plug-in skills:** three markdown skills for research ideation, experiment management, and hourly self-assessment checklists raise Opus from 10.4% to 20.1% (improving 18 of 20 benchmarks) and Codex from 4.4% to 8.1% (12 of 20). Individual skills are not ablated in the main text.
- The paper presents averages as a per-benchmark probe rather than a leaderboard, noting run-to-run variation. TODO(reference): number of runs per agent.

## Typical Duration

12 hours of wall-clock time per run on 8 H200 GPUs; Opus averages 490 turns and 338 tool calls per run. An appendix reports 3-day runs on two benchmarks. TODO(reference): token and API cost per run.

## Main Contribution

A long-horizon testbed that measures how far agents can improve on published state-of-the-art scientific ML models under fixed compute, with held-out evaluation by a separate agent and audited misconduct checks, plus a trajectory analysis and plug-in skills that target the failure patterns it finds.

## Key Design Ideas

- The baseline is the reproduced published best, so any positive score exceeds the field's reported result on that benchmark.
- Hill-climbing and test evaluation run in separate containers, and only a separate agent touches the test set.
- Misconduct auditing is cross-checked across model families and by human spot checks.
- The skills intervention is designed against the three failure patterns found in trajectories.

## Strengths

- Every task starts from a reproduction verified against the original paper's number.
- The paper quantifies agent behavior (turns, tool calls, intervention mix) alongside scores.
- The skills experiment applies the same benchmarks and budgets with and without the intervention.

## Limitations

- The authors list no human-researcher baseline, single-agent harness coverage, imperfect held-out verification, limited scope of hill-climbing, and possible overfitting of the plug-in skills, which were optimized for Claude Code.
- Each domain has only one to five benchmarks, so per-domain conclusions rest on few tasks.
- Misconduct detection relies on LLM auditors, checked by spot checks rather than full human review.
- Repository note: relative improvement is not comparable across metrics with different baseline magnitudes; the paper reports it per benchmark and as a mean.

## Related Works

- [MLE-bench](./mle-bench.md) — Also scores agents on ML engineering tasks, against Kaggle leaderboards rather than published scientific baselines.
- [AIRS-Bench](./airs-bench.md) — Also a 20-task suite of research-science ML problems, but with no baseline code supplied.
- [Harness-Bench](./harness-bench.md) — Also compares agent performance across harness configurations.
