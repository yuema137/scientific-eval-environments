# BixBench (2025)

> **English** | [简体中文](../zh/works/bixbench.md)

## Overview

BixBench is a benchmark for LLM-based agents in computational biology: over 50 real-world scenarios of practical biological data analysis with nearly 300 associated open-answer questions, in which agents explore datasets and perform long, multi-step analytical trajectories inside a containerized Jupyter environment.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.00096>
- **Code:** <https://github.com/Future-House/BixBench>
- **Dataset:** <https://huggingface.co/datasets/futurehouse/BixBench>
- **Venue:** arXiv preprint (q-bio.QM, cs.AI), 2025

## Summary

BixBench derives its scenarios from real published analyses and asks agents to explore the underlying datasets, run multi-step analyses, and interpret nuanced results. Evaluation runs in both an open-answer regime (LLM-graded) and a multiple-choice regime, with Docker-containerized code execution through an open-sourced agent harness. Frontier models perform poorly: the latest models achieve only 17% accuracy open-answer and no better than random on multiple choice.

## Tasks

50+ real-world biological data-analysis scenarios with nearly 300 open-answer questions (abstract figures; the current repository revision lists 205 questions from 60 published Jupyter notebooks), run as exploratory multi-step agent trajectories with containerized code execution.

## Domains

Computational biology and bioinformatics data analysis, derived from real published notebook analyses.

## Evaluation

- Open-answer regime with LLM-based grading and a multiple-choice regime with exact match; majority vote over replicas per the official repository.
- **Reported.** Frontier models (GPT-4o, Claude 3.5 Sonnet) achieve only 17% accuracy in the open-answer regime and no better than random on multiple choice.

## Typical Duration

Long, multi-step analytical trajectories per scenario; budgets are TODO(reference).

## Main Contribution

Real published analyses recast as open-ended agent tasks, showing that frontier agents fail the exploratory data analysis practicing computational biologists do daily.

## Key Design Ideas

- Scenarios come from real notebooks, so difficulty reflects genuine analytical practice.
- The open-answer/multiple-choice pairing separates generation ability from recognition.
- Containerized execution makes multi-step trajectories reproducible across agents.

## Strengths

- Ecologically grounded task provenance from published analyses.
- The 17%-and-random result set a stark early baseline for bioinformatics agents.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation. Abstract and current repository state different question counts (≈296 vs. 205), apparently reflecting a dataset revision.

## Related Works

- [GenoTEX](./genotex.md) — Also real-analysis-derived bioinformatics agent evaluation, with expert-curated reference pipelines.
- [BioAgent Bench](./bioagent-bench.md) — Also end-to-end bioinformatics pipelines, artifact-graded with robustness perturbations.
- [HeurekaBench](./heurekabench.md) — Also derives open-ended questions from published studies and their code, in single-cell biology.
