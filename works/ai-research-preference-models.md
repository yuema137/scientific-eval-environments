# AI Research Preference Models (2026)

> **English** | [简体中文](../zh/works/ai-research-preference-models.md)

> **First appeared:** 2026-08-14 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.13940)

## Overview

AI Research Preference Models (RPMs) predict which of an AI research agent's candidate solutions are worth the GPU time to execute, so a fixed execution budget can be spent on the candidates most likely to pay off. Two variants are built from frozen pretrained language models with no task-specific training — one that reasons over plans and code alone, and one that first runs small pilot experiments — and both are integrated into the AIRA-dojo search agent and measured on AIRS-Bench.

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.13940>
- **Code:** `TODO(reference)` — no release location is stated in the paper; the arXiv posting is CC BY 4.0.
- **Venue:** arXiv preprint (August 2026); 34 pages, 17 figures, 6 tables.

## Summary

The framing problem is an asymmetry in cost: an AI research agent can write a candidate solution in minutes, but finding out whether it works takes hours to days of GPU time. An agent can therefore always propose more candidates than it can afford to run, which makes its *research preference* — how it allocates a fixed execution budget across candidates — a determinant of progress independent of its ability to generate good ideas. RPMs supply that preference. The inference-only variant reasons over candidate plans, candidate code, and the prior executed solutions with their validation scores, and picks without running anything. The agentic variant additionally gets a sandboxed clone of the execution environment and runs small-scale pilot experiments — a multi-turn agent with python, bash and submit tools under a five-minute cap — before deciding. Both are dropped into AIRA-dojo's child-creation step, where the search generates 15 candidates per step under Draft, Improve and Debug operators. The result is reported as both a score gain and a budget saving, and the paper measures how far below an oracle its selections fall.

## Tasks

The evaluation substrate is **[AIRS-Bench](./airs-bench.md)**: **20 publicly released text and tabular tasks** spanning language modeling, mathematics, bioinformatics and time-series forecasting. Performance is a **normalized score** per task, `NS = [φ(s) − φ(s_min)] / [φ(s_sota) − φ(s_min)]`, where **NS = 0** is a minimum baseline and **NS = 1** is public state of the art — which is what makes results comparable across heterogeneous task metrics.

The host agent is **AIRA-dojo**, an evolutionary tree-search framework: greedy parent selection always mutates the node with the highest current validation score, **N = 15** candidate solutions are generated per step, and the final submission is the node with the best validation score anywhere in the tree.

## Domains

**AI & Machine Learning Research.** The work being selected among is machine-learning research work — model and training changes scored by held-out task performance — and the contribution is measured entirely as AIRS-Bench normalized score. No science co-domain is assigned: although AIRS-Bench itself spans bioinformatics and mathematics, this paper reports no per-domain breakdown of its 20 tasks, and its two named per-task results (WinoGrande, SVAMP) are single tasks rather than a sized domain slice.

## Evaluation

End-to-end results over **24-hour runs on one H200 GPU per task, 10 seeds, 20 tasks — 200 H200 GPU-hours in total**:

| Configuration | Normalized score | Wall-clock to match baseline |
|---|---|---|
| Unguided AIRA-dojo (no RPM) | **0.684** | 24 h |
| Inference-only RPM | **0.711** | 14.88 h (1.61× speedup) |
| Agentic RPM | **0.729** | 15.50 h (1.55× speedup) |
| Validation-oracle ceiling | 0.748 | — |
| Test-oracle ceiling | 0.759 | — |

Both variants match the unguided agent's 24-hour performance in roughly 15 hours, **using less than two-thirds of its execution budget**. The oracle rows are the informative part: the agentic RPM at 0.729 closes most of the 0.684→0.748 gap to a perfect validation-based selector, so the remaining headroom from better selection alone is small.

New state of the art is reported on two AIRS-Bench tasks: **WinoGrande 94.1%** (previous SOTA 88.1%) and **SVAMP 95.7%** (previous 94.2%).

Selection quality is measured separately. Selection advantage over random is ~0.0 for random, higher for inference-only and highest for agentic, and correlates with the final score at **Pearson r = 0.55, Spearman ρ = 0.56**.

An offline evaluation over candidate pairs compares backbones: **GPT-5 64.66%**, **Gemini 3.1 Pro 67.40%**, **Claude Opus 4.8 67.44%**, **majority-vote ensemble 68.04%**, **LLM-arbiter ensemble 69.35%**. End-to-end runs use **Qwen3.6-27B** for both child creation and the RPM backbone; prompts are optimized with MIPROv2 from DSPy.

