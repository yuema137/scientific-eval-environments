# General Long-Horizon Agent Benchmarks

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
- **Asynchronous environments.** [Gaia2](../works/gaia2.md) runs 1,120 scenarios in event-driven environments that advance on their own clock rather than only when the agent acts, making temporal awareness a scored capability: GPT-5 (high) leads at 42.1% pass@1 overall yet scores 0.0 on the Time split, and every evaluated model scores below 9 there.

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

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
