# Trajectory Evaluation

> **English** | [简体中文](../zh/topics/trajectory_evaluation.md) · [← All topics](./README.md)

## Start Here

Two agents can reach the same answer by very different routes. One uses relevant evidence and verifies the result; another makes several unsupported guesses and gets lucky. Final-answer scoring treats them as equal.

Trajectory evaluation keeps the route. For a five-step tool task, an evaluator can mark the first invalid call, whether each subgoal completed, how much evidence supported the conclusion, and how many retries were wasted. That makes failure easier to locate. It also adds cost and judge dependence: a detailed trace is useful only if the evaluator can score it reliably.

## Definition

Trajectory evaluation refers to evaluation methods that score an agent based on the sequence of actions and intermediate states it produces, not only its final answer. Metrics may include per-step correctness, subgoal completion, per-capability subprocess scoring, reasoning quality, evidence grounding, or process efficiency.

## Motivation

End-task success is a coarse signal. Two agents that both fail — or both succeed — can differ meaningfully in *how* they got there. Trajectory-level metrics surface those differences and enable diagnosis of *where* a capability breaks down.

Trajectory evaluation is also load-bearing for longer-horizon settings, where a single terminal reward provides too little signal to identify which step went wrong.

## Existing Approaches

Trajectory-evaluation contributions cluster into six design lines. The first four are task-suite benchmarks; the fifth is a diagnostic-framework line that overlays existing benchmarks; the sixth targets the reference-trajectory generation problem itself.

