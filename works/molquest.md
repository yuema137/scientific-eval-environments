# MolQuest (2026)

> **English** | [简体中文](../zh/works/molquest.md)

## Overview

MolQuest recasts chemical structure elucidation as an agentic task: a multi-turn interactive setting in which models must proactively plan experimental steps, integrate heterogeneous spectral sources such as NMR and MS, and iteratively refine structural hypotheses — state-of-the-art models reach only about 50% accuracy.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.25253>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

Where staged benchmarks hand the model its spectra, MolQuest makes the model earn them: elucidation is formalized as abductive reasoning in a multi-turn loop of choosing experiments, reading the resulting spectra, and revising the structural hypothesis. Under this agent-based evaluation framework, even state-of-the-art models achieve only approximately 50% accuracy, and most models remain below 30%.

## Tasks

Multi-turn interactive structure-elucidation episodes: plan experimental steps, integrate NMR/MS and other spectral sources, iteratively refine hypotheses. Instance counts are TODO(reference) — not stated in the abstract.

## Domains

Chemistry — analytical chemistry: spectrum-driven structure elucidation as sequential experimental reasoning.

## Evaluation

- Accuracy of the final elucidated structure under the agentic multi-turn protocol.
- **Reported.** SOTA models ≈50% accuracy; most other models below the 30% threshold.

## Typical Duration

Multi-turn interactive episodes with model-initiated experimental steps.

## Main Contribution

Moving elucidation evaluation from "interpret given spectra" to "decide which spectra to acquire" — testing the abductive, experiment-planning half of the skill that static benchmarks omit.

## Key Design Ideas

- Experiment selection is part of the measured behavior, not fixed by the benchmark.
- Iterative hypothesis refinement rewards models that use evidence incrementally.
- Abductive framing: the target is the best structure explaining the accumulated evidence.

## Strengths

- Directly complements static elucidation benchmarks by adding the interactive planning dimension.
- The 50%-ceiling finding indicates substantial headroom even for frontier models.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond the abstract await full-paper validation. No code or project release is verifiable from the paper's arXiv page.

## Related Works

- [MolPuzzle](./molpuzzle.md) — The static, staged counterpart: same spectra-to-structure problem without interaction.
- [SMDD-Bench](./smdd-bench.md) — Also multi-turn molecular problem-solving under constrained information access.
- [Gravity-Bench-v1](./gravity-bench.md) — Also evaluates choosing observations/experiments as part of scientific inference.
