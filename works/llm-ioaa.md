# LLM-IOAA (2025)

> **English** | [简体中文](../zh/works/llm-ioaa.md)

## Overview

LLM-IOAA is a systematic evaluation of frontier large language models on the complete theory and data-analysis exams of the International Olympiad on Astronomy & Astrophysics (IOAA), graded by former IOAA contestants and team leaders against the official marking schemes and scored against real contestant distributions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.05016>
- **Code:** <https://github.com/OSU-NLP-Group/LLM-IOAA>
- **Venue:** arXiv preprint, astro-ph.IM (October 2025); no peer-reviewed venue stated in the primary source

## Summary

The work takes four consecutive years of IOAA exams (2022–2025) — an international pre-university olympiad whose problems demand deep conceptual understanding, multi-step astrophysical derivation, and multimodal analysis of real observational data — and runs five frontier LLMs on every problem. Answers are graded by two authors who are themselves former IOAA participants and national team leaders, using the official IOAA rubrics, with every model–problem assessment independently graded twice and discrepancies resolved by consensus. Gemini 2.5 Pro and GPT-5 reach gold-medal-level scores on the theory exams, ranking in roughly the top two among the 200–300 human contestants per year, while performance on the data-analysis exams diverges sharply across models. The authors accompany the scores with an eight-category error taxonomy that locates the remaining failures in conceptual and geometric/spatial reasoning rather than arithmetic.

## Tasks

57 problems drawn from the official IOAA exams of 2022, 2023, 2024 and 2025: 49 theory problems and 8 data-analysis problems. Theory exams are worth 300 points per year (250 in 2023) and data-analysis exams 150 points per year (125 in 2023); individual problems are valued between 5 and 75 points. Problems were converted to LaTeX for model input, with permission from the IOAA Executive Committee, and the processed problems, model responses and grading report are released. Theory problems are further split by the authors into a geometric/spatial-reasoning category (37%) and a physics/mathematics category (63%). Content spans stellar and galactic astrophysics, celestial mechanics and spherical astronomy, cosmology, and interpretation of plots and astronomical images.

## Domains

Astronomy and astrophysics — the evaluated objective is astronomical throughout: positional and spherical astronomy, stellar structure and evolution, celestial mechanics, galactic and extragalactic astronomy, cosmology, and the analysis of real observational data such as light curves, spectra and sky images. The physics and mathematics invoked are applied to astronomical objects and observations rather than studied for their own sake.

## Evaluation

Human expert grading against the official IOAA rubrics and marking schemes, awarding partial credit exactly as for human contestants. Two graders — a 2018 IOAA participant and 2022–2023/2025 team leader, and a 2018 participant and 2021 team leader — independently produced all 285 assessments (57 problems × 5 models); discrepancies were resolved by discussion until consensus. Scores are reported as percentages of available points per exam and mapped onto the medal thresholds and contestant score distributions of the corresponding year. Errors are classified into eight categories: conceptual errors (most prevalent), geometric/spatial reasoning, plot/image interpretation, calculation, approximation, notation precision, incomplete derivations, and LaTeX formatting.

- **Reported (theory, all years combined):** Gemini 2.5 Pro 85.6% ± 8.0, GPT-5 84.2% ± 6.1, OpenAI o3 77.5% ± 12.2, Claude Opus 4.1 64.7% ± 13.5, Claude Sonnet 4 60.6% ± 9.5.
- **Reported (data analysis, all years combined):** GPT-5 88.5% ± 12.6, Gemini 2.5 Pro 75.7% ± 15.5, OpenAI o3 67.7% ± 18.0, Claude Opus 4.1 54.8% ± 19.1, Claude Sonnet 4 47.9% ± 20.9.
- **Reported (ranking):** GPT-5 and Gemini 2.5 Pro place in roughly the top two among 200–300 contestants across the 2022–2025 theory exams, i.e. gold-medal level.

## Typical Duration

Single-pass direct prompting per problem; no interactive environment, tool use or iterative trajectory. Per-problem token or wall-clock budgets are not stated in the primary source. TODO(reference).

## Main Contribution

The first systematic assessment of frontier LLMs against the full theory and data-analysis exams of an international astronomy olympiad, graded by domain-expert former contestants under the official rubrics and calibrated against real human score distributions, together with an error taxonomy showing that the residual gap lies in conceptual and geometric/spatial reasoning rather than computation.

## Key Design Ideas

- Use complete, unmodified official olympiad exams rather than curated question subsets, so the difficulty and coverage are set by an external standard.
- Grade with the official IOAA marking schemes and partial-credit rules, making model scores directly comparable to human contestant scores and medal thresholds.
- Recruit graders who are themselves former IOAA participants and national team leaders, and grade every model–problem pair twice independently.
- Keep the data-analysis exams as a separate track, so multimodal handling of plots, images and real observational data is measured apart from closed-form derivation.
- Separate theory problems into geometric/spatial versus physics/mathematics categories to localize where models fail.
- Release the LaTeX-converted problems, model responses, grading report and prompting code under permission from the IOAA Executive Committee.

## Strengths

- Grading is anchored to an external, official rubric and to real human score distributions, avoiding a self-defined difficulty scale.
- Double-blind-style dual grading of all 285 assessments with consensus resolution gives unusually strong scoring reliability for a free-response evaluation.
- The data-analysis half goes beyond recall, requiring interpretation of plots, images and observational data.
- The eight-category error taxonomy makes the results diagnostic rather than a single leaderboard number.
- Materials are publicly released with explicit permission from the exam organizers.

## Limitations

- 57 problems across four exam years is a small sample; per-exam standard deviations are large (up to ±21 percentage points on data analysis).
- Pre-university olympiad problems are well-posed with known answers and do not test open-ended astronomical research, tool use, or work on real archival datasets.
- Single-pass direct prompting only; no agentic scaffold, retrieval, or code execution is evaluated.
- Repository note: IOAA exams and their solutions are publicly available, so contamination of model training data cannot be excluded; the primary source's treatment of this risk is not transcribed here. TODO(reference).
- Repository note: the paper describes itself as a preprint "to be submitted"; no peer-reviewed venue is confirmed as of this card's compilation (August 2026).

## Related Works

- [Stargazer](./stargazer.md) — also astronomy-specific agent evaluation, but on iterative model fitting over radial-velocity time series rather than exam problems.
- [ReplicationBench](./replicationbench.md) — also astrophysics evaluation, targeting replication of published research instead of olympiad problems.
- [AstroMLab 1](./astromlab-1.md) — the astronomy-knowledge MCQ benchmark this work contrasts with by using free-response, rubric-graded problems.
- [SeePhys](./seephys.md) — comparable exam-derived multimodal reasoning evaluation in physics.
- [MaScQA](./mascqa.md) — comparable exam-derived domain evaluation with a conceptual-versus-computational error analysis.
