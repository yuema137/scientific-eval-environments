# HLS-Eval (2025)

> **English** | [简体中文](../zh/works/hls-eval.md)

## Overview

HLS-Eval is a benchmark and framework for evaluating LLMs on high-level synthesis design tasks: 94 unique designs with natural-language descriptions and testbenches, over two tasks — generating HLS code from natural language and performing HLS-specific edits to optimize performance and hardware efficiency — scored by parseability, compilability, runnability, and synthesizability on Vitis HLS.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.12268>
- **Code:** <https://github.com/stefanpie/hls-eval>
- **Venue:** ICLAD 2025 (per the official repository; arXiv metadata carries no venue)

## Summary

High-level synthesis compiles C/C++ into hardware, and its quality depends on code written with hardware in mind. HLS-Eval evaluates whether LLMs can do that: 94 designs (from standard HLS benchmarks and novel sources), each with a natural-language description and testbench, over two tasks — generate HLS code from the description, and apply HLS-specific edits to optimize performance and hardware efficiency, reflecting the iterative HLS design cycle. Outputs are graded on four hardware-grounded metrics on Vitis HLS: parseability, compilability, runnability, and synthesizability, with pass@k reported.

## Tasks

Two tasks over 94 HLS designs: natural-language-to-HLS code generation, and HLS-specific optimization edits; framework-harnessed generation, evaluated on Vitis HLS.

## Domains

Electrical Engineering — high-level synthesis: LLM generation and optimization of synthesizable hardware code.

## Evaluation

- Four metrics — parseability, compilability, runnability, synthesizability — plus pass@k, evaluated on Vitis HLS.
- **Reported.** Open-source LLMs are evaluated; specific scores are in the paper body (TODO(reference)).

## Typical Duration

Single-shot generation or edit per design; tool-evaluated.

## Main Contribution

Bringing HLS — a distinct hardware-code discipline — into LLM evaluation, with hardware-grounded metrics that go beyond "does it compile" to "does it synthesize."

## Key Design Ideas

- The four-metric ladder (parse → compile → run → synthesize) grades hardware-readiness, not just text.
- The optimization-edit task captures the iterative HLS refinement loop, not just first-draft generation.
- Real Vitis HLS evaluation keeps results tied to an industrial toolchain.

## Strengths

- Covers HLS, which pure Verilog/RTL benchmarks omit, with an open framework.
- Synthesizability grading targets the property that actually matters for hardware.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the ICLAD 2025 venue is a repository claim, not in arXiv metadata. Per-model scores are in the paper body.

## Related Works

- [VerilogEval](./verilogeval.md) — Also LLM hardware-code generation, at the RTL/Verilog level rather than HLS.
- [CVDP](./cvdp.md) — Also multi-task hardware design evaluation, spanning generation and verification.
- [RTLLM](./rtllm.md) — Also design-level hardware generation from natural language.
