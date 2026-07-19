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

TODO(reference): exact task count is not stated in the abstract; verify against the paper before adding a number.

## Domains

Tool-use tasks.

## Evaluation

Step-by-step, per-subprocess scoring across six capability axes:

1. Instruction following
2. Planning
3. Reasoning
4. Retrieval
5. Understanding
6. Review

Subprocess scores are combined into a fine-grained profile. Consistency with outcome-oriented metrics is preserved as a sanity check.

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
