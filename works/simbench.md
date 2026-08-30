# SimBench (2024)

> **English** | [简体中文](../zh/works/simbench.md)

> **First appeared:** 2024-08-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2408.11987)

## Overview

SimBench evaluates and diagnoses LLM-based digital-twin generation for multi-physics simulation: simulator-oriented LLMs build digital twins for the open-source Chrono simulator — multibody dynamics, finite element analysis, vehicle dynamics, robotic dynamics, and sensor simulation — through multi-turn interactions, scored by an LLM judge with predefined rules and human-in-the-loop guidance.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2408.11987>
- **Code:** <https://github.com/uwsbel/SimBench>
- **Venue:** arXiv preprint; IEEE Access 2026 per the official repository

## Summary

SimBench asks whether an LLM can stand up a working simulation of a physical system from dialogue: over 33 open- and closed-source simulator-oriented LLMs are compared on generating Chrono digital twins across five physics areas, with a judge LLM assigning scores under predefined rules and human-in-the-loop guidance. Per the official repository the suite spans 102 demonstration tasks over 34 physical systems with 3,000+ expert-scored multi-turn dialogues (plus a companion 280-question PyChronoBench), and the project has since evolved under the name ChronoBench; the design is presented as extensible to ANSYS, ABAQUS, OpenFOAM, and other simulators.

## Tasks

Multi-turn digital-twin generation for the Chrono multi-physics simulator; 102 demonstration tasks across 34 physical systems per the official repository.

## Domains

Multi-physics simulation engineering: multibody dynamics, finite element analysis, vehicle dynamics, robotic dynamics, and sensor simulation.

## Evaluation

- LLM-as-a-judge scoring with predefined rules and human-in-the-loop guidance over multi-turn generations.
- **Reported.** Over 33 simulator-oriented LLMs compared; numeric rankings are TODO(reference).

## Typical Duration

Multi-turn dialogue episodes per digital-twin task.

## Main Contribution

The first systematic comparison of LLMs as digital-twin engineers, establishing multi-turn simulator-code generation — not one-shot scripting — as the evaluated skill.

## Key Design Ideas

- Digital-twin generation bundles geometry, dynamics, and solver configuration into one realistic deliverable.
- Multi-turn interaction mirrors how simulation engineers actually iterate.
- Rule-guided LLM judging with human oversight balances scale against grading fidelity.

## Strengths

- Breadth across five physics areas and 33+ models.
- Maintained by the Chrono developers, keeping tasks aligned with the real simulator.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. The repository has been renamed ChronoBench and cites an IEEE Access 2026 publication; the arXiv page itself carries no venue.

## Related Works

- [FEABench](./feabench.md) — Also drives professional simulation software (COMSOL) through language interfaces.
- [CFDLLMBench](./cfdllmbench.md) — Also multi-tier simulation-code evaluation, specialized to CFD with physics-grounded checks.
- [SciConvBench](./sciconvbench.md) — Also examines the dialogue side of simulation setup, via clarification of ill-posed requests.
