# MooseBench (2026)

> **English** | [简体中文](../zh/works/moosebench.md)

## Overview

MooseBench is a 220-case multiphysics benchmark with PDE-level ground truth, released with a paper whose title states its finding: "Your Simulation Runs but Solves the Wrong Physics." The paired Intent Fidelity Score (IFS) deterministically reconstructs the PDE encoded by LLM-generated MOOSE input files and compares it to the intended contract.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.09360>
- **Venue:** arXiv preprint (cs.LG, cs.AI, cs.CL, cs.SE), 2026

## Summary

Execution success is a treacherous signal for simulation code: a MOOSE input file can run to completion while encoding the wrong governing terms, boundary conditions, or coefficients. The paper's IFS is a structural metric covering governing terms, BCs, ICs, coefficients, and time scheme, computed by deterministically reconstructing the encoded PDE from MOOSE Kernel/BC objects. Across the 220 MooseBench cases, execution-only repair improves execution success while leaving 39–40% of all cases runnable but still solving the wrong physics; a PDE-grounded refinement loop driven by deterministic violation reports adds +0.22 to +0.41 absolute IFS where direct generation falls below 0.7. A proof of concept extends the approach to UFL/FEniCS, FreeFEM, FiPy, and Devito.

## Tasks

220 multiphysics simulation-code generation cases for the MOOSE framework, each with PDE-level mathematical ground truth (the intended contract).

## Domains

Multiphysics finite-element simulation (MOOSE), with PDE weak-form reconstruction extending to UFL/FEniCS, FreeFEM, FiPy, and Devito.

## Evaluation

- **Intent Fidelity Score (IFS):** structural comparison of the deterministically reconstructed PDE (governing terms, BCs, ICs, coefficients, time scheme) against the intended contract.
- **Reported.** Execution-only repair leaves 39–40% of the 220 cases runnable but solving the wrong physics; PDE-grounded refinement adds +0.22 to +0.41 absolute IFS on cases starting below IFS 0.7.

## Typical Duration

Generation plus automated refinement loops per case; not an interactive environment.

## Main Contribution

Names and measures the comprehension-generation gap in simulation code: runnable is not right, and only PDE-level reconstruction — not execution — can tell the difference.

## Key Design Ideas

- The ground truth is the PDE, not the program: reconstruction makes physics fidelity checkable deterministically.
- Deterministic violation reports give the refinement loop actionable, judge-free feedback.
- The DSL proof-of-concept shows the reconstruction idea generalizes beyond MOOSE.

## Strengths

- The 39–40% runnable-but-wrong figure is the sharpest quantification yet of silent physics errors.
- IFS decomposes fidelity into auditable components rather than one score.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.
- Repository note: the paper's primary contribution is the IFS metric and refinement method; MooseBench is released alongside them, and this card documents the benchmark.

## Related Works

- [PDEAgent-Bench](./pdeagent-bench.md) — Also gates LLM-generated solvers beyond executability, via staged accuracy and efficiency checks.
- [CFDLLMBench](./cfdllmbench.md) — Also physics-grounded verification of simulation workflows, via convergence under refinement.
- [gwBenchmarks](./gwbenchmarks.md) — Also documents agents "completing" scientific tasks spuriously without external verification.
