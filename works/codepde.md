# CodePDE (2025)

> **English** | [简体中文](../zh/works/codepde.md)

> **First appeared:** 2025-05-13 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.08783)

## Overview

CodePDE is an inference framework for LLM-driven PDE solver generation: PDE solving is framed as code generation, and the framework's evaluation study — spanning reasoning, debugging, self-refinement, and test-time scaling on representative PDE problems — functions as the reference evaluation for LLM-generated numerical solvers.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.08783>
- **Code:** <https://github.com/LithiumDA/CodePDE>
- **Venue:** TMLR

## Summary

Instead of training surrogates, CodePDE asks LLMs to write the numerical solver itself, then measures the generated solvers' accuracy on representative PDE problems. The framework systematically evaluates the capabilities critical to solver generation — reasoning about the discretization, debugging failing code, self-refinement over iterations, and test-time scaling — and reports that LLMs can achieve strong performance across a range of representative PDE problems, while analysis identifies where solver generation still fails.

## Tasks

PDE-solver code generation over representative PDE problems, with iterative refinement; task and model counts are TODO(reference).

## Domains

Numerical solution of partial differential equations for modeling physical systems.

## Evaluation

- Accuracy of generated solvers on representative PDE problems, with axes for reasoning, debugging, self-refinement, and test-time scaling; specific metric definitions are TODO(reference).
- **Reported.** LLMs achieve strong performance across a range of representative PDE problems.

## Typical Duration

Generate-and-refine solver episodes per problem; not an interactive environment.

## Main Contribution

Repositioned PDE solving as an LLM code-generation problem — the solver, not the solution field, is the generated artifact — and established the evaluation axes (reasoning, debugging, refinement, scaling) subsequent solver-generation benchmarks adopt.

## Key Design Ideas

- Generating the solver preserves interpretability and numerical guarantees that end-to-end surrogates give up.
- Refinement and test-time scaling are treated as measured capabilities, not implementation details.
- Solutions are checked against reference solutions rather than judged.

## Strengths

- The founding evaluation for the LLM-writes-the-solver paradigm.
- TMLR-published with released code.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- Repository note: CodePDE is an inference framework whose built-in evaluation study serves as its benchmark; there is no fixed task suite of record in the verified sources.

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — The fixed-suite successor: 645 solver-generation instances with staged executability/accuracy/efficiency checks.
- [CFDLLMBench](./cfdllmbench.md) — Also evaluates solver coding with physics-grounded verification, specialized to CFD.
- [MooseBench](./moosebench.md) — Also verifies LLM-generated simulation code beyond execution, via PDE-level reconstruction.
