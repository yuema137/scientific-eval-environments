# VerilogEval (2023)

> **English** | [简体中文](../zh/works/verilogeval.md)

> **First appeared:** 2023-09-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2309.07544)

## Overview

VerilogEval is the canonical benchmark for evaluating LLMs on Verilog code generation: 156 problems from the HDLBits instructional website, with functional correctness checked automatically by simulating generated RTL against golden solutions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2309.07544>
- **Code:** <https://github.com/NVlabs/verilog-eval>
- **Venue:** ICCAD 2023 (invited)

## Summary

VerilogEval established functional-correctness evaluation for LLM hardware code generation: 156 HDLBits problems on which a model generates Verilog RTL, checked by simulating the output against a golden reference and reporting pass@k. The follow-up "Revisiting VerilogEval" (arXiv 2408.11053) extends the infrastructure with a specification-to-RTL task, in-context learning, and automatic failure classification, reporting GPT-4o at a 63% pass rate on spec-to-RTL. VerilogEval remains the reference point for RTL code-generation benchmarks.

## Tasks

156 HDLBits-derived Verilog problems; the LLM generates RTL from a problem description (code-completion in v1, plus specification-to-RTL in v2). Static generation scored by simulation.

## Domains

Electrical Engineering — digital design: Verilog RTL code generation.

## Evaluation

- Functional correctness by simulating generated RTL against a golden solution; pass@k.
- **Reported.** Supervised fine-tuning bootstrapping improves pass rates; the v2 paper reports GPT-4o at 63% on specification-to-RTL.

## Typical Duration

Single-shot RTL generation per problem; simulation-verified.

## Main Contribution

The founding functional-correctness benchmark for LLM Verilog generation, whose HDLBits-based design and pass@k protocol became the template for the RTL-codegen field.

## Key Design Ideas

- Simulation against golden solutions makes correctness functional, not textual.
- HDLBits sourcing gives graded, instructionally validated problems.
- The v2 spec-to-RTL task moves beyond code completion toward specification following.

## Strengths

- The de facto standard for RTL code-generation evaluation, with an actively maintained NVlabs release.
- Pass@k over simulation is objective and widely comparable.

## Limitations

- Repository note: card compiled from the arXiv abstract, Comments, and official repository (August 2026); ICCAD 2023 is confirmed via Comments and repo. Headline numbers cited here come from the v2 paper (2408.11053).

## Related Works

- [RTLLM](./rtllm.md) — Also Verilog generation from natural language, at full-design rather than HDLBits-problem scale.
- [RTL-Repo](./rtl-repo.md) — Also RTL generation, at repository scale with full cross-file context.
- [CVDP](./cvdp.md) — Also RTL evaluation, extended to verification and agentic formats.