- **Subgoal-based.** Trajectories are annotated with a chain of subgoals; the primary metric is the fraction completed. [AgentBoard](../works/agentboard.md) is the exemplar, pairing subgoal progress rate with an analytical dashboard.
- **Graded-subtask / dense-reward.** Tasks are decomposed into subtasks that receive graded (not binary) rewards, aggregated under configurable thresholds. [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) follows this line for long-horizon terminal tasks.
- **Capability-decomposed.** A complex capability is decomposed into a small number of subprocesses, each scored on isolated tasks. [T-Eval](../works/t-eval.md) applies this to tool use across six subprocesses; [Enconda-bench](../works/enconda-bench.md) applies it to environment configuration across planning / diagnosis / repair / execution; [PEOA](../works/peoa.md) applies it to chemical and process engineering, scoring the four stages of tool learning — task planning against gold plans, tool selection by Recall@K / NDCG@K / COMP@K against a ground-truth tool set, tool calling by stipulation consistency, parameter-extraction correctness, and error handling, and response generation by BLEU / ROUGE-L / exact match.
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
- **In-the-wild trajectories with commit-grounded outcomes.** [SWE-chat](../works/swe-chat.md) replaces curated tasks with ~6,000 real coding-agent sessions logged from opted-in open-source developers, attributing every committed line to human or agent. Its trajectory metrics are grounded in what users actually keep — only 44.3% of agent-produced code ends up in user commits — complemented by LLM-annotated session success (0–100) and per-turn pushback labels validated against human gold labels.
- **Skill-aware trajectory verification.** [SkillTV-Bench](../works/skilltv-bench.md) benchmarks LLM-as-a-Judge and Agent-as-a-Judge methods on 681 real trajectories from skill-augmented executions — a setting where the judge needs task-aware skill knowledge to verify correctly. Its SkillTV-Evolve loop distills misjudged cases into a reusable JudgeSkill that raises the same judge's accuracy by 14.8 percentage points and lifts best-of-ten trajectory selection from 22.9% to 45.5%.
- **Localize-attribute-repair auditing of failed search runs.** [SearchAuditor](../works/searchauditor.md) turns failure analysis into a benchmarked task over SearchAuditBench's 1,243 expert-annotated failed deep-search trajectories (averaging 65.1K tokens), grading critical-step localization, search-specific root-cause attribution, and rubric-graded repair end to end.
- **Error-lifecycle tracing.** [TRAJDEBUG](../works/trajdebug.md) separates errors an agent later recovers from errors that actually determine failure, via multi-granularity history compression, evidence-based error identification, and resolution-status tracing, anchored by TrajErrBench's 486 manually annotated failed trajectories from Tau2Bench and SWE-Bench Pro.
- **Execution-trace semantic evaluation.** [EnvTrace](../works/envtrace.md) scores LLM-generated instrument-control code by executing it against a synchrotron-beamline digital twin and aligning execution traces into a multi-faceted functional-correctness score — trajectory comparison standing in for unit tests where correctness is physical behavior over time; 30+ LLMs evaluated.
- **Modular embodied error analysis.** [Embodied Agent Interface](../works/embodied-agent-interface.md) breaks embodied-LLM failures into hallucination, affordance, and planning errors per decision module, checked against simulator state.
- **Robot failure explanation.** [REFLECT / RoboFail](../works/robofail.md) has an LLM reason over hierarchical multisensory experience summaries to explain manipulation failures and guide correction planning.
- **Failure detection at scale.** [AHA](../works/aha.md) fine-tunes a VLM on procedurally generated failure trajectories (FailGen) to detect and explain manipulation failures, beating GPT-4o in-context learning by 10.3%.
- **Categorized failure QA.** [RoboFAC](../works/robofac.md) provides 78,623 QA pairs over 9,440 erroneous trajectories across eight failure-understanding dimensions, with a specialist model used as a real-pipeline supervisor.
- **Lab-robot failure analysis.** [LabRobFail](../works/labrobfail.md) injects control-, physics-, and semantic-level failures into simulated chemical self-driving-lab executions and scores six diagnostic capabilities.
- **Counterfactual routing evaluation.** [The Replay Gap](../works/the-replay-gap.md) shows that scoring per-step model switching by replaying logged trajectories measures a world that never runs, and replaces it with branching counterfactual rollouts and matched same-model control forks.
- **Telemetry sufficiency for fault localization.** [TelemetrySuffBench](../works/telemetrysuffbench.md) separates failure detection from fault-origin localization over synthetic multi-component traces with delayed-binding faults, exposing a detection–localization gap under ablated telemetry.
- **Component-level trajectory attribution.** [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md) introduces primary-component attribution and attribution-chain recovery over 1,351 annotated agent trajectories under a unified component schema.
- **Plan compliance.** [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md) measures how faithfully SWE-agent trajectories follow an instructed plan across 16,991 runs, decomposing compliance into phase coverage, ordering, and per-phase fidelity.
- **Counterfactual causal attribution over traces.** [TempoBench](../works/tempobench.md) separates forward simulation from minimal-necessary-cause identification on formally verifiable Mealy-machine execution traces, quantifying the SIM/MIN gap.
- **Reasoning-aligned code evaluation.** [RACE-Bench](../works/race-bench.md) pairs executable patch verification with structured reference reasoning, scoring how well a repository-level code agent's intermediate reasoning aligns with developer-accepted trajectories.
- **Stage-aligned issue-resolution diagnosis.** [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md) augments executable patch evaluation with validated ground truths for requirement clarification and implementation planning, enabling GT-aligned diagnosis of full coding trajectories.
- **Reasoning-trajectory reliability.** [MiraMind](../works/miramind.md) scores mental-health reasoning trajectories along usability, logical structure, and informational contribution, separating a correct final answer from an unreliable evidence-to-judgment path.
- **Adversarially measured per-action admissibility.** [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md) makes the individual proposed action, not the end task, the unit of judgement: each LLM-proposed control action is checked by graph traversal over the plant's P&ID for tag existence, actuatability, fail-state consistency, and downstream impact. Coverage of that checker is itself measured — 43 crafted invalid proposals over its failure modes, on which 100% recall is reported for the covered categories, plus an N = 50 robustness study spanning runs where 10%–70% of proposals are unsafe and a B0–B3 ladder that credits each context-enrichment stage separately.
- **The trajectory read for what it says about a skill.** Where the agent is augmented with a reusable skill, the trajectory becomes the only place the skill's effect is visible, and a cluster of works instruments it accordingly. [SkillJuror](../works/skilljuror.md) counts distinct skill resources touched and effective uptake events per trajectory and finds that organization moves those before it moves outcomes. [Skill Coverage](../works/skill-coverage.md) transplants test adequacy: skill instructions are compiled into conditionally scoped behavior constraints, and each trajectory is scored for which constraints it covered and whether the observed behavior passed. [SkillCoach](../works/skillcoach.md) derives its rubrics from real rollouts under a validation gate and scores selection, following, composition and reflection separately, deliberately leaving the external verifier outside the rubric so process and outcome can disagree. [SkillLearnBench](../works/skilllearnbench.md) adds a third level beneath both, scoring the generated skill artifact alongside the trajectory that produced it.
- **Lifecycle gates instead of one terminal verdict.** [SkillMisevo-Bench](../works/skillmisevo-bench.md) measures authoring, retrieval and execution as separate gates over the trajectory-to-skill pipeline, because a terminal attack-success number cannot distinguish a safe library from an unsafe artifact that was simply never retrieved; across its grid all 21 evolved conditions author unsafe artifacts, 19 retrieve them, and only 15 retain harm into a fresh session.
- **Process discipline as a scored dimension of engineering work.** [RigorBench](../works/rigorbench.md) computes seven weighted pillars — planning fidelity, verification coverage, recovery efficiency, abstention quality, atomic transition integrity, test assertion density, exploration efficiency — from the instrumented execution trajectory, and scores outcome separately on the same runs so the process-outcome relationship is an object of study; it holds the foundation model fixed and varies the harness.
- **Gold plans annotated per instance.** [AISE-Bench](../works/aise-bench.md) annotates every one of its 1,133 instances end to end — query, plan, executed API calls with validated parameters, referenced answer — so process metrics have gold references rather than heuristics: planning is scored as graph edit distance against the annotated plan, and parameter accuracy is reported as a first-class metric, which is where most evaluated methods lose ground despite high partial completion.
- **Reference operation chains where the artifact resists inspection.** [DrafterBench](../works/drafterbench.md) scores civil-engineering drawing revision by intersection-over-union between the agent's recorded operation chain and a reference chain, using dual functions that log the operation path without modifying files — so a revised PDF never has to be inspected visually. Instruction quality is a controlled variable over its 1,920 tasks: unstructured phrasing, vague values and incomplete information are toggled independently, and results are reported per controller, making a trajectory-score drop attributable to a specific instruction defect.

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
| SWE-chat | 2026 | Code survival / efficiency / cost per committed line + LLM-annotated session success and per-turn pushback, over real user trajectories | In-the-wild coding-agent sessions (open-source repositories) | [→](../works/swe-chat.md) |
| SkillTV-Bench | 2026 | Judge accuracy on skill-augmented executions + rollout-pool selection success | Skill-augmented agent execution (11 domains) | [→](../works/skilltv-bench.md) |
| SearchAuditor | 2026 | End-to-end pass on critical-step localization, root-cause attribution, and rubric-graded repair | Long-horizon deep-search trajectories | [→](../works/searchauditor.md) |
| TRAJDEBUG | 2026 | Error identification + critical attribution via resolution status and terminal impact | Tool-use and coding failed trajectories | [→](../works/trajdebug.md) |
| EnvTrace | 2025 | Execution-trace alignment against a digital twin; multi-faceted functional-correctness score | Instrument-control code (synchrotron beamlines) | [→](../works/envtrace.md) |
| Embodied Agent Interface | 2024 | Typed error taxonomy (hallucination / affordance / planning) per decision module | Embodied task planning (VirtualHome, BEHAVIOR) | [→](../works/embodied-agent-interface.md) |
| REFLECT / RoboFail | 2023 | LLM failure explanation from multisensory summaries; correction-planning success | Robot manipulation failure analysis | [→](../works/robofail.md) |
| AHA | 2024 | Free-form failure detection/reasoning; fuzzy-match, ROUGE-L, binary success | Robotic-manipulation failures (sim-generated + real) | [→](../works/aha.md) |
| RoboFAC | 2025 | Eight-dimension failure QA; failure-analysis accuracy | Robot-manipulation failure analysis and correction | [→](../works/robofac.md) |
| LabRobFail | 2026 | Six capabilities incl. temporal localization and severity assessment | Chemical self-driving-lab robot failures (simulation) | [→](../works/labrobfail.md) |
| The Replay Gap | 2026 | Branching-rollout divergence (normalized edit distance, action-rewrite fraction) vs. matched same-model control forks; replay-evaluator audit | Agentic model routing (SWE-bench substrate) | [→](../works/the-replay-gap.md) |
| TelemetrySuffBench | 2026 | Origin-step Top-1 localization vs. detection F1 under telemetry masks; abstention (FAR / UAR) | Agent telemetry / trace diagnosis (synthetic) | [→](../works/telemetrysuffbench.md) |
| Long-Horizon Agent Trajectory Attribution | 2026 | Primary-component localization (Hit@1, MRR) + attribution-chain recovery (Recall@K, MAP) | LLM-agent tool-use / safety trajectories | [→](../works/long-horizon-agent-trajectory-attribution.md) |
| Evaluating Plan Compliance (From Plan to Action) | 2026 | Plan Phase Compliance / Order Compliance / Phase Fidelity (geometric mean) over 16,991 trajectories | Programming agents (SWE-bench) | [→](../works/from-plan-to-action.md) |
| TempoBench | 2025 | SIM/MIN separation: forward-simulation step accuracy vs. minimal-necessary-cause identification | Execution-trace causal reasoning (Mealy machines) | [→](../works/tempobench.md) |
| RACE-Bench | 2026 | Dual-track: patch resolved rate + reasoning-alignment recall / over-prediction vs. developer reference trajectories | Repository-level code agents (feature addition) | [→](../works/race-bench.md) |
| SWE-RPG | 2026 | Resolved rate + GT-aligned stage failure attribution and per-stage clarification / planning coverage | Repository-level issue resolution (Python / Java) | [→](../works/a-unified-issue-resolution-benchmark-for-requireme.md) |
| MiraMind | 2025 | Reasoning-trajectory scoring on usability, logical structure, informational contribution (alongside outcome metrics) | Mental-health reasoning | [→](../works/miramind.md) |
| PEOA | 2024 | Stage-decomposed tool-learning scoring: planning (tool-usage awareness, pass rate, plan accuracy vs. gold plans), tool selection (Recall@K, NDCG@K, COMP@K), tool calling (stipulation consistency, parameter extraction, error handling), response generation (BLEU, ROUGE-L, EM) | Chemical and process engineering problem solving (MathComp, ChemProc) | [→](../works/peoa.md) |
| Autonomous Action Execution (AAE) Framework | 2026 | Per-proposed-action validation by P&ID graph traversal (tag existence, actuatability, fail-state, downstream impact); validator recall over 43 injected invalid proposals, N = 50 robustness runs, B0–B3 context ladder | Industrial process control (Tennessee Eastman and two further plant scenarios) | [→](../works/aae-framework.md) |
| DrafterBench | 2025 | Intersection-over-union between the recorded operation chain and a reference chain, layered on two-level scoring (code executability, then target completeness over six subtasks) with a weak-subtask penalty; reported per instruction controller | Civil-engineering technical drawing revision over 46 custom tools | [→](../works/drafterbench.md) |
| AstroVisBench | 2025 | Stage-separated scoring of one workflow: Variable Inspection Score over the ground-truth in-memory variables the processing stage produces, then a No / Minor / Major error verdict on the resulting plot from a judge chosen by correlation (ρ = 0.822) with five professional astronomers, with crash and VisFail rates reported apart from both | Astronomy scientific computing and visualization from tutorial notebooks | [→](../works/astrovisbench.md) |
| Spec-o3 / SpecVI-Bench | 2026 | Six astronomers score 100 reasoning trajectories on a published 0–5 rubric for coherence and physical consistency, separately from label accuracy, plus a pairwise-preference comparison against o3 on 50 cases per survey; tool calls per trajectory capped at 8 | Astronomical spectroscopic vetting of rare objects (LAMOST, SDSS/DESI) | [→](../works/spec-o3.md) |
| Plausible but Wrong | 2026 | Four mutually exclusive failure modes defined by thresholds on Execution Success, Parameter Accuracy and Numerical Accuracy — code failure, wrong parameters, wrong computation, correct — so that a silent numerical error is classified apart from a crash rather than collapsed into one pass/fail | Astrophysical computation workflows (CAMB solver calls and archival-data analysis) | [→](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md) |
| First head-to-head comparison of agentic AI on Einstein Telescope data | 2026 | Process behaviour counted from the agents' own logs — restarts, silent deviations from the specification versus explicit self-corrections, unsolicited optimisations, token-budget changes and instruction-interpretation divergences — reported beside identical scientific outputs, runtime and peak memory | Gravitational-wave pipeline execution on simulated Einstein Telescope data | [→](../works/first-head-to-head-comparison-of-agentic-ai-applie.md) |
| SkillJuror | 2026 | Distinct skill resources touched and effective uptake events per trajectory (1.18 → 3.85 and 1.33 → 3.92 under Progressive Disclosure), with verifier-passing trials as a lagging secondary signal | Agent-skill organization, over an 82-task SkillsBench study in 410 matched trials | [→](../works/skilljuror.md) |
| Skill Coverage | 2026 | Coverage of extracted skill behavior constraints per trajectory, plus Pass / Fail verdicts on the covered ones | Reusable agent skills, applied to SkillsBench leaderboard trajectories | [→](../works/skill-coverage.md) |
| SkillCoach | 2026 | Self-evolving skill-grounded rubrics over four dimensions — skill selection (F1 against the gold skill set), skill following, composition against precedence dependencies, and skill-grounded reflection — scored apart from the external verifier | Agent skill-use over 28 task families filtered from SkillsBench and SkillLearnBench | [→](../works/skillcoach.md) |
| SkillLearnBench | 2026 | Three levels: task pass rate, generated-skill quality (functional coverage, executability, safety), and trajectory quality (key-point recall, execution order, completeness) | Continual skill learning over 20 skill-dependent tasks in 15 sub-domains (100 verified instances) | [→](../works/skilllearnbench.md) |
| SkillMisevo-Bench | 2026 | Nine lifecycle-gated metrics separating online behavior, evolved-artifact unsafety (content unsafety, unsafe generalization, stealthiness), and post-reset unsafe retrieval and carryover | Persistent skill libraries under sandboxed agentic operations; four agent frameworks × six evolution methods | [→](../works/skillmisevo-bench.md) |
| RigorBench | 2026 | Seven process-discipline pillars computed from the instrumented trajectory and combined into a weighted RigorScore, with outcome scored separately on the same runs | AI coding agents over 100 tasks in five categories, foundation model held fixed across harnesses | [→](../works/rigorbench.md) |
| AISE-Bench | 2026 | Planning graph edit distance against the annotated plan, parameter accuracy, and execution success rate, reported apart from answer correctness / completeness / faithfulness / F1-LM | Academic information seeking over scholarly knowledge-graph APIs (AMiner, Google Scholar) | [→](../works/aise-bench.md) |
| Replica | 2026 | Five-dimension rubric over the rollout — visual match, scientific claim support, experimental implementation, compute-budget use and scientific integrity — with judge self-consistency reported (τ = 0.66) alongside human agreement (τ = 0.19) | AI & ML research | [→](../works/replica.md) |
| AutoResearchEval | 2026 | 45 failure patterns on two orthogonal axes (six lifecycle stages plus a cross-stage layer × four root-cause pillars), annotated over 800 complete trajectories for 12,712 total hits | Multi-domain science | [→](../works/autoresearcheval.md) |
| Beyond Final Scores | 2026 | Three deterministic rule-based families — Solution Framing, Execution, Feedback Control — computed from verifier outcomes and recorded execution signals rather than from any judge | AI & ML research | [→](../works/beyond-final-scores.md) |
| Apodex Discovery | 2026 | Six process dimensions (Tools, Repair, Alternatives, Coherence, Evidence, Scope) scored blind to outcome and with solver identity withheld, plus a load-bearing-step method that re-solves critical steps in isolation | Discovery across ten industrial and scientific areas | [→](../works/apodex-discovery.md) |
| Agents Catching Agents | 2026 | Transcript-reading judge against a referee that privately re-queries the agent; only the interventional referee transfers across modalities (77–88% precision at 13–21% false-positive rate) | Medicine & health | [→](../works/agents-catching-agents.md) |

