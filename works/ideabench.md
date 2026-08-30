# IdeaBench (2024)

> **English** | [简体中文](../zh/works/ideabench.md)

> **First appeared:** 2024-10-31 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2411.02429)

## Overview

IdeaBench benchmarks LLMs for research idea generation: it profiles LLMs as domain-specific researchers grounded in the same context human researchers use — titles and abstracts of influential papers plus their references — and evaluates generated ideas with a two-stage framework combining GPT-4o ranking and a relative "Insight Score."

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.02429>
- **Venue:** arXiv preprint (cs.CL), 2024

## Summary

IdeaBench treats research ideation as an evaluable task: it grounds an LLM as a domain-specific researcher in the context a human would have — titles and abstracts of influential papers and their referenced works — and asks it to generate new research ideas. Evaluation is two-stage: GPT-4o first ranks ideas on user-specified quality indicators such as novelty and feasibility, then a relative-ranking "Insight Score" quantifies quality. IdeaBench provides both the dataset and this evaluation framework as a reproducible way to compare ideation across models.

## Tasks

Research idea generation grounded in influential-paper titles/abstracts and their references; static single-turn generation, scored by the two-stage framework.

## Domains

AI & Machine Learning Research — research ideation: generating novel research ideas in a scientific context.

## Evaluation

- Two-stage: GPT-4o ranking on novelty/feasibility indicators, then a relative "Insight Score."
- **Reported.** No single headline number in the abstract; the contribution is the dataset plus the evaluation framework.

## Typical Duration

Single-turn idea generation per context; no interactive setting.

## Main Contribution

A reproducible dataset-plus-framework for benchmarking LLM research ideation — grounding models in real research context and scoring ideas by novelty and feasibility rather than ad hoc inspection.

## Key Design Ideas

- Grounding in influential papers and references mirrors a researcher's actual starting context.
- The two-stage rank-then-Insight-Score design turns fuzzy "idea quality" into a metric.
- Separating novelty and feasibility indicators avoids collapsing distinct criteria.

## Strengths

- One of the first structured benchmarks for research idea generation, with a defined evaluation protocol.
- The Insight Score gives a comparable, relative measure across models.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); no venue and no official code/dataset URL are verifiable from the arXiv page (marked TODO(reference)); scale figures (models, dataset size) are not stated in the abstract.

## Related Works

- [LiveIdeaBench](./liveideabench.md) — Also research idea generation, from minimal single-keyword context.
- [MLR-Bench](./mlr-bench.md) — Also evaluates the idea-generation stage, within a full research pipeline.
- [MLGym](./mlgym.md) — Also exercises hypothesis/idea generation, as part of an AI-research loop.
