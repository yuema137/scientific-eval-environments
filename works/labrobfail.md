# LabRobFail (2026)

> **English** | [简体中文](../zh/works/labrobfail.md)

> **First appeared:** 2026-07-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.23704)

## Overview

LabRobFail benchmarks robotic failure analysis in chemical self-driving laboratories: over 20,000 trajectories across 70+ task scenarios with failures injected at the control, physics, and semantic levels (five categories, 11 fine-grained types), evaluating six capabilities from failure detection to actionable correction — the paired domain-specialized VLM reaches 90.83% detection accuracy and lifts downstream task success by 4–16 percentage points as a real-time supervisor.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — capability probe; the agent does not itself perform a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2607.23704>
- **Code:** <https://github.com/Su-ISE-2001/SciRobo>
- **Venue:** arXiv preprint (cs.RO), 2026 (Comments state under review)

## Summary

Self-driving labs fail in ways household robots don't — a mis-gripped vial or mis-timed transfer silently corrupts an experiment. LabRobFail builds the failure-centric evaluation stack for this setting: LabRobFail-Sim injects anomalies into Isaac Sim lab-robot executions at three levels, LabRobFail-Data accumulates 20,000+ trajectories over 70+ scenarios, and LabRobFail-Bench scores six capabilities — task understanding, failure detection, temporal localization, severity assessment, failure classification, and actionable correction. LabRobFail-VLM, the domain-specialized model, achieves 90.83% failure-detection and 77.21% temporal-localization accuracy, substantially outperforming general-purpose VLMs, and improves downstream task success by 4–16 points when integrated as a real-time supervisor.

## Tasks

Failure analysis over 20,000+ simulated lab-robot trajectories (70+ scenarios; 5 failure categories, 11 types injected at control/physics/semantic levels); static diagnosis for the benchmark plus real-time supervision downstream. Simulation only (Isaac Sim).

## Domains

Robotics — laboratory-robot manipulation failure analysis: control-, physics-, and semantic-level anomalies in simulated chemical self-driving-lab executions, with the VLM deployed as a closed-loop supervisor.

## Evaluation

- Six capability scores: task understanding, failure detection, temporal localization, severity assessment, failure classification, actionable correction.
- **Reported.** LabRobFail-VLM: 90.83% failure-detection accuracy, 77.21% temporal-localization accuracy; +4–16 percentage points downstream task success as a supervisor.

## Typical Duration

Per-trajectory diagnosis; supervisor mode runs continuously during lab-task execution.

## Main Contribution

Bringing failure-centric evaluation to laboratory robotics, where undetected failures corrupt science rather than just tasks — with a three-level injection taxonomy that separates control faults from physics accidents from semantic mistakes.

## Key Design Ideas

- Injection at control, physics, and semantic levels makes failure provenance part of the ground truth.
- Temporal localization and severity assessment go beyond detection toward triage.
- The supervisor integration converts benchmark scores into recovered experiments.

## Strengths

- The first failure-analysis benchmark specialized to self-driving laboratories among documented works.
- Capability decomposition gives six separately actionable scores rather than one detection rate.

## Limitations

- Repository note: card compiled from the arXiv abstract and official repository (August 2026); the paper is under review per arXiv Comments, and the benchmark is simulation-only — no physical lab deployment is verifiable from those sources.

## Related Works

- [RoboFAC](./robofac.md) — Also failure analysis and correction with a specialized model, for general manipulation.
- [AHA](./aha.md) — Also procedural failure injection to manufacture training and evaluation data.
- [EnvTrace](./envtrace.md) — Also evaluates lab-instrument control by execution behavior, via trace alignment on a digital twin.
