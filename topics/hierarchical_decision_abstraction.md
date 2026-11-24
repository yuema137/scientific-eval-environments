# Hierarchical Decision Abstraction

> **English** | [简体中文](../zh/topics/hierarchical_decision_abstraction.md) · [← All topics](./README.md)

## Start Here

One agent trajectory can be described at several useful scales. An autonomous car chooses a route, decides to change lanes, and then emits steering, throttle, and brake controls. Calling all of these simply “actions” hides which decision failed.

The same problem appears in scientific agents. `Diagnose the data pipeline` can be a high-level action that expands into reading logs, checking distributions, and running one discriminating test. If the diagnosis was sensible but the script used the wrong column, repair the executor; if every command ran correctly but the diagnosis was poor, repair the planner. The hierarchy improves diagnosis only when each level has a clear interface and a defensible score.

## Definition

An agent acts at more than one scale. It chooses a goal, a strategy, a subgoal, a reasoning operation, a tool call, and finally tokens or low-level controls. Hierarchical decision abstraction decides where to draw those boundaries and how to represent, score, and improve each level. Its first question is not whether a decision was good, but what span of behavior should count as one decision.

## Motivation

A flat terminal score mixes strategy with execution. In autonomous driving, choosing a route, deciding to change lanes, and moving the steering wheel happen at different time scales. A scientific agent has the same structure: it chooses a diagnostic strategy, selects an experiment, invokes a tool, and writes the code that drives it. Compressing all four into one trajectory hides which layer failed.

Once the levels are visible, evaluation can distinguish a sound subgoal followed by poor execution from a poor subgoal executed perfectly. Training can send reward to the responsible level, and developers can repair the planner, executor, skill, or controller instead of retraining the whole system. The hierarchy therefore connects diagnosis directly to a modular intervention.

This differs from [Skill Hierarchy](./skill_hierarchy.md), which asks what abilities a task requires. It also differs from [Planning & Decision-Making Evaluation](./planning_decision_evaluation.md), which asks whether the chosen decision was good. Here the question is the decision's granularity: route, maneuver, control input, or another level.

## Existing Approaches

- **Token macro-actions.** [MA-RLHF](../works/ma-rlhf.md) groups token sequences or higher-level language constructs into macro-actions, shortening the effective horizon between action and reward.
- **Learned latent actions.** [CoLA](../works/cola.md) learns a compact action space from future-token-conditioned inverse dynamics instead of fixing the action vocabulary by hand.
- **Semantic reasoning actions.** [MetaAct-RL](../works/metaact-rl.md) models reasoning as selection and execution of meta-actions such as forward reasoning, critique, and refinement.
- **Policy-selected cognitive operations.** [PG-HAP](../works/pg-hap.md) trains a lightweight planner over named reasoning actions while freezing the executor, isolating the value of action selection from language generation ability.
- **Subgoal-to-execution hierarchy.** [HiPER](../works/hiper.md) separates a high-level subgoal planner from a low-level multi-action executor and assigns advantage at both levels.
- **Plan-guided token reasoning.** [PTA-GRPO](../works/pta-grpo.md) distills compact plans and jointly rewards plan quality and the final reasoning output.
- **Reusable meta-abilities.** [Beyond 'Aha!'](../works/beyond-aha.md) explicitly aligns deduction, induction, and abduction before domain-specific RL, treating general reasoning primitives as learning targets rather than accidental emergent behavior.

A second line leaves model weights unchanged and draws the levels from stored trajectories. The abstraction is a memory or skill artifact placed in a frozen agent's context, and levels are compared by running the same agent on the same tasks with different artifacts.

- **Single-level versus mixed-level ablation.** [STAIR](../works/stair.md) abstracts past issue-repair trajectories into plan trees with low-, medium-, and high-level nodes. On 125 SWE-bench Verified instances with one backbone, raw trajectories resolve 72, single levels 73 to 80, and the mixed hierarchy 100. [Trace2Tower](../works/trace2tower.md) induces action, procedure, and strategy skills from an outcome-weighted transition graph; on ALFWorld its strategy-only variant reaches 84.83% against 87.31% for the full three-level library, with 1,966 against 3,623 characters of skill context.
- **Granularity as the manipulated variable.** [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) keeps one induction prompt and changes only whether a skill is written per task or per subtask. Averaged over 11 models, task-level text skills fall below the no-memory baseline (20.9% against 22.1%) while subtask-level text skills rise above it (26.7% against 24.8%), so the unit of abstraction decides the sign of the effect.
- **Sub-routines and meta-procedures.** [Agent Workflow Memory](../works/agent-workflow-memory.md) induces sub-task workflows with placeholder values and lets later workflows reuse earlier ones as sub-goals; it also compares workflows placed in context with workflows exposed as callable actions. [MACLA](../works/macla.md) composes recurring procedures into meta-procedures with a continue/skip/repeat/abort control policy; removing the meta-procedure level lowers ALFWorld unseen success from 90.3 to 78.4.
- **Choosing the level per unit at reuse time.** [SkillLens](../works/skilllens.md) stores skills as policies, strategies, procedures, and primitives, and a verifier decides per unit whether to accept, decompose, rewrite, or skip it. Its comparison against rewrite-all and parent-only adaptation reports both accuracy and adaptation cost.
- **Abstraction for analysis and guidance.** [ATLAS](../works/atlas-agent-strategies.md) maps each action-observation pair to an abstract symbol and learns a Markov chain over the symbolic traces of many runs. An analyst reads the chain for strategies and failure loops, and the same chain guides smaller executor models, whose success on penetration-testing machines rises from 5.0% and 1.7% without guidance to 28.3% and 38.3% in the dynamic mode.

