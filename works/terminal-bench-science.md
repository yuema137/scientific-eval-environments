# Terminal-Bench Science (2026)

> **English** | [简体中文](../zh/works/terminal-bench-science.md)

## Overview

Terminal-Bench Science extends the Terminal-Bench framework to natural-science domains, evaluating AI agents on containerized scientific-computing workflows with deterministic programmatic verification.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Project:** <https://www.tbench.ai/news/tb-science-announcement>
- **Code:** <https://github.com/harbor-framework/terminal-bench-science>
- **Task Dashboard:** <https://stevendillmann.github.io/tb-science-task-dashboard/>
- **License:** Apache 2.0

## Summary

Terminal-Bench Science is a scientist-driven benchmark for evaluating AI agents on real computational workflows drawn from natural-sciences research. Tasks run in containerized environments and are validated with pytest-based deterministic checks. The project is hosted by Stanford University and the Laude Institute, and follows a structured Propose → Build → Review contribution model.

## Tasks

8 tasks currently across 5 scientific domains, with a target of 100+ tasks. PR deadline for the initial task-contribution round is 2026-08-17.

## Domains

Five scientific domains:

- **Life Sciences** — Biology, Ecology, Medicine, Neuroscience.
- **Physical Sciences** — Astronomy, Chemistry, Materials Science, Physics.
- **Earth Sciences** — Atmospheric, Environmental, Geosciences, Ocean Sciences.
- **Mathematical Sciences** — Applied Mathematics, Formal Mathematics, Operations Research, Statistics.
- **Engineering Sciences** — Chemical, Civil, Electrical, Mechanical Engineering.

## Evaluation

- Containerized execution environments.
- Deterministic pytest-based verification.
- Stated target: 10–20% solve rate at release (deliberately hard tasks).
- Task validation gate: three approvals (domain reviewer, general reviewer, bar-raiser) plus CI checks.

## Typical Duration

Minutes to hours per task depending on workflow complexity (per project announcement).

## Main Contribution

A scientist-driven extension of Terminal-Bench to natural-science computational workflows with deterministic containerized verification and an explicit contribution / review protocol.

## Key Design Ideas

- Domain-expert-authored tasks under a structured Propose → Build → Review protocol.
- Programmatic verification via pytest inside containers.
- Explicit difficulty target (10–20% solve rate) at release.
- Cross-domain scientific breadth under a shared execution framework.

## Strengths

- Direct scientist involvement gives ecological validity.
- Deterministic pytest-based grading avoids LLM-judge variance.
- Cross-domain scientific coverage under a shared execution framework.

## Limitations

- Repository note: 8 tasks in the current release — the 100+ task target is aspirational; results at time of writing rest on a small task set.
- Repository note: Reference is the project announcement and GitHub repository — no peer-reviewed paper accompanies the release yet.

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Sibling extension of Terminal-Bench, focused on long-horizon tasks broadly rather than scientific ones.
- [NatureBench](./naturebench.md) — Also science-focused, but anchored on published SOTA in Nature-family papers rather than executable workflows.
