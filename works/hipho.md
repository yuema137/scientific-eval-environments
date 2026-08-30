# HiPhO (2025)

> **English** | [简体中文](../zh/works/hipho.md)

> **First appeared:** 2025-09-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2509.07894)

## Overview

HiPhO is a high-school physics olympiad benchmark compiling the 13 latest (2024–2025) international and regional olympiad exams, graded with official marking schemes at both answer and step level, and mapping model scores onto official gold/silver/bronze medal thresholds for direct comparison with human contestants.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.07894>
- **Code:** <https://github.com/SciYu/HiPhO>
- **Leaderboard:** <https://phyarena.github.io/>
- **Venue:** ICML 2026

## Summary

HiPhO's distinctive commitment is human-aligned evaluation: instead of inventing a grading scheme, it adopts the exams' official marking schemes for fine-grained answer- and step-level grading fully aligned with human examiners, then assigns medals by the official thresholds. The exams are the latest available (2024–2025), keeping contamination pressure low, and cover mixed text-only and diagram-based modalities. Across 30 state-of-the-art (M)LLMs: open-source MLLMs mostly remain at or below bronze; open-source LLMs show promising progress with multiple golds; closed-source reasoning MLLMs achieve 6 to 12 gold medals — yet most models remain far from full marks.

## Tasks

13 latest (2024–2025) high-school physics olympiad exams, international and regional, mixing text-only and diagram-based problems; static exam solving.

## Domains

High-school olympiad physics; subfield composition follows the source exams and is not separately enumerated.

## Evaluation

- Official marking schemes applied at answer and step level; medal assignment by official gold/silver/bronze thresholds.
- **Reported.** Of 30 (M)LLMs: open-source MLLMs at or below bronze, open-source LLMs reach multiple golds, closed-source reasoning MLLMs achieve 6–12 golds; most models remain well short of full marks.

## Typical Duration

Exam-style problem solving; not an interactive agent setting.

## Main Contribution

Grades models exactly as human olympiad contestants are graded — official rubrics, official medal lines — making the human comparison direct rather than reconstructed.

## Key Design Ideas

- Official marking schemes remove grading design from the benchmark authors' hands.
- Medal thresholds convert scores into a scale the physics community already understands.
- Using only the latest exams renews contamination control every competition cycle.

## Strengths

- Step-level grading aligned with human examiners rather than binary answer checks.
- The medal framing communicates model capability in human-calibrated terms.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [PHYBench](./phybench.md) — Also olympiad-difficulty physics with a differentiating metric, via original problems rather than official exams.
- [SeePhys](./seephys.md) — Also mixed-modality physics evaluation, spanning school to PhD level.
- [UGPhysics](./ugphysics.md) — Also human-exam-anchored physics evaluation, at undergraduate breadth.
