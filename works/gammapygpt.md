# gammapyGPT (2025)

> **English** | [简体中文](../zh/works/gammapygpt.md)

## Overview

An agent that writes, executes and validates Gammapy analysis code for ground-based gamma-ray astronomy inside a controlled execution environment, together with an accompanying benchmarking suite of gamma-ray analysis tasks whose numerical outputs are checked against expected values.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.26110>
- **Demo:** <https://majestix-vm8.zeuthen.desy.de>
- **Venue:** ICRC 2025 proceedings, PoS(ICRC2025)753

## Summary

Specialized scientific libraries such as Gammapy lack the documentation volume, example corpus and API stability that foundation models rely on for popular frameworks, so code generated against them is often outdated or wrong. The work addresses this for Gammapy with an agent that expands a user prompt into a governed chat history, emits a single Python script, executes it under a pared-down environment with a data pointer and a hard time limit, and feeds a concise error summary back into the next iteration until the script validates or the attempt budget is exhausted. Retrieval-augmented generation is optional, injecting top-k tutorial snippets when available. The contribution is packaged as a small Python package (`gammapygpt`) with a minimal web demo and a benchmarking harness.

## Tasks

Four domain-specific Gammapy tasks: **ObservationList** (select observations for a given source and report the number of observations), **ReflectedSignificance** (compute a reflected-region significance for a source), **ReflectedSpectrum** (perform a reflected-region spectral extraction and report total energy flux and spectral index), and **Source3DAnalysis** (reduce all available observations of a source to a `MapDataset` and fit a spatial–spectral model). Tasks are defined against real observational data reached through a data pointer (`PHOTON_STORAGE`) rather than synthetic fixtures.

## Domains

Astronomy — specifically ground-based gamma-ray astronomy and high-energy astrophysics, in the Cherenkov Telescope Array Observatory analysis context. The scored quantities are astronomical results (observation counts, region significance, energy flux, spectral index, spatial–spectral source fits) obtained through the Gammapy analysis library, so the evaluated objective is an astronomical data-analysis one even though the agent's output medium is code.

## Evaluation

- Generated scripts are executed in a controlled environment; validation is per-task, with criteria scaling to task complexity. ObservationList requires an exact integer match; the spectral tasks compare floats against expected values within tolerance; Source3DAnalysis passes if the script runs end-to-end within the timeout, a relaxation the authors attribute to the task's complexity.
- The harness logs exception classes, a compact traceback tail, input / cached-input / output / reasoning token counts, and the attempt index at which validation passed — so a pass is recorded together with how many correction rounds it took.
- **Reported.** Two OpenAI reasoning models (o3 and GPT-5) were run at the highest available reasoning effort; on the smaller per-source tasks both reached a 100% pass rate in the authors' runs, with the more recent model slightly faster.

## Typical Duration

Per-task agent sessions with an iterative correct-and-retry loop bounded by an attempt budget (value not stated) and a hard wall-clock limit on each script execution (value not stated). A typical successful run recorded 7.3k output tokens, of which roughly 6.5k were reasoning tokens.

## Main Contribution

An execution-grounded code-generation agent for a scientific library that foundation models handle poorly, delivered with a benchmarking suite that validates the agent's *numerical analysis results* rather than the plausibility of its code.

## Key Design Ideas

- Validation is the loop's controller: execution output, not model self-assessment, decides whether an attempt passed and what error summary seeds the next attempt.
- Pass criteria are graded to task difficulty — exact integer match, float-with-tolerance, and end-to-end execution for the hardest task.
- Instrumentation captures the attempt index at which validation passed, separating first-shot success from recovered-after-error success.
- Retrieval of tutorial snippets is an optional switch, letting the contribution of RAG be isolated from the base model.
- Scripts run under a stripped environment carrying only a data pointer, keeping the executed task reproducible and bounded.

## Strengths

- Grounds scoring in real Gammapy outputs against real observational data, not in code similarity or judged plausibility.
- Token and traceback logging make failure modes and cost visible per attempt rather than only in aggregate pass rates.
- Targets a genuine gap: an actively developed, thinly documented instrument-analysis library where model priors are weakest.

## Limitations

- Only four tasks, all single-source Gammapy analyses; the suite is small relative to the analysis surface of the library.
- The hardest task (Source3DAnalysis) is scored on execution completion rather than on the correctness of the fitted spatial–spectral model, so a passing run need not be scientifically correct.
- Only two proprietary reasoning models were evaluated, and both saturated the smaller tasks at 100%, leaving little discriminative headroom as reported.
- The paper states the accompanying code was not yet public at publication time, so the benchmark's reusability by third parties is unconfirmed.
- Repository note: a short conference-proceedings contribution (ICRC 2025) that explicitly summarizes design and current status; several harness parameters, including the attempt budget and the execution timeout, are described qualitatively without values.

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — Also scores coding agents on astrophysics-domain numerical outputs with an external validation framework rather than agent self-reports.
- [Stargazer](./stargazer.md) — Also evaluates agents on astronomical analysis with explicit physical pass criteria.
- [SciCode](./scicode.md) — Also evaluates scientific code generation with execution-based correctness checks over research-level tasks.
- [SUPER](./super.md) — Also scores agents on getting real research code to run correctly in a controlled environment.
