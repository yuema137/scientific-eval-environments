# CFDLLMBench (2025)

> **English** | [简体中文](../zh/works/cfdllmbench.md)

> **First appeared:** 2025-09-19 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2509.20374)

## Overview

CFDLLMBench is a three-tier benchmark suite for evaluating large language models on computational fluid dynamics, progressing from graduate-level CFD knowledge (CFDQuery) through numerical and physical reasoning in generated Python solvers (CFDCodeBench) to end-to-end OpenFOAM case configuration and execution (FoamBench).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.20374>
- **Project:** <https://openreview.net/forum?id=kTcH1MnkjY>
- **Code:** <https://github.com/NREL-Theseus/cfdllmbench>
- **Venue:** Journal of Data-centric Machine Learning Research (JDMLR), 2026

## Summary

CFDLLMBench argues that CFD is a uniquely demanding testbed for scientific LLM capability because it requires domain knowledge, numerical method selection, and long-context software operation at once — and that prior CFD-LLM evaluation stopped at whether generated OpenFOAM cases execute, without asking whether the resulting simulation is physically correct. The suite is structured as three progressively harder tiers probing distinct competencies, so a model's profile across tiers is the reported result rather than one aggregate number. Its evaluation framework grades on outcomes rather than implementation: solutions are scored on executability, relative numerical error against reference solutions, and numerical convergence under mesh and time-step refinement. The paper evaluates both zero-shot LLMs and agentic frameworks (MetaOpenFOAM, Foam-Agent) on the hardest tier.

## Tasks

Three components, 240 tasks total:

- **CFDQuery** — 90 multiple-choice questions curated by three domain experts, probing fluid mechanics, linear algebra, and numerical methods; adapted from web-scraped content and CFD lecture notes, and created exclusively for this benchmark.
- **CFDCodeBench** — 24 problems requiring the model to generate Python code that numerically solves a stated PDE. Each specifies the governing PDE, boundary and initial conditions, spatial and temporal domain, and target variables. Covers 1D and 2D, linear and nonlinear PDEs across fluid mechanics, thermal transport, and turbulence; reference solutions are closed-form analytical expressions or expert-authored Python implementations, averaging 70 lines of code per problem. Curated from public GitHub repositories and established sources, with experts authoring descriptions for the advanced problems.
- **FoamBench** — 126 OpenFOAM cases across more than 15 distinct geometric and physics scenarios, split into **Basic** (110 cases derived from 11 OpenFOAM tutorials by altering boundary conditions and parameters on a case-specific basis) and **Advanced** (16 expert-hand-crafted cases deliberately unlike the tutorials, requiring the model to select a turbulence model, create new geometry, and generate an appropriate mesh from a natural-language prompt). Prompts state the physical scenario, geometry, boundary conditions, parameters, turbulence model, timestep, solver, and save intervals.

## Domains

Computational fluid dynamics and adjacent scientific computing: fluid mechanics, thermal transport, turbulence modeling, numerical methods and discretization, mesh generation, and OpenFOAM workflow operation.

## Evaluation

- **CFDQuery.** Multiple-choice accuracy, reported as Success Rate.
- **CFDCodeBench.** Four metrics: **Executability** `M_exec` (binary, akin to pass@1); **Relative Error** `M_NMSE`, a normalized mean-squared-error percentage against the reference solution at final time, banded 1 / 0.5 / 0 at NMSE thresholds of ≤10%, 10–30%, and >30% — thresholds the paper grounds in engineering practice and an empirical sensitivity analysis; **Numerical convergence** `M_conv` (refine both spatial and temporal discretization, score 1 if the error decreases); and a stringent **Success Rate** counting only problems where all three score 1.
- **FoamBench.** **Executability** `M_exec`; **Folder and File Structure** `M_struct` (ROUGE similarity of the generated project structure against the reference case); **File Similarity** `M_file` (ROUGE over file contents); **Relative Error** `M_NMSE` as above. Success Rate here requires `M_exec` and `M_NMSE` both to score 1 — structure and file similarity are reported but do not gate success.
- **Outcome-based, not method-based.** A different but valid numerical algorithm (finite difference vs. finite volume) is accepted provided error stays under tolerance and the solution converges; the paper states the benchmark does not penalize algorithmic diversity. The paper argues code-similarity metrics are inadequate because simulation code varies widely while yielding equivalent solutions.
- **Setup.** OpenFOAM v10 throughout. CFDQuery and CFDCodeBench use zero-shot prompting. FoamBench is evaluated both zero-shot and under two agentic frameworks — MetaOpenFOAM and Foam-Agent — in three configurations (RAG + Reviewer, RAG without Reviewer, Reviewer without RAG) to isolate each component's contribution.
- **Reported.** Performance falls sharply across the tiers. On CFDQuery all closed-weight models do well, o3-mini leading at 92% while the open-weight model reaches 60%. Best CFDCodeBench Success Rate is about 14%. On FoamBench the best configuration — Foam-Agent with RAG and Reviewer on Claude Sonnet 3.5 — reaches 34% on Basic and 25% on Advanced. Zero-shot prompting collapses on the same tier: Sonnet 3.5 scores 0.045 Success Rate on Basic and 0.007 on Advanced. Comparing frameworks on Basic with Sonnet 3.5 under RAG + Reviewer, Foam-Agent reaches 0.336 Success Rate (`M_exec` 0.836, `M_NMSE` 0.427) against MetaOpenFOAM's 0.136 (`M_exec` 0.555, `M_NMSE` 0.173); removing the Reviewer drops Foam-Agent to 0.200. Sonnet 3.5's advantage carries a cost premium — an average of $6.56 per run versus $0.42 for GPT-4o (API pricing as of May 2025).

