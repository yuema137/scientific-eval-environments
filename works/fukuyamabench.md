# FukuyamaBench (2026)

> **English** | [简体中文](../zh/works/fukuyamabench.md)

## Overview

FukuyamaBench is a difficult benchmark for hierarchical reaction-mechanism reasoning, derived from Fukuyama's Advanced Organic Reaction Mechanism book; it is released by a training-focused paper on mechanistic reasoning, whose fine-tuned Qwen3-30B-A3B reaches 8.3% exact pathway match on Set A, surpassing the specialized FlowER model (5.1%).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.12771>
- **Venue:** arXiv preprint, 2026

## Summary

The paper "Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models" builds a large-scale reasoning dataset of reaction mechanisms for training, then establishes FukuyamaBench to rigorously evaluate hierarchical mechanism reasoning — deducing full elementary-reaction pathways, not just products. The headline evaluation result: mechanism-aware fine-tuning brings Qwen3-30B-A3B to 8.3% exact pathway match on FukuyamaBench Set A versus 5.1% for the specialized FlowER model — numbers that mostly demonstrate how hard the benchmark is.

## Tasks

Stepwise deduction of elementary-reaction mechanism pathways for organic reactions, sourced from a graduate-level mechanism textbook; static reasoning tasks. Set sizes are TODO(reference) — not stated in the abstract.

## Domains

Chemistry — organic reaction mechanisms: elementary-step pathway reasoning underlying product prediction and retrosynthesis.

## Evaluation

- Exact pathway match on the deduced mechanism.
- **Reported.** Fine-tuned Qwen3-30B-A3B: 8.3% exact pathway match on Set A; specialized FlowER model: 5.1%.

## Typical Duration

Single-episode multi-step mechanism derivations.

## Main Contribution

An evaluation target for mechanism-level (not product-level) chemical reasoning, hard enough that the best reported system solves fewer than one pathway in ten exactly.

## Key Design Ideas

- Sourcing from an advanced textbook pins difficulty to expert training material rather than scraped reactions.
- Exact pathway match demands the full mechanism, closing the shortcut of guessing products.
- Hierarchical structure separates single-step from full-pathway competence.

## Strengths

- Probes a layer of chemical understanding — mechanisms — that product-prediction benchmarks bypass.
- Single-digit SOTA scores leave clear, measurable headroom.

## Limitations

- Repository note: the paper's primary contribution is a training dataset and mechanism-aware fine-tuning; FukuyamaBench is its secondary, evaluation-side contribution, and this card covers only the benchmark. The paper is not titled "FukuyamaBench".
- Repository note: card compiled from the arXiv abstract and metadata (August 2026); no code or dataset release is verifiable from the paper's arXiv page.

## Related Works

- [ChemCoTBench](./chemcotbench.md) — Also step-structured reaction reasoning, at the level of modular molecular operations.
- [ChemCensor / CREED](./chemcensor.md) — Also rethinks reaction-direction evaluation, on the retrosynthesis side.
- [QCBench](./qcbench.md) — Also shortcut-resistant chemistry problems demanding explicit multi-step work.
