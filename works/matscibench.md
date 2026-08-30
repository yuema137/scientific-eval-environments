# MatSciBench (2025)

> **English** | [简体中文](../zh/works/matscibench.md)

> **First appeared:** 2025-10-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.12171)

## Overview

MatSciBench benchmarks the reasoning ability of large language models in materials science: 1,340 college-level problems spanning the essential subdisciplines, with detailed reference solutions for 946 and images for 315 — DeepSeek-R1 tops text-only questions at 75.22% while GPT-5 leads image questions at 53.02%.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.12171>
- **Code:** <https://github.com/Jun-Kai-Zhang/MatSciBench>
- **Dataset:** <https://huggingface.co/datasets/JunkaiZ/MatSciBench>
- **Venue:** KDD 2026 (per the official repository; arXiv metadata carries no venue)

## Summary

MatSciBench moves materials evaluation from knowledge recall to multi-step reasoning: 1,340 college-level problems across the essential materials subdisciplines, 946 with detailed reference solutions and 315 posed with images. Leading thinking and non-thinking LLMs are evaluated, and the split by modality is telling — DeepSeek-R1 reaches 75.22% on text-only questions but the best image performer (GPT-5) manages only 53.02%, marking multimodal materials reasoning as the harder frontier.

## Tasks

1,340 college-level materials-science problems across the field's subdisciplines (946 with reference solutions, 315 with images); static text and multimodal QA.

## Domains

Materials science — college-level reasoning across the essential subdisciplines of the field.

## Evaluation

- Accuracy on text-only and image questions, with reference solutions supporting process-level error analysis.
- **Reported.** DeepSeek-R1 75.22% on text-only questions; GPT-5 53.02% on image questions.

## Typical Duration

Single-turn problems; no interactive setting.

## Main Contribution

A reasoning-centered materials benchmark with reference solutions and a text-vs-image split that quantifies how far multimodal materials reasoning lags text reasoning.

## Key Design Ideas

- Reference solutions enable process-level, not just answer-level, evaluation.
- The text/image partition isolates the multimodal reasoning gap.
- Broad subdiscipline coverage prevents narrow-topic overfitting.

## Strengths

- Venue-verified (KDD 2026) with full public code and dataset.
- The 75% vs 53% modality gap is a clear, citable capability marker.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the exact number of evaluated LLMs is not stated in the abstract. The KDD 2026 venue is a repository claim, not in arXiv metadata.

## Related Works

- [MaScQA](./mascqa.md) — Also materials-knowledge QA, at exam scope without reference-solution grading.
- [MatVQA](./matvqa.md) — Also multimodal materials reasoning, focused on characterization imagery.
- [AtomWorld](./atomworld.md) — Also materials reasoning, on verifiable crystal-structure manipulation.
