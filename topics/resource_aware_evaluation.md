# Resource-aware Evaluation

> **English** | [简体中文](../zh/topics/resource_aware_evaluation.md) · [← All topics](./README.md)

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
- **Observation budgets on physics discovery.** [Gravity-Bench-v1](../works/gravity-bench.md) caps how many observations an agent may take of a simulated two-body gravitational system, so experimental design becomes part of what is scored; per the official project page, the top model falls from 74% with full data access to 49% under the budget.
- **Oracle calls as the priced resource in molecular design.** [SMDD-Bench](../works/smdd-bench.md) bounds each of its 502 guaranteed-solvable drug-design tasks with a limited oracle-call budget, so exploration must be planned rather than exhaustive; the best frontier model solves only 40.2%.
- **Diagnostic cost on the score sheet.** [SDBench](../works/sdbench.md) charges agents (and 21 physicians) for every visit and test ordered while a gatekeeper reveals findings only on request, scoring the accuracy-cost frontier; orchestration shifts that frontier more than model choice.
- **Cost as the task itself.** [ChemCost](../works/chemcost.md) does not budget the agent's spending — it asks the agent to compute what a reaction costs, against a frozen pricing snapshot with judge-free exact ground truth and stage-level failure diagnosis.
- **Budget as an online control signal.** [BAGEN](../works/bagen.md) makes the agent predict an upper and lower bound on remaining budget at every turn and flag infeasibility, scoring resource use as a per-step estimation target rather than a post-execution tally.
- **Evaluation calls as the budgeted resource.** [VeRO / VeRO-Bench](../works/vero.md) benchmarks coding agents that optimize other agents under a hard evaluation-call budget: every scoring of the target agent passes through a gated evaluator that decrements n_E ≤ B and blocks requests beyond it, mirroring black-box optimization with expensive queries; a budget ablation over B ∈ {2, 4, 8, 16, 32} separates budget effects from capability effects.
- **Interaction budget on iterative design optimization.** [Frontier-Eng](../works/frontier-eng.md) bounds each real-world engineering task with a fixed interaction budget on its propose-execute-evaluate loop: the agent must allocate a limited number of simulator interactions to refine a candidate design under continuous reward and hard feasibility constraints, making the benchmark inherently resource-aware.
- **Economic consistency as the measured object.** [EcoAgent-Bench](../works/ecoagent-bench.md) prices every action under an explicit per-task budget across 304 tasks and pairs upgrade-oriented with save-oriented task groups, so a one-sided policy that always spends or always saves cannot score well. Tool-API agents reach at most 7.3% economic consistency, and a budget sweep moves GPT-5.4's escalation rate only from 0% to 3%.
- **Evaluation budget on harness optimization.** [HarnessOpt-Bench](../works/harnessopt-bench.md) gives optimizer LLMs a seed harness, evaluation feedback, and a fixed budget of target evaluations inside a TEE-audited loop, scoring normalized gain over the seed on a held-out partition; across 4 tasks, 5 optimizer models, and 111 scored runs, the optimizer model separates more than the coding harness it acts through.
- **Efficiency written into the rubric.** [MASSE](../works/masse.md) neither budgets the agent nor reports cost separately: its holistic system benchmark MASEB allots 20 of 100 points to Efficiency and Robustness, and the GPT-5 judge that grades a complete structural-engineering analysis log emits total token usage and total runtime in the same JSON object as the four scores, so an accurate but expensive pipeline cannot reach full marks. The paper's accompanying cost/runtime trade-off analysis across four backends then reads off the same measurements.
- **Resource saved, rather than resource spent.** [SkillAudit](../works/skillaudit.md) measures the resource *delta* an installed artifact produces: matched with-skill and no-skill runs on identical instructions and inputs yield an Efficiency Gain (relative saving in execution time) and a Cost Gain (relative saving in effective input tokens), each clipped to [-1, 1] and combined into an Efficiency-Cost Gain reported beside utility and safety in the same per-skill report. Nothing is budgeted; what is measured is whether adopting the skill pays for the context it occupies.
- **One currency for tokens and tool calls.** [BATS / Budget Tracker](../works/bats-budget-aware.md) formalizes `C_unified = c_token + Σ cᵢ·Pᵢ`, pricing tool invocations at a flat $0.001 alongside token cost, which is what allows cost-performance *scaling curves* to be drawn instead of accuracies compared at nominally equal tool budgets. Its finding is that raising a budget without telling the agent how much remains does not help: injecting used/remaining counts alone matches a ReAct baseline's accuracy at one-tenth its budget, for 31.3% lower cost.
- **Cost-performance frontier reporting.** Other work reports accuracy alongside token or dollar cost so that agents can be compared on a Pareto frontier rather than a single accuracy number. This is analysis-time resource-awareness rather than benchmark-time resource-awareness.

