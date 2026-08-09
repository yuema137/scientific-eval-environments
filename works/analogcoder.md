# AnalogCoder (2024)

> **English** | [简体中文](../zh/works/analogcoder.md)

## Overview

AnalogCoder is the first training-free LLM agent for designing analog circuits through Python code generation, using a feedback-enhanced self-correcting flow and a reusable circuit tool library; it successfully designs 20 circuits — five more than standard GPT-4o — over a curated benchmark of analog circuit design tasks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.14918>
- **Code:** <https://github.com/laiyao1/AnalogCoder>
- **Venue:** AAAI 2025 (Oral) (per the official repository; arXiv metadata carries no venue)

## Summary

Analog circuit design resists the code-generation recipe that works for digital hardware, and AnalogCoder tackles it training-free: an LLM agent generates Python code that constructs analog circuits, iterates through a feedback-enhanced self-correcting flow with domain-specific prompts, and archives reusable modular sub-circuits in a tool library. Evaluated on a curated benchmark of analog design tasks (24 tasks in the official repository), it designs 20 circuits successfully — five more than standard GPT-4o.

## Tasks

Analog circuit design over a curated task set (24 tasks per the official repository); the agent generates and self-corrects Python code that builds circuits — agentic, not static QA.

## Domains

Electrical Engineering — analog circuit design: topology construction via code generation.

## Evaluation

- Pass@1 / Pass@5 ranked by number of tasks solved (official repository metrics).
- **Reported.** AnalogCoder designs 20 circuits successfully, five more than standard GPT-4o.

## Typical Duration

Iterative generate-and-self-correct episodes per circuit.

## Main Contribution

The first training-free agentic approach to analog circuit design — with a reusable task benchmark and a tool library that turns solved sub-circuits into building blocks.

## Key Design Ideas

- Training-free operation via feedback and domain prompts, avoiding scarce analog training data.
- A circuit tool library reuses solved sub-circuits as modular components.
- Python-code generation grounds designs in an executable, checkable representation.

## Strengths

- Beats GPT-4o on circuits-solved without any fine-tuning.
- Ships a reusable curated benchmark alongside the agent.

## Limitations

- Repository note: the paper's primary contribution is the AnalogCoder agent; the curated task set is its paired benchmark, and this card centers the benchmark. The 24-task count, Pass@k metric, and the AAAI 2025 Oral venue are stated by the official repository, not arXiv metadata.

## Related Works

- [AnalogXpert](./analogxpert.md) — Also an LLM agent for analog design, focused on topology synthesis with a larger benchmark.
- [MMCircuitEval](./mmcircuiteval.md) — Also analog-inclusive circuit evaluation, as multimodal QA rather than design.
- [ControlAgent / ControlEval](./controleval.md) — Also an LLM agent for an electrical-design task, in control systems.
