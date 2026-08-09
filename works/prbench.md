# PRBench (2026)

> **English** | [简体中文](../zh/works/prbench.md)

## Overview

PRBench is a benchmark that tests whether AI agents can reproduce published physics research end to end — comprehending a paper's methodology, implementing its algorithms from scratch, and producing quantitative results that match the original publication. It comprises 30 expert-curated tasks spanning 11 subfields of physics, each run in a sandboxed execution environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Research Reproduction & Replication](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.27646>
- **Project:** <https://prbench.phybench.cn/>

## Summary

PRBench addresses the open question of whether AI agents powered by large language models can reliably perform end-to-end reproduction from real scientific papers. The authors assemble 30 expert-curated physics tasks, contributed by domain experts from over 20 research groups at the School of Physics, Peking University, each grounded in a real published paper and validated through end-to-end reproduction with verified ground-truth results and detailed scoring rubrics. The best-performing agent, OpenAI Codex powered by GPT-5.3-Codex, achieves a mean overall score of 34%, and all evaluated agents exhibit a zero end-to-end callback success rate.

## Tasks

30 tasks. Each task gives the agent only the task instruction and the full paper content and requires it to comprehend the methodology of a published physics paper, implement the corresponding algorithms from scratch, and produce quantitative results matching the original publication, with expected outputs in a standardized CSV format. Tasks were contributed by domain experts from more than 20 research groups at the School of Physics, Peking University, through a four-stage pipeline of paper selection, expert reference implementation, structured task specification, and independent verification against the original publication.

## Domains

Physics: 11 subfields, including quantum chromodynamics (QCD), quantum optics, nuclear physics, plasma physics, and condensed matter physics.

## Evaluation

- **Weighted rubric score.** Each task is graded on four dimensions — Methodology Understanding (weight 0.05), Code Implementation Correctness (0.30), Data Reproduction Accuracy (0.60), and Task Completeness (0.05) — combined as a weighted sum into an overall score against the task's expert-written rubric.
- **End-to-end callback rate.** A run counts as successful only if every dimension scores above 0.9; the callback rate is the fraction of tasks on which an agent achieves such end-to-end success.
- **Agentified assessment pipeline.** A white agent solves and executes the task while a green agent orchestrates and grades, comparing generated outputs against ground-truth metadata provided by domain experts in the same sandboxed environment.
- **Reported.** The best-performing agent, OpenAI Codex (GPT-5.3-Codex), reaches a mean overall score of 34%, scoring 43% on Code Implementation Correctness and 21% on Data Reproduction Accuracy; OpenCode-based agents follow at 28.5% with GPT-5.3-Codex, 20.57% with Kimi K2.5 (1T), 18.5% with DeepSeek V3.2 (671B), 17.97% with Minimax 2.7 (230B), and 17.87% with GLM-5 (744B); the end-to-end callback rate is zero for every agent.

## Typical Duration

Per-task sandbox limits are an execution timeout of 800–21,600 seconds and a memory limit of 2–8 GB, task-dependent, and tasks are selected to be executable within a few hours. No step, token, or monetary budget is stated.

## Main Contribution

A rigorous benchmark of 30 expert-curated paper-reproduction tasks for evaluating progress toward autonomous scientific research, grounded in real published physics papers with verified ground-truth results and detailed scoring rubrics.

## Key Design Ideas

- Every task grounded in a real published physics paper, shipping verified ground-truth results and a fine-grained scoring rubric alongside the instruction.
- A closed setting in which agents receive only the task instruction and paper content and must implement every algorithm from scratch in a sandboxed execution environment.
- Outcome-weighted scoring that places weight 0.60 on Data Reproduction Accuracy, against 0.30 for Code Implementation Correctness and 0.05 each for Methodology Understanding and Task Completeness.
- A two-agent assessment design pairing a task-solving white agent with a green agent that orchestrates execution and grades outputs against expert-provided ground truth.

## Strengths

- Expert validation through end-to-end reproduction gives every task verified ground-truth results rather than answers inferred from the source paper.
- The callback criterion — every dimension above 0.9 — measures complete reproduction separately from partial credit, and its current value of zero signals substantial headroom.
- Failure-mode analysis identifies systematic error classes beyond the headline scores, including formula implementation errors, inability to debug numerical simulations, and fabricated output data.

## Limitations

- Repository note: All tasks are contributed by research groups at a single institution — the School of Physics, Peking University — so subfield coverage reflects one community's research portfolio.
- Repository note: Grading is invoked by the green agent of the agentified assessment pipeline, so dimension scores depend on automated rubric judgement against the expert-provided ground-truth metadata.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also extracts tasks from peer-reviewed publications, but scores standalone data-analysis programs rather than end-to-end reproduction of a paper's quantitative results.
- [Aviary](./aviary.md) — Also runs language agents on scientific tasks in execution environments, but builds training gymnasiums whose environments supply terminal rewards rather than a fixed benchmark of expert-validated reproduction tasks.
