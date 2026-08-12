# DrBencher (2026)

> **English** | [简体中文](../zh/works/drbencher.md)

## Overview

DrBencher is a synthetic benchmark generator that produces questions requiring interleaved web browsing and multi-step computation, synthesizing answer-first from knowledge-graph chains so that gold answers are verifiable by executing parameterized code over knowledge-graph values.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General-purpose deep-research browsing+computation benchmark generator spanning mostly non-science domains (finance, security, history); generic web retrieval and arithmetic, not a scientific/research activity.

## Links

- **Paper:** https://arxiv.org/abs/2604.09251
- **Code:** https://github.com/IBM/DrBencher
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

DrBencher targets a reported blind spot in deep-research agent evaluation: existing benchmarks assess browsing and computation in isolation, whereas real tasks interleave the two. Rather than start from seed passages, DrBencher generates questions answer-first from knowledge-graph chains, with no provenance text. A unified pipeline enforces four criteria — verifiability, complexity, difficulty, and diversity — across five domains, and the authors release both the generation pipeline and a human-verified benchmark dataset.

## Tasks

Questions require multi-hop entity identification, retrieval of quantitative properties, and domain-specific computation over the retrieved values. Questions are synthesized answer-first from knowledge-graph chains (no seed passages or provenance text). The released human-verified benchmark spans five domains: biochemistry, financial, geophysical, security, and history. Total item count of the released benchmark: TODO(reference) (primary-source extractions consulted for this card disagreed on the exact count and the number retained after human validation).

## Domains

Five domains: biochemistry, financial, geophysical, security, and history. Per-domain knowledge sources include Wikidata/Wikipedia across all domains, with domain-specific sources such as PubChem, UniProt, RCSB PDB, and ChEMBL (biochemistry), SEC EDGAR (financial), and NIST NVD, FIRST EPSS, and CISA KEV (security). Only the biochemistry (Chemistry/Biology) and geophysical (Earth Science) domains fall under the repository's science/engineering domain taxonomy; financial, security, and history do not.

## Evaluation

Automatic evaluation is execution-based: gold answers are computed by executing parameterized code over knowledge-graph values, and a model's numerical response is scored against the gold answer within a relative tolerance (reported as ~2% for most domains, with exact match for history). The reported "answer accuracy" is the fraction of questions whose answer matches the gold value within tolerance. A two-stage verification cascade (closed-book, then tool-augmented) filters out questions solvable by the generating model. Human evaluation reported 76% validity, with 35% of errors attributed to outdated knowledge-graph entries.

## Typical Duration

TODO(reference) — the paper does not report a standardized per-task token budget or wall-clock time in the sources consulted; tasks require interleaved browsing and multi-step computation.

## Main Contribution

An answer-first, provenance-free benchmark-generation pipeline that synthesizes browsing-plus-computation questions from knowledge-graph chains, jointly enforcing verifiability (executable gold answers), complexity (multi-hop identification, retrieval, and computation), difficulty (a two-stage verification cascade that discards questions solvable by the generating model), and diversity (a greedy max-min embedding filter). The authors report that DrBencher achieves the highest semantic diversity relative to manually constructed benchmarks (BrowseComp+, MATH-500, GPQA), and that the strongest frontier model evaluated reaches only 20% answer accuracy.

## Key Design Ideas

- **Answer-first synthesis.** Questions are generated from knowledge-graph chains with no seed passages or provenance text, so each gold answer is fixed before the natural-language question is composed.
- **Verifiability by construction.** Gold answers are computed by executing parameterized code over knowledge-graph values rather than judged by a model.
- **Difficulty filtering via a two-stage cascade.** A closed-book verification stage followed by a tool-augmented stage discards questions the generating model can already solve.
- **Diversity via greedy max-min embedding filter.** Selection maximizes coverage across entities, templates, and linguistic expression.
- **Multi-domain knowledge sources.** Domain-specific APIs/knowledge graphs (e.g., PubChem, UniProt, SEC EDGAR, NIST NVD) supply the values used to compute gold answers.

## Strengths

- Deterministic, execution-based gold answers reduce dependence on model-judge scoring (paper).
- Explicitly targets interleaved browsing + computation, which the authors argue existing benchmarks evaluate only in isolation (paper).
- Releases both the generation pipeline and a human-verified dataset (paper; https://github.com/IBM/DrBencher).

## Limitations

- Human evaluation found 76% validity, with 35% of errors due to outdated knowledge-graph entries — an inherent limitation of reasoning over evolving data that the authors highlight (paper).
- Repository note: three of the five domains (financial, security, history) fall outside the repository's science/engineering domain taxonomy, so the benchmark is only partially scientific in scope.
- Repository note: the exact size of the released benchmark and the number of items retained after human validation could not be verified consistently from the sources consulted for this card; these are marked `TODO(reference)`.

## Related Works

- [MedBrowseComp](./medbrowsecomp.md) — another deep-research benchmark requiring multi-hop browsing plus retrieval/reasoning over structured domain data.
