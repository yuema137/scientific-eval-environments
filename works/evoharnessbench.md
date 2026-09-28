# EvoHarnessBench (2026)

> **English** | [简体中文](../zh/works/evoharnessbench.md)

> **First appeared:** 2026-09-03 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.04280)

## Overview

EvoHarnessBench asks whether an agent still solves earlier tasks when its available harness grows. It changes the tools, skills, or specialist-agent pool while keeping previously introduced task instances fixed, separating retention from adaptation to newly available capabilities.

## Topics

- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — general harness evaluation over enterprise and software-tool tasks, rather than a dedicated scientific research workflow.

## Links

- **Paper:** [EvoHarnessBench: Can Your Agents Keep Pace with an Evolving Harness?](https://arxiv.org/abs/2609.04280), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.04280v1>
- **Official project and evaluation documentation:** <https://mas-orchestra.salesforceresearch.ai/evoharness/>

## Summary

The benchmark constructs 17 streams with three to six stages from EnterpriseOps-Gym and Agents' Last Exam. Its 802 unique tasks produce 1,510 axis-specific examples, not 1,510 distinct tasks. Deployment evaluation carries no experience between stages; adaptation evaluation allows persistent artifacts learned from a separate adaptation split.

## Tasks

Each task is introduced only once all required capabilities are available and at least one is new. Later stages expose the entire cumulative harness, including irrelevant capabilities. The evaluator reruns earlier tasks under that larger harness and also tests newly introduced tasks. The streams span 520 tools, 42 latent reference skills, and 62 specialist agents.

## Domains

General enterprise workflows and heterogeneous software-tool environments. Repository note: no field-specific scientific slice is established here, so the card is organized through evaluation topics rather than a catch-all domain.

## Evaluation

Verifiers check task outcomes such as database state and file content. A stage-by-cohort performance matrix records new-task accuracy and retention of earlier cohorts. Backward transfer compares earlier cohorts at introduction versus the final stage; forward transfer compares new-cohort performance before versus after that stage's adaptation. Tokens, tool calls, and latency track operating cost. Reported analyses distinguish capability selection from successful use.

## Typical Duration

Three to six harness stages per stream. The study reports operating-cost measures rather than a universal task duration.

## Main Contribution

An evaluation protocol for harness-induced loss of competence even when model weights do not change.

## Key Design Ideas

- Grow the available capability set monotonically while preserving earlier tasks.
- Keep adaptation and held-out evaluation splits separate.
- Report retention and adaptation independently instead of relying on one aggregate accuracy.

## Strengths

- Controlled deployment runs isolate harness expansion from accumulated experience.
- Verifier-based outcomes and cost reporting expose both success and operating overhead.

## Limitations

- Capabilities only accumulate; removal and modification are not tested.
- The benchmark inherits tasks and verifiers from two source environments.
- Repository note: the inclusion basis is harness and skill evaluation; the specialist-agent axis does not broaden this repository into general multi-agent-system coverage.

## Related Works

- [HarnessOpt-Bench](./harnessopt-bench.md)
- [Skill-Use](./skill-use.md)
