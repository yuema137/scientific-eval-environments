# onepot-Bench 0 (2026)

> **English** | [简体中文](../zh/works/onepot-bench.md)

## Overview

onepot-Bench 0 is a proprietary, lab-aware chemistry benchmark suite in three parts: ChemAbacus (tool-free cheminformatics literacy and numerical reasoning), SynthRefusal (safety and refusal behavior across benign, controlled, and designer-drug targets), and SynthBench (reaction-outcome prediction and catalyst selection on private experimental data generated in the authors' laboratory).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Modeling & Prediction](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.02595>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

The suite's motivating claim is that public chemistry evaluations may already sit inside model training corpora, so onepot-Bench 0 anchors its hardest component to data that cannot have leaked: experiments run in the authors' own lab. ChemAbacus probes what a model can compute about molecules unaided; SynthRefusal characterizes where models draw safety lines across a spectrum from benign to designer-drug synthesis targets; SynthBench asks for reaction outcomes and catalyst selections that only the private experimental record can confirm.

## Tasks

Three complementary evaluations — cheminformatics/numerical questions (tool-free), refusal probes across target categories, and reaction-outcome/catalyst-selection predictions against private lab data; static prediction, not interactive. Task counts are TODO(reference) — not stated in the abstract.

## Domains

Chemistry — synthetic chemistry and cheminformatics, with catalyst selection and wet-lab-generated ground truth.

## Evaluation

- Per-suite evaluation: literacy/numerical scoring (ChemAbacus), refusal-behavior characterization (SynthRefusal), and prediction against private experimental results (SynthBench).
- **Reported.** No headline numbers in the abstract.

## Typical Duration

Single-turn questions and predictions across the three sub-suites.

## Main Contribution

A leakage-proof-by-construction evaluation anchor: reaction outcomes measured in the authors' lab cannot appear in any training corpus, whatever a model's cutoff.

## Key Design Ideas

- Private experimental generation attacks contamination at the source rather than by filtering.
- Bundling capability (ChemAbacus) with safety (SynthRefusal) evaluates the same models on both axes.
- "Lab-aware" framing: ground truth comes from bench chemistry, not databases.

## Strengths

- The private-data design gives contamination guarantees no public benchmark can match.
- Refusal characterization across a graded target spectrum is rare in chemistry evaluation.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond the abstract await full-paper validation. The suite is explicitly proprietary — no public code, data, or task counts — which limits independent reproduction and comparison.

## Related Works

- [ChemIQ](./chemiq.md) — Also tool-free cheminformatics and numerical reasoning, as a public benchmark.
- [LABBench2](./labbench2.md) — Also laboratory-grounded evaluation of models against experimental reality.
- [BioXArena](./bioxarena.md) — Also uses private/hidden test data to close the leakage channel.
