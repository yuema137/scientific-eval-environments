# Materials Hypothesis Generation (2025)

> **English** | [简体中文](../zh/works/materials-hypothesis.md)

## Overview

This work evaluates goal-driven, constraint-guided LLM agents for materials discovery: given research goals and specific constraints, the agents generate hypotheses for achieving them, scored by a scalable evaluation metric designed to emulate how a materials scientist would critically judge a hypothesis.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.13299>
- **Venue:** NAACL 2025

## Summary

Published as "Hypothesis Generation for Materials Discovery and Design Using Goal-Driven and Constraint-Guided LLM Agents," this NAACL 2025 work pairs a curated dataset from recent journal publications with a novel scalable evaluation metric that emulates a materials scientist's critical judgment of a hypothesis. The LLM agents are goal-driven and constraint-guided: they generate hypotheses for achieving stated goals under specific constraints, and the metric scores whether those hypotheses are worth pursuing — providing an evaluation path for a task where ground truth is inherently open-ended.

## Tasks

Hypothesis generation under explicit goals and constraints, over a dataset curated from recent journal publications; scored by a scalable, expert-emulating metric. Dataset size figures are TODO(reference) — not stated in the abstract.

## Domains

Materials science — hypothesis generation for materials discovery and design, grounded in recent published research goals and constraints.

## Evaluation

- A scalable evaluation metric emulating a materials scientist's critical assessment of a hypothesis.
- **Reported.** No numeric headline in the abstract; the contribution is the curated dataset plus the evaluation metric.

## Typical Duration

Single-episode hypothesis generation per goal/constraint specification.

## Main Contribution

An evaluation path for LLM materials-hypothesis generation — a curated dataset and an expert-emulating metric that make an open-ended discovery task measurable.

## Key Design Ideas

- Explicit goals and constraints make hypotheses checkable against a specification.
- The scalable metric emulates expert critique rather than requiring an exact reference.
- Curation from recent publications keeps the goals realistic and current.

## Strengths

- Venue-verified (NAACL 2025) and aimed at the hardest-to-grade stage of discovery.
- The expert-emulating metric addresses the open-endedness that blocks hypothesis benchmarks.

## Limitations

- Repository note: the paper foregrounds its goal-driven/constraint-guided agent method alongside the dataset and metric; this card centers the dataset and evaluation contribution. Dataset scale numbers are not in the abstract and remain TODO(reference); no code/dataset URL is verifiable from the arXiv page.

## Related Works

- [AlchemyBench](./alchemybench.md) — Also LLM-driven materials discovery, at the synthesis-planning rather than hypothesis stage.
- [MOOSE-Chem](./moose-chem.md) — Also LLM scientific-hypothesis rediscovery, in chemistry.
- [ResearchClawBench](./researchclawbench.md) — Also end-to-end research-finding rediscovery, spanning materials among its domains.
