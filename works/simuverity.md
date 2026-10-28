# SimuVerity (2026)

> **English** | [简体中文](../zh/works/simuverity.md)

> **First appeared:** 2026-10-01 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.02304)

## Overview

A Simulink model generated from a text specification can look like the reference model and still fail as an engineering artifact: it may not compile, may miss a required signal path, or may behave wrongly under faults. SimuVerity asks agents to build executable Simulink models for 101 engineering systems and scores them by simulating them natively. A hierarchical evaluator first gates on delivery, executability, and an engineering qualification check, and only then scores six engineering dimensions over withheld test scenarios. The authors validate the evaluator against two experts and test whether structural similarity to the reference predicts the score.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Optimization & Engineering Design](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](https://arxiv.org/abs/2610.02304), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2610.02304v1>
- **Code and data:** <https://github.com/SimuVerity/SimuVerity>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.LG), 2026

## Summary

Reference systems come from public examples, engineering projects, research artifacts, and expert-built models; each is rebuilt or independently built, profiled by domain experts, and turned into a prompt. The agent works in MATLAB/Simulink R2025a through the MATLAB MCP server and must deliver an `.slx` file. The evaluator checks that the file exists, loads, compiles, and simulates, then applies task-specific expert checks for required functional roles and signal paths. A qualified model is run through the task's formal scenarios and scored as a weighted geometric mean of accuracy, output quality, mechanistic fidelity, control and causal integrity, robustness, and dynamic response. The best system scores 42.86 against 96.01 for the reference models.

## Tasks

101 text-to-Simulink tasks in ten engineering domains: power electronics & control 9, automotive systems 11, mechanical systems 11, battery systems 10, robotics 10, aerospace systems 10, thermal systems 11, communication systems 9, fluid systems 11, biomedical systems 9. The tasks carry 595 formal test scenarios in four families (operating envelope, interaction and fault, temporal process, mechanism and causal check).

## Domains

System-level dynamic modeling across power electronics and control, automotive, mechanical, battery, robotic, aerospace, thermal, communication, fluid, and biomedical systems.

## Evaluation

- **Gates:** artifact delivery (the `.slx` file), native executability (load, update, compile, simulate), and engineering qualification G (pass/fail expert checks of functional roles, signal paths, and valid evidence in the formal scenarios).
- **Score:** S_t(x) = Γ_t · H_t(v_t), where Γ_t applies the gates and H_t is a weighted geometric mean of the applicable dimensions A (objective accuracy), Q (output quality), M (mechanistic fidelity), C (control and causal integrity), R (operating-domain robustness), and D (dynamic response and recovery). Weights are set per task; for XAUTO-07 they are 0.25, 0.10, 0.25, 0.20, 0.10, 0.10.
- **No LLM judge.** Two experts rated 30 candidates on a five-point scale: weighted Cohen's κ = 0.90, evaluator-versus-expert mean Spearman ρ = 0.94, and expert-versus-expert ρ = 0.87.
- **Results (overall / delivered / executable / G pass, three runs per task):** Claude Opus 4.8 + Claude Code 42.86 / 94.72% / 86.47% / 76.90%; GPT-5.5 + Codex 41.72 / 98.68% / 94.72% / 75.58%; DeepSeek-V4-Pro + Claude Code 28.40 / 97.03% / 88.12% / 61.39%; Qwen3.8-Max + Claude Code 25.01 / 89.77% / 80.86% / 53.80%; GLM-5.3-Flash + Claude Code 4.98 / 96.04% / 48.18% / 13.20%; Qwen3.8-27B-FP8 + Claude Code 1.60 / 30.36% / 13.53% / 6.27%.
- **Structural similarity:** of 95 delivered Opus run-1 candidates, 39 are reference-aligned, 43 partially similar, and 13 structurally distinct, with end-to-end means of 52.13, 44.05, and 42.37. Twelve of the 24 top-quartile candidates are partially similar or structurally distinct, and seven reference-aligned candidates score zero.
- **Visual layout:** measured separately from the score with block overlap, routing detour, and line-crossing density; experts flagged 8 of 31 high-scoring models as severely disordered.
- **Ablations:** a No-Simulation MCP setting and a batch-only setting.

## Typical Duration

Not reported. A run ends when the agent declares completion; reasoning effort is set to the highest supported level.

## Main Contribution

A Simulink generation benchmark whose score comes from native simulation under withheld scenarios, behind executability and expert qualification gates, with the evaluator validated against expert ratings.

## Key Design Ideas

- Test conditions, scenario combinations, thresholds, and scoring logic are withheld from the agent during generation.
- The geometric mean means a model that fails one dimension badly cannot compensate with the others.
- Source lineage tracking, same-source deduplication, and near-duplicate screening; example directories and reference files are hidden and outbound network and web tools are disabled. The authors report that no trajectory reached these resources.

## Strengths

- The evaluator's agreement with experts is measured (κ = 0.90) rather than assumed.
- Per-gate pass rates show where each system drops out, separating non-delivery, non-execution, and qualification failure from weak engineering performance.
- The structural-similarity analysis tests directly whether matching the reference model predicts the score.

## Limitations

- The authors state that the benchmark depends on MATLAB/Simulink and that native simulation-based evaluation can be slow.
- Visual layout quality is reported separately and does not enter the score.
- Repository note: the paper does not report a human baseline; 96.01 is the mean score of the reference models.
- Repository note: per-task time, turn, or cost budgets are not reported.

## Related Works

- [SimBench](./simbench.md) — Also evaluates generation of simulator models (Chrono digital twins), scored by an LLM judge rather than native simulation.
- [EngDesign](./engdesign.md) — Also covers control and system design tasks checked by simulation.
