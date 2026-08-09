# MolecularIQ (2026)

> **English** | [简体中文](../zh/works/moleculariq.md)

## Overview

MolecularIQ is a molecular structure reasoning benchmark restricted exclusively to symbolically verifiable tasks: every answer can be checked against the molecular graph itself, eliminating the literature labels, surrogate labels, and multiple-choice formats that let leakage and bias into most chemistry benchmarks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.15279>
- **Code:** <https://github.com/ml-jku/moleculariq>
- **Leaderboard:** <https://huggingface.co/spaces/ml-jku/molecularIQ_leaderboard>
- **Venue:** ICLR 2026 (per the official repository; arXiv metadata carries no venue)

## Summary

MolecularIQ's premise is that a molecule's properties are determined by the composition and structure encoded in its molecular graph, so reasoning about molecules requires actually parsing that graph. Its tasks are chosen so correctness is symbolically verifiable — no literature or surrogate labels that risk leakage, no multiple choice. Fine-grained evaluation localizes model failures to specific tasks and molecular structures, yielding capability patterns ("fingerprints") for current chemistry LLMs.

## Tasks

Symbolically verifiable molecular-graph reasoning tasks; static evaluation. Task and instance counts are TODO(reference) — not stated in the abstract or repository README.

## Domains

Chemistry — molecular structure and graph-level reasoning, the substrate beneath property and reaction prediction.

## Evaluation

- Symbolic verification against the molecular graph; fine-grained breakdowns localize failures to specific tasks and structures.
- **Reported.** No headline numbers in the abstract; a public leaderboard is maintained.

## Typical Duration

Single-turn tasks; no interactive setting.

## Main Contribution

A leakage-resistant measurement of whether chemistry LLMs can genuinely parse molecular structure, with verification that needs no labels beyond the molecule itself.

## Key Design Ideas

- Symbolic verifiability as an admission criterion for tasks, not an afterthought.
- Failure localization to structure types makes the benchmark diagnostic rather than just comparative.
- Capability fingerprints replace single-score rankings.

## Strengths

- Immune by construction to label leakage and annotation bias.
- Diagnostic granularity that guides model development, not just selection.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); scale numbers are not stated in those sources and remain TODO(reference).

## Related Works

- [MolLangBench](./mollangbench.md) — Also cheminformatics-verified structure tasks, extended to editing and generation.
- [ChemIQ](./chemiq.md) — Also judge-free chemistry evaluation with canonical-structure matching.
- [FGBench](./fgbench.md) — Also structure-grounded property reasoning, at functional-group granularity.
