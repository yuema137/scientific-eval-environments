# RoboSpatial (2024)

> **English** | [简体中文](../zh/works/robospatial.md)

> **First appeared:** 2024-11-25 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2411.16537)

## Overview

RoboSpatial teaches and tests spatial understanding for robotics-oriented vision-language models: 1M images, 5K 3D scans, and 3M annotated spatial relationships over real indoor and tabletop scenes, in both 2D- and 3D-ready form — models trained on it outperform baselines on spatial affordance prediction, spatial relationship prediction, and robot manipulation.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2411.16537>
- **Code:** <https://github.com/NVlabs/RoboSpatial>
- **Project:** <https://chanh.ee/RoboSpatial>
- **Dataset:** <https://huggingface.co/datasets/chanhee-luke/RoboSpatial-Home>
- **Venue:** CVPR 2025 (Oral)

## Summary

Generic VQA data teaches models to describe scenes; robots need to answer where things can go and what fits where, from the robot's frame. RoboSpatial builds that training and evaluation substrate from real 3D-scanned indoor and tabletop scenes — 3M spatial relationships over 1M images and 5K scans — covering spatial configuration, context, and compatibility from multiple reference frames. Fine-tuned models beat baselines on downstream spatial tasks, and per the official project page a real-robot experiment shows RoboSpatial-trained pointing directing a manipulator to a 52.6% grasp success rate versus 23.7% for the baseline.

## Tasks

Spatial QA over real scenes (configuration, context, compatibility; 2D and 3D), used both as fine-tuning data and as evaluation sets (RoboSpatial-Val, RoboSpatial-Home); static VQA with a real-robot manipulation evaluation component (project page).

## Domains

Robotics — robot-centric spatial understanding on real scanned scenes, validated through a physical-manipulator grasping evaluation.

## Evaluation

- Downstream-task performance on spatial affordance prediction, spatial relationship prediction, and robot manipulation, against baseline VLMs.
- **Reported.** Trained models outperform baselines across the downstream tasks; project page: 52.6% vs. 23.7% real-robot grasp success (LLaVA-NeXT + RoboSpatial vs. baseline).

## Typical Duration

Per-query spatial questions; the robot evaluation runs pointing-conditioned grasp episodes.

## Main Contribution

Making robot-frame spatial understanding a trainable, measurable capability — with real-scan grounding and a physical grasping validation connecting VQA scores to actuation.

## Key Design Ideas

- Real 3D scans give geometric ground truth that rendered scenes and web images lack.
- Configuration/context/compatibility typing spans the spatial questions manipulation actually poses.
- 2D- and 3D-ready formats serve both VLM families without re-annotation.

## Strengths

- Venue-verified (CVPR 2025 oral) at a scale — 3M relationships — that supports training, not just testing.
- The grasp-success transfer result links benchmark performance to physical outcomes.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); the robot-experiment figures come from the project page, not the abstract. Primarily a training-plus-evaluation dataset rather than a pure benchmark.

## Related Works

- [PAC Bench](./pac-bench.md) — Also robot-prerequisite VLM evaluation, on properties, affordances, and constraints.
- [ManipBench](./manipbench.md) — Also VLM evaluation correlated with real-robot manipulation outcomes.
- [Robo2VLM](./robo2vlm.md) — Also real-robot-grounded VQA, generated from tele-operation trajectories.
