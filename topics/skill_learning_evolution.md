# Skill Learning & Evolution

> **English** | [简体中文](../zh/topics/skill_learning_evolution.md) · [← All topics](./README.md)

## Start Here

Completing one task after reading its solution does not show that an agent learned a reusable skill. It may simply replay the trajectory. The test is what remains when the original trace is removed and the context, task wording, or required composition changes.

One evaluation loop can let the agent solve examples, write a skill file, freeze that file, and deploy it on held-out tasks. Compare the frozen skill with raw-trajectory reuse and with no memory. If it transfers, the artifact captured something reusable; if it works only on near-duplicates, it compressed experience without learning a general procedure.

## Definition

Skill learning and evolution studies whether agents can turn experience, trajectories, demonstrations, or evaluator feedback into reusable procedural artifacts and whether those artifacts transfer when tasks, contexts, or compositions change.

## Motivation

Task success during acquisition does not show that a reusable skill was learned. Evaluation must separate episodic reuse from abstraction, skill authoring from retrieval, and immediate replay from frozen deployment. This differs from Skill Hierarchy, which decomposes a capability for measurement rather than studying how skills are acquired and revised.

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

- [Beyond 'Aha!'](../works/beyond-aha.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [GATE](../works/gate.md)
