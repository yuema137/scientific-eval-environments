# RTLLM (2023)

> **English** | [简体中文](../zh/works/rtllm.md)

## Overview

RTLLM is an open-source benchmark for generating design RTL from natural-language instructions: 29 hand-crafted designs (expanded to 50 in v2.0) graded on three progressive goals — syntax, functionality, and design quality — paired with a "self-planning" prompting method that boosts GPT-3.5.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.05345>
- **Code:** <https://github.com/hkust-zhiyao/RTLLM>
- **Venue:** ASP-DAC 2024

## Summary

Where problem-set benchmarks test small snippets, RTLLM evaluates generation of complete design RTL from natural-language descriptions. Its 29 hand-crafted designs (the v2.0 release expands to 50, categorized as arithmetic, memory, control, and miscellaneous) are graded on three progressive goals — syntax correctness, functional correctness, and design quality. The paper also introduces "self-planning," a prompting method that significantly boosts GPT-3.5's performance on the benchmark.

## Tasks

29 hand-crafted RTL design tasks (v2.0: 50) generated from natural-language instructions; static generation graded on syntax, functionality, and design quality.

## Domains

Electrical Engineering — digital design: full-design RTL generation from natural language.

## Evaluation

- Three progressive goals — syntax, functionality, design quality — evaluated on GPT-3.5 with and without self-planning.
- **Reported.** Self-planning significantly boosts GPT-3.5; the abstract gives no single numeric pass rate.

## Typical Duration

Single-shot design generation per task.

## Main Contribution

An early design-level (not snippet-level) RTL benchmark with a graded goal ladder, plus the self-planning prompting method that became a widely cited baseline.

## Key Design Ideas

- Full designs, not HDLBits snippets, push generation toward realistic hardware.
- The syntax → functionality → quality ladder gives partial-credit structure.
- Self-planning demonstrates prompt structure matters as much as model choice.

## Strengths

- A foundational open RTL-generation benchmark, actively expanded (v1.1, v2.0).
- The three-goal grading separates "compiles" from "works" from "well-designed."

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); ASP-DAC 2024 is confirmed via the arXiv Journal-ref. The abstract's 29-design set corresponds to v1.0; the repository's v2.0 expands to 50 designs.

## Related Works

- [VerilogEval](./verilogeval.md) — Also LLM Verilog generation, at HDLBits-problem scale with pass@k.
- [RTL-Repo](./rtl-repo.md) — Also RTL generation, at repository scale with cross-file context.
- [CVDP](./cvdp.md) — Also RTL design evaluation, spanning verification and agentic formats.
