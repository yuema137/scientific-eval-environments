# MedAgentGym (2025)

> **English** | [简体中文](../zh/works/medagentgym.md)

## Overview

MedAgentGym is a scalable agentic environment for code-centric reasoning in biomedical data science: 72,413 task instances across 129 categories derived from 12 authentic real-world biomedical scenarios, each encapsulated in an executable sandbox with interactive feedback and verifiable ground truth.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Data Analysis & Statistical Inference](../activities/data_analysis_statistical_inference.md)
- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.04405>
- **Code:** <https://github.com/wshi83/MedAgentGym>
- **Project:** <https://wshi83.github.io/MedAgentGym-Page>
- **Dataset:** <https://huggingface.co/MedAgentGym>
- **Venue:** ICLR 2026 (per the official repository)

## Summary

MedAgentGym doubles as benchmark and training environment: its sandboxed tasks carry detailed specifications, interactive feedback mechanisms, verifiable ground-truth annotations, and scalable trajectory generation for offline and online reinforcement learning. The paper benchmarks 29 LLMs on the suite and trains Med-Copilot, which gains +43.02% from offline and +45.28% from online RL — presented as a cost-effective, privacy-preserving alternative competitive with proprietary models. Some underlying datasets require credentialed PhysioNet access (per the official repository).

## Tasks

72,413 coding task instances across 129 categories from 12 real-world biomedical data-science scenarios, each in an executable sandbox with interactive feedback.

## Domains

Biomedical data science, including EHR-derived scenarios (MIMIC-III, eICU per the official repository).

## Evaluation

- Verifiable ground-truth annotations checked in executable sandboxes.
- **Reported.** 29 LLMs benchmarked; the paired Med-Copilot agent gains +43.02% (offline RL) and +45.28% (online RL).

## Typical Duration

Multi-turn coding episodes in sandboxes; budgets are TODO(reference).

## Main Contribution

Brings verifiable, sandbox-executed evaluation to biomedical data-science coding at five-digit scale, in an environment equally usable for benchmarking and for trajectory-based agent training.

## Key Design Ideas

- Every task is executable with verifiable ground truth, so scale does not dilute grading rigor.
- Interactive feedback makes the sandbox a genuine environment rather than a static test set.
- The same infrastructure serves evaluation and RL training, which the evaluation-focused reader should treat as two distinct uses.

## Strengths

- 72K instances across 129 categories is the largest verifiable biomedical coding suite documented here.
- 29-model benchmarking gives broad frontier coverage.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); details beyond those sources await full-paper validation.
- Repository note: Med-Copilot and the RL training pipeline are agent-training contributions out of this repository's scope; the card documents the benchmark environment.

## Related Works

- [MedAgentBench](./medagentbench.md) — Also an interactive medical-agent environment, over a FHIR virtual EHR rather than coding sandboxes.
- [SciAgentArena](./sciagentarena.md) — Also biomedical research-task evaluation with per-domain stepwise verification.
- [BioXArena](./bioxarena.md) — Also end-to-end biomedical ML tasks under standardized compute with hidden labels.
