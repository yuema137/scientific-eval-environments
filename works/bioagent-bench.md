# BioAgent Bench (2026)

> **English** | [简体中文](../zh/works/bioagent-bench.md)

## Overview

BioAgent Bench is an AI-agent evaluation suite for bioinformatics: manually curated end-to-end tasks — RNA-seq, variant calling, metagenomics — that agents must complete as multi-step pipelines producing concrete output artifacts, with robustness probed via controlled perturbations.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.21800>
- **Venue:** ICML 2026

## Summary

Each task hands the agent a task-specific prompt and expects a completed bioinformatics pipeline whose output artifacts are then scored by an LLM-based grader for pipeline progress and outcome validity. Frontier closed- and open-weight models are evaluated across multiple agent harnesses, and robustness is tested with controlled perturbations — corrupted inputs, decoy files, and prompt bloat. The headline finding: frontier agents can complete multi-step bioinformatics pipelines without elaborate custom scaffolding, but correct high-level pipeline construction does not guarantee reliable step-level reasoning.

## Tasks

Manually curated end-to-end bioinformatics pipelines (e.g., RNA-seq, variant calling, metagenomics), completed from task prompts to concrete output artifacts; exact task counts are TODO(reference).

## Domains

Bioinformatics workflows: RNA sequencing, variant calling, and metagenomics.

## Evaluation

- LLM-based grader scoring pipeline progress and outcome validity from output artifacts.
- Robustness suite with controlled perturbations: corrupted inputs, decoy files, prompt bloat.
- **Reported.** Frontier agents complete multi-step pipelines without elaborate scaffolding, but high-level pipeline correctness does not guarantee reliable step-level reasoning.

## Typical Duration

Multi-step pipeline construction and execution per task; budgets are TODO(reference).

## Main Contribution

Separates "can build the right pipeline" from "reasons correctly at each step" in bioinformatics, and shows perturbation robustness is a distinct axis from clean-input success.

## Key Design Ideas

- Grading from output artifacts keeps evaluation harness-agnostic.
- Controlled perturbations (decoys, corruption, bloat) measure robustness rather than assuming it.
- Multi-harness evaluation exposes how much performance is scaffolding-dependent.

## Strengths

- End-to-end realism over standard pipeline families used across genomics labs.
- The pipeline-vs-step-reasoning gap is a diagnostic other suites do not isolate.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [BixBench](./bixbench.md) — Also exploratory bioinformatics agent evaluation, from published notebook analyses.
- [GenoTEX](./genotex.md) — Also pipeline-level genomics evaluation, against expert-curated reference analyses.
- [MDArena](./mdarena.md) — Also containerized, research-derived scientific workflows, in molecular dynamics.
