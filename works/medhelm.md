# MedHELM (2025)

> **English** | [简体中文](../zh/works/medhelm.md)

## Overview

MedHELM extends Stanford CRFM's Holistic Evaluation of Language Models (HELM) to medical tasks. It combines a clinician-validated taxonomy of medical work with a broad benchmark suite and an LLM-jury evaluation methodology whose agreement against clinician ratings is explicitly measured.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.23802>

## Summary

MedHELM argues that ad-hoc medical benchmarks miss the breadth of clinical work. It proposes a clinician-validated taxonomy paired with an aggregation across 35 benchmarks (17 existing + 18 newly formulated), and introduces an LLM-jury evaluation methodology whose agreement against clinician ratings is reported explicitly.

## Tasks

121 tasks organized under a clinician-validated taxonomy of 5 categories and 22 subcategories, developed with 29 clinicians.

## Domains

Medical / clinical tasks. Reported category examples include Clinical Note Generation and Administration & Workflow.

## Evaluation

- Aggregation across 35 benchmarks (17 existing + 18 newly formulated).
- LLM-jury evaluation methodology.
- Reported clinician agreement: ICC = 0.47; outperforms automated baselines including ROUGE-L and BERTScore.
- 9 frontier LLMs tested, including DeepSeek R1, o3-mini, and Claude 3.5 Sonnet.
- Reported domain ranges: Clinical Note Generation 0.73–0.85; Administration & Workflow 0.53–0.63.
- Cost-adjusted comparison: Claude 3.5 Sonnet delivers comparable results at approximately 40% lower computational cost.

## Typical Duration

Per-task evaluation; specific horizon not stated in the abstract.

## Main Contribution

A clinician-validated medical evaluation taxonomy paired with a 35-benchmark suite, plus an LLM-jury evaluation methodology whose agreement with clinician ratings (ICC = 0.47) is explicitly measured.

## Key Design Ideas

- Clinician-designed taxonomy: 5 categories → 22 subcategories → 121 tasks, developed with 29 clinicians.
- Aggregated evaluation across 35 benchmarks (17 existing + 18 newly formulated).
- LLM-jury as the primary scoring mechanism, validated against clinician ratings.
- Cost-adjusted frontier-model comparison.

## Strengths

- Direct clinician grounding of the taxonomy.
- Broad benchmark aggregation reduces reliance on any single scoring paradigm.
- Explicit clinician-agreement number (ICC = 0.47) makes the LLM-jury methodology assessable.
- Cost-adjusted model comparisons surface a distinct axis of practical usability.

## Limitations

- Repository note: LLM-jury agreement with clinicians is moderate (ICC = 0.47); rankings derived from this methodology inherit that reliability bound.
- Repository note: Domain-scoped to medicine — the taxonomy does not directly transfer to other scientific domains.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also scientific-domain benchmarking, but centered on executable computational workflows across five scientific domains rather than clinician-validated task taxonomies.
