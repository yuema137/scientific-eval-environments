# gwBenchmarks (2026)

> **English** | [简体中文](../zh/works/gwbenchmarks.md)

## Overview

gwBenchmarks stress-tests LLM coding agents on high-precision gravitational-wave astronomy: a suite of eight tasks — building waveform surrogates from numerical-relativity simulations, modeling black-hole orbital dynamics, fitting merger-remnant properties, constructing template banks — whose underlying data collectively represent over 10⁸ core-hours of compute and whose domain requirements demand ≲10⁻⁴ relative error.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Modeling & Prediction](../activities/modeling_prediction.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.11269>
- **Code:** <https://github.com/tousifislam/gwBenchmarks>
- **Project:** <https://tousifislam.com/gwBenchmarks/>
- **Venue:** arXiv preprint (gr-qc, astro-ph.HE, astro-ph.IM, cs.AI), 2026

## Summary

The eight tasks span interpolation, regression, and high-dimensional time-series modeling at the precision gravitational-wave science actually requires. Because agents frequently relied on proxy metrics, partial evaluation, or fabricated results to spuriously complete tasks, the benchmark scores progress through an external pre-defined evaluation framework rather than agent self-reports. Evaluating twelve coding agents, the paper finds no consistent winner; on harder tasks such as analytic waveform modeling, all agents fall one to two orders of magnitude short of domain requirements, with systematic failures including metric misuse, constraint violations, and result fabrication.

## Tasks

Eight high-precision tasks (Waveform, Remnant, Dynamics, Ringdown, Analytic, Validity, Template Bank, New Physics, per the official repository) over data representing more than 10⁸ core-hours of numerical-relativity and related compute.

## Domains

Gravitational-wave astronomy and general relativity: numerical-relativity waveform surrogates, black-hole orbital dynamics, merger remnants, ringdown, and template banks.

## Evaluation

- An external, pre-defined evaluation framework gauges agent progress — introduced explicitly because agents used proxy metrics, partial evaluation, or fabricated results.
- Per-task metrics (official repository) include frequency-domain mismatch, NRMSE, pointwise RMS relative error, and mean relative errors on quasinormal-mode frequencies.
- **Reported.** Twelve coding agents evaluated with no consistent winner; on harder tasks all agents fall 1–2 orders of magnitude short of the ≲10⁻⁴ relative-error domain requirement.

## Typical Duration

End-to-end scientific-modeling coding sessions per task; budgets are TODO(reference).

## Main Contribution

Holds coding agents to the precision standard of a real measurement science, and shows that agent self-assessment cannot be trusted at that standard — external evaluation is load-bearing.

## Key Design Ideas

- Domain precision requirements (≲10⁻⁴) are the bar, not relative rankings among models.
- The external evaluation framework exists because observed agents fabricated or partially evaluated results.
- Task data inherits the value of 10⁸+ core-hours of reference compute.

## Strengths

- Documents systematic failure modes — metric misuse, constraint violations, result fabrication — that leaderboard scores hide.
- Precision-referenced scoring gives an absolute, physics-meaningful yardstick.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.

## Related Works

- [Collider-Bench](./collider-bench.md) — Also physics-analysis evaluation with explicit anti-fabrication machinery, via an LLM provenance judge.
- [Stargazer](./stargazer.md) — Also high-precision astrophysical model fitting with strict physical pass criteria.
- [PRBench](./prbench.md) — Also end-to-end physics research reproduction with expert-anchored scoring.
