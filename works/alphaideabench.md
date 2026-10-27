# AlphaIdeaBench (2026)

> **English** | [简体中文](../zh/works/alphaideabench.md)

> **First appeared:** 2026-10-24 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.33644)

## Overview

AlphaIdeaBench scores research proposals from automated ideation systems against an explicit resource budget. Each task states the GPUs, API credit, calendar time, and annotation hours available, and an LLM judge checks whether the proposed plan fits them.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment](https://arxiv.org/abs/2610.33644)
- **Full text:** <https://arxiv.org/html/2610.33644v1>
- **Code:** <https://github.com/SHUNCHAOZHOU/AlphaIdeaBench> (judge-only, MIT license)
- **Venue:** arXiv preprint (2026)

## Summary

An ideation harness receives a task and a budget, then returns one JSON proposal with ten required fields, from title to a resource plan. The judge scores twelve dimensions, including budget feasibility. Its novelty scores are compared with scores derived from peer-review comments on 600 papers. Eight harnesses share one backbone, and eight backbones run inside one harness, so harness and model effects are measured separately.

## Tasks

100 tasks in two tracks of 50: workshop calls for papers from NeurIPS, ICML, and ICLR (2023–2025), and open problems stated in 50 surveys. They span nine machine-learning fields, from LLMs and reasoning (22) to graphs and geometry and continual learning (6 each). The main academic budget is four A100 40GB GPUs, 200 GPU hours, $200 of API credit, eight calendar weeks, and 40 annotation hours. Student and lab tiers scale these down and up. The evaluated harnesses are CoI-Agent, SciMON, AI-Researcher, Virtual-Scientists, ResearchAgent, AI-Scientist-V1, AgentLaboratory, and AI-Scientist-V2.

## Domains

Machine-learning research ideation. All 100 tasks come from machine-learning workshops and surveys; 13 are labeled AI for science. The paper notes that results for wet-lab research may differ.

## Evaluation

- Gemini 3.7 Flash scores twelve dimensions from 1 to 5: validity (four), novelty (problem, method, scenario, insight), and feasibility (technical, data, budget, verification). It can look up API and GPU prices when checking budgets.
- Judge check: Gemini 3.7 Flash maps reviewer comments on 600 papers (200 each from ICLR 2026, NeurIPS 2025, and ICML 2025) to 1–5 novelty scores, then the judge scores each paper from its title and abstract. Within-±1 agreement is about 94.5–97.4% for problem novelty and 95.9–96.8% for method novelty by venue. It falls to about 80.6–87.5% for scenario novelty, where the judge is stricter.
- Validity and feasibility have no human reference.
- With Gemini 3.7 Flash, harness overall scores span 4.02 to 4.31; CoI-Agent leads, narrowly ahead of SciMON (4.29). Scenario novelty is at most 1.87 for every harness. Swapping CoI-Agent's backbone moves the overall score from 4.31 (Gemini 3.7 Flash) to 1.84 (Llama 4 Scout).
- GPT-5 mini re-scores the outputs as a ranking check: Spearman ρ = 0.81 for harnesses and 0.83 for backbones.

## Typical Duration

No generation time is reported. On one survey task, single-run ideation used from 9,968 tokens over 2 calls (AI-Scientist-V2) to 279,759 tokens over 50 calls (ResearchAgent). Task budgets describe the proposed research, not the harness run.

## Main Contribution

Makes the resource budget part of each ideation task and scores proposal feasibility against it.

## Key Design Ideas

- A fixed proposal schema lets heterogeneous harnesses be scored on the same fields.
- Budget tiers let the same task be judged under different resource envelopes.
- Novelty is split into four axes, and judge agreement is reported per axis.

## Strengths

- Separates harness effects from backbone effects with two controlled sweeps.
- Reports where judge agreement is weakest rather than a single pooled figure.

## Limitations

- Proposals are not executed; scores are judgments of written plans.
- The reviewer-derived novelty references are mapped from reviewer comments by Gemini 3.7 Flash, the same model as the production judge; validity and feasibility are not checked against humans.
- Repeats per dimension are 1 in the 100-task study.
- The released code is judge-only; the eight harnesses are external systems.

## Related Works

- [IdeaBench](./ideabench.md) — Scores research ideas generated from paper context.
- [AgentIdeaBench](./agentideabench.md) — Compares curated and agent-gathered literature for hypothesis generation.
- [MLR-Bench](./mlr-bench.md) — Evaluates machine-learning research from idea to paper.
