# ChemCensor / CREED (2026)

> **English** | [简体中文](../zh/works/chemcensor.md)

## Overview

ChemCensor is an evaluation methodology for single-step retrosynthesis that replaces exact-match Top-K against a single ground truth with a chemical-plausibility metric; the same validator generates CREED, a dataset of millions of validated reaction records for LLM training.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.03554>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

Published as "When Single Answer Is Not Enough: Rethinking Single-Step Retrosynthesis Benchmarks for LLMs", the work observes that retrosynthesis admits many valid precursor sets, so Top-K accuracy against one recorded answer mismeasures the task. It contributes a benchmarking framework that evaluates general-purpose and chemistry-specialized LLMs with ChemCensor, a novel metric for chemical plausibility, and CREED, millions of ChemCensor-validated reaction records used to train a model that improves over LLM baselines under the framework.

## Tasks

Single-step retrosynthesis: given a target molecule, propose plausible precursor sets; static prediction evaluated for plausibility rather than exact match. Evaluation-set sizes are TODO(reference) — not stated in the abstract.

## Domains

Chemistry — synthesis planning and drug discovery: single-step retrosynthesis evaluation.

## Evaluation

- ChemCensor chemical-plausibility scoring, emphasizing plausibility over exact match to a single recorded ground truth.
- **Reported.** No headline numbers in the abstract; a CREED-trained model improves over LLM baselines under the benchmark.

## Typical Duration

Single-turn predictions; no interactive setting.

## Main Contribution

Diagnosing and fixing a metric artifact: when a task is many-to-one, exact-match Top-K punishes chemically valid answers, and a plausibility metric changes both the rankings and what training optimizes for.

## Key Design Ideas

- The evaluation metric doubles as a data validator — the same plausibility check that scores models filters training records at scale.
- Plausibility scoring accepts the full space of valid precursors instead of the one that happened to be recorded.
- Pairing metric and dataset closes the loop: better evaluation directly yields better training signal.

## Strengths

- Addresses a well-known distortion in retrosynthesis leaderboards at the evaluation-design level.
- The millions-scale validated dataset demonstrates the metric works as an automated filter.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond the abstract await full-paper validation. No code or dataset release is verifiable from the paper's arXiv page, and no venue is stated in arXiv metadata.

## Related Works

- [Speak-to-Structure (TOMG-Bench)](./tomg-bench.md) — Also one-to-many evaluation replacing single-reference matching, for molecule generation.
- [FukuyamaBench](./fukuyamabench.md) — Also reaction-direction reasoning evaluation, at mechanism level.
- [FormalRewardBench](./formalrewardbench.md) — Also studies whether an evaluation signal accepts valid answers and rejects invalid ones.
