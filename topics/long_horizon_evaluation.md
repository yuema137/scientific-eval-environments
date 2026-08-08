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

## Open Questions

- **What counts as "long horizon"?** Steps? Wall-clock? Distinct tool calls? Distinct sub-decisions? Different benchmarks pick different notions, complicating cross-benchmark comparison.
- **Terminal reward vs. trajectory metric.** Benchmarks with dense subtask rewards produce non–Pass@1 signals; benchmarks with only terminal outcomes do not. How should the field weight the two on long-horizon leaderboards?
- **Ecological validity vs. reproducibility.** Ecologically grounded tasks (Agents' Last Exam, Terminal-Bench Science) draw from real workflows and pay a review cost. Synthetically constructed tasks scale more easily. Which regime should serve as the primary evaluation surface?
- **Headroom.** Frontier models saturate short-horizon benchmarks quickly. Do current long-horizon benchmarks retain headroom over the next model generation?

## Related Works

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

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