### A gap: budgets are given, not predicted

Every approach above supplies the budget as a *constraint the agent must respect* and then measures what it spent. Almost none asks the agent, or the harness, to estimate **in advance** what a proposed action will cost. Two carded works come closest and are worth distinguishing:

- [BAGEN](../works/bagen.md) makes the agent predict upper and lower bounds on its *remaining* budget each turn and flag infeasibility — prediction over the aggregate, scored per step.
- [AI Research Preference Models](../works/ai-research-preference-models.md) predicts which *candidate solutions* are worth executing before paying for them, but predicts relative worth rather than a resource quantity, and does so inside one search scaffold rather than as a reusable interface.

Neither yields what a planner would need to choose between plans: a per-action, task-conditioned distribution over tokens, wall-clock, GPU time, memory and dollars, with calibrated uncertainty. See the Open Questions below.

## Comparison

| Benchmark | Year | Resource currency | Resource role | Setting | Card |
|---|---|---|---|---|---|
| CostBench | 2025 | Configurable per-tool costs (atomic and composite) | First-class objective — plan for cost-optimality | Dynamic (blocking events); ~40% static→dynamic drop | [→](../works/costbench.md) |
| SimulCost | 2026 | Simulation time + experimental resources | First-class objective — parameter tuning under budget | Single-round and multi-round; 13 simulators | [→](../works/simulcost.md) |
| CATP-LLM / OpenCATP | 2024 | Normalized tool price (USD; execution time + memory) | Reported jointly with performance via Quality of Plan (QoP = α·perf − (1−α)·cost) | 111 tool-planning tasks / 11,100 samples | [→](../works/catp-llm.md) |
| MaD Physics | 2026 | Measurement cost (fidelity-priced observations) | Fixed per-trial budget the agent allocates | Simulated classical / fluid / quantum physics | [→](../works/mad-physics.md) |
| BAGEN | 2026 | Tokens; time / occupancy / cost | Prediction target + early-stop objective | Puzzle / retrieval / coding / supply-chain | [→](../works/bagen.md) |
| VeRO / VeRO-Bench | 2026 | Evaluation calls on the target agent (gated budget n_E ≤ B) | Enforced hard constraint — optimizer allocates expensive evaluations | Agent-harness optimization over 5 target-agent task suites | [→](../works/vero.md) |
| Frontier-Eng | 2026 | Simulator interactions (fixed per-task budget) | Hard bound on the propose-execute-evaluate loop | Real-world engineering optimization; 47 tasks, 5 categories | [→](../works/frontier-eng.md) |
| EcoAgent-Bench | 2026 | Priced actions under explicit per-task budgets | First-class objective — economic consistency across upgrade/save paired groups | 304 QA-derived tasks in 5 families; tool-API and workspace-CLI settings | [→](../works/ecoagent-bench.md) |
| HarnessOpt-Bench | 2026 | Target-evaluation calls (fixed budget, TEE-metered) | Enforced hard constraint on the optimize-evaluate loop | Harness optimization; 4 tasks × 5 optimizer LLMs, 111 scored runs | [→](../works/harnessopt-bench.md) |
| Gravity-Bench-v1 | 2025 | Observations of the simulated system (up to 100 per run, official project page) | Enforced budget on experimental design; full-access vs. budget gap reported | Gravitational-physics discovery over simulated binaries | [→](../works/gravity-bench.md) |
| SMDD-Bench | 2026 | Oracle calls (limited per-task budget) | Enforced hard constraint on design-space exploration | Small-molecule drug design; 502 solvable tasks, 102 targets | [→](../works/smdd-bench.md) |
| SDBench | 2025 | Cost of physician visits and diagnostic tests | Scored jointly with accuracy as a frontier | Sequential diagnosis over 304 NEJM-CPC cases with an information gatekeeper | [→](../works/sdbench.md) |
| ChemCost | 2026 | Supplier quotes and purchasable packs from a frozen pricing snapshot | Cost is the task itself — agents compute reaction cost against exact ground truth | Reaction pricing; 1,427 reactions, 230,775 quotes; noise-injected robustness views | [→](../works/chemcost.md) |
| MASSE | 2025 | Total token usage and total runtime, emitted by the judge alongside the quality scores | Scored component — Efficiency and Robustness carries 20 of the 100 MASEB points; the same totals drive a cost/runtime trade-off analysis across four backends | Multi-agent structural engineering workflow; 100 expert-validated problems, ten trials each | [→](../works/masse.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | Wall-clock runtime and peak memory per pipeline execution; token cost deliberately not measured and listed as a limitation | Reported measure, not a budget — runtime and memory sit beside the scientific outputs, and the speed-versus-auditability trade-off between the two agents is read off them | Two agentic coding systems executing one gravitational-wave pipeline specification on identical hardware; four autonomous runs | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SkillAudit | 2026 | Agent execution time and effective input tokens, measured as savings against a matched no-skill run (Efficiency Gain, Cost Gain, combined into ECG on [-1, 1]) | Reported measure, not a budget — the efficiency-cost gain is one of three per-skill report dimensions alongside utility (pass-rate gain) and a safety score | Auto-generated per-skill audits over 226 real-world skill packages spanning 23 occupational categories; 643 valid scenarios in the Codex / GPT-5.4 configuration | [→](../works/skillaudit.md) |
| Beyond Final Scores | 2026 | Wall-clock hours per task and USD inference cost per model | Budget bounds the run; cost is reported alongside the score rather than folded into it | Long-horizon AI R&D over 36 AutoLab tasks | [→](../works/beyond-final-scores.md) |
| R³-Bench | 2026 | Output tokens (tool-free) or counted tool actions (agentic), calibrated per model as ρ ∈ {0.2, 0.8} of its own unbudgeted baseline | Shared across a six-problem suite, making allocation itself the evaluated skill | Mathematics, competitive programming and abstract reasoning | [→](../works/r3-bench.md) |
| AI Research Preference Models | 2026 | H200 GPU-hours of candidate execution | The budget is fixed and the contribution is how it is ALLOCATED — a frozen-LM predictor picks which candidates are worth running | AI research agents searching over ML solutions (AIRA-dojo on AIRS-Bench) | [→](../works/ai-research-preference-models.md) |
| BATS / Budget Tracker | 2025 | Unified currency: token cost + tool invocations priced at a flat $0.001 each | Budget is a hard constraint made VISIBLE to the agent each turn; scaling curves are drawn in the unified currency | Web-search agents (BrowseComp, BrowseComp-ZH, HLE-Search), plus τ²-bench and SWE-bench Verified | [→](../works/bats-budget-aware.md) |

## Open Questions

- **Resource normalization across settings.** A dollar of API spend, a dollar of tool-call fee, and a second of wall-clock or simulation time do not compare cleanly. Which currency should be canonical for cross-benchmark comparison, and can any of them be canonical at all?
- **Static vs. dynamic robustness.** CostBench reports a substantial static-to-dynamic drop. Is such a gap a property of current models or of the specific perturbation distributions used? Should the field settle on standard perturbations?
- **Reporting vs. optimizing.** Benchmarks that make a resource first-class force the agent to plan under budget; benchmarks that only report resource use do not. Should the two classes be labeled distinctly so their numbers are not silently compared?
- **Token vs. tool-use cost.** Should aggregate leaderboards report only tokens (portable, model-comparable) or also tool-use resources (scientifically meaningful but domain-specific)?
- **Predicted cost versus spent cost.** Every work on this page budgets or measures resource use *after* an action is chosen. None exposes a per-action, task-conditioned prediction of what an action will cost before it runs — `C(action, task features) → distribution` over tokens, wall-clock, GPU time, peak memory and dollars, with an uncertainty estimate. This matters because agent workflows have high variance and conditional structure: a run that fails triggers a diagnose-and-retry chain, so expected cost is `C₀ + P(fail)·C_retry + …` rather than a sum over planned steps, and a planner choosing under a budget needs a tail quantile (p90) rather than a mean. Three questions follow. Is a cost predictor an *evaluation* instrument or an agent component — that is, does it belong on this axis at all? Should such a predictor be scored on its own calibration (predicted versus actual, per action class) rather than only on the downstream task score it enables? And should benchmarks report **prediction error** alongside consumption, so that an agent which stays under budget by luck is distinguishable from one that stays under budget by knowing what things cost?
- **Whose estimate counts.** Where a resource estimate is produced by the planner's own prose ("this should take about twenty minutes"), it is ungrounded and unscored. Separating the actor that proposes an action, the estimator that prices it, and the policy that admits or rejects it under budget would make each independently measurable — but no benchmark on this page currently evaluates those three roles apart.

## Related Works

- [CostBench](../works/costbench.md) — Cost-optimal planning under dynamic tool-use conditions.
- [SimulCost](../works/simulcost.md) — Cost-aware physics-simulation parameter tuning across 13 simulators.
- [CATP-LLM / OpenCATP](../works/catp-llm.md) — OpenCATP, a dataset for cost-aware tool planning (11,100 samples).
- [MaD Physics](../works/mad-physics.md) — Fidelity-priced measurement budgets in simulated physics; agents trade measurement quality against quantity to infer altered physical laws.
- [BAGEN](../works/bagen.md) — Progressive budget-interval prediction with trainable early-stopping across token and multi-resource agents.
- [VeRO / VeRO-Bench](../works/vero.md) — Benchmarking coding agents as agent optimizers under a gated evaluation-call budget.
- [Frontier-Eng](../works/frontier-eng.md) — Iterative engineering optimization under a fixed simulator-interaction budget.
- [EcoAgent-Bench](../works/ecoagent-bench.md) — Economic decision-making under priced actions and explicit budgets, scored for economic consistency.
- [HarnessOpt-Bench](../works/harnessopt-bench.md) — LLMs optimizing agent harnesses under a fixed, TEE-audited evaluation budget.
- [Gravity-Bench-v1](../works/gravity-bench.md) — Budgeted observation planning for gravitational-physics discovery.
- [SMDD-Bench](../works/smdd-bench.md) — Guaranteed-solvable drug design under a limited oracle-call budget.
- [SDBench](../works/sdbench.md) — Sequential diagnosis scored on the accuracy-versus-cost frontier.
- [ChemCost](../works/chemcost.md) — Reaction-cost computation as the measured task, with judge-free exact pricing ground truth.
- [MASSE](../works/masse.md) — Token usage and runtime scored as a rubric component of an end-to-end structural engineering workflow benchmark.
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) — Runtime and peak memory measured per autonomous pipeline run, making speed and footprint a comparison axis between two agents that produce the same science.
- [SkillAudit](../works/skillaudit.md) — Time and token savings measured against a matched no-skill run, reported per skill package alongside utility and safety.
- [Beyond Final Scores](../works/beyond-final-scores.md) — Per-task wall-clock budgets and per-model inference cost reported next to performance, spanning a roughly 20× cost spread across seven models.
- [R³-Bench](../works/r3-bench.md) — One budget shared across a six-problem suite, calibrated against each model's own demonstrated single-problem competence.
- [AI Research Preference Models](../works/ai-research-preference-models.md) — Matches the unguided agent's 24-hour score in ~15 hours on under two-thirds of its execution budget, with validation- and test-oracle ceilings reported alongside.
- [BATS / Budget Tracker](../works/bats-budget-aware.md) — Prices tokens and tool calls in one currency; injecting remaining budget alone matches a ReAct baseline's accuracy at one-tenth the budget.

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. Identifies cost-efficiency as an under-covered dimension in current agent evaluation. <https://arxiv.org/abs/2503.16416>

