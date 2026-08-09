# GenoTEX (2024)

> **English** | [简体中文](../zh/works/genotex.md)

## Overview

GenoTEX is an LLM-agent benchmark for automated gene expression data analysis: agents carry out dataset selection, preprocessing, and statistical analysis for gene-trait association problems in a pipeline that follows computational genomics standards, evaluated against expert-curated annotations from bioinformaticians.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.15341>
- **Code:** <https://github.com/Liu-Hy/GenoTEX>
- **Venue:** arXiv preprint (cs.LG, cs.AI, q-bio.GN); MLCB 2025 oral per the official repository

## Summary

GenoTEX packages a wide range of gene-trait association problems with reference analysis code and results curated by bioinformaticians. Per the official repository, it comprises 1,384 gene-trait association analysis problems (132 unconditional, 1,252 conditional) over 911 datasets. The paper also presents GenoAgent, a team of LLM-based agents adopting a multi-step programming workflow with flexible self-correction, as a baseline; experiments demonstrate the promise of LLM-based methods while error analysis highlights the remaining challenges.

## Tasks

Gene-trait association analysis problems over gene expression datasets — dataset selection, preprocessing, and statistical analysis following computational genomics standards; 1,384 problems over 911 datasets per the official repository.

## Domains

Computational genomics and bioinformatics: gene expression analysis and gene-trait association.

## Evaluation

- Agent outputs compared against expert-curated annotations from bioinformaticians, with reference analysis code and results provided.
- **Reported.** Experiments demonstrate the potential of LLM-based methods; error analysis highlights the challenges. Specific figures are TODO(reference).

## Typical Duration

Multi-step code-writing analysis pipelines with self-correction; budgets are TODO(reference).

## Main Contribution

Anchors genomics-agent evaluation to what practicing bioinformaticians actually produce — expert-curated reference pipelines and results — rather than synthetic labels.

## Key Design Ideas

- The evaluation unit is a full analysis pipeline (selection → preprocessing → statistics), not a single question.
- Expert reference code makes agent analyses comparable step by step, not only at the answer.
- Conditional and unconditional problem variants separate straightforward association from context-dependent analysis.

## Strengths

- Expert-curated ground truth at unusual scale for genomics analysis (1,384 problems, 911 datasets per the repository).
- Follows computational genomics standards, so scores reflect field practice.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: GenoAgent, the paper's baseline multi-agent method, is agent implementation and out of this repository's scope; the card documents the benchmark.

## Related Works

- [BixBench](./bixbench.md) — Also evaluates agents on real computational-biology analysis, via exploratory Jupyter scenarios rather than curated pipelines.
- [GeneBench-Pro](./genebench-pro.md) — Also genomics analysis evaluation, on constructively simulated data with fully known causal structure.
- [ScienceAgentBench](./scienceagentbench.md) — Also expert-validated data-analysis tasks unified to executable programs, across disciplines.