## Open Questions

- **Annotator dependence of subgoal metrics.** Progress-rate scores depend on the annotator's decomposition of the task. Agents that solve tasks via alternative decompositions can be penalized without behaving worse. How stable are subgoal-based metrics across annotator choices?
- **Reliability of automated trajectory judgment.** Utility-function metrics rely on evaluators — models or humans — rating reasoning quality and evidence grounding. How does the reliability of LLM-judge trajectory scoring compare against human raters, and how does it scale?
- **Composing decomposed scores.** Both subgoal-based and capability-decomposed approaches produce per-piece scores. What is the right way to combine per-piece scores into a single trajectory score without losing the diagnostic signal that motivated decomposition?
- **Convergence across design lines.** Subgoal-based, graded-subtask, capability-decomposed, utility-function, and diagnostic-overlay approaches all produce non-Pass@1 trajectory signals. Do they rank models consistently on shared tasks?
- **Overlay frameworks vs. task suites.** AgentAtlas and Insights Generator do not add tasks; they interpret existing benchmarks. Should the field standardize on such overlays so that trajectory-level signal is comparable across otherwise incomparable benchmarks?
- **Deterministic vs. LLM-generated ground truth.** Traxgen demonstrates that deterministic ground-truth generation from structured workflow specs is orders of magnitude faster than LLM-based generation while achieving 100% alignment with human-validated references. Does this shift the appropriate baseline for future trajectory-evaluation work away from LLM-authored gold trajectories?

