# RoCo / RoCoBench (2023)

> **English** | [简体中文](../zh/works/rocobench.md)

> **First appeared:** 2023-07-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2307.04738)

## Overview

RoCoBench is a 6-task benchmark for multi-robot collaboration in which each robot is driven by an LLM: the robots discuss task strategy in natural-language dialog, generate sub-task plans and task-space waypoint paths, and improve them iteratively from environment feedback — released with the RoCo collaboration method.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2307.04738>
- **Code:** <https://github.com/MandiZhao/robot-collab>
- **Project:** <https://project-roco.github.io>
- **Venue:** arXiv preprint (cs.RO), 2023

## Summary

RoCo puts an LLM behind each robot arm and lets collaboration emerge through dialog: agents negotiate who does what, propose waypoint paths, and revise plans when collision checking rejects them. RoCoBench packages this into 6 collaborative manipulation tasks in MuJoCo whose semantics can be varied to test adaptation, plus RoCoBench-Text, a 269-question reasoning set covering self-knowledge, memory, communication, and adaptation (official project page). The approach is also demonstrated on a real UR5 arm with a human collaborator in the loop.

## Tasks

6 collaborative multi-robot manipulation tasks in MuJoCo simulation with semantic task variations, plus the 269-question RoCoBench-Text reasoning set; real-robot demonstration on a UR5 arm.

## Domains

Robotics — multi-robot manipulation and control: LLM-negotiated sub-task plans and waypoint paths executed in simulation and demonstrated on a physical UR5 arm.

## Evaluation

- Task success rates on RoCoBench, adaptation under task-semantic variations, and question answering on RoCoBench-Text.
- **Reported.** No numeric results in the abstract; figures await full-paper validation.

## Typical Duration

Multi-turn dialog-plus-replanning episodes per collaborative task.

## Main Contribution

Demonstrating — and making measurable — that inter-robot natural-language dialog can serve as the coordination substrate for multi-robot manipulation.

## Key Design Ideas

- Dialog as the coordination channel makes the collaboration interpretable and probeable.
- Environment feedback (collision checks) closes the loop on LLM-proposed motion.
- Semantic task variations measure adaptation, not memorized role assignment.

## Strengths

- The founding benchmark for LLM multi-robot collaboration, with an unusually complete public stack.
- RoCoBench-Text isolates the reasoning components from the control components.

## Limitations

- Repository note: the paper's primary contribution is the RoCo collaboration method; RoCoBench is its paired benchmark, and this card covers the benchmark. An ICRA 2024 venue claim circulates but is not verifiable from arXiv metadata or the official pages — the venue line stays at arXiv preprint.
- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); numeric results await full-paper validation.

## Related Works

- [PARTNR](./partnr.md) — Also embodied multi-agent collaboration benchmarking, at 100K-task scale with human partners.
- [VIKI-Bench](./viki-bench.md) — Also multi-robot cooperation evaluation, hierarchically structured across embodiments.
- [CaP-X](./cap-x.md) — Also LLMs producing executable robot control, via code synthesis rather than dialog.
