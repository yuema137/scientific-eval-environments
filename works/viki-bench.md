# VIKI-Bench (2025)

> **English** | [简体中文](../zh/works/viki-bench.md)

## Overview

VIKI-Bench is the first hierarchical benchmark for embodied multi-agent cooperation, structured in three levels — agent activation, task planning, and trajectory perception — over diverse robot embodiments with multi-view visual observations; it is paired with VIKI-R, a VLM fine-tuning method using chain-of-thought demonstrations and reinforcement learning.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2506.09049>
- **Code:** <https://github.com/MARS-EAI/VIKI-R>
- **Project:** <https://faceong.github.io/VIKI-R/>
- **Dataset:** <https://huggingface.co/datasets/henggg/VIKI-R>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

VIKI-Bench decomposes visual multi-robot cooperation into a hierarchy: level 1 selects which robots to activate from a scene image and task context, level 2 generates the multi-agent action plan, and level 3 perceives fine-grained motion trajectories from egocentric views. Per the official project page the suite holds 20,000+ task samples over 100 scenes with 6 heterogeneous robot types (humanoids, quadrupeds, wheeled manipulators), built on RoboCasa and ManiSkill3. The paired VIKI-R method — chain-of-thought fine-tuning followed by RL under multi-level rewards — significantly outperforms baselines across all levels.

## Tasks

Hierarchical visual-reasoning tasks at three levels (activation, planning, trajectory perception) over 20,000+ samples, 100 scenes, and 6 robot embodiments (project page); per-query visual reasoning rather than closed-loop control. Simulation only.

## Domains

Robotics — heterogeneous multi-robot coordination: robot-embodiment selection, multi-agent action planning, and robot-motion perception across humanoid, quadruped, and wheeled-manipulator platforms in simulation.

## Evaluation

- Per-level metrics: in-distribution and out-of-distribution planning accuracy; RMSE, Hausdorff distance, and directional Fourier distance for trajectory perception (project page).
- **Reported.** VIKI-R significantly outperforms baseline methods across all task levels (abstract); numeric level scores appear on the project page.

## Typical Duration

Single visual-reasoning queries per sample across the three hierarchy levels.

## Main Contribution

Structuring multi-robot cooperation as a measurable hierarchy, so "can models coordinate robots" decomposes into who, what plan, and what motion — each separately scored.

## Key Design Ideas

- Heterogeneous embodiments make agent activation a genuine capability question, not a formality.
- Multi-view and egocentric observations tie planning to perception rather than abstract state.
- OOD planning splits measure generalization beyond memorized scene-task pairs.

## Strengths

- Venue-verified with a full public stack across benchmark, method, and dataset.
- The hierarchy gives partial credit structure that end-to-end cooperation scores lack.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); scale figures come from the project page, not the abstract. The paper's title contribution is the VIKI-R method; VIKI-Bench is the benchmark this card covers.
- Simulation-only; no physical robot evaluation.

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — Also multi-robot cooperation evaluation, through inter-robot dialog with real-arm demos.
- [PARTNR](./partnr.md) — Also large-scale embodied multi-agent benchmarking, with human collaborators.
- [EmbodiedBench](./embodiedbench.md) — Also vision-driven embodied MLLM evaluation, single-agent.
