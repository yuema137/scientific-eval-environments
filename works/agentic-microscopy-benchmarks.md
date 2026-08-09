# Agentic Self-Driving Microscopy Benchmarks (2026)

> **English** | [简体中文](../zh/works/agentic-microscopy-benchmarks.md)

## Overview

An industry study (Carl Zeiss Research Microscopy Solutions) pairing a benchmark-and-trace-logging framework for agentic self-driving microscopy with a meta-finding: 53 benchmark tests across 105 agent configurations support qualification, regression testing, and diagnosis — but do not predict performance on unseen tasks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Laboratory & Instrument Control](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.05266>
- **Code:** <https://github.com/natertott/agentic_microscopy_benchmarks_XRM>
- **Venue:** arXiv preprint (cs.AI, cond-mat.mtrl-sci, cs.LG), 2026

## Summary

The study runs 1,949 individual test runs and 49,109 RAG retrievals over 53 microscopy benchmark tests, varying one-, two-, and three-agent graph topologies, five LLMs, and RAG and context parameters, with full trace logging plus latency, token-use, cost, and failure-mode comparisons. Its central negative result: surrogate models trained on agent architecture and test results did not reliably predict an agent's performance on new, unseen tasks — the heterogeneous test suite supports qualification but not a task-independent global configuration model.

## Tasks

53 microscopy benchmark tests for instrument-controlling agents, run across 105 agent configurations (agent-graph topology × five LLMs × RAG/context parameters), totaling 1,949 test runs.

## Domains

Microscopy and materials characterization instrumentation (cond-mat.mtrl-sci); self-driving scientific instruments.

## Evaluation

- Benchmark tests with full trace logging; comparisons of latency, token use, cost, and failure mode across configurations.
- **Reported.** Surrogate models trained on agent architecture and test results did not reliably predict performance on new, unseen tasks; benchmarks are useful for qualification, regression testing, diagnosis, and direct comparison.

## Typical Duration

Instrument-control agent runs per test; per-run budgets are TODO(reference).

## Main Contribution

An empirical warning for agent benchmarking itself: even a substantial, instrumented test suite in one domain does not yield a task-independent model of which agent configuration will work next.

## Key Design Ideas

- Configuration space is explored systematically (topology × model × RAG/context), not anecdotally.
- Trace logging makes every run auditable and failure modes classifiable.
- Benchmark validity is itself treated as an empirical question, tested via surrogate prediction on held-out tasks.

## Strengths

- Rare industrial-scale evidence (1,949 runs) on how far benchmark scores generalize.
- Grounded in real instrument-control workloads rather than synthetic tasks.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- Repository note: the paper names no branded benchmark; this card uses a descriptive title after the paper's own phrasing.

## Related Works

- [AFMBench](./afmbench.md) — Also benchmarks agents on a real microscopy instrument, with a named error taxonomy.
- [Harness-Bench](./harness-bench.md) — Also finds measured capability is a property of the configuration, not the model alone.
- [EnvTrace](./envtrace.md) — Also evaluates instrument-control behavior via execution traces, at synchrotron beamlines.
