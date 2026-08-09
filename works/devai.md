# DevAI / Agent-as-a-Judge (2024)

> **English** | [简体中文](../zh/works/devai.md)

## Overview

DevAI is a benchmark of 55 realistic automated-AI-development tasks with 365 hierarchical user requirements, released with Agent-as-a-Judge — an evaluation method in which agentic systems evaluate agentic systems, providing step-by-step feedback and matching human-evaluation reliability while far outperforming LLM-as-a-Judge.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.10934>
- **Code:** <https://github.com/metauto-ai/agent-as-a-judge>
- **Dataset:** <https://huggingface.co/DEVAI-benchmark>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

The paper "Agent-as-a-Judge: Evaluate Agents with Agents" contributes an evaluation method — agentic systems judging agentic systems, an organic extension of LLM-as-a-Judge that inspects the entire task-solving process and gives intermediate feedback — and, as its proof-of-concept testbed, DevAI: a reusable benchmark of 55 realistic automated-AI-development tasks with 365 hierarchical user requirements and rich manual annotations. On DevAI, Agent-as-a-Judge dramatically outperforms LLM-as-a-Judge and is as reliable as a human-evaluation baseline, positioning agentic evaluation as a scalable substitute for expert review of AI-development agents.

## Tasks

55 automated-AI-development tasks (building AI/ML projects) with 365 hierarchical requirements; agentic systems solve them and are evaluated step-by-step. Interactive-agentic and long-horizon.

## Domains

AI & Machine Learning Research — automated AI development: agents building AI/ML projects against hierarchical requirements.

## Evaluation

- Requirement-level assessment with the Agent-as-a-Judge method providing intermediate, process-level feedback; compared against LLM-as-a-Judge and a human-evaluation baseline.
- **Reported.** Agent-as-a-Judge dramatically outperforms LLM-as-a-Judge and matches the human-evaluation baseline's reliability.

## Typical Duration

Long-horizon AI-development episodes per task, evaluated step by step.

## Main Contribution

DevAI provides a requirements-structured benchmark for AI-development agents, and Agent-as-a-Judge shows that agentic, process-level evaluation can match human reliability far more cheaply than LLM-as-a-Judge.

## Key Design Ideas

- 365 hierarchical requirements make grading fine-grained rather than pass/fail per task.
- Process-level (not just outcome) evaluation credits intermediate progress.
- Releasing DevAI standalone lets the benchmark be reused independently of the judging method.

## Strengths

- A reusable, richly annotated AI-development benchmark plus a validated agentic evaluator.
- Public code and HuggingFace dataset; the judge is shown as reliable as human evaluation.

## Limitations

- Repository note: the paper's headline contribution is the Agent-as-a-Judge method; DevAI is its paired, independently released benchmark, and this card centers the benchmark. No venue is stated in arXiv metadata; efficiency figures (time/cost savings) are repository claims.

## Related Works

- [MLE-bench](./mle-bench.md) — Also agent evaluation on building ML systems, on Kaggle competitions.
- [MLR-Bench](./mlr-bench.md) — Also uses an automated (LLM-reviewer) evaluation framework for research agents.
- [AstaBench](./astabench.md) — Also holistic agent evaluation with rubric- and judge-based scoring.
