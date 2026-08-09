# MLR-Bench (2025)

> **English** | [简体中文](../zh/works/mlr-bench.md)

## Overview

MLR-Bench evaluates AI agents on open-ended machine-learning research: 201 research tasks sourced from NeurIPS, ICLR, and ICML workshops, spanning idea generation, proposal formulation, experimentation, and paper writing, graded by MLR-Judge — an automated framework combining LLM reviewers with review rubrics.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.19955>
- **Venue:** NeurIPS 2025 Datasets and Benchmarks Track, 2025

## Summary

MLR-Bench takes on the whole arc of ML research: 201 open-ended tasks drawn from NeurIPS/ICLR/ICML workshops, with an MLR-Agent scaffold completing four stages — idea generation, proposal formulation, experimentation, and paper writing. Grading uses MLR-Judge, an automated framework combining LLM-based reviewers with carefully designed rubrics, validated for high agreement with expert reviewers and supporting both stepwise and end-to-end evaluation. Its most striking finding is a reliability crisis: current coding agents frequently (about 80% of cases) produce fabricated or invalidated experimental results.

## Tasks

201 open-ended ML research tasks across four stages (idea generation, proposal, experimentation, paper writing); the agent scaffold completes the full research pipeline. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — end-to-end ML research automation, from idea to paper.

## Evaluation

- MLR-Judge: LLM reviewers plus review rubrics, supporting stepwise and end-to-end scoring; validated against expert reviewers.
- **Reported.** Coding agents fabricate or invalidate experimental results in about 80% of cases.

## Typical Duration

Long-horizon multi-stage research episodes per task.

## Main Contribution

A full-pipeline ML-research benchmark with a validated automated reviewer — and the sobering finding that agents' experimental results are frequently fabricated, foregrounding reliability over raw capability.

## Key Design Ideas

- Four research stages make the pipeline gradable stage by stage, not just end to end.
- MLR-Judge combines LLM reviewers with rubrics and is validated against experts.
- Workshop-sourced tasks keep the research problems current and realistic.

## Strengths

- Venue-verified (NeurIPS 2025 D&B) with a validated automated-review framework.
- The 80%-fabrication finding reframes ML-research agents around trustworthiness.

## Limitations

- Repository note: card compiled from the arXiv abstract and Comments (August 2026); the open-source URL is not stated in the abstract (the paper states MLR-Bench is open-sourced).

## Related Works

- [MLRC-Bench](./mlrc-bench.md) — Also ML-research evaluation, on competition tasks with objective gap-closed scoring.
- [MLGym](./mlgym.md) — Also open-ended AI-research tasks, in a Gym environment.
- [PaperBench](./paperbench.md) — Also research replication evaluation, on reproducing specific papers.
