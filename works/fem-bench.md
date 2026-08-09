# FEM-Bench (2025)

> **English** | [简体中文](../zh/works/fem-bench.md)

## Overview

FEM-Bench is a structured scientific-reasoning benchmark for code-generating LLMs in computational mechanics: FEM-Bench 2025 comprises introductory but nontrivial tasks aligned with a first graduate course — 33 tasks in the function-writing track — with objective verification and paired unit-test-writing evaluation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.20732>
- **Venue:** arXiv preprint (cs.LG, cs.AI, cs.SE), 2025

## Summary

FEM-Bench treats the finite element method as a probe of whether models can connect physical reasoning — forces, deformation, constraints — to correct numerical code. Models are evaluated on two tracks over five attempts each: writing FEM and related functions, and writing unit tests, both objectively verified. The best function-writing model, Gemini 3 Pro, completes 30/33 tasks at least once and 26/33 all five times; the best test-writing model, GPT-5, reaches a 73.8% Average Joint Success Rate — capable but short of the reliability engineering practice requires.

## Tasks

Graduate-course-aligned computational-mechanics coding tasks (33 in the function-writing track), plus a unit-test-writing track; five attempts per model-task pair.

## Domains

Computational mechanics and the finite element method: forces, deformation, and constraints rendered as code.

## Evaluation

- Objective verification of generated functions and unit tests; per-task success over five attempts; **Average Joint Success Rate** for test writing.
- **Reported.** Gemini 3 Pro completes 30/33 function tasks at least once and 26/33 all five times; GPT-5 reaches 73.8% Average Joint Success Rate on test writing.

## Typical Duration

Single-function and single-test generation; not an interactive setting.

## Main Contribution

Grounds FEM code generation at the granularity where curricula ground human engineers — and adds test-writing as a scored capability, since verification code matters as much as solver code.

## Key Design Ideas

- Course alignment makes the difficulty scale legible to the mechanics community.
- Five-attempt evaluation separates one-off success from reliability.
- The unit-test track measures whether models can verify, not just produce, numerical code.

## Strengths

- Clean objective verification at a well-calibrated difficulty level.
- The consistency gap (30/33 once vs. 26/33 always) quantifies flakiness.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — Also FEM-library code generation, at research scale with staged accuracy/efficiency gates.
- [FEABench](./feabench.md) — Also finite-element evaluation, through operating professional software rather than writing functions.
- [SciCode](./scicode.md) — Also scientist-aligned research-code generation with gold tests, across 16 subfields.
