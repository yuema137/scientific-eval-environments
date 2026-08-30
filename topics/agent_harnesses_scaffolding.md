# Agent Harnesses & Scaffolding

> **English** | [简体中文](../zh/topics/agent_harnesses_scaffolding.md) · [← All topics](./README.md)

## Start Here

Give the same model to two agent systems and they can behave like different models. One harness may plan before editing, run tests after every change, and retry after failure; another may send one prompt and stop. If we compare only the final scores, we may credit the base model for behavior supplied by the surrounding software.

This topic makes that surrounding software visible. For one coding task, hold the repository, budget, and evaluator fixed, then change only the planning or verification loop. If success rises after a test-and-repair step is added, the gain belongs to the model–harness configuration. The comparison still does not prove the same component will help every model or task.

## Definition

Agent harnesses and scaffolding are the surrounding control structures that shape how a model plans, uses tools, manages context, verifies work, retries, delegates, and terminates. This topic studies harness effects, component attribution, controlled comparison, and evaluation-driven harness optimization.

## Motivation

Observed capability belongs to a model–harness configuration, not automatically to the base model. Without holding tasks and budgets fixed, model comparisons confound planning loops, prompts, tools, permissions, memory, verification, and recovery policies.

## Existing Approaches

- **Controlled harness comparison.** [Harness-Bench](../works/harness-bench.md) fixes tasks, sandboxes, budgets, and evaluators while varying harnesses.
- **Process-discipline measurement.** [RigorBench](../works/rigorbench.md) scores planning, verification, recovery, abstention, and exploration separately from outcome.
- **Autonomous harness improvement.** [Evo-Bench](../works/evo-bench.md), [HarnessOpt-Bench](../works/harnessopt-bench.md), and [VeRO](../works/vero.md) give agents evaluator access and measure held-out lift from harness edits.
- **Cross-loop interaction.** [Curation-Bench](../works/curation-bench.md) shows that a method-guided scaffold changes which data-curation policies an agent explores.
- **Post-training configurations.** [PostTrainBench](../works/posttrainbench.md) compares agents through multiple CLI scaffolds under the same GPU-time protocol.

## Comparison

| Work | Harness role | Controlled variables | Evaluation feedback | Outcome |
|---|---|---|---|---|
| Harness-Bench | Object being compared | Tasks, models, budgets, evaluators | Terminal + process score | Configuration-level capability |
| RigorBench | Source of engineering discipline | Foundation model and tasks | Instrumented process metrics | Process and outcome separation |
| Evo-Bench | Artifact optimized by an agent | Target tasks and evaluator | Iterative benchmark feedback | Improved harness |
| HarnessOpt-Bench | Audited optimization target | Held-out splits and eval budget | Metered evaluator calls | Held-out gain |
| VeRO | Arbitrary programmatic harness | Permissions, versions, budgets | Standardized observation interface | Expected lift |
| Curation-Bench | Research scaffold | Model, recipe, evaluator | Per-iteration benchmark results | Better data policy |

## Open Questions

- Which harness components causally produce gains rather than correlate with them?
- How should model and harness contributions be reported when they interact nonlinearly?
- What prevents adaptive harness optimization from overfitting or gaming the evaluator?
- How should cost, permissions, reproducibility, and security constrain harness search?
- Can harness findings transfer across models, tasks, and scientific environments?

## Related Works

- [Harness-Bench](../works/harness-bench.md)
- [RigorBench](../works/rigorbench.md)
- [Evo-Bench](../works/evo-bench.md)
- [HarnessOpt-Bench](../works/harnessopt-bench.md)
- [VeRO](../works/vero.md)
- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
