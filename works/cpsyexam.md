# CPsyExam (2024)

> **English** | [简体中文](../zh/works/cpsyexam.md)

## Overview

CPsyExam is a Chinese benchmark for evaluating psychology knowledge in LLMs using examination questions: from a pool of 22,000 questions, 4,000 are curated into the benchmark along two axes — psychological knowledge and case analysis.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.10212>
- **Venue:** COLING 2025

## Summary

CPsyExam assembles psychology examination questions into a structured LLM benchmark: a 22,000-question pool distilled to a 4,000-question benchmark with balanced subject coverage, organized along two axes — psychological knowledge (recall and understanding) and case analysis (applying psychology to scenarios). It compares open-source and API-based LLMs across granularities, targeting psychology as a knowledge domain rather than testing whether models have psychological traits.

## Tasks

4,000 examination questions (from a 22,000-question pool) across psychology subjects, split into psychological-knowledge and case-analysis axes; static QA.

## Domains

Neuroscience & Cognitive Science — psychology knowledge and case analysis, assessed through Chinese examination questions.

## Evaluation

- Accuracy across subjects and the two axes (psychological knowledge, case analysis), compared across LLMs at various granularities.
- **Reported.** LLMs are compared across granularities; per-model numeric results are TODO(reference) — not stated in the abstract.

## Typical Duration

Single-turn question answering; no interactive setting.

## Main Contribution

A structured psychology-knowledge benchmark separating recall from case application — measuring psychology as a scientific domain, distinct from the psychology-of-LLMs capability literature.

## Key Design Ideas

- The knowledge / case-analysis split separates factual recall from applied reasoning.
- Distilling 22k to a balanced 4k keeps subject coverage even.
- Examination sourcing anchors difficulty to a recognized standard.

## Strengths

- Venue-verified (COLING 2025) and one of the larger dedicated psychology-knowledge benchmarks.
- The two-axis design makes applied-reasoning weakness visible separately from recall.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); the subject count and per-model results are in the paper body (TODO(reference)), and no code URL is confirmed from the arXiv page.

## Related Works

- [ConceptPsy](./conceptpsy.md) — Also a Chinese psychology-knowledge benchmark, organized by concept comprehensiveness.
- [PsychCounsel-Bench](./psychcounsel-bench.md) — Also psychology-exam evaluation, on U.S. counselor-certification questions.
- [MaScQA](./mascqa.md) — Also an exam-sourced domain-knowledge benchmark, in materials science.
