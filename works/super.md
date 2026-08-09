# SUPER (2024)

> **English** | [简体中文](../zh/works/super.md)

## Overview

SUPER evaluates agents on setting up and executing tasks from research repositories: 45 end-to-end problems with expert solutions, 152 sub-problems targeting specific challenges, and 602 automatically generated problems from real ML/NLP GitHub repos — where the best model (GPT-4o) solves only 16.3% end to end.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2409.07440>
- **Code:** <https://github.com/allenai/super-benchmark>
- **Venue:** EMNLP 2024

## Summary

Reproducing research means getting someone else's repository to actually run, and SUPER (from AI2) benchmarks exactly that: agents must set up and execute tasks from real ML/NLP research repositories in the GitHub wild — resolving dependencies, fixing errors, and running code to reproduce results. It comprises 45 end-to-end problems with expert solutions, 152 sub-problems isolating specific setup challenges, and 602 automatically generated problems. GPT-4o, the best model, solves only 16.3% of the end-to-end set (46.1% of scenarios), showing how brittle real-world reproduction remains for agents.

## Tasks

Setting up and executing tasks from real research repositories: 45 end-to-end problems, 152 sub-problems, and 602 auto-generated problems; the agent configures environments, resolves errors, and runs code. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — research reproduction: setting up and executing ML/NLP research repositories.

## Evaluation

- End-to-end solve rate plus scenario/sub-problem (landmark) success.
- **Reported.** GPT-4o solves 16.3% of the end-to-end set and 46.1% of scenarios.

## Typical Duration

Long-horizon repo-setup-and-execution episodes per task.

## Main Contribution

Isolating the setup-and-execute bottleneck of research reproduction — the unglamorous but decisive step of making real research code run — as a graded agent benchmark.

## Key Design Ideas

- Real "in-the-wild" GitHub repos capture the messiness reproduction actually faces.
- The end-to-end / sub-problem / auto-generated split gives graded difficulty and scale.
- Expert solutions anchor the 45 end-to-end problems.

## Strengths

- Targets the reproduction step that determines whether research is usable, with a public AI2 release.
- The 16.3% end-to-end ceiling is a clear reproducibility-frontier marker.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the EMNLP 2024 venue is not stated in arXiv Comments (the paper was presented at EMNLP 2024).

## Related Works

- [ML-Bench](./ml-bench.md) — Also repository-level ML tasks, spanning code generation and agentic execution.
- [ResearchCodeBench](./researchcodebench.md) — Also research-code evaluation, on implementing paper contributions.
- [MLR-Bench](./mlr-bench.md) — Also ML-research automation, across the full research pipeline.
