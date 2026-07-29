# Trajectory Evaluation

## Definition

Trajectory evaluation refers to evaluation methods that score an agent based on the sequence of actions and intermediate states it produces, not only its final answer. Metrics may include per-step correctness, subgoal completion, per-capability subprocess scoring, reasoning quality, evidence grounding, or process efficiency.

## Motivation

End-task success is a coarse signal. Two agents that both fail — or both succeed — can differ meaningfully in *how* they got there. Trajectory-level metrics surface those differences and enable diagnosis of *where* a capability breaks down.

Trajectory evaluation is also load-bearing for longer-horizon settings, where a single terminal reward provides too little signal to identify which step went wrong.

## Existing Approaches

Trajectory-evaluation contributions cluster into six design lines. The first four are task-suite benchmarks; the fifth is a diagnostic-framework line that overlays existing benchmarks; the sixth targets the reference-trajectory generation problem itself.

- **Subgoal-based.** Trajectories are annotated with a chain of subgoals; the primary metric is the fraction completed. [AgentBoard](../works/agentboard.md) is the exemplar, pairing subgoal progress rate with an analytical dashboard.
- **Graded-subtask / dense-reward.** Tasks are decomposed into subtasks that receive graded (not binary) rewards, aggregated under configurable thresholds. [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) follows this line for long-horizon terminal tasks.
- **Capability-decomposed.** A complex capability is decomposed into a small number of subprocesses, each scored on isolated tasks. [T-Eval](../works/t-eval.md) applies this to tool use across six subprocesses; [Enconda-bench](../works/enconda-bench.md) applies it to environment configuration across planning / diagnosis / repair / execution.
- **Utility-function based.** A joint metric over multiple quality dimensions is applied to whole trajectories. [TRACE](../works/trace.md) uses a hierarchical utility over accuracy, efficiency, evidence grounding, and reasoning quality for deep-research agents; [FinTrace](../works/fintrace.md) uses nine metrics across four dimensions for financial tool use.
- **Diagnostic overlay.** Frameworks that are not themselves task suites, but layer diagnostic vocabularies and audit protocols on top of existing benchmarks. [AgentAtlas](../works/agentatlas.md) provides a six-way control-decision taxonomy and failure taxonomy applied across 15 agent benchmarks; [Insights Generator](../works/insights-generator.md) is a multi-agent system for corpus-level trace diagnostics.
- **Deterministic ground-truth generation.** Trajectory evaluation depends on high-quality reference trajectories. [Traxgen](../works/traxgen.md) tackles the reference-generation problem directly by compiling structured workflow specifications and user data into deterministic DAG-based gold trajectories, replacing LLM-driven ground-truth generation with a reproducible, orders-of-magnitude-faster alternative.
- **Human-labeled step-level effectiveness.** [AgentProcessBench](../works/agentprocessbench.md) labels 8,509 assistant steps across 1,000 multi-turn tool-use trajectories with a ternary +1 / 0 / −1 scheme at 89.1% inter-annotator agreement.
- **Verification-paired trajectory reviews.** [AgentLens](../works/agentlens.md) averages five LLM-judge dimensions with formal verification into one quality index and attaches a written, evidence-linked review to every score, so a run that passes objective checks via brittle shortcuts is separated from one that is genuinely clean.
- **Span-level error localization.** [TELBench](../works/telbench.md) segments 1,000 verified deep-research trajectories (avg. 11.95 spans) into error / non-error spans and asks a model to find the earliest harmful commitment, where its DRIFT auditing framework lifts overall macro-F1 as high as 54.91.
- **Formal-logic step adjudication.** [MATP](../works/matp.md) autoformalizes each natural-language reasoning step to First-Order Logic and lets an automated theorem prover rule on it, reaching 94.26% macro F1 for step correctness on PrOntoQA-OOD against 47.79% for a GPT-4o prompting baseline.
- **Solver-derived reference chains.** [VCoT-Bench](../works/vcot-bench.md) lifts Z3 proofs into human-readable Verus steps and scores models on completing deliberately removed blocks, so trajectory credit is measured against the reasoning the prover required rather than a binary verification outcome.
- **Gated artifact correctness.** [SysMoBench](../works/sysmobench.md) scores AI-generated TLA+ models of eleven real system artifacts on four automatically checked metrics — syntax, runtime, trace conformance, and invariant correctness — each gating the next, and rejects LLM-as-a-judge scoring outright.
- **Module-level proof checking.** [Pseudo-Formalization](../works/pseudo-formalization.md) verifies each premise–conclusion module of a rewritten proof independently, scoring error localization over 35 arXiv papers with 40 disclosed errors.
- **Pairwise trajectory preference.** [Plan-RewardBench](../works/plan-rewardbench.md) pits a chosen trajectory against a confusable hard negative across 1,171 pairs, scoring the judge rather than the agent.
- **Judge-against-expert agreement.** [AgentRewardBench](../works/agentrewardbench.md) scores 12 LLM judges and the benchmarks' own rule-based evaluators against expert labels on 1,302 web agent trajectories, finding no judge above 70% precision.
- **Harness-effect diagnostics.** [Harness-Bench](../works/harness-bench.md) fixes tasks, sandboxes, budgets, and evaluators while varying the harness around each model backend, scoring 5,194 trajectories with a security-gated product of completion and a trace-derived process score (robustness, tool use, consistency); a 23.8-point gap between the best and worst configurable harness on identical tasks and models supports reporting capability per model–harness configuration.

## Comparison

