# SkillSec-Eval (2026)

> **English** | [简体中文](../zh/works/skillsec-eval.md)

> **First appeared:** 2026-07-15 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.13987)

## Overview

SkillSec-Eval is a lifecycle-aware evaluation framework for reusable agent skills: it decomposes the skill lifecycle into five stages with distinct trust boundaries — repository admission, semantic retrieval, planner selection, runtime execution, and skill evolution — and evaluates attacks and defenses separately at each stage over a repository of 327 real-world skills.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent security evaluation framework; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.13987>
- **Venue:** arXiv preprint (cs.CR), 2026

## Summary

Reusable skills package agent capabilities for sharing and reuse, but security research has concentrated on prompt injection and runtime execution, leaving the rest of the lifecycle unexamined. The paper builds a threat taxonomy organized by the trust boundary each attack violates, instantiates it as SkillSec-Eval, and runs a stage-by-stage empirical study with attack and defense conditions at every stage. The result is a per-stage vulnerability profile rather than a single aggregate safety score, showing that failures arise well before execution — at admission, retrieval and planner selection.

## Tasks

A benchmark built from an enterprise-scale skill repository of 327 benign skills spanning 15 skill clusters, drawn from the SkillMCP repository after filtering duplicates and incomplete entries; the clusters cover infrastructure management, DevOps automation, software engineering, cloud operations, data engineering, database optimization, security and compliance, productivity automation, and project management. Capability-clustered workloads comprise 440 benchmark queries across the 15 capability domains, with the 327 real skills supplying realistic retrieval neighborhoods. Lifecycle-specific attack classes are instantiated at each of the five stages, each paired with a defense condition.

## Domains

Reusable skills for general-purpose LLM agents, sourced from an enterprise skill repository whose clusters are infrastructure, DevOps, software and data engineering, and business automation. The evaluated object is the security of the skill lifecycle rather than a domain task, so no canonical science or engineering domain is assigned.

## Evaluation

- **Per-stage attack/defense contrast.** Each lifecycle stage is measured with a baseline (undefended) condition and a defended condition, so mitigation effect is reported per stage rather than pooled.
- **Repository admission.** Malicious admission rate and false-positive rate — a hybrid defense admits 7.9% of malicious skills at a 20.0% false-positive rate, against 52.9% malicious admission for a rules-only filter.
- **Semantic retrieval.** Attack success rate on retrieval poisoning — keyword stuffing 46.59% baseline versus 7.83% defended; Sybil attack 93.20% baseline versus 26.59% defended.
- **Planner selection.** Fake recommendation 45.64% baseline versus 8.72% defended; misleading description 27.27% baseline versus 0.00% defended.
- **Runtime execution.** 100% attack success rate at baseline, reduced to 23% by the proposed defense, which blocks 87% of policy violations.
- **Skill evolution.** Malicious-update detection rate 92.5%, false-positive rate 37.0%, update acceptance rate 63.0%.
- **Setup.** Gemini 1.5 Flash as the planner LLM; semantic retrieval uses all-MiniLM-L6-v2 embeddings with FAISS indexing.

## Typical Duration

N/A — a stage-wise security evaluation harness rather than a long-horizon task suite; no per-query wall-clock or token budgets are reported.

## Main Contribution

A lifecycle-oriented threat taxonomy for reusable agent skills, organized by violated trust boundary, together with a modular evaluation framework and benchmark that make security measurable and reproducible at each lifecycle stage — establishing empirically that vulnerabilities are not confined to runtime execution.

## Key Design Ideas

- The lifecycle is decomposed into stages with independent trust boundaries, so vulnerabilities and defenses can be analyzed in isolation instead of confounded end to end.
- Skill *evolution* — updates to an already-admitted skill — is treated as its own attack surface, which one-shot vetting does not cover.
- Workloads are capability-clustered so that retrieval neighborhoods resemble a real repository, which is what makes retrieval-poisoning attacks meaningful.
- Every defense is reported with its false-positive cost alongside its detection rate, rather than detection rate alone.

## Strengths

- Per-stage reporting yields an interpretable profile of where the skill layer actually fails, not a single number.
- The 327-skill repository and 440-query workload come from a real skill registry rather than synthetic stubs.
- Defenses are evaluated in the same harness as the attacks, so mitigation is measured rather than proposed.

## Limitations

- A single planner LLM (Gemini 1.5 Flash) is used, so results conflate framework findings with one backbone's behavior.
- Defense false-positive rates are high in places — 20.0% at admission and 37.0% at skill evolution — which limits practical deployment.
- No code or data release URL is stated in the paper — TODO(reference).
- Repository note: the candidate metadata for this work described it as a survey; it is not — the paper's substantive contribution is the SkillSec-Eval framework, its benchmark, and an empirical attack/defense study.

## Related Works

- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](./agent-skill-evaluation-survey.md) — Surveys the same skill-evaluation layer, where this work contributes a lifecycle-specific framework.
- [SCR-Bench](./scr-bench.md) — Also argues that isolated per-skill vetting is insufficient, from composition within one execution context rather than across lifecycle stages.
- [HarmfulSkillBench](./harmfulskillbench.md) — Also measures the security of public skill registries, focusing on harmful intent rather than lifecycle trust boundaries.
- [SkillAudit](./skillaudit.md) — Also produces a multi-dimensional per-skill report, combining utility and cost with safety.
