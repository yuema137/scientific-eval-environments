# AssertionBench (2024)

> **English** | [简体中文](../zh/works/assertionbench.md)

## Overview

AssertionBench evaluates large language models on hardware assertion generation: 100 curated Verilog designs from OpenCores paired with formally verified assertions (from the GoldMine and HARM tools), measuring whether LLMs can infer functionally correct assertions for digital hardware.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2406.18627>
- **Venue:** NAACL 2025

## Summary

Assertions are the executable specification of what a hardware design must never violate, and writing them is expert, tedious work. AssertionBench turns assertion generation into a measurable LLM task: 100 Verilog designs from OpenCores, each with a set of formally verified assertions sourced from the GoldMine and HARM tools as ground truth. State-of-the-art LLMs are scored on the fraction of functionally correct assertions they produce, and the paper studies how the number of in-context exemplars affects quality — concluding there is significant room for improvement in LLM-based assertion generators.

## Tasks

Generate functionally correct SystemVerilog assertions for 100 OpenCores Verilog designs; static generation, evaluated against formally verified reference assertions.

## Domains

Electrical Engineering — digital hardware verification: assertion generation for Verilog designs.

## Evaluation

- Fraction of functionally correct assertions generated, with an analysis of in-context-exemplar count.
- **Reported.** Significant room for improvement across SOTA LLMs; no single headline number in the abstract.

## Typical Duration

Single-shot assertion generation per design; no interactive setting.

## Main Contribution

A formally-grounded benchmark for hardware assertion generation — measuring an LLM's grasp of design intent against machine-verified ground truth rather than surface plausibility.

## Key Design Ideas

- Formally verified reference assertions (GoldMine, HARM) give objective correctness.
- Real OpenCores designs anchor difficulty in practical hardware.
- Varying in-context exemplars isolates prompting effects from model capability.

## Strengths

- Venue-verified (NAACL 2025) with formally grounded correctness.
- Targets verification, the bottleneck of hardware design, rather than only code generation.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); no code URL is confirmed from the arXiv page, and the abstract gives no single headline accuracy figure.

## Related Works

- [FVEval](./fveval.md) — Also LLM hardware verification, spanning assertion generation and formal-verification reasoning.
- [VerilogEval](./verilogeval.md) — Also LLM evaluation on Verilog, on functional code generation rather than assertions.
- [CVDP](./cvdp.md) — Also RTL design and verification, in a comprehensive multi-task agentic benchmark.
