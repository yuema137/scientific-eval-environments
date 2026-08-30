# ATOM-Bench (2026)

> **English** | [简体中文](../zh/works/atom-bench.md)

> **First appeared:** 2026-06-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2606.16826)

## Overview

ATOM-Bench is a real-world robot benchmark that separates *atomic* manipulation skills from *compositional* tasks built out of them, so that a failure on a composed task can be attributed either to a weak underlying atom or to a genuine failure of compositional reuse.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose robot-manipulation policy benchmark; the evaluated policies perform tabletop manipulation, not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2606.16826>
- **Project:** <https://flageval-baai.github.io/AtomBenchPage/>
- **Dataset:** <https://huggingface.co/AtomBench>
- **Venue:** arXiv preprint, June 2026

## Summary

Generalist manipulation policies are increasingly presented as foundation models for robotic control, but the paper argues their real-world generalization is hard to diagnose: a policy may succeed on demonstrated tasks while still failing the fine-grained atomic skills underneath, or failing to recombine skills into new task structures. ATOM-Bench factorizes tabletop manipulation into **motor atoms** and **instruction atoms**, evaluating both atomic skill acquisition and held-out compositional generalization on paired single-arm and dual-arm robot tracks. Policies are fine-tuned on the atomic tasks and then evaluated on both the atomic tasks and the held-out compositional tasks, with two metrics designed to separate the two failure sources. The authors release both the demonstration data and the evaluation rollout data to support reproducible real-world evaluation.

## Tasks

**30 atomic tasks and 24 held-out compositional tasks** across paired single-arm and dual-arm robot tracks (Franka Panda single-arm; Agilex Cobot Magic dual-arm, Mobile ALOHA style). The atom taxonomy has two families:

- **Motor atoms:** pick-place, reorientation, pushing, stacking, pouring, articulated-object access.
- **Instruction atoms:** color, shape, size, counting, exclusion, spatial relations, goal destination.

Compositional tasks combine one or more motor atoms with multiple instruction atoms and are held out from fine-tuning. **3,000 human teleoperation demonstrations** are collected for atomic fine-tuning. `TODO(reference)` — the exact per-track split of the 30 atomic tasks between motor and instruction families is stated in the paper but not confirmed against a second source here.

## Domains

Robotics — real-robot tabletop manipulation on two physical platforms, with all reported results coming from physical rollouts rather than simulation.

## Evaluation

Policies are scored by task success rate plus a per-atom **Process Success Rate (PSR)** annotated by humans against task-completion predicates. Two derived metrics separate the failure sources:

- **Atomic Score (AS)** — the mean PSR over the atoms that a task requires, i.e. an estimate of how well the policy holds the ingredients of that task.
- **Compositional Failure Share (CFS)** — the share of a task's failure that cannot be explained by weak atoms, computed as `max(0, AS(X) − PSR(X)) / (1 − PSR(X))`. A high CFS indicates failure from composition rather than from missing atomic competence.

Evaluation uses 10 shared physical test seeds per task with mask-guided object placement for reproducible initial states. Five policies were evaluated over **2,700 physical rollouts**: Pi0.5, Motus, LingBot-VLA, GROOT N1.6, and SmolVLA — all vision-language-action generalist manipulation policies.

Reported headline result: Pi0.5 is the strongest policy, reaching 46.2% success on motor atoms on the Franka track and 94.3% on instruction atoms, but only 15.8% on held-out compositional tasks despite an Atomic Score of 83.3% — strong atomic performance does not transfer to composition. Pouring and articulated-object access are the hardest motor atoms across policies.

## Typical Duration

`TODO(reference)` — the sources consulted report rollout counts (10 seeds per task, 2,700 rollouts total) but not per-episode wall-clock time or horizon length.

## Main Contribution

A real-world benchmark that factorizes manipulation into motor and instruction atoms and pairs atomic evaluation with held-out compositional evaluation, together with two diagnostic metrics (Atomic Score and Compositional Failure Share) that distinguish failures caused by weak atomic skills from failures caused by limited compositional reuse.

## Key Design Ideas

- Factorizing tabletop manipulation into two orthogonal atom families — motor atoms (what the arm does) and instruction atoms (what the language specifies) — rather than a single flat task list.
- Fine-tuning policies on atomic tasks only, so compositional tasks are genuinely held out.
- Human-annotated per-atom Process Success Rate as the substrate for the aggregate metrics, rather than binary task success alone.
- Compositional Failure Share as an explicit attribution metric: it subtracts the failure already predicted by weak atoms.
- Paired single-arm and dual-arm tracks so results are reported per embodiment.
- Mask-guided object placement and shared test seeds to make real-robot evaluation reproducible.
- Release of both demonstration data and evaluation rollout data.

## Strengths

- Real-robot evaluation at scale (2,700 physical rollouts), not simulation transfer (paper).
- Directly instruments the aggregate-score-conflation problem: the AS/CFS pair makes it possible to say *why* a composed task failed (paper).
- Held-out compositional split is enforced by the fine-tuning protocol rather than assumed (paper).
- Two embodiments evaluated in parallel, so single-arm results are not generalized to dual-arm by assumption (paper).

## Limitations

- The authors note the benchmark is constrained by the cost of real-robot evaluation and of fine-tuning each policy, and that evaluation remains labor-intensive (human annotation of process success).
- Coverage excludes deformable-object manipulation, tool use, mobile manipulation, and highly long-horizon tasks (paper).
- `Repository note:` the atom taxonomy is authored by the benchmark designers; the paper does not establish that these atoms are a minimal or complete basis for tabletop manipulation, so AS is only as meaningful as the chosen factorization.
- `Repository note:` per-episode duration and token/compute budgets are not reported in the sources consulted.

## Related Works

- [VLA-Arena](./vla-arena.md) — also evaluates VLA manipulation policies along structured difficulty axes, but in simulation rather than on real hardware.
- [ManipBench](./manipbench.md) — probes low-level manipulation reasoning in VLMs via multiple-choice questions instead of physical rollouts.
- [RoboFAC](./robofac.md) — complementary failure-attribution angle: analyzing and correcting erroneous manipulation trajectories.
- [T-Eval](./t-eval.md) — the same decomposition commitment (score subprocesses separately rather than one aggregate) applied to tool use.
- [CFDLLMBench](./cfdllmbench.md) — another benchmark whose tiers are nested rather than parallel, producing a ceiling-shaped capability profile.
