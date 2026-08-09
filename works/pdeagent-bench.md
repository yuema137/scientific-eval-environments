# PDEAgent-Bench (2026)

> **English** | [简体中文](../zh/works/pdeagent-bench.md)

## Overview

PDEAgent-Bench is a multi-metric, multi-library benchmark for PDE solver generation: 645 instances across 6 mathematical categories and 11 PDE families, targeting the common finite-element libraries DOLFINx, Firedrake, and deal.II, with a staged evaluation in which generated solvers must sequentially pass executability, numerical accuracy, and computational efficiency checks.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.09636>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Each instance provides an agent-facing problem specification from which the model must produce solver code for one of three FEM libraries. The staged evaluation makes the ladder explicit: code that runs is not code that is accurate, and accurate code is not necessarily efficient — solvers face case-specific accuracy and runtime targets against reference solutions on a prescribed evaluation grid. The headline finding: models often produce runnable code, but pass rates drop substantially once accuracy and efficiency requirements are enforced.

## Tasks

645 PDE-to-solver-code instances across 6 mathematical categories and 11 PDE families, each targeting DOLFINx, Firedrake, or deal.II.

## Domains

Numerical PDEs and the finite-element method across three production FEM libraries.

## Evaluation

- Staged checks: executability → numerical accuracy (against reference solutions on a prescribed grid, with case-specific targets) → computational efficiency (runtime targets).
- **Reported.** Models often produce runnable code, but pass rates drop substantially once accuracy and efficiency requirements are enforced.

## Typical Duration

Specification-to-solver generation per instance with automated staged checking.

## Main Contribution

Separates "it runs" from "it is right" from "it is fast" for LLM-generated PDE solvers, across multiple FEM libraries rather than one toolchain.

## Key Design Ideas

- The staged gate structure localizes failure to execution, accuracy, or efficiency.
- Three FEM libraries make library-specific memorization visible.
- Case-specific accuracy and runtime targets replace one-size-fits-all thresholds.

## Strengths

- The largest fixed suite documented here for solver generation (645 instances, 11 PDE families).
- The runnable-but-inaccurate gap quantifies exactly the failure mode practitioners fear.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [CodePDE](./codepde.md) — The framework that established LLM solver generation as an evaluation target.
- [MooseBench](./moosebench.md) — Also verifies that generated simulation code solves the intended physics, via PDE reconstruction.
- [FEM-Bench](./fem-bench.md) — Also FEM code generation, at graduate-coursework granularity with objective verification.
