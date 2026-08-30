# Planning & Decision-Making Evaluation

> **English** | [简体中文](../zh/topics/planning_decision_evaluation.md) · [← All topics](./README.md)

## Definition

Planning and decision-making evaluation measures whether an agent selects a sound action, action sequence, or plan from the state, goal, constraints, available tools, and evidence known at the time of choice. It includes complete-plan generation, constraint satisfaction, tool and action selection, feedback-conditioned replanning, infeasibility recognition, and evaluation of plan quality against valid alternatives.

## Motivation

End-to-end success entangles planning with execution, tool operation, perception, state tracking, and recovery. A failed run therefore does not establish that the chosen plan was poor, while a successful local action may still have large opportunity cost relative to a better alternative. Planning-specific evaluation makes the decision itself observable: what should the agent do next, why is that choice admissible, and how should it revise the plan when the state changes?

This topic is distinct from long-horizon evaluation, which characterizes how much sequential interaction a task requires, and from trajectory evaluation, which scores a sequence after it has been produced. A planning task can be tool-free and single-response, as in [NATURAL PLAN](../works/natural-plan.md); a long trajectory can fail for reasons unrelated to planning; and a trajectory metric need not judge whether each decision was good under the information available at that moment.

## Existing Approaches

The literature progresses from controlled plan validity toward realistic, agent-native decisions:

- **Formal and verifiable planning.** [PlanBench](../works/planbench.md) translates classical planning domains into natural language and uses formal planners and validators to score plan generation, cost optimality, state reasoning, and replanning. Its obfuscated domains probe whether models are applying transition rules rather than retrieving familiar lexical patterns.
- **Natural-language constraint planning.** [NATURAL PLAN](../works/natural-plan.md) supplies all required flight, map, and calendar information in context, removing tool execution as a confound while varying the number of cities, participants, schedules, and constraints.
- **Tool-using plans under realistic constraints.** [TravelPlanner](../works/travelplanner.md) requires agents to retrieve from a closed multi-tool sandbox and construct itineraries satisfying environment, commonsense, and explicit user constraints. It measures both component constraint pass rates and full-plan feasibility.
- **Agent-native planning diagnostics.** [Agent Planning Benchmark](../works/agent-planning-benchmark.md) explicitly separates holistic plans from feedback-conditioned one- to three-step decisions, then introduces extraneous tools, broken tools with substitutes, and logically unsolvable tasks.
- **Execution-grounded embodied planning.** [LoTa-Bench](../works/lota-bench.md) executes language-model plans in a simulator and scores goal completion, while [Embodied Agent Interface](../works/embodied-agent-interface.md) localizes affordance and planning errors against simulator state.
- **Reference-plan and process comparison.** [AISE-Bench](../works/aise-bench.md) measures graph edit distance from annotated gold plans; [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) supplies validated implementation-planning ground truth; and [RigorBench](../works/rigorbench.md) scores planning fidelity separately from engineering outcomes.
- **Plan and trajectory preference.** [Plan-RewardBench](../works/plan-rewardbench.md) asks evaluators to choose between preferred and confusable tool-use trajectories, including single- and multi-turn planning splits. This line evaluates the judge of a plan rather than the planner itself.
- **Scientific project planning.** [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) holds the research goal fixed and uses expert and model panels to score methods, resources, feasibility, timelines, and risks in proposals for real physics and astronomy projects.

## Comparison

