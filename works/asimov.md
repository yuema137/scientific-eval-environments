# ASIMOV (2025)

> **English** | [简体中文](../zh/works/asimov.md)

## Overview

The ASIMOV Benchmark evaluates the semantic safety of VLMs serving as robot brains — judging the desirability and safety of situations and rejecting unconstitutional actions — using large-scale datasets generated from real-world visual scenes and hospital injury reports, paired with a method that auto-generates and amends robot constitutions to a top alignment rate of 84.3%.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Links

- **Paper:** <https://arxiv.org/abs/2503.08663>
- **Code:** <https://github.com/asimov-benchmark/code/>
- **Project:** <https://asimov-benchmark.github.io>
- **Venue:** CoRL 2025 (per the official project page; arXiv metadata carries no venue)

## Summary

Published by Google DeepMind as "Generating Robot Constitutions & Benchmarks for Semantic Safety", this work attacks the semantic layer of robot safety: not collision avoidance but whether the robot's brain recognizes that an action is undesirable. The ASIMOV datasets ground undesirability in reality — real visual scenes and human injury reports from hospitals — and the evaluation measures alignment between model judgments and human preferences. The paired method generates robot constitutions automatically and amends them (Constitutional AI mechanisms), reaching a top alignment rate of 84.3%, beating both no-constitution and human-written-constitution baselines; a robot is demonstrated rejecting unconstitutional actions.

## Tasks

Static safety-judgment evaluation: VLMs assess situation desirability and action permissibility over injury-report- and visual-scene-grounded data. Dataset scale figures are TODO(reference) — not stated in the abstract.

## Domains

Robotics — semantic-safety evaluation of VLMs acting as robot brains, grounded in real injury reports and visual scenes; the benchmark is static safety judgment rather than robot control.

## Evaluation

- Alignment rate with human preferences on behavior desirability and safety, under different constitution conditions.
- **Reported.** Top alignment rate 84.3% with generated constitutions, outperforming no-constitution and human-written-constitution baselines.

## Typical Duration

Per-item judgment queries; no episodic interaction in the benchmark itself.

## Main Contribution

Grounding robot safety evaluation in documented human harm — injury reports — and showing machine-generated, self-amending constitutions align robot judgment better than human-written rules.

## Key Design Ideas

- Injury reports import the actual distribution of physical harm into safety evaluation.
- Constitutions make the safety criterion explicit, auditable, and improvable.
- Auto-amendment closes the loop: misalignments feed back into constitution revisions.

## Strengths

- Rare real-harm grounding in a field of hypothetical hazards.
- The generated-beats-human-written result is directly actionable for deployed robot policies.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); the paper's title is "Generating Robot Constitutions & Benchmarks for Semantic Safety" — ASIMOV names the benchmark artifact. The CoRL 2025 venue is stated by the project page, not arXiv metadata; dataset scale figures are not in the abstract.
- Benchmark and constitution-generation method are co-contributions; scores under generated constitutions reflect both.

## Related Works

- [SafeAgentBench](./safeagentbench.md) — Also embodied-agent safety, evaluated by executed hazardous plans rather than judgment alignment.
- [BadRobot](./badrobot.md) — Also robot-safety evaluation, adversarially eliciting the harms ASIMOV asks models to recognize.
- [PhysBench](./physbench.md) — Also evaluates the world-understanding layer beneath embodied deployment.
