# Speak-to-Structure / TOMG-Bench (2024)

> **English** | [简体中文](../zh/works/tomg-bench.md)

## Overview

Speak-to-Structure (S²-Bench, introduced as TOMG-Bench) evaluates LLMs on open-domain natural-language-driven molecule generation: three tasks — molecule editing (MolEdit), molecule optimization (MolOpt), and customized generation (MolCustom) — where instructions admit many valid molecules and answers are checked for validity against the instruction rather than one reference.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.14642>
- **Code:** <https://github.com/phenixace/S2-TOMG-Bench>
- **Dataset:** <https://huggingface.co/datasets/phenixace/S2-TOMG-Bench>
- **Venue:** KDD 2026

## Summary

Most text-to-molecule evaluation is one-to-one: an instruction with a single reference answer. Speak-to-Structure makes it one-to-many — open-ended instructions where any molecule satisfying the request counts — across editing, optimization, and customized generation. The first version (TOMG-Bench) organized each task into three subtasks of 5,000 test samples each; the current version reports a comprehensive evaluation of 31 LLMs. The paper pairs the benchmark with OpenMolIns, a large-scale instruction-tuning dataset that lifts Llama3.1-8B past GPT-4o and Claude-3.5 on the benchmark.

## Tasks

Three open-domain molecule-generation task families — MolEdit, MolOpt, MolCustom — evaluated one-to-many against instruction satisfaction; 5,000 test samples per subtask in the original release (nine subtasks). Static single-turn generation.

## Domains

Chemistry — natural-language-driven molecule design: editing, property optimization, and de novo customized generation.

## Evaluation

- Instruction-satisfaction checking over open-ended generations (one-to-many), rather than string match against a single reference.
- **Reported.** 31 LLMs evaluated; OpenMolIns instruction tuning enables Llama3.1-8B to surpass GPT-4o and Claude-3.5 on S²-Bench.

## Typical Duration

Single-turn generation per instruction; no interactive setting.

## Main Contribution

Making one-to-many evaluation the default for text-driven molecule generation — measuring whether models satisfy chemical constraints rather than reproduce a memorized reference.

## Key Design Ideas

- Open-domain instructions remove the single-reference bottleneck that penalizes valid novel molecules.
- The edit/optimize/generate split separates local structure manipulation from global design.
- The paired OpenMolIns dataset demonstrates the benchmark's headroom is trainable.

## Strengths

- 31-model coverage plus a public leaderboard-scale dataset.
- The retitled camera-ready (KDD 2026) confirms sustained maintenance from v1 (2024) onward.

## Limitations

- Repository note: card compiled from the arXiv abstract (v1 and v4) and official repositories (August 2026). The paper was retitled between versions — TOMG-Bench (v1, 2024) to Speak-to-Structure/S²-Bench (v4, 2026); the 5,000-per-subtask figure is stated in the v1 abstract.

## Related Works

- [MolLangBench](./mollangbench.md) — Also language-prompted molecule manipulation, with recognition tasks verified by cheminformatics tools.
- [ChemCoTBench](./chemcotbench.md) — Also molecule editing and optimization, evaluated at the reasoning-step level.
- [ChemCensor / CREED](./chemcensor.md) — Also replaces single-reference exact match with a many-valid-answers evaluation, in retrosynthesis.
