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

## Open Questions

- **Transfer versus repackaging.** Does a higher-level action space produce compositional OOD transfer, or merely compress familiar trajectories into a new template vocabulary?
- **Choosing the level.** Which abstraction is useful for a given environment, and can an agent move between levels without hiding important decisions inside an oversized macro-action?
- **Action discovery.** Hand-authored semantic actions are interpretable but may encode the designer's ontology; learned latent actions may discover useful structure but can recreate the black box this hierarchy was meant to open.
- **Level-specific ground truth.** How can a benchmark label a high-level decision as wrong when several strategies are valid and only downstream outcomes are observable?
- **Cross-level credit.** When a good subgoal fails because of execution, how should rewards and blame be separated without assuming planner and executor independence?
- **Interface errors.** A hierarchy can fail at translation between levels even when both modules are competent. Evaluation needs to distinguish planner error, executor error, and grounding/interface error.
- **Matched abstraction studies.** The field lacks controlled comparisons that hold model, data, reward, compute, and environment fixed while changing only the action representation, then measure IID success, OOD transfer, composition, sample efficiency, strategy diversity, and decision cost.

## Related Works

- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [CoLA](../works/cola.md)
- [MA-RLHF](../works/ma-rlhf.md)
