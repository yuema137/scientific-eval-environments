# Co-Evolution in Agentic Systems: Toward Self-Directed Evolution Beyond Human Design (2026)

> **English** | [简体中文](../zh/works/co-evolution-agentic-systems-survey.md)

> **First appeared:** 2026-08-10 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.10299)

## Overview

A survey of co-evolution in agentic systems — the multi-component form of self-evolution in which several agents and their environment exert adaptive pressure on one another. It organises the literature under a progressive three-stage taxonomy tracing how a system sheds human-engineered constraints, and devotes a section to why evaluating such systems is harder than evaluating a fixed agent.

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — a survey of self-evolution methodology for general agentic systems. It evaluates no agent on any scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2608.10299>
- **Venue:** arXiv preprint (August 2026).

## Summary

The survey's starting observation is that single-entity self-evolution is bounded by a static learning context: an agent that improves against fixed tasks and fixed feedback eventually exhausts what that context can teach it. Co-evolution removes that ceiling by letting the other components move too. The three-stage taxonomy is ordered by how much human design remains. **Agent–Agent Co-Evolution** covers agents adapting to dynamic peers, split into adversarial pressure (pairwise and multi-source), collaborative adaptation (parallel and role-differentiated), and evolving agent organizations. **Agent–Environment Co-Evolution** extends the loop to the environment itself across three spaces: the task space (exposure and selection; adaptive task generation), the feedback space (preference-driven, outcome-driven, and consistency-augmented feedback), and the interaction space (executable world construction and model-based world construction). **Meta Co-Evolution** asks whether the evolution mechanism can itself be made evolvable, discussed under open-endedness and under precursors to meta co-evolution. The survey closes on open challenges in evaluation, scaling across components, and keeping increasingly autonomous evolutionary processes safe and controllable.

## Tasks

N/A — a survey. It contributes no task suite. References span from Hillis (1990) through the paper's own August 2026 posting; `TODO(reference)` — the survey does not state a paper count or an explicit coverage window.

## Domains

No canonical domain is assigned. The subject is general agentic-system methodology; the benchmarks it discusses are tool use, web browsing, software engineering, computer use and multi-agent interaction, none of which is a science or engineering field on this repository's domain axis.

## Evaluation

N/A as a scoring protocol — but evaluation is one of the survey's named open challenges, and its treatment is the reason this card is indexed here. The authors argue that existing benchmarks mainly measure an agent's final capabilities, whereas evaluating co-evolution "must determine whether all evolving components improve, whether their gains transfer to unseen partners and environments, and how each component contributes to the joint progress."

Three failure modes are named as specific to this setting: **evaluator exploitation**, **partner overfitting**, and **diversity collapse**. The recommended response is to pair fixed benchmarks with process-level testing — specifically **historical cross-play, component ablations, and held-out evaluators**.

The survey enumerates the benchmarks it discusses inline rather than in a table: τ-Bench, ToolSandbox, PlanBench-XL, CostBench and AdaPlanBench for tool use; WebArena and BrowseComp for web browsing; SWE-Bench and SWE-Lancer for software engineering; AppWorld, OSWorld and Terminal-Bench for computer use; SOTOPIA, AgentSense and MultiAgentBench for multi-agent interaction. Of these it identifies only **PostTrainBench** as evolution-aware — which is the survey's evidence that the evaluation gap it describes is real and largely unfilled.

## Typical Duration

N/A — a survey.

## Main Contribution

A taxonomy that orders self-evolution research by how much human-designed structure it removes, extending the frame from single-agent self-improvement to co-evolution across agents, tasks, feedback and interaction spaces — together with an argument that this class of system breaks the assumptions of static benchmarking, and a concrete list of what would need to be measured instead.

## Key Design Ideas

- The taxonomy's ordering principle is the amount of remaining human design, so the three stages form a progression rather than a partition — Stage 3 is where the evolution mechanism itself becomes a target of evolution.
- Agent–Environment co-evolution is decomposed by *which* part of the environment moves (tasks, feedback, or the interaction space), which separates lines of work that otherwise blur together.
- The evaluation section identifies three failure modes specific to co-evolving systems, each of which is invisible to a fixed benchmark by construction: an evaluator that can be exploited, partners that can be overfit, and diversity that can collapse.
- The proposed remedies are structural rather than metric-level — cross-play against historical opponents, component ablations, and held-out evaluators — matching the claim that the problem is with the evaluation design rather than the score.
- Surveying which existing benchmarks are evolution-aware (one) quantifies the gap instead of asserting it.

## Strengths

- The evaluation discussion is unusually concrete for a survey, naming both the failure modes and the specific testing designs that would address them.
- Identifying exactly one evolution-aware benchmark among the fifteen or so it discusses is a checkable claim that gives the paper's gap argument evidence.
- The three-stage ordering by removed human design gives the taxonomy a principle rather than a list structure, so new work has a determinate place in it.
- The authors state directly where their own Stage 3 is thin, rather than padding it.
- Coverage reaches back to Hillis (1990), placing recent LLM-agent self-evolution in a longer co-evolutionary-computation lineage.

## Limitations

- No paper count or explicit coverage window is stated, so the survey's completeness cannot be assessed (recorded above as `TODO(reference)`).
- The authors state that only limited work meets their definition of Stage 3, so much of that discussion necessarily draws on single-entity meta-evolution as a precursor rather than on meta co-evolution proper.
- Safety, monitoring and human oversight are treated at the level of desiderata; the authors state they do not develop concrete safeguards or protocols.
- No public paper list or repository is mentioned, so the survey is not maintained as a living index.
- The benchmarks discussed are general-agent benchmarks; scientific and engineering evaluation is not covered, so the survey's evaluation critique is not grounded in the scientific-agent literature.
- Repository note: this card is indexed for the survey's evaluation-challenge section. The bulk of the work reviews self-evolution *methods*, which fall outside this repository's scope.

## Related Works

- [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](./agent-skill-evaluation-survey.md) — The closest neighbour: also taxonomises evolution paradigms and the benchmarks that score them, scoped to agent skills rather than to whole systems.
- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — General agent-evaluation taxonomy, covering the static-benchmark setting this survey argues co-evolution breaks.
- [Evaluation and Benchmarking of LLM Agents: A Survey](./agent-evaluation-benchmarking-survey.md) — Organises agent evaluation by objectives versus process, the same distinction this survey reaches for in recommending process-level testing.
- [PACE-Bench](./pace-bench.md) — Evaluates self-evolving agents specifically after the environment changes, an instance of the adaptation-under-shift measurement this survey argues is missing.
