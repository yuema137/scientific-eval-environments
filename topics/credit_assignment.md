# Credit Assignment

> **English** | [简体中文](../zh/topics/credit_assignment.md) · [← All topics](./README.md)

## Start Here

Suppose an agent takes 30 steps and fails on the last one. A terminal score of zero treats the first 29 steps exactly like a run that failed immediately. That is too little information for diagnosis or learning.

Credit assignment changes the scoring path. The evaluator may award completed subgoals, label the first bad step, or estimate which action changed the outcome. A trace can then read `plan correct → data loaded correctly → wrong unit conversion → failed result`. This identifies where credit or blame belongs, but only if the intermediate labels or counterfactual estimates are trustworthy.

## Definition

Credit assignment asks which part of a trajectory produced the result. Instead of attaching one pass or fail label to the whole run, an evaluator can score completed subgoals, intermediate outputs, or individual actions. The terminal result may still be one bit, but the retained step-level signal shows where progress happened and where it stopped.

## Motivation

Long and open-ended tasks can fail in many different ways. One agent may choose the right plan and make a unit error near the end; another may choose the wrong plan immediately. A zero gives both runs the same label. The reverse problem also occurs: two successful runs may contain very different amounts of sound reasoning, wasted work, or luck. Credit assignment preserves those differences so developers know what to repair and learners receive a more useful signal.

This is not the same as [Skill Hierarchy](./skill_hierarchy.md). Skill hierarchy asks which abilities an agent has. Credit assignment asks which event in this run changed the outcome. One benchmark can answer both questions, but the labels and evidence are different.

## Existing Approaches

