# First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope (2026)

> **English** | [简体中文](../zh/works/first-head-to-head-comparison-of-agentic-ai-applie.md)

## Overview

A controlled head-to-head evaluation in which two commercial agentic coding systems, Claude Code and Codex, are given an identical written specification and identical hardware and asked to execute an end-to-end gravitational-wave analysis pipeline on simulated Einstein Telescope data without human intervention, with both the scientific outputs and the agents' process behaviour recorded and compared.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.28916>
- **Supplemental material:** <https://gianlucainguglia.eu/agent_experiment.pdf>

## Summary

The study asks whether two agentic AI systems, given the same instructions and the same machine, produce the same science and reach it the same way. A single specification document (`exp.md`) describes a seven-stage gravitational-wave pipeline — power spectral density estimation from raw Einstein Telescope simulated strain, geometric template-bank generation, injection and matched-filter recovery of 100 binary-black-hole signals, results and diagnostic plots, an LLM-written manuscript in the style of Physical Review D, and a self-reported `metrics.json`. Claude Code and Codex each executed the specification twice, once with unrealistically loud injections and once with signals rescaled to a physically motivated signal-to-noise range. The scientific results converged in both runs, but the runtimes, memory footprints, error-handling styles and manuscripts diverged sharply, and in the second run a difference in how each agent read one instruction produced a genuine scientific divergence.

## Tasks

One task, instantiated as four autonomous pipeline executions (two agents × two runs). The specification covers seven stages: PSD estimation from ten raw GWF frame files using Welch's method; geometric template-bank generation with `pycbc_geom_nonspinbank` using the IMRPhenomD approximant, a 5 Hz lower frequency cutoff and a minimum match of 0.97; injection of 100 pre-generated BBH waveforms into 2-second noise segments; a matched-filter search with detection threshold ρ = 8; generation of results and diagnostic plots; production of a LaTeX manuscript in Physical Review D style through a two-model API strategy; and a `metrics.json` self-report. Injection parameters were drawn randomly with component masses m₁ ∈ [50, 80] M☉ and m₂ ∈ [20, 50] M☉ and luminosity distances d_L ∈ [1000, 5000] Mpc; the noise is simulated Einstein Telescope E1 strain from the ET Mock Data Challenge. Run 1 used loud injections with ρ ≫ 8; Run 2 rescaled the targets to ρ ∈ [7, 50]. The specification also stated quantitative acceptance thresholds on template-bank size, detection efficiency and total runtime. Both agents ran on the same local server (four NVIDIA RTX 4000 Ada GPUs, 64 CPU cores, Python 3.9, PyCBC 2.8.2). Claude Code used `claude-haiku-4-5` for file I/O and data summarisation and `claude-sonnet-4-6` for scientific writing; Codex used GPT-5 mini for schema-constrained JSON summarisation through the Responses API and GPT-5.2 for LaTeX writing.

## Domains

Astronomy. The evaluated objective is gravitational-wave source science: recovering binary-black-hole signals injected into simulated Einstein Telescope detector noise, with detection efficiency and recovered signal-to-noise ratios as the scored scientific outputs, and the astrophysical parameters of the injected population (component masses, luminosity distances) defining the task. Physics is a secondary co-domain through the waveform modelling and detector-noise characterisation the pipeline rests on.

## Evaluation

Two families of measurements are reported side by side. The **scientific-output** measures are template-bank size, detection efficiency (fraction of injections recovered above ρ = 8), mean/median/minimum/maximum recovered SNR, peak memory usage and total runtime. The **behavioural** measures are counted from the agents' logs: pipeline restarts, silent deviations from the specification versus explicit self-corrections, unsolicited optimisations, token-budget adjustments, divergences in instruction interpretation, and manuscript quality judged on page length, number of equations, presence of fabricated content and reference handling. In Run 1 both agents recovered every injection (detection efficiency 1.00) with near-identical template banks (Claude 3399, Codex 3396) and mean SNR (298.8 versus 298.7), but Claude finished in 3.38 minutes at 810 MB peak memory while Codex took 15.92 minutes at 187 MB. In Run 2 Claude reached detection efficiency 1.00 with mean SNR 27.93 in 3.54 minutes; Codex reached 0.99 with mean SNR 29.02 in 5.98 minutes. Run 1 contained three mismatches between the written specification and the runtime environment — an invalid command-line flag, a file-indexing discrepancy and a PSD header format issue — which Claude Code corrected silently and continued past without restarting, while Codex diagnosed each one explicitly, patched the relevant script and restarted the affected stage. The authors label these `proceed-and-correct` and `diagnose-and-restart` behavioural profiles. In Run 2 the single-instruction divergence is the headline result: Claude silently shifted the lower bound of the target SNR distribution from 7 to 8, while Codex read [7, 50] literally and consequently produced one injection recovered at ρ̂ = 7.97, just below the detection threshold. Claude also autonomously raised the `max_tokens` parameter of its manuscript-writing call from 4096 to 16000.

