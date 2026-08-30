# Skill-Use (2026)

> **English** | [简体中文](../zh/works/skill-use.md)

> **First appeared:** 2026-08-05 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.04828)

## Overview

Skill-Use is a benchmark asking whether LLM agents can actually use skills in agentic harnesses: 79 real skills with 177 executable tasks across nine domains, each grounded in real files and run in an isolated Docker sandbox.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent benchmark; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.04828>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

Skill-Use measures three separable facets of skill use — triggering (does the agent invoke the relevant skill), procedural compliance (does it faithfully follow the prescribed procedure), and boundary adherence (does it avoid forbidden operations) — combined into an SU score in which execution earns credit only after the skill is triggered. The strongest configuration reaches an SU of only 0.613, and triggering and compliance emerge as independent bottlenecks that vary across harnesses.

## Tasks

79 real skills paired with 177 executable tasks across nine domains, each grounded in real files and executed in an isolated Docker sandbox.

## Domains

Nine domains; the abstract does not enumerate them.

## Evaluation

- **SU score** over three facets: Trigger (invoking the relevant skill), Compliance (faithful adherence to the prescribed procedure), Boundary (avoiding forbidden operations); execution receives credit only after triggering.
- **Reported.** The strongest configuration reaches an SU of only 0.613; triggering and procedural compliance behave as independent bottlenecks, with performance varying across agent harnesses.

## Typical Duration

Sandboxed executable episodes per skill-task pair.

## Main Contribution

Decomposes skill use into trigger / compliance / boundary and shows each fails independently — a capability profile no aggregate task-success number reveals.

## Key Design Ideas

- Real skills and real files rather than synthetic skill descriptions.
- Credit gating on triggering prevents scoring execution that ignored the skill.
- Cross-harness comparison shows skill use is a property of the model-harness pair.

## Strengths

- Cleanly separates knowing a skill exists, following it, and respecting its limits.
- Executable, sandboxed verification rather than judged compliance.

## Limitations

- Repository note: card compiled from the arXiv abstract and metadata (August 2026); details beyond those stated in the abstract await full-paper validation.

## Related Works

- [SkillTV-Bench](./skilltv-bench.md) — Also targets the skill-augmented setting, benchmarking judges of skill-using executions rather than the executing agent.
- [UniClawBench](./uniclawbench.md) — Also organizes evaluation around capability axes, at benchmark level rather than per-skill.
- [Harness-Bench](./harness-bench.md) — Also finds the harness materially changes measured capability, for general workflows rather than skill use.
