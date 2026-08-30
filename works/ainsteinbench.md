# AInsteinBench (2025)

> **English** | [简体中文](../zh/works/ainsteinbench.md)

> **First appeared:** 2025-12-24 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2512.21373)

## Overview

AInsteinBench benchmarks coding agents on scientific repositories: tasks derived from maintainer-authored pull requests in six widely used, production-grade scientific codebases — spanning quantum chemistry, quantum computing, molecular dynamics, numerical relativity, fluid dynamics, and cheminformatics — resolved in executable environments with test-driven verification.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2512.21373>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.PL), 2025

## Summary

SWE-bench-style evaluation meets scientific software: AInsteinBench curates tasks from what maintainers of real scientific codebases actually merged, via multi-stage filtering and expert review, and evaluates agents in executable environments with test-driven verification and attention to scientifically meaningful failure modes. Where general-purpose coding benchmarks test web-app plumbing, these tasks require respecting numerical conventions, physical units, and algorithmic contracts of scientific computing.

## Tasks

Maintainer-PR-derived tasks across six production scientific repositories (quantum chemistry, quantum computing, molecular dynamics, numerical relativity, fluid dynamics, cheminformatics); task counts are TODO(reference).

## Domains

Scientific software engineering across quantum chemistry, quantum computing, molecular dynamics, numerical relativity, fluid dynamics, and cheminformatics codebases.

## Evaluation

- Test-driven verification in executable environments; curation by multi-stage filtering and expert review; scientifically meaningful failure-mode analysis.
- **Reported.** Numeric results are TODO(reference); the abstract states no figures.

## Typical Duration

Repository-level agent coding sessions per task.

## Main Contribution

Ports the maintainer-PR evaluation paradigm from general software to scientific computing, where correctness means numerical and physical validity, not just passing generic tests.

## Key Design Ideas

- Maintainer-authored PRs anchor tasks to changes the science actually needed.
- Executable environments with test-driven verification keep grading mechanical.
- Failure modes are categorized scientifically, not just as test failures.

## Strengths

- Production-grade repositories across six scientific fields.
- Expert-reviewed curation guards task validity.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release or task counts are verifiable from the paper's arXiv page.

## Related Works

- [SWE-bench](./swe-bench.md) — The general-software paradigm AInsteinBench ports to scientific codebases.
- [SciCode](./scicode.md) — Also scientist-curated research coding, as standalone problems rather than repository PRs.
- [MDArena](./mdarena.md) — Also research-derived scientific computing tasks, in one simulation modality.