| Work | Year | Trajectory metric | Domain | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | Progress rate over annotated subgoals | Embodied / game / web / tool | [→](../works/agentboard.md) |
| T-Eval | 2023 | Per-subprocess scoring across 6 tool-use capabilities | Tool use | [→](../works/t-eval.md) |
| Long-Horizon-Terminal-Bench | 2026 | Graded subtasks; threshold-aggregated partial reward | Terminal long-horizon | [→](../works/long-horizon-terminal-bench.md) |
| Enconda-bench | 2025 | Process-level scoring across 4 configuration subprocesses | Software env. configuration | [→](../works/enconda-bench.md) |
| TRACE | 2026 | Hierarchical trajectory utility + scaffolded-capability assessment | Deep research | [→](../works/trace.md) |
| FinTrace | 2026 | 9 metrics across 4 dimensions (action, efficiency, process, output) | Finance | [→](../works/fintrace.md) |
| AgentAtlas | 2026 | 6-way control-decision taxonomy + failure taxonomy (audit over 15 benchmarks) | Cross-benchmark overlay | [→](../works/agentatlas.md) |
| Insights Generator | 2026 | Automated corpus-level trace diagnostics (multi-agent hypothesis testing) | Trace-corpus analysis | [→](../works/insights-generator.md) |
| Traxgen | 2025 | Deterministic DAG-based ground-truth trajectory generation (100% alignment with gold; >17,000× median speedup vs. LLM-based generation) | Customer-service tool use (companion benchmark) | [→](../works/traxgen.md) |
| AgentProcessBench | 2026 | Step effectiveness (StepAcc / FirstErrAcc) | Tool use (web / CLI / APIs) | [→](../works/agentprocessbench.md) |
| AgentLens | 2026 | Quality index over 5 LLM-judge dimensions + formal verification; pairwise side-by-side reviews | Interactive coding (Java) | [→](../works/agentlens.md) |
| TELBench | 2026 | Span-level F1 + first-error accuracy | Deep-research agent trajectories (GAIA, XBench, BrowseComp) | [→](../works/telbench.md) |
| MATP | 2025 | Per-step provable / refutable / indeterminate verdict, plus six-way chain classification | Deductive logical reasoning | [→](../works/matp.md) |
| VCoT-Bench | 2026 | Weighted syntactic + semantic block-completion accuracy | Rust verification in Verus | [→](../works/vcot-bench.md) |
| SysMoBench | 2025 | Four gated partial-credit metrics (syntax → runtime → trace conformance → invariant), no LLM judge | Formal modeling of concurrent / distributed systems | [→](../works/sysmobench.md) |
| Pseudo-Formalization | 2026 | Error-location precision + recall; per-proof coverage and false errors | Mathematical proof verification | [→](../works/pseudo-formalization.md) |
| Plan-RewardBench | 2026 | Pairwise accuracy on chosen / rejected trajectory pairs | Tool-integrated agent planning | [→](../works/plan-rewardbench.md) |
| AgentRewardBench | 2025 | Judge precision against expert success labels | Web agents | [→](../works/agentrewardbench.md) |
| Harness-Bench | 2026 | Security-gated Completion × Process (robustness / tool use / consistency from traces) | Cross-harness executable agent workflows (8 categories) | [→](../works/harness-bench.md) |

## Open Questions

- **Annotator dependence of subgoal metrics.** Progress-rate scores depend on the annotator's decomposition of the task. Agents that solve tasks via alternative decompositions can be penalized without behaving worse. How stable are subgoal-based metrics across annotator choices?
- **Reliability of automated trajectory judgment.** Utility-function metrics rely on evaluators — models or humans — rating reasoning quality and evidence grounding. How does the reliability of LLM-judge trajectory scoring compare against human raters, and how does it scale?
- **Composing decomposed scores.** Both subgoal-based and capability-decomposed approaches produce per-piece scores. What is the right way to combine per-piece scores into a single trajectory score without losing the diagnostic signal that motivated decomposition?
- **Convergence across design lines.** Subgoal-based, graded-subtask, capability-decomposed, utility-function, and diagnostic-overlay approaches all produce non-Pass@1 trajectory signals. Do they rank models consistently on shared tasks?
- **Overlay frameworks vs. task suites.** AgentAtlas and Insights Generator do not add tasks; they interpret existing benchmarks. Should the field standardize on such overlays so that trajectory-level signal is comparable across otherwise incomparable benchmarks?
- **Deterministic vs. LLM-generated ground truth.** Traxgen demonstrates that deterministic ground-truth generation from structured workflow specs is orders of magnitude faster than LLM-based generation while achieving 100% alignment with human-validated references. Does this shift the appropriate baseline for future trajectory-evaluation work away from LLM-authored gold trajectories?

## Related Works

- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [Enconda-bench](../works/enconda-bench.md)
- [TRACE](../works/trace.md)
- [FinTrace](../works/fintrace.md)
- [AgentAtlas](../works/agentatlas.md)
- [Insights Generator](../works/insights-generator.md)
- [Traxgen](../works/traxgen.md)
- [AgentProcessBench](../works/agentprocessbench.md)
- [AgentLens](../works/agentlens.md)
- [TELBench](../works/telbench.md)
- [MATP](../works/matp.md)
- [VCoT-Bench](../works/vcot-bench.md)
- [SysMoBench](../works/sysmobench.md)
- [Pseudo-Formalization](../works/pseudo-formalization.md)
- [Plan-RewardBench](../works/plan-rewardbench.md)
- [AgentRewardBench](../works/agentrewardbench.md)
- [Harness-Bench](../works/harness-bench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
