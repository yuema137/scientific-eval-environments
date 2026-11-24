# AIS-Bench (2026)

> **English** | [简体中文](../zh/works/ais-bench.md)

> **First appeared:** 2026-09-18 · **Source:** [OpenReview submission](https://openreview.net/forum?id=RT78MFtfKQ)

## Overview

AIS-Bench evaluates AI Scientist systems (agents that generate hypotheses, implement methods, and report findings) phase by phase instead of only by their final manuscript. Each item is built from a published machine-learning paper with executable code and split into a context, the idea, the reference code, and the paper. A system is scored separately on reconstructing the idea from the context, implementing it as code, and reporting results, so a weak end-to-end outcome can be traced to the phase where the artifact went wrong. On matched items, implementation receives the lowest phase score.

## Topics


- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities


- [End-to-End Research](../activities/end_to_end_research.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** [AIS-Bench: An AI Scientist Benchmark for Autonomous Scientific Discovery](https://openreview.net/forum?id=RT78MFtfKQ), ICLR 2027 submission 39831 (PDF: <https://openreview.net/pdf?id=RT78MFtfKQ>). Authors: TODO(reference).
- **Venue:** ICLR 2027 submission under review, primary area datasets and benchmarks; OpenReview page dated 18 Sept 2026, modified 05 Oct 2026; license CC BY 4.0.
- **Code:** TODO(reference)

## Summary

Existing AI Scientist evaluations either test one capability in isolation or judge the end product, which leaves the intermediate artifacts unchecked. AIS-Bench fixes a <Context, Idea, Code, Paper> quadruplet per item and scores three phases independently: Reference-Conditioned Idea Reconstruction (the system produces the idea given the context), Code Implementation (the system produces code against an executable reference implementation), and Controlled Reporting (the system writes up findings given specified evidence). Judge-based parts of the phase metrics are validated against held-out human judgments. Under a common human-calibrated artifact-validity criterion, implementation scores lowest of the three phases, and this ordering holds under paired bootstrap intervals and alternative aggregations.

## Tasks

753 aligned <Context, Idea, Code, Paper> quadruplets with executable reference implementations, produced by the construction protocol from 3,174 machine-learning papers. Each quadruplet supports three phase tasks: idea reconstruction conditioned on reference context, code implementation, and controlled reporting. Construction filters, the exact phase inputs, and per-phase item counts are TODO(reference).

## Domains

Machine-learning research (source papers are machine-learning papers).

## Evaluation

- **Phase-specific metrics:** each phase is scored independently; metric definitions are TODO(reference).
- **Judge validation:** judge-based components are validated against held-out human judgments; agreement statistics are TODO(reference).
- **Systems evaluated:** 13 prompting strategies, specialized systems, and end-to-end agents; names and per-system scores are TODO(reference).
- **Phase comparison:** on matched quadruplets under a common human-calibrated artifact-validity criterion, implementation receives the lowest phase score; paired bootstrap intervals and alternative aggregations preserve this ordering. Numeric phase scores are TODO(reference).
- **Audits:** among classified implementation failures, functional-logic deviations dominate; in reports, metric exaggeration and unresolved citations persist despite specified evidence. Audit counts are TODO(reference).

## Typical Duration

TODO(reference)

## Main Contribution

A diagnostic framework that scores automated research in three independently evaluated phases (idea reconstruction, code implementation, controlled reporting) on paper-derived quadruplets with executable reference code, rather than scoring only isolated capabilities or final manuscripts.

## Key Design Ideas

- Quadruplet construction aligns context, idea, code, and paper from the same source work, so each phase has its own reference.
- Reference-conditioned idea reconstruction gives the idea phase a fixed target instead of open-ended novelty judging.
- Controlled reporting supplies the evidence, so reporting errors (metric exaggeration, unresolved citations) are separated from implementation errors.
- A common human-calibrated artifact-validity criterion allows phase scores to be compared on matched items.

## Strengths

- Phase-separated scoring localizes where automated research fails; the abstract reports implementation as the weakest phase.
- Judge-based components are checked against held-out human judgments.
- Robustness of the phase ordering is checked with paired bootstrap intervals and alternative aggregations.

## Limitations

- Repository note: this card is written from the OpenReview submission page only; the full paper could not be retrieved, so metrics, system names, scores, and author-stated limitations are TODO(reference).
- Repository note: the First appeared date is the posting date shown on the OpenReview submission page; whether the submission was publicly visible on that date could not be verified, and no earlier public version (arXiv or code release) was found.
- Repository note: all source papers are machine-learning papers, so the phase ordering is reported for ML research only.

## Related Works

- [PaperBench](./paperbench.md) — Also builds tasks from ML papers, but scores replication of a whole paper against a hierarchical rubric rather than separate idea, code, and reporting phases.
- [ResearchCodeBench](./researchcodebench.md) — Also scores implementation of research-paper contributions as executable code, the phase AIS-Bench reports as weakest.
- [AI-Researcher](./ai-researcher.md) — Scientist-Bench also anchors each task to a real paper, but scores the final manuscript in pairwise LLM review rather than scoring idea, code, and report separately.
