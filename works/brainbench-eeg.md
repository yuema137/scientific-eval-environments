# BrainBench (EEG) (2026)

> **English** | [简体中文](../zh/works/brainbench-eeg.md)

## Overview

BrainBench (EEG) benchmarks LLMs on comprehensive EEG understanding: instruction-conditioned analysis across four subsets — Foundational Analysis, Sleep Assessment, Neurocognitive Assessment, and Physiological Integration — over 17 datasets, where a system must analyze EEG recordings and produce a scientifically grounded report.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.04156>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Distinct from the earlier neuroscience-result-prediction BrainBench, this benchmark targets EEG signal understanding. Given an instruction and EEG recordings (with optional physiological signals), a system must perform the analysis and produce a scientifically grounded report and, when required, artifacts. It spans four subsets — Foundational Analysis, Sleep Assessment, Neurocognitive Assessment, and Physiological Integration — over 17 datasets, and evaluates models under two execution paradigms: autonomous code execution with CodeAct and structured agentic analysis with BrainAgent, across more than 100K executions. Outputs are validated along numerical, categorical, set, sequence, semantic, and artifact dimensions, with results varying substantially across models, subsets, difficulty, and paradigm.

## Tasks

Instruction-conditioned EEG-analysis tasks across four subsets and 17 datasets; the system analyzes recordings and produces reports/artifacts, under autonomous-code-execution (CodeAct) and agentic (BrainAgent) paradigms. Interactive-agentic. Exact task, instance, and model counts are TODO(reference) — not resolved in the arXiv abstract.

## Domains

Neuroscience & Cognitive Science — electroencephalography analysis: signal processing, quantitative evidence, and scientific interpretation across foundational, sleep, neurocognitive, and physiological tasks.

## Evaluation

- Multi-faceted validation: numerical, categorical, set, sequence, semantic, and artifact checks, over 100K+ executions.
- **Reported.** Results vary substantially across models, subsets, difficulty levels, and execution paradigms; specific figures are TODO(reference).

## Typical Duration

Multi-step agentic analysis episodes per EEG task (code execution or structured agentic workflow).

## Main Contribution

An instruction-conditioned, execution-grounded benchmark for EEG understanding that spans the analysis workflow — from signal processing to scientific interpretation — and evaluates both autonomous-code and agentic paradigms.

## Key Design Ideas

- Six validation modes (numerical … artifact) grade heterogeneous EEG-analysis outputs.
- Two execution paradigms (CodeAct vs BrainAgent) compare autonomy styles on the same tasks.
- Four clinically/scientifically meaningful subsets structure the difficulty range.

## Strengths

- Broad dataset coverage (17) and large execution scale (100K+) for a specialized modality.
- Execution-grounded validation rather than text-similarity scoring.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); several scale figures (task, instance, and model counts) are unresolved LaTeX macros on the arXiv page and are marked TODO(reference). The code and benchmark are stated as "to be released" — no URL is yet available.
- Repository note: name collision — this is a different work from the documented [BrainBench](./brainbench.md) (neuroscience-result prediction, 2024).

## Related Works

- [BrainBench](./brainbench.md) — The earlier, unrelated BrainBench: predicting neuroscience experimental outcomes.
- [Rodent-Bench](./rodent-bench.md) — Also multimodal neuroscience-data analysis, on rodent behavior video.
- [EnvTrace](./envtrace.md) — Also execution-grounded evaluation of scientific analysis code, via trace validation.
