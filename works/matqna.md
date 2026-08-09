# MatQnA (2025)

> **English** | [简体中文](../zh/works/matqna.md)

## Overview

MatQnA is a benchmark dataset for multimodal LLMs in materials characterization and analysis, spanning ten mainstream characterization methods — XPS, XRD, SEM, TEM and others — where the most advanced models (GPT-4.1, Claude 4, Gemini 2.5, Doubao Vision Pro) already reach nearly 90% on objective questions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.11335>
- **Dataset:** <https://huggingface.co/datasets/richardhzgg/matQnA>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

MatQnA organizes materials-characterization evaluation by method: ten mainstream techniques including X-ray photoelectron spectroscopy, X-ray diffraction, scanning electron microscopy, and transmission electron microscopy. Its QA pairs — both multiple-choice and subjective — are built by a hybrid approach combining LLMs with human-in-the-loop validation. Preliminary results show frontier multimodal models (GPT-4.1, Claude 4, Gemini 2.5, Doubao Vision Pro 32K) already achieve nearly 90% accuracy on objective data-interpretation questions, marking characterization QA as closer to solved than the harder reasoning benchmarks.

## Tasks

Multiple-choice and subjective QA over ten characterization methods (XPS, XRD, SEM, TEM, and others); static multimodal QA. Total question count is TODO(reference) — not stated in the abstract.

## Domains

Materials science — instrument-level materials characterization and analysis across ten techniques.

## Evaluation

- Objective (multiple-choice) accuracy and subjective evaluation; QA built via LLM-plus-human-in-the-loop validation.
- **Reported.** Frontier models reach nearly 90% accuracy on objective questions (described as preliminary results).

## Typical Duration

Single-turn multimodal questions; no interactive setting.

## Main Contribution

A method-organized characterization benchmark whose near-90% frontier scores locate objective data interpretation as an area where current MLLMs are already strong — a useful contrast to the reasoning-heavy materials benchmarks where they fail.

## Key Design Ideas

- Organizing by characterization method makes per-technique competence visible.
- Mixing objective and subjective questions separates recall from open interpretation.
- Human-in-the-loop validation guards QA quality.

## Strengths

- Broad instrument coverage in one dataset with a public HuggingFace release.
- The near-90% objective result is a clear, citable capability marker.

## Limitations

- Repository note: card compiled from the arXiv abstract and dataset page (August 2026); the total question count is not stated, and results are described by the authors as preliminary. No venue is stated in arXiv metadata.

## Related Works

- [MatCha](./matcha.md) — Also multimodal characterization evaluation, organized by research stage rather than method.
- [MatVQA](./matvqa.md) — Also characterization VQA, with shortcut-resistant visual reasoning tasks.
- [OpenXRD](./openxrd.md) — Also characterization QA, specialized to X-ray diffraction.
