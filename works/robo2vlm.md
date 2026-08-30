# Robo2VLM (2025)

> **English** | [简体中文](../zh/works/robo2vlm.md)

> **First appeared:** 2025-05-21 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2505.15517)

## Overview

Robo2VLM generates visual question answering from large-scale in-the-wild robot manipulation data: Robo2VLM-1 holds 684,710 multiple-choice questions covering 463 distinct scenes and 3,396 manipulation tasks, derived from 176K real tele-operated robot trajectories whose sensor streams — end-effector pose, gripper aperture, force sensing — supply the ground truth.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2505.15517>
- **Dataset:** <https://huggingface.co/datasets/keplerccc/Robo2VLM-1>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

Most VQA ground truth comes from human annotators looking at pictures; Robo2VLM's comes from physics. The framework segments real tele-operation trajectories into manipulation phases, extracts 3D properties of the robot, task goal, and target object from proprioceptive and force sensing, and instantiates spatial, goal-conditioned, and interaction-reasoning question templates whose answers are certified by the sensor record rather than opinion. The result probes whether VLMs can read contact, intent, and geometry from robot imagery — and can serve both to benchmark and to fine-tune.

## Tasks

Static multiple-choice VQA: 684,710 questions over 463 scenes and 3,396 manipulation tasks from 176K real robot trajectories; spatial, goal-conditioned, and interaction-reasoning templates. No robot execution in the evaluation.

## Domains

Robotics — manipulation-scene reasoning grounded in real tele-operated robot trajectories, with sensor-derived (pose, gripper, force) ground truth.

## Evaluation

- Multiple-choice accuracy over template families; trajectory-sensor-derived answers require no human labeling or LLM judge.
- **Reported.** Robo2VLM-1 can benchmark and improve VLM capabilities in spatial and interaction reasoning; per-model figures are TODO(reference) — not stated in the abstract.

## Typical Duration

Per-question static queries; no episodic interaction.

## Main Contribution

Sensor-certified VQA generation: turning the robot's own proprioception and force record into scalable, objective ground truth for manipulation-scene understanding.

## Key Design Ideas

- Ground truth from sensing eliminates annotator disagreement at the source.
- Phase segmentation situates questions at semantically meaningful trajectory moments.
- The generation framework scales with fleet data — more tele-operation, more benchmark.

## Strengths

- Among the largest robot-grounded VQA resources, from genuinely in-the-wild data.
- Dual benchmark/fine-tuning use, with the dataset (107 GB) publicly released.

## Limitations

- Repository note: card compiled from the arXiv abstract and official dataset page (August 2026); no venue and no code repository are verifiable from those sources, and per-model results await full-paper validation.

## Related Works

- [RoboSpatial](./robospatial.md) — Also real-data robot spatial understanding, with 3D-scan grounding.
- [ManipBench](./manipbench.md) — Also manipulation-reasoning MCQ for VLMs, curated rather than sensor-generated.
- [PhysBench](./physbench.md) — Also physical-understanding VQA, at world scope beyond manipulation.
