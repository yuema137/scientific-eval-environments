# PaperBench (2025)

> **English** | [简体中文](../zh/works/paperbench.md)

> **First appeared:** 2025-04-02 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2504.01848)

## Overview

PaperBench evaluates whether AI agents can replicate state-of-the-art AI research: agents must replicate 20 ICML 2024 Spotlight and Oral papers from scratch — understanding the contributions, developing a codebase, and executing experiments — graded against author-co-developed hierarchical rubrics totaling 8,316 individually gradable tasks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.01848>
- **Code:** <https://github.com/openai/preparedness>
- **Venue:** arXiv preprint (cs.AI, cs.CL), 2025

## Summary

PaperBench makes replication objectively gradable by decomposing each paper into a hierarchical rubric of sub-tasks with clear grading criteria, co-developed with the paper's own authors. An LLM-based judge grades replication attempts against the rubrics at scale, and the judge itself is assessed on a separate judge benchmark. The best-performing tested agent, Claude 3.5 Sonnet (New) with open-source scaffolding, reaches an average replication score of 21.0%, and recruited top ML PhDs still outperform the models on the attempted subset.

## Tasks

Replication of 20 ICML 2024 Spotlight and Oral papers from scratch, decomposed into 8,316 individually gradable rubric tasks spanning comprehension, codebase development, and experiment execution.

## Domains

AI research (machine learning): replication of ICML 2024 papers.

## Evaluation

- **Rubric plus reproduction, then a judge.** Each paper carries an author-co-developed hierarchical rubric; when a run ends, the submission is copied to a fresh Ubuntu 24.04 VM with an A10 GPU and its `reproduce.sh` is executed from a clean start, so results hard-coded during the run can be told apart from results the code actually produces. SimpleJudge then grades every rubric leaf node independently, prompted with the paper, the rubric JSON, the node's requirement, and the ten submission files it ranks most relevant.
- **The judge has its own benchmark.** JudgeEval takes partial replications of four PaperBench papers plus one from the development set, built either from scratch or by modifying the original authors' codebases, with the researchers grading every leaf node by hand; those labels are the ground truth for the binary decision the judge makes at each node. Macro-averaged across papers, SimpleJudge reaches F1 0.59 with GPT-4o-mini ($8 per paper), 0.73 with GPT-4o ($120), 0.78 with o1-mini ($72), 0.84 with o1 ($830) and 0.83 with o3-mini ($66), against 0.49 for random labeling. o3-mini is the judge used for the main results, chosen on cost rather than peak F1.
- **Reported.** Best tested agent, Claude 3.5 Sonnet (New) with open-source scaffolding, scores 21.0% on average. On a 3-paper subset the ML-PhD baseline reaches 41.4% after 48 hours of tracked effort, against 26.6% for o1 on the same subset; in a 36-hour extended run o1 leads the humans early and is passed after 24 hours.

## Typical Duration

Agents get a maximum run-time of 12 hours in an Ubuntu 24.04 Docker container with a single NVIDIA A10 GPU; one extended run of o1 with IterativeAgent goes to 36 hours, with hourly snapshots graded at 1, 3, 6, 12, and 36 hours. The separate reproduction step caps `reproduce.sh` at 12 hours, which was enough for every script to finish — agent-produced scripts ran 5.5 minutes on average. The eight human-baseline participants worked part-time with active hours tracked on a timesheet, and their scores are read off snapshots at matched hour counts.

## Main Contribution

Hierarchical, author-co-developed rubrics that turn "did the agent replicate the paper" into thousands of objectively gradable sub-judgments — with the grading judge itself benchmarked.

## Key Design Ideas

- Rubric co-development with the original authors fixes what counts as replication.
- Hierarchical decomposition yields partial credit at fine grain instead of a single replication bit.
- A separate judge benchmark makes the automated grader's reliability a measured quantity.

## Strengths

- 8,316 gradable nodes give unusually fine resolution on where replication fails.
- A concurrent expert-human baseline anchors the model scores.

## Limitations

- Repository note: Every score is judge-assigned. SimpleJudge with o3-mini reaches F1 0.83 on JudgeEval rather than exact agreement, and JudgeEval itself is built from partial replications of five papers, so grading error is measured on a small labeled sample rather than removed.
- Repository note: The suite is 20 ICML 2024 papers in machine learning; the human anchor was collected on 4 of them with 3 attempts each, and the headline expert comparison is reported on a 3-paper subset, so it rests on a small slice of the benchmark.

## Related Works

- [ReplicationBench](./replicationbench.md) — Also author-co-developed paper replication, for astrophysics rather than AI research.
- [PRBench](./prbench.md) — Also rubric-scored paper reproduction, in physics.
- [CORE-Bench](./core-bench.md) — Also targets reproducibility, from provided code and data rather than from scratch.
