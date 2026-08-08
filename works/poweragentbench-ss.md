# PowerAgentBench-SS (2026)

> **English** | [简体中文](../zh/works/poweragentbench-ss.md)

## Overview

PowerAgentBench-SS benchmarks agentic AI in power-system steady-state studies: given public case data, action constraints, a tool API, and a validation budget, agents inspect a grid case, call simulators, screen contingencies, propose admissible mitigations, and produce an auditable evidence trail — while a hidden evaluator recomputes physical validity and scores the submitted report.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.18789>
- **Venue:** arXiv preprint (eess.SY), 2026

## Summary

Power-grid analysis is exactly the setting where an agent's self-reported success cannot be trusted: PowerAgentBench-SS therefore recomputes everything. Its pilot runs a DC thermal N-2 contingency search over IEEE 39-bus operating-point variants, with agents (three locally hosted Ollama models and one OpenAI API agent) interfacing through an LLM JSON-command adapter. The scoring vocabulary is unusually rich — submitted recall, evidence-backed recall, found recall, false-safe penalties, severity regret, residual violation score, action cost, tool-use efficiency, and workflow diagnostics — designed to show why solver-only or answer-only evaluation is insufficient.

## Tasks

Agentic steady-state grid studies: case inspection, tool selection, simulator calls, contingency screening, and mitigation proposals under a validation budget; pilot on IEEE 39-bus operating-point variants with DC thermal N-2 contingency search.

## Domains

Power-system operation and planning: steady-state analysis and N-2 contingency screening.

## Evaluation

- A hidden evaluator recomputes physical validity and scores the report: submitted/evidence-backed/found recall, false-safe penalties, severity regret, residual violation score, action cost, tool-use efficiency, workflow diagnostics.
- **Reported.** Solver-only or answer-only evaluation is shown to be insufficient; numeric results are TODO(reference).

## Typical Duration

Multi-step tool-calling studies per grid case under a validation budget.

## Main Contribution

Grid-agent evaluation where every claim is re-derived: the hidden evaluator's recomputation, false-safe penalties, and severity regret make unsupported "all clear" reports a scored failure mode.

## Key Design Ideas

- Recomputation-based grading assumes agents may submit unverified claims — and checks.
- False-safe penalties price the dangerous error class (missing a real violation) above the noisy one.
- The validation budget makes verification effort itself a rationed resource.

## Strengths

- The richest safety-oriented metric vocabulary among the engineering-agent benchmarks documented here.
- Reproducible pilot on standard IEEE test systems.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — Also distrusts agent self-reports and imposes external evaluation, in gravitational-wave science.
- [Frontier-Eng](./frontier-eng.md) — Also engineering optimization under hard feasibility constraints and budgets.
- [StructureClaw](./structureclaw.md) — Also safety-relevant engineering workflows with strict assertion-based verification.