## Typical Duration

Not reported as wall-clock. Scale is instead indicated by cost and loop counts: the agentic FoamBench configurations average roughly 63k–379k total tokens per run depending on model and framework, with Foam-Agent averaging 2 reviewer loops for Sonnet 3.5 against 7 for the compared configuration. CFDCodeBench solutions average 70 lines of code; FoamBench requires generating a full OpenFOAM case directory and running the solver to completion.

## Main Contribution

The first benchmark to evaluate LLMs on CFD holistically across three tiers — graduate-level knowledge, numerical and physical reasoning, and practical simulation workflow automation — with an execution-based framework that scores physical accuracy and numerical convergence rather than executability or text similarity alone.

## Key Design Ideas

- Three progressively harder tiers isolate distinct competencies, so a strong knowledge score cannot mask an inability to run a simulation.
- Physical accuracy is graded numerically against reference solutions, with NMSE bands calibrated to engineering practice rather than chosen arbitrarily.
- Numerical convergence is an explicit metric: the solution is re-run under mesh and time-step refinement to check the error actually decreases — a property no code-similarity metric can detect.
- Success Rate is deliberately stringent (conjunction of all component metrics), separating partial competence from a genuinely usable simulation.
- The Advanced split is built to defeat retrieval: cases are unlike the tutorials, forcing genuine geometry and mesh construction rather than adaptation of a nearby exemplar.
- Agentic frameworks are evaluated as ablatable configurations (RAG, Reviewer) rather than as monolithic systems, so each component's contribution is measured.

## Strengths

- Grades what a CFD practitioner actually cares about — does the simulation run, is the answer physically right, does it converge — rather than whether files were produced.
- The Basic/Advanced split cleanly separates tutorial-adjacent competence from open-ended engineering, and the reported gap between them is large.
- Accepting any valid numerical method avoids penalizing legitimate implementation diversity.
- Reports cost alongside capability, surfacing that the strongest FoamBench model is over an order of magnitude more expensive per run.
- Substantial headroom remains at every tier beyond CFDQuery, and the suite is released under a BSD 3-Clause license with public code.

## Limitations

- The authors identify spatial reasoning as a major gap rather than a solved variable: in the Advanced `doubleSquare` case the prompt states obstacle locations precisely, yet the generated geometry and mesh are wrong, and the paper calls LLM geometric understanding a major area needing improvement.
- The authors note some evaluated models impose an internal context-window limit of roughly 8,000 tokens covering both prompt and output, and that o3-mini does not permit setting temperature (its default is undisclosed), so configurations are not fully uniform across models.
- Repository note: FoamBench Basic derives 110 cases from 11 tutorial cases by varying boundary conditions and parameters, so cases within a family are not independent; the Advanced split, which is hand-crafted to be unlike the tutorials, holds only 16 cases.
- Repository note: `M_struct` and `M_file` are ROUGE similarities against a specific reference case directory, so they reward resembling the reference layout — but by design they do not gate Success Rate, which depends only on execution and numerical error.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also evaluates scientific computational workflows in a controlled environment, with deterministic pytest verification rather than numerical-error and convergence grading.
- [ScienceAgentBench](./scienceagentbench.md) — Also grades scientific code execution against expert-validated references, across data-driven discovery tasks rather than a single simulation domain.
- [Stargazer](./stargazer.md) — Also scores iterative scientific model fitting with physical-consistency feedback, in astronomy rather than fluid dynamics.
- [T-Eval](./t-eval.md) — Also decomposes a capability into separately scored tiers, by tool-use subprocess rather than by knowledge / reasoning / implementation depth.
