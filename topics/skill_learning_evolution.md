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

## Comparison

| Work | Learned artifact | Feedback | Transfer test | Main separation |
|---|---|---|---|---|
| SkillEvolBench | Written skill library | Verifier feedback | Context shift, adversarial, composition | Skill vs raw trajectory reuse |
| SkillLearnBench | Generated skills | None, self, teacher, creator pipeline | Held-out skill-dependent tasks | Artifact vs trajectory vs outcome |
| SkillCoach | Evolving skill-use rubric | Rollout evidence + validation gate | Held-out task families | Process quality vs outcome |
| SkillMisevo-Bench | Evolved potentially unsafe skills | Online evolution updates | Fresh-session persistence | Authoring vs retrieval vs harm |
| GATE | Hierarchical tool graph | Execution experience | New tasks using evolved graph | Structured capability artifact |

## Open Questions

- What evidence shows abstraction rather than memorized trajectory replay?
- How should skill quality, retrieval quality, and execution quality be scored separately?
- When does evaluator feedback cause recursive drift, overfitting, or unsafe generalization?
- How can frozen deployment measure long-term transfer without blocking legitimate adaptation?
- Which skill representations support composition and inspection across agent harnesses?

## Related Works

- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [GATE](../works/gate.md)
