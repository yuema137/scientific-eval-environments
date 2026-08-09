# DA-Code (2024)

> **English** | [简体中文](../zh/works/da-code.md)

## Overview

DA-Code is an agent-oriented data-science code-generation benchmark: complex data wrangling, analytics, and code generation tasks set in a controllable, executable sandbox environment, where even the best current LLMs reach only 30.5% accuracy.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.07331>
- **Code:** <https://github.com/yiyihum/da-code>
- **Venue:** EMNLP 2024

## Summary

DA-Code targets the code an agent must actually write to do data science: challenging data wrangling, analytics, and modeling tasks that require grounding and planning, executed in a controllable Docker sandbox. Its paired DA-Agent baseline iteratively generates and runs data-science code. Despite outperforming existing frameworks, the best LLMs reach only 30.5% accuracy, marking substantial headroom in agentic data-science coding.

## Tasks

Agentic data-science coding tasks — data wrangling, analytics, and code generation — executed in a controllable Docker sandbox environment. Exact task counts are TODO(reference) — not stated in the abstract.

## Domains

AI & Machine Learning Research — data science: executable code generation for data wrangling and analytics.

## Evaluation

- Execution-based accuracy in a controllable sandbox environment, with the DA-Agent baseline.
- **Reported.** The best LLMs achieve only 30.5% accuracy, above existing frameworks but far from solved.

## Typical Duration

Iterative code-generate-and-execute episodes per task in the sandbox.

## Main Contribution

An execution-grounded data-science coding benchmark that demands real wrangling and analytics code, not just answers — with sandboxed verification.

## Key Design Ideas

- A controllable executable environment makes correctness a matter of running code, not judging text.
- Complex wrangling and analytics require grounding and planning, not single-shot generation.
- The DA-Agent baseline establishes a concrete reference for the task.

## Strengths

- Execution-grounded scoring over realistic data-science coding.
- Venue-verified (EMNLP 2024) with a public repository.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); exact task counts are not stated in the abstract and are marked TODO(reference).

## Related Works

- [DSBench](./dsbench.md) — Also data-science agent evaluation, spanning analysis and modeling tasks.
- [BLADE](./blade.md) — Also data-driven-science analysis, evaluated against expert ground truth.
- [ML-Bench](./ml-bench.md) — Also code-centric ML evaluation, at repository level.
