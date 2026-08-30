# SciConvBench (2026)

> **English** | [简体中文](../zh/works/sciconvbench.md)

> **First appeared:** 2026-05-18 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.18630)

## Overview

SciConvBench benchmarks LLMs on multi-turn clarification for task formulation in computational science: given an ill-posed simulation request in fluid mechanics, solid mechanics, materials science, or PDEs, the model must elicit missing information (disambiguation) and detect internally contradictory requirements (inconsistency resolution) through dialogue before any computation happens.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.18630>
- **Code:** <https://github.com/csml-rpi/SciConvBench>
- **Venue:** arXiv preprint (cs.AI, physics.comp-ph), 2026

## Summary

Most simulation failures begin before the first solve: the request itself is underspecified or self-contradictory. SciConvBench evaluates the conversational competence that precedes computation, using a structured task ontology and a rubric-based framework scoring three dimensions — clarification behavior, conversational grounding, and final-specification fidelity — with metrics including grounded conversation rate and clarification recall/precision (per the official repository). Even the best model resolves only 52.7% of the disambiguation cases in fluid mechanics.

## Tasks

Multi-turn clarification dialogues over ill-posed computational-science requests across four domains (fluid mechanics, solid mechanics, materials science, PDEs), in disambiguation and inconsistency-resolution variants; task counts are TODO(reference).

## Domains

Computational-science task formulation across fluid mechanics, solid mechanics, materials science, and PDEs.

## Evaluation

- Rubric-based framework over a structured task ontology: clarification behavior, conversational grounding, and final-specification fidelity; grounded conversation rate and clarification recall/precision per the official repository.
- **Reported.** The best model resolves only 52.7% of disambiguation cases in fluid mechanics.

## Typical Duration

Multi-turn clarification dialogues per task.

## Main Contribution

Moves the evaluation boundary upstream of the solver: whether a model can turn an ill-posed scientific request into a well-posed specification is measured as its own capability.

## Key Design Ideas

- Ill-posedness is constructed deliberately (missing versus contradictory information), so the required dialogue behavior is known.
- Specification fidelity is scored at the end, tying conversation quality to a checkable artifact.
- A non-scientific control set separates domain competence from generic dialogue skill (per the official repository).

## Strengths

- Targets the failure stage most simulation benchmarks assume away.
- The 52.7% fluid-mechanics ceiling shows clarification is far from solved.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [SWE-Interact](./swe-interact.md) — Also measures progressive-requirement dialogue, in software engineering.
- [SimBench](./simbench.md) — Also multi-turn simulation setup, evaluated at the generated-artifact level.
- [CFDLLMBench](./cfdllmbench.md) — The downstream counterpart: evaluating the solves that follow well-posed CFD specifications.
