# RoboGraphBench (2026)

> **English** | [简体中文](../zh/works/compiling-and-benchmarking-task-state-horizons-for.md)

> **First appeared:** 2026-08-08 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.08036)

## Overview

A benchmark and task compiler (RoboGraph) that evaluates agentic foundation models as high-level planners for long-horizon embodied tasks, characterizing difficulty by the *task-state horizon* (TSH) — the span of task-relevant state transitions an agent must track, maintain, explore, and update over a trajectory.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General embodied high-level planning benchmark (household manipulation/navigation); evaluates state-tracking in generic robotics, not a scientific/research activity.

## Links

- **Paper:** https://arxiv.org/abs/2608.08036
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

The work argues that existing long-horizon robotic benchmarks characterize difficulty mainly through action-sequence length and subtask complexity, and overlooks a distinct challenge: agents must track evolving task-relevant world states induced by both their own exploration and environmental dynamics. It formalizes this as the *task-state horizon* (TSH) and introduces RoboGraph, a robotic task compiler that translates spatial and temporal causal state-transition dependencies — including those induced by unexpected failures and interventions during execution — into executable symbolic graphs. Building on RoboGraph, the authors release a benchmark of 588 episodes across 84 scenes spanning a range of TSHs, and evaluate 15 agentic models in both semantic (symbolic) and visual closed-loop environments.

## Tasks

588 episodes across 84 scenes of household manipulation and rearrangement, split into a tabletop setting (399 episodes from 57 scenes) and an indoor navigation setting (189 episodes from 27 scenes); reported task themes include cosmetics storage, desk organization, dining-table organization, food packing, and fridge-condiment loading. Each scene yields one baseline plus six intervention conditions (action failure, state regression, subgoal rollback, wrong relocation, added occlusion, added object), producing the 588 total. RoboGraph compiles each task into a symbolic scene graph encoding state-transition dependencies; the paper reports average scene graphs of 18.4 nodes, 21.8 edges, 6.1 occluded nodes, and 14.3 subgoals.

## Domains

Robotics — embodied high-level planning for robotic manipulation and indoor navigation, evaluated in tabletop and kitchen simulators.

## Evaluation

Unified closed-loop evaluation harness with a 100-step maximum per episode; success requires achieving the goal predicates and issuing a "stop" action within the step budget. Two environment modes are used: a semantic mode presenting scene graphs as text observations without visual rendering, and a visual mode using the RoboTwin 2.0 simulator (three-view RGB) for tabletop tasks and the RoboCasa simulator for indoor kitchen navigation. Reported metrics include task success — Success Rate (SR) and Success weighted by Symbolic Action Length (SSAL) — five state-management metrics grouped as maintenance (Action Executability Rate, Redundant Action Rate), exploration (State Exploration Gain, Action-Distance Reduction Rate), and updating (Intervention Recovery Rate), plus recovery metrics F1@Recovery Detection and Accuracy@Recovery Grounding.

## Typical Duration

Closed-loop episodes with a maximum of 100 steps each. No wall-clock time or token budget per task is reported (`TODO(reference)`).

## Main Contribution

Introduces the task-state horizon (TSH) as an axis of long-horizon difficulty distinct from action-sequence length, along with RoboGraph, a compiler that turns spatial/temporal causal state-transition dependencies (including failure- and intervention-induced ones) into executable symbolic graphs, and a 588-episode benchmark for measuring how agent performance varies with TSH.

## Key Design Ideas

- **Task-state horizon (TSH)** decomposed into three measurable dimensions: `H_maintain` (maximum steps between acquiring a temporally-dependent fact and its last use), `H_explore` (maximum view-expanding actions needed to expose spatially-dependent facts), and `H_update` (count of facts invalidated by exogenous events during the oracle solution).
- **RoboGraph compiler** translates state-transition dependencies into executable symbolic graphs, allowing tasks to be constructed at controlled TSHs.
- **Intervention conditions** — six perturbations (action failure, state regression, subgoal rollback, wrong relocation, added occlusion, added object) injected per scene to induce state updates and test recovery.
- **Dual environment modes** — a purely symbolic (semantic) mode and a visual closed-loop mode (RoboTwin 2.0 for tabletop, RoboCasa for indoor), sharing one evaluation harness.
- **State-management metric suite** separating maintenance, exploration, and updating behaviors, plus explicit recovery detection and grounding metrics.

## Strengths

- Isolates a state-tracking dimension of long-horizon difficulty that action-length-based benchmarks do not directly measure, and operationalizes it with quantitative TSH sub-measures.
- Evaluates the same tasks in both symbolic and visual closed-loop settings, separating planning/state-tracking from perception.
- Systematically injects failures and interventions to probe recovery, with dedicated recovery-detection and grounding metrics.

## Limitations

- Tasks are household manipulation and rearrangement in simulation (RoboTwin 2.0, RoboCasa); the paper does not report real-robot execution (`TODO(reference)`).
- No code or project URL was located in the primary source at the time of writing (`TODO(reference)`).
- Repository note: the benchmark evaluates high-level symbolic planning by foundation models rather than low-level robot control policies; conclusions concern planners' state-tracking behavior, not end-to-end robot autonomy.

## Related Works

- [CaP-X](./cap-x.md) — also evaluates frontier models as robotic planners over symbolic/program abstractions of manipulation tasks.
- [VIKI-Bench](./viki-bench.md) — embodied multi-robot planning benchmark evaluating foundation models in simulated scenes.
- [REFLECT / RoboFail](./robofail.md) — shares the focus on failures and correction/recovery in robot manipulation episodes.
