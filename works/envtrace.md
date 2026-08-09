# EnvTrace (2025)

> **English** | [简体中文](../zh/works/envtrace.md)

## Overview

EnvTrace is a simulation-based evaluation methodology for LLM-generated instrument-control code: instead of static unit tests, it executes candidate code against a digital twin of a synchrotron beamline and scores semantic equivalence by aligning execution traces.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Laboratory & Instrument Control](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** <https://arxiv.org/abs/2511.09964>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.PL), 2025

## Summary

EnvTrace starts from the observation that the behavior of physical systems cannot be fully captured by unit tests alone: correctness of control code is a property of what it does to the instrument over time. Candidate code runs against a beamline control-logic digital twin, and trace alignment produces a multi-faceted score for functional correctness across key behavioral dimensions. Over 30 LLMs were evaluated this way, with many top-tier models approaching human-level performance in rapid control-code generation; the digital twin also enables pre-execution validation of live experiments.

## Tasks

N/A — evaluation methodology, demonstrated on synchrotron beamline control-code generation; over 30 LLMs evaluated via trace alignment against a control-logic digital twin.

## Domains

Synchrotron beamline instrumentation — experimental-physics infrastructure control.

## Evaluation

- **Execution-trace alignment** against a digital twin, yielding a multi-faceted functional-correctness score across key behavioral dimensions.
- **Reported.** Many top-tier models approach human-level performance in rapid control-code generation.

## Typical Duration

N/A — evaluation of generated control code by simulated execution.

## Main Contribution

Replaces stateless unit-testing with trace-level semantic comparison for code whose meaning is its physical behavior, and shows a digital twin can double as a pre-execution safety gate for live experiments.

## Key Design Ideas

- Semantic code equivalence is judged by what the code does in simulation, not by its text or by static tests.
- The multi-faceted score decomposes correctness into behavioral dimensions instead of one pass bit.
- The same twin that evaluates offline can validate commands before they touch the real instrument.

## Strengths

- Evaluation object matches deployment reality for instrument control.
- Broad model coverage (30+ LLMs) for a specialized scientific setting.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [SysMoBench](./sysmobench.md) — Also scores artifacts by execution-grounded conformance (trace conformance among its gated metrics), rejecting LLM-judge scoring.
- [AFMBench](./afmbench.md) — Also evaluates agents against a real physical instrument, on an atomic force microscope.
- [Traxgen](./traxgen.md) — Also builds trajectory-level references deterministically, for ground-truth generation rather than execution alignment.
