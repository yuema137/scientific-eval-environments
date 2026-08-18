# AutoResearchEval (2026)

> **English** | [简体中文](../zh/works/autoresearcheval.md)

## Overview

AutoResearchEval is a diagnostic evaluation of end-to-end autonomous research agents over 100 tasks grounded in published frontier science, spanning the full research lifecycle from ideation to review. Rather than ranking systems by a final score, it annotates 800 complete trajectories at the process level and organises the results into ARFT, a taxonomy of 45 empirically grounded failure patterns.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [End-to-End Research](../activities/end_to_end_research.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.14905>
- **Code:** `TODO(reference)` — the paper states that AutoResearchEval and ARFT are publicly released but gives no repository URL in the main text.
- **Venue:** arXiv preprint (August 2026).

## Summary

The authors observe that existing AutoResearch evaluations report performance without revealing process: tasks are narrowly scoped, scores say nothing about where an agent broke down, and failure diagnoses lack systematic coverage or visibility into intermediate artifacts. AutoResearchEval is built to answer the diagnostic question instead. Tasks are grounded in published frontier science and cover six lifecycle stages, and each of eight harness–model combinations is run over all 100 tasks to produce 800 trajectories with process-level annotation. Those annotations are consolidated into ARFT, which cross-classifies failures by lifecycle stage and by root cause. To make fine-grained attribution affordable at this scale, the authors build a human-calibrated agent-as-a-judge pipeline that inspects complete trajectories and intermediate artifacts rather than final answers. The headline finding is convergent: failure patterns across every configuration point to a missing metacognitive loop — the ability to check produced output against gathered evidence, revise when it does not hold, and question whether the chosen path was sound.

## Tasks

**100 tasks**, filtered down from **5,878 initial candidates** across nine domains, retaining seven scientific domains. Tasks split into **open-ended discovery (n = 70)** and **target-anchored optimization (n = 30)**. Each task exercises the full research lifecycle across six stages: **A — Ideation & Planning**, **B — Retrieval & Synthesis**, **C — Execution & Implementation**, **D — Analysis & Interpretation**, **E — Writing & Documentation**, and **F — Self-Verification & Review**. `TODO(reference)` — the per-domain task counts appear only in a figure and are not stated numerically in the main text, so the size of each domain slice cannot be quoted.

## Domains

The benchmark spans **seven scientific domains**, but the paper reports their distribution only graphically and gives no per-domain task counts. Because a multi-field benchmark earns a domain on this repository's domain axis only when the slice is both identifiable and sized, **no canonical domain is assigned** pending a numeric breakdown from the authors.

## Evaluation

**Eight harness–model combinations** produce **800 trajectories**: Claude Code paired with opus-4.8, claude-sonnet-5, qwen3.7-max, glm-5.2, minimax-m3 and deepseek-v4-pro; Codex with gpt-5-mini; and Gemini CLI with gemini-3.5-flash.

Scoring is diagnostic rather than comparative — **no per-model performance table is reported**. Trajectories are labelled against **ARFT**, which organises **45 failure patterns** on two orthogonal axes: the lifecycle stage (A–F plus a cross-stage layer X) and a root-cause pillar, each pattern mapping to exactly one pillar — **R1 Grounding & Faithfulness (12 patterns)**, **R2 Cognitive Depth & Adaptability (13)**, **R3 Scientific Integrity & Alignment (13)**, **R4 Engineering Robustness (7)**.

Attribution is performed by an **agent-as-a-judge** pipeline calibrated on **50 validation trajectories**, reaching **κ = 0.75** at the pattern level and **κ = 0.83** at the taxonomy level, against **κ = 0.53 / 0.62** for a single-call LLM-as-a-judge baseline, with a **+17.2** recall gain at the pattern level. Across the 800 analyses the annotation records **12,712 total pattern hits**; the single most frequent pattern, **F.4 (uncorrected self-awareness), appears in 82.5%** of analyses, and the three cognitive pillars R1–R3 account for **92.1%** of all hits.

## Typical Duration

Fixed wall-clock and token budgets are applied per run, but the paper does not state their values. `TODO(reference)` — the specific budgets are not reported.

## Main Contribution

A shift from scoring autonomous research agents to diagnosing them: a lifecycle-spanning task set, an empirically derived failure taxonomy with root-cause attribution, and a validated judge that makes trajectory-level annotation affordable — yielding the finding that the same failure patterns recur across all eight configurations including the strongest models, which locates the deficit at the model level rather than in any particular scaffold.

## Key Design Ideas

- Tasks are organised by research lifecycle stage rather than by capability, so a failure can be attributed to where in the research process it occurred.
- ARFT's two-axis structure separates *where* a failure happened (stage) from *why* (root-cause pillar), and each pattern is forced to exactly one pillar so hit counts remain interpretable.
- The judge reads complete trajectories and intermediate artifacts rather than final outputs, which is what makes process-level attribution possible.
- Judge calibration is reported against human annotation with a same-task LLM-as-a-judge control, so the gain from artifact-aware judging is isolated rather than asserted.
- Holding the task set fixed while varying eight harness–model pairs is what licenses the model-level conclusion: a scaffold-specific deficit would not recur across all of them.
- The paper marks the limit of its own inference, stating that whether orchestration-level interventions could close the metacognitive gap is an open question this work does not test.

## Strengths

- Diagnostic depth is unusual at this scale: 800 fully annotated trajectories with artifact-level visibility, rather than aggregate scores over a larger task set.
- The failure taxonomy is derived from observed trajectories rather than posited in advance, and its category sizes are reported.
- The judge is calibrated against humans with a control condition, and the recall gain over the baseline is quantified.
- Varying harness and model together across eight configurations supports a claim about where the deficit lives that a single-configuration study could not make.
- The authors state plainly what their design cannot establish, separating the model-level attribution they support from the orchestration question they did not test.
- Task selection funnels 5,878 candidates to 100, so the retained set reflects explicit filtering rather than convenience.

## Limitations

- No repository URL appears in the main text despite the stated public release, so the artifact is not currently locatable (recorded above as `TODO(reference)`).
- Per-domain task counts are not given numerically, which prevents assigning the work to any domain page and makes the "seven scientific domains" claim unverifiable in detail.
- No comparative performance table is reported, so the work cannot be used to rank systems — by design, but it limits reuse as a leaderboard.
- ARFT is grounded in eight systems, and the authors note the patterns may not exhaust the failure space.
- Fixed wall-clock and token budgets mean resource pressure cannot be separated from failure causation.
- The authors state that data contamination cannot be fully excluded despite de-identification, a risk shared with other benchmarks built on real published science.
- Judge agreement is reported in aggregate only; the authors state that per-pattern and per-pillar agreement is not reported at this time.

## Related Works

- [AutoResearchBench](./autoresearchbench.md) — Also evaluates end-to-end autonomous research, scoring outcomes where AutoResearchEval annotates process.
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](./ara-survey.md) — Surveys the same class of systems along a verifiability axis, and supplies the framing this work's failure taxonomy fills in empirically.
- [Beyond Final Scores](./beyond-final-scores.md) — The same "final scores hide the process" argument applied to long-horizon AI R&D, using deterministic rule-based process metrics rather than a judge.
- [Replica](./replica.md) — Narrows the target to reproducing one redacted figure, trading lifecycle coverage for a checkable end state.
- [ScienceAgentBench](./scienceagentbench.md) — Task-level scientific agent evaluation with per-task validated outputs, complementary to trajectory-level failure attribution.