These works measure whether a level helps a fixed agent at inference time. None trains the agent at the new level, so they do not show whether the same hierarchy would help a policy optimized on it.

## Comparison

| Work | Decision unit | Abstraction source | Lower-level executor | Evaluation of the abstraction |
|---|---|---|---|---|
| MA-RLHF | Token macro-action | Fixed-length or learned token grouping | Same LLM policy | Reward, task quality, convergence speed |
| CoLA | Compact latent action | Learned inverse dynamics | Language world model | Math, preference, and agent-task performance; seen/unseen splits |
| MetaAct-RL | Forward reasoning, critique, refinement | Authored semantic action set | Same model emits action and content | Six reasoning benchmarks, action diversity, sampling efficiency |
| PG-HAP | Analysis, decomposition, reasoning, coding, verification, knowledge, final answer | Authored action set and transition graph | Frozen LLM | Accuracy, redundancy, and action-sequence diversity |
| HiPER | Subgoal | Planner-generated | Low-level agent policy over environment actions | Success plus planner- and executor-level advantage analyses |
| PTA-GRPO | Compact high-level guidance | Distilled from solution traces | Same LLM generates fine-grained reasoning | Ten reasoning benchmarks and plan-quality reward |
| Beyond 'Aha!' | Deduction, induction, abduction | Authored meta-ability taxonomy and synthetic tasks | Domain-specific reasoning model | Held-out math, coding, and science transfer |
| [STAIR](../works/stair.md) | Plan-tree node: artifact-specific sub-goal, project-agnostic strategy, or cross-project principle | LLM grouping and abstraction of past repair trajectories, segmented by repair stage | Frozen coding agent (Lingxi; mini-SWE-agent v2 for transfer) receiving per-stage plans in its prompt | SWE-bench Verified Pass@1; 125-instance ablation of raw trajectories vs. each single level vs. mixed levels |
| [Trace2Tower](../works/trace2tower.md) | Action, procedure, or strategy skill | Spectral clustering of an outcome-contrastive transition graph over past trajectories | Fixed Skill User model retrieving skills under a token budget | ALFWorld and WebShop success, steps, invalid actions, and context size; strategy-only variant and component ablations |
| [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) | Task-level vs. subtask-level skill, in text or code | Same induction prompt applied after each task or each subtask | Same LLM agent retrieving skills by embedding similarity | Success against a no-memory baseline at each level over 11 models and three benchmarks; run-free utility score |
| [Agent Workflow Memory](../works/agent-workflow-memory.md) | Sub-task workflow with placeholder values, reusable inside later workflows | LM induction from annotated examples (offline) or from LM-evaluator-approved test trajectories (online) | Same web agent, with workflows in memory or as callable actions | WebArena and Mind2Web success and steps; text vs. code and context vs. action-space ablations |
| [MACLA](../works/macla.md) | Procedure, and meta-procedure with a continue/skip/repeat/abort control policy | Frozen-LLM segmentation of trajectories, merged by embedding similarity | Frozen Llama-2-7B | Scores on four benchmarks; ablation removing the meta-procedure level |
| [SkillLens](../works/skilllens.md) | Policy, strategy, procedure, or primitive skill unit | Four-layer skill graph | Main agent receiving units accepted, decomposed, or locally rewritten by a verifier | MuLocbench and ALFWorld accuracy plus time and token cost vs. rewrite-all and parent-only adaptation |
| [ATLAS](../works/atlas-agent-strategies.md) | (action category, observation category) symbol; learned Markov-chain state | LLM categorization and normalization of traces, then Alergia automata learning | Analyst reading the model; small executor models guided by extracted strategies | Qualitative model inspection; executor successes out of 60 runs under five guidance modes |

## Open Questions

- **Transfer versus repackaging.** Does a higher-level action space produce compositional OOD transfer, or merely compress familiar trajectories into a new template vocabulary?
- **Choosing the level.** Which abstraction is useful for a given environment, and can an agent move between levels without hiding important decisions inside an oversized macro-action?
- **Action discovery.** Hand-authored semantic actions are interpretable but may encode the designer's ontology; learned latent actions may discover useful structure but can recreate the black box this hierarchy was meant to open.
- **Level-specific ground truth.** How can a benchmark label a high-level decision as wrong when several strategies are valid and only downstream outcomes are observable?
- **Cross-level credit.** When a good subgoal fails because of execution, how should rewards and blame be separated without assuming planner and executor independence?
- **Interface errors.** A hierarchy can fail at translation between levels even when both modules are competent. Evaluation needs to distinguish planner error, executor error, and grounding/interface error.
- **Matched abstraction studies.** The field lacks controlled comparisons that hold model, data, reward, compute, and environment fixed while changing only the action representation, then measure IID success, OOD transfer, composition, sample efficiency, strategy diversity, and decision cost. STAIR and Break It Down, Pass It On hold the agent and tasks fixed while changing only the level of a stored artifact, but they involve no training and report task success rather than the full set of measures.

## Related Works

- [Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents](../works/trace2tower.md)
- [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md)
- [ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning](../works/atlas-agent-strategies.md)
- [STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](../works/stair.md)
- [SkillLens](../works/skilllens.md)
- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](../works/macla.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [CoLA](../works/cola.md)
- [MA-RLHF](../works/ma-rlhf.md)
- [Agent Workflow Memory](../works/agent-workflow-memory.md)
