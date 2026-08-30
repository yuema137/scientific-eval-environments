# VLA-Arena (2025)

> **English** | [简体中文](../zh/works/vla-arena.md)

> **First appeared:** 2025-12-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2512.22539)

## Overview

VLA-Arena is an open-source benchmark and toolchain for evaluating Vision-Language-Action (VLA) models as generalist robot-manipulation policies, using a structured task-design framework that varies difficulty along three orthogonal axes.

## Topics


- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities


N/A — General-purpose robot-manipulation (VLA) benchmark; evaluates generic embodied control, not a scientific or research activity.

## Links

- **Paper:** https://arxiv.org/abs/2512.22539
- **Project:** https://vla-arena.github.io
- **Code:** https://github.com/PKU-Alignment/VLA-Arena
- **Venue:** ICML 2026 (arXiv preprint, December 2025)

## Summary

VLA-Arena introduces a structured task-design framework that quantifies task difficulty across three orthogonal axes — Task Structure, Language Command, and Visual Observation — so that manipulation tasks can be constructed with fine-grained, controllable difficulty. The benchmark reports that its extensive evaluation of state-of-the-art VLAs surfaces recurring limitations: memorization over generalization, superficial visual perception, and neglect of safety constraints. The authors also report that model rankings reverse across difficulty levels L0–L2, which they take as evidence that each level yields non-redundant diagnostic information. The complete framework, datasets, and an end-to-end toolchain are released for reproducibility.

## Tasks

The benchmark comprises **11 task suites totaling 170 tasks**, organized into four dimensions: Safety, Distractor, Extrapolation, and Long Horizon. The GitHub README reports the split as Safety (5 suites, 75 tasks), Distractor (2 suites, 30 tasks), Extrapolation (3 suites, 45 tasks), and Long Horizon (1 suite, 20 tasks). Each suite spans **three difficulty levels (L0–L2)**, with fine-tuning restricted to L0 to assess generalization to unseen harder levels. Orthogonal to task structure, **language perturbations (W0–W4)** and **visual perturbations (V0–V4)** can be applied to any task as diagnostic probes intended to separate robust grounding from superficial pattern matching. The task suites are built on top of the RoboSuite, LIBERO, and VLABench frameworks (as acknowledged in the repository). Three fine-tuning dataset variants are released: VLA-Arena-S, VLA-Arena-M, and VLA-Arena-L.

## Domains

Robotics — simulated robot manipulation and control, evaluating VLA models as robot policies. `Repository note:` the primary sources describe simulation-based evaluation and do not report real-robot experiments.

## Evaluation

Evaluation uses two primary metrics: **Success Rate (SR)** and **Cumulative Cost (CC)**. Per the project page, Safety tasks report both SR and CC, while the other task categories report SR only. The released framework provides evaluation configurations for VLA models including OpenVLA, OpenVLA-OFT, UniVLA, SmolVLA, and Openpi (`openpi`). `TODO(reference)` — precise per-model numeric results are reported in the paper but not transcribed here.

## Typical Duration

`TODO(reference)` — the primary sources do not report per-task wall-clock time or step budgets. `Repository note:` the Long Horizon suite (20 tasks) requires extended multi-step manipulation sequences, whereas the other suites consist of shorter episodes.

## Main Contribution

A benchmark with a novel structured task-design framework that decomposes manipulation difficulty into three orthogonal axes (Task Structure, Language Command, Visual Observation), enabling systematically graded tasks (L0–L2) and orthogonal language/visual perturbation probes for precise measurement of VLA capability frontiers and failure modes, released with a full open-source toolchain.

## Key Design Ideas

- Decompose task difficulty into three orthogonal axes (Task Structure, Language Command, Visual Observation) so difficulty can be varied independently and diagnostically.
- Organize the 170 tasks into four capability dimensions — Safety, Distractor, Extrapolation, and Long Horizon.
- Restrict fine-tuning to the easiest level (L0) and test on harder levels (L1–L2) to measure generalization rather than memorization.
- Apply language (W0–W4) and visual (V0–V4) perturbations as post-hoc diagnostic probes on any task.
- Include a cost-based metric (Cumulative Cost) alongside Success Rate, especially for Safety tasks.

## Strengths

- Controlled, factorized difficulty design allows attributing failures to specific axes (structure, language, or vision) rather than to overall task hardness (paper).
- The authors report that model rank reversals across L0–L2 demonstrate each level contributes non-redundant diagnostic signal (paper).
- Open-source end-to-end toolchain, multiple fine-tuning dataset sizes, and a leaderboard support reproducibility (paper, project page).

## Limitations

- `Repository note:` the primary sources describe simulation-based evaluation; they do not report physical-robot deployment, so sim-to-real transfer of the reported findings is not established by the sources reviewed.
- `TODO(reference)` — the exact set of evaluated models and their numeric scores are in the paper but are not transcribed in this card.

## Related Works

- [CaP-X](./cap-x.md) — another benchmark evaluating VLA/manipulation models on simulated robot control across difficulty tiers.
- [ManipBench](./manipbench.md) — evaluates VLM/VLA reasoning about low-level robot manipulation.
