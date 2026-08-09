# LiveIdeaBench (2024)

> **English** | [简体中文](../zh/works/liveideabench.md)

## Overview

LiveIdeaBench evaluates LLMs' divergent-thinking capabilities for scientific idea generation with minimal context: over 40 leading models generate ideas from single-keyword prompts across 1,180 keywords spanning 22 scientific domains, scored by an LLM panel on five dimensions — originality, feasibility, fluency, flexibility, and clarity.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Experiment Design & Scientific Discovery](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2412.17596>
- **Code:** <https://github.com/x66ccff/LiveIdeaBench>
- **Dataset:** <https://huggingface.co/datasets/6cf/liveideabench>
- **Venue:** Nature Communications (per the official repository; arXiv metadata carries no venue)

## Summary

Published in its current version as "Evaluating LLMs' Divergent Thinking Capabilities for Scientific Idea Generation with Minimal Context," LiveIdeaBench isolates creativity from context: models generate scientific ideas from single-keyword prompts, testing divergent thinking rather than context-rich elaboration. Over 40 leading models are evaluated across 1,180 keywords spanning 22 scientific domains, scored by a dynamic panel of state-of-the-art LLMs on five dimensions grounded in Guilford's creativity theory — originality, feasibility, fluency, flexibility, and clarity. A key finding: creativity is poorly predicted by general-intelligence metrics — QwQ-32B-preview rivals top models like claude-3.7-sonnet:thinking despite lower general-intelligence scores.

## Tasks

Scientific idea generation from single-keyword prompts across 1,180 keywords and 22 domains, over 40+ models; static generation scored by an LLM panel on five creativity dimensions.

## Domains

AI & Machine Learning Research — scientific research ideation and divergent thinking (spanning many scientific domains via keyword prompts).

## Evaluation

- LLM-panel scoring on five dimensions (originality, feasibility, fluency, flexibility, clarity), grounded in Guilford's creativity theory.
- **Reported.** Creativity is poorly predicted by general-intelligence metrics; QwQ-32B-preview rivals claude-3.7-sonnet:thinking despite lower general-intelligence scores.

## Typical Duration

Single-turn keyword-to-idea generation; no interactive setting.

## Main Contribution

A minimal-context divergent-thinking benchmark that separates scientific creativity from general capability — showing idea-generation quality is not captured by standard intelligence metrics.

## Key Design Ideas

- Single-keyword prompts strip away context, isolating divergent thinking.
- Five Guilford-grounded dimensions give creativity a structured, theory-based rubric.
- A dynamic LLM panel scores at breadth (40+ models, 1,180 keywords, 22 domains).

## Strengths

- Large, cross-domain creativity evaluation with a theory-grounded rubric and public release.
- The creativity-vs-general-intelligence dissociation is a novel, citable finding.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); the paper was retitled, and the Nature Communications venue is a repository claim not in arXiv metadata. The repository lists 41 models versus the abstract's "over 40."

## Related Works

- [IdeaBench](./ideabench.md) — Also research idea generation, grounded in richer paper context rather than single keywords.
- [MLR-Bench](./mlr-bench.md) — Also evaluates idea generation, within a full research pipeline.
- [MLGym](./mlgym.md) — Also involves hypothesis/idea generation, in an AI-research loop.
