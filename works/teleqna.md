# TeleQnA (2023)

> **English** | [简体中文](../zh/works/teleqna.md)

## Overview

TeleQnA is the first benchmark dataset for assessing the telecommunications knowledge of large language models: 10,000 multiple-choice questions drawn from standards (3GPP, IEEE) and research articles, on which LLMs can rival active telecom professionals in general knowledge but struggle with complex standards questions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.15051>
- **Code:** <https://github.com/netop-team/TeleQnA>
- **Venue:** arXiv preprint (cs.IT), 2023

## Summary

TeleQnA measures whether LLMs know telecommunications: 10,000 multiple-choice questions spanning lexicon, research overview, research publications, standards overview, and standards specifications, sourced from 3GPP and IEEE standards and the research literature. GPT-3.5 and GPT-4 are benchmarked against active telecom professionals, and the paper studies how adding telecom context changes performance. The finding is a split: LLMs rival professionals on general telecom knowledge but struggle with complex standards-related questions.

## Tasks

10,000 multiple-choice telecom questions across five categories (lexicon, research overview, research publications, standards overview, standards specifications); static knowledge QA.

## Domains

Electrical Engineering — telecommunications and communications engineering knowledge, grounded in 3GPP/IEEE standards and research literature.

## Evaluation

- Multiple-choice accuracy, benchmarked against active telecom professionals, with a context-augmentation study.
- **Reported.** LLMs rival professionals on general telecom knowledge; they struggle with complex standards-specification questions.

## Typical Duration

Single-turn question answering; no interactive setting.

## Main Contribution

The founding telecom-knowledge benchmark for LLMs — with a professional baseline that locates the frontier weakness precisely at standards specifications.

## Key Design Ideas

- Sourcing from 3GPP/IEEE standards grounds difficulty in the field's authoritative documents.
- The five categories separate vocabulary and overview knowledge from deep standards detail.
- A professional human baseline turns "good at telecom" into a measured comparison.

## Strengths

- Large (10,000) and widely reused as the reference telecom-knowledge benchmark, publicly released.
- The standards-vs-general split is a clear, actionable finding for telecom LLM builders.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is stated in arXiv metadata. Category counts come from the repository, not the abstract.
- Evaluates GPT-3.5/GPT-4 only in the original paper; newer models are not covered there.

## Related Works

- [MaScQA](./mascqa.md) — Also expert-domain knowledge QA benchmarked against professionals, in materials science.
- [ElecBench](./elecbench.md) — Also an electrical-domain LLM benchmark, on power-grid operation.
- [SciExplore](./sciexplore.md) — Also standards/literature-grounded information seeking, across broader disciplines.
