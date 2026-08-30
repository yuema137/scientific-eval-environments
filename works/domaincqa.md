# DomainCQA / AstroChart (2025)

> **English** | [简体中文](../zh/works/domaincqa.md)

> **First appeared:** 2025-03-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2503.19498)

## Overview

DomainCQA is a methodology for building knowledge-intensive chart question-answering benchmarks in a scientific domain, instantiated as **AstroChart** — 1,690 QA pairs over 482 charts taken from astronomy papers — and used to evaluate 21 multimodal large language models against a human baseline.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.19498>
- **Code:** <https://github.com/LingZhong01/DomainCQA>
- **Data:** <https://huggingface.co/datasets/yangjing0128/AstroChart>
- **Venue:** arXiv preprint, first submitted March 2025 (v6, January 2026)

## Summary

The authors argue that existing chart benchmarks mostly probe surface-level parsing — reading labels, ticks and legends — and therefore say little about whether a model can reason about a scientific figure the way a domain reader does. DomainCQA answers this with a three-phase construction recipe (chart selection, QA-pair generation, expert validation) that deliberately separates two question families: *Fundamental QA* (FQA), which tests chart comprehension, and *Advanced QA* (AQA), which requires integrating domain knowledge that is not present in the figure. AstroChart applies the recipe to astronomy, drawing charts from arXiv astronomy papers and validating every item with domain experts. Twenty-one MLLMs are scored zero-shot, and four astronomy researchers answer a 10% sample to establish a human reference point.

## Tasks

1,690 QA pairs over 482 distinct charts extracted from arXiv astronomy papers, split into 1,509 FQA pairs and 181 AQA pairs.

- **FQA — Visual (602):** Color (211), Style (133), Text (213), Layout (45).
- **FQA — Data (316):** Point (130), Interval (102), Calculation (84).
- **FQA — Inference (289).**
- **FQA — Chart Description (302).**
- **AQA — Knowledge-Based Inference (181).**

Construction: charts are selected with a chart-complexity vector and non-parametric Gibbs sampling so that the sample is domain-representative, with a separate selection path for AQA charts in which a chain-of-thought "chart abstract selector" identifies each paper's main findings by cross-model majority voting. Generated QA pairs are then reviewed independently by domain experts, who mark each item Valid or Flawed until consensus. Beyond astronomy, the paper reports partial AQA studies in biochemistry, economics, medicine and social science as pilots; astronomy is the only fully built dataset.

## Domains

Astronomy. Every AstroChart item is a figure from an astronomy paper — plots, spectra, distributions and derived-quantity charts — and the AQA half requires astrophysical knowledge beyond what the figure displays, so the evaluated objective is astronomical figure interpretation rather than generic chart parsing. The pilot domains (biochemistry, economics, medicine, social science) are partial AQA studies used to argue that the construction recipe transfers; they are not released as complete datasets.

## Evaluation

- **Numerical answers** are scored by relative error normalized by the axis range; derivation-style answers use exact match.
- **Open-ended answers** are scored 0–1 by an LLM judge (DeepSeek-V3) on relevance, correctness and completeness. Judge agreement against human annotation on a 176-item sample is reported at Pearson r = 0.816, Spearman ρ = 0.817, MAE = 0.096.
- **Supplementary metrics:** ROUGE-L, BLEU-4 and L3Score.
- **Protocol:** zero-shot evaluation of 21 MLLMs (proprietary and open-weights); four astronomy researchers answer 10% of the questions as a human baseline.
- **Reported (selected rows, as `Visual-All / Data-All / Inference / Chart-Desc / KB-Inference / Overall`):**
  - Gemini-2.5-Pro — 88.22 / 72.66 / 81.31 / 81.09 / 73.65 / **81.30**
  - Pixtral-Large-124B — 86.11 / 59.38 / 78.65 / 80.93 / 70.83 / 77.23
  - GPT-4o — 86.23 / 53.19 / 75.40 / 80.96 / 73.04 / 75.84
  - Human baseline (10% sample) — 98.60 / 96.40 / 91.82 / 70.00 / 39.00 / 85.56

## Typical Duration

N/A — single-turn question answering; the paper reports no per-item wall-clock, token or cost budget.

## Main Contribution

A generalizable recipe for turning domain papers into a knowledge-intensive chart-QA benchmark, separating chart comprehension from knowledge-dependent inference, together with AstroChart as its astronomy instantiation and an analysis attributing model failures to three causes: chart reasoning (inferring trends), numerical computation (extracting values reliably), and domain-fact integration.

## Key Design Ideas

- Two question families by design: FQA measures whether the model reads the figure, AQA measures whether it can combine the figure with domain knowledge it must already hold.
- Chart selection is sampled for domain representativeness rather than convenience, with a distinct selection path for AQA anchored on the source paper's main findings.
- Fine-grained FQA taxonomy (Visual → Color/Style/Text/Layout; Data → Point/Interval/Calculation; Inference; Chart Description) so failures can be localized instead of collapsing into one accuracy number.
- Mixed scoring: axis-range-normalized relative error for numbers, exact match for derivations, LLM judge for open-ended text, with the judge itself validated against human scores.
- A human baseline answered by domain researchers on a fixed 10% sample rather than by crowd workers.

## Strengths

- The AQA split isolates knowledge-dependent inference, which is the part of scientific figure reading that generic chart benchmarks do not test.
- Every item passes independent expert review with an explicit Valid/Flawed adjudication to consensus.
- The LLM judge is not assumed reliable: its agreement with human annotation is measured and reported.
- Wide model coverage (21 MLLMs, proprietary and open-weights) with per-category breakdowns rather than a single headline score.
- Charts, QA pairs and code are publicly released.

## Limitations

- AQA is small (181 items) relative to FQA (1,509), so the knowledge-dependent conclusions rest on the smaller half of the dataset.
- The human baseline is measured on a 10% sample by four researchers, and its per-category profile is uneven — very high on Visual and Data, but 70.00 on Chart Description and 39.00 on Knowledge-Based Inference, below several models. This makes the aggregate 85.56 an unreliable ceiling and suggests the open-ended judge rewards model-style verbosity.
- Repository note: this is single-turn multimodal question answering, not an agent evaluation — there is no tool use, no archive access and no multi-step trajectory. It is recorded here under the repository's exam-derived-QA precedent: a named, sized item set with a stated scoring protocol and many models compared.
- Repository note: the non-astronomy pilots are partial AQA studies only, so the paper's claim that the recipe generalizes across domains is supported by construction-quality evidence rather than by complete benchmarks.

## Related Works

- [AstroMMBench](./astrommbench.md) — The closest neighbour: also multimodal astronomy questions built from figures in astronomy papers with expert review, but multiple-choice rather than mixed numeric/open-ended, and without a knowledge-inference split.
- [AstroMLab 1](./astromlab-1.md) — Also an astronomy knowledge benchmark scored across many models, but text-only multiple choice derived from review articles.
- [AstroAlertBench](./astroalertbench.md) — Also single-turn multimodal astronomy evaluation, on survey alert stamps rather than paper figures.
- [MaScQA](./mascqa.md) — Precedent for admitting a sized, protocol-stated domain question set evaluated across multiple models.
