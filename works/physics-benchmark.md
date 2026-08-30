# PHYSICS (2025)

> **English** | [简体中文](../zh/works/physics-benchmark.md)

> **First appeared:** 2025-03-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2503.21821)

## Overview

PHYSICS is a comprehensive benchmark for university-level physics problem solving: 1,297 expert-annotated problems covering six core areas — classical mechanics, quantum mechanics, thermodynamics and statistical mechanics, electromagnetism, atomic physics, and optics — with a robust automated evaluation system.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.21821>
- **Venue:** Findings of ACL 2025

## Summary

Each PHYSICS problem requires advanced physics knowledge and mathematical reasoning, and the benchmark's automated evaluation system provides precise, reliable validation of answers. Evaluation of leading foundation models reveals substantial limitations — the most advanced model tested, o3-mini, achieves only 59.9% accuracy. The paper accompanies the scores with comprehensive error analysis, exploration of diverse prompting strategies, and RAG-based knowledge augmentation to identify where improvement must come from.

## Tasks

1,297 expert-annotated university-level problems across six core areas of physics; static problem solving.

## Domains

University-level physics: classical mechanics, quantum mechanics, thermodynamics and statistical mechanics, electromagnetism, atomic physics, and optics.

## Evaluation

- Robust automated evaluation system for precise and reliable answer validation.
- **Reported.** The most advanced model tested, o3-mini, achieves only 59.9% accuracy.

## Typical Duration

Single-problem solving; not an interactive agent setting.

## Main Contribution

University-breadth physics evaluation with reliable automated validation, plus a diagnosis — via error analysis, prompting variations, and RAG augmentation — of where physics problem solving actually fails.

## Key Design Ideas

- Six core areas keep coverage representative of a physics curriculum rather than one subfield.
- Automated validation is engineered for reliability, not delegated to a generic judge.
- Failure analysis and knowledge augmentation are part of the contribution, not an afterthought.

## Strengths

- Expert annotation at four-digit scale across the core undergraduate curriculum.
- The sub-60% ceiling for a frontier reasoning model documents clear headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [UGPhysics](./ugphysics.md) — Also undergraduate-breadth physics with an automated judgment pipeline, bilingual and larger-scale.
- [PhysGym](./physgym.md) — Also physics evaluation, moved into interactive discovery rather than static problems.
- [CMPhysBench](./cmphysbench.md) — Also curriculum-anchored physics problems, at graduate level in one subfield with partial credit.
