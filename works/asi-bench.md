# ASI-Bench (2026)

> **English** | [简体中文](../zh/works/asi-bench.md)

> **First appeared:** 2026-08-18 · **Source:** [arXiv:2608.17271v1](https://arxiv.org/abs/2608.17271)

## Overview

ASI-Bench is a benchmark of 60 project-level scientific research tasks across 11 domains that measures how far an agent can carry a research project as human methodological guidance is progressively withdrawn. Each task is posed at four matched prompt levels (B1–B4) that keep the objective, data, and required outputs fixed while removing the method, the procedure, and finally adding factually correct but irrelevant information.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.17271>
- **Code:** <https://github.com/apexin-ai/ASI-Bench>
- **Project:** <https://asibench.apexin.ai/>
- **Submission portal:** <https://asibench.apexin.ai/submit>
- **Package:** `pip install asibench`

## Summary

ASI-Bench argues that existing benchmarks mostly test whether an AI can produce correct answers from learned knowledge, or complete tasks under extensive human guidance, and therefore do not measure autonomous scientific execution. It introduces 60 project-level research tasks across 11 scientific domains, each rewritten at four guidance levels within the same research project so that method selection, workflow construction, and distractor robustness can be isolated. The benchmark was built by more than 40 experts at a stated cost of 31,000+ human hours, drawing on more than 1,300 candidate research ideas and more than 1,100 review assignments. Across 18 agent–model configurations the average score falls from 50.91 at B1 (full methodological guidance) to 29.10 at B2 (method only) and 26.62 at B3 (agent determines the method), which the authors read as evidence that current systems remain heavily dependent on human guidance.

## Tasks

60 project-level research tasks. Each task is issued at four matched prompt levels that hold the research objective, provided data, and required outputs constant:

- **B1** — scientific background, method, equations, and full procedure.
- **B2** — intended method and relevant constraints, without the full procedure; the agent must build the executable workflow.
- **B3** — objective, data, constraints, and required outputs only; the agent determines the method.
- **B4** — B3 plus factually correct but non-essential information, testing robustness to distraction.

Complete research trajectories across the suite involve more than 2,600 interaction turns and 2,400 execution steps, spanning over 35 hours of agent execution. Tasks are sourced from scientific literature (1,300+ candidate ideas) and filtered through multiple expert review rounds to the final 60.

## Domains

11 scientific domains, as listed in the paper: mathematics, physics, chemistry, biology, astronomy, materials science, earth science, medicine and biostatistics, computer science, robotics, and electrical engineering.

## Evaluation

- **Guidance-gradient scoring.** Every task is scored on the same 0–100 scale at each of B1–B4; the headline results are macro averages over the 60 tasks and 18 agent–model configurations: B1 = 50.91, B2 = 29.10, B3 = 26.62.
- **Per-task scorers.** Tasks are graded by task-specific evaluation gates and weighted scorers against reproducible per-task reference outputs (each task ships a ground-truth generator and an optional custom scorer). Repository note: the paper does not give a single sentence separating deterministic checks from any model-judged component.
- **Reference sets and seeds.** A public `seed31415` set publishes reference outputs (on Hugging Face) and supports local scoring; the official `seed42` set keeps references private and is scored through the submission Portal.
- **Sandboxed execution.** Runs execute in an isolated sandbox; local runs may use the `none` or `linux_ns` sandbox, while official `seed42` submission requires the Docker-based `os` sandbox. Every task undergoes expert review, AI-assisted auditing, sandbox execution, and scorer validation.
- **Difficulty guardrail.** For a task to be accepted, its B3 and B4 mean scores must each be strictly below 40; B1 and B2 have no ceiling. This keeps the autonomous levels unsaturated.
- **Cost is reported, not scored.** Token use and wall-clock time are measured and reported per guidance level, and the paper notes that higher cost does not guarantee a better score, but computational cost is not part of the task metric.

## Typical Duration

Over 35 hours of cumulative agent execution across the suite, with more than 2,600 interaction turns and 2,400 execution steps for complete trajectories. Per-task wall-clock and token figures are reported by guidance level rather than as a single budget; no fixed per-task step or token cap is imposed on submissions.

## Main Contribution

The first benchmark to progressively withdraw human methodological guidance within the same research project (B1–B4), turning "can the agent select its own method and still finish the project" into a measured quantity across 60 project-level tasks and 11 domains, with a public contribution portal and a difficulty guardrail on the autonomous levels.

## Key Design Ideas

- Four matched prompt levels per task that vary only the amount of methodological guidance, so the B1→B3 drop isolates method selection and workflow construction from task difficulty.
- A distractor level (B4) that adds true but irrelevant information to B3, separating robustness-to-distraction from method selection.
- An acceptance rule that forces every task's B3 and B4 mean below 40, keeping the autonomous regime from saturating.
- Public/private reference split (`seed31415` / `seed42`) with Portal-based scoring for the official set.
- Agent-neutral harness adapters (Codex CLI, Claude Code, Kimi Code, CodeWhale, AntiGravity) plus a generic command interface.

## Strengths

- The within-project guidance gradient is a controlled manipulation: the same task at B1 and B3 differs only in provided method, so the score gap is interpretable.
- Large curation and validation investment (40+ experts, 31,000+ human hours, multiple review rounds, AI-assisted auditing, sandbox execution, scorer validation).
- Difficulty guardrail on B3/B4 is checked at task-acceptance time, not asserted after the fact.
- Open task contribution with a documented submission and validation flow, and reproducible per-task ground-truth generation.

## Limitations

- Repository note: the public description does not fully specify the scorer design per task (weighting, and whether any component is model-judged), so cross-task comparability of the 0–100 scale rests on the private scorer code.
- Repository note: headline numbers are macro averages over 18 agent–model configurations; per-domain and per-task difficulty spread is not summarized in the abstract-level material consulted here.
- Repository note: `medicine and biostatistics` is a single combined domain in the paper's list, so the 11-domain count is not a clean partition of the repository's canonical domains.

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — Also extracts execution-scored scientific tasks from the literature with expert validation, but grades individual analysis subtasks as standalone programs rather than posing whole research projects at varying guidance levels.
- [AstaBench](./astabench.md) — Also a multi-domain scientific research suite with a public leaderboard, but organized around cost-controlled scoring across literature, code, data analysis, and end-to-end discovery rather than a within-project guidance gradient.
- [AIRS-Bench](./airs-bench.md) — Also withholds baseline code to force agents to build workflows from scratch, but does so at one guidance level across 20 tasks rather than four matched levels across 60.
- [PaperBench](./paperbench.md) — Also measures autonomous end-to-end research, but scored as replication of a specific target paper rather than open-method completion of a research objective.
- [Terminal-Bench Science](./terminal-bench-science.md) — Also an agent-neutral, container-executed multi-domain scientific benchmark, but built from domain-expert terminal tasks with deterministic pytest checks and no guidance-level manipulation.
