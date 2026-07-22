# T-Eval (2023)

## Overview

T-Eval is a fine-grained tool-use benchmark that decomposes evaluation into six capability subprocesses and scores each independently, rather than reducing tool-use to an end-task success rate.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- Skill Hierarchy *(topic page pending)*

## Links

- **Paper:** <https://arxiv.org/abs/2312.14033>
- **Code:** <https://github.com/open-compass/T-Eval>

## Summary

T-Eval argues that holistic tool-use scoring conflates several distinct competencies — an agent can appear "good at tool use" while being weak on planning, or vice versa. The benchmark decomposes tool-use into six subprocesses and evaluates each one on isolated tasks, producing a per-capability profile alongside conventional outcome accuracy.

## Tasks

23,305 test cases derived from 553 query–solution annotation pairs (averaging 5.8 tool-calling steps per query), spanning 15 tools across 6 domains (Research, Travel, Entertainment, Web, Life, Financials). Per-dimension test cases: Instruct 2,660, Plan 553, Reason 6,426, Retrieve 6,426, Understand 6,753, Review 487.

## Domains

Tool-use tasks.

## Evaluation

Each of the six subprocesses is scored on isolated tasks under two parallel protocols — a loose "string" format and a strict "JSON" format — and the final T-Eval score is the unweighted arithmetic mean across the six dimensions:

- **Instruct** (format following) — 0.5 for emitting a validly formatted tool call, plus 0.5 × the fraction of correctly matched parameters (max 1.0).
- **Plan** (action-sequence generation) — predicted vs. golden sequence compared via Sentence-BERT cosine similarity, matched with Hopcroft–Karp bipartite maximum matching (similarity threshold ≈ 0.7) and a Longest Increasing Subsequence to enforce order; scored as F1 = 2pr/(p+r).
- **Reason** (next-thought generation) — Sentence-BERT cosine similarity between the predicted and golden thought.
- **Retrieve** (tool selection) — exact match on the chosen tool name (1/0).
- **Understand** (argument generation) — Sentence-BERT similarity between predicted and golden API parameters.
- **Review** (response judgement) — classify the tool response into one of five categories (Success, Internal Error, Input Error, Irrelevant Response, Unable to Accomplish), scored by exact match.

Reported overall: GPT-4 ≈ 86.4, GPT-3.5 ≈ 84.0, and the best open-source model Qwen-72B ≈ 71.4, with the largest open-source-vs-GPT-4 gaps on Retrieve and Review.

## Typical Duration

Short, per-instance interactions targeting one capability axis at a time.

## Main Contribution

Reframes tool-use evaluation from a single end-task metric into a decomposed, subprocess-level assessment that supports interpretable diagnosis of where an agent fails.

## Key Design Ideas

- Capability decomposition of tool-use into six subprocesses.
- Isolated evaluation of each subprocess on targeted tasks.
- Comparability with holistic outcome metrics preserved.

## Strengths

- Diagnostic granularity: identifies which subprocess drives a tool-use failure.
- Complements rather than replaces end-task evaluation.
- Publicly available codebase.

## Limitations

- Scope confined to tool-use; does not evaluate multi-turn state maintenance, long-horizon planning, or embodied interaction.

## Related Works

- [AgentBoard](./agentboard.md) — Also decomposes evaluation below end-task success, but along task subgoals rather than tool-use subprocesses.
