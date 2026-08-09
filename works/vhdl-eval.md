# VHDL-Eval (2024)

> **English** | [简体中文](../zh/works/vhdl-eval.md)

## Overview

VHDL-Eval is a framework for evaluating LLMs on VHDL code generation: 202 problems assembled by translating Verilog evaluation problems into VHDL and aggregating publicly available VHDL problems, evaluated under zero-shot, in-context learning, and parameter-efficient fine-tuning.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.04379>
- **Venue:** LAD 2024 (IEEE International Workshop on LLM-Aided Design)

## Summary

Verilog dominates LLM hardware benchmarks, but VHDL is the other major HDL, and VHDL-Eval fills the gap: 202 problems built by translating a collection of Verilog evaluation problems to VHDL and aggregating publicly available VHDL challenges, each with self-verifying testbenches. LLMs are evaluated under zero-shot generation, in-context learning, and parameter-efficient fine-tuning, and the paper's key finding is that supervised fine-tuning specifically for VHDL is necessary — general models transfer poorly.

## Tasks

202 VHDL code-generation problems (Verilog-translated plus aggregated public VHDL), each with self-verifying testbenches; static generation under zero-shot, ICL, and PEFT settings.

## Domains

Electrical Engineering — digital design: VHDL code generation.

## Evaluation

- Functional correctness via self-verifying testbenches, across zero-shot, in-context-learning, and PEFT settings.
- **Reported.** The results argue for the necessity of VHDL-specific supervised fine-tuning; the abstract gives no single numeric pass rate.

## Typical Duration

Single-shot VHDL generation per problem; testbench-verified.

## Main Contribution

Extending LLM hardware-code evaluation to VHDL — and documenting that Verilog-centric models do not transfer, so VHDL needs dedicated fine-tuning.

## Key Design Ideas

- Translating Verilog problems to VHDL bootstraps a benchmark where few existed.
- Self-verifying testbenches make correctness checkable without manual grading.
- Comparing zero-shot/ICL/PEFT isolates where VHDL competence has to come from.

## Strengths

- The reference VHDL code-generation benchmark, addressing an underserved HDL.
- The fine-tuning-necessity finding is directly actionable for VHDL tooling.

## Limitations

- Repository note: card compiled from the arXiv abstract and Comments (August 2026); LAD'24 is confirmed via Comments. No official code URL is verifiable from the arXiv page.

## Related Works

- [VerilogEval](./verilogeval.md) — The Verilog counterpart whose problems VHDL-Eval translates.
- [RTLLM](./rtllm.md) — Also HDL design generation from specifications, in Verilog.
- [HLS-Eval](./hls-eval.md) — Also hardware-code generation evaluation, at the high-level-synthesis layer.
