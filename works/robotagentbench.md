# RobotAgentBench (2026)

> **English** | [简体中文](../zh/works/robotagentbench.md)

> **First appeared:** 2026-10-26 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2610.34649)

## Overview

RobotAgentBench (RAB) asks whether a household robot can act on its own, not only whether it can manipulate objects. It rebuilds one real home in Isaac Sim as 50 household layouts and tests standalone VLA and world-action-model (WAM) policies alongside coding agents that plan, execute, and verify through a shared framework. Tasks are scored on five abilities (manipulation, task discovery, context reasoning, failure recovery, robustness) and on four open-ended scenarios that combine them. The best configuration averages 48.5 on the task level and 15.4 on the open-ended scenarios; the best standalone policy averages 18.0.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Agent Harnesses & Scaffolding](../topics/agent_harnesses_scaffolding.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — general-purpose household robot benchmark; the evaluated policies and agents perform household manipulation and navigation, not a scientific or research activity.

## Links

- **Paper:** [RobotAgentBench: Towards Open-world Robot Autonomy](https://arxiv.org/abs/2610.34649), 2026 preprint (Aether AI, UC San Diego, UC Davis).
- **Full text:** <https://arxiv.org/html/2610.34649v1>
- **Code:** <https://github.com/AetherLabsAI/RobotAgentBench> (Apache-2.0 evaluation code; team-authored assets and task data under CC BY 4.0)
- **Assets:** <https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-assets>
- **Training data:** <https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-TrainingData>
- **Model:** <https://huggingface.co/AetherLabs-AI/InternVLA-A1.5-RAB>
- **Project:** <https://aetherlabsai.github.io/RobotAgentBench/>
- **Venue:** arXiv preprint (cs.RO), 2026

## Summary

A semi-automated real-to-sim pipeline builds the environments. A coding agent retrieves or reconstructs 3D assets to match measurements and photos of a real home, human reviewers check visual and physical fidelity, and teleoperated real demonstrations are replayed in simulation to tune geometry and physics. The robot is an AgiBot G1 with a mobile base; no planned routes or automatic navigation actions are provided. Every system is described as a planner, an executor, and a verifier, each of which is code-based (C), a learned VLA/WAM policy (L), hybrid (H), or absent (–). Standalone policies, fully code-based coding agents (C/C/C), mixed configurations, and a C/C/C configuration with recursive self-improvement (RSI) are evaluated on the same tasks. In the RSI setting, the coding agent creates, refines, and reuses control tools from execution feedback over ten iterations, and successful improvements are kept.

## Tasks

A foundation of 90 atomic household tasks, such as pushing, pulling, bimanual coordination, and mobile manipulation, is composed into 18 short-horizon tasks (for example "Prepare coffee", "Wipe the table") and 8 long-horizon tasks (for example "Prepare a meal", "Find and pack an item"). The task level adds four discovery scenarios, four context-reasoning settings (drink, snack, waste, and sofa object selection), five failure-recovery variants (four missed grasps and one tipped cup), and six robustness variants with human interventions and lighting changes. The scenario level has four open-ended families: preparing dinner, hosting guests, preparing to leave, and tidying the room. Each task or scenario is evaluated on 30 distinct instances. A 101.8-hour simulation dataset (50 demonstrations per atomic and short-horizon task, 10 per long-horizon task and open-ended scenario) is provided for training policies.

## Domains

Robotics: household mobile manipulation on a simulated AgiBot G1, task planning for long-horizon and open-ended household goals, self-directed navigation, failure recovery, and VLA/WAM policy evaluation. A sim-to-real comparison runs a subset on the physical robot.

## Evaluation

- **Task level:** Discovery is the fraction of target objects touched within a contact budget (N+2 touches for N targets). Reasoning credits contact with the correct target; no grasp is required. Manipulation, Recovery, and Robustness use task progress scores from task-specific scoring rules over the current physical state. Average is the mean of the five ability scores.
- **Scenario level:** Open-Ended is the final progress score over all task checkpoints in a scenario. Task Coverage, Task Progress, Recovery Rate, and Stagnation describe behavior. An episode ends after 120 s of simulated time without a progress increase, with caps of 200 model responses per episode and 600 control steps per tool call. The paper describes no LLM or VLM judge in scoring.
- **Systems:** 8 VLAs (π0.5, Xiaomi Robotics-1, InternVLA-A1.5, MolmoAct2, LingBot-VLA2, HY-VLA, Galaxea G0.5, X-VLA), 3 WAMs (τ0, OpenWAM-Alpha, LingBot-VA), and coding agents Codex (GPT-6 Astra, the default), Claude Code (Opus 5.5), and Antigravity CLI (Gemini 4 Argon).
- **Results (Table 1, Average / Open-Ended):** standalone policies range from 3.2 / 1.9 (MolmoAct2) to 18.0 / 1.0 (InternVLA-A1.5). Fully code-based agents: Codex 31.0 / 8.4, Claude Code 33.3 / 9.2, Antigravity CLI 39.7 / 9.8. Codex with InternVLA-A1.5: –/L/C 23.3 / 3.7, C/L/– 26.4 / 9.1, C/H/C 48.5 / 15.4. Codex C/C/C + RSI at the tenth iteration: 42.3 / 10.8.
- **Behavior (Table 2):** Stagnation is 88.3 for InternVLA-A1.5 and 84.6 for OpenWAM-Alpha, against 18.4–33.7 for the three coding agents. With RSI, Codex's Recovery Rate rises from 15.4 to 38.9 and its Stagnation falls from 33.7 to 12.3.
- **Issue composition (Appendix D.2):** across the coding agents' open-ended traces, motion-feasibility issues and execution shortfalls make up 82.1% of identified issues and code or interface errors 15.3%. The paper notes that these shares describe issue composition, not the overall error rate.
- **Sim-to-real (Table 3):** on a matched subset of tasks and four scenario contexts, Average falls from 17.8 to 13.5 (InternVLA-A1.5), 8.5 to 8.2 (OpenWAM-Alpha), and 34.2 to 31.9 (Codex). The project page states that rankings hold.

## Typical Duration

An episode ends after 120 s of simulated time without progress, after 200 model responses, or when the task is finalized; a tool call executes up to 600 control steps (about 30 s simulated). Token counts, dollar costs, and wall-clock time are not reported.

## Main Contribution

Puts standalone robot policies and coding-agent architectures on the same household tasks and scores task discovery, context reasoning, recovery, and robustness separately from manipulation. The planner–executor–verifier notation then shows which component a gain comes from.

## Key Design Ideas

- Score abilities that a manipulation success rate hides: finding the targets, choosing the right object from context, and recovering from an induced failure.
- Describe every system by the type of its planner, executor, and verifier, so that standalone policies, coding agents, and hybrids are compared on one axis.
- Test harness-level recursive self-improvement by letting a coding agent keep and refine its own control tools across ten iterations.

## Strengths

- One table reports all 18 configurations on the same five abilities and on the open-ended scenarios.
- Planner × executor combinations, the three coding agents, and the RSI iterations are compared directly (Figures 4–6).
- The evaluation code, assets, 1,470 saved initial configurations, training data, and a fine-tuned policy are released.

## Limitations

- The authors state that reliable autonomy in open-ended scenarios remains far from solved; the best Open-Ended score is 15.4.
- All 50 layouts derive from one real home.
- Real-world scores are lower than simulated ones in the sim-to-real comparison, which covers only a subset of tasks and three systems.
- Repository note: the paper reports no repeated runs, variance, or confidence intervals.
- Repository note: each coding agent is tied to one backbone model, so harness and model effects are not separated among the three C/C/C rows.
- Repository note: the paper does not state whether the coding agents have network access during evaluation.

## Related Works

- [CaP-X](./cap-x.md) — Also has coding agents write robot-control programs and transfers to an AgiBot G1, but on tabletop tasks across abstraction tiers.
- [RoboGraphBench](./compiling-and-benchmarking-task-state-horizons-for.md) — Long-horizon household planning, scored at the planning level rather than with physical execution by the evaluated system.
- [PhysRSI-eval](./physrsi-eval.md) — Also measures physical self-improvement of coding agents, over up to 17 rounds on RoboDojo manipulation tasks.
