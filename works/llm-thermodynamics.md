# Using Large Language Models for Solving Thermodynamic Problems (2025)

> **English** | [简体中文](../zh/works/llm-thermodynamics.md)

## Overview

A benchmark study that evaluates five large language models on 22 chemical-engineering thermodynamics problems, with answers graded by trained human experts in the manner of academic exam grading.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2502.05195
- **Venue:** Computers and Chemical Engineering, Volume 204 (2026), article 109333 — DOI 10.1016/j.compchemeng.2025.109333 (arXiv preprint submitted January 2025)

## Summary

The work constructs a benchmark of 22 thermodynamics problems, spanning both simple and advanced difficulty, to probe how well LLMs handle domain-specific reasoning in chemical-engineering thermodynamics. Five models — GPT-3.5, GPT-4, GPT-4o, Llama 3.1, and Mistral's le Chat — are prompted on the problems and their responses are scored by trained human experts. The study finds that models generally do well on simple problems but exhibit inconsistency, contextual misunderstanding, and incorrect assumptions on advanced problems, concluding that current LLMs struggle with the interpretation and reasoning required for complex thermodynamic tasks.

## Tasks

22 thermodynamics problems written by the authors for this study, all fully specified in text, each with a unique solution, and each requiring the calculation of numerical values of variables. 13 are classified as simple: closed systems containing an ideal gas undergoing a single change of state (isothermal, isobaric, isochoric, polytropic; adiabatic and non-adiabatic variants). 9 are classified as advanced and span a wider range of thermodynamic knowledge — closed and open systems, multi-step processes including cyclic processes, and processes involving liquids as well as gases. Each problem was presented three times to each model as independent queries.

## Domains

Chemical Engineering: the problems target chemical-engineering thermodynamics, a core subject of the discipline, and the work is published in *Computers and Chemical Engineering*. The subject matter overlaps with physical chemistry, but the framing, problem set, and venue are chemical-engineering.

## Evaluation

Model responses are graded by trained human experts following a methodology akin to grading academic exam responses, using a partial-credit rubric that awards 0.5 points for each correctly executed step towards the final solution; the authors estimate the resulting score uncertainty at typically ±0.5 points. Scores are aggregated as mean percentages per model and reported separately for the simple and advanced subsets, alongside an analysis of answer consistency across the three repetitions. Reported mean scores include, on the simple problems, 88.57% (GPT-4), 87.09% (GPT-4o), 75.88% (Llama 3.1) and 72.82% (le Chat); on the advanced problems 55.19% (GPT-4o), 51.93% (le Chat), 47.52% (GPT-4) and 40.70% (Llama 3.1).

## Typical Duration

N/A — single-turn question answering rather than an agentic trajectory; no per-task token or wall-clock budget is reported.

## Main Contribution

A domain-specific benchmark and expert-graded evaluation of five LLMs on chemical-engineering thermodynamics problems, quantifying that current models reason reliably on simple problems but fail on advanced ones due to inconsistency, contextual misunderstanding, and incorrect assumptions.

## Key Design Ideas

- A purpose-written set of 22 thermodynamics problems split into 13 simple and 9 advanced items, all text-specified with unique numerical solutions so that grading is unambiguous.
- Human expert grading modeled on academic exam marking rather than automated string/answer matching, with 0.5 points per correctly executed solution step so that partial reasoning credit is captured.
- Three independent repetitions of every problem per model, making answer consistency (not just accuracy) an explicit evaluation dimension.
- Comparative evaluation across five models spanning proprietary and open families (GPT-3.5, GPT-4, GPT-4o, Llama 3.1, Mistral le Chat).

## Strengths

- Expert human grading captures partial correctness and reasoning quality, appropriate for open-ended thermodynamics problems.
- Difficulty stratification (simple vs. advanced) isolates where model reasoning degrades.
- Cross-model comparison over both proprietary and open-weight LLMs.

## Limitations

- Small scale (22 problems), limiting statistical power and coverage of the thermodynamics curriculum.
- Human expert grading is costly and not directly reproducible as an automated harness; the authors themselves put the score uncertainty at typically ±0.5 points.
- Simple problems are confined to single changes of state of an ideal gas in closed systems, so the easy half of the benchmark exercises a narrow slice of thermodynamics.
- Repository note: the problems are answered in a single turn with no tools, so the benchmark measures model knowledge and reasoning rather than agentic behaviour; there is no environment, trajectory, or resource dimension.
- Repository note: no public code/data repository is linked from the arXiv landing page, so the benchmark items and rubric may not be independently reusable.

## Related Works

- [ChemBench](./chembench.md) — LLM evaluation on chemistry knowledge and reasoning, an adjacent (chemistry, not process-engineering) domain benchmark.
- [CRAFTS](./crafts.md) — chemical-engineering evaluation on the executable process-simulation side, in contrast to this work's closed-form problem solving.
