# HARDMath (2024)

> **English** | [简体中文](../zh/works/hardmath.md)

## Overview

HARDMath is a benchmark dataset for challenging problems in applied mathematics — the analytical approximation techniques of a graduate asymptotics course — with auto-generated problems whose solutions are validated against numerical ground truths, plus 40 word problems in applied-science contexts; its HARDMath-mini test set holds 366 problems.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.09988>
- **Code:** <https://github.com/sarahmart/HARDMath>
- **Venue:** arXiv preprint (cs.LG, cs.AI), 2024

## Summary

Applied mathematics as practiced is approximation: knowing which asymptotic technique applies, and carrying it through. HARDMath auto-generates such problems at scale and validates every solution against numerical ground truth, sidestepping the annotation bottleneck of expert-written suites while keeping answers checkable. With few-shot chain-of-thought prompting, even leading closed-source models like GPT-4 achieve only 43.8% overall accuracy on HARDMath-mini, and the paper's error analysis maps where approximation reasoning breaks.

## Tasks

Auto-generated applied-mathematics problems requiring analytical approximation techniques, validated against numerical ground truths; HARDMath-mini test set of 366 problems plus 40 applied-science word problems; static problem solving.

## Domains

Applied mathematics: asymptotic methods and analytical approximation techniques at graduate-course level.

## Evaluation

- Accuracy against numerically validated ground-truth solutions, with few-shot chain-of-thought prompting and detailed error analysis.
- **Reported.** GPT-4 reaches only 43.8% overall accuracy with few-shot chain-of-thought.

## Typical Duration

Single-problem derivations; not an interactive setting.

## Main Contribution

Made approximation — not exact solution — the tested mathematical skill, with an auto-generation pipeline whose numerical validation keeps generated problems trustworthy.

## Key Design Ideas

- Auto-generation with numerical validation scales problem supply without sacrificing checkability.
- Asymptotics targets the applied-math reasoning that exact-answer benchmarks never touch.
- Word problems connect the techniques to applied-science contexts.

## Strengths

- A rare benchmark of approximation reasoning, foundational to PDE and physical modeling practice.
- The 43.8% GPT-4 ceiling left clear headroom at release.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. The full (non-mini) dataset size is not stated in the verified sources.

## Related Works

- [TPBench](./tpbench.md) — Also auto-verifiable graduate-to-research evaluation, in theoretical physics.
- [CMPhysBench](./cmphysbench.md) — Also derivation-centric evaluation with tailored grading, in condensed matter physics.
- [PDE-Controller](./pde-controller.md) — Also applied-mathematics reasoning for PDE systems, oriented to control.
