# AstaBench (2025)

> **English** | [简体中文](../zh/works/astabench.md)

## Overview

AstaBench is a benchmark suite that provides a holistic measure of agentic ability to perform scientific research, pairing its tasks with a reproducible tool environment and cost-controlled scoring. It comprises 2,400+ problems across 11 benchmarks in four task categories — literature understanding, code & execution, data analysis, and end-to-end discovery — with many problems inspired by actual user requests to deployed Asta agents.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.21652>
- **Project:** <https://allenai.org/asta/leaderboard>
- **Code:** <https://github.com/allenai/asta-bench>
- **Venue:** ICLR 2026

## Summary

AstaBench argues that existing agent benchmark suites lack reproducible tools for controlled comparison, fail to account for confounders such as model cost and tool access, rarely standardize task interfaces for general agents, lack tasks informed by authentic product usage, and offer few comprehensive baselines. The authors formalize benchmarking principles and instantiate them as a suite of 2,400+ problems in 11 benchmarks, backed by the Asta Environment — the first scientific research environment with production-grade, date-restricted search tools — together with the `agent-eval` cost-accounting toolkit and the `agent-baselines` suite of standardized agents. Evaluating 57 agents across 22 agent classes, the paper finds that despite meaningful progress on individual aspects, AI remains far from solving the challenge of science research assistance.

## Tasks

2,400+ problems across 11 benchmarks: literature understanding (PaperFindingBench, LitQA2-FullText-Search, ScholarQA-CS2, LitQA2-FullText, ArxivDIGESTables-Clean), code & execution (SUPER-Expert, CORE-Bench-Hard⁻, DS-1000), data analysis (DiscoveryBench), and end-to-end discovery (E2E-Bench, E2E-Bench-Hard), each with test and validation splits. Of the 11 benchmarks, 7 were created by the authors (4 previously unreleased) and the rest adapt prior datasets in slightly modified form; many problems derive from real usage of deployed Asta systems — PaperFindingBench from PaperFinder and OpenSciLM usage logs, ScholarQA-CS2 from 100 user questions issued to OpenSciLM — while the two end-to-end benchmarks pair machine-generated research tasks with human expert review. Literature benchmarks carry per-benchmark corpus date cutoffs so that retrieval is limited to papers predating benchmark creation.

## Domains

Multiple scientific domains weighted towards computer science: benchmark-level domains are CS, biology, or mixed, with DiscoveryBench alone spanning sociology, biology, humanities, economics, engineering, and meta-science, and CORE-Bench-Hard⁻ spanning computer science, social science, and medicine.

## Evaluation

- **Literature-understanding metrics.** PaperFindingBench scores navigational and metadata queries with F1 over the result set and semantic queries with the harmonic mean of estimated recall and nDCG; LitQA2-FullText reports accuracy and LitQA2-FullText-Search recall@30; ScholarQA-CS2 averages four LLM-judged facets (citation recall, citation precision, answer relevance, answer coverage); ArxivDIGESTables-Clean unrolls generated tables into atomic statements and reports LLM-judged entailment recall against reference tables.
- **Code, data-analysis, and discovery metrics.** SUPER-Expert computes exact match against expert-annotated gold solutions, DS-1000 the accuracy of proposed code passing target test cases, DiscoveryBench a Hypothesis Matching Score (the product of three LLM-as-judge alignment scores over context, variables, and relationship), and E2E-Bench / E2E-Bench-Hard rubric-based LLM-as-judge assessment of each agent's report, code, and artifacts.
- **Time-invariant cost accounting.** The `agent-eval` toolkit computes normalized dollar cost per problem from model usages logged through Inspect, priced against a frozen snapshot of the `litellm` cost map with cache discounts factored in, so costs remain comparable as API prices change.
- **Confounder-aware reporting.** Suite and category scores are macro averages over benchmark statistics (the two LitQA2 benchmarks weight 0.5 each) with 95% confidence intervals; every leaderboard entry is categorized by agent openness and agent tooling, and score-vs-cost Pareto frontiers identify cost-optimal agents.
- **Reported (Table 4).** Asta v0 leads with an overall score of 53.0% at $3.40 per problem vs. 44.0% for ReAct with gpt-5; ReAct with gpt-5-mini scores 31.6% at $0.04 per problem; the best open-weight configuration, Smolagents Coder with Llama-4-Scout-17B-16E-Instruct, reaches 11.1%.

## Typical Duration

No suite-wide per-task step, token, or wall-clock budget is stated; the ReAct baseline caps agents at a maximum of 100 steps per task (in practice most models average under 12 steps), and notebook code cells return a timeout message after 5 minutes by default. Resource use is tracked as normalized dollar cost per problem instead, from $0.04 for the most economical strong baseline to $3.40 macro-averaged for the top-scoring Asta v0.

## Main Contribution

A benchmark suite and accompanying agent environment that measure holistic scientific-research ability under standardized tools, confounder-aware scoring, and time-invariant cost accounting, with comprehensive baseline agents and a public leaderboard.

## Key Design Ideas

- Standard, reproducible tooling: Asta Scientific Corpus literature-search tools served over MCP with per-benchmark corpus date cutoffs, plus a sandboxed stateful Jupyter notebook for code execution.
- Time-invariant cost accounting that converts Inspect-logged model usage into normalized dollar cost per problem via a frozen `litellm` cost-map snapshot.
- Confounder-aware leaderboard design: submissions categorized by agent openness and agent tooling, with Pareto frontiers plotting score against cost.
- A standardized task interface plus the `agent-baselines` suite — 16 agent classes including 9 science-optimized Asta agents — so general agents can be evaluated without per-benchmark adaptation.

## Strengths

- Controlled, date-restricted search tools let score differences reflect agentic capability rather than privileged tool or corpus access.
- Cost-aware, confounder-categorized reporting surfaces trade-offs: ReAct with gpt-5-mini lands within 21% (absolute) of the best-performing models while costing over an order of magnitude less.
- Coverage of the full research pipeline, including the agent-neutral E2E-Bench, exposes compounding failure modes that single-stage benchmarks do not measure.

## Limitations

- Repository note: Holistic coverage is weighted towards computer science — the paper's own comparison table characterizes it as "Broad (weighted towards CS)", and both end-to-end discovery benchmarks pose AI/NLP research tasks only.
- Repository note: 6 of the 11 benchmarks rely on LLM-as-judge scoring; the authors report validation (system-level Kendall τ = 0.467 against expert rankings on ScholarQA-CS2, rising to 0.800 excluding Elicit; spot-checked end-to-end rubric scores) and name refining LLM-judge grading for discovery tasks as ongoing work.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also evaluates agents on data-driven scientific tasks, but scores standalone generated programs for individual analysis subtasks rather than spanning literature, code, data analysis, and end-to-end discovery under one cost-accounted suite.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also a multi-domain scientific agent benchmark, but built from domain-expert-authored terminal tasks in containers rather than a standardized research-tool environment with cost-controlled leaderboard scoring.
- [Aviary](./aviary.md) — Also provides scientific task environments for agents, but packages them as language-grounded POMDPs with terminal rewards oriented to training rather than a benchmark suite with confounder-aware scoring.