- **Partial credit via subgoal progress.** [AgentBoard](../works/agentboard.md) gives credit for the fraction of annotated subgoals completed, so a trajectory that fails at the end still receives non-zero score if it made intermediate progress.
- **Graded partial reward under thresholds.** [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) decomposes tasks into subtasks with graded rewards and aggregates them under configurable thresholds (0.95 partial-reward, 1.0 perfect-reward), letting the metric distinguish "almost solved" from "no progress."
- **Per-dimension credit across a trajectory.** [FinTrace](../works/fintrace.md) scores whole trajectories against 9 metrics across 4 dimensions (action correctness, execution efficiency, process quality, output quality), so a trajectory can succeed on some dimensions and fail on others.
- **Utility-function credit.** [TRACE](../works/trace.md) applies a hierarchical trajectory utility function that jointly credits accuracy, efficiency, evidence grounding, and reasoning quality — treating them as complementary sources of credit rather than substitutes.
- **Action-level credit against an oracle DAG.** [Gaia2](../works/gaia2.md) credits only state-changing write actions, checked against a minimal oracle sequence along four dimensions — consistency, causality, timing, and completeness — while leaving read actions unlimited and unpenalized. On 450 hand-labeled trajectories the verifier reaches 0.98 agreement against 0.72 for an LLM-judge-only baseline.
- **Meta-evaluation of the credit signal itself.** [QVal](../works/qval.md) scores 21 dense supervision methods by how well their per-step scores rank candidate actions against reference-policy Q-values, making the step-level credit signal the object of evaluation rather than the agent.
- **Expert step labels on frontier proofs.** [Hard2Verify](../works/hard2verify.md) has mathematical experts label all 1,860 steps of 200 frontier-model Olympiad solutions under grading that carries no credit forward, so a step loses credit as soon as any earlier step it depends on is wrong.
- **Golden decisive-step labels by construction.** [Who&When Pro](../works/who-and-when-pro.md) injects a single error into an exactly replayed successful prefix across 12,326 failed trajectories, so credit for a failure lands on one agent, step, and error mode by construction rather than by annotation.
- **Benchmarking the step-level judge itself.** [CUARewardBench](../works/cuarewardbench.md) scores vision-language reward models against 346 expert step-correctness labels over 272 annotated computer-using agent trajectories, making the reliability of the per-step credit signal a measured quantity rather than an assumed one.
- **Step-level reward-model benchmarking.** [ToolPRMBench](../works/toolprmbench.md) converts tool-use agent trajectories into 987 forced-choice step cases across four source benchmarks and ranks 17 LLMs, general PRMs, and tool-specialized PRMs on whether they pick the correct action over a plausible incorrect one.
- **Step-level error localization.** [ProcessBench](../works/processbench.md) asks a judge to return the index of the earliest erroneous step across 3,400 expert-annotated math solutions, and finds that 51.8% of Omni-MATH solutions with correct final answers still contain a process error.
- **Error-type-resolved step credit.** [PRMBench](../works/prmbench.md) benchmarks process-level reward models against nine injected error sub-categories, so a model's credit signal is diagnosed by failure mode rather than by aggregate step accuracy.
- **Benchmarking the reward models that would densify credit.** [FormalRewardBench](../works/formalrewardbench.md) tests whether learned reward models prefer a verified Lean 4 proof over an injected-error variant across 250 preference pairs, making the credit signal itself the measured object rather than the scoring instrument.
- **Standardized computer-use judge benchmarking.** [OSReward](../works/osreward.md) scores cross-platform computer-use reward models against multi-stage human-annotated verdicts, identifies systematic leniency bias in state-of-the-art judges, and shows that open 9B/35B judges trained on its OS-Shepherd-100K corpus match frontier commercial judges at 30–60× lower cost.
- **Localize, attribute, repair.** [SearchAuditor](../works/searchauditor.md) grades auditors end-to-end on 1,243 expert-annotated failed search trajectories — localization of the critical error step, attribution to a search-specific root cause, and repair against reference rubrics — with the strongest baseline passing only 26.6% end-to-end.
- **Credit inside the skill artifact.** [SkillSV](../works/skillsv.md) moves credit assignment from trajectory steps to the internal units of an agent skill: structure-aware Shapley valuation over a skill's compiled units, dependencies, and hierarchy, with paired deletion and length-neutral padding separating content value from context cost.
- **Credit at the step of a skill, under a measured estimation budget.** [SkillShapley](../works/skillshapley.md) pushes the same idea one level finer than SkillSV, treating each individual step of a skill as a player in a coalitional game. Its contribution is as much to the estimator as to the attribution: because agentic benchmark rewards are discretized into cliffs and step interactions turn out to be largely additive, the sampler concentrates its budget near informative boundaries, and its approximation error is reported against exact Shapley values rather than assumed.
- **Error-lifecycle attribution.** [TRAJDEBUG](../works/trajdebug.md) traces each detected error's resolution status and terminal impact over TrajErrBench's 486 manually annotated failed trajectories, so credit for a failure lands on the error that actually determined it rather than on errors the agent later recovered from.
- **Fault-origin localization from telemetry.** [TelemetrySuffBench](../works/telemetrysuffbench.md) tests whether execution telemetry is sufficient to attribute a failure to its origin component, using delayed-binding faults that decouple symptom from cause and exact-equal ambiguous origin pairs that make abstention the correct answer.
- **Component-level trajectory attribution.** [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md) attributes an observed agent outcome to the responsible trajectory component and recovers the surrounding attribution chain, with likelihood-based and leave-one-out reference baselines.
- **Minimal necessary cause.** [TempoBench](../works/tempobench.md) isolates counterfactual credit assignment — which inputs were necessary for an observed output — over formally labeled Mealy-machine execution traces, distinct from forward simulation.

## Comparison

