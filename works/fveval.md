# FVEval (2024)

> **English** | [简体中文](../zh/works/fveval.md)

> **First appeared:** 2024-10-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2410.23299)

## Overview

FVEval is an NVIDIA benchmark for understanding language-model capabilities in formal verification of digital hardware, across three sub-tasks — generating SystemVerilog assertions from natural language, generating them from a testbench/design, and design-level verification reasoning — validated with the Cadence Jasper formal tool.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.23299>
- **Code:** <https://github.com/NVlabs/FVEval>
- **Venue:** arXiv preprint (cs.AR), 2024

## Summary

Formal verification is where hardware correctness is actually proven, and FVEval measures whether LLMs can participate. It defines three sub-tasks at different levels: NL2SVA-Machine and NL2SVA-Human generate SystemVerilog assertions from natural language, and Design2SVA generates assertions/testbenches from a design. Generated artifacts are checked with the Cadence Jasper formal tool rather than by heuristics, and the benchmark ships pre-generated datasets and evaluation code under an open license.

## Tasks

Three formal-verification sub-tasks: NL2SVA-Machine, NL2SVA-Human (natural-language-to-SVA), and Design2SVA (design-to-assertions/testbench); static generation validated by a formal tool.

## Domains

Electrical Engineering — formal verification of digital hardware: SystemVerilog assertion and testbench generation.

## Evaluation

- Correctness of generated assertions/testbenches verified with the Cadence Jasper formal tool.
- **Reported.** LLM capability varies across the three sub-tasks; total problem counts and headline numbers are TODO(reference) — not stated in the abstract.

## Typical Duration

Single-shot generation per task; verification is tool-checked.

## Main Contribution

A formal-tool-grounded benchmark decomposing hardware verification into distinct LLM capabilities — machine-style vs. human-style assertion generation vs. design-level reasoning.

## Key Design Ideas

- Formal-tool checking (Jasper) makes correctness a proof, not a heuristic.
- Three sub-tasks separate translation difficulty from design understanding.
- Open datasets plus evaluation code make the benchmark reproducible.

## Strengths

- Grounds evaluation in industrial formal verification, not simulation heuristics.
- Public NVlabs release with pre-generated datasets and harness.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); no venue is stated in arXiv metadata, and per-task problem counts and scores are in the paper body.

## Related Works

- [AssertionBench](./assertionbench.md) — Also LLM assertion generation, benchmarked against formally verified references.
- [CVDP](./cvdp.md) — Also RTL verification alongside design, in a broader agentic benchmark.
- [VerilogEval](./verilogeval.md) — Also LLM Verilog evaluation, on functional code generation.
