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

## Comparison

| Benchmark | Year | Credit signal | Trajectory unit credited | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | Fraction of annotated subgoals completed | Per subgoal | [→](../works/agentboard.md) |
| Long-Horizon-Terminal-Bench | 2026 | Graded subtask reward + threshold aggregation | Per subtask, weighted | [→](../works/long-horizon-terminal-bench.md) |
| FinTrace | 2026 | 9 metrics × 4 dimensions | Per trajectory, per dimension | [→](../works/fintrace.md) |
| TRACE | 2026 | Hierarchical utility over accuracy / efficiency / grounding / reasoning | Per trajectory, per component | [→](../works/trace.md) |

## Open Questions

- **Where to assign credit.** Per subgoal (AgentBoard), per graded subtask (Long-Horizon-Terminal-Bench), per trajectory-level dimension (FinTrace, TRACE) — each choice reflects a different theory of what a trajectory is made of. Are these equivalent under aggregation, or do they surface distinct model behaviors?
- **Weighting.** Threshold-based aggregation (Long-Horizon-Terminal-Bench) and utility functions (TRACE) both need weights. How should the weights be chosen so that credit-assigned scores are comparable across benchmarks?
- **Judge dependence.** Trajectory-level dimensions like "reasoning quality" typically require a model or human judge. Is the reliability of the judge itself a bottleneck for credit-assignment metrics?

## Related Works

- [AgentBoard](../works/agentboard.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [FinTrace](../works/fintrace.md)
- [TRACE](../works/trace.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