**Prior lineage for the predicted-cost question.** The Open Questions above restate, for tool-using LLM agents, a problem with a long history in AI. These references are recorded for orientation; none is an LLM-agent evaluation and none is carded.

- Russell, Wefald. *Principles of Metareasoning*. Artificial Intelligence 49(1–3):361–395, 1991 (earlier at KR 1989, 400–411). Treats deliberation itself as an action with a cost, and defines the value of computation as its expected improvement minus that cost — the formal ancestor of asking whether a tool call or an experiment is worth running. DOI 10.1016/0004-3702(91)90015-C
- Zilberstein. *Operational Rationality through Compilation of Anytime Algorithms*. AI Magazine 16(2):79–80, 1995. Summarizes the resource-bounded-reasoning line in which a component carries a **conditional performance profile** — its output quality as a function of input conditions and allotted time — which a runtime monitor then uses to allocate resources across a composed system. This is the closest classical term for a per-action, condition-dependent cost/quality profile. DOI 10.1609/aimag.v16i2.1136
- Klein, Falkner, Bartels, Hennig, Hutter. *Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets* (FABOLAS). arXiv 1605.07079, 2016; AISTATS 2017. Learns an explicit cost model alongside the objective and selects the next evaluation by information gain per unit predicted cost — the same predict-then-choose structure, in hyperparameter optimization. <https://arxiv.org/abs/1605.07079>
- Lee, Perrone, Archambeau, Seeger. *Cost-aware Bayesian Optimization*. arXiv 2003.10870, 2020. Cost-aware acquisition under a fixed budget where evaluation costs vary and are themselves modeled. <https://arxiv.org/abs/2003.10870>

The constrained formulation ("maximize task quality subject to expected GPU-hours ≤ B₁ and dollars ≤ B₂") is standard as a **constrained Markov decision process**; where the remaining budget is carried explicitly in the state it is often called a budgeted MDP.

**Budget-aware agent methods (not carded — methods, not evaluations).** Adjacent recent work that conditions agent behaviour on a budget without contributing an evaluation instrument:

- Li, Deng, Li, Li. *Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents* (BAVT). arXiv 2603.12634, 2026. Budget-conditioned node selection that shifts from exploratory to greedy as resources deplete, with a residual value predictor for step-level progress. <https://arxiv.org/abs/2603.12634>
- Yang, Luo, Liu, Lou, Chen. *BAMAS: Structuring Budget-Aware Multi-Agent Systems*. arXiv 2511.21572, 2025. Integer-linear-programming selection among LLMs of differing cost, then a learned collaboration topology; reports comparable performance at up to 86% lower cost. <https://arxiv.org/abs/2511.21572>
