# FlyAOC (2026)

> **English** | [简体中文](../zh/works/flyaoc.md)

## Overview

FlyAOC is a benchmark for end-to-end agentic ontology curation: given only a gene symbol, an agent must search and read a corpus of 16,898 full-text Drosophila papers and emit ontology-grounded structured annotations, scored against 7,397 expert curations drawn from FlyBase. (The arXiv abstract of the same version also refers to the benchmark as "FlyBench"; the paper title, the released code, and the repository name all use FlyAOC.)

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.09163>
- **Code:** <https://github.com/xingjian-zhang/flyaoc>

## Summary

Maintaining a scientific knowledge base requires expert curators to find the relevant papers, reconcile evidence across documents, and express the result as ontology-grounded annotations. FlyAOC argues that existing benchmarks capture only isolated subtasks of this workflow — named entity recognition, relation extraction — and instead scores the whole curator loop. The benchmark is built from FlyBase, the Drosophila melanogaster knowledge base, and pairs a fixed literature corpus with the expert annotations that curators actually produced from it. Four baseline agent architectures are compared, and the paper reports that architecture matters more than backbone scale, with all baselines leaving substantial headroom.

## Tasks

100 benchmark genes, each posed as an open-ended curation task over a shared corpus of 16,898 full-text papers (reported as more than 140 million words, sourced from PubMed Central). Three annotation task types are scored, totalling 7,397 expert-curated ground-truth annotations: Gene Ontology function terms (3,621 annotations across 1,228 unique terms), expression patterns (1,331 annotations over 465 anatomy terms and 69 developmental stages), and historical synonyms linking decades of nomenclature (2,445 annotations). The paper additionally identifies a "corpus-grounded" subset — the annotations actually recoverable from the released corpus — covering 28.9% of GO terms, 37.0% of expression annotations, and 36.4% of synonyms.

## Domains

Biology. The tasks are drawn from Drosophila melanogaster genetics and molecular biology as curated in FlyBase, and require reading primary biological literature and mapping evidence onto the Gene Ontology and anatomy/developmental-stage ontologies. No co-domain is claimed; the retrieval-augmented reasoning capability is presented as transferable, but the evaluated tasks are biological.

## Evaluation

Predictions are scored per annotation type. Gene Ontology and expression annotations use semantic recall@k, which awards partial credit for ontologically related predictions via Wang similarity over the ontology's directed acyclic graph; historical synonyms use case-insensitive exact matching with standard recall@k. The paper uses k=20 for GO and synonyms and k=10 for expression, chosen as roughly twice the mean number of corpus-grounded annotations per gene. Micro-averaged recall, weighting all annotations equally, is the primary reported metric. Four baseline architectures are compared: memorization (no retrieval), fixed pipeline, single-agent, and multi-agent. At 16 papers per gene with GPT-5-mini, the multi-agent baseline reports semantic recall of 53.1% on Gene Ontology, 52.8% on expression, and 57.3% on synonyms; the single-agent baseline degrades beyond roughly 8 papers as context overflows.

## Typical Duration

No wall-clock budget is reported. Cost is reported per gene at 16 papers per gene with GPT-5-mini: about $0.37/gene for the multi-agent baseline, $0.85/gene for the single-agent baseline, and $0.10/gene for the fixed pipeline.

## Main Contribution

The first benchmark, in the authors' framing, to evaluate AI agents on end-to-end agentic ontology curation from scientific literature, rather than on the isolated extraction subtasks that prior benchmarks target — grounded in a real, actively maintained scientific knowledge base and its expert curation record.

## Key Design Ideas

- The task input is deliberately minimal — a gene symbol only — so that retrieval, cross-document reconciliation, and ontology grounding are all inside the evaluated loop.
- A fixed, released corpus of 16,898 full-text papers makes retrieval reproducible and lets the authors separate what is recoverable from the corpus from what is not.
- Ontology-aware scoring: semantic recall@k with Wang similarity gives partial credit for predictions that are ontologically near the gold term, rather than treating the label set as flat.
- A memorization baseline (no retrieval) isolates how much of an agent's output comes from parametric knowledge of a heavily studied model organism.
- Four architectures spanning the design space — memorization, fixed pipeline, single-agent, multi-agent — are used to attribute performance to architecture versus backbone scale.

## Strengths

- Ground truth is real curatorial output from a production knowledge base, not annotations created for the benchmark.
- The corpus-grounded subset makes the ceiling explicit, so recall numbers can be read against what the released corpus actually supports.
- Ontology-aware partial credit is a better fit for curation than exact-match scoring, and the synonyms task retains exact matching where it is appropriate.
- Per-gene cost is reported alongside accuracy, making the architecture comparison legible as a cost/quality trade-off.
- The behavioural analysis is diagnostic rather than decorative: the finding that agents mainly use retrieval to confirm parametric knowledge rather than to discover new information is a concrete failure mode.

## Limitations

- Text-only evaluation; figures, which carry a large share of expression evidence, are excluded.
- The corpus covers only roughly 30% of the papers related to the benchmark genes, so absolute recall understates achievable performance.
- FlyBase ground truth may itself be incomplete, so unmatched predictions are not necessarily wrong.
- The setting is fully autonomous curation; the human-in-the-loop workflow that real curation uses is not evaluated.
- Drosophila is among the most intensively studied model organisms, so parametric knowledge is unusually strong here — the memorization baseline is informative, but transfer to less-studied organisms is untested.
- Repository note: reported headline numbers come from one backbone (GPT-5-mini) at one retrieval depth; the card does not carry a full cross-model table.

## Related Works

- [BioKGBench](./biokgbench.md) — Also puts a biomedical knowledge graph at the centre of an agent task, but scores error-finding in an existing KG rather than producing new curations.
- [Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes](./frontier-llm-based-agents-can-overcome-the-ontolog.md) — The same evaluated task (agentic ontology curation against expert curators), in comparative morphology rather than Drosophila genetics.
- [LAB-Bench](./lab-bench.md) — Biology-research capability suite whose literature and database subtasks are the isolated subtasks FlyAOC contrasts itself against.
- [CeProBench](./ceprobench.md) — Uses expert entity/relation annotations as ground truth for a document-to-knowledge-graph extraction task in a different domain.
- [ScholarQuest](./scholarquest.md) — Agentic literature search evaluated on its own, without the downstream structured-annotation step.