## Related Works

- [MobileJudgeBench](../works/mobilejudgebench.md)
- [SkillJuror](../works/skilljuror.md)
- [Skill Coverage](../works/skill-coverage.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [RigorBench](../works/rigorbench.md)
- [AISE-Bench](../works/aise-bench.md)
- [AstroVisBench](../works/astrovisbench.md)
- [Spec-o3](../works/spec-o3.md)
- [Plausible but Wrong: A Case Study on Agentic Failures in Astrophysical Workflows](../works/plausible-but-wrong-a-case-study-on-agentic-failur.md)
- [First head-to-head comparison of agentic AI applied to the analysis of simulated data of the Einstein Telescope](../works/first-head-to-head-comparison-of-agentic-ai-applie.md)
- [DrafterBench](../works/drafterbench.md)
- [PEOA](../works/peoa.md)
- [Autonomous Action Execution (AAE) Framework](../works/aae-framework.md)
- [TempoBench](../works/tempobench.md)
- [TelemetrySuffBench](../works/telemetrysuffbench.md)
- [Evaluating Plan Compliance in Autonomous Programming Agents](../works/from-plan-to-action.md)
- [Long-Horizon Agent Trajectory Attribution](../works/long-horizon-agent-trajectory-attribution.md)
- [MiraMind](../works/miramind.md)
- [SWE-RPG](../works/a-unified-issue-resolution-benchmark-for-requireme.md)
- [RACE-Bench](../works/race-bench.md)
- [The Replay Gap](../works/the-replay-gap.md)
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
- [SWE-chat](../works/swe-chat.md)
- [SkillTV-Bench](../works/skilltv-bench.md)
- [SearchAuditor](../works/searchauditor.md)
- [TRAJDEBUG](../works/trajdebug.md)
- [EnvTrace](../works/envtrace.md)
- [Embodied Agent Interface](../works/embodied-agent-interface.md)
- [REFLECT / RoboFail](../works/robofail.md)
- [AHA](../works/aha.md)
- [RoboFAC](../works/robofac.md)
- [LabRobFail](../works/labrobfail.md)
- [Replica](../works/replica.md)
- [AutoResearchEval](../works/autoresearcheval.md)
- [Beyond Final Scores](../works/beyond-final-scores.md)
- [Apodex Discovery](../works/apodex-discovery.md)
- [Agents Catching Agents](../works/agents-catching-agents.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
