# SCI-AGENT-EXAM (2026)

> **English** | [简体中文](../zh/works/sci-agent-exam.md)

> **First appeared:** 2026-10-23 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.32441)

## Overview

SCI-AGENT-EXAM scores the code a scientific agent runs and the report it writes as separate channels on the same task. Many benchmarks check only a final answer, or only an executable result. Here every one of 120 tasks requires a structured answer, executable artifacts, and a written report. Deterministic checkers rerun the code on hidden inputs, and an LLM judge applies an expert-written rubric to the report. Reporting both channels shows when an agent writes a convincing report about analysis that did not execute correctly, and the reverse.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** [SCI-AGENT-EXAM: Benchmarking Agents on Scientific Research Tasks](https://arxiv.org/abs/2610.32441), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.32441v1>
- **Code and data (as given in the paper):** <https://github.com/SKYLENAGE-AI/Sci-Agent-Exam>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

Each task is a versioned package: instruction, frozen offline Docker environment, visible files, a hidden reference solution, weighted programmatic checks, and a human-written rubric. The agent works in the container through a common Claude Code harness. Afterwards, the checker imports its code or reads its artifacts and reruns the computation on hidden data; the judge grades the report against the rubric. The task score mixes the two with fixed weights per task type, from 0.70 programmatic for Code Generation to 0.20 for Literature Synthesis. Both component scores are reported beside the final score. The authors also rescore workspace snapshots along each trajectory to see when quality is reached and whether it is later lost.

## Tasks

120 tasks across seven task types of the paper's Scientific Workflow Task Taxonomy (SWTT): Literature Synthesis 10, Hypothesis Validation 16, Tool Orchestration 28, Code Generation 20, End-to-End Analysis 25, Error Diagnosis 11, Result Interpretation 10. Sources are recent research papers, scientific competitions and datasets, and actively maintained open-source projects; only redistributable licenses are used. A PhD-level expert designs each task, builds the package and a reference solution, and writes the rubric after the solution. The reference report must score at least 90% on its own rubric. Many tasks contain a trap, such as a precomputed dashboard from a leaky procedure or a salient statistic that fails a downstream physical gate, so that only the full procedure earns credit. 156 domain experts took part. Each task passed an independent reviewer and an auditor, with an 85% reviewer–auditor agreement threshold. Example: in `bioinformatics-end-to-end-analysis-02`, the agent must select a metagenomic assembly-and-binning pipeline that is robust across four stress axes, using one mounted paper and 14 data files. It is scored by 20 rubric criteria (weight 70) and eight programmatic checks (weight 30), including a held-out replay with every identifier relabeled.

## Domains

11 fields (task counts from Table 2): biology 15, scientific computation 13, physical science 12, bioinformatics 11, chemistry 11, physics simulation 11, computer science 10, data science 10, materials science 10, mathematics 9, engineering 8. The paper does not say which science "physical science" or "engineering" tasks cover.

## Evaluation

- **Programmatic score:** a weighted mean of checker functions in [0, 1], testing execution status, numerical values within declared tolerances, output schemas, required files, invariance under allowed perturbations, and task-specific constraints. A missing artifact scores zero on every dependent check.
- **LLM-judge score:** a weighted mean of pass/fail rubric criteria covering scientific correctness, execution and validation, source grounding, communication, and completeness. GPT-5.6 Sol is the judge. It sees the source excerpts and rubric but not the reference score; criteria that depend on a missing file fail in preflight. Tasks average about 8 programmatic checks and 20 rubric criteria.
- **Protocol:** ten models, all in Claude Code at high effort, three runs per task. Scores are averaged over runs, then macro-averaged over tasks. Pass@0.95 is the fraction of runs scoring at least 0.95.
- **Results (Table 3, final score / Pass@0.95):** GPT-6 Astra 80.9 / 26.0%; Claude Fable 5 67.3 / 9.7%; Claude Opus 5 64.2 / 10.5%; Qwen3.8 Max 62.7; Kimi K3 62.6; GPT-5.6 Sol 59.6; Claude Opus 4.8 57.1; GLM-5.3 55.9; Grok-4.6 52.4; DeepSeek-V4-Pro 50.9 / 1.9%.
- **Execution versus report:** the share of task outcomes with judge ≥ 0.5 but programmatic < 0.5 ranges from 0.14 (GPT-6 Astra) to 0.48 (DeepSeek-V4-Pro). In case studies, a DeepSeek-V4-Pro run scores 1.00 programmatically but 0.43 from the judge, and a Claude Opus 5 run scores 1.00 from the judge but 0.11 programmatically.
- **Trajectories:** snapshots after each file read or write are rescored to measure early completion, dip (a passing criterion later fails), recover, and regret (it fails at the end). GPT-5.6 Sol's mean dip rate across the five rubric dimensions is 27.0%, against 18.3% for GPT-6 Astra.
- **Sensitivity (50-task subset):** under Codex instead of Claude Code, Kimi K3 and GLM-5.3 lose 15.9 and 20.1 points and GPT-5.6 Sol gains 14.3. Moving from high to max effort raises the nine-model mean from 61.8 to 65.1.
- Repository note: the abstract calls the judge "calibrated, expert-validated". The calibration the paper describes is the requirement that each reference report score at least 90% on its own rubric. No agreement statistic between the judge and human graders is reported.

## Typical Duration

On the paper's "peer subset", mean cost per run ranges from $5.13 (Claude Opus 4.8) to $57.96 (GLM-5.3), runtime from 22.0 to 56.6 minutes, and turns from 30.2 to 102.4 (GLM-5.3). GPT-6 Astra averages $20.79 and 22.1 minutes. Task writers spent about six hours per task.

## Main Contribution

Requires an answer, executable artifacts, and a report for every task across seven workflow task types, and keeps execution correctness and report quality as separately reported scores, so that one cannot hide a failure in the other.

## Key Design Ideas

- Fixed per-type weights decide how much a task rests on execution or on reporting, before any model is evaluated.
- Hidden-input reruns, identifier relabeling, and input mutation defeat hard-coded answers and shortcut solutions.
- Rubrics are written by the task authors after the reference solution, not generated by an LLM.

## Strengths

- Component scores are always shown next to the final score, which makes report-without-execution failures countable.
- Snapshot rescoring adds when quality is reached and whether it is kept, beyond the final state.
- The harness and effort sensitivity runs show how much a single-harness ranking depends on configuration.

## Limitations

- The authors note that the study covers general-purpose models under a standardized agent setting, not specialized agents with domain tools or memory.
- Per-field counts are small (8 to 15 tasks), and four field labels (physical science, data science, scientific computation, engineering) do not name a specific science.
- The main ranking uses one harness; the authors show that some models move by 14 to 20 points under another.
- Repository note: the GitHub URL given in the paper returned HTTP 404 when checked on 2026-10-27, so the release could not be confirmed.
- Repository note: the paper says source-specific contamination controls are detailed in an appendix, but that appendix documents provenance, licensing, and trap design rather than a post-cutoff or leakage-screening rule.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also scores generated programs by execution on data-driven scientific tasks, but without a required written report.
- [Terminal-Bench Science](./terminal-bench-science.md) — Containerized scientific tasks checked by task-specific tests.
- [ASI-Bench](./asi-bench.md) — Project-level scientific tasks across 11 domains; compared in the paper's Table 1.
