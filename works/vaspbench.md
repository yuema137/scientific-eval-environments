# AutoDFT / VASPBench (2026)

> **English** | [简体中文](../zh/works/vaspbench.md)

## Overview

VASPBench is a purpose-built benchmark for autonomous density-functional-theory calculations, spanning 34 tasks across 9 DFT calculation types; it is released with AutoDFT, a closed-loop multi-agent framework that plans, runs, and repairs VASP calculations and reaches 94.1% task-level success with GPT-5.2.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.26179>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2026

## Summary

Setting up DFT is expert, fiddly, and failure-prone, and AutoDFT automates the loop: a strategic planner lays out skeletal step objectives, a step planner fills in numerical parameters just in time, and a monitor-recover-reflect cycle diagnoses and repairs failures while revising the plan. VASPBench measures this over 34 tasks across 9 DFT calculation types, on which AutoDFT achieves 94.1% task-level success with GPT-5.2, alongside quantitatively reliable predictions of electronic, magnetic, and energetic properties against established materials databases.

## Tasks

34 DFT-calculation tasks across 9 calculation types; the agent plans, executes, and repairs VASP runs in a closed loop. Interactive/agentic; runs real DFT calculations.

## Domains

Materials science — autonomous density-functional-theory workflow execution (VASP), producing electronic, magnetic, and energetic property predictions.

## Evaluation

- Task-level success on VASPBench, plus quantitative property-prediction accuracy against established materials databases.
- **Reported.** AutoDFT reaches 94.1% task-level success with GPT-5.2.

## Typical Duration

Closed-loop, multi-step episodes per DFT task, including failure diagnosis and re-planning.

## Main Contribution

Bringing autonomous, self-repairing agents to DFT calculation setup — and a benchmark (VASPBench) that scores whether an agent can drive a real electronic-structure workflow to a correct result.

## Key Design Ideas

- Separating a strategic planner from a just-in-time step planner mirrors how experts stage DFT work.
- The monitor-recover-reflect cycle makes failure repair part of the measured behavior.
- Grounding against established databases checks property correctness, not just job completion.

## Strengths

- One of the first agent benchmarks for DFT-workflow orchestration in materials.
- Closed-loop failure repair is evaluated, not just one-shot setup.

## Limitations

- Repository note: the paper's primary contribution is the AutoDFT framework; VASPBench is its paired benchmark, and this card centers the benchmark. No public release of VASPBench is verifiable from the arXiv page, and no venue is stated in arXiv metadata.

## Related Works

- [MatTools](./mattools.md) — Also LLMs driving materials computation, via pymatgen tool-use rather than DFT orchestration.
- [MDArena](./mdarena.md) — Also agentic computational workflows over molecular-dynamics rather than DFT.
- [EnvTrace](./envtrace.md) — Also evaluates scientific-instrument/computation control by execution behavior.
