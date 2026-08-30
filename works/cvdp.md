# CVDP (2025)

> **English** | [简体中文](../zh/works/cvdp.md)

> **First appeared:** 2025-06-17 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2506.14074)

## Overview

CVDP (Comprehensive Verilog Design Problems) is NVIDIA's next-generation benchmark for evaluating LLMs and agents on RTL design and verification: 783 problems across 13 task categories — RTL generation, verification, debugging, specification alignment, and technical Q&A — in both non-agentic and agentic formats, on which state-of-the-art models achieve no more than 34% pass@1 on code generation.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.14074>
- **Code:** <https://github.com/NVlabs/cvdp_benchmark>
- **Dataset:** <https://huggingface.co/datasets/nvidia/cvdp-benchmark-dataset>
- **Venue:** arXiv preprint (cs.LG), 2025

## Summary

CVDP consolidates the fragmented RTL-benchmark landscape into one comprehensive suite: 783 problems across 13 task categories spanning RTL generation, verification, debugging, specification alignment, and technical Q&A. Crucially, each problem exists in both a non-agentic format (single-shot, fixed input/output) and an agentic format (multi-step, tool- and repository-interacting), so the same task measures both a model and an agent. State-of-the-art models reach no more than 34% pass@1 on code generation, with agentic tasks particularly challenging. The framework runs on a Docker-based open-source simulation image (cocotb, Icarus Verilog, Yosys, Verilator), withholds reference solutions to limit contamination, and has been adopted by the Si2 LLM Benchmarking Coalition.

## Tasks

783 problems / 13 categories (RTL generation, verification, debugging, specification alignment, technical Q&A) in non-agentic and agentic formats; both static generation and interactive tool/repo-using agents.

## Domains

Electrical Engineering — digital design and verification: comprehensive RTL design, debugging, and verification.

## Evaluation

- pass@1, scored with open-source tools and model-scoring infrastructure in a containerized simulation environment.
- **Reported.** State-of-the-art models achieve no more than 34% pass@1 on code generation; agentic tasks are particularly challenging.

## Typical Duration

Single-shot for non-agentic tasks; multi-step tool/repo-interacting episodes for agentic tasks.

## Main Contribution

A single comprehensive RTL benchmark that spans design, verification, and debugging and evaluates both models and agents on identical tasks — with contamination controls and industrial adoption.

## Key Design Ideas

- Dual non-agentic/agentic formats measure the same task as a model and as an agent.
- Withheld reference solutions plus a partial-release policy limit training contamination.
- A containerized open-source EDA stack makes evaluation reproducible.

## Strengths

- The broadest RTL benchmark by task-category coverage, from NVIDIA, with public framework and dataset.
- The low SOTA ceiling (≤34% pass@1) leaves clear, measurable headroom.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); no venue is stated in arXiv metadata (an ICLAD'25 attribution is unverified). The public release omits some datapoints and withholds reference solutions.

## Related Works

- [VerilogEval](./verilogeval.md) — Also RTL generation evaluation, narrower and simulation-scored.
- [FVEval](./fveval.md) — Also hardware verification evaluation, focused on formal verification.
- [RTLLM](./rtllm.md) — Also design-level RTL generation, without the verification and agentic scope.
