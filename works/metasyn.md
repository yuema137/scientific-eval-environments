# MetaSyn (2026)

> **English** | [简体中文](../zh/works/metasyn.md)

> **First appeared:** 2026-06-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.17041)

## Overview

MetaSyn is a benchmark for LLM agents on systematic review and meta-analysis, built from 422 expert-curated meta-analyses sourced from more than 34,000 Nature Portfolio articles, with research questions, structured eligibility criteria, the originally included studies, and a shared PubMed-anchored corpus.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.17041>
- **Venue:** arXiv preprint, 2026

## Summary

MetaSyn asks whether LLM agents can conduct reliable systematic review and synthesis following standardized protocols (the PI/ECO framework). Each task provides a research question with structured eligibility criteria and a corpus containing both the studies the original reviewers included and ineligible distractors; agents must identify the eligible set and synthesize. The paper also releases an MA-Retriever model alongside the dataset.

## Tasks

422 expert-curated meta-analyses drawn from over 34,000 published Nature Portfolio articles, each packaged with the research question, structured eligibility criteria, the studies included by the original reviewers, and a shared PubMed-anchored corpus with ineligible distractors.

## Domains

Meta-analysis subjects span physics, chemistry, psychology, and medical science.

## Evaluation

- Study-identification against the original reviewers' included set, with ineligible distractors in the corpus.
- Stage-wise evaluation and analysis locating where systems underperform along the meta-analysis pipeline.
- **Reported.** The authors conclude existing AI systems are far from perfect at protocol-faithful meta-analysis.

## Typical Duration

Multi-stage systematic-review workflows over a literature corpus; per-task budgets are TODO(reference).

## Main Contribution

The first large-scale benchmark anchoring agent evaluation to expert-conducted meta-analyses, making protocol-faithful systematic review a measurable agent capability.

## Key Design Ideas

- Ground truth is what the original expert reviewers actually included, not synthetic labels.
- A shared PubMed-anchored corpus with distractors turns eligibility screening into a controlled retrieval problem.
- Stage-wise evaluation localizes failures along the review pipeline instead of reporting one end score.

## Strengths

- 422 tasks distilled from 34,000+ articles give unusual scale for expert-grounded evaluation.
- PI/ECO protocol fidelity is evaluated, not just answer overlap.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [DeepResearch Bench](./deepresearch-bench.md) — Also evaluates literature-grounded synthesis, scoring open-domain research reports rather than protocol-bound meta-analyses.
- [AutoResearchBench](./autoresearchbench.md) — Also scores literature identification against verified answer sets, for paper discovery rather than eligibility screening.
- [NatureBench](./naturebench.md) — Also derives evaluation targets from Nature-family publications, for method reproduction rather than evidence synthesis.
