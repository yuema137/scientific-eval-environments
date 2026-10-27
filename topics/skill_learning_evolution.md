# Skill Learning & Evolution

> **English** | [简体中文](../zh/topics/skill_learning_evolution.md) · [← All topics](./README.md)

## Start Here

Completing one task after reading its solution does not show that an agent learned a reusable skill. It may simply replay the trajectory. The test is what remains when the original trace is removed and the context, task wording, or required composition changes.

One evaluation loop can let the agent solve examples, write a skill file, freeze that file, and deploy it on held-out tasks. Compare the frozen skill with raw-trajectory reuse and with no memory. If it transfers, the artifact captured something reusable; if it works only on near-duplicates, it compressed experience without learning a general procedure.

## Definition

Skill learning asks whether an agent can turn experience into a reusable procedure. The source may be a trajectory, demonstration, or evaluator feedback; the result may be a skill file, policy, memory item, or other artifact. Evolution asks whether the agent can revise that artifact after failure. Evaluation then tests whether it still works when the task, context, or skill combination changes.

## Motivation

Solving the acquisition example proves only that the agent solved that example. It may have copied the original trace instead of learning a method. A useful evaluation freezes the skill, removes the source trajectory, and tests transfer on held-out conditions. This differs from Skill Hierarchy, which decomposes an existing capability rather than studying how a skill is acquired, revised, and reused.

## Existing Approaches

- **Frozen deployment controls.** [SkillEvolBench](../works/skillevolbench.md) compares learned skills with raw trajectories and curated seeds under context shift, adversarial shortcuts, and composition.
- **Artifact, trajectory, and outcome scoring.** [SkillLearnBench](../works/skilllearnbench.md) evaluates generated skill quality alongside execution and task success.
- **Evaluation-derived process supervision.** [SkillCoach](../works/skillcoach.md) evolves skill-use rubrics from rollouts and uses them to filter training trajectories.
- **Lifecycle safety.** [SkillMisevo-Bench](../works/skillmisevo-bench.md) separates unsafe authoring, retrieval, execution, and persistence across skill-evolution methods.
- **Reusable capability structures.** [GATE](../works/gate.md) evolves hierarchical tool graphs rather than written skill files.

[EvoHarnessBench](../works/evoharnessbench.md) tests learned artifacts after the surrounding capability set changes. Its separate retention and adaptation measures prevent improvements on new tasks from hiding losses on earlier ones.

Three embodied works test learning from earlier attempts in simulated household and robot-manipulation tasks. [EmbodiedCLBench](../works/embodiedclbench.md) compares no experience, full trajectories from two basic tasks, and a written skill summary of them on an unseen advanced task; either form of experience lifts success from 3–12% to 16–52%, but more than one learning sample brings no consistent further gain. [PhysRSI-eval](../works/physrsi-eval.md) gives an agent a persistent workspace of code, tools, skills, and notes over up to 17 graded robot attempts per task. In an ablation with GPT-6 Astra on six tasks, removing the history drops late-round success from 15/36 to 3/36, and frozen workspaces still solve 25/60 attempts on unseen layouts. [RobotAgentBench](../works/robotagentbench.md) runs a coding agent that keeps and refines its own control tools over ten iterations; its household-task average rises from 31.0 to 42.3.

## Comparison

| Work | Learned artifact | Feedback | Transfer test | Main separation |
|---|---|---|---|---|
| SkillEvolBench | Written skill library | Verifier feedback | Context shift, adversarial, composition | Skill vs raw trajectory reuse |
| SkillLearnBench | Generated skills | None, self, teacher, creator pipeline | Held-out skill-dependent tasks | Artifact vs trajectory vs outcome |
| SkillCoach | Evolving skill-use rubric | Rollout evidence + validation gate | Held-out task families | Process quality vs outcome |
| SkillMisevo-Bench | Evolved potentially unsafe skills | Online evolution updates | Fresh-session persistence | Authoring vs retrieval vs harm |
| GATE | Hierarchical tool graph | Execution experience | New tasks using evolved graph | Structured capability artifact |
| [EvoHarnessBench](../works/evoharnessbench.md) | Persistent skills, prompts, or code | Experience from adaptation tasks | New and earlier cohorts under expanding harnesses | Adaptation gains versus retained competence |
| [EmbodiedCLBench](../works/embodiedclbench.md) | Full trajectories in context, or a written Markdown skill summary | Interaction on two related basic tasks | Unseen advanced tasks composing 2–4 basic-task categories | Trajectory vs skill summary vs no experience |
| [PhysRSI-eval](../works/physrsi-eval.md) | Persistent workspace of policy code, tools, skills, and notes | Native grader score, success flag, and failure reason after each physical attempt | Frozen workspaces on unseen layouts; three cross-task cases | First attempt vs improvement after failure |
| [RobotAgentBench](../works/robotagentbench.md) | Reusable robot-control tools created and refined by a coding agent | Execution feedback across ten iterations | None reported beyond the same tasks and scenarios | Code-only agent with vs without self-improvement |

## Open Questions

- What evidence shows abstraction rather than memorized trajectory replay?
- How should skill quality, retrieval quality, and execution quality be scored separately?
- When does evaluator feedback cause recursive drift, overfitting, or unsafe generalization?
- How can frozen deployment measure long-term transfer without blocking legitimate adaptation?
- Which skill representations support composition and inspection across agent harnesses?

## Related Works

- [RobotAgentBench](../works/robotagentbench.md)
- [PhysRSI-eval](../works/physrsi-eval.md)
- [EmbodiedCLBench](../works/embodiedclbench.md)
- [EvoHarnessBench](../works/evoharnessbench.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [GATE](../works/gate.md)
