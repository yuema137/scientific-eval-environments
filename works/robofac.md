# RoboFAC (2025)

> **English** | [简体中文](../zh/works/robofac.md)

## Overview

RoboFAC is a comprehensive framework for robotic failure analysis and correction: 9,440 erroneous manipulation trajectories and 78,623 QA pairs across 53 scenes in both simulation and real-world environments, with systematically categorized failure types, a benchmark over eight QA dimensions, and a specialized RoboFAC-7B model that beats GPT-4o on failure analysis by 34.1%.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2505.12224>
- **Code:** <https://github.com/MINT-SJTU/RoboFAC>
- **Dataset:** <https://huggingface.co/datasets/MINT-SJTU/RoboFAC-dataset>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

RoboFAC covers the full failure-understanding pipeline — task understanding, failure analysis, failure correction — over erroneous manipulation trajectories collected in ManiSkill, ReplicaCAD, and AI2-THOR simulations plus real-world environments. The benchmark spans eight QA types targeting different aspects of failure understanding and correction. The paired lightweight RoboFAC-7B model achieves 34.1% higher failure-analysis accuracy than GPT-4o, and when integrated as an external supervisor in a real-world VLA control pipeline yields a 29.1% relative improvement across four tasks at much lower latency than GPT-4o.

## Tasks

Failure-analysis and correction QA over 9,440 erroneous trajectories (78,623 QA pairs, 53 scenes, simulation + real); static QA for the benchmark, plus online use as an external supervisor in a real-robot VLA pipeline.

## Domains

Robotics — robot-manipulation failure analysis across simulated and real-world environments, deployed as a real-time supervisor in a physical VLA control pipeline.

## Evaluation

- Per-dimension scoring across eight QA types; failure-analysis accuracy as the headline metric.
- **Reported.** RoboFAC-7B: +34.1% failure-analysis accuracy over GPT-4o; +29.1% relative downstream improvement across four real-pipeline tasks with reduced latency.

## Typical Duration

Per-trajectory QA; supervisor deployments run continuously inside robot control loops.

## Main Contribution

Scaling failure understanding into a supervised discipline — a categorized failure corpus large enough to both benchmark frontier models and train a small specialist that outperforms them.

## Key Design Ideas

- Eight QA dimensions separate knowing something failed from knowing where, why, and how to fix it.
- Mixed sim + real collection keeps the corpus from overfitting simulator artifacts.
- The supervisor deployment tests failure analysis where it matters: live, in the loop, under latency constraints.

## Strengths

- The largest categorized robot-failure QA corpus among the works documented here.
- The small-specialist-beats-GPT-4o result quantifies the value of domain failure data.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repositories (August 2026); no venue is verifiable from those sources. Benchmark, dataset, and model share the RoboFAC name; this card centers the benchmark/dataset.

## Related Works

- [AHA](./aha.md) — Also failure detection and reasoning with a fine-tuned VLM, from procedurally generated failures.
- [REFLECT / RoboFail](./robofail.md) — The founding failure-explanation formulation and dataset.
- [LabRobFail](./labrobfail.md) — Also failure analysis with a domain-specialized VLM, for laboratory robots.
