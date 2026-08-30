# CODE2BENCH (2025)

> **English** | [简体中文](../zh/works/code2bench.md)

## Overview

CODE2BENCH is a dynamic benchmark-construction framework that mines recent real-world code repositories and generates Python and Java tasks under a 100% branch-coverage quality gate.

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

N/A — general code-generation benchmark construction; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2508.07180>
- **Project:** <https://code2bench.github.io/>
- **Venue:** arXiv preprint (2025; revised 2026)

## Summary

CODE2BENCH combines two forms of scaling: continuously refreshing task sources from recent repositories and increasing test rigor through property-based testing. Scope-graph analysis classifies dependencies, and generated suites must achieve 100% branch coverage before admission. CODE2BENCH-2509 contains native Python and Java tracks drawn from 220 Python and 189 Java repositories and is evaluated on ten models.

## Tasks

Three tracks: self-contained Python, weakly self-contained Python requiring repository APIs, and self-contained Java. Instances are generated from recent repository functions and paired with property-based tests; exact per-track counts are reported in the paper's dataset table.

## Domains

Software engineering and code generation. The contribution is benchmark construction rather than a scientific application task, so it is not added to the domain axis.

## Evaluation

Pass@1 under generated property-based tests that pass a 100% branch-coverage gate. Diagnostic fingerprints separate compile, runtime, logic, dependency, and near-pass behavior; 6.94% of SC-Python submissions pass simpler tests but fail the high-rigor suite.

## Typical Duration

Single code-generation submission per task for Pass@1; no common wall-clock budget is stated.

## Main Contribution

A reproducible construction pipeline that treats source freshness and verifier rigor as two independent benchmark-validity requirements.

## Key Design Ideas

- Mine recent repositories instead of relying on a fixed problem bank.
- Use scope graphs to distinguish self-contained from dependency-bearing functions.
- Generate property-based tests and require full branch coverage.
- Publish failure fingerprints rather than only aggregate pass rates.

## Strengths

- Dynamic source acquisition directly reduces dependence on stale static tasks.
- The coverage gate makes test adequacy an explicit admission criterion.
- Native Python and Java tracks expose language-ecosystem effects.

## Limitations

- Recency reduces contamination risk but cannot prove absence from model training data.
- Branch coverage does not guarantee semantic completeness of a test suite.
- The benchmark targets function-level code generation rather than full agent workflows.

## Related Works

- [ResearchCodeBench](./researchcodebench.md) — uses recent research papers to construct contamination-aware implementation tasks.
- [FrontierCode](./frontiercode.md) — couples live coding tasks with explicit contamination detection.
- [LiveCodeBench](./livecodebench.md) — continuously refreshes competitive-programming evaluation from new contests.
