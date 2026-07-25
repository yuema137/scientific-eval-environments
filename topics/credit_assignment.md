# Credit Assignment

## Definition

Credit assignment, in evaluation, is the problem of attributing a trajectory's success or failure to specific steps, subgoals, or intermediate outputs — rather than treating success as an unstructured property of the trajectory as a whole. In benchmarks, credit-assignment machinery shows up as dense intermediate rewards, partial-credit scoring, or per-step scoring that survives when the terminal outcome is a single bit.

## Motivation

Long-horizon and open-ended tasks produce trajectories where a single terminal signal — pass or fail — is too coarse to be useful. Two failing trajectories can differ in *where* they went wrong; two successful trajectories can differ in whether the success was earned by sound intermediate reasoning or by a lucky final step. Credit assignment is the design commitment to preserve that finer signal at evaluation time.

Credit assignment is related to but distinct from [Skill Hierarchy](./skill_hierarchy.md). Skill hierarchy asks *which subskill an agent has*; credit assignment asks *which step of a trajectory drove the outcome*. Many benchmarks contribute to both.

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

## Open Questions

- **Where to assign credit.** Per subgoal (AgentBoard), per graded subtask (Long-Horizon-Terminal-Bench), per trajectory-level dimension (FinTrace, TRACE) — each choice reflects a different theory of what a trajectory is made of. Are these equivalent under aggregation, or do they surface distinct model behaviors?
- **Weighting.** Threshold-based aggregation (Long-Horizon-Terminal-Bench) and utility functions (TRACE) both need weights. How should the weights be chosen so that credit-assigned scores are comparable across benchmarks?
- **Judge dependence.** Trajectory-level dimensions like "reasoning quality" typically require a model or human judge. Is the reliability of the judge itself a bottleneck for credit-assignment metrics?

## Related Works

- [AgentBoard](../works/agentboard.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FinTrace](../works/fintrace.md)
- [TRACE](../works/trace.md)
- [Gaia2](../works/gaia2.md)
- [QVal](../works/qval.md)
- [Hard2Verify](../works/hard2verify.md)
- [Who&When Pro](../works/who-and-when-pro.md)
- [CUARewardBench](../works/cuarewardbench.md)
- [ToolPRMBench](../works/toolprmbench.md)
- [ProcessBench](../works/processbench.md)
- [PRMBench](../works/prmbench.md)
- [FormalRewardBench](../works/formalrewardbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
