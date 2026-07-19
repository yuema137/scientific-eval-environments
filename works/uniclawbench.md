# UniClawBench (2026)

## Overview

UniClawBench is a universal benchmark for proactive agents on real-world tasks, organized around five model capabilities and evaluated in live Docker containers via a closed-loop executor / supervisor / user simulation.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.08768>

## Summary

UniClawBench targets proactive agents that operate everyday tools and assist users in real-world environments. Tasks are executed in live Docker containers with step-by-step checkpoints, and evaluation runs in a closed loop with executor, supervisor, and user agents simulating multi-turn feedback without exposing grading criteria to the agent under test.

## Tasks

400 bilingual real-world tasks.

## Domains

Cross-platform proactive-agent tasks. Task construction is capability-driven across five axes rather than domain-partitioned.

## Evaluation

- Capability-driven, along five axes: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination.
- Live Docker environments with step-level checkpoints.
- Closed-loop simulation with executor, supervisor, and user agents.
- Grading standards are hidden from the agent under test.

## Typical Duration

Multi-turn interactions with checkpoints; long-horizon per task. Specific per-task duration not stated in the abstract.

## Main Contribution

A capability-oriented, closed-loop simulation-based benchmark for proactive agents in which grading criteria remain hidden from the agent under test.

## Key Design Ideas

- Five explicit capability axes as the organizing principle.
- Docker-based live environments per task.
- Multi-agent closed-loop simulation (executor + supervisor + user).
- Hidden grading standards to reduce evaluation gaming.

## Strengths

- Capability-driven design surfaces where an agent is weak, not just whether it fails.
- Hidden grading standards reduce leakage risk during optimization.
- Bilingual coverage across 400 real-world tasks.

## Limitations

- Repository note: Closed-loop simulation depends on the fidelity of the simulator agents; simulator quality bounds evaluation fidelity.

## Related Works

- [Agents' Last Exam](./agents-last-exam.md) — Also targets real-world proactive-agent tasks, but grounded in industry-expert workflows rather than a capability taxonomy.
- [AgentBoard](./agentboard.md) — Also capability-oriented multi-turn evaluation, but at subgoal-progress granularity.
