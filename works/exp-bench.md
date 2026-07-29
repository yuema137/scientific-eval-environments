# EXP-Bench (2025)

> **English** | [简体中文](../zh/works/exp-bench.md)

## Overview

EXP-Bench is a benchmark that evaluates AI agents on conducting complete research experiments from influential AI publications: formulating hypotheses, designing and implementing experimental procedures, executing them, and analyzing results. It curates 461 tasks from 51 NeurIPS 2024 and ICLR 2024 papers through a semi-autonomous extraction pipeline.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.24785>
- **Code:** <https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench>

## Summary

EXP-Bench addresses the limitation that current AI agents struggle with the complexities of rigorous, end-to-end experimentation, despite the promise of automating AI research. Given a research question and incomplete starter code, agents must formulate hypotheses, design and implement experimental procedures, execute them, and analyze results; a semi-autonomous pipeline extracts and structures these tasks from research papers and their associated open-source code. Leading agents such as OpenHands and IterativeAgent score 20–35% on individual aspects like design or implementation correctness, but only 0.5% on complete, executable experiments.

## Tasks

461 tasks from 51 top-tier AI research papers — NeurIPS 2024 (53%) and ICLR 2024 (47%) — each giving the agent a research question, a high-level method description, and incomplete starter code from the paper's repository. Tasks were curated by a three-stage pipeline (impact-based filtering, multi-pass extraction from paper and codebase, validation with lightweight human review) and decompose into 12,737 individually gradable subtasks spanning design, implementation, and conclusion.

## Domains

Diverse AI research subfields, including Computer Vision, NLP, and Reinforcement Learning.

## Evaluation

- **Design correctness (D).** An LLM-based judge scores the proportion of ground-truth design criteria met by the agent's experimental design.
- **Implementation correctness (I) and execution (E).** An LLM-based judge compares the agent's code modifications against the ground-truth git diff; a code execution validator re-runs them in a clean containerized environment, and the conjunctive I·E requires both.
- **Conclusion correctness (C).** An LLM-based judge checks the agent's final conclusion for conceptual soundness, completeness, and alignment with the ground-truth answer to the research question.
- **All✓ and All·E✓.** All✓ counts tasks fully correct on D, I, and C; All·E✓ adds the executability requirement; a monitor first screens agent logs for disallowed behaviors such as accessing the source paper, Git operations, or fabricated data.
- **Reported (Table 1).** The best complete-and-executable rate, All·E✓, is 0.5%, achieved by OpenHands with o3-mini (All✓ 1.4%); OpenHands with Claude-3.7 Sonnet reaches 35.0% on implementation correctness and 33.2% on execution, yet 0.4% on All·E✓.

## Typical Duration

Capped at 40 minutes of wall-clock time per agent per task (a limit the authors note can be adjusted), inside an Ubuntu 24.04 Docker container with four Nvidia A40 GPUs. No per-task step or token budget is stated.

## Main Contribution

A benchmark of 461 authentic end-to-end AI research experiment tasks, extracted from influential papers and their open-source code by a semi-autonomous pipeline, for locating the bottlenecks that keep AI agents from conducting complete research experiments.

## Key Design Ideas

- Semi-autonomous curation pipeline that extracts and structures experimental details from papers and their associated open-source code, with impact-based filtering and lightweight human validation.
- Each task pairs a research question and a high-level method description with incomplete starter code; ground-truth design, code diff, and conclusion are derived from the source paper's own scripts.
- Fine-grained decomposition of every task into individually gradable subtasks (12,737 in total) across design, implementation, and conclusion, separating per-aspect scores from end-to-end success.
- Containerized execution with a monitor integrity check that screens agent logs for disallowed behaviors before grading.

## Strengths

- Tasks are grounded in authentic published experiments, with executable ground truth derived from the papers' own code.
- Per-aspect grading separates design, implementation, execution, and conclusion failures, exposing where agents break down.
- Large gap between per-aspect scores (20–35%) and complete executable success (0.5%) signals substantial headroom.

## Limitations

- Repository note: Design, implementation, and conclusion grading all rely on LLM-based judges against extracted ground truth; only the execution check is programmatic, so aggregate scores inherit judge reliability.
- Repository note: Every task reproduces a published AI experiment from two 2024 venues — open-ended experimentation and non-AI scientific domains are outside the evaluated setting.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also extracts tasks from peer-reviewed publications with execution-based grading, but each task targets a single standalone data-analysis program rather than a full design → implement → execute → conclude experiment.
- [AIRS-Bench](./airs-bench.md) — Also sources end-to-end AI research tasks from machine-learning papers, but provides no baseline code and scores agents on the measured performance of the models they build rather than on fidelity to the source experiment's design and conclusions.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also a scientific agent benchmark run in containerized environments, but its tasks are domain-expert-authored under a Propose → Build → Review protocol rather than extracted from published papers.