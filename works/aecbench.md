# AECBench (2026)

> **English** | [简体中文](../zh/works/aecbench.md)

## Overview

AECBench is a hierarchical Chinese-language knowledge benchmark for the architecture, engineering and construction field: 4,800 engineer-authored questions across 23 tasks organized by a five-level cognition framework, with open-ended answers scored by an LLM judge against expert rubrics and a calibration step that corrects measured judge bias.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.18776>
- **Code:** <https://github.com/ArchiAI-LAB/AECBench>
- **Dataset:** <https://huggingface.co/datasets/jackluoluo/AECBench>
- **Venue:** Advanced Engineering Informatics, Vol. 71 (2026), Article 104314

## Summary

The authors argue that AEC work is safety-critical and code-governed, so a pooled accuracy number says little about whether an LLM can be trusted in practice; competence has to be resolved by cognitive level. AECBench therefore arranges 23 practice-derived tasks along five levels — Knowledge Memorization, Knowledge Understanding, Knowledge Reasoning, Knowledge Calculation, and Knowledge Application — with the application level further split into analysis, evaluation, and creation. Objective items are scored by accuracy; open-ended items, up to roughly 2,000-word engineering documents, are scored by an LLM-as-a-Judge against rubrics predefined by domain experts. The paper treats that judge as an object of study rather than an oracle, measuring its bias against expert scores and fitting regression calibrations to correct it.

## Tasks

4,800 questions across 23 tasks. Knowledge Memorization (3 tasks): code clause retrieval, terminology, abbreviations. Knowledge Understanding (3): code interpretation, design literacy, tabular data comprehension. Knowledge Reasoning (3): design decisions, building-type inference, reasoning over tables. Knowledge Calculation (4): architectural design, MEP design, construction, engineering economics. Knowledge Application (10): analysis (5), evaluation (2), creation (3). Questions come from two sources — items crafted by a cross-disciplinary team of domain engineers, and items drawn from official engineering licensure examinations — and passed a two-round review, a preliminary content review followed by expert review by engineers with 10+ years of experience. Answer formats shift with level: multiple choice dominates the lower levels, while higher levels use classification, extraction and open-ended generation, with creation tasks requiring documents of about 2,000 words. Questions are in Chinese.

## Domains

Civil & Structural Engineering: the question set is anchored in building codes and code tables, structural and seismic design, concrete structures, construction practice and engineering economics. Architectural and MEP design content is included as part of the AEC built-environment scope and folds into the same canonical domain; no second canonical domain is claimed.

## Evaluation

- Objective items (multiple choice, classification, extraction) are scored by accuracy against reference answers.
- Open-ended responses are scored by an LLM-as-a-Judge against rubrics predefined by domain experts, rather than against reference texts.
- The judge is calibrated: uncalibrated judging systematically compresses the scale, averaging 4.25/10 on responses experts rated 0–2 and 7.96/10 on responses rated 8–10. Isotonic regression and piecewise linear regression calibration reduce mean absolute error against expert scores from 2.947 to roughly 1.93–2.02.
- **Reported.** Nine LLMs were evaluated, including DeepSeek-R1, DeepSeek-V3, GPT-4o, GLM-4-Plus, Qwen-Turbo, QwQ-32B, Moonshot-v1-128k and Hunyuan-TurboS. DeepSeek-R1 leads on 14 of the 23 tasks. Performance falls monotonically across the five levels: terminology memorization exceeds 95% accuracy, while creation tasks average below 60% for every model. The paper's stated finding is that despite proficiency at the memorization and understanding levels, models "showed significant performance deficits, particularly in interpreting knowledge from tables in building codes, executing complex reasoning and calculation, and generating domain-specific documents."

## Typical Duration

N/A — single-turn question answering and document generation; no trajectory, wall-clock, or token budget is reported.

## Main Contribution

A cognition-oriented, level-resolved knowledge benchmark for the AEC field, built from practitioner-authored and licensure-exam items, together with an evaluation protocol that quantifies and corrects LLM-judge bias on open-ended engineering documents instead of assuming the judge is reliable.

## Key Design Ideas

- Five ordered cognition levels turn a single score into a degradation curve, localizing failure to a cognitive stage rather than a topic.
- The application level is subdivided into analysis, evaluation and creation, with creation requiring full-length engineering documents rather than short answers.
- Expert-predefined rubrics, not gold reference texts, drive judging for open-ended items.
- Judge outputs are recalibrated to the expert scale by isotonic and piecewise linear regression, and the calibration gain is reported as a measured error reduction.

## Strengths

- Items authored and reviewed by practising engineers with 10+ years of experience, plus official licensure-exam material.
- Explicitly measures LLM-judge bias against expert ratings and reports the residual error after calibration.
- Peer-reviewed venue, with public code and dataset.

## Limitations

- Not agentic: single-turn question answering and document generation, with no tools, environment, or multi-step execution.
- Items are in Chinese and anchored to Chinese national codes; transfer to Eurocode, ACI, AISC or ASCE practice is untested.
- The benchmark measures knowledge and document generation, not verified engineering outcomes — no answer is checked against a solver or a compliance engine.
- Repository note: the paper reports task counts per cognition level but does not break out the 4,800 questions per level.

## Related Works

- [ERI Benchmark](./eri-benchmark.md) — Also a taxonomy-driven engineering knowledge benchmark with a civil field, but synthetically generated across nine engineering disciplines.
- [StructureClaw](./structureclaw.md) — Also civil/structural, but scores executable structural-analysis workflows instead of knowledge questions.
- [AEC-Bench](./aec-bench.md) — Similarly named but distinct: an agentic multimodal benchmark over real construction documents.
- [DrafterBench](./drafterbench.md) — Also civil-engineering practice work, evaluated as tool-executing drawing revision rather than knowledge QA.
