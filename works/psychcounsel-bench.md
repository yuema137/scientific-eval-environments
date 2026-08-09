# PsychCounsel-Bench (2025)

> **English** | [简体中文](../zh/works/psychcounsel-bench.md)

## Overview

PsychCounsel-Bench evaluates the psychology intelligence of LLMs on professional-certification questions: approximately 2,252 single-choice questions from the U.S. National Counselor Certification Exam, where advanced models clear the ~70% passing threshold while smaller open-source models fall well short.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.01611>
- **Code:** <https://github.com/cloversjtu/PsychCounsel-Bench>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

PsychCounsel-Bench grounds psychology evaluation in a professional standard: about 2,252 curated single-choice questions from the U.S. National Counselor Certification Exam (NCE), scored against the exam's ~70% passing threshold. Advanced models — GPT-4o, Llama3.3-70B, Gemma3-27B — clear the threshold comfortably, while smaller open-source models (Qwen2.5-7B, Mistral-7B) remain far below, making the benchmark a clean pass/fail-anchored measure of professional psychology knowledge.

## Tasks

~2,252 single-choice questions from the U.S. National Counselor Certification Exam; static QA scored against the ~70% pass threshold.

## Domains

Neuroscience & Cognitive Science — professional counseling psychology knowledge, sourced from a certification examination.

## Evaluation

- Accuracy against the ~70% NCE passing threshold across evaluated models.
- **Reported.** GPT-4o, Llama3.3-70B, and Gemma3-27B clear the threshold; Qwen2.5-7B and Mistral-7B fall far below.

## Typical Duration

Single-turn question answering; no interactive setting.

## Main Contribution

Anchoring psychology-knowledge evaluation to a real professional-certification standard, giving a pass/fail reference the field's ad-hoc accuracy scores lack.

## Key Design Ideas

- A certification exam supplies both questions and an authoritative pass threshold.
- Single-choice format keeps scoring objective and judge-free.
- The advanced-vs-small-model split locates where professional competence emerges.

## Strengths

- Professional-standard grounding with a public GitHub release.
- The 70%-threshold anchor makes results interpretable beyond relative ranking.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is stated in arXiv metadata, and per-model numeric scores are in the paper body.

## Related Works

- [CPsyExam](./cpsyexam.md) — Also psychology-exam evaluation, on Chinese examinations with a case-analysis axis.
- [ConceptPsy](./conceptpsy.md) — Also psychology-knowledge evaluation, at concept granularity.
- [MedHELM](./medhelm.md) — Also professional-standard clinical evaluation, across a broad medical taxonomy.
