# ConceptPsy (2023)

> **English** | [简体中文](../zh/works/conceptpsy.md)

## Overview

ConceptPsy is a psychology benchmark suite built for conceptual comprehensiveness: 12 core subjects and 1,383 manually collected concepts, with each question annotated to a chapter so that per-concept performance — not just an aggregate score — becomes visible.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2311.09861>
- **Venue:** arXiv preprint (cs.CL), 2023

## Summary

ConceptPsy argues that a single psychology accuracy number hides where models actually fail, so it organizes evaluation by concept: 12 core subjects and 1,383 manually collected concepts, with GPT-4-generated questions per concept reviewed by psychologists and each item annotated to a chapter. Chapter-wise accuracy reveals significant performance variation across concepts — even for models from the same series — that an aggregate score would mask.

## Tasks

Psychology questions spanning 12 core subjects and 1,383 concepts, each annotated to a chapter; static QA. Total question count is TODO(reference) — not stated in the abstract.

## Domains

Neuroscience & Cognitive Science — psychology knowledge across 12 core subjects at concept granularity.

## Evaluation

- Overall accuracy plus chapter-wise (per-concept) accuracy across a broad range of LLMs.
- **Reported.** Significant performance variation across concepts, even within the same model series; numeric results are TODO(reference).

## Typical Duration

Single-turn question answering; no interactive setting.

## Main Contribution

Concept-level psychology evaluation — annotating every question to a chapter so that per-concept weaknesses surface instead of averaging out.

## Key Design Ideas

- Concept-level annotation turns one score into a per-concept profile.
- Manual concept collection (1,383) ensures comprehensive coverage.
- Psychologist review of generated questions guards item quality.

## Strengths

- Concept granularity makes the benchmark diagnostic rather than just comparative.
- Comprehensive coverage across 12 core psychology subjects.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); the paper is under review (no venue on arXiv), the total question count is not stated, and no code URL is confirmed from the arXiv page.

## Related Works

- [CPsyExam](./cpsyexam.md) — Also a Chinese psychology-knowledge benchmark, organized along knowledge and case-analysis axes.
- [PsychCounsel-Bench](./psychcounsel-bench.md) — Also psychology-knowledge evaluation, on counselor-certification questions.
- [BrainBench](./brainbench.md) — Also a neuroscience/psychology-domain benchmark, on prospective result prediction.
