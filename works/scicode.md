# SciCode (2024)

> **English** | [简体中文](../zh/works/scicode.md)

## Overview

SciCode is a research coding benchmark curated by scientists: 80 challenging main problems decomposed into 338 subproblems, built with input from scientists and AI researchers in 16 natural-science subfields spanning mathematics, physics, chemistry, biology, and materials science.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.13168>
- **Code:** <https://github.com/scicode-bench/SciCode>
- **Dataset:** <https://huggingface.co/datasets/SciCode1/SciCode>
- **Project:** <https://scicode-bench.github.io/>
- **Venue:** NeurIPS 2024 Datasets and Benchmarks (per the official repository)

## Summary

SciCode's problems come from real research: each main problem naturally factorizes into subproblems involving knowledge recall, reasoning, and code synthesis, with optional scientific-background descriptions controlling how much domain knowledge is supplied. Evaluation runs against scientist-annotated gold-standard solutions and test cases. In the most realistic setting, the best-performing model tested, Claude 3.5 Sonnet, solves only 4.6% of the main problems.

## Tasks

80 main research-coding problems decomposed into 338 subproblems across 16 natural-science subfields; each subproblem mixes knowledge recall, reasoning, and code synthesis, with optional background descriptions.

## Domains

Sixteen natural-science subfields with mathematics, physics, chemistry, biology, and materials science named as the main domains.

## Evaluation

- Execution against scientist-annotated gold-standard solutions and test cases, at subproblem and main-problem level.
- **Reported.** Claude 3.5 Sonnet, the best-performing model tested, solves only 4.6% of main problems in the most realistic setting.

## Typical Duration

Multi-subproblem code-generation episodes per main problem; not an interactive agent setting.

## Main Contribution

Scientist-curated research code as the evaluation object, with a decomposition that shows models failing to compose subproblem competence into full research solutions.

## Key Design Ideas

- Scientists author and annotate the problems, so difficulty reflects research practice rather than exam convention.
- The main-problem/subproblem factorization separates composition failures from unit failures.
- Optional background descriptions make supplied domain knowledge an experimental variable.

## Strengths

- Gold-standard solutions and tests from working scientists across 16 subfields.
- The 4.6% realistic-setting score set an early, credible research-coding baseline.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The per-subfield distribution of problems is not stated in those sources.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also expert-validated scientific code tasks from real research, unified to executable Python programs.
- [NatureBench](./naturebench.md) — Also holds coding agents to published research standards, via SOTA-matching.
- [MDArena](./mdarena.md) — Also research-derived scientific computing, containerized in one simulation modality.
