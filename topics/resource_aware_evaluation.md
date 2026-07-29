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
- **A dedicated dataset for cost-aware planning.** [CATP-LLM / OpenCATP](../works/catp-llm.md) contributes OpenCATP, described as the first dataset for cost-aware planning (11,100 samples), where tool execution cost (e.g., execution time) is scored jointly with task performance. Its paired planning method is agent-construction work outside this repository's scope; the dataset is the resource-aware evaluation contribution documented here.
- **Fidelity-priced measurement budgets.** [MaD Physics](../works/mad-physics.md) charges each observation a cost that rises with its precision and caps total spend per trial, so agents must allocate a fixed budget across measurements to infer an unknown — and sometimes altered — physical law.
- **Budget as an online control signal.** [BAGEN](../works/bagen.md) makes the agent predict an upper and lower bound on remaining budget at every turn and flag infeasibility, scoring resource use as a per-step estimation target rather than a post-execution tally.
- **Evaluation calls as the budgeted resource.** [VeRO / VeRO-Bench](../works/vero.md) benchmarks coding agents that optimize other agents under a hard evaluation-call budget: every scoring of the target agent passes through a gated evaluator that decrements n_E ≤ B and blocks requests beyond it, mirroring black-box optimization with expensive queries; a budget ablation over B ∈ {2, 4, 8, 16, 32} separates budget effects from capability effects.
- **Cost-performance frontier reporting.** Other work reports accuracy alongside token or dollar cost so that agents can be compared on a Pareto frontier rather than a single accuracy number. This is analysis-time resource-awareness rather than benchmark-time resource-awareness.

## Comparison

| Benchmark | Year | Resource currency | Resource role | Setting | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | Configurable per-tool costs (atomic and composite) | First-class objective — plan for cost-optimality | Dynamic (blocking events); ~40% static→dynamic drop | [→](../works/costbench.md) |
| SimulCost | 2026 | Simulation time + experimental resources | First-class objective — parameter tuning under budget | Single-round and multi-round; 13 simulators | [→](../works/simulcost.md) |
| CATP-LLM / OpenCATP | 2024 | Normalized tool price (USD; execution time + memory) | Reported jointly with performance via Quality of Plan (QoP = α·perf − (1−α)·cost) | 111 tool-planning tasks / 11,100 samples | [→](../works/catp-llm.md) |
| MaD Physics | 2026 | Measurement cost (fidelity-priced observations) | Fixed per-trial budget the agent allocates | Simulated classical / fluid / quantum physics | [→](../works/mad-physics.md) |
| BAGEN | 2026 | Tokens; time / occupancy / cost | Prediction target + early-stop objective | Puzzle / retrieval / coding / supply-chain | [→](../works/bagen.md) |
| VeRO / VeRO-Bench | 2026 | Evaluation calls on the target agent (gated budget n_E ≤ B) | Enforced hard constraint — optimizer allocates expensive evaluations | Agent-harness optimization over 5 target-agent task suites | [→](../works/vero.md) |

## Open Questions

- **Resource normalization across settings.** A dollar of API spend, a dollar of tool-call fee, and a second of wall-clock or simulation time do not compare cleanly. Which currency should be canonical for cross-benchmark comparison, and can any of them be canonical at all?
- **Static vs. dynamic robustness.** CostBench reports a substantial static-to-dynamic drop. Is such a gap a property of current models or of the specific perturbation distributions used? Should the field settle on standard perturbations?
- **Reporting vs. optimizing.** Benchmarks that make a resource first-class force the agent to plan under budget; benchmarks that only report resource use do not. Should the two classes be labeled distinctly so their numbers are not silently compared?
- **Token vs. tool-use cost.** Should aggregate leaderboards report only tokens (portable, model-comparable) or also tool-use resources (scientifically meaningful but domain-specific)?

## Related Works

- [CostBench](../works/costbench.md) — Cost-optimal planning under dynamic tool-use conditions.
- [SimulCost](../works/simulcost.md) — Cost-aware physics-simulation parameter tuning across 13 simulators.
- [CATP-LLM / OpenCATP](../works/catp-llm.md) — OpenCATP, a dataset for cost-aware tool planning (11,100 samples).
- [MaD Physics](../works/mad-physics.md) — Fidelity-priced measurement budgets in simulated physics; agents trade measurement quality against quantity to infer altered physical laws.
- [BAGEN](../works/bagen.md) — Progressive budget-interval prediction with trainable early-stopping across token and multi-resource agents.
- [VeRO / VeRO-Bench](../works/vero.md) — Benchmarking coding agents as agent optimizers under a gated evaluation-call budget.

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. Identifies cost-efficiency as an under-covered dimension in current agent evaluation. <https://arxiv.org/abs/2503.16416>
