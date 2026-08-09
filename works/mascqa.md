# MaScQA (2023)

> **English** | [简体中文](../zh/works/mascqa.md)

## Overview

MaScQA is a question-answering dataset for probing the materials-science knowledge of large language models: 650 challenging questions drawn from India's GATE engineering exams, classified into four types, where GPT-4 reaches about 62% accuracy and most errors are conceptual rather than computational.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.09115>
- **Code:** <https://github.com/M3RG-IITD/MaScQA>
- **Venue:** Digital Discovery, 2024 (per the official repository; arXiv metadata carries no venue)

## Summary

MaScQA curates 650 materials-science and metallurgy questions from GATE (Graduate Aptitude Test in Engineering) papers, spanning 14 topics and four question types. GPT-3.5 and GPT-4 answer them under zero-shot and chain-of-thought prompting, with GPT-4 best at roughly 62% accuracy. The error analysis is the substance: conceptual errors dominate at about 64% versus 36% computational, locating the deficit in materials understanding rather than arithmetic.

## Tasks

650 GATE-derived materials-science and metallurgy questions in four types across 14 topics; static QA under zero-shot and chain-of-thought prompting.

## Domains

Materials science — undergraduate/graduate materials-science and metallurgical-engineering knowledge, sourced from standardized engineering exams.

## Evaluation

- Accuracy on the 650 questions, with an error taxonomy splitting conceptual from computational errors.
- **Reported.** GPT-4 best at ~62% accuracy; conceptual errors ~64% vs. computational ~36%.

## Typical Duration

Single-turn question answering; no interactive setting.

## Main Contribution

An early, exam-grounded measurement of LLM materials knowledge whose error analysis showed the gap is conceptual — the substrate benchmark later materials-QA work builds on.

## Key Design Ideas

- GATE-exam sourcing anchors difficulty to a recognized professional standard.
- Four question types separate recall from multi-step problem solving.
- The conceptual-vs-computational error split makes the failure mode diagnostic.

## Strengths

- A clean, widely reused reference for materials-knowledge QA, publicly released.
- The error taxonomy gives more insight than a single accuracy number.

## Limitations

- Repository note: card compiled from the arXiv abstract, full text, and official repository (August 2026); the dataset holds exactly 650 questions (a "1,038" figure sometimes cited is a misattribution). The Digital Discovery venue is stated by the repository, not arXiv metadata.
- Evaluates off-the-shelf GPT-3.5/GPT-4 only; newer models are not covered by the original paper.

## Related Works

- [MatSciBench](./matscibench.md) — Also materials-knowledge evaluation, scaled to 1,340 college-level reasoning problems with images.
- [OpenXRD](./openxrd.md) — Also expert-curated materials QA, specialized to crystallography.
- [MaCBench](./macbench.md) — Also materials/chemistry evaluation, in a multimodal setting.
