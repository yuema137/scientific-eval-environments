# MatCha (2025)

> **English** | [简体中文](../zh/works/matcha.md)

## Overview

MatCha is a multimodal benchmark on materials characterization: 1,500 questions across four key stages of materials research comprising 21 distinct tasks over real characterization imaging data, revealing a significant performance gap between multimodal LLMs and human experts.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.09307>
- **Code:** <https://github.com/FreedomIntelligence/MatCha>
- **Dataset:** <https://huggingface.co/datasets/FreedomIntelligence/MatCha>
- **Venue:** EMNLP 2025 Findings (per the official repository; arXiv metadata carries no venue)

## Summary

Published as "Can Multimodal LLMs See Materials Clearly?", MatCha asks whether MLLMs can do the perception-and-interpretation work of materials characterization. Its 1,500 questions span four key stages of materials research across 21 distinct tasks, grounded in real-world characterization imaging data. Models show a significant gap from human experts, degrade on questions requiring higher-level expertise, and are not rescued by simple few-shot or chain-of-thought prompting.

## Tasks

1,500 questions across four materials-research stages comprising 21 distinct tasks over real characterization imagery; static multimodal QA.

## Domains

Materials science — materials characterization across the research workflow, on real characterization imaging data.

## Evaluation

- Accuracy across the 21 tasks with a human-expert baseline for comparison.
- **Reported.** Significant gap from human experts; degradation on higher-expertise questions; few-shot and chain-of-thought prompting do not alleviate the limitations.

## Typical Duration

Single-turn multimodal questions; no interactive setting.

## Main Contribution

A stage-structured characterization benchmark that maps where MLLM materials perception breaks down — and shows the failure is expertise depth, not fixable by prompting tricks.

## Key Design Ideas

- Four research stages order tasks by where in the workflow characterization is used.
- A human-expert baseline turns "hard" into a measured gap.
- Testing few-shot and CoT explicitly rules out cheap fixes.

## Strengths

- Real characterization imagery with a broad 21-task span.
- The prompting-does-not-help finding sharpens the diagnosis of the deficit.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the EMNLP 2025 Findings venue is a repository claim, not in arXiv metadata. The abstract does not enumerate the characterization modalities (e.g., SEM/TEM/XRD).

## Related Works

- [MatVQA](./matvqa.md) — Also multimodal materials characterization reasoning, with shortcut-resistant construction.
- [MatQnA](./matqna.md) — Also characterization QA, organized explicitly by ten characterization methods.
- [MaCBench](./macbench.md) — Also multimodal chemistry/materials evaluation.
