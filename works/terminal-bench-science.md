# Terminal-Bench Science (2026)

> **English** | [简体中文](../zh/works/terminal-bench-science.md)

> **First appeared:** 2026-01-25 · **Source:** [Official repository creation](https://github.com/harbor-framework/terminal-bench-science)

## Overview

Terminal-Bench Science extends the Terminal-Bench framework to natural-science domains, evaluating AI agents on containerized scientific-computing workflows with deterministic programmatic verification.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Release 0.1:** <https://www.tbench.ai/news/terminal-bench-science-0-1>
- **Leaderboard:** <https://www.terminal-bench-science.ai/>
- **Code:** <https://github.com/harbor-framework/terminal-bench-science>
- **Initial call:** <https://www.tbench.ai/news/tb-science-announcement>
- **Opus 5.5 evaluation:** <https://www.anthropic.com/claude-opus-5-5>
- **License:** Apache 2.0

## Summary

Researchers contribute executable scientific workflows through proposal, implementation, and review. Agents produce analyses, simulations, proofs, code, or data products in containerized environments; task-specific tests check the artifacts. Version 0.1 replaces the early task-collection snapshot with a released suite, and reports resolution alongside dollar and token costs.

## Tasks

Version 0.1 contains 70 tasks across five broad scientific tracks. Work includes data analysis, statistical inference, simulation, optimization, theorem proving, image reconstruction, signal processing, inverse problems, sensor calibration, model fitting, classification, and scientific machine learning. The release selected 70 tasks from 386 implementation pull requests.

## Domains

Five scientific domains:

- **Life Sciences** — Biology, Ecology, Medicine, Neuroscience.
- **Physical Sciences** — Astronomy, Chemistry, Materials Science, Physics.
- **Earth Sciences** — Atmospheric, Environmental, Geosciences, Ocean Sciences.
- **Mathematical Sciences** — Applied Mathematics, Formal Mathematics, Operations Research, Statistics.
- **Engineering Sciences** — Chemical, Civil, Electrical, Mechanical Engineering.

## Evaluation

- Containerized execution with task-specific programmatic verification, including pytest checks.
- Domain review checks scientific validity; technical review checks task construction and verification; a bar raiser provides the final review.
- The 0.1 launch evaluation runs three independent trials per task across all 70 tasks. Opus 5 with Claude Code resolves 30.0%; GPT-5.6 Sol with Codex resolves 22.4%. Cost and token Pareto comparisons accompany resolution rates.
- Anthropic’s September 22 Opus 5.5 report gives 58.7% at max effort, versus its reproduced Opus 5 baseline of 29.0%. It quotes GPT-6 Astra at 64.6% from OpenAI; Opus 5.5 is therefore not the highest score in that comparison. Reported standard errors are 3.5–5 percentage points per model.
- That vendor setup allows older-model fallbacks when production safeguards intervene on biology or frontier-model-development tasks. Keep it distinct from the launch leaderboard’s 30.0% baseline and three-trial protocol.

## Typical Duration

Minutes to hours per task depending on workflow complexity (per project announcement).

## Main Contribution

A scientist-driven extension of Terminal-Bench to natural-science computational workflows with deterministic containerized verification and an explicit contribution / review protocol.

## Key Design Ideas

- Researchers supply workflows and concrete artifacts to verify.
- Scientific, technical, and final quality reviews precede inclusion.
- Versioned tasks permit reuse, regrading, or rerunning of trials.
- Later releases can add workflows and retire saturated or underspecified tasks.

## Strengths

- Direct scientist involvement gives ecological validity.
- Deterministic pytest-based grading avoids LLM-judge variance.
- Cross-domain scientific coverage under a shared execution framework.

## Limitations

- Repository note: the 70-task total covers all five broad tracks; it does not establish a count for each canonical domain in this repository.
- Repository note: launch scores and later vendor evaluations use different setups and must retain their source and version labels.
- The project describes 0.1 as the first release of a continuing benchmark, rather than a fixed, final task distribution.

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Sibling extension of Terminal-Bench, focused on long-horizon tasks broadly rather than scientific ones.
- [NatureBench](./naturebench.md) — Also science-focused, but anchored on published SOTA in Nature-family papers rather than executable workflows.
