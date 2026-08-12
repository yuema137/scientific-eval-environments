# General Long-Horizon Agent Benchmarks

> **English** | [简体中文](../zh/topics/long_horizon_evaluation.md) · [← All topics](./README.md)

## Definition

Long-horizon agent evaluation covers benchmarks whose tasks require many sequential decisions, tool calls, or interaction turns before the task can be judged complete. "Long" is not a fixed step count; it is the property that failures accumulate across steps, that intermediate state matters, and that a single terminal reward gives too little diagnostic signal.

## Motivation

Short-horizon benchmarks over-reward models that are strong at one-shot reasoning. Real deployments — professional workflows, scientific-computing pipelines, multi-turn tool use — are longer than a single prompt-response. Long-horizon benchmarks are the setting in which planning, error recovery, state maintenance, and cost-awareness become measurable, and they are typically the setting in which trajectory-level evaluation is worth its overhead.

## Existing Approaches

Long-horizon benchmarks differ along several axes: the environment substrate, the horizon length, the presence of dense intermediate rewards, and the ecological grounding of tasks.

- **Professional-workflow grounding.** [Agents' Last Exam](../works/agents-last-exam.md) grounds long-horizon tasks in the U.S. occupational taxonomy across 13 industry clusters, co-designed with 250+ industry experts.
- **Terminal-based long-horizon extension.** [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md) extends Terminal-Bench toward longer horizons with dense reward-based grading.
- **Scientific long-horizon workflows.** [Terminal-Bench Science](../works/terminal-bench-science.md) targets natural-science computational workflows in containerized environments.
- **Capability-driven proactive-agent tasks.** [UniClawBench](../works/uniclawbench.md) evaluates proactive agents across five capability axes with Docker-based closed-loop simulation.
- **Deep-research trajectories.** [TRACE](../works/trace.md) targets long-horizon deep-research workflows with a hierarchical trajectory utility function.
- **Long-horizon financial tool use.** [FinTrace](../works/fintrace.md) evaluates long-horizon financial decision-making with 9 metrics across 4 dimensions.
- **Real software-engineering tasks.** [SWE-bench](../works/swe-bench.md) tasks agents with resolving 2,294 real GitHub issues by editing a codebase, graded by executing each repository's own test suite; its human-validated 500-instance SWE-bench Verified subset is the reliability-focused variant.
- **Multi-environment agent capability.** [AgentBench](../works/agentbench.md) assembles 8 distinct interactive environments under one harness to probe LLM-as-agent reasoning and decision-making across multi-round interaction.
- **General-assistant questions.** [GAIA](../works/gaia.md) poses 466 real-world questions requiring reasoning, multimodality, web browsing, and tool use, with single unambiguous answers — humans reach 92% vs. 15% for GPT-4 with plugins.
- **Realistic web environments.** [WebArena](../works/webarena.md) hosts fully functional websites across four domains and scores long-horizon web tasks by functional correctness (best GPT-4 agent 14.41% vs. 78.24% human).
- **Whole-computer tasks.** [OSWorld](../works/osworld.md) provides 369 open-ended tasks in real operating systems (Ubuntu / Windows / macOS) with per-task execution-based evaluation scripts (best model 12.24% vs. 72.36% human).
- **Realistic multi-app tool orchestration.** [Toolathlon](../works/toolathlon.md) spans 32 real software applications and 604 tools exposed through MCP servers, initializing environments with realistic states from real software and scoring 108 cross-app tasks (~20 turns on average) with deterministic, state-based evaluation scripts; the best model reaches 38.6% pass@1, and the pass@3 / pass^3 gap surfaces reliability as a distinct weakness.
- **Documentation-intensive data analysis.** [LongDA](../works/longda.md) makes navigating long documentation the bottleneck: 505 analytical queries over 17 U.S. national surveys whose documentation averages 263k tokens, solved in multi-turn blocks of document retrieval, integration, and Python execution under a 100-step budget; the strongest evaluated model reaches only a 68.91% match rate, and the paper attributes success to retrieval and tool-use strategy rather than reasoning.
- **Open-ended literature search.** [AutoResearchBench](../works/autoresearchbench.md) makes the horizon open-ended by construction: its 1,000 literature-discovery queries involve an unknown number of qualifying papers, so agents must sustain progressive multi-step probing and decide when to stop; the strongest models stay below 10% on both of its task types.
- **Asynchronous environments.** [Gaia2](../works/gaia2.md) runs 1,120 scenarios in event-driven environments that advance on their own clock rather than only when the agent acts, making temporal awareness a scored capability: GPT-5 (high) leads at 42.1% pass@1 overall yet scores 0.0 on the Time split, and every evaluated model scores below 9 there.
- **Terminal report quality over a research horizon.** [DeepResearch Bench](../works/deepresearch-bench.md) covers the same deep-research horizon as TRACE but deliberately scores only the end product, on the grounds that commercial agents' internal retrieval and reasoning are not observable: 100 expert-authored tasks whose topical mix is compressed from 44,019 filtered real user queries, judged by a reference-based adaptive-criteria framework (RACE) alongside live citation verification (FACT). Gemini-2.5-Pro Deep Research leads at 48.88 RACE overall, and the citation-grounding ordering diverges from the report-quality ordering.
- **Iterative engineering optimization.** [Frontier-Eng](../works/frontier-eng.md) makes the horizon an optimization trajectory: over 47 real-world engineering tasks, the agent repeatedly proposes a candidate design, receives continuous reward from an industrial-grade simulator under hard feasibility constraints, and revises within a fixed interaction budget — with both improvement frequency and improvement magnitude decaying as power laws across the trajectory.
- **Mergeability as the target.** [FrontierCode](../works/frontiercode.md) (Cognition; industry benchmark, no paper) grades PR-scale tasks in real open-source repositories on whether a maintainer would actually merge the result — correctness, test quality, scope discipline, style — via an ensemble of tests, rubrics, and verifiers, with solution-consulting runs zeroed.
- **Open-ended survival horizon.** [KellyBench](../works/kellybench.md) drops agents into a season-long simulation of non-stationary sports-betting markets where the objective is long-term bankroll growth; every frontier model evaluated loses money on average (best −8%), and a human-expert rubric rates their strategies as unsophisticated.
- **The interactive transfer gap.** [SWE-Interact](../works/swe-interact.md) reruns software-engineering tasks as multi-turn, user-driven sessions with progressively revealed requirements; models that solve ~50% single-turn drop to ~25% interactive.
- **Replayed real sessions.** [SWE-Together](../works/swe-together.md) curates 109 verifiable repository-level tasks from 11,260 real user-agent sessions and replays them through an intent-preserving user simulator, scoring final correctness together with the corrective feedback turns the agent consumes.
- **Long-horizon biological discovery.** [scBench-Long](../works/scbench-long.md) gives agents raw or near-raw single-cell data and no prescribed methods, requiring them to sustain a full analysis journey to the study's published conclusions; controlled answer vocabularies keep the open-ended horizon deterministically gradable, and the best model-harness pair passes only 25.4% of runs.
- **Execution-scored embodied planning.** [LoTa-Bench](../works/lota-bench.md) automates LLM task-planner comparison by executing plans in ALFRED/AI2-THOR and VirtualHome and grading goal satisfaction, replacing human plan inspection.
- **Ability-decomposed embodied decision making.** [Embodied Agent Interface](../works/embodied-agent-interface.md) evaluates LLMs across four modules — goal interpretation, subgoal decomposition, action sequencing, transition modeling — against simulator state with a typed error taxonomy over VirtualHome and BEHAVIOR.
- **The high-vs-low competence split.** [EmbodiedBench](../works/embodiedbench.md) runs 24 MLLMs as vision-driven agents over 1,128 tasks in four environments; models handle high-level semantics but fail low-level manipulation, capping GPT-4o at 28.9% average.
- **Category-broad interactive evaluation.** [EmbodiedEval](../works/embodiedeval.md) puts MLLMs through 328 tasks in 125 3D scenes spanning navigation, object and social interaction, and embodied QA, with a large shortfall to human level.
- **Collaboration overhead, measured.** [PARTNR](../works/partnr.md) benchmarks LLM planners on 100,000 human-robot collaboration tasks and finds that an LLM partner makes a human slower than working alone (1.1x the steps).
- **Asynchrony as the variable.** [Robotouille](../works/robotouille.md) isolates asynchronous planning: identical ReAct machinery drops from 47% on synchronous cooking tasks to 11% when actions overlap in time.
- **Dialog as coordination.** [RoCo / RoCoBench](../works/rocobench.md) evaluates multi-robot collaboration where each arm's LLM negotiates plans and waypoints in natural language, with real-UR5 demonstration.
- **Safety-aware embodied planning.** [SafeAgentBench](../works/safeagentbench.md) pairs hazardous and safe tasks (750 total, 10 hazards) in an executable environment; the most cautious baseline rejects only 10% of detailed hazards, and swapping the LLM does not help.
- **Scaffolding dependence in coding-agent robotics.** [CaP-X](../works/cap-x.md) benchmarks 12 frontier models writing robot-control programs across abstraction tiers, showing success degrades as human-crafted primitives are removed.
- **ML engineering on Kaggle.** [MLE-bench](../works/mle-bench.md) has agents run full Kaggle competitions end to end — data prep, training, iteration — graded against medal thresholds over 75 competitions.
- **A trainable ML-engineering gym.** [MLE-Dojo](../works/mle-dojo.md) makes ML engineering an interactive, RL-trainable environment over 200+ Kaggle challenges with iterative feedback loops.
- **Improve-the-metric experimentation.** [MLAgentBench](../works/mlagentbench.md) runs read-execute-inspect-iterate loops across 13 ML tasks, scoring measured improvement over starter code.
- **Novel-method research competitions.** [MLRC-Bench](../works/mlrc-bench.md) has agents propose and implement research methods over 7 competition tasks, scored by the human-gap they close.
- **Repository setup and execution.** [SUPER](../works/super.md) requires multi-step configuration and execution of real research repositories to reproduce results.
- **Full research pipelines.** [MLR-Bench](../works/mlr-bench.md) spans idea, proposal, experiment, and paper stages over 201 tasks, foregrounding result-fabrication reliability.
- **Time-budgeted AI R&D.** [RE-Bench](../works/re-bench.md) evaluates agents against human experts on open-ended research engineering under 2/8/32-hour budgets.
- **An AI-research gym.** [MLGym](../works/mlgym.md) runs the full research loop — idea to analysis — over 13 tasks in a Gym environment supporting RL training.
- **AI-development agents.** [DevAI / Agent-as-a-Judge](../works/devai.md) has agents build AI/ML projects against 365 hierarchical requirements, evaluated step by step.
- **Factorized-difficulty robot manipulation.** [VLA-Arena](../works/vla-arena.md) evaluates Vision-Language-Action policies over 170 manipulation tasks with orthogonal difficulty axes and graded levels L0–L2, including a dedicated Long Horizon suite and a cumulative-cost metric.
- **Task-state horizon.** [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md) introduces the task-state horizon — the span of task-relevant state an agent must track, maintain, explore, and update — and compiles 588 embodied-planning episodes with intervention-induced state updates and recovery metrics.
- **End-to-end data-science workflows.** [DSAgentBench](../works/dsagentbench.md) frames data science as long-horizon, multi-stage, multi-tool work executed inside real computer environments, pairing each of 275 tasks with a deterministic evaluator.
- **Interleaved browsing and computation.** [DrBencher](../works/drbencher.md) synthesizes deep-research questions that require multi-hop browsing interleaved with multi-step computation, with execution-verifiable gold answers from knowledge-graph chains.
- **Harness self-improvement.** [Evo-Bench](../works/evo-bench.md) scores a model on how much it can improve its own agent harness across a bounded evolution loop, reporting downstream performance and an anytime-validation trajectory.
- **Multilingual large-scale refactoring.** [SWE-Bench ProMax](../works/swe-bench-promax.md) tests coordinated, behavior-preserving changes averaging 11.4 files and 261.6 lines per instance across seven programming languages.
- **Loop engineering.** [LoopsBench](../works/loopsbench.md) models sustained software development as a dependency DAG over separately testable units, with a flow-aware runtime that releases tests along the ready frontier and retains completed nodes as regression obligations.

## Comparison

| Benchmark | Year | Horizon signal | Environment | Card |
|---|---|---|---|---|
| Agents' Last Exam | 2026 | ~1,000+ real-world professional tasks | Occupational-taxonomy tasks | [→](../works/agents-last-exam.md) |
| Long-Horizon-Terminal-Bench | 2026 | 46 tasks; hundreds of steps; dense graded reward | Terminal (Docker) | [→](../works/long-horizon-terminal-bench.md) |
| Terminal-Bench Science | 2026 | Minutes-to-hours scientific workflows | Container (pytest verification) | [→](../works/terminal-bench-science.md) |
| UniClawBench | 2026 | 400 multi-turn checkpointed tasks | Live Docker + closed-loop simulation | [→](../works/uniclawbench.md) |
| TRACE | 2026 | Deep-research multi-step trajectories | Deep research | [→](../works/trace.md) |
| FinTrace | 2026 | 800 long-horizon financial trajectories | Financial tool use | [→](../works/fintrace.md) |
| SWE-bench | 2023 | 2,294 issues; multi-file cross-function edits | Software engineering (Python repos); execution-graded | [→](../works/swe-bench.md) |
| AgentBench | 2023 | 8 interactive environments; multi-round | Cross-environment agent capability | [→](../works/agentbench.md) |
| GAIA | 2023 | 466 multi-tool assistant questions | General assistant (reasoning / browsing / tools) | [→](../works/gaia.md) |
| WebArena | 2023 | Long-horizon web tasks; functional correctness | Live self-hosted websites (4 domains) | [→](../works/webarena.md) |
| OSWorld | 2024 | 369 open-ended computer tasks | Real OS (Ubuntu / Windows / macOS); execution-graded | [→](../works/osworld.md) |
| Gaia2 | 2026 | 1,120 scenarios across seven capability splits; the environment advances independently of the agent | Simulated smartphone universe of 12 stateful apps; write-action verifier | [→](../works/gaia2.md) |
| AutoResearchBench | 2026 | 1,000 open-ended literature-discovery queries; progressive multi-turn probing with unknown answer-set size | Agentic search over academic and general web retrieval | [→](../works/autoresearchbench.md) |
| LongDA | 2026 | 505 queries in multi-turn publication blocks; 100-step budget over avg 263k-token documentation | Document navigation + sandboxed Python over U.S. federal survey data | [→](../works/longda.md) |
| Toolathlon | 2025 | 108 cross-app tasks; ~20 turns on average (100-turn cap); avg 69.9 tools exposed per task | 32 real applications / 604 tools via MCP; containerized + remote; state-based scripts | [→](../works/toolathlon.md) |
| Frontier-Eng | 2026 | 47 tasks; iterative propose-execute-evaluate loops under a fixed interaction budget | Industrial-grade engineering simulators (continuous reward, hard feasibility constraints) | [→](../works/frontier-eng.md) |
| DeepResearch Bench | 2025 | 100 PhD-level research-report tasks; horizon unbudgeted and scored only at the end product | Commercial deep research agents + search-enabled LLMs; reference-based LLM-judge report scoring + live citation verification | [→](../works/deepresearch-bench.md) |
| FrontierCode | 2026 | PR-scale end-to-end tasks authored at 40+ hours each; graded on mergeability | Real open-source repositories (industry benchmark; ensemble of tests, rubrics, verifiers) | [→](../works/frontiercode.md) |
| KellyBench | 2026 | A full simulated season of sequential decisions; ruin is absorbing | Non-stationary sports-betting markets (2023–24 EPL simulation) | [→](../works/kellybench.md) |
| SWE-Interact | 2026 | Multi-turn user-driven sessions; ~50% single-turn vs. ~25% interactive | Software engineering with a simulated user revealing requirements progressively | [→](../works/swe-interact.md) |
| SWE-Together | 2026 | 109 replayed repository-level sessions; corrective-turn counting alongside correctness | Real-session-derived interactive coding via an intent-preserving user simulator | [→](../works/swe-together.md) |
| scBench-Long | 2026 | 21 evaluations from near-raw data to published conclusions; 1,068 trajectories | Single-cell biology analysis with deterministic grading + trajectory rubrics | [→](../works/scbench-long.md) |
| LoTa-Bench | 2024 | Multi-step skill-sequence plans executed to goal satisfaction | ALFRED/AI2-THOR and Watch-And-Help/VirtualHome (simulation) | [→](../works/lota-bench.md) |
| Embodied Agent Interface | 2024 | Four decision modules scored against simulator state; typed error taxonomy | VirtualHome and BEHAVIOR (simulation) | [→](../works/embodied-agent-interface.md) |
| EmbodiedBench | 2025 | 1,128 tasks, high-level to atomic action; six capability subsets | Four embodied environments (simulation) | [→](../works/embodiedbench.md) |
| EmbodiedEval | 2025 | 328 interactive tasks across five categories | 125 3D scenes (simulation) | [→](../works/embodiedeval.md) |
| PARTNR | 2024 | 100,000 collaboration tasks; steps-vs-human-baseline overhead | 60 Habitat houses, human-in-the-loop (simulation) | [→](../works/partnr.md) |
| Robotouille | 2025 | Synchronous vs. asynchronous success gap (47% → 11%) | Long-horizon cooking simulation | [→](../works/robotouille.md) |
| RoCo / RoCoBench | 2023 | 6 collaboration tasks; dialog + replanning under environment feedback | MuJoCo multi-robot + real UR5 demo | [→](../works/rocobench.md) |
| SafeAgentBench | 2024 | 750 hazardous/safe tasks; rejection rate and success rate | SafeAgentEnv embodied simulation | [→](../works/safeagentbench.md) |
| CaP-X | 2026 | Code-synthesis success across abstraction tiers; scaffolding dependence | Robosuite/LIBERO-PRO/BEHAVIOR sim + real robots | [→](../works/cap-x.md) |
| MLE-bench | 2024 | End-to-end Kaggle competitions; medal-anchored scoring | 75 curated Kaggle ML-engineering competitions | [→](../works/mle-bench.md) |
| MLE-Dojo | 2025 | Iterative experiment/debug loops; long-horizon solution quality | Gym environment over 200+ Kaggle challenges | [→](../works/mle-dojo.md) |
| MLAgentBench | 2023 | Read-execute-inspect-iterate; improvement over starter code | 13 ML-experimentation tasks | [→](../works/mlagentbench.md) |
| MLRC-Bench | 2025 | Propose + implement novel methods; gap-closed vs. top humans | 7 ML research-competition tasks | [→](../works/mlrc-bench.md) |
| SUPER | 2024 | Multi-step repo setup and execution; end-to-end vs. scenario success | Real ML/NLP research repositories | [→](../works/super.md) |
| MLR-Bench | 2025 | Four research stages; ~80% fabricated-result rate | 201 open-ended ML research tasks | [→](../works/mlr-bench.md) |
| RE-Bench | 2024 | Best-of-k under 2/8/32-hour budgets vs. human experts | 7 research-engineering environments (METR) | [→](../works/re-bench.md) |
| MLGym | 2025 | Full research loop; RL-trainable Gym | 13 open-ended AI-research tasks (Meta) | [→](../works/mlgym.md) |
| DevAI / Agent-as-a-Judge | 2024 | Build AI/ML projects; step-wise requirement grading | 55 AI-development tasks, 365 requirements | [→](../works/devai.md) |
| VLA-Arena | 2025 | 170 tasks over 11 suites; graded levels L0–L2 incl. a Long Horizon suite; SR + Cumulative Cost | Simulated robot manipulation (RoboSuite / LIBERO / VLABench) | [→](../works/vla-arena.md) |
| RoboGraphBench | 2026 | 588 episodes; task-state horizon (maintain / explore / update); 100-step closed loop; state-management + recovery metrics | Embodied high-level planning (RoboTwin 2.0 / RoboCasa simulators) | [→](../works/compiling-and-benchmarking-task-state-horizons-for.md) |
| DSAgentBench | 2026 | 275 multi-stage, multi-tool data-science workflows | Real computer environments (notebooks / IDEs / terminals / browsers / databases) | [→](../works/dsagentbench.md) |
| DrBencher | 2026 | Interleaved multi-hop browsing + multi-step computation; answer-first KG-chain synthesis | Deep research over five domains (web + domain APIs) | [→](../works/drbencher.md) |
| Evo-Bench | 2026 | 608 tasks; bounded harness-evolution loop (20 iters / 1,000 steps / 48h); Overall + Anytime Validation Score | Search / Office / General agent harness self-improvement | [→](../works/evo-bench.md) |
| SWE-Bench ProMax | 2026 | 170 refactoring instances; avg 11.4 files / 261.6 LOC changed per task | Multilingual software repositories (7 languages); execution-graded | [→](../works/swe-bench-promax.md) |
| LoopsBench | 2026 | 112 tasks; dependency-DAG "loop engineering" over 5,300+ development units; flow-aware regression obligations | Software development (8 languages, 9 domains); Docker-backed | [→](../works/loopsbench.md) |

## Open Questions

- **What counts as "long horizon"?** Steps? Wall-clock? Distinct tool calls? Distinct sub-decisions? Different benchmarks pick different notions, complicating cross-benchmark comparison.
- **Terminal reward vs. trajectory metric.** Benchmarks with dense subtask rewards produce non–Pass@1 signals; benchmarks with only terminal outcomes do not. How should the field weight the two on long-horizon leaderboards?
- **Ecological validity vs. reproducibility.** Ecologically grounded tasks (Agents' Last Exam, Terminal-Bench Science) draw from real workflows and pay a review cost. Synthetically constructed tasks scale more easily. Which regime should serve as the primary evaluation surface?
- **Headroom.** Frontier models saturate short-horizon benchmarks quickly. Do current long-horizon benchmarks retain headroom over the next model generation?

## Related Works

- [VLA-Arena](../works/vla-arena.md)
- [DrBencher](../works/drbencher.md)
- [LoopsBench](../works/loopsbench.md)
- [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md)
- [SWE-Bench ProMax](../works/swe-bench-promax.md)
- [DSAgentBench](../works/dsagentbench.md)
- [Evo-Bench](../works/evo-bench.md)
- [Agents' Last Exam](../works/agents-last-exam.md)
- [Long-Horizon-Terminal-Bench](../works/long-horizon-terminal-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [UniClawBench](../works/uniclawbench.md)
- [TRACE](../works/trace.md)
- [FinTrace](../works/fintrace.md)
- [SWE-bench](../works/swe-bench.md)
- [AgentBench](../works/agentbench.md)
- [GAIA](../works/gaia.md)
- [WebArena](../works/webarena.md)
- [OSWorld](../works/osworld.md)
- [Gaia2](../works/gaia2.md)
- [AutoResearchBench](../works/autoresearchbench.md)
- [LongDA](../works/longda.md)
- [Toolathlon](../works/toolathlon.md)
- [Frontier-Eng](../works/frontier-eng.md)
- [DeepResearch Bench](../works/deepresearch-bench.md)
- [FrontierCode](../works/frontiercode.md)
- [KellyBench](../works/kellybench.md)
- [SWE-Interact](../works/swe-interact.md)
- [SWE-Together](../works/swe-together.md)
- [scBench-Long](../works/scbench-long.md)
- [LoTa-Bench](../works/lota-bench.md)
- [Embodied Agent Interface](../works/embodied-agent-interface.md)
- [EmbodiedBench](../works/embodiedbench.md)
- [EmbodiedEval](../works/embodiedeval.md)
- [PARTNR](../works/partnr.md)
- [Robotouille](../works/robotouille.md)
- [RoCo / RoCoBench](../works/rocobench.md)
- [SafeAgentBench](../works/safeagentbench.md)
- [CaP-X](../works/cap-x.md)
- [MLE-bench](../works/mle-bench.md)
- [MLE-Dojo](../works/mle-dojo.md)
- [MLAgentBench](../works/mlagentbench.md)
- [MLRC-Bench](../works/mlrc-bench.md)
- [SUPER](../works/super.md)
- [MLR-Bench](../works/mlr-bench.md)
- [RE-Bench](../works/re-bench.md)
- [MLGym](../works/mlgym.md)
- [DevAI / Agent-as-a-Judge](../works/devai.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