| Work | Planning object | Information / feedback | Validity or quality signal | Planning isolated from execution? | Counterfactual alternatives |
|---|---|---|---|---|---|
| PlanBench | Complete formal plan; replanned suffix | Explicit action model, initial state, goal; changed state for replanning | Solver / validator correctness and cost optimality | Yes | Optimal-cost reference for one task family |
| NATURAL PLAN | Natural-language itinerary or schedule | All tool-derived facts supplied in context; no live feedback | Exact match to golden plan | Yes | No |
| TravelPlanner | Multi-day tool-grounded itinerary | Tool retrieval and environment feedback | Deterministic environment, commonsense, hard-constraint, and final pass rates | No | No |
| Agent Planning Benchmark | Holistic plan or next 1–3 actions | Full task for holistic mode; trajectory prefix and feedback for step-wise mode | Correctness, graded rubric, E1–E6 errors | Yes; downstream transfer tested separately | Alternative tools and refusal cases, but no exhaustive regret metric |
| LoTa-Bench | Executable embodied plan | Simulator observations | Executed goal satisfaction | No | No |
| Embodied Agent Interface | Per-module embodied decisions | Simulator state and affordances | State-grounded planning-error diagnosis | No | No |
| AISE-Bench | Tool/API plan graph | Per-instance query and tool environment | Graph edit distance to annotated gold plan | Partially | One annotated reference plan |
| SWE-RPG | Requirement and implementation plan | Repository issue and code context | Alignment to validated planning ground truth plus executable patch checks | Partially | No |
| RigorBench | Engineering plan and adherence during execution | Repository state and execution trace | Planning-fidelity pillar, reported separately from outcome | No | No |
| Plan-RewardBench | Pair of tool-use trajectories | Full recorded conversations, tools, calls, and outputs | Gold pairwise preference | Evaluates the judge, not execution | One confusable alternative per pair |
| AI's Capability in Assisting Scientific Research II | One-page research proposal | Fixed expert-written title, background, and goal | Human and LLM rubric scores | Yes | Human and three model proposals per project |

## Open Questions

- **Counterfactual decision quality and regret.** A valid action can still be globally poor. How can an evaluator estimate the opportunity cost of choosing `a_t` rather than the best available alternative, `V(s_t, a_t*) - V(s_t, a_t)`, when exhaustive branching or a trusted simulator is unavailable?
- **Decision-time information boundaries.** Retrospective judges can accidentally use observations that were not available when an action was chosen. How should benchmarks enforce the agent's information set at time `t` while still using later outcomes as evidence?
- **Planning versus execution attribution.** When a good plan fails in execution, or a weak plan succeeds through recovery, what intervention or paired-run design can identify the causal contribution of the planner?
- **Multiple valid plans.** Exact match and distance to one gold plan penalize legitimate alternatives, while open-ended rubric judges may be inconsistent. How can evaluation represent a set or distribution of valid plans without making verification intractable?
- **Replanning under irreversible change.** Current tests commonly inject a broken tool or changed state. Real scientific and engineering work also changes evidence, budgets, safety envelopes, and downstream option value; evaluation needs to distinguish prudent revision from reactive plan churn.
- **Resource-aware action choice.** Resource-aware evaluation asks how much was spent; planning evaluation asks whether spending those resources on this action was justified relative to alternatives. Joint benchmarks need cost-calibrated decision value without collapsing cost and task quality into one opaque score.
- **Long-horizon credit for locally reasonable choices.** A sequence may contain no obviously invalid step yet converge to a poor outcome. It remains unclear how to score locally defensible decisions whose accumulated strategic effect is harmful.

## Related Works

- [PG-HAP](../works/pg-hap.md) — stepwise policy over high-level reasoning actions.
- [HiPER](../works/hiper.md) — high-level subgoal planning separated from low-level execution.
- [PTA-GRPO](../works/pta-grpo.md) — compact plan guidance optimized alongside detailed reasoning.
- [PlanBench](../works/planbench.md) — formal plan generation, optimality, validation, and replanning.
- [NATURAL PLAN](../works/natural-plan.md) — natural-language constraint planning with tool information supplied in context.
- [TravelPlanner](../works/travelplanner.md) — tool-using real-world planning under heterogeneous constraints.
- [Agent Planning Benchmark](../works/agent-planning-benchmark.md) — holistic, feedback-conditioned, robustness, and infeasibility diagnostics.
- [LoTa-Bench](../works/lota-bench.md) — simulator-executed embodied planning.
- [Embodied Agent Interface](../works/embodied-agent-interface.md) — state-grounded localization of embodied planning failures.
- [AISE-Bench](../works/aise-bench.md) — gold-plan graph comparison for tool learning.
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) — validated implementation-planning ground truth in repository issue resolution.
- [RigorBench](../works/rigorbench.md) — planning fidelity scored separately from engineering outcome.
- [Plan-RewardBench](../works/plan-rewardbench.md) — pairwise judging of tool-use trajectories with dedicated planning splits.
- [AI's Capability in Assisting Scientific Research II](../works/ai-assisting-research-ii-project-planning.md) — expert-rubric evaluation of plans for real research projects.
