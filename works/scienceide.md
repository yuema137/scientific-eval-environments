# ScienceIDE (2026)

> **English** | [简体中文](../zh/works/scienceide.md)

> **First appeared:** 2026-09-16 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2609.19134)

## Overview

Scientific simulation codes are public, but a public repository is not a task an agent can be trained or scored on: it has no task statement, no isolated starting state, and no check that says whether a change is scientifically correct. ScienceIDE turns repositories into executable environments. An agent and a domain expert split each code into modules with one scientific responsibility, the module's official tests are kept as checks, and task factories inject defects or remove implementations. A private verifier then compares the agent's numerical outputs with scientific references. The same verifier scores frontier agents on a hard subset, filters supervised fine-tuning demonstrations, and supplies the reward for reinforcement learning.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

- [Scientific Software & Workflow Engineering](../activities/scientific_software_workflow_engineering.md)
- [Simulation & Scientific Computing](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [ScienceIDE: Turning World's Scientific Codebase into Agent Learnable Environments](https://arxiv.org/abs/2609.19134), 2026 preprint.
- **Full text:** <https://arxiv.org/html/2609.19134v1>
- **Code:** <https://github.com/aitofound/ScienceIDE>
- **Venue:** arXiv preprint (cs.CL, cs.CY), 2026

## Summary

An agent first builds a pinned revision of a scientific code and runs its official tests and examples. It then proposes a module decomposition, which a domain expert reviews; a curator owns module boundaries and the equivalence contract. Each approved module is packaged with an editable workspace, checks, and a private verifier. Factories in seven categories (Acceleration, Repair, Discovery, Reproduction, Integration, Calibration, Implementation) generate candidate tasks, and a task is admitted only if a known-valid witness passes and the unfixed baseline leaves headroom. A repair task, for example, starts from injected defects; the agent edits the module, the verifier reruns it, and the score is the share of the gap between the defective start and a full pass that the edit closes. The authors state that the released tasks are mostly repair and implementation in computational physics and geoscience, not open-ended discovery.

## Tasks

27 scientific codebases, 64 environments, and 2,812 manufactured tasks: 2,515 repair, 295 implementation, and 2 acceleration. The environments carry 1,076 executable checks of numerical outputs and physical invariants. ScienceIDE-Hard is an evaluation subset of 85 tasks (52 repair, 33 implementation) from 18 environments; codebases named for it include PLUTO, Athena++, MITgcm, LAPS, and PHANTOM. Per-domain task counts are given only in a figure. TODO(reference): per-domain counts.

## Domains

Computational physics and geoscience codes: astrophysical flows, plasma physics, ocean and atmospheric modeling, and particle simulations.

## Evaluation

- **Verifier:** deterministic. Outputs are compared with private scientific references under pointwise tolerances (|c − r| ≤ a + ρ|r|) or with invariant checks. The paper states that trace audits can diagnose failures but that no judge can override the deterministic checks.
- **Repair score:** r_repair = max(0, (r − f)/(1 − f)), where f is the defective starting point's raw score; strict success requires r_repair = 1.
- **Agent results on ScienceIDE-Hard (strict success, one-hour budget, 15 models from 8 providers):** Fable 5.1 67.1%, Opus 5 64.6%, Astra 63.1%, Sol 55.0%, all others below 40% (DeepSeek V4.1 Flash 36.0%). Cost per task is $7.90 for Fable and $3.56 for Astra. At a 10-minute budget Astra reaches 49.6% and Fable 25.9%. Spearman correlation of success with runtime is −0.22 and with output volume 0.01.
- **Failure analysis:** budget exhaustion accounts for 37.3% of task-balanced failures on the hard subset; in a trace review of Fable and Astra, mismatches with the reference's conventions account for most task-balanced failures.
- **SFT (LoRA, three epochs, demonstrations from GPT-5.6-sol filtered by the verifier; 4,567 training segments from 564 tasks):** mean repair reward on held-out tasks rises, for example from 0.0000 to 0.3333 (4B, PLUTO-Particles-Dust) and from 0.3125 to 0.5000 (9B, LAPS). On public benchmarks, the 4B model gains 10.98 points on HumanEvalFix JavaScript and the 9B model rises from 0.240 to 0.576 on BBH Word Sorting.
- **RL (Qwen3.5-4B, 30 steps, group size 8, 99 LAPS and 87 MITgcm-biogeo repair tasks):** held-out reward rises from 0.357 to 0.857 on LAPS and from 0.286 to 0.571 on MITgcm-biogeo; the held-out tasks come from the same environments as training.

## Typical Duration

One-hour episode budget per task on ScienceIDE-Hard. SFT evaluation uses an 8,192-token context and a 2,048-token response limit; RL uses a turn cap and response budget whose values are not given.

## Main Contribution

Infrastructure that converts scientific repositories into environments whose tasks are admitted and scored by expert-reviewed numerical verifiers, with the same verifier used for agent evaluation, demonstration filtering, and RL reward. The authors release PhAI-IDE-72B, -9B, and -4B, trained on verified trajectories.

## Key Design Ideas

- Modules are cut along scientific responsibilities, and each official test is kept as a check, excluded with a reason, or flagged as a coverage gap.
- Task admission needs both a passing known-valid witness and headroom over the unfixed baseline, so tasks that are already solved or unsolvable are dropped.
- Repair credit is normalized against the defective start rather than counted from zero.
- In RL, budget-truncated trajectories are masked from the loss but kept in the group baseline.

## Strengths

- Scoring is fully deterministic against private scientific references, with partial credit defined by a closed-form formula.
- The hard-subset results report cost and time budget alongside success, showing that ranking changes between a 10-minute and a one-hour budget.
- The failure analysis attributes a measured share of failures to budget exhaustion.

## Limitations

- The authors state that coverage is mostly repair and implementation in computational physics and geoscience; only 2 acceleration tasks exist and the other factory categories are not represented in the task counts.
- The authors note that factory variants may share code paths, so the task count overstates independent coverage.
- The hard set tests only up to a one-hour budget and two coupled edit sites.
- Verification covers chosen observables only; the authors list external audits and adversarial reward-hacking tests as outstanding.
- The authors state that SFT gains are on selected public benchmarks and RL gains on hinted tasks within training environments; neither shows transfer to unseen codebases.
- The authors state that retrieval controls cannot rule out pretraining exposure to the public code, and that selection is not shown to be contamination-free.
- Repository note: the number of domain experts involved is not stated.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also scores agents on containerized scientific computing tasks with deterministic checks.
- [MooseBench](./moosebench.md) — Also evaluates agents working inside a large simulation framework's codebase.
- [PostTrainBench](./posttrainbench.md) — Also uses evaluation results inside a post-training loop.
