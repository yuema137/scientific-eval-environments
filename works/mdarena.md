# MDArena (2026)

> **English** | [简体中文](../zh/works/mdarena.md)

## Overview

MDArena is a benchmark that evaluates coding agents on realistic molecular dynamics (MD) workflows. It comprises 50 containerized tasks sourced from active research projects, spanning 29 molecular systems and 14 research protocols.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.02642>
- **Venue:** arXiv preprint (physics.chem-ph, cs.AI), 2026

## Summary

MDArena argues that while coding agents show promise for automating scientific workflows, their reliability on realistic molecular dynamics tasks remains poorly characterized. The benchmark packages authentic biomolecular simulation work — trajectory analysis, system preparation, free-energy calculations, and enhanced sampling — into containerized tasks and scores agents with strict success rates alongside process-level partial credit.

## Tasks

50 containerized tasks sourced from active research projects, covering 29 molecular systems and 14 research protocols. Task categories include trajectory analysis, system preparation, free-energy calculations, and enhanced sampling methods.

## Domains

Biomolecular simulation and computational chemistry, including membrane-protein systems and alchemical free-energy calculations.

## Evaluation

- **Strict-Pass@1** as the headline success metric.
- **Correctness and process-reward metrics** capture partial progress beyond binary success.
- **Reported.** Six model configurations evaluated; Codex GPT-5.5 (extra-high reasoning) leads with 24/50 tasks (48%), Codex GPT-5.5 (Medium) reaches 21/50, and OpenCode Gemini Flash 3.5 reaches 20/50.

## Typical Duration

Containerized simulation workflows; per-task wall-clock is TODO(reference).

## Main Contribution

A benchmark of authentic, containerized molecular dynamics workflows that characterizes coding-agent reliability on realistic biomolecular simulation rather than synthetic exercises.

## Key Design Ideas

- Tasks are sourced from active research projects rather than authored for the benchmark.
- Containerization makes heterogeneous MD toolchains reproducible evaluation surfaces.
- Strict success is complemented by process-reward metrics that credit partial progress.

## Strengths

- Realistic task provenance: 29 molecular systems and 14 protocols from active research.
- Substantial headroom — the best configuration solves 48% of tasks.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — Also evaluates simulation-domain scientific computing with execution-grounded scoring, in fluid dynamics rather than molecular dynamics.
- [ScienceAgentBench](./scienceagentbench.md) — Also extracts executable scientific tasks from real research, across data-driven discovery disciplines rather than one simulation modality.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also containerized scientific workflows, community-contributed across five domain tracks.
