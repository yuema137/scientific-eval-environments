# MatViX (2024)

> **English** | [简体中文](../zh/works/matvix.md)

> **First appeared:** 2024-10-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2410.20494)

## Overview

MatViX benchmarks multimodal information extraction from visually rich materials articles: 324 full-length research articles paired with 1,688 complex structured JSON files curated by domain experts, where vision-language models must extract compositions and property curves from text, tables, and figures in a zero-shot setting.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.20494>
- **Code:** <https://github.com/ghazalkhalighinejad/matvix>
- **Project:** <https://matvix-bench.github.io/>
- **Venue:** arXiv preprint (cs.CL), 2024

## Summary

Materials knowledge is locked in figures and tables as much as prose, and MatViX tests whether VLMs can free it: 324 full-length articles (polymer nanocomposites and biodegradation) map to 1,688 expert-curated structured JSON targets combining compositions (strings) and properties (lists of (x,y) curve points). Models extract in zero-shot mode, and the benchmark's distinctive metrics grade not just entities but the fidelity of extracted curves.

## Tasks

Zero-shot multimodal extraction over 324 full-length articles into 1,688 structured JSON records (compositions + property curves), from text, tables, and figures; static extraction.

## Domains

Materials science — structured data extraction for polymer nanocomposites and biodegradation, from visually rich full-text articles.

## Evaluation

- F1 for composition alignment; Curve Similarity Score (CSS) and Curve Alignment Score (CAS) for extracted property curves.
- **Reported.** Zero-shot VLMs are benchmarked across baseline, text-only, and text+image configurations; per-model numbers are in the paper body (TODO(reference)).

## Typical Duration

Per-article extraction over full-length documents; no interactive setting.

## Main Contribution

Extending materials extraction evaluation to full documents and to curves — grading the (x,y) data buried in figures, not just named entities in text.

## Key Design Ideas

- Curve-fidelity metrics (CSS, CAS) evaluate the figure data that materials papers actually carry.
- Full-length articles force cross-section integration (text + tables + figures).
- Expert-curated JSON targets make the extraction schema faithful to the domain.

## Strengths

- One of the few materials extraction benchmarks that grades figure-derived numeric curves.
- Public project, code, and expert-curated targets.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); the evaluated-model roster and per-model numbers are in the paper body. No venue is stated in arXiv metadata; the dataset was marked "coming soon" at time of writing.

## Related Works

- [MatCha](./matcha.md) — Also multimodal materials understanding, on characterization QA rather than extraction.
- [ChemX](./chemx.md) — Also agentic chemical/materials information extraction, over expert-validated datasets.
- [MatTools](./mattools.md) — Also structured materials computation by models, via tool-use.
