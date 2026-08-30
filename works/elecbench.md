# ElecBench (2024)

> **English** | [简体中文](../zh/works/elecbench.md)

> **First appeared:** 2024-07-07 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2407.05365)

## Overview

ElecBench is a power-dispatch evaluation benchmark for large language models: eight LLMs assessed across general-knowledge and professional-business power scenarios on six core metrics — factuality, logicality, stability, security, fairness, and expressiveness — subdivided into 24 sub-metrics.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.05365>
- **Code:** <https://github.com/xiyuan-zhou/ElecBench-a-PowerDispatch-Evaluation-Benchmark-for-Large-LanguageModels>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

Power dispatch — keeping a grid stable, secure, and economical in real time — is a demanding decision domain, and ElecBench asks whether LLMs can reason about it. It splits scenarios into general knowledge and professional business and scores eight LLMs on a six-category framework (factuality, logicality, stability, security, fairness, expressiveness) subdivided into 24 sub-metrics, positioning itself as a standard benchmark for LLM applications in the power sector. The metric design reflects grid priorities: stability and security are first-class, not afterthoughts.

## Tasks

Power-dispatch evaluation across general-knowledge and professional-business scenarios; LLMs produce natural-language reasoning and decisions for grid operation, scored on the six-category / 24-sub-metric framework. Static evaluation.

## Domains

Energy Systems — power-system operation and dispatch: grid stability, security, and economic dispatch decisions.

## Evaluation

- Six core metrics (factuality, logicality, stability, security, fairness, expressiveness) subdivided into 24 sub-metrics, over eight LLMs.
- **Reported.** Eight LLMs evaluated across scenarios; ElecBench is positioned as a standard benchmark for the power sector.

## Typical Duration

Single-turn scenario responses; no interactive setting.

## Main Contribution

A domain-specific evaluation framework for LLMs in power-grid dispatch, whose metric taxonomy encodes what grid operation actually requires — stability and security alongside factual correctness.

## Key Design Ideas

- Stability and security as explicit metric categories reflect grid-operation priorities.
- Splitting general knowledge from professional business separates recall from operational competence.
- 24 sub-metrics turn a broad rubric into fine-grained diagnosis.

## Strengths

- Purpose-built metric framework for a safety-critical operational domain.
- Public test set covering eight LLMs.

## Limitations

- Repository note: card compiled from the arXiv abstract and paper PDF (August 2026); no venue is stated in arXiv metadata, and the code URL (from the PDF) was not independently confirmed live.

## Related Works

- [PowerAgentBench-SS](./poweragentbench-ss.md) — Also LLM evaluation for power-system studies, on steady-state contingency analysis with recomputed validity.
- [HydroAgent](./hydroagent.md) — Also an energy/environmental operational model evaluated for agentic use.
- [TeleQnA](./teleqna.md) — Also an electrical-domain knowledge benchmark, on telecommunications.
