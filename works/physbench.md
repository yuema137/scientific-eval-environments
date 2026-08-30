# PhysBench (2025)

> **English** | [简体中文](../zh/works/physbench.md)

> **First appeared:** 2025-01-27 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2501.16411)

## Overview

PhysBench benchmarks vision-language models on physical-world understanding: 10,002 entries of interleaved video-image-text data across four domains — physical object properties, object relationships, scene understanding, and physics-based dynamics — in 19 subclasses and 8 capability dimensions, evaluated on 75 VLMs and paired with the PhysAgent enhancement framework.

## Topics

_No methodology-axis topic — indexed under the [Robotics](../domains/robotics.md) domain (field axis)._

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2501.16411>
- **Code:** <https://github.com/USC-GVL/PhysBench>
- **Project:** <https://physbench.github.io/>
- **Dataset:** <https://huggingface.co/datasets/USC-GVL/PhysBench>
- **Venue:** ICLR 2025

## Summary

Motivated by embodied AI's dependence on physical common sense, PhysBench measures whether VLMs understand the physical world they would act in. Across 75 representative VLMs the finding is consistent: models excel at common-sense reasoning but struggle with physical understanding — likely, the paper argues, from the absence of physical knowledge in training data and missing embedded physical priors. The paired PhysAgent framework combines VLM generality with specialized vision models, improving GPT-4o's physical understanding by 18.4%, and the paper demonstrates that better physical understanding helps embodied agents such as MOKA.

## Tasks

Static multiple-choice QA over 10,002 interleaved video-image-text entries in four physical domains (19 subclasses, 8 capability dimensions); a public leaderboard and EvalAI challenge host submissions.

## Domains

Robotics — physical-world understanding as the perception substrate for embodied and robot agents, with a demonstrated transfer to the MOKA embodied agent; the benchmark itself is static VQA rather than robot control.

## Evaluation

- Multiple-choice accuracy across domains and capability dimensions; leaderboard-based comparison.
- **Reported.** 75 VLMs struggle with physical understanding despite strong common-sense reasoning; PhysAgent improves GPT-4o by 18.4%; enhanced physical understanding aids the MOKA embodied agent.

## Typical Duration

Per-question static queries; no episodic interaction in the benchmark.

## Main Contribution

Separating physical understanding from general common sense at scale — and locating the former, not the latter, as the deficient layer beneath embodied deployment.

## Key Design Ideas

- Four-domain taxonomy spans properties through dynamics, not just static attributes.
- Interleaved video-image-text entries let dynamics questions actually show motion.
- The PhysAgent pairing demonstrates the deficit is addressable with specialized visual expertise.

## Strengths

- Venue-verified with unusually wide model coverage (75 VLMs) and a maintained leaderboard.
- The embodied-transfer demonstration connects the static benchmark to agent outcomes.

## Limitations

- Repository note: card compiled from the arXiv abstract and official project materials (August 2026); an "oral" designation circulates but only "ICLR 2025" is verifiable from arXiv Comments. The real-vs-simulated composition of entries is not stated in verified sources.

## Related Works

- [PAC Bench](./pac-bench.md) — Also physical-concept evaluation for VLMs, specialized to manipulation prerequisites.
- [EmbodiedEval](./embodiedeval.md) — Also MLLM embodied competence, measured interactively rather than as understanding.
- [RoboSpatial](./robospatial.md) — Also a perception-layer benchmark with a demonstrated downstream robot effect.
