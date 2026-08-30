# ScholarQuest (2026)

> **English** | [简体中文](../zh/works/scholarquest.md)

> **First appeared:** 2026-06-18 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.20235)

## Overview

ScholarQuest is a large-scale, taxonomy-guided benchmark for agentic academic paper search in open literature environments, constructed from over 1,000 computer science topics and four representative research intents.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.20235>
- **Venue:** arXiv preprint (cs.IR), 2026

## Summary

ScholarQuest systematically evaluates LLM-based search agents performing iterative literature exploration. Its four research-intent categories — method-oriented, setting-anchored, comparison-based, and scope-controlled queries — model how researchers actually search. Agentic methods outperform single-shot baselines, yet the best-performing agent achieves only 0.314 Recall@100 and 0.355 Recall@All, and the paper analyzes search efficiency, intent-level robustness, and failure cases.

## Tasks

Queries constructed from over 1,000 computer science topics across four research-intent categories: method-oriented, setting-anchored, comparison-based, and scope-controlled. Exact query counts are TODO(reference).

## Domains

Computer science literature (information retrieval and AI focus).

## Evaluation

- **Recall@100 and Recall@All** against the ground-truth paper sets.
- Analyses of search efficiency, intent-level robustness, and failure cases.
- **Reported.** The best-performing agent achieves only 0.314 Recall@100 and 0.355 Recall@All; agentic methods outperform single-shot baselines but leave substantial room for improvement.

## Typical Duration

Iterative literature-exploration episodes in open literature environments.

## Main Contribution

A taxonomy of research intents applied at scale to agentic paper search, showing recall stays low even for the best agents once intent structure is controlled.

## Key Design Ideas

- Intent taxonomy (method / setting / comparison / scope) replaces undifferentiated 'find papers' queries.
- Open literature environments rather than a frozen corpus.
- Recall at two cutoffs separates ranking quality from coverage.

## Strengths

- Scale (1,000+ topics) with controlled intent structure.
- Failure-case analysis identifies where iterative exploration breaks down.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [AutoResearchBench](./autoresearchbench.md) — Also benchmarks agentic literature discovery; ScholarQuest organizes queries by research intent rather than deep/wide task types.
- [SciExplore](./sciexplore.md) — Also evaluates scientific information seeking, across progressive capability levels rather than search intents.
- [AstaBench](./astabench.md) — Also includes paper-finding among its literature-understanding tasks, with cost-controlled scoring.
