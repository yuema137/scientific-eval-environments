# MatTools (2025)

> **English** | [简体中文](../zh/works/mattools.md)

## Overview

MatTools benchmarks large language models on materials-science tools: 69,225 QA pairs testing understanding of the pymatgen codebase plus a real-world suite of 49 tasks (138 subtasks) requiring the model to generate and execute functional Python code to answer materials-property questions.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.10852>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2025

## Summary

Using materials software correctly is its own skill, and MatTools measures it in two parts: a 69,225-pair QA benchmark derived from the pymatgen codebase and documentation (does the model understand the tools?), and a real-world benchmark of 49 tasks and 138 subtasks where the model must write and run functional Python to compute an answer. Across models the findings run against intuition: generalist models outperform specialists, larger models do better on AI-related tasks ("AI knows AI"), and simpler approaches often beat elaborate ones ("less is more").

## Tasks

Two components: 69,225 tool-comprehension QA pairs over pymatgen, and 49 real-world tasks (138 subtasks) requiring functional Python code generation and execution; code-generation benchmark with execution, not a multi-turn agent loop.

## Domains

Materials science — computational-materials tool use: understanding and programming the pymatgen library for property calculations.

## Evaluation

- Tool-comprehension QA accuracy plus real-world code-generation success (generate-and-execute).
- **Reported.** Generalist models outperform specialists; larger models do better on AI-related tasks; simpler approaches often outperform complex ones. No single headline number in the abstract.

## Typical Duration

Per-question QA and per-task code-generation episodes; execution-verified.

## Main Contribution

A two-level measurement of whether LLMs can actually operate materials software — separating knowing the tools from writing runnable code that uses them.

## Key Design Ideas

- Splitting comprehension from code generation localizes where tool use fails.
- Real pymatgen tasks with execution make correctness objective.
- The generalist-beats-specialist finding challenges the domain-fine-tuning reflex.

## Strengths

- Large comprehension set (69,225 pairs) plus execution-verified real tasks.
- Actionable meta-findings for building materials coding assistants.

## Limitations

- Repository note: card compiled from the arXiv abstract and Comments (August 2026); no official code/dataset URL is present on the arXiv page, and per-model numbers are in the paper body. No venue is stated in arXiv metadata.

## Related Works

- [MatViX](./matvix.md) — Also structured materials computation by models, via extraction rather than tool code.
- [LLM4Mat-Bench](./llm4mat-bench.md) — Also LLMs over materials properties, by direct prediction rather than tool-use.
- [AutoDFT / VASPBench](./vaspbench.md) — Also LLM agents driving materials computation, at the DFT-workflow level.
