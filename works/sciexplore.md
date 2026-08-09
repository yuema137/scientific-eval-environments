# SciExplore (2026)

> **English** | [简体中文](../zh/works/sciexplore.md)

## Overview

SciExplore is a benchmark evaluating autonomous agents on scientific information seeking, from database navigation to cross-source information integration. It comprises 103 expert-curated tasks in four progressive task types across more than ten scientific disciplines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.20926>
- **Venue:** arXiv preprint, 2026 (submitted to ACL 2026)

## Summary

SciExplore evaluates the scientific information-seeking and reasoning capabilities of LLMs and agents through four progressive task types — scientific database navigation, ambiguous literature retrieval, missing reference completion, and cross-source structured knowledge synthesis — assessing capabilities from entity-level reasoning and document-level identification to evidence-level grounding and domain-level synthesis.

## Tasks

103 expert-curated tasks in four task types: scientific database navigation, ambiguous literature retrieval, missing reference completion, and cross-source structured knowledge synthesis, across more than ten scientific disciplines.

## Domains

More than ten scientific disciplines; the abstract does not itemize them.

## Evaluation

- Over ten state-of-the-art LLMs and autonomous agents evaluated across the four progressive task types.
- **Reported.** Substantial performance gaps, with performance degrading sharply as task complexity increases and extremely low accuracy on the most challenging structured-synthesis tasks.

## Typical Duration

Multi-step information-seeking workflows over scientific databases and literature; per-task budgets are TODO(reference).

## Main Contribution

A progressive-capability benchmark for scientific information seeking that separates database navigation, retrieval, evidence grounding, and cross-source synthesis instead of scoring them as one blended ability.

## Key Design Ideas

- Four task types form a capability progression from entity-level reasoning to domain-level synthesis.
- Expert curation across more than ten disciplines rather than a single-field testbed.

## Strengths

- Cleanly separates where scientific information-seeking breaks down as complexity increases.
- The hardest tier (structured synthesis) shows extremely low accuracy, leaving clear headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [AutoResearchBench](./autoresearchbench.md) — Also isolates scientific literature discovery, with exact-match and set-IoU scoring over 1,000 queries.
- [AstaBench](./astabench.md) — Also evaluates literature understanding among broader research capabilities, with cost-controlled scoring.
- [ScholarQuest](./scholarquest.md) — Also evaluates agentic paper search, taxonomy-guided over computer science topics.