There is **no human or expert agreement measurement**. Offline ground truth is a "subtree-max label" — the highest test score anywhere in a candidate's subtree — which the authors state inherits a bias from the greedy search policy that produced the tree, since nodes with strong early scores were favoured during search.

## Typical Duration

**24 hours on one H200 GPU per task** for the end-to-end runs, 10 seeds each. The agentic RPM's pilot experiments are capped at **5 minutes per candidate selection**. RPM inference itself is cheap relative to the budget it governs: self-hosted Qwen3.6-27B adds **0.66 hours per 24-hour run**, and a run charged for that latency still scores 0.708 against 0.711 unadjusted.

## Main Contribution

Treating budget allocation as a first-class lever for AI research agents, and showing that a frozen pretrained model with no task-specific training can predict which candidate solutions deserve execution well enough to buy the same result for under two-thirds of the compute — with the oracle ceilings reported alongside, so the remaining headroom from selection alone is visible.

## Key Design Ideas

- The RPM is built from a frozen pretrained model with **no task-specific training**, so the gain comes from the prediction being possible at all rather than from fitting the benchmark.
- The two variants isolate a clean trade: reasoning over plans and code costs nothing to run, while pilot experiments cost real sandbox time; reporting both prices the extra information.
- The agentic variant is deployed only for Draft and Improve operators, not Debug — pilot experiments buy little where the task is fixing a known failure.
- Reporting validation-oracle and test-oracle ceilings converts "our selector is better" into "our selector recovers most of what any selector could", which is a much stronger claim shape.
- Selection advantage is measured against random and correlated with the end result, so selection quality is validated as the mechanism rather than assumed from the score gain.
- RPM inference latency is charged against the budget it saves (0.66 h per 24 h run), so the efficiency claim survives its own overhead.
- The offline backbone comparison and ensembling are kept separate from the end-to-end claim, which the authors state their main conclusions rest on.

## Strengths

- The headline result is a budget saving with the score held constant, which is a harder and more useful claim than a score gain at equal budget.
- Oracle ceilings are reported, so the reader can see how much of the achievable selection gain was actually captured and that the remaining margin is thin.
- The overhead of the method is measured and charged against its own benefit rather than excluded.
- The authors mark their offline evaluation as off-policy and biased and state explicitly that the main claims rest on the end-to-end results instead.
- The subtree-max label's bias is named and explained rather than left implicit.
- 200 H200 GPU-hours across 10 seeds per task is a substantial evaluation for a claim about search efficiency, where single-seed results would be dominated by variance.

## Limitations

- No release location is stated for code or data (recorded above as `TODO(reference)`), so the RPMs are not directly reusable.
- The authors state the method is demonstrated only in AIRA-dojo's child-selection step, with a single backbone (Qwen3.6-27B) on a single benchmark, and that portability to other scaffolds and backbones is future work.
- Applying the RPM to final-node selection rather than child creation shows little improvement over ordinary validation-based selection (Appendix D), so the gain is specific to where in the search it is inserted.
- The agentic variant requires a sandboxed clone of the execution environment, which is a real deployment cost the inference-only variant avoids.
- Offline evaluation ground truth is derived from trees produced by the greedy policy being improved upon, so the offline backbone rankings are not a clean measurement.
- No human or expert judgment is used anywhere; selection quality is validated only against downstream task scores.
- Repository note: the paper's primary framing is a **search component that makes an agent better**, not an instrument for measuring agents, and it introduces no benchmark or scoring protocol of its own — it is evaluated on the pre-existing AIRS-Bench. This card indexes it under Resource-aware Evaluation on the reading that a cheap surrogate predictor of solution quality under a fixed execution budget is an evaluation function; that classification is the repository's, not the authors'.

## Related Works

- [AIRS-Bench](./airs-bench.md) — The benchmark this work is measured on: the ML-research task suite whose normalized score every number above is expressed in.
- [Beyond Final Scores](./beyond-final-scores.md) — Also studies long-horizon AI R&D under a wall-clock budget, measuring how agents spend a run rather than steering what they spend it on.
- [MLE-bench](./mle-bench.md) — Machine-learning engineering under a compute budget, where budget bounds the run rather than being the object of allocation.
- [SimulCost](./simulcost.md) — Cost-aware evaluation where compute spent is scored against accuracy achieved, the same accuracy-per-compute framing on simulation tuning.
- [R³-Bench](./r3-bench.md) — Allocation of a shared budget across candidate problems, measured against an oracle built from observed outcomes — the same "how well was the budget spent" question posed as a benchmark rather than solved as a method.
