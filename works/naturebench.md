# NatureBench (2026)

## Overview

NatureBench evaluates whether AI coding agents can match the published state-of-the-art of Nature-family scientific publications — framed as a move beyond reproduction toward the claim of methodological discovery.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.24530>

## Summary

NatureBench distills tasks from peer-reviewed Nature-family publications and asks whether coding agents can reach or exceed the published SOTA. The benchmark tests both cross-discipline scientific coverage and the depth needed to match a real publication's results.

## Tasks

90 tasks distilled from peer-reviewed Nature-family publications.

## Domains

Cross-discipline scientific problems drawn from Nature-family publications.

## Evaluation

- Comparison against the published SOTA on each distilled task.
- Reported: the strongest models exceed published performance on only 17.8% of tasks.
- Author observation: agent successes are frequently driven by reformulating scientific problems into conventional prediction tasks, rather than genuine methodological innovation.

## Typical Duration

TODO(reference): abstract does not state per-task duration.

## Main Contribution

Anchors benchmark difficulty to the published SOTA of top-venue scientific publications, providing a bar aligned with real research output rather than curated toy tasks.

## Key Design Ideas

- Task grounding in Nature-family publications provides a real-world SOTA reference point.
- Cross-discipline scope within a single benchmark.
- Explicit distinction between "matching SOTA" and "discovery."

## Strengths

- SOTA-grounded difficulty is tied directly to published scientific outcomes.
- Reveals a substantial gap (17.8% success on strongest models) against a hard reference.
- Author observation surfaces a distinct evaluation concern (problem reformulation).

## Limitations

- Repository note: Distilled from Nature-family publications only — coverage is shaped by those venues' editorial focus.

## Related Works

- [AIRS-Bench](./airs-bench.md) — Also research-lifecycle science, but organized around a curated task suite rather than published SOTA reference.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also science-focused, but centered on containerized executable verification.
