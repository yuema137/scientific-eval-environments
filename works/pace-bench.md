# PACE-Bench (2026)

> **English** | [简体中文](../zh/works/pace-bench.md)

> **First appeared:** 2026-08-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.14441)

## Overview

PACE-Bench (Physics Adaptation via Code Evolution) evaluates self-evolving agents on recovery after the world changes underneath them. Each of its 144 tasks pairs a source physics environment with a mutated target environment sharing the same goal and interface, where a code-driven design that succeeds in the source fails in the target and the agent must iteratively repair it using diagnostic sandbox feedback within a bounded attempt budget.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.14441>
- **Code:** <https://github.com/thunlp/PACE-Bench> (CC BY 4.0)
- **Venue:** arXiv preprint (August 2026).

## Summary

Existing evaluations of self-evolving agents optimise under fixed execution conditions and never test what happens when those conditions change. PACE-Bench closes that gap by construction. A task begins from a working solution — a Python program defining `build_agent()` for structure assembly and `agent_action()` for control logic — that succeeds in a source Box2D environment. The target environment shares the goal and the interface but mutates physical parameters such as friction, material strength, gravity or force limits, and the source design fails there. The agent must adapt the program into a working target design, guided by structured diagnostic feedback that reports what went wrong without prescribing a fix. The authors compare ten self-evolving methods from four paradigms and find the benchmark far from saturated. Two results shape the paper's argument: simulator-grounded reflection proves more reliable than unverified self-revision, and — in the study's most pointed experiment — telling the agent exactly which physical variables changed does not raise the ceiling, which locates the bottleneck in mechanism redesign rather than parameter inference.

## Tasks

**36 base tasks** yielding **144 source-to-target adaptation pairs** (four per task), evenly distributed across **six physics domains at 6 tasks each**: Statics & Equilibrium, Kinematics & Linkages, Dynamics & Energy, Granular & Fluid Interaction, Cybernetics & Control, and Exotic Physics. The four pairs per task form escalating stages, with **stages 1–4 mutating between 2 and 10 parameters** each. The simulator is the **Box2D** 2D rigid-body engine at **60 FPS**.

## Domains

**Physics.** The six task families are physics domains in the literal sense — statics, kinematics, dynamics, granular and fluid interaction, control, and a non-standard-physics family — and success requires reasoning about mechanism under changed physical parameters, verified by rigid-body simulation. No engineering co-domain is assigned: the designs are simulated 2D mechanisms rather than artifacts evaluated against any engineering standard or fabrication constraint.

## Evaluation

The attempt budget is **20 per source-to-target pair**. After each attempt the agent receives structured diagnostic feedback: a constraint-satisfaction fraction (v), a task score (s) in **[−100, 100]**, and a diagnostic report (d) listing physics-grounded quantities such as peak joint force and failure timestamp — deliberately without prescriptive fixes. Results are reported as **Pass@2** and **Score@2**.

**Ten methods across four paradigms** are compared: context-based (Vanilla, Reflexion, Self-Refine), memory-augmented (ACE, ExpeL, ReasoningBank), inference-time search (Tree-of-Thoughts, CodeEvolve), and parameter-based (SEAL, RAGEN, TTT-Discover).

The benchmark is far from saturated. **Reflexion + Qwen3-14B reaches only 35.9% Pass@2 (28.0 Score@2)** on the full benchmark, against **32.0% / 25.5** for Vanilla + Qwen3-14B. On the Statics subset under the full budget, **GPT-5.5 reaches 66.7% Pass@2 (78.1 Score@2)** and **Qwen3-32B 37.5% (28.4)**. Per-method, Tree-of-Thoughts scores **20.3% Pass@2** while leading efficiency at **57.8 Score/Hour**; ACE reaches **25.0%**; Self-Refine collapses to **7.1%**. Per-category difficulty is wide: Exotic Physics is most solvable at **56.3%** Pass@2 and Dynamics & Energy hardest at **12.5%** (Qwen3-14B, Vanilla).

