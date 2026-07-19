# Traxgen (2025)

## Overview

Traxgen is a deterministic ground-truth trajectory generation toolkit for AI-agent evaluation. It compiles structured workflow specifications and user profiles into fully specified reference trajectories via a directed acyclic graph (DAG), removing the LLM from the ground-truth generation loop. The paper also releases a companion benchmark of 675 task instances used to evaluate LLM planning against Traxgen-generated references.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** *Traxgen: Ground-Truth Trajectory Generation for AI Agent Evaluation* (Mazzolenis & Zhang)
- **Venue:** NeurIPS 2025 Workshop on Scaling Environments for Agents (SEA)
- **License:** MIT
- **Distribution:** PyPI package (`traxgen`)

## Summary

Traxgen argues that trajectory-level agent evaluation depends on high-quality reference trajectories, and that LLM-based generation of those references is slow, noisy, and unsuitable for compliance-critical domains. It offers a fully deterministic alternative: workflows are specified as JSON with steps, soft-ordering blocks, and conditional rules over user data; the toolkit compiles each workflow–user pair into a DAG, prunes it by the conditionals, and enumerates valid trajectories. The paper contributes both the toolkit (MIT-licensed) and a companion benchmark used to compare six LLMs against the deterministic references.

## Tasks

Companion benchmark: 675 task instances across 9 workflows over 3 domains (E-Commerce, HR, Travel), with 71 tools total. 10% of task instances are multi-intent.

Complexity distribution:

- Simple: 3 workflows × 50 instances (E-Commerce)
- Intermediate: 3 workflows × 75 instances (HR)
- Complex: 3 workflows × 100 instances (Travel)

## Domains

Customer-service tool-use workflows (E-Commerce, HR, Travel). Traxgen the toolkit is domain-agnostic; the released benchmark is customer-service.

## Evaluation

- **Trajectory quality metrics** — Exact Match, Count Agreement, Tool-level and Parameter-level Precision / Recall / F1, Contiguous Overlap Length (CMR), Prefix Length. Predictions are aligned to best-matching gold trajectories via the Hungarian algorithm.
- **Ablation dimensions on the LLM baseline** — input format (natural language vs. JSON), prompt style (Vanilla / ReAct / ReAct + few-shot), inference strategy (direct generation vs. DFSDT-guided search).
- **Six LLMs benchmarked**: DeepSeek-Chat-v3-0324, Mistral-7B-Instruct, Llama-4-Maverick, Gemini-2.0-Flash-001, Claude-3.7-Sonnet, GPT-4.1.
- **Reported**: Traxgen achieves 100% alignment with gold trajectories on all metrics; median 30,000× speedup on simple workflows and > 17,000× across all complexity levels versus LLM-based generation. On complex workflows Sonnet and Gemini significantly outperform other tested LLMs; performance degrades as complexity increases; JSON input consistently outperforms natural language on intermediate complexity; ReAct-style prompting gives only marginal, inconsistent gains.

## Typical Duration

Traxgen executes near-instantaneously per trajectory (fractions of a millisecond). LLM baselines take approximately 1.5 s – 29 s per trajectory depending on model and complexity (see paper Table 2).

## Main Contribution

A fully deterministic, DAG-based framework for generating gold-standard agent trajectories from structured workflow specifications and user data — replacing LLM-based ground-truth generation with a reproducible, MIT-licensed, orders-of-magnitude-faster alternative — together with a benchmark that quantifies the gap between LLM-generated and deterministic reference trajectories.

## Key Design Ideas

- Workflows are JSON: Steps + Soft Ordering blocks + Conditional rules over user data.
- Trajectory planning as DAG construction: node insertion, conditional pruning, edge wiring, cycle check, soft-order permutation.
- Multi-agent composition via concatenation of per-agent trajectories.
- Four output formats for interoperability (Tool Only, Google Style, LangChain Tool Style, Traxgen Style).
- Deterministic and reproducible — no inference-time randomness in the reference generator.
- Companion benchmark uses Traxgen-generated drafts plus independent human review (two blinded annotators) to seed gold trajectories.

## Strengths

- Removes LLM noise from ground-truth generation — 100% alignment with human-validated references reported.
- Orders-of-magnitude speedup over LLM-based generation (median > 17,000×).
- MIT license and PyPI availability lower adoption cost.
- Suitability for compliance-critical domains (finance, healthcare) is an explicit design goal.
- Companion LLM benchmark isolates input-format, prompt-style, and inference-strategy effects.

## Limitations

- Authors note: Not yet validated on real-world workflows that involve complex interdependencies, multimodal inputs, or non-idempotent behavior.
- Authors note: Enumerating all permutations of soft-order blocks grows factorially, limiting scalability for large soft-order groups.
- Authors note: The framework does not adapt to novel or ambiguous inputs without pre-specified logic.
- Authors note: LLM benchmarking is constrained by the specific models and prompt designs tested.
- Repository note: Companion benchmark is domain-limited to customer-service workflows (E-Commerce, HR, Travel) despite the toolkit being domain-agnostic.

## Related Works

- [FinTrace](./fintrace.md) — Also multi-dimensional trajectory evaluation with per-dimension metrics, but as a benchmark rather than a ground-truth generation toolkit.
- [AgentBoard](./agentboard.md) — Also uses annotated ground-truth structure per task (subgoals) as the reference against which trajectories are scored.
- [TRACE](./trace.md) — Also targets trajectory-first evaluation, but via a hierarchical utility function on the trajectory rather than deterministic reference generation.
