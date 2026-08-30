# Skill²-Bench (2026)

> **English** | [简体中文](../zh/works/skill2-bench.md)

> **First appeared:** 2026-08-05 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.05139)

## Overview

Skill²-Bench is a benchmark of *cross-skill long-horizon tasks* — multi-step problems whose consecutive steps require different reasoning skills and depend on earlier answers — calibrated by **skill entropy**, a directed pairwise measure of how hard it is to switch from one skill to another. It is introduced together with Skill-Entropy RL, a training method that reuses the same measure as a reward signal.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose cross-skill reasoning benchmark; math, science and coding items are seed material rewritten into synthetic scenarios to measure skill switching, not evaluated as scientific or research tasks in their own right.

## Links

- **Paper:** <https://arxiv.org/abs/2608.05139>
- **Code:** <https://github.com/Gen-Verse/Skill-Entropy-RL>
- **Venue:** arXiv preprint (cs.CL / cs.LG), 2026

## Summary

Frontier models often do well on single-skill benchmarks yet remain brittle when one reasoning chain must move between skills — a math derivation whose result feeds a scheduling step, which in turn guides an extraction step. The authors formalize such problems as cross-skill long-horizon tasks and define skill entropy SkE(s_a, s_b) as a smoothed ratio between average single-skill accuracy and cross-skill accuracy under a fixed reference model, with values above 1 meaning the switch is hard. Task-level skill entropy averages the pairwise values along a task's skill sequence and is used to sample tasks at low, medium and high difficulty levels. Evaluating eight frontier and four open-source models exposes a skill-switching gap that single-domain evaluations do not surface, after which the same quantity is converted into a reward for Skill-Entropy RL.

## Tasks

A skill bank of 558 labelled skills across nine domains — six verifiable (math 186, science 137, coding 46, logic 14, information extraction 92, planning 34) and three open-ended (creative writing 12, context retrieval 12, instruction following 25) — is built by prompting an LLM to annotate 3–5 fine-grained skills on each seed question, clustering the labels by embedding, and manually reviewing each cluster so that skill granularity is comparable across domains. Seed datasets are OpenR1-Math, MMLU-Pro, LiveCodeBench, ZebraLogicBench and Guru-RL-92k, WikiTable and WebSRC, and NaturalPlan; the three open-ended domains have their skill lists generated directly. Each task is a length-L sequence (L ∈ [2, 10]) of question–answer pairs in which consecutive steps come from different domains: a skill sequence is sampled at a target skill-entropy level, one seed question–answer pair is drawn per skill, and an LLM *proposer* fuses them into a single coherent scenario in which each step depends on the preceding answer, after which a separate *verifier* filters out tasks failing its checklist. The reported evaluation uses a held-out test set of 300 cross-skill tasks balanced across the three skill-entropy levels and the nine domains.

## Domains

Nine general reasoning domains, of which "science" is drawn from MMLU-Pro and "math" from OpenR1-Math. No canonical science or engineering domain is assigned: the evaluated objective is the difficulty of switching between skills, and the domain-specific items serve as calibrated substrate rather than as the target of measurement.

## Evaluation

Each domain has its own scorer eval_d: (â, a, q) → [0, 1] — for example symbolic equivalence for math and sandboxed unit-test execution for coding — while open-ended steps are graded in [0, 1] by an LLM judge (Claude-opus-4.7) against a rubric. A task's score is the average of its per-step scores, and Skill²-Bench performance is a model's average per-step score. Every model is queried in two modes: a *single-skill* mode that asks each step in isolation, and the *cross-skill* mode that presents the full long-horizon task and requires answers in order; the difference between the two isolates the switching cost. Sampling is four times at temperature 0.7. Skill entropies are derived once with Claude-opus-4.7 as the fixed reference model (Laplace smoothing α = 0.1) so the difficulty scale is held constant across evaluated models. Eight frontier models (Claude-haiku-4.5, Claude-sonnet-4.5, Claude-opus-4.7, Gemini-3.1-flash, Gemini-3.1-pro, GPT-5.4-mini, O4-mini, GPT-5.5) and four open-source models (Qwen3-4B, Qwen3-8B, Qwen3-32B, Olmo-3-7B-Think) are evaluated.

## Typical Duration

Tasks run 2 to 10 dependent steps in a single reasoning chain; no wall-clock or token budget per task is reported. `TODO(reference)` for cost.

## Main Contribution

The authors formalize cross-skill long-horizon tasks, introduce skill entropy as a directed pairwise measure of switching difficulty, release Skill²-Bench as a skill-entropy-calibrated benchmark over 558 skills and nine domains, and show that the same measure converts into a training reward (Skill-Entropy RL) that transfers to unseen domains.

## Key Design Ideas

- Difficulty is defined by *transitions*, not by surface features: two tasks of the same length and skill set can differ greatly in how hard their switches are.
- Skill entropy is directional — SkE(s_a, s_b) and SkE(s_b, s_a) are computed on different two-step pairs and generally differ.
- A single fixed reference model derives all skill entropies, so the difficulty scale does not move when a new model is evaluated.
- Paired single-skill and cross-skill querying separates switching cost from per-skill competence.
- Proposer–verifier construction: an LLM fuses seed questions into one scenario with cross-step dependencies, and a checklist verifier discards tasks that fail it.
- Skill labels are made explicit at inference time in the training half, letting the reward grade the predicted skill chain against the gold chain.

## Strengths

- Provides a quantitative, model-independent difficulty scale for skill composition rather than an ad-hoc "hard/easy" split, and shows accuracy decreases nearly monotonically as task-level skill entropy rises.
- Reuses established, verifiable seed datasets with domain-appropriate automatic scorers, limiting reliance on LLM judging to the three open-ended domains.
- Reports that accuracy drops by roughly 4 to 13 points when a skill is exercised inside a cross-skill task rather than as a single-skill question, isolating a gap that per-domain leaderboards hide.
- Finds that per-domain skill entropy is largely decoupled from per-domain difficulty — science is an easy domain with the highest switching entropy — which is a non-obvious empirical result about where composition breaks down.
- Identifies a concrete dominant failure mode: at later steps models reuse the previous step's skill and answer modality instead of switching.

## Limitations

- Tasks are synthetically fused from seed questions by an LLM proposer, so ecological validity depends on the proposer and the verifier checklist rather than on naturally occurring multi-skill workloads.
- Skill labels themselves are LLM-generated and clustered, with manual review only at the cluster level; skill granularity across the 558 skills is therefore approximate.
- Skill entropy is approximated in practice by skill-to-domain switches rather than by every skill pair.
- Repository note: the paper is half evaluation and half training contribution; the reported Skill-Entropy RL gains (34.4% → 68.4% on Qwen3-4B-Instruct, 14.6% → 40.1% on Qwen3-1.7B) are measured on the authors' own benchmark, so benchmark and method share a design.
- Repository note: it evaluates model reasoning chains, not agents acting in an environment — there is no tool use, no external state, and no recovery from failed steps.

## Related Works

- [Skill-Use](./skill-use.md) — also decomposes skill competence into separable facets, but for executing authored skills rather than switching between reasoning skills.
- [T-Eval](./t-eval.md) — earlier capability-subprocess decomposition, scoring six tool-use subprocesses on isolated tasks.
- [SkillSV](./skillsv.md) — treats a skill's internal structure as the unit of analysis, assigning structure-aware value to its parts.
- [AgentBoard](./agentboard.md) — long-horizon evaluation with per-subgoal progress, a complementary way of exposing where a multi-step chain breaks.