The change-exposure experiment reveals the exact changed variables and values (CE) against hiding them (CH). Exposure **does not help and mostly hurts**: Reflexion-14B **17.9% → 14.6% (−3.3)**, Vanilla-14B **17.0% → 9.8% (−7.2)**, with ACE-4B the sole gainer at **6.0% → 12.0% (+6.0)**.

## Typical Duration

**20 attempts per pair.** Wall-clock is not reported directly, but efficiency is reported as Score per Hour — Tree-of-Thoughts leads at **57.8 Score/Hour** — so per-method runtime differs substantially. `TODO(reference)` — absolute wall-clock and token budgets per pair are not tabulated.

## Main Contribution

An adaptation benchmark whose difficulty comes from a controlled change to the environment rather than from task novelty, isolating the capacity to repair a working design after its assumptions break — and the accompanying negative result that revealing what changed does not raise the ceiling, which reframes the bottleneck as mechanism redesign ("know how") rather than parameter inference ("know what").

## Key Design Ideas

- Every task starts from a *working* solution, so the measured quantity is recovery from a broken assumption rather than cold-start problem solving.
- Source and target share goal and interface, which holds everything constant except the physics and makes the mutation the sole explanation for failure.
- Diagnostic feedback is physics-grounded but non-prescriptive: it reports peak joint force and failure timestamp, not what to change.
- Four escalating stages per base task give a difficulty gradient from 2 to 10 mutated parameters, so saturation can be located rather than merely observed.
- The change-exposure ablation is an upper-bound probe: by handing the agent the ground-truth parameter delta, it separates "did not infer the change" from "could not redesign the mechanism".
- Comparing four distinct self-evolution paradigms on one task set makes the paradigm-level findings — memory anchors to early designs, broad tree search explores without converging — comparable rather than anecdotal.

## Strengths

- Success is decided by a rigid-body simulator against an explicit constraint-satisfaction fraction, not by an LLM judge.
- The change-exposure experiment is a genuine attempt to refute the paper's own likely explanation, and it reports the result even though the effect is mostly negative.
- Per-category results are broken out, so the four-fold spread between Exotic Physics and Dynamics & Energy is visible rather than hidden in an aggregate.
- Ten methods across four paradigms give the comparison enough coverage to support paradigm-level rather than method-level claims.
- Efficiency is reported alongside accuracy (Score/Hour), so a method that wins by spending more is not credited as strictly better.
- Code and data are public under CC BY 4.0.

## Limitations

- Everything runs in 2D Box2D. The authors state directly that findings may not transfer to 3D environments or real robots.
- The 20-attempt budget is fixed, capping the interaction horizon and leaving open how far the ceiling would move with more attempts.
- Frontier-model, parameter-disclosure and visual-feedback studies cover only selected domains and methods due to compute cost, so the strongest models are not evaluated on the full benchmark — GPT-5.5's 66.7% is a Statics-only figure and is not comparable to the full-benchmark numbers.
- Absolute wall-clock and token cost per pair are not tabulated (recorded above as `TODO(reference)`).
- Repository note: the mutations are parameter changes to an existing simulation rather than structural changes to the physical model, so "physics adaptation" here means adapting to different parameter values within one simulator, not to a different physical regime.

## Related Works

- [Gravity-Bench-v1](./gravity-bench.md) — Physics discovery where the environment can violate known laws and observation budget is part of scoring, testing inference about physics rather than recovery after it changes.
- [SimulCost](./simulcost.md) — Cost-aware evaluation of simulation parameter tuning, sharing the budgeted-iteration framing on a parameter-fitting rather than mechanism-redesign task.
- [EngDesign](./engdesign.md) — Engineering design evaluated by simulation against specifications, where the design is produced from scratch rather than repaired after an environment change.
- [AutoWorldModel-Bench](./autoworldmodel-bench.md) — Also gives agents a working artifact to improve under a fixed budget, targeting a learned world model rather than a physical mechanism.
