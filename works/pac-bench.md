# PAC Bench (2025)

> **English** | [简体中文](../zh/works/pac-bench.md)

## Overview

PAC Bench asks whether foundation models understand the prerequisites for executing manipulation policies — object Properties, Affordances, and Constraints: over 30,000 annotations spanning 673 real-world images (115 object classes), 100 real humanoid-view scenarios, and 120 simulated constraint scenarios across four tasks.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2506.23725>
- **Project:** <https://pacbench.github.io/>
- **Dataset:** <https://huggingface.co/datasets/Pacbench/pacbench>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

Before a robot plans a manipulation, something must know that a glass is fragile, a handle affords pulling, and an overhang blocks a grasp. PAC Bench evaluates exactly this prerequisite layer from a task-executability perspective: VLMs answer property, affordance, and constraint questions over real images (including Unitree G1 humanoid-view captures) and simulated constraint scenarios. The evaluations reveal significant gaps in current VLMs' grasp of fundamental physical concepts — on identifying all correct affordances, performance drops to near zero for most models (project page).

## Tasks

Static multiple-choice/comprehension evaluation over 30,000+ annotations: 673 real images (115 object classes, 15 property types, 1–3 affordances per class), 100 real humanoid-view scenarios, 120 simulated constraint scenarios across four tasks. No robot execution.

## Domains

Robotics — manipulation-prerequisite understanding evaluated on real robot-viewpoint (Unitree G1) and tabletop imagery, framed by executability for manipulation policies.

## Evaluation

- Accuracy per category (Properties / Affordances / Constraints) across roughly 8–10 frontier and open VLMs (project page).
- **Reported.** Significant gaps in fundamental physical concepts; all-correct-affordance identification near zero across models (exceptions 11–20%, project page).

## Typical Duration

Per-question static queries; no episodic interaction.

## Main Contribution

Benchmarking the prerequisite layer beneath manipulation policies — showing that models proposed as robot brains cannot yet reliably enumerate what objects are, allow, and forbid.

## Key Design Ideas

- The P/A/C decomposition mirrors the checklist a planner implicitly runs before acting.
- Humanoid-view captures test perception from the deployment viewpoint, not curated web angles.
- The all-affordances criterion punishes partial knowledge that single-answer accuracy hides.

## Strengths

- Cleanly isolates a failure layer that end-to-end manipulation scores can't attribute.
- Mixed real/simulated construction with the real side dominant.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project page (August 2026); no venue is verifiable from those sources (the project page states the work is under review).

## Related Works

- [RoboSpatial](./robospatial.md) — Also robot-oriented VLM evaluation, on spatial understanding with real-robot validation.
- [ManipBench](./manipbench.md) — Also probes VLM manipulation reasoning, at the movement-decision level.
- [PhysBench](./physbench.md) — Also physical-understanding evaluation for VLMs, at broader world scope.
