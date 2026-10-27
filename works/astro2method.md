# Astro2Method (2026)

> **English** | [简体中文](../zh/works/astro2method.md)

> **First appeared:** 2026-10-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.30282)

## Overview

Astro2Method tests whether an LLM can choose the better machine-learning method for an astronomy problem. Each question gives a problem setup and two methods; the correct answer is the one the source paper measured as better. The benchmark then checks whether retrieval, agent scaffolds, or the source paper's own pipeline description change that choice.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** [Astro2Method: Benchmarking LLMs on Machine Learning Method Selection in Astronomy](https://arxiv.org/abs/2610.30282)
- **Full text:** <https://arxiv.org/html/2610.30282v1>
- **Dataset:** <https://huggingface.co/datasets/Xingzhongfan/Astro2Method> (500-row test split, CC BY 4.0)
- **Venue:** arXiv preprint (2026)

## Summary

Questions are built from comparisons reported in published astronomy papers. A comparison is kept only if the gap is significant: at least two standard deviations when uncertainties are reported, otherwise at least a 10% relative improvement. Difficulty depends on what the source authors explain. Easy items have a direct, complete explanation of why one method won; Hard items have only a partial one. Under direct prompting, models do well on Easy and stay close to chance on Hard. Retrieval and reasoning scaffolds do not consistently help. Supplying the source paper's pipeline description, with method names masked, raises Hard accuracy most.

## Tasks

500 binary questions from 346 papers, selected from 1,028 astronomy papers published 2024-01-01 to 2026-06-30; 376 Easy and 124 Hard. An LLM helped read papers and draft questions; human experts reviewed and revised every question. The number of experts is not stated. Example (Easy): to estimate stellar surface gravity from light curves, which network gives lower prediction error, a convolution-augmented Transformer or a convolution-only network? The model returns JSON with option A or B and a one-to-three-sentence reason. The item is correct if the option matches the source paper's result.

## Domains

Astronomy. Named topics include stellar astrophysics (stellar surface gravity, very metal-poor stars, accreted versus in-situ stars), galaxy photometric redshift, and a high-energy and time-domain group covering compact objects, transients, gravitational waves, and particle observations. Per-topic question counts appear only in a figure.

## Evaluation

- Metric: accuracy, reported as Overall, Easy, and Hard. Chance is 50%; the majority baseline is 50.4%.
- Direct prompting, five models: 87.50–92.55% on Easy, 58.87–64.52% on Hard, only 8.9–14.5 points above chance.
- Three models are also tested with text and structured RAG over 1,081 ML-in-astronomy papers from 2014–2023, a no-skill agent, ReAct, Self-Ask, CRITIC, three skills from Scientific Agent Skills, and required web search.
- ReAct, Self-Ask, and CRITIC search only the historical corpus; they score 1.4–6.2 points below direct prompting overall.
- Required web search reaches 70.97–75.00% on Hard. Its gains come mainly from questions where search found the source paper; on Hard questions without such a hit, no model has a positive net gain.
- Adding the masked source pipeline description raises Hard accuracy by 12.1–14.5 points over direct prompting.

## Typical Duration

Not reported. Agent settings are capped at six searches with three results each, six Self-Ask follow-ups, or three CRITIC verification rounds. Cost is not scored.

## Main Contribution

A literature-grounded benchmark that isolates machine-learning method selection in astronomy and separates comparisons whose reasons the source papers fully explain from those they only partly explain.

## Key Design Ideas

- Each answer key is a significance-filtered comparison reported by the source paper.
- Difficulty depends on how completely the source explains the result.
- Separate conditions supply related papers, the open web, or the masked source pipeline. They test whether the missing ingredient is experimental context or reasoning.

## Strengths

- Deterministic scoring against published results.
- Every question was human-reviewed, and the dataset is public.
- Source-paper exposure is counted per question, so web-search gains can be traced to finding the answer source.

## Limitations

- Two-option questions; ML-versus-traditional-method comparisons and papers without method comparisons are excluded.
- The authors cannot rule out that source papers appear in model training data. No human baseline or reviewer count is reported.
- Repository note: a label records which method the source paper measured as better under its own setup; it does not establish that method's advantage elsewhere.

## Related Works

- [AstroMLab 1](./astromlab-1.md) — Astronomy knowledge questions built from review literature.
- [AstroAlertBench](./astroalertbench.md) — Astrophysical classification decisions on survey alerts.
