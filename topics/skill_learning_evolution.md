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

A group of method papers changes the step at which a candidate skill or memory item is admitted. Earlier induction pipelines summarized a trajectory and stored the result without testing it. These methods put an evaluation between writing and storing, and they differ in what that evaluation runs.

- **Paired with/without tests.** [SkillGen](../works/skillgen.md) reruns a verification subset with and without the candidate skill, counts repairs and regressions separately, and deploys the skill only if their difference clears a threshold. The selection matters: the latest round-8 candidate averages −3.1 pp on held-out splits, the best verified candidate +8.1 pp. [Trace2Tower](../works/trace2tower.md) applies a similar paired-outcome gate to edits of an existing skill library and rolls back rejected edits.
- **Rerun on the source task.** [SKILL-KD](../works/skill-kd.md) writes a patch from the difference between a weak student's failure and a stronger teacher's run, and commits it only if the student then succeeds on that task. The gate shows the patch fixes one task, not that it generalizes.
- **Reconstruction by a second agent.** [MIND-Skill](../works/mind-skill.md) asks a separate agent, without the source trajectory, to re-solve the task from the skill alone. Environment outcome, an LLM-judged trajectory match, and a documentation rubric then drive edits to the skill-writer's prompt.
- **Outcome statistics per stored item.** [MACLA](../works/macla.md) keeps a Beta posterior over each procedure's success rate, selects by expected utility, and rewrites a procedure only after it has at least three successes and three failures to contrast. [Agent Workflow Memory](../works/agent-workflow-memory.md) admits online workflows only from trajectories an LM evaluator labels successful, so evaluator errors can enter memory. [STAIR](../works/stair.md) does not gate individual nodes by outcome; it stores abstracted repair trajectories and lets an LLM verifier filter retrieved nodes.
- **Evolving the reuse policy rather than the skill.** [SkillLens](../works/skilllens.md) leaves skill content in place and edits the verifier's routing rules from failure reports, keeping an edit when it raises correctness minus normalized cost.

Two studies test assumptions that these gains rely on. [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) shows that induced skills can lower success below a no-memory baseline when written per task, and proposes a utility score computed from embeddings before any task is run. [LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md) empties, shuffles, or replaces inserted experience and finds that perturbing condensed experience often leaves scores unchanged. A rise in success after adding memory therefore does not by itself show that the agent used the stored skill; an intervention on the memory content is needed to establish that.

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
| [Trace2Tower](../works/trace2tower.md) | Three-level skill library (action, procedure, strategy) | Success/failure labels weighting a transition graph; paired-outcome gate on library edits | Held-out ALFWorld and WebShop tasks; cross-model author/user transfer | Outcome-contrastive vs. flat skill induction; component ablations |
| [STAIR](../works/stair.md) | Multi-level plan trees from past repairs | None per node; LLM verifier filters retrieved nodes | Later SWE-bench Verified issues in the same repository; transfer to mini-SWE-agent v2 | Raw trajectories vs. single abstraction levels vs. mixed hierarchy |
| [MACLA](../works/macla.md) | Procedures and meta-procedures for a frozen LLM | Environment outcomes updating a Beta posterior per procedure | Test splits of four benchmarks | Bayesian selection, contrastive refinement, and meta-procedures ablated separately |
| [Agent Workflow Memory](../works/agent-workflow-memory.md) | Reusable workflows with placeholder values | Annotated examples (offline); LM-evaluator success labels on own test trajectories (online) | Mind2Web cross-task, cross-website, and cross-domain splits | Offline vs. online induction; text vs. code workflows |
| [MIND-Skill](../works/mind-skill.md) | Skill documents, via an optimized induction prompt | Reconstruction match (LLM judge), environment outcome, documentation rubric (LLM judge) | Held-out AppWorld and BFCL-v3 tasks | Each of the three losses ablated |
| [SkillGen](../works/skillgen.md) | One natural-language skill per base agent | Paired with/without-skill reruns counting repairs and regressions | Held-out splits of 11 benchmarks; cross-model reuse | Verified best candidate vs. latest candidate vs. no skill |
| [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) | Task-level or subtask-level skills in text or code | None beyond task completion in an ordered stream | Later tasks in the same stream | Granularity and format vs. a no-memory baseline |
| [SkillLens](../works/skilllens.md) | Textual verifier registry routing a four-layer skill graph | Benchmark score minus normalized cost; gap reports from failed tasks | 7:3 evolution/validation split on MuLocbench and ALFWorld | Mixed-granularity adaptation vs. rewrite-all and parent-only |
| [SKILL-KD](../works/skill-kd.md) | Skill file of patches for a frozen student agent | Student rerun success after each teacher-contrasted patch | Held-out splits of five benchmarks, two student–teacher settings | Student-only, teacher-only, batch, and pairwise acquisition; with vs. without consolidation |
| [LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md) | N/A — diagnoses raw and condensed experience in four existing frameworks | Controlled interventions on the inserted experience | Same environments under each intervention | Raw vs. condensed experience; content vs. prompt-structure controls |

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
- [Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents](../works/trace2tower.md)
- [EvoHarnessBench](../works/evoharnessbench.md)
- [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](../works/stair.md)
- [SKILL-KD](../works/skill-kd.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [MIND-Skill](../works/mind-skill.md)
- [SkillGen](../works/skillgen.md)
- [SkillLens](../works/skilllens.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md)
- [MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](../works/macla.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [GATE](../works/gate.md)
- [Agent Workflow Memory](../works/agent-workflow-memory.md)
