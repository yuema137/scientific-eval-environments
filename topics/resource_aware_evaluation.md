# Resource-aware Evaluation

## Definition

Resource-aware evaluation treats resource expenditure — tokens, tool-call fees, wall-clock time, compute, simulation time, or a domain-specific currency — as part of what the benchmark measures rather than as a post-hoc statistic. In its strongest form, one such resource (typically cost) becomes an explicit optimization objective the agent must balance against task success.

## Motivation

Agent capability and resource consumption tend to move together: stronger models are usually more expensive, and longer trajectories often yield better answers. Evaluating capability in isolation therefore rewards *solve at any cost*, which does not match the deployment setting for scientific or production agents.

Two meaningful distinctions structure the space:

- **Resource as reported metric** vs. **resource as objective.** The former surfaces trade-offs at analysis time; the latter tests whether the agent can *plan* under a budget.
- **Token cost only** vs. **tool-use cost (simulation time, experimental resources).** Focusing on token cost alone misses the dominant cost in many scientific workflows.

## Existing Approaches

- **Cost as a first-class objective in tool-use.** [CostBench](../works/costbench.md) makes cost minimization the task itself in a travel-planning domain with configurable per-tool costs and blocking events that force replanning.
- **Tool-use cost beyond tokens, in scientific simulation.** [SimulCost](../works/simulcost.md) extends cost-aware evaluation to physics-simulation parameter tuning, explicitly modeling simulation time and experimental-resource costs across 13 simulators, with direct comparison against traditional methods.
- **Cost-performance frontier reporting.** Other work reports accuracy alongside token or dollar cost so that agents can be compared on a Pareto frontier rather than a single accuracy number. This is analysis-time resource-awareness rather than benchmark-time resource-awareness.

## Comparison

| Benchmark | Year | Resource currency | Resource role | Setting | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | Configurable per-tool costs (atomic and composite) | First-class objective — plan for cost-optimality | Dynamic (blocking events); ~40% static→dynamic drop | [→](../works/costbench.md) |
| SimulCost | 2026 | Simulation time + experimental resources | First-class objective — parameter tuning under budget | Single-round and multi-round; 13 simulators | [→](../works/simulcost.md) |

## Open Questions

- **Resource normalization across settings.** A dollar of API spend, a dollar of tool-call fee, and a second of wall-clock or simulation time do not compare cleanly. Which currency should be canonical for cross-benchmark comparison, and can any of them be canonical at all?
- **Static vs. dynamic robustness.** CostBench reports a substantial static-to-dynamic drop. Is such a gap a property of current models or of the specific perturbation distributions used? Should the field settle on standard perturbations?
- **Reporting vs. optimizing.** Benchmarks that make a resource first-class force the agent to plan under budget; benchmarks that only report resource use do not. Should the two classes be labeled distinctly so their numbers are not silently compared?
- **Token vs. tool-use cost.** Should aggregate leaderboards report only tokens (portable, model-comparable) or also tool-use resources (scientifically meaningful but domain-specific)?

## Related Works

- [CostBench](../works/costbench.md) — Cost-optimal planning under dynamic tool-use conditions.
- [SimulCost](../works/simulcost.md) — Cost-aware physics-simulation parameter tuning across 13 simulators.

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. Identifies cost-efficiency as an under-covered dimension in current agent evaluation. <https://arxiv.org/abs/2503.16416>
