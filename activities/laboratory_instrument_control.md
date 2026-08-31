# Laboratory & Instrument Control

> **English** | [简体中文](../zh/activities/laboratory_instrument_control.md) · [← All activities](./README.md)

## Definition

Evaluates the agent on executing or controlling experimental systems — laboratory robotics, instrument, microscope, and beamline control, experimental automation, and control code whose correctness is defined by physical system behaviour.

## Scope

Includes real-hardware operation and high-fidelity digital twins that explicitly represent instrument or laboratory operation, and control code whose correctness is defined through physical system behaviour. It excludes generic software tool use and generic robot manipulation that is not laboratory or instrument operation.

## Task Patterns

This activity appears in two distinct forms. The first is direct operation of a real instrument: an agent drives physical hardware through a vendor API across a full experimental workflow, and correctness is judged by what happens on the machine. [AFMBench](../works/afmbench.md) exemplifies this, holding LLM agents to physical execution on a real Nanosurf DriveAFM across 100 tasks from experimental design to analysis, while [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md) instruments agentic microscopy control across many agent configurations with full trace logging.

The second form evaluates instrument-control *code* against a high-fidelity digital twin rather than live hardware, where the code's meaning is its physical behaviour over time. [EnvTrace](../works/envtrace.md) runs candidate control code against a synchrotron beamline control-logic digital twin and scores semantic equivalence by aligning execution traces, replacing stateless unit tests with trace-level comparison. Across both forms, the recurring emphasis is temporal, stateful correctness and behaviour-defined success that static QA or unit testing cannot capture.

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AFMBench | 2025 | LLM agents operate a real atomic force microscope end-to-end | 100 curated tasks on Nanosurf DriveAFM via Python API, run 3x | Task completion; best model 65% overall, 23.3% on doc+analysis | [card](../works/afmbench.md) |
| EnvTrace | 2025 | Evaluate LLM-generated beamline instrument-control code | Trace alignment vs synchrotron beamline digital twin; over 30 LLMs | Multi-faceted functional-correctness score; top models near human-level | [card](../works/envtrace.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | Benchmark and trace-log agentic self-driving microscopy control | 53 tests x 105 agent configs, 1,949 runs (Zeiss study) | Qualification/regression support; no task-independent config prediction | [card](../works/agentic-microscopy-benchmarks.md) |

## Related Works

- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
- [EnvTrace](../works/envtrace.md)
- [AFMBench](../works/afmbench.md)
