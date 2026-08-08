# Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap (2026)

> **English** | [简体中文](../zh/works/ara-survey.md)

## Overview

A survey of autonomous research agents ('AI scientists') centered on the verification gap: the distance between systems' ability to complete research tasks and the field's ability to verify their claims. From 125 screened candidates, 35 works are included, 26 with full-text coding across seven audit dimensions.

## Topics

- [Survey](../topics/survey.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.05179>
- **Venue:** arXiv preprint (cs.CY, cs.AI), 2026

## Summary

The survey codes systems along seven audit dimensions — lifecycle stage, autonomy level, evaluation method, released artifacts, human-in-the-loop points, novelty verification, and result-selection disclosure. It finds that 83% of systems release code while only 38% release seeds or execution traces and only 38% report any novelty-verification method; among nine closed-loop L4 systems, seven verify by mechanical reruns and one is author-claimed without external check; no LLM-era system in the corpus demonstrates an externally validated in-loop oracle. A reviewer checklist operationalizes the audit.

## Tasks

N/A — survey paper. Corpus: 125 candidate works screened, 35 included, 26 with full-text coding (24 runnable systems, 2 position/study papers).

## Domains

Autonomous research agents across scientific fields; the survey itself is field-agnostic.

## Evaluation

- N/A — survey paper. The contribution is the seven-dimension audit protocol and the coded corpus.
- **Reported.** 83% of systems release code; 38% release seeds or execution traces; 38% report any novelty-verification method; no LLM-era system demonstrates an externally validated in-loop oracle.

## Typical Duration

N/A — survey paper.

## Main Contribution

Names and quantifies the verification gap in autonomous research agents, and converts the audit into a reusable reviewer checklist.

## Key Design Ideas

- Verification artifacts (seeds, traces, oracles) are audited separately from headline capability claims.
- Autonomy levels are mapped against lifecycle stages, so 'closed-loop' claims can be checked per stage.
- Result-selection disclosure is treated as a first-class audit dimension.

## Strengths

- Grounds a widely felt concern in coded, per-system evidence.
- The reviewer checklist makes the audit repeatable by others.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — Also surveys agent evaluation broadly; this survey audits the research-agent subfield for verifiability.
- [EXP-Bench](./exp-bench.md) — A benchmark instantiating the verification concern: full-experiment reproduction with executable checks.
- [ResearchClawBench](./researchclawbench.md) — A benchmark whose hidden-paper design responds directly to the verification problem the survey documents.
