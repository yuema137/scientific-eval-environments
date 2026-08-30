# ManipBench (2025)

> **English** | [简体中文](../zh/works/manipbench.md)

> **First appeared:** 2025-05-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.09698)

## Overview

ManipBench benchmarks vision-language models on low-level robot manipulation reasoning — deciding precise robot movements, including object-object interaction and deformable-object manipulation — across 33 representative VLMs from 10 model families, with performance strongly correlated to real-world manipulation outcomes.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2505.09698>
- **Code:** <https://github.com/slurm-lab-usc/ManipBench-Real-Robot-question>
- **Project:** <https://manipbench.github.io>
- **Venue:** CoRL 2025

## Summary

High-level planning benchmarks ask what to do; ManipBench asks exactly how — which grasp point, which direction, which fabric fold. Its 12,617 multiple-choice questions (project page) draw from real robot trajectories (DROID, Bridge), manually curated fabric-manipulation scenarios, and simulation environments spanning pick-and-place, drawer closing, rope manipulation, sweeping, and ball shooting. Evaluating 33 VLMs across 10 families shows performance varies significantly by task, correlates strongly with real-world manipulation trends, and remains well below human-level understanding.

## Tasks

Static multiple-choice questions (12,617 per the project page) probing low-level movement decisions over real robot data, fabric scenarios, and simulated environments; paired real-world manipulation tasks establish the correlation.

## Domains

Robotics — low-level manipulation reasoning built from real robot trajectories and validated by a strong correlation with physical manipulation performance.

## Evaluation

- Multiple-choice accuracy per task family; correlation analysis against real-world manipulation task performance.
- **Reported.** Performance varies significantly across tasks; strong correlation with real-world manipulation trends; a significant gap to human-level understanding remains.

## Typical Duration

Per-question static queries; the correlated real-robot tasks are physical episodes.

## Main Contribution

Validated proxy measurement: showing an MCQ benchmark can rank VLMs consistently with their physical manipulation utility, making low-level capability measurable without a robot in every lab.

## Key Design Ideas

- Movement-level questions target the layer VLA policies delegate to VLM priors.
- Deformables and object-object interaction cover the contact-rich cases rigid-object suites skip.
- The real-world correlation study is part of the benchmark's claim, not an afterthought.

## Strengths

- Venue-verified with the widest VLM coverage (33 models) among documented robot-reasoning benchmarks.
- The proxy-validity evidence raises the bar for what robot-relevant VQA should demonstrate.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); the question count comes from the project page, not the abstract.

## Related Works

- [PAC Bench](./pac-bench.md) — Also low-level manipulation-relevant VLM evaluation, at the prerequisite layer.
- [Robo2VLM](./robo2vlm.md) — Also manipulation-scene MCQ, generated from real trajectory sensing.
- [RoboSpatial](./robospatial.md) — Also robot-frame VLM evaluation, on spatial understanding.
