# SLBench (2026)

> **English** | [简体中文](../zh/works/slbench.md)

## Overview

SLBench is an 86-case executable benchmark testing whether LLM agents resolve the logical relations that hold among the instructions inside an agent skill — preconditions, constraints, fallbacks and five further relation types catalogued by its companion framework SkillLogic.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent reliability and safety probe; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.09016>
- **Venue:** arXiv preprint, 2026

## Summary

Agent skills package reusable procedures, tools, and domain workflows, but their safe execution depends on the agent honouring dependencies among interacting instructions. SkillLogic analyses logical relations in skill files under a taxonomy of eight relation types and compiles executable tests from them; a scan of over 5000 public skills finds that 70% contain at least one logical relation. SLBench selects the high-confidence, high-impact, locally testable relations into 86 executable cases, and an inference-time scaffold, SLGuard, is evaluated as a mitigation.

## Tasks

86 executable cases, constructed by SkillLogic from logical relations mined out of a scan of over 5000 public skills and filtered to those that are high-confidence, high-impact, and locally testable. The relation taxonomy has eight types, including preconditions that gate valid actions, constraints that limit how allowed actions may be performed, and fallbacks that specify recovery behavior after failure.

## Domains

Agent skills for general-purpose LLM agents, exercised through coding-agent harnesses; the reported failure consequences are software and system operations (privacy leaks, unsafe configuration changes, incomplete cleanup). No canonical science or engineering domain is assigned.

## Evaluation

- **Executable tests** derived from each logical relation, with violations detected by execution rather than by a judge.
- **Unsafe rate** as the headline metric, reported per harness and backbone.
- **Reported.** Evaluating Codex and Claude Code across six LLM backbones shows unsafe rates up to 70%, with violations leading to privacy leaks, unsafe configuration changes, and incomplete cleanup. A human audit attributes failures both to agent capability gaps and to low-salience skill text. SLGuard, a lightweight inference-time scaffold, reduces violations by 63% on targeted cases.

## Typical Duration

TODO(reference) — the abstract does not report per-case wall-clock or token budgets.

## Main Contribution

Establishes logical-relation following as a distinct reliability challenge for skill-guided agents, separable from general instruction following, and supplies both a taxonomy for mining such relations at scale and an executable benchmark built from them.

## Key Design Ideas

- A relation taxonomy (eight types) turns implicit dependencies inside skill prose into explicit, checkable structure.
- Cases are filtered for local testability, so each violation can be verified by execution in isolation.
- The ecosystem scan quantifies prevalence (70% of over 5000 public skills carry at least one relation) before the benchmark is built, motivating case selection.
- Failures are attributed by human audit to two distinct causes — agent capability and skill-text salience — rather than charged wholly to the model.

## Strengths

- Executable verification rather than judged compliance.
- Benchmark construction is grounded in a measured property of the real public skill ecosystem.
- Pairs the diagnosis with an evaluated mitigation (SLGuard) instead of stopping at failure rates.

## Limitations

- Restricted by construction to *locally testable* relations, so relations whose violation manifests only across long horizons are excluded.
- 86 cases is a small suite relative to the scanned skill population.
- Repository note: card compiled from the arXiv abstract and metadata (August 2026); the six evaluated backbones are not enumerated in the abstract — TODO(reference).

## Related Works

- [Skill-Use](./skill-use.md) — Also measures whether an agent respects a skill's prescribed procedure and boundaries, by task facet rather than by logical relation type.
- [SkillSV](./skillsv.md) — Also compiles skills into units and dependencies, for credit valuation rather than safety testing.
- [SkillJuror](./skilljuror.md) — Also treats a skill's internal structure as the manipulated variable, for organization rather than logical dependency.
- [SafeAgentBench](./safeagentbench.md) — Also scores unsafe agent behavior with executable checks, in embodied tasks rather than skill files.
