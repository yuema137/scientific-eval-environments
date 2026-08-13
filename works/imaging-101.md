# Imaging-101 (2026)

> **English** | [简体中文](../zh/works/imaging-101.md)

## Overview

Imaging-101 is a benchmark of 57 expert-verified computational-imaging tasks spanning six scientific domains, each grounded in a peer-reviewed paper and its open-source reference implementation, used to evaluate LLM coding agents on building complete reconstruction pipelines.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** https://arxiv.org/abs/2607.10789
- **Code:** https://github.com/AI4ImagingLab/imaging-101-release
- **Project:** https://starpacker.github.io/agent-imaging-website/

## Summary

Computational imaging recovers hidden signals from indirect, noisy measurements, and assembling a correct reconstruction pipeline requires domain expertise in the measurement physics as well as in numerical inverse solvers. Imaging-101 canonicalizes 57 such tasks into a standardized four-stage pipeline — preprocessing, forward physics modeling, inverse solver, and visualization — so that agent output can be graded stage by stage. Three evaluation tracks (planning, function-level unit tests, and end-to-end reconstruction) probe different agent capabilities over the same task set. Seven frontier LLMs are evaluated, and the authors report systematic failures in algorithm selection, physical-convention handling, and pipeline integration that general coding benchmarks do not surface.

## Tasks

57 tasks across six scientific domains: astronomy, biology, chemistry & materials science, earth science, medicine, and physics. Every task is grounded in a peer-reviewed paper and its open-source reference implementation; construction used an expert-in-the-loop pipeline that reproduced reference runs, refactored the code into the standardized four-stage layout, synthesized unit tests from captured input/output, and drafted task tutorials. Each task ships a `README.md`, a reference plan (`plan/approach.md`, `plan/design.md`), data, requirements, per-function signatures with docstrings, paired pytest suites, and a `metrics.json` of acceptance thresholds. The astronomy tasks include several Event Horizon Telescope black-hole imaging variants (`eht_black_hole_original` — recovering a black-hole radio image from gain-corrupted visibilities — plus dynamic, uncertainty-quantification, feature-extraction and tomography variants), `exoplanet_imaging` (detecting a faint exoplanet from a coronagraphic image sequence), `lucky_imaging` (reconstructing a high-resolution lunar image from a short-exposure video), `shack_hartmann`, and `shapelet_source_reconstruction`. Exact per-domain task counts: `TODO(reference)`.

## Domains

Astronomy is one of the six named domains, instantiated as radio-interferometric imaging (Event Horizon Telescope black-hole reconstruction from visibilities), high-contrast exoplanet imaging, atmospheric-turbulence lucky imaging, Shack–Hartmann wavefront sensing, and shapelet-based source reconstruction — the scored output in each case is an astronomical image or source estimate. Co-domains from the remaining task groups are Biology, Chemistry, Materials Science, Earth Science, Medicine & Health, and Physics.

## Evaluation

Three tracks over the same 57 tasks. **Planning:** the agent produces algorithm documentation and a module architecture, scored per pipeline component (preprocessing, forward physics, inverse solver) by a two-stage human–LLM pipeline in which domain experts assign a binary pass/fail per dimension; the Overall score requires all three components correct. **Function-level:** given the README, the reference plan, and a target function signature and docstring, the model iterates in a sandboxed environment until it passes the paired pytest suite or exhausts its budget; reported as Module % (all functions in a module pass) and Function % (individual functions passing). **End-to-end:** given only the README, `data/`, and `requirements.txt`, the agent must produce the complete `src/` pipeline, execute it, and deliver a reconstruction meeting the thresholds in `metrics.json`, scored with normalized cross-correlation (NCC) and normalized root-mean-square error (NRMSE). Reported headline results for the seven models evaluated (Claude-4.6-Opus, DeepSeek-V3, Gemini-3.1-Pro, GPT-5.4, Qwen3.6-Plus, Kimi-k2.5, GLM-5): best planning Overall 30/57 (52.6%), best function-level Module Overall 13/57 (22.8%), best end-to-end success rate 17/57 (29.8%).

## Typical Duration

No wall-clock or token budget is reported. The function-level track caps the agent at a fixed budget of 10 reflection rounds per function; mean rounds to success range from 2.60 to 9.28 across models. The end-to-end track reports mean rounds to success between 1.45 and 2.75.

## Main Contribution

The authors present the first benchmark targeting LLM coding agents on scientific computational imaging: 57 expert-verified, paper-grounded tasks canonicalized into a common four-stage pipeline, with three evaluation tracks that separate planning, module implementation, and end-to-end reconstruction. Their evaluation of seven frontier LLMs identifies capability gaps — algorithm selection, physical-convention handling, and pipeline integration — that they argue are specific to computational imaging and not exposed by general coding benchmarks.

## Key Design Ideas

- Canonicalizing heterogeneous imaging papers into one fixed four-stage pipeline (preprocessing → forward physics modeling → inverse solver → visualization), which makes stage-level attribution of failures possible across domains.
- Three tracks of increasing autonomy over an identical task set: planning (design only), function-level (implement one module against unit tests with the reference plan supplied), end-to-end (build and run the whole pipeline from the README and data alone).
- Grounding every task in a peer-reviewed paper plus its open-source reference implementation, with unit tests synthesized from captured reference input/output.
- Numerical acceptance thresholds stored per task in `metrics.json`, with image-quality scoring by NCC and NRMSE rather than text similarity.
- Human–LLM planning judgment: domain experts assign binary pass/fail per pipeline component with LLM-judge assistance, and Overall requires all components correct.

## Strengths

- Execution-graded rather than answer-matched: end-to-end tasks are scored by running the agent's code and measuring reconstruction quality against calibrated tolerances.
- The three-track design separates whether a model fails at algorithm choice, at implementing a single module, or at integrating a full pipeline.
- Genuinely multi-domain, with the astronomy slice covering real instrument-specific reconstruction problems (interferometric visibilities, coronagraphy, wavefront sensing) rather than generic image restoration.
- Code and evaluation harness released under an MIT license, with a public project page.

## Limitations

- Low absolute scores concentrate the signal: the best end-to-end result is 17/57, so the benchmark currently separates models mostly at the bottom of its range.
- Planning is scored by binary expert pass/fail per component with LLM-judge assistance, which is coarser and less reproducible than the execution-based tracks.
- Repository note: per-domain task counts are not stated in the main text, so the size of the astronomy slice relative to the other five domains could not be verified from the primary source.
- Repository note: the function-level track supplies the reference plan and function signatures, so it measures implementation given a correct design rather than autonomous problem formulation.

## Related Works

- [SciCode](./scicode.md) — research-grounded scientific coding tasks decomposed into subproblems and graded by execution.
- [ResearchCodeBench](./researchcodebench.md) — implementing code for methods drawn from recent papers, graded against reference implementations.
- [AstroVisBench](./astrovisbench.md) — astronomy-specific evaluation of agent-written analysis and visualization code.
- [ScienceAgentBench](./scienceagentbench.md) — data-driven scientific discovery tasks graded by executing agent-produced code.
