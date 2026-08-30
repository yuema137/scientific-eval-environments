# ChemX (2025)

> **English** | [简体中文](../zh/works/chemx.md)

> **First appeared:** 2025-10-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2510.00795)

## Overview

ChemX benchmarks agentic systems on automated scientific information extraction in chemistry: 10 manually curated, domain-expert-validated datasets on nanomaterials and small molecules, against which document-extraction agents such as ChatGPT Agent and chemistry-specific pipelines are compared.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.00795>
- **Dataset:** <https://huggingface.co/ai-chem>
- **Venue:** AI4Mat Workshop, NeurIPS 2025

## Summary

ChemX targets the extraction bottleneck of chemical data curation: turning papers — with their domain terminology, complex tables, schematics, and context-dependent ambiguity — into structured records. Ten expert-validated datasets (including cytotoxicity, nanozymes, co-crystals, and oxazolidinones collections) provide the ground truth. The paper benchmarks agentic extractors including ChatGPT Agent and chemical-specific data-extraction agents, alongside a single-agent approach with precise control over document preprocessing and static GPT-5-class baselines, finding persistent challenges across all of them.

## Tasks

Structured chemical-data extraction from scientific documents against 10 curated datasets covering nanomaterials and small molecules; agentic document processing, not lab-interactive.

## Domains

Chemistry and materials science — nanomaterials (nanozymes, nanomagnetics) and small-molecule datasets, published at a NeurIPS materials-discovery workshop.

## Evaluation

- Extraction quality benchmarked against domain-expert-validated records.
- **Reported.** Persistent challenges for all evaluated systems: domain-specific terminology, complex tabular and schematic representations, and context-dependent ambiguities. Quantitative figures are TODO(reference) — not stated in the abstract.

## Typical Duration

Per-document extraction episodes over full scientific papers.

## Main Contribution

Expert-validated ground truth for chemistry-domain information extraction at the agentic level — measuring the step that decides whether literature-scale chemical databases can be machine-built.

## Key Design Ideas

- Ten separate datasets spread the evaluation across genuinely different chemical record types.
- Expert validation of every dataset makes extraction errors attributable to the system, not the labels.
- Comparing agentic pipelines against controlled single-agent preprocessing isolates where agency helps.

## Strengths

- Covers the practically critical, rarely benchmarked literature-to-database step.
- Public datasets on an institutional HuggingFace hub.

## Limitations

- Repository note: card compiled from the arXiv abstract and official dataset hub (August 2026); details beyond those sources await full-paper validation. The venue per arXiv Comments is the AI4Mat workshop at NeurIPS 2025, not the main Datasets and Benchmarks track.

## Related Works

- [MetaSyn](./metasyn.md) — Also literature-grounded evaluation of extracting structured evidence from published papers.
- [MaCBench](./macbench.md) — Also chemistry/materials data extraction, tested at the vision-language perception layer.
- [SciExplore](./sciexplore.md) — Also structured scientific information seeking, across broader disciplines.
