# SkillSV (2026)

> **English** | [简体中文](../zh/works/skillsv.md)

## Overview

SkillSV (structure-aware Shapley valuation of agent skills) is an attribution framework that assigns credit to the internal units of an agent skill — compiling a skill into units, dependencies, and hierarchy so that only valid counterfactual skills are evaluated.

## Topics

- [Credit Assignment](../topics/credit_assignment.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.04562>
- **Venue:** arXiv preprint, 2026

## Summary

SkillSV answers 'what is a skill worth, and which parts of it carry the value?' by Shapley valuation over a skill's compiled structure. Paired deletion and length-neutral padding separate content value from context cost. Evaluated on four agentic benchmarks for faithfulness, actionability, and explanation quality, the framework recovers unit interactions, preserves aggregate skill lift, and guides safe pruning and compression.

## Tasks

N/A — attribution method, not a task suite. Evaluated on four agentic benchmarks; their identities are TODO(reference).

## Domains

Agent skills as structured artifacts; no single science domain.

## Evaluation

- Faithfulness, actionability, and explanation quality of the valuations across four agentic benchmarks.
- **Reported.** SkillSV recovers unit interactions, preserves aggregate skill lift, and guides safe pruning and compression; further numbers are TODO(reference).

## Typical Duration

N/A — post-hoc valuation over completed evaluations.

## Main Contribution

Brings structure-aware Shapley credit to the internals of agent skills, so a skill's value can be located in specific units rather than asserted for the whole.

## Key Design Ideas

- Compiling skills into units/dependencies/hierarchy restricts counterfactuals to valid skills, unlike naive ablation.
- Paired deletion with length-neutral padding controls for context-length confounds.
- Valuation is validated by whether it guides pruning without losing skill lift.

## Strengths

- Makes skill libraries auditable: which units earn their context cost.
- Explicitly separates content value from context cost.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.
- The abstract reports no numerical results; benchmark identities and magnitudes are TODO(reference).

## Related Works

- [Skill-Use](./skill-use.md) — Also treats skills as first-class evaluation objects, scoring agents' use of them rather than valuing their internals.
- [GATE](./gate.md) — Also analyzes structured skill/tool artifacts, via graph-based tool evolution rather than credit valuation.
- [QVal](./qval.md) — Also meta-evaluates a credit signal itself, for step-level supervision rather than skill units.