## Typical Duration

Wall-clock runtime for the full pipeline is the primary cost measure: 3.38 minutes (Claude) versus 15.92 minutes (Codex) in Run 1, and 3.54 versus 5.98 minutes in Run 2, alongside peak memory of 810 MB versus 187 MB in Run 1. Token costs were not measured; the authors list this omission among the study's limitations.

## Main Contribution

The authors present this as a first controlled comparison of two state-of-the-art agentic AI systems executing an identical, fully specified gravitational-wave analysis autonomously on shared infrastructure, and as evidence that agents which converge on the same scientific answer can nonetheless differ in ways that matter for scientific practice. The framing conclusion is that speed and throughput favour the Claude Code behavioural profile while auditability and reproducibility favour the Codex profile, and that silent reinterpretation of an ambiguous instruction can propagate into the science rather than being caught as an error.

## Key Design Ideas

- A single written specification document is the experimental control: both agents receive the identical `exp.md`, identical compute, and identical input data, so behavioural divergence cannot be attributed to differing instructions.
- Process behaviour is treated as a first-class measurement alongside scientific accuracy — restarts, silent deviations and unsolicited optimisations are counted rather than described anecdotally.
- The experiment is run twice at different injection loudness, so that a regime where the science is trivially recoverable can be separated from one where an instruction ambiguity has observable scientific consequences.
- The pipeline deliberately terminates in an autonomously written PRD-style manuscript, extending the evaluation past numerical outputs to the reporting artifact, which is inspected for fabricated content and reference quality.
- A `metrics.json` self-report is required from each agent, giving a checkable record of what the agent believed it had achieved against the independently measured outcome.
- Intermediate data representations between the two models used within each agent (summariser and writer) are examined as a failure surface in multi-model pipelines.

## Strengths

- The control is genuinely tight: same specification, same server, same library versions, same input data, with the two agents launched in parallel.
- The most interesting finding is negative and specific — identical converged science masking a silent specification deviation — rather than a leaderboard ranking.
- Behavioural profiles are grounded in enumerated incidents (three named environment mismatches in Run 1, a named parameter change in Run 2) rather than impressions.
- Cost dimensions that agent evaluations often omit, wall-clock runtime and peak memory, are reported per run for both agents.
- The specification document, the autonomously generated manuscripts and supporting material are released, so the exact prompt that produced the behaviour is inspectable.
- The authors state the confounds and the narrow generality of the result plainly rather than over-claiming.

## Limitations

- The authors describe the study as "a first rudimentary test": a single pipeline with two runs per agent, four executions in total, so the observed behavioural profiles may not generalise.
- Token costs were not measured, leaving the economic side of the speed-versus-auditability trade-off unquantified.
- Different underlying LLMs were used for manuscript writing by each agent, which confounds agent-harness effects with model effects.
- Behavioural observations were reconstructed from logs after the fact; the authors note that a rigorous study would instrument the agents directly.
- The Run 2 SNR range does not fully probe the sub-threshold regime, so the instruction-interpretation divergence is observed on a single marginal injection.
- Repository note: there is no reusable task suite, held-out split or public scoring harness — the contribution is a comparison study built around one specification, so results cannot be extended to new agents without re-running the authors' setup.
- Repository note: the paper is a single-author preprint with no peer-reviewed venue recorded, and the scientific outputs are scored against the specification's own thresholds rather than against an independent ground-truth pipeline.

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — the reusable task-suite counterpart in the same gravitational-wave setting, where this work is a two-agent comparison on one pipeline.
- [Terminal-Bench Science](./terminal-bench-science.md) — also evaluates coding agents executing scientific pipelines end to end in a terminal environment.
- [Quantifying the Reproducibility of Astrophysical Methods with Large Language Models and Information Theory](./quantifying-the-reproducibility-of-astrophysical-m.md) — another single-case-study astrophysics evaluation that scores what agents reconstruct from a written specification.
- [ReplicationBench](./replicationbench.md) — astrophysics replication tasks, sharing the concern with whether an agent's result faithfully follows the source description.
- [Stargazer](./stargazer.md) — astronomy agent evaluation on quantitative model fitting, complementary to this work's process-behaviour focus.
