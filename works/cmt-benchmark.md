# CMT-Benchmark (2025)

> **English** | [简体中文](../zh/works/cmt-benchmark.md)

## Overview

CMT-Benchmark is a benchmark of 50 expert-researcher-level problems in condensed matter theory, built by expert researchers and machine-graded against expert-supplied ground truth, including symbolic handling of non-commuting operators via normal ordering.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.05228>
- **Dataset:** <https://huggingface.co/datasets/JVRoggeveen/cmt_benchmark>
- **Venue:** ICLR 2026

## Summary

CMT-Benchmark spans analytical and computational condensed-matter-theory approaches — Hartree-Fock, exact diagonalization, quantum and variational Monte Carlo, DMRG, and statistical mechanics — over quantum many-body systems and classical statistical mechanics. Solutions are checked programmatically against expert ground truth with grading that generalizes across tasks, including normal-ordered symbolic comparison of non-commuting operators.

## Tasks

50 problems covering condensed matter theory, spanning Hartree-Fock, exact diagonalization, quantum/variational Monte Carlo, DMRG, and statistical mechanics.

## Domains

Condensed matter theory: quantum many-body systems, classical statistical mechanics, computational physics methods.

## Evaluation

- Programmatic checking against expert-supplied ground truth, with machine grading that generalizes across tasks — including symbolic handling of non-commuting operators via normal ordering.
- **Reported.** The best model, GPT-5, solves 30% of problems; the average across 17 models is 11.4±2.1%; 18 problems are solved by none of the 17 models and 26 by at most one.

## Typical Duration

Single-problem theoretical and computational derivations; not an interactive agent setting.

## Main Contribution

Expert-researcher-level condensed matter theory rendered machine-gradable, demonstrating that most problems defeat every evaluated frontier model.

## Key Design Ideas

- Problems are authored by expert researchers at the level of their own work, not adapted from coursework.
- Normal-ordering-based symbolic grading solves the non-commuting-operator comparison problem that generic checkers cannot handle.
- Unsolved-problem counts (18 by none, 26 by at most one) are reported as first-class results.

## Strengths

- Machine-gradable at a difficulty level usually requiring expert human grading.
- Extreme headroom, documented per problem rather than only in averages.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CMPhysBench](./cmphysbench.md) — Also condensed-matter evaluation, at graduate level with 520+ problems and partial-credit scoring.
- [PRBench](./prbench.md) — Also expert-anchored physics evaluation, via reproduction of published papers.
- [Hard2Verify](./hard2verify.md) — Also uses expert-produced ground truth at frontier difficulty, for proof-step verification in mathematics.
