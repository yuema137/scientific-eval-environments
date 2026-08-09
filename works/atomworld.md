# AtomWorld (2025)

> **English** | [简体中文](../zh/works/atomworld.md)

## Overview

AtomWorld is a benchmark for evaluating the spatial reasoning of large language models on crystalline materials: models perform ten fundamental atomic-structure actions across four widely used modelling categories, with verifiable checks — and struggle badly on operations involving complex spatial relations (below 12% success for rotations).

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.04704>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2025

## Summary

Crystalline materials are defined by the geometry of their atomic structure, so an LLM that reasons about them must manipulate that structure, not just recall facts about it. AtomWorld poses ten fundamental actions — constructing and modifying atomic structures — across four common modelling categories, scored by verifiable checks on the resulting structure rather than by a judge. The finding is a sharp spatial-reasoning gap: even the strongest models handle simple edits but fail on operations needing complex spatial relations, with rotation success below 12%.

## Tasks

Ten fundamental atomic-structure construction and modification actions across four modelling categories; text/structure-based (no image inputs), statically verifiable. Per-category question counts are TODO(reference) — not stated in the abstract.

## Domains

Materials science — crystalline-structure spatial reasoning: constructing and modifying atomic structures under standard modelling operations.

## Evaluation

- Verifiable checks on the produced atomic structure per action; no LLM judge.
- **Reported.** Strong models handle simple operations but fail on complex spatial relations; rotation success below 12%. The current abstract names Claude Opus 4.6 as the best performer.

## Typical Duration

Single-action structure edits; not an interactive multi-step loop.

## Main Contribution

Isolating spatial manipulation of crystal structures as a distinct, verifiable LLM capability — and exposing that current models understand materials text far better than materials geometry.

## Key Design Ideas

- Verifiable structure checks make grading objective without a judge.
- The four modelling categories separate representation from operation type.
- Rotation and other spatial-relation actions surface the geometric blind spot.

## Strengths

- Verifiable, judge-free scoring on a genuinely geometric task.
- Positioned as an agent/RL testbed, not only a static leaderboard.

## Limitations

- Repository note: card compiled from the arXiv abstract (August 2026); per-category counts and code availability are not stated there. No venue is present in arXiv metadata.
- Repository note: the abstract's "Claude Opus 4.6" naming is anomalous for the paper's date and should be re-checked against the published version.

## Related Works

- [MatText](./mattext.md) — Also probes LLM crystal-structure understanding, from text representations rather than manipulation actions.
- [OpenXRD](./openxrd.md) — Also crystallography-centered LLM evaluation, on XRD question answering.
- [MatSciBench](./matscibench.md) — Also materials reasoning evaluation, at broader college-level scope.
