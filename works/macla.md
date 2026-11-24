# MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement (2025)

> **English** | [简体中文](../zh/works/macla.md)

> **First appeared:** 2025-12-22 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2512.18950)

## Overview

MACLA keeps the LLM frozen and adapts an agent by maintaining an external two-level library of procedures extracted from its trajectories, scoring each procedure by how often it has succeeded. Parameter-training approaches update the model from trajectories; MACLA instead records, for each procedure, a Beta posterior over its success rate, selects procedures by expected utility under that posterior, and asks the LLM to rewrite a procedure by contrasting its successful and failed executions. The paper evaluates this on ALFWorld, WebShop, TravelPlanner, and InterCodeSQL against prompted and fine-tuned baselines, and ablates Bayesian selection, contrastive refinement, and the meta-procedure level.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities


N/A — Agent-memory method evaluated on general household, web-shopping, travel-planning, and SQL benchmarks; no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2512.18950>
- **Code:** <https://github.com/S-Forouzandeh/MACLA-LLM-Agents-AAMAS-Conference>
- **Venue:** AAMAS 2026 (accepted, per the arXiv comments)

## Summary

The frozen LLM segments each trajectory into sub-tasks; each segment becomes a procedure ⟨goal, preconditions, abstracted action sequence, postconditions⟩ and is merged with an existing one when embedding cosine similarity exceeds 0.85. A sequence of at least three procedures that repeatedly succeeds in a stable order becomes a meta-procedure ("playbook") with a control policy choosing continue, skip, repeat, or abort. Each execution outcome updates the procedure's Beta(α, β) posterior, starting from Beta(1, 1); at a decision point the agent picks the candidate with the highest expected utility and falls back to zero-shot reasoning when the best utility is below a confidence threshold. Once a procedure has at least three successes and three failures, the LLM compares the two sets and edits preconditions, actions, and postconditions, possibly splitting the procedure into specialized variants.

## Tasks

N/A — method paper; it introduces no new task suite. Experiments use existing benchmarks: ALFWorld (2,851 train, 274 test), WebShop (1,624 train, 200 test), TravelPlanner (1,000 train, 180 validation, 45 test), and InterCodeSQL (split sizes `TODO(reference)`).

## Domains

General household interaction, web shopping, travel planning, and SQL query generation; no canonical science or engineering domain is evaluated.

## Evaluation

The backbone is Llama-2-7B (4-bit quantized via Ollama, temperature 0.7, frozen). Each benchmark is scored by its task reward or quality score on a 0–100 scale; TravelPlanner uses the Commonsense score. Success and failure feedback for posterior updates comes from the task environment; the paper does not state an explicit success threshold.

The expected utility used for selection is

`EU = Rel · α/(α+β) · R_max − Risk · β/(α+β) · C_fail + λ_info · H[Beta(α, β)]`, with `λ_info = 0.1` and `C_fail = 0.5`.

Reported results (MACLA): WebShop 70.2, InterCodeSQL 59.3, TravelPlanner 83.3, ALFWorld 87.2 seen / 90.3 unseen, average 78.1. The strongest comparison rows include IPR (WebShop 71.3, InterCodeSQL 61.3, ALFWorld unseen 74.7) and Qwen2.5-72B (average 75.6, TravelPlanner 63.8), so MACLA is not highest on WebShop or InterCodeSQL. Memory construction takes 56 seconds on one RTX 3090 (0.016 GPU-hours) against 44.8 GPU-hours for IPR, compressing 2,851 trajectories into 187 procedures.

Ablations on ALFWorld (seen / unseen): full 87.1 / 90.3; without Bayesian selection 79.4 / 81.2; without contrastive refinement 83.6 / 85.7; without meta-procedures 81.2 / 78.4; without ontology 82.8 / 84.1.

## Typical Duration

Multi-step interactive episodes; the paper discusses long episodes of 50+ steps as a cost case. Per-task wall-clock time is `TODO(reference)`.

## Main Contribution

An external hierarchical procedural memory for a frozen LLM agent in which execution outcomes drive both selection (Bayesian reliability and expected utility) and revision (contrastive refinement of procedures from success and failure sets).

## Key Design Ideas

- Two levels: atomic procedures and meta-procedures composed of them with a control policy.
- A Beta posterior per procedure turns execution outcomes into a reliability estimate with uncertainty.
- Expected-utility selection trades estimated success, failure cost, and an information bonus for uncertain procedures.
- Contrastive refinement is triggered only after enough successes and failures accumulate (at least three of each).
- Bounded memory (200 procedures, 50 meta-procedures) with pruning by a utility weighting reliability 0.5, frequency 0.3, and recency 0.2.

## Strengths

- Ablations separate the effect of Bayesian selection, contrastive refinement, and the meta-procedure level (paper).
- Reports memory construction cost against a parameter-training baseline (paper).
- Analyzes its weakest benchmark (InterCodeSQL), attributing it to low procedure reuse (51%), low reliability (0.64), and little meta-procedure use (18%) (paper).

## Limitations

- The authors list ambiguous preconditions (for example, inferring an unneeded cooling step), accumulating scoring cost in long episodes, possible forgetting of rare skills under the 200-procedure cap, and hallucinated dependencies in LLM-based precondition extraction.
- MACLA does not lead on WebShop or InterCodeSQL in the reported table (paper).
- The paper reports slightly different figures for the same quantity in different places (for example, 87.1 versus 87.2 for ALFWorld seen).
- Repository note: the rule mapping an execution to a success or failure for posterior updates is described as environment feedback without an explicit threshold.

## Related Works

- [Trace2Tower](./trace2tower.md) — also uses success and failure evidence to induce multi-level skills from trajectories and ranks skills by smoothed success reliability.
- [Agent Workflow Memory](./agent-workflow-memory.md) — induces reusable sub-routines from trajectories, filtering online experiences with an LM evaluator rather than per-procedure posteriors.
- [SkillEvolBench](./skillevolbench.md) — benchmarks the distillation of episodic trajectories into reusable procedural skills.
