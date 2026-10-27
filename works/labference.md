# Labference (2026)

> **English** | [简体中文](../zh/works/labference.md)

> **First appeared:** 2026-10-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.35252)

## Overview

Labference tests whether a laboratory robot uses what it has just observed to choose its next operation, and whether it can then carry that operation out. A finished workflow alone cannot show this: a correct choice can be lost to a dropped object, and a successful transfer can carry the wrong object. Labference therefore scores operation selection, physical execution, and task completion separately.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)

## Activities

- [Laboratory & Instrument Control](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** [Labference: Benchmarking the Reasoning-Action Connection in Robotic Laboratories](https://arxiv.org/abs/2610.35252)
- **Full text:** <https://arxiv.org/html/2610.35252v1>
- **Project:** <https://zhaochunhai.github.io/Labference/>
- **Venue:** arXiv preprint (2026)

## Summary

Each task has a contract that fixes the decision-relevant state, the evidence the robot may use, the legal next operations, the physical predicates that confirm an outcome, waiting and terminal conditions, and supported diagnostic interfaces. Choice is scored at the first identifiable operation; execution is scored on fixed subgoals from shared verified starts; completion requires a confirmed terminal predicate. The design also defines answer-changing evidence pairs and Oracle-assisted continuations for locating bottlenecks, but the reported experiments cover only randomized easy feedback-weighing episodes.

## Tasks

Three core families, each with a basic and an extended condition:

- **Centrifuge loading:** place an equal-mass tube pair in opposite slots of a twelve-slot rotor (Pick, Insert, Wait, Stop). The basic condition starts with one tube seated; the extended one starts with both outside.
- **Feedback weighing:** reach a target mass with 10, 20, 50, and 100 g standards by adding or removing a standard, waiting for a valid reading, or finishing.
- **Placement recall:** place a tube in a 3×4 rack and retrieve it after occlusion; the extended condition adds three distractor tubes and moves the rack.

Appendix A also catalogs 24 tasks: twelve laboratory workflows (L01–L12) and twelve readout and relational tasks (R01–R12). In the reported weighing runs, the target is 160, 180, or 200 g and one standard closes the gap; for example, at 170 g toward 180 g, the robot must add the 10 g standard.

## Domains

Robotics: laboratory manipulation by a simulated Franka Panda in Isaac Sim 5.1 (PhysX), with front and wrist cameras and an eight-dimensional joint interface (seven arm targets plus a gripper command). The tasks reproduce routine bench operations (centrifuge loading, balance weighing, rack handling) rather than a specific chemistry or biology experiment.

## Evaluation

- **Choice:** `B_next` is the fraction of checkpoints whose first identified choice is legal; `C_id` is the fraction with any identifiable choice by the deadline. Reach rate (`N_reach / N_run`) is reported apart from correctness after reaching.
- **Execution:** `E_fixed` is fixed-subgoal success, physically confirmed, over a common population of verified starts with the same correct operations and geometric references.
- **Completion:** clean and recovered completion are reported separately. Weighing needs a final reading within 1 g of target held for 3 s; centrifuge insertion needs at most 10° axial error, at least 60% socket depth, and opposite occupancy held for 3 s.
- **Planned diagnostics:** answer-changing pairs (`P_state` requires both members correct), geometric-equivariance pairs, and Oracle-assisted continuations in assist or replace mode over Semantic, Decision, Geometry, and Skill scopes, scored by paired differences from shared checkpoints.
- **Reported results (Table 3, simulated easy weighing):** fine-tuned π0.5 and GR00T-N1.5 (50 episodes each) select the required standard in 20% and 18% of episodes and complete 16% (8/50) and 8% (4/50). An investigator-reported GPT-driven control selects correctly in 10/10 trials and completes 8/10; the GPT model is not named. Table 3's episode-level selection rate is not the checkpoint metric `B_next`.
- VLA failures include grasping and placing a standard of the wrong mass. GPT-driven failures involve weights slipping or falling, followed by regrasp attempts.

## Typical Duration

VLA weighing episodes are capped at 3,600 evaluation steps; mean runtimes are 135.60 s (π0.5) and 86.81 s (GR00T-N1.5), including failed episodes. The GPT-driven control takes about 30 minutes of model computation per trial, excluding network delay, plus about 50 s of task execution.

## Main Contribution

A laboratory-robot benchmark that ties confirmed physical outcomes to legal next operations and scores selection, execution, and completion separately, with a shared-checkpoint protocol for testing targeted support.

## Key Design Ideas

- Physical-confirmation predicates use explicit tolerances and hold windows and do not depend on policy intent.
- Separate scores can show a correct transfer of the wrong standard, or a correct choice lost to a drop.
- Answer-changing pairs hold the goal fixed while changing the evidence that determines the correct next operation.

## Strengths

- Thresholds, legal operation sets, and metric equations are specified per task.
- The initial results already separate selection failures (VLA policies) from execution failures and computation cost (GPT-driven control).

## Limitations

- Quantitative results cover only easy feedback weighing. Hard weighing, centrifuge loading, placement recall, matched Oracle studies, and the Harness-VLA comparison are stated as future work.
- Samples are small: 50 episodes per VLA policy and 10 GPT-driven trials.
- Table 3 results are simulated; Appendix B shows only keyframes from physical-robot pilot recordings.
- No measured human baseline is reported.
- Repository note: no public code was found. The arXiv record and the paper link none; the project page links <https://github.com/zhaochunhai/Labference>, which returned not found on 2026-10-27, and no Labference repository appears among that account's public repositories. The project page also lists a dataset link (Baidu Netdisk) and reports no eligible model results on its leaderboard.

## Related Works

- [LabRobFail](./labrobfail.md) — Evaluates failure analysis for simulated laboratory robots.
- [EnvTrace](./envtrace.md) — Evaluates laboratory instrument-control code against a digital twin.
- [AFMBench](./afmbench.md) — Evaluates agents operating a physical atomic force microscope.
