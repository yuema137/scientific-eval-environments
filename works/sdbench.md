# SDBench (2025)

> **English** | [简体中文](../zh/works/sdbench.md)

> **First appeared:** 2025-06-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2506.22405)

## Overview

SDBench (the Sequential Diagnosis Benchmark) recasts 304 diagnostically challenging NEJM clinicopathological conference cases as interactive encounters: the agent starts from a short case abstract and must iteratively request findings from a gatekeeper model that reveals information only when explicitly queried, scored on diagnostic accuracy and the cost of visits and tests ordered. The accompanying MAI-DxO orchestrator is agent-construction work (see the repository note under Limitations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.22405>
- **Project:** <https://microsoft.ai/new/the-path-to-medical-superintelligence/>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

SDBench makes diagnosis a budgeted information-acquisition problem: every test ordered has a cost, and the gatekeeper reveals findings only on explicit request, so the evaluated quantity is the accuracy-cost frontier rather than accuracy alone. Models from the OpenAI, Gemini, Claude, Grok, DeepSeek, and Llama families are evaluated alongside 21 practicing US/UK physicians (mean 20% accuracy on completed cases, per the official page). The paper's paired MAI-DxO orchestrator with o3 reaches 80% accuracy — four times the physician average — while cutting diagnostic costs 20% versus physicians and 70% versus off-the-shelf o3; its maximum-accuracy configuration reaches 85.5%.

## Tasks

304 NEJM-CPC cases run as sequential diagnostic encounters: query the gatekeeper for findings, order costed tests, and commit to a diagnosis.

## Domains

Clinical diagnosis (general and internal medicine via NEJM-CPC cases), diagnostic testing, and cost of care.

## Evaluation

- Diagnostic accuracy paired with the cost of physician visits and tests performed — an explicit accuracy-versus-cost frontier; final-diagnosis grading details are TODO(reference).
- **Reported.** MAI-DxO with o3: 80% accuracy (vs. 20% physician mean) at 20% lower cost than physicians and 70% lower than plain o3; 85.5% in maximum-accuracy configuration.

## Typical Duration

Iterative gatekeeper-query episodes per case, with per-action costs accumulating.

## Main Contribution

Puts a price on every diagnostic question: by scoring cost jointly with accuracy, the benchmark distinguishes clinicians (and agents) who diagnose well from those who diagnose affordably.

## Key Design Ideas

- The gatekeeper turns information acquisition into explicit, auditable actions.
- Cost accounting makes over-testing a measured failure mode rather than a free strategy.
- A physician cohort on identical cases anchors both axes of the frontier.

## Strengths

- The cleanest cost-aware clinical evaluation documented here.
- Frontier results demonstrate orchestration (not just model choice) shifts the accuracy-cost frontier.

## Limitations

- Repository note: card compiled from the arXiv abstract and the official Microsoft page (August 2026); details beyond those sources await full-paper validation. The official page states SDBench and MAI-DxO are research demonstrations and not publicly released; absolute dollar figures are TODO(reference).
- Repository note: MAI-DxO, the paper's second contribution, is agent implementation and out of this repository's scope; the card documents the benchmark.

## Related Works

- [AgentClinic](./agentclinic.md) — Also sequential clinical evaluation, emphasizing dialogue, bias, and multimodality over cost.
- [CostBench](./costbench.md) — Also makes cost-optimal decision-making the evaluated object, in tool-use planning.
- [MedHELM](./medhelm.md) — The static clinician-validated suite this sequential design complements.
