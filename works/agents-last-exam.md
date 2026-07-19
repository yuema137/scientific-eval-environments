# Agents' Last Exam (2026)

## Overview

Agents' Last Exam (ALE) is a frontier long-horizon benchmark co-designed with over 250 industry experts, targeting economically meaningful professional workflows organized around the U.S. occupational taxonomy. Its stated goal is to bridge the gap between benchmark performance and real-world professional deployment.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.05405>

## Summary

ALE is presented as a "living" benchmark that continuously incorporates new workflows. It covers non-physical industries mapped onto the U.S. occupational taxonomy, with tasks constructed and validated by domain experts. The paper reports that the hardest difficulty tier is deliberately unsaturated at release.

## Tasks

Approximately 1,000+ tasks organized across 13 industry clusters and 55 sub-fields.

## Domains

Non-physical industries, structured against the U.S. occupational taxonomy.

## Evaluation

Measurable outcomes on long-horizon real-world tasks. Reported: the hardest difficulty tier remains unsaturated at release, with average full pass rates below 1%.

## Typical Duration

Long-horizon multi-step tasks. Per-task duration not specified in the abstract.

## Main Contribution

A frontier benchmark grounded in economically meaningful professional workflows, co-designed with industry experts, aimed at exposing the gap between benchmark scores and real-world deployment readiness.

## Key Design Ideas

- Task design driven by 250+ industry experts.
- Grounded in the U.S. occupational taxonomy.
- "Living" benchmark model — continuous incorporation of new workflows.
- Difficulty tiers, with the hardest tier deliberately unsaturated at release.

## Strengths

- Direct industry-expert grounding gives strong ecological validity.
- Difficulty headroom — the hardest tier remains open for frontier models.
- Breadth across 13 industry clusters and 55 sub-fields.

## Limitations

- Repository note: Non-physical industries only — results do not extend to embodied or hardware-dependent workflows.

## Related Works

- [Long-Horizon-Terminal-Bench](./long-horizon-terminal-bench.md) — Also long-horizon, but scoped to terminal environments rather than the occupational taxonomy.
