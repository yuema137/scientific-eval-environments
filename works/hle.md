# Humanity's Last Exam (2025)

> **English** | [简体中文](../zh/works/hle.md)

> **First appeared:** 2025-01-24 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2501.14249)

## Overview

Humanity's Last Exam (HLE) is a multi-modal benchmark at the frontier of human knowledge, designed as the final closed-ended academic benchmark of its kind: 2,500 questions across dozens of subjects — mathematics, humanities, and the natural sciences — developed globally by subject-matter experts. It is a general academic benchmark rather than an agent benchmark (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.14249>
- **Project:** <https://lastexam.ai>
- **Publication:** <https://www.nature.com/articles/s41586-025-09962-4>
- **Venue:** Nature, 2025

## Summary

HLE responds to benchmark saturation — LLMs exceeding 90% on suites like MMLU — with questions at the expert human frontier. Each of the 2,500 multiple-choice and short-answer questions has a known, unambiguous, easily verifiable solution suitable for automated grading, yet cannot be quickly answered via internet retrieval. State-of-the-art LLMs demonstrate low accuracy and calibration on HLE, quantifying the gap between current models and the expert human frontier on closed-ended academic questions.

## Tasks

2,500 expert-authored multiple-choice and short-answer questions across dozens of subjects, including mathematics, humanities, and the natural sciences; static question answering.

## Domains

Dozens of academic subjects spanning mathematics, humanities, and the natural sciences; the benchmark is deliberately subject-broad rather than field-specific.

## Evaluation

- Automated grading against known, unambiguous solutions; calibration measured alongside accuracy.
- **Reported.** State-of-the-art LLMs demonstrate low accuracy and calibration on HLE.

## Typical Duration

Single-question answering; not an interactive agent setting.

## Main Contribution

A globally expert-authored ceiling for closed-ended academic evaluation: hard enough to restore headroom, automatically gradable, and retrieval-resistant by construction.

## Key Design Ideas

- Questions must be unambiguous and verifiable yet not answerable by quick internet retrieval.
- Global expert authorship pushes difficulty to the frontier of each subject.
- Calibration is reported alongside accuracy, so overconfidence at the frontier is itself measured.

## Strengths

- Restores measurable headroom where popular benchmarks have saturated.
- Public release with automated grading keeps frontier comparison reproducible.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: HLE is a general closed-ended academic benchmark, not an agent or science-specific benchmark; it is documented here as the frontier-difficulty reference point that research-level scientific benchmarks position themselves against.

## Related Works

- [Agents' Last Exam](./agents-last-exam.md) — The agentic namesake: long-horizon professional workflows rather than closed-ended questions.
- [CritPt](./critpt.md) — Also frontier-difficulty, guess-resistant academic evaluation, specialized to research-level physics.
- [GAIA](./gaia.md) — Also positions itself against benchmark saturation, via tool-requiring assistant questions rather than expert knowledge.
