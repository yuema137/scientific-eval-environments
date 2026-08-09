# MolLangBench (2025)

> **English** | [简体中文](../zh/works/mollangbench.md)

## Overview

MolLangBench benchmarks language-prompted molecular structure recognition, editing, and generation across linear strings, molecular images, and molecular graphs: recognition tasks are auto-constructed with cheminformatics tools, editing and generation tasks are expert-annotated, and the strongest model (GPT-5) still drops to 43.0% on generation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.15054>
- **Code:** <https://github.com/TheLuoFengLab/MolLangBench>
- **Dataset:** <https://huggingface.co/datasets/ChemFM/MolLangBench>
- **Venue:** ICLR 2026

## Summary

MolLangBench covers the full read–modify–write loop on molecular structure through language: recognizing structural features, editing molecules per instruction, and generating molecules to specification, with inputs spanning SMILES-style strings, images, and graphs. Recognition tasks come from cheminformatics construction (leak-resistant and automatically checkable); editing and generation are expert-annotated. GPT-5 achieves 86.2% on recognition and 85.5% on editing but only 43.0% on generation.

## Tasks

Three task families — structure recognition, editing, and generation — over linear strings, molecular images, and molecular graphs; static single-turn tasks. Instance counts are TODO(reference) — not stated in the abstract.

## Domains

Chemistry — cheminformatics: molecular structure recognition and manipulation through natural-language interfaces.

## Evaluation

- Per-task accuracy; recognition answers are verifiable by construction via cheminformatics tooling.
- **Reported.** GPT-5: 86.2% recognition, 85.5% editing, 43.0% generation.

## Typical Duration

Single-turn tasks; no interactive setting.

## Main Contribution

A recognition→editing→generation gradient on one benchmark, showing frontier models read and locally modify structures far better than they construct them.

## Key Design Ideas

- Auto-constructed recognition tasks give a leak-resistant, judge-free foundation layer.
- The same molecules appear as strings, images, and graphs, isolating representation effects.
- Expert annotation is reserved for the tasks (editing, generation) that genuinely need it.

## Strengths

- The recognition/generation gap (86% vs 43%) cleanly localizes the frontier weakness.
- ICLR 2026 acceptance verified on the arXiv page itself; full public code and data.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); task counts are not stated in those sources and remain TODO(reference).

## Related Works

- [MolecularIQ](./moleculariq.md) — Also symbolically verifiable structure reasoning, restricted entirely to graph-checkable tasks.
- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — Also language-driven molecule editing and generation, evaluated one-to-many.
- [MolPuzzle](./molpuzzle.md) — Also multimodal structure tasks, oriented to spectrum-based elucidation.
