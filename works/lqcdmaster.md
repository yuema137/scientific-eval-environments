# LQCDMaster (2026)

> **English** | [简体中文](../zh/works/lqcdmaster.md)

## Overview

LQCDMaster is a skill-guided lattice-QCD computing agent released together with a 70-task benchmark of lattice-QCD measurement code, in which each generated PyQUDA workflow is checked by direct numerical comparison against an expert-written reference implementation at machine precision.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.15001>
- **Code:** <https://github.com/sjtu-sai-agents/LQCD_Master>
- **Venue:** arXiv preprint (hep-lat), 2026

## Summary

Lattice quantum chromodynamics (LQCD) computes hadronic observables from first principles, but turning a research motivation into a reliable computing workflow demands substantial expertise. LQCDMaster converts natural-language LQCD research tasks into executable PyQUDA workflows — measurement scripts, job-submission artifacts, execution logs and numerical outputs — by combining agentic planning, expert-annotated LQCD skills, and a deterministic Wick-contraction tool (`generate_einsum`) that constrains the algebraically fragile part of code generation. The evaluation contribution is a 70-task LQCD computing benchmark with expert reference implementations and a machine-precision verification protocol, released with the code.

## Tasks

70 LQCD computing tasks: 20 local two-point functions (2PTs) for mesons and baryons, 10 nonlocal Wilson-line 2PTs, 13 meson three-point functions (3PTs), 15 baryon 3PTs using sequential sources, and 12 Wilson-loop measurements. Each task pairs a natural-language research request with a hand-written expert reference implementation for the same observable, ensemble and kinematic setup. The expert-annotated skill library used by the agent contains three skills: `lqcd-physics-correlator`, `pyquda-tool`, and `pyquda-gauge`.

## Domains

Physics — lattice quantum chromodynamics, a first-principles hadronic-structure and spectroscopy setting (mesons, baryons, Wilson loops, light-cone distribution amplitudes, light nuclei and hypernuclei spectra). The workflows are executed through the PyQUDA/QUDA GPU stack with SLURM job submission, so the tasks also exercise scientific software and HPC workflow engineering, but the evaluated objective is a physics observable.

## Evaluation

- **Verification by numerical comparison.** Each generated workflow is validated by direct numerical comparison with the hand-written reference implementation for the same observable, ensemble and kinematic setup.
- **Three-way outcome labels.** *Matched* — agreement with the expert reference at machine precision, |Δ| ≲ 10⁻¹²; *Convention Mismatch* — a minor discrepancy such as a single global sign or phase transformation; *Failure* — any remaining algebraic or numerical discrepancy.
- **Reported (GPT-5.4 backbone).** 63/70 Matched, 3 Convention Mismatch, 4 Failure — 90.0% accuracy overall; per category: local 2pt 20/20 (100.0%), nonlocal 2pt 8/10 (80.0%), Wilson loop 12/12 (100.0%), meson 3pt 13/13 (100.0%), baryon 3pt 10/15 (66.7%).
- **Backbone robustness (DeepSeek-V4-Pro).** 56/70 Matched, 3 Convention Mismatch, 11 Failure — 80.0% accuracy.

## Typical Duration

Reported as implementation wall-clock rather than token budget: expert implementation takes 1–8 hours per observable, LQCDMaster 3.5–10.9 minutes, with per-observable speedups of 17×, 30×, 54×, 38× and 44×. Per-task token and turn counts are TODO(reference).

## Main Contribution

An agentic scientific-computing system for lattice QCD paired with a released 70-task benchmark at research-level difficulty, whose scoring is exact numerical agreement with expert-written code rather than a judged or textual match. The authors additionally use the system to compute a lattice quantity not previously computed — light-cone distribution amplitudes with a diagonal Wilson line — and the spectrum of proton, deuteron, triton, hyperon, hyperdeuteron and hypertriton.

## Key Design Ideas

- Correctness is defined against expert reference implementations at machine precision, giving a deterministic verifier for a domain where no answer key otherwise exists.
- A separate *Convention Mismatch* label isolates global sign/phase differences from genuine algebraic errors, so a physically equivalent workflow is not scored as a failure.
- The algebraically fragile Wick-contraction step is delegated to a deterministic tool rather than left to code generation.
- Expert-annotated skills specialize a general backbone to the domain without model training.
- The benchmark spans observable families of differing structural difficulty (2PT, nonlocal, 3PT with sequential sources, Wilson loops), which is what exposes the baryon-3PT weak point.

## Strengths

- Deterministic, high-precision verification rather than LLM judging.
- Task set, generated scripts, submission scripts and production outputs are released alongside the agent.
- Results are reported per observable family, so the failure concentration (baryon 3PTs) is visible rather than averaged away.
- Backbone robustness is checked with a second model, separating architecture effects from backbone strength.

## Limitations

- 70 tasks within a single sub-field; observable coverage is broad for LQCD but narrow as an agent benchmark.
- Reference implementations come from the same expert group that designed the tasks, so task and answer key are not independently sourced.
- Only two backbones are reported, and the comparison with a general coding agent is a supplementary section rather than a full baseline sweep.
- Repository note: the task set is not given a separate benchmark name in the paper; it is distributed with the system repository as "the LQCD benchmark with 70 scientific computing tasks".

## Related Works

- [CFDLLMBench](./cfdllmbench.md) — Also a domain-specific scientific-computing benchmark whose hardest tier is end-to-end solver configuration and execution.
- [Collider-Bench](./collider-bench.md) — Also evaluates agents on high-energy-physics analyses scored against hidden reference numerical results.
- [FEABench](./feabench.md) — Also scores agents by whether a generated simulation workflow reproduces the correct physical quantity through a real solver.
- [CodePDE](./codepde.md) — Also frames numerical scientific computing as LLM code generation checked by execution.
