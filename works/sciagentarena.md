# SciAgentArena (2026)

## Overview

SciAgentArena is a systematic benchmark for evaluating AI agents in real-world scientific research scenarios across scales. It provides roughly 200 tasks with stepwise verification in an interactive, agent-agnostic environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.12736>
- **Project:** <https://sciagentarena.github.io/>

## Summary

Titled *Benchmarking AI Agents for Addressing Scientific Challenges Across Scales*, SciAgentArena addresses the fact that AI agents' practical capabilities in real research settings remain poorly understood. It provides an interactive, agent-agnostic environment with roughly 200 tasks constructed from real-world scientific research scenarios across multiple domains, using stepwise verification. It reports that agents perform well on structured data-analysis workflows but struggle with novel insights, self-directed exploration, and open-ended questions, and it catalogs common failure modes.

## Tasks

Approximately 200 tasks with stepwise verification (the paper gives no exact integer), constructed from real biomedical research scenarios across five fields — single-cell omics, spatial omics, computational drug discovery, electronic health records (EHR) modeling, and genetics — plus a small cross-domain set (eQTL, target identification, synthetic lethality). Tasks fall into four categories: Data Analysis, Optimization, Discovery, and Validity.

## Domains

Biomedical research across five fields (single-cell omics, spatial omics, computational drug discovery, EHR modeling, genetics). "Across scales" refers to the biological hierarchy — molecular → cellular → tissue → human body → genome/population — not physical scale.

## Evaluation

- **Heterogeneous, per-domain stepwise verification — execution- and expert-criteria-based, not LLM-judge.** There is no single global 0–1 scale; scoring is native to each domain: expert-designed binary (0/1) criteria per subtask (genetics PRS/MR, reported as pass counts such as "all 14 subtasks"), action-level F1 via bidirectional substring matching against a ground-truth action list (EHR tasks T1–T4), and task-native metrics elsewhere (AUROC, Jaccard, correlation). Single-cell omics is scored both step-by-step and pipeline-based.
- **Both step-level and final-outcome scoring**, with execution-based code checks against ground-truth / oracle outputs; drug-discovery scores are averaged over three independent runs with per-task standard error.
- **Reported (18 agents, incl. GPT-5.2, Gemini 3 Pro, Claude Sonnet 4.6, and specialist agents Biomni / STELLA / ToolUniverse):** e.g., hERG prediction 68.1 AUROC, differential-expression detection 29.4 F1, spatially-variable-gene detection 47.6 Jaccard, EHR FHIR-query top F1 ≈ 0.91 (STELLA). Agents are strong on structured data analysis (reading/joining tables, computing descriptors, running standard pipelines) but weak on optimization (only ~1–25% solve multi-objective molecular design; none budget their oracle calls), discovery (many fail to produce runnable code on out-of-distribution tasks), and validity (agents tend to assume infeasible tasks are feasible rather than rejecting them). Hardest: EHR drug management (all agents F1 < 0.32).

## Typical Duration

Not stated: no per-task wall-clock, step, or token budget is given. The one budget-like constraint is domain-specific — drug-discovery optimization caps molecular oracle calls at 100.

## Main Contribution

A systematic, agent-agnostic benchmark for measuring AI-agent progress on real scientific-research scenarios across scales, with stepwise verification and an explicit account of where agents currently succeed and fail.

## Key Design Ideas

- Real-world scientific research scenarios spanning multiple scales.
- Stepwise verification rather than only terminal outcome scoring.
- Agent-agnostic, interactive environment supporting diverse agents.
- Explicit failure-mode analysis (novel insight, self-directed exploration, open-ended questions).

## Strengths

- Stepwise verification gives finer-grained signal than terminal success alone.
- Agent-agnostic design supports comparison across diverse agent implementations.
- Reports concrete strengths/weaknesses rather than a single score.

## Limitations

- Repository note: The paper states "approximately 200 tasks" but never gives an exact total or a per-domain task table — only workflow-internal subtask counts. Because scoring scales differ by domain (binary criteria, F1, and native metrics), there is no single uniform metric for cross-domain aggregation.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also assesses agents on data-driven scientific tasks, but grades a unified Python-program output rather than stepwise verification across scales.
- [AIRS-Bench](./airs-bench.md) — Also targets research-science tasks, evaluating an end-to-end research lifecycle.
