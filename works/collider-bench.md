# Collider-Bench (2026)

## Overview

Collider-Bench is a benchmark that evaluates whether LLM agents can reproduce experimental analyses from the Large Hadron Collider (LHC) using only public papers and open scientific software. Its first release holds 10 Simulation tasks drawn from four CMS supersymmetry searches, run in a containerized sandbox with the public collider-simulation stack and scored by continuous histogram fidelity against hidden reference yields.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.13950>
- **Code:** <https://github.com/dfaroughy/Collider-Bench>

## Summary

Collider-Bench addresses the gap that existing long-horizon tool-use benchmarks rarely capture the complexity and nuance of real scientific work: the public toolchain only approximates the software used internally by the LHC collaborations, and published papers omit implementation details needed for a faithful reconstruction, so agents must fill the gaps through physical reasoning, domain knowledge, and trial-and-error. Each task requires the agent to turn a published analysis into an executable simulation-and-selection pipeline and submit predicted collision event yields in specified signal regions, evaluated with histogram metrics that provide continuous fidelity scores without a hand-written rubric, complemented by per-task computational-cost reporting and an LLM judge over the codebase and full session trace. Across a capability ladder of six general-purpose coding agents, on average no agent reliably beats the physicist-in-the-loop solution.

## Tasks

10 primary Simulation tasks drawn from four CMS supersymmetry searches at 13 TeV with 35.9 fb⁻¹ of integrated luminosity (CMS-SUS-16-034, CMS-SUS-16-046, CMS-SUS-16-047, CMS-SUS-16-051), each fixing a target search paper, a signal benchmark point, a target observable or signal region, and a fixed output template; a secondary Shape task suite removes the requirement to predict the absolute event yield, and difficulty is graded from easy to hard on the basis of the physicist-in-the-loop experiments. The agent must read the paper, generate signal events through the public simulation stack (MadGraph5, Pythia 8.313, Delphes 3.5.0, with Prospino 2.1 for cross sections), implement the published event selection, and submit a binned histogram of predicted signal yields together with analysis code, simulation configurations, and a short methodological report. Each task was first solved by a domain expert working with an agent through the same toolchain, establishing that the public stack can reproduce the published target, and the authors state that at least an order of magnitude more tasks are available for future releases.

## Domains

Experimental particle physics: recasting CMS searches for supersymmetry (simplified-model signal topologies) at the Large Hadron Collider.

## Evaluation

- **Relative L² distance.** The primary fidelity metric: the bin-level discrepancy between the predicted and hidden reference histograms, normalized to the reference so that high-yield bins contribute more strongly; a complementary yield-normalization error and a shape–normalization decomposition separate event-selection failures from absolute-rate failures.
- **Thresholded accuracy.** A run passes if its relative L² error falls below a tolerance τ = 0.33, chosen as the worst relative L² error achieved by the physicist-in-the-loop baseline across the task set — a deliberately lenient criterion under which an agent passes only by matching or improving on the weakest supervised reproduction.
- **LLM provenance judge.** Claude-Opus-4.6 inspects the agent's full workspace and execution trace and flags each run Passed, Failed, or Fabricated, where fabrication covers hand-coded fallback arrays, surrogate shape generators, made-up efficiencies, and values copied from public sources; the judge does not assign the numerical score.
- **Cost and efficiency.** API cost, token usage, and wall-clock time are reported as separate efficiency metrics, not folded into the fidelity score, treating scientific accuracy and inference cost as distinct axes of agent performance.
- **Reported.** Six systems — Claude Code (Opus 4.7, Sonnet 4.6, Haiku 4.5), Codex CLI (GPT-5.5, GPT-5.4-mini), and ForgeCode (DeepSeek-V4) — are each run three times per task: agents improve along the capability ladder and form a visible cost–performance frontier, but even the strongest systems pass only a subset of the tasks, and on average no agent reliably beats the physicist-in-the-loop solution; across 364 judged runs the provenance judge returns Passed 87%, Failed 6%, and Fabricated 6%, with Haiku 4.5 accounting for the majority of fabricated submissions.

## Typical Duration

A 2.5-hour wall-clock budget per task, run as a single autonomous session at maximum reasoning effort with access to 128 AMD EPYC 7763 CPU cores for simulation workloads. Mean run time per Simulation task ranges from 0.299 h (Haiku 4.5) to 1.706 h (DeepSeek-V4), at mean Spring-2026 list-price API costs between $0.89 (DeepSeek-V4) and $14.21 (Opus 4.7).

## Main Contribution

A benchmark formalizing LHC recasting — the end-to-end reproduction of published collider searches from public papers and open simulation software — as a long-horizon agent task scored by continuous histogram fidelity against hidden reference yields and audited by an LLM provenance judge.

## Key Design Ideas

- Tasks anchored to published LHC searches whose public information underdetermines the solution, forcing agents to fill gaps left by internal collaboration software and omitted implementation details through physical reasoning and trial-and-error.
- Hidden reference yields and evaluator code kept outside the agent's workspace, separating the public problem specification from the private scoring target and preventing the task from reducing to information retrieval from plots, tables, or public records.
- Continuous physics-motivated scoring — relative L² fidelity with a shape–normalization decomposition — in place of a hand-written rubric, with the pass threshold calibrated to the worst physicist-in-the-loop reproduction.
- An LLM provenance judge outside the sandbox auditing whether submitted values trace to an executed simulation rather than to fabricated scaling factors or values copied from the literature.

## Strengths

- Every task was first solved by a domain expert through the same public toolchain, so failure reflects agent limitations rather than an unreproducible target.
- Continuous fidelity scores with a physicist-calibrated pass threshold give graded signal on genuinely underdetermined scientific work without hand-written rubrics.
- Separating numerical scoring from provenance auditing catches fabricated submissions that a fidelity score alone would credit.

## Limitations

- Repository note: The first release holds 10 Simulation tasks from four CMS supersymmetry searches at a single center-of-mass energy — the stated order-of-magnitude task expansion and any coverage beyond SUSY simplified-model searches remain future releases.
- Repository note: The pass threshold and the difficulty grading both derive from a single physicist-in-the-loop workflow (Claude Code with Opus 4.7 under domain-expert supervision), so the human reference is one supervised reproduction rather than an independent expert cohort.

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — Also evaluates agents on containerized natural-science computing workflows, but verifies with deterministic pytest checks rather than continuous histogram fidelity against published results.
- [NatureBench](./naturebench.md) — Also anchors difficulty to published scientific results, but spans Nature-family disciplines under a SOTA-matching criterion rather than reproducing one domain's analyses under a physicist-calibrated threshold.
- [ScienceAgentBench](./scienceagentbench.md) — Also extracts tasks from peer-reviewed publications, but unifies outputs to standalone Python programs across four disciplines rather than an end-to-end simulation-and-selection pipeline in a single domain.
