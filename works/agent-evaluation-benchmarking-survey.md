# Evaluation and Benchmarking of LLM Agents: A Survey (2025)

> **English** | [简体中文](../zh/works/agent-evaluation-benchmarking-survey.md)

> **First appeared:** 2025-07-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2507.21504)

## Overview

*Evaluation and Benchmarking of LLM Agents: A Survey* is a survey of the LLM-agent evaluation field that introduces a two-dimensional taxonomy organizing existing work by evaluation objectives (what to evaluate) and evaluation process (how to evaluate), and highlights enterprise-specific evaluation challenges. It is included here as a reference paper, not a benchmark contribution.

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — survey or position paper; no evaluated task.

## Links

- **Paper:** <https://arxiv.org/abs/2507.21504>

## Summary

The survey provides an in-depth overview of LLM-agent evaluation, which it characterizes as a complex and underdeveloped area. It organizes the field along a two-dimensional taxonomy: (1) evaluation objectives — what to evaluate, such as agent behavior, capabilities, reliability, and safety; and (2) evaluation process — how to evaluate, including interaction modes, datasets and benchmarks, metric computation methods, and tooling. Beyond the taxonomy, it highlights enterprise-specific challenges often overlooked in current research — role-based access to data, reliability guarantees, dynamic and long-horizon interactions, and compliance — and identifies future directions toward holistic, more realistic, and scalable evaluation.

## Tasks

N/A — survey paper.

## Domains

Cross-domain coverage: LLM-agent evaluation and benchmarking, with explicit attention to enterprise deployment settings.

## Evaluation

N/A — survey paper. The survey itself organizes evaluation-process methods (interaction modes, datasets and benchmarks, metric computation methods, tooling) as one axis of its taxonomy.

## Typical Duration

N/A.

## Main Contribution

A two-dimensional taxonomy of LLM-agent evaluation — organizing work by evaluation objectives (what to evaluate) and evaluation process (how to evaluate) — together with an articulation of enterprise-specific evaluation challenges.

## Key Design Ideas

- Two-dimensional taxonomy separating *what* to evaluate (objectives) from *how* to evaluate (process).
- Evaluation objectives: agent behavior, capabilities, reliability, and safety.
- Evaluation process: interaction modes, datasets and benchmarks, metric computation methods, and tooling.
- Explicit treatment of enterprise challenges: role-based data access, reliability guarantees, dynamic and long-horizon interactions, and compliance.

## Strengths

- Separates evaluation objectives from evaluation process, clarifying an otherwise fragmented landscape.
- Surfaces enterprise-deployment concerns (access control, reliability, compliance) that benchmark-centric surveys often omit.
- Frames concrete future directions: holistic, realistic, and scalable evaluation.

## Limitations

- Repository note: Survey papers freeze the state of the field at publication time; as a July 2025 survey, it does not cover later works documented in this repository.

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — Also a survey focused specifically on LLM-agent evaluation; organizes the field along a five-perspective taxonomy rather than a two-dimensional objectives/process split.
- [A Survey on Large Language Model based Autonomous Agents](./llm-autonomous-agents-survey.md) — Broader agent survey covering construction and applications alongside evaluation, rather than evaluation alone.
- [From Chatbot to Digital Colleague](./from-chatbot-to-digital-colleague.md) — Also a meta-level reference paper; a position paper arguing a direction rather than a survey cataloguing the field.
