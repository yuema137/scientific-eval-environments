# MolPuzzle (2024)

> **English** | [简体中文](../zh/works/molpuzzle.md)

## Overview

MolPuzzle is a multimodal benchmark for molecular structure elucidation posed as a puzzle in three stages — molecule understanding, spectrum interpretation, and molecule construction — over 200 elucidation instances with 23,678 collected examples; GPT-4o exactly matches the ground-truth structure only 1.4% of the time, far below humans.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper (OpenReview):** <https://openreview.net/forum?id=t1mAXb4Cop>
- **Project:** <https://kehanguo2.github.io/Molpuzzle.io/>
- **Code:** <https://github.com/KehanGuo2/MolPuzzle>
- **Dataset:** <https://huggingface.co/datasets/kguo2/MolPuzzle_data>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks Track, 2024 (per the official project page; no arXiv listing exists)

## Summary

Published as "Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation", MolPuzzle decomposes elucidation the way chemists work it: Stage 1 derives saturation degree, aromatic rings, and functional groups from the formula; Stage 2 interprets IR, mass, ¹H-NMR, and ¹³C-NMR spectra; Stage 3 assembles the molecule from the gathered constraints. Across a broad slate of LLMs and vision-language models, GPT-4o performs best yet still exactly matches ground truth on only 1.4% of final structures, well below the human baseline.

## Tasks

200 molecular structure elucidation instances decomposed into three stages, with 23,678 data examples collected across the stages; multimodal (spectra as images) but static QA-style — not interactive.

## Domains

Chemistry — analytical and organic chemistry: structure elucidation from IR, MS, ¹H-NMR, and ¹³C-NMR spectroscopy.

## Evaluation

- Exact-match accuracy on the final structure plus per-stage evaluation; human baseline across all stages.
- **Reported.** GPT-4o outperforms other models but reaches only 1.4% exact match on ground-truth structures, underperforming humans.

## Typical Duration

Staged single-episode puzzles; each stage is a bounded QA step feeding the next.

## Main Contribution

Turning the classic spectra-to-structure exam problem into a staged multimodal benchmark that localizes where elucidation fails — understanding, interpretation, or construction.

## Key Design Ideas

- The three-stage decomposition mirrors human workflow, so stage scores are diagnostic.
- Multimodal spectra force genuine cross-modal chemistry, not text pattern-matching.
- Exact structure match leaves no partial-credit ambiguity at the final stage.

## Strengths

- The 1.4%-vs-human gap is among the starkest documented deficits for frontier models in chemistry.
- Full public stack: project page, code, and dataset.

## Limitations

- Repository note: card compiled from the official project page (August 2026); the paper has no arXiv listing and OpenReview metadata was unreachable during validation, so per-stage details and any spotlight designation await verification.

## Related Works

- [MolQuest](./molquest.md) — Also structure elucidation from spectra, recast as an interactive multi-turn agentic task.
- [ChemIQ](./chemiq.md) — Also NMR-based elucidation, in tool-free short-answer form.
- [MolLangBench](./mollangbench.md) — Also structure recognition and construction tasks, prompted through language.
