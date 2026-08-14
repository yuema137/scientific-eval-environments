# MaCBench (2024)

> **English** | [简体中文](../zh/works/macbench.md)

## Overview

MaCBench probes the limitations of multimodal (vision-language) models for chemistry and materials research across three core aspects — data extraction, experimental understanding, and results interpretation — finding near-perfect equipment identification and standardized data extraction but fundamental limits in spatial reasoning, cross-modal synthesis, and multi-step inference.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2411.16955>
- **Code:** <https://github.com/lamalab-org/MaCBench>
- **Dataset:** <https://huggingface.co/datasets/jablonkagroup/MaCBench>
- **Venue:** arXiv preprint (cs.LG, cond-mat.mtrl-sci), 2024

## Summary

MaCBench evaluates whether vision-language models can do the visual work of chemistry and materials research: reading instruments and lab scenes, extracting data from figures and tables, and interpreting experimental results. Models identify equipment and extract standardized data nearly perfectly, yet show fundamental limitations in spatial reasoning, cross-modal information synthesis, and multi-step logical inference — competence at perception, breakdown at integration. The benchmark runs on the ChemBench evaluation pipeline and maintains a public leaderboard.

## Tasks

Multimodal (image + text) chemistry and materials tasks across three aspects: data extraction, experimental understanding, and results interpretation; static VLM evaluation. Task counts are TODO(reference) — not stated in the abstract or repository.

## Domains

Chemistry and materials science — both named explicitly in the paper's title and scope, with the materials side reflected in its cond-mat.mtrl-sci listing.

## Evaluation

- Accuracy over multimodal tasks via the ChemBench pipeline, with per-aspect breakdowns.
- **Reported.** Near-perfect performance on equipment identification and standardized data extraction; fundamental limitations in spatial reasoning, cross-modal information synthesis, and multi-step logical inference.

## Typical Duration

Single-turn multimodal questions; no interactive setting.

## Main Contribution

Locating the vision-language bottleneck for scientific work: current models see lab images well but cannot yet reason across modalities and steps — the part of the workflow that constitutes doing science rather than reading it.

## Key Design Ideas

- The three-aspect split (extract / understand / interpret) orders tasks by integration depth.
- Reusing the ChemBench pipeline keeps scoring consistent with the text-only sibling benchmark.
- Ablation datasets isolate which visual properties drive failures.

## Strengths

- One of the few chemistry/materials evaluations aimed squarely at VLMs rather than text models.
- The perception-vs-integration contrast gives a precise capability boundary.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); task counts are not stated in those sources and remain TODO(reference). No venue is stated in arXiv metadata or the official repository.

## Related Works

- [ChemBench](./chembench.md) — The text-only sibling whose evaluation pipeline MaCBench runs on.
- [ChemX](./chemx.md) — Also chemistry/materials data extraction, at the agentic document-processing level.
- [MolPuzzle](./molpuzzle.md) — Also multimodal chemistry evaluation, on spectral rather than lab imagery.
