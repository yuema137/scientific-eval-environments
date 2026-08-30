# Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes (2026)

> **English** | [简体中文](../zh/works/frontier-llm-based-agents-can-overcome-the-ontolog.md)

> **First appeared:** 2026-05-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.28965)

## Overview

A controlled re-evaluation of an established biocuration gold standard in which five frontier LLMs, each run as an "agentic curator" inside a self-contained workspace, produce Entity-Quality phenotype annotations and are scored against the same gold standard, the same three trained human curators, and the same NLP baseline used in the original 2018 study.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.28965>
- **Code:** <https://github.com/phenoscape/goldstandard>

## Summary

Phenotype annotation — linking free-text phenotype descriptions to ontology terms — is the step that makes comparative morphological data integrable across studies, and it has remained expert-bound and therefore unscalable. Dahdul et al. (2018) built a Gold Standard of Entity-Quality (EQ) annotations across seven phylogenetic studies and used it to compare three human curators with the Semantic CharaParser NLP tool, finding machine-human consistency well below human-human consistency. This paper revisits that benchmark with five frontier hosted LLMs from Anthropic and OpenAI. Each model is given a self-contained workspace containing the source publication PDF, the same annotation guide the human curators used, the four project ontologies, and a validation script, and is evaluated with the original semantic-similarity metrics.

## Tasks

The evaluation reuses the Dahdul et al. (2018) Gold Standard: 203 characters (463 character states) sampled from seven phylogenetic studies in vertebrate morphology. To avoid leakage from workspace refinement, scoring is restricted to characters 51–203, comprising 344 character states. Each task asks the agent to read the source publication and emit EQ annotations for the character states, grounded in four OBO-format ontologies (UBERON, PATO, BSPO, GO), with a validation script available in the workspace.

## Domains

Biology. Specifically comparative vertebrate morphology and evolutionary biology, with the annotations feeding phenotype knowledge bases used for cross-study data integration. No co-domain is claimed.

## Evaluation

Four ontology-based semantic-similarity metrics carried over from the original study: SimJ (Jaccard similarity of ancestor sets), NIC (normalized information content of common ancestors), partial precision (penalizing extra annotations), and partial recall (penalizing missing annotations). Agents are scored against the Gold Standard and compared both to the three trained human biocurators and to Semantic CharaParser. The five models evaluated are Opus 4.6, Opus 4.7 and Sonnet 4.6 from Anthropic and GPT-5.4 and GPT-5.4-mini from OpenAI. Every agent falls within the range of inter-curator variability among the three human curators; the best agents comfortably exceed two of the three curators but do not reach the best human curator (WD); all agents substantially outperform Semantic CharaParser on all four metrics, with the Claude Opus models roughly twice as high on SimJ.

## Typical Duration

No turn, step, or wall-clock limit is reported. Cost is reported per annotated character: approximately $0.26 for Opus 4.6 and $0.43 for Opus 4.7.

## Main Contribution

Evidence, on an unmodified pre-existing gold standard with unmodified metrics, that frontier LLM agents have closed the human-machine gap in ontology-based phenotype curation that the 2018 study documented — reframing the curation bottleneck as tractable rather than intrinsically expert-bound.

## Key Design Ideas

- Reuse of an eight-year-old published benchmark, its metrics, and its human-curator scores unchanged, so the comparison is against a fixed prior reference point rather than a new baseline the authors chose.
- The agent is given exactly what a human curator was given — the source PDF, the same annotation guide, and the project ontologies — rather than a preprocessed extraction task.
- A validation script inside the workspace lets the agent check its own output against ontology structure before committing, making the setup agentic rather than single-shot.
- Characters 1–50 are held out from scoring because they were used while refining the workspace, keeping the reported evaluation clean of tuning.
- Human inter-curator variability is used as the reference band, so the question posed is "is the agent within the range of trained curators" rather than "does the agent beat a single score".

## Strengths

- The comparison point is a fixed prior reference — an eight-year-old published benchmark with its metrics and human-curator scores reused unchanged — rather than a baseline the authors selected for themselves.
- Human inter-curator variability is used as the reference band, so the reported result ("within the range of trained curators") is interpretable in a way a single-number comparison would not be.
- Agents receive exactly what a human curator received: the source PDF, the same annotation guide, and the project ontologies, rather than a preprocessed extraction task.
- Characters 1–50 are held out from scoring because they were used while refining the workspace, keeping the reported evaluation clean of tuning.
- The four ontology-aware metrics (SimJ, NIC, partial precision, partial recall) give partial credit by ontology structure, which suits a task where a near-miss annotation is not simply wrong.

## Limitations

- The Gold Standard has been publicly available since 2018 and may appear in model training data; the authors acknowledge this contamination risk explicitly.
- Local open-weight models did not succeed at the task, so the result is specific to frontier hosted models.
- Scope is vertebrate morphology; extension to other taxa depends on the existence of a sufficiently rich anatomy ontology.
- Five models on 344 character states from seven studies is a small evaluation, and the paper is a seven-page report rather than a full benchmark release.
- Repository note: the contribution is an evaluation study over an existing dataset, not a newly released benchmark artifact — the reusable object is the agentic-curator workspace and the scoring pipeline in the linked repository.

## Related Works

- [FlyAOC](./flyaoc.md) — The same evaluated task, agentic ontology curation for a scientific knowledge base, released as a purpose-built benchmark in Drosophila genetics.
- [BioKGBench](./biokgbench.md) — Biomedical knowledge-graph agent tasks, scoring error detection in an existing KG rather than annotation against expert curators.
- [LAB-Bench](./lab-bench.md) — Biology-research capability suite with human expert baselines, using multiple-choice rather than open-ended ontology grounding.
- [CeProBench](./ceprobench.md) — Also uses expert-authored structured annotations as ground truth for extraction, in chemical process development.
