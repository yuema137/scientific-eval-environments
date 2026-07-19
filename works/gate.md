# GATE (2026)

## Overview

GATE (Graph-based Adaptive Tool Evolution Across Diverse Tasks) is a framework that dynamically constructs and evolves a hierarchical graph of reusable tools for LLMs. It is included in this repository for completeness of coverage of the initial reference list, but note: **its actual subject is tool-making for LLMs, not skill-hierarchy evaluation of agents** — the maintainer input's Skill-Hierarchy classification was based on a superficial name match rather than the paper's content.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://aclanthology.org/2026.acl-long.87/>
- **Venue:** ACL 2026

## Summary

GATE dynamically constructs and evolves a hierarchical graph of reusable tools that LLMs can leverage across scenarios. The hierarchical graph captures tool relationships and reusability patterns across domains, enabling adaptive tool construction for different problem types. Evaluated on Minecraft, TextCraft, DABench, and code generation.

## Tasks

Not a task suite. Evaluated across four downstream benchmarks: Minecraft, TextCraft, DABench, and code generation.

## Domains

Tool-making / tool evolution for LLMs. Downstream evaluation on games (Minecraft, TextCraft), data analysis (DABench), and code generation.

## Evaluation

Performance on the four downstream benchmarks; the paper reports improvements over existing methods (per abstract).

## Typical Duration

Depends on the downstream benchmark.

## Main Contribution

An adaptive framework for constructing and evolving a hierarchical graph of reusable tools that LLMs can leverage across diverse tasks.

## Key Design Ideas

- Hierarchical graph of reusable tools as the primary abstraction.
- Adaptive tool construction across task types.
- Cross-benchmark applicability.

## Strengths

- Adaptive tool structure across heterogeneous downstream benchmarks.
- Improves over existing methods (per abstract) on four distinct downstream benchmarks.

## Limitations

- Repository note: GATE is a tool-making / tool-evolution framework — despite this card being placed under Skill Hierarchy per the maintainer's initial reference list, the paper's actual subject is the *construction of tools for LLMs*, not the *decomposition of agent capability into subskills*. Read the paper for its actual scope before drawing skill-hierarchy conclusions.
- Repository note: Not a task suite; downstream tasks (Minecraft, TextCraft, DABench, code generation) are the substrate.

## Related Works

- None directly comparable in this repository — GATE is a tool-evolution framework rather than a benchmark. See [Skill Hierarchy](../topics/skill_hierarchy.md) for adjacent skill-decomposition benchmarks whose scope actually matches the topic.
