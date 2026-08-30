# SeePhys (2025)

> **English** | [简体中文](../zh/works/seephys.md)

> **First appeared:** 2025-05-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.19099)

## Overview

SeePhys is a large-scale multimodal benchmark for vision-based physics reasoning, spanning middle school to PhD qualifying exams across 7 fundamental physics domains and 21 categories of highly heterogeneous diagrams, with 75% of problems vision-essential.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.19099>
- **Code:** <https://github.com/SeePhys/seephys-project>
- **Dataset:** <https://huggingface.co/datasets/SeePhys/SeePhys>
- **Project:** <https://seephys.github.io/>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks

## Summary

SeePhys asks whether seeing helps thinking: its problems are built so that a substantial proportion (75%) cannot be solved without extracting information from the diagram — circuit schematics, Feynman diagrams, and 19 other diagram categories. Per the official project page it comprises 2,000 rigorously validated questions across 8 knowledge tiers, with 43 models evaluated (23 MLLMs and 20 LLMs). Even the most advanced visual reasoning models, such as Gemini 2.5 Pro and o4-mini, achieve sub-60% accuracy.

## Tasks

Multimodal physics problems from middle school to PhD qualifying level across 7 domains and 21 diagram categories; 2,000 validated questions per the official project page; static problem solving.

## Domains

Physics across 7 fundamental domains (not enumerated in the abstract), with diagram types including circuit schematics and Feynman diagrams.

## Evaluation

- Accuracy on vision-essential multimodal problem solving.
- **Reported.** The most advanced visual reasoning models (e.g., Gemini 2.5 Pro, o4-mini) achieve sub-60% accuracy; the official page reports best MLLM GPT-5 (high) at 63.2% and human experts at 86.5%.

## Typical Duration

Single-problem multimodal solving; not an interactive agent setting.

## Main Contribution

Makes the diagram a load-bearing part of physics evaluation: with 75% vision-essential problems, scores measure physical reasoning over visual information, not text-only shortcuts.

## Key Design Ideas

- Vision-essentiality is enforced at construction, so blind models cannot score by language alone.
- 21 heterogeneous diagram categories cover the actual visual vocabulary of physics.
- The school-to-PhD span turns one benchmark into a difficulty ladder.

## Strengths

- Strict multimodality with quantified vision-essential share.
- Broad model coverage (43 models per the project page) against a human-expert anchor.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The seven domains are not enumerated in those sources.

## Related Works

- [PHYBench](./phybench.md) — Also original-problem physics evaluation, text-only with an expression-distance metric.
- [UGPhysics](./ugphysics.md) — Also broad-coverage physics problem solving, bilingual and text-only.
- [HiPhO](./hipho.md) — Also mixes text and diagram modalities, on recent olympiad exams with official marking.