| Benchmark | Year | Credit signal | Trajectory unit credited | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | Fraction of annotated subgoals completed | Per subgoal | [→](../works/agentboard.md) |
| Long-Horizon-Terminal-Bench | 2026 | Graded subtask reward + threshold aggregation | Per subtask, weighted | [→](../works/long-horizon-terminal-bench.md) |
| FinTrace | 2026 | 9 metrics × 4 dimensions | Per trajectory, per dimension | [→](../works/fintrace.md) |
| TRACE | 2026 | Hierarchical utility over accuracy / efficiency / grounding / reasoning | Per trajectory, per component | [→](../works/trace.md) |
| Gaia2 | 2026 | Write-action match to a minimal oracle sequence (consistency / causality / timing / completeness) | Per state-changing action | [→](../works/gaia2.md) |
| QVal | 2026 | Q-alignment of a method's score with reference-policy Q-values | Per state-action pair | [→](../works/qval.md) |
| Hard2Verify | 2025 | Binary expert step label; first-error index | Per proof step | [→](../works/hard2verify.md) |
| Who&When Pro | 2026 | Golden agent / step / error-mode labels from controlled error injection | Per step, one decisive step per trace | [→](../works/who-and-when-pro.md) |
| CUARewardBench | 2025 | Expert binary correct/incorrect label per key action, used to score VLM reward models | 346 selected key actions across 272 annotated trajectories | [→](../works/cuarewardbench.md) |
| ToolPRMBench | 2026 | Forced-choice accuracy on a correct vs. plausible incorrect action pair | Single decision step | [→](../works/toolprmbench.md) |
| ProcessBench | 2024 | Earliest erroneous step index, expert-annotated | Reasoning step within a static solution | [→](../works/processbench.md) |
| PRMBench | 2025 | Step-level validity + redundancy scores; negative F1 and PRMScore | Individual reasoning step in a static solution process | [→](../works/prmbench.md) |
| FormalRewardBench | 2026 | Preference judgment between a verified proof and an injected-error variant | Per whole proof; no step-level credit | [→](../works/formalrewardbench.md) |
| OSReward | 2026 | Reward-model verdicts vs. multi-stage human annotation; fine-grained efficiency and alignment scores (Multi split) | Computer-use trajectories judged whole, plus per-dimension | [→](../works/osreward.md) |
| SearchAuditor | 2026 | Expert-annotated critical step, search-specific root cause, rubric-graded repair | Per critical step within a failed search trajectory | [→](../works/searchauditor.md) |
| SkillSV | 2026 | Structure-aware Shapley value over a skill's compiled units | Per skill unit, not per trajectory step | [→](../works/skillsv.md) |
| TRAJDEBUG | 2026 | Error lifecycle: occurrence, resolution status, terminal impact | Per error within a failed trajectory | [→](../works/trajdebug.md) |
| TelemetrySuffBench | 2026 | Origin-step localization from telemetry with delayed-binding faults; abstention on ambiguous origins | Per injected fault-origin component / event | [→](../works/telemetrysuffbench.md) |
| Long-Horizon Agent Trajectory Attribution | 2026 | Primary-component attribution (Hit@1 / MRR) + attribution-chain recovery (Recall@K / MAP) | Per trajectory component (root cause + chain) | [→](../works/long-horizon-agent-trajectory-attribution.md) |
| TempoBench | 2025 | Minimal-necessary-cause identification via counterfactual attribution, vs. forward simulation | Per input condition of an execution trace | [→](../works/tempobench.md) |
| SkillShapley | 2026 | Shapley value over coalitions of skill steps, estimated by boundary-adaptive sampling; MAE against exact Shapley values plus removal-validation curves | Per step inside an agent skill, not per trajectory step | [→](../works/skillshapley.md) |

## Open Questions

- **Where to assign credit.** Per subgoal (AgentBoard), per graded subtask (Long-Horizon-Terminal-Bench), per trajectory-level dimension (FinTrace, TRACE) — each choice reflects a different theory of what a trajectory is made of. Are these equivalent under aggregation, or do they surface distinct model behaviors?
- **Weighting.** Threshold-based aggregation (Long-Horizon-Terminal-Bench) and utility functions (TRACE) both need weights. How should the weights be chosen so that credit-assigned scores are comparable across benchmarks?
- **Judge dependence.** Trajectory-level dimensions like "reasoning quality" typically require a model or human judge. Is the reliability of the judge itself a bottleneck for credit-assignment metrics?

## Related Works

- [SkillShapley](../works/skillshapley.md)
- [TelemetrySuffBench](../works/telemetrysuffbench.md)
- [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md)
- [TRAJDEBUG](../works/trajdebug.md)
- [SearchAuditor](../works/searchauditor.md)
- [SkillSV](../works/skillsv.md)
- [OSReward](../works/osreward.md)
- [Who&When Pro](../works/who-and-when-pro.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [QVal](../works/qval.md)
- [FormalRewardBench](../works/formalrewardbench.md)
- [FinTrace](../works/fintrace.md)
- [From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models](../works/from-reasoning-to-agentic.md)
- [HiPER](../works/hiper.md)
- [Gaia2](../works/gaia2.md)
- [TRACE](../works/trace.md)
- [ToolPRMBench](../works/toolprmbench.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [TempoBench](../works/tempobench.md)
- [CUARewardBench](../works/cuarewardbench.md)
- [Hard2Verify](../works/hard2verify.md)
- [PRMBench](../works/prmbench.md)
- [ProcessBench](../works/processbench.md)
- [MA-RLHF](../works/ma-rlhf.md)
- [AgentBoard](../works/agentboard.md)
## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
