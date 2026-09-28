# AgentActionBench (2026)

> **English** | [简体中文](../zh/works/agentactionbench.md)

> **First appeared:** 2026-04-19 · **Source:** [official task-material release commit](https://github.com/KOU-199024/NLPCC-2026-Shared-Task-11/commit/4dabe5fdd22a28a24d72dc31d77ba3c2e11c0892)

## Overview

AgentActionBench evaluates paper reproduction using recorded actions as evidence. An MCP Action Recorder captures reading, writing, and command execution so that a plausible final repository cannot by itself stand in for an executed experiment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** [Overview of the NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction from Scientific Papers](https://arxiv.org/abs/2609.11117), September 10, 2026 preprint describing the shared task.
- **Full text:** <https://arxiv.org/html/2609.11117v1>
- **Official task, data and recorder:** <https://github.com/KOU-199024/NLPCC-2026-Shared-Task-11>

## Summary

The paper documents 150 reproduction tasks: 120 ML papers and 30 AI4Science papers. A 15-paper human-annotated subset supports development and rubric validation; the remaining papers determine the main leaderboard. The April repository release already contains task instructions, papers, rubrics, and recorder code; the September paper reports the expanded benchmark and results.

## Tasks

Given a paper in PDF or Markdown, the agent builds and runs a reproduction repository through Read, Write, and Execute tools. It submits the repository and chronological action log. The evaluator checks five stages: paper observation, plan writing, code implementation, command execution, and result matching.

## Domains

AI and machine-learning research (120 papers), plus astronomy, biology, chemistry, environmental science, materials science, and medicine (30 AI4Science papers in total). Individual counts for the six scientific fields are not reported. All tasks aim to reproduce specific published experiments.

## Evaluation

For each rubric item, ChatGPT-4o-mini reads the paper and relevant tool logs, assigns pass or fail, and contributes the item's importance weight to the reproduction score. Execution logs supply evidence, but the final rubric decision remains model-based. The benchmark contains more than 10,000 items. On the human subset, scores from generated versus human-authored rubrics correlate at Pearson 0.93 and Spearman 0.88. This compares rubric sources, not independent human judgments of every agent action. Stage-level scores expose substantially weaker command execution and result matching than planning and implementation.

## Typical Duration

The paper reports two NVIDIA L40S GPUs for the experiments, but no standard per-task wall-clock budget.

## Main Contribution

A process-based reproduction benchmark with an instrumented execution environment and paper-specific scoring criteria.

## Key Design Ideas

- Match rubric stages to the tool logs that can support them.
- Use a reviewed human subset to assess automatically generated rubrics.
- Keep development rubrics separate from the main leaderboard tasks.

## Strengths

- Exposes the difference between writing code and executing it successfully.
- Includes scientific applications beyond conventional ML papers.

## Limitations

- Repository note: correlation between rubric sources does not establish the accuracy of each automated pass/fail judgment.
- The human rubric subset is small, and no measured human reproduction baseline is reported.
- Hidden test rubrics do not make the already published papers themselves unseen to models.

## Related Works

- [PaperBench](./paperbench.md)
- [Beyond Final Scores](./beyond-final-scores.md)
