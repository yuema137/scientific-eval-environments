# CritPt (2025)

> **English** | [简体中文](../zh/works/critpt.md)

## Overview

CritPt (Complex Research using Integrated Thinking – Physics Test, pronounced "critical point") is a benchmark of 71 composite, unpublished research-level physics challenges, decomposed into 190 simpler checkpoint tasks, newly created by more than 50 active physics researchers across 11+ subfields.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.26574>
- **Code:** <https://github.com/CritPt-Benchmark/CritPt>
- **Dataset:** <https://huggingface.co/datasets/CritPt-Benchmark/CritPt>
- **Project:** <https://critpt.com>
- **Venue:** arXiv preprint (cs.AI, cond-mat, hep-th, quant-ph), 2025

## Summary

CritPt simulates full-scale research projects at the entry level: every challenge is unpublished and hand-curated to admit a guess-resistant, machine-verifiable answer, graded by an automated pipeline heavily customized for advanced physics-specific output formats. Challenges decompose into 190 checkpoint tasks that localize where reasoning breaks down. The best average accuracy among base models is only 5.7% (GPT-5, high), rising moderately to around 10% when models are equipped with coding tools.

## Tasks

71 composite research challenges plus 190 decomposed checkpoint tasks, authored by 50+ active physics researchers; answers are unpublished, guess-resistant, and machine-verifiable.

## Domains

Eleven-plus physics subfields: condensed matter, quantum physics, atomic, molecular & optical physics, astrophysics, high energy physics, mathematical physics, statistical physics, nuclear physics, nonlinear dynamics, fluid dynamics, and biophysics.

## Evaluation

- Automated grading pipeline customized for advanced physics-specific output formats; answers designed guess-resistant and machine-verifiable.
- **Reported.** Best base-model average accuracy 5.7% (GPT-5, high); around 10% with coding tools.

## Typical Duration

Composite research-challenge episodes, optionally with coding tools; not an interactive environment.

## Main Contribution

Sets the evaluation bar at unpublished, entry-level research problems while keeping grading fully automatic — and shows frontier models converge to single-digit accuracy there.

## Key Design Ideas

- Unpublished, researcher-authored challenges make contamination structurally impossible.
- Guess-resistant answer formats close the lucky-guess channel that plagues hard QA.
- The challenge → checkpoint decomposition locates failure within a research workflow, not just at its end.

## Strengths

- 50+ active researchers authoring at their own working level.
- The 5.7%→10% tool delta cleanly measures what coding tools buy on research-level physics.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. Venue acceptance claims circulating for this work are not verifiable from the paper's arXiv page.

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — Also researcher-authored, machine-graded physics at expert level, confined to condensed matter theory.
- [PRL-Bench](./prl-bench.md) — Also frontier physics research evaluation, sourced from recent PRL papers rather than unpublished challenges.
- [PhySciBench](./physcibench.md) — Also expert-curated physical-science evaluation, at deep-research rather than research-entry level.
