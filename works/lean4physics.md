# Lean4Physics / LeanPhysBench (2025)

> **English** | [简体中文](../zh/works/lean4physics.md)

## Overview

Lean4Physics (Lean4PHYS) is a reasoning framework for college-level physics in Lean4, contributing LeanPhysBench — 200 hand-crafted, peer-reviewed formal physics statements derived from university textbooks and competition problems — together with PhysLib, a community-driven repository of unit systems and theorems for formal physics reasoning. The paper presents it as the first physics benchmark in Lean4.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.26094>
- **Venue:** ICLR 2026

## Summary

LeanPhysBench moves physics evaluation into a formal proof assistant: solving a problem means producing a Lean4 proof the kernel accepts, so correctness is machine-checked rather than judged. Because formal physics needs infrastructure mathematics libraries lack — unit systems, physical theorems — the paper also builds PhysLib as a foundation. Evaluating expert math Lean4 provers and state-of-the-art closed-source models, the best results are 16% (DeepSeek-Prover-V2-7B) and 35% (Claude-Sonnet-4), and PhysLib adds an average 11.75% improvement.

## Tasks

200 hand-crafted, peer-reviewed Lean4 physics statements derived from university textbooks and physics competition problems; static theorem-proving evaluation.

## Domains

College-level physics rendered as formal Lean4 statements; subfield composition is not stated in the abstract.

## Evaluation

- Lean4 proof success — correctness is established by the proof assistant, with no judge in the loop.
- **Reported.** Best performance 16% for DeepSeek-Prover-V2-7B and 35% for Claude-Sonnet-4; PhysLib yields an average improvement of 11.75%.

## Typical Duration

Single-statement formal proving; not an interactive agent setting.

## Main Contribution

Brings kernel-checked formal verification to physics evaluation, and supplies the missing physical foundation library (unit systems, theorems) that makes formal physics provable at all.

## Key Design Ideas

- A proof assistant as the grader removes judge error from physics evaluation entirely.
- PhysLib treats physical infrastructure (units, base theorems) as a first-class reusable artifact.
- Statements are peer-reviewed, so formalization fidelity is itself checked.

## Strengths

- The strictest possible verification standard: a proof either checks or it does not.
- Measured library effect (+11.75%) demonstrates how much of formal-physics difficulty is missing infrastructure.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation. No code release is verifiable from the paper's arXiv page.

## Related Works

- [FormalRewardBench](./formalrewardbench.md) — Also uses Lean 4 verification as ground truth, to test reward models on proof preferences.
- [Hard2Verify](./hard2verify.md) — Also verification-centric evaluation at frontier difficulty, via expert step labels on informal proofs.
- [MATP](./matp.md) — Also delegates step verdicts to formal machinery, via autoformalization to first-order logic.
