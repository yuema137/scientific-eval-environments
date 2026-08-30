# LAB-Bench (2024)

> **English** | [简体中文](../zh/works/lab-bench.md)

> **First appeared:** 2024-07-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2407.10362)

## Overview

LAB-Bench (Language Agent Biology Benchmark) measures capabilities of language models for biology research: over 2,400 multiple-choice questions across eight categories — literature recall and reasoning (LitQA2), figure and table interpretation (FigQA, TableQA), database access (DbQA, SuppQA), protocol planning (ProtocolQA), and DNA/protein sequence manipulation (SeqQA, CloningScenarios) — with human expert biologist baselines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)
- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.10362>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/lab-bench>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

LAB-Bench targets the practical capabilities biology research actually requires rather than textbook knowledge: recall and reasoning over literature, interpretation of figures, access and navigation of databases, and comprehension and manipulation of DNA and protein sequences. Its eight subtasks include the widely cited CloningScenarios (multi-step molecular-cloning workflows) and are scored against human expert biology researchers; roughly 80% of the benchmark (1,967 questions) is publicly released.

## Tasks

2,400+ multiple-choice questions across eight categories / 30 subtasks: LitQA2, DbQA, SuppQA, FigQA, TableQA, ProtocolQA, SeqQA, and CloningScenarios; static, tool-use optional.

## Domains

Biology research practice broadly: molecular biology and cloning, DNA and protein sequences, protocols, literature and databases.

## Evaluation

- Multiple-choice scoring against answer keys, with human expert biology researchers as the reference baseline.
- **Reported.** Comparative model-vs-expert figures are TODO(reference); the abstract states no numeric results.

## Typical Duration

Single-question answering, optionally with tools; not an interactive environment.

## Main Contribution

Shifted biology evaluation from exam knowledge to research practice — figures, databases, sequences, protocols, cloning — and became the de-facto reference suite for biology-capable language systems.

## Key Design Ideas

- Categories mirror the daily verbs of research (read, look up, interpret, plan, manipulate sequences), not curriculum topics.
- CloningScenarios chains sequence-level steps so multi-step wet-lab reasoning is probed in MCQ form.
- A held-back private split protects against contamination.

## Strengths

- Human-expert baselines across all categories.
- Broad adoption makes its scores a common reference point across the field.

## Limitations

- Repository note: card compiled from the arXiv abstract and official dataset materials (August 2026); details beyond those sources await full-paper validation. The arXiv Comments field records submission to NeurIPS 2024 Datasets and Benchmarks as "in review"; no acceptance is verifiable from those sources.

## Related Works

- [LABBench2](./labbench2.md) — The successor suite with more realistic contexts and a substantial difficulty jump.
- [BioProBench](./bioprobench.md) — Also protocol-centric evaluation, at corpus scale with generation and repair tasks.
- [Aviary](./aviary.md) — Also FutureHouse biology evaluation, as interactive environments (SeqQA and cloning appear in both lineages).
