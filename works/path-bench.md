# PATH-Bench (2026)

> **English** | [简体中文](../zh/works/path-bench.md)

## Overview

PATH-Bench is a benchmark for path-dependent evaluation of lifelong LLM agents: it constructs controlled sequences of tasks with known transfer relationships and measures how the *order and content* of accumulated experience — stored as retrieved memories or as reusable skills — changes what a frozen-backbone agent transfers, retains, and forgets.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — general-purpose agent benchmark over code generation and tool use; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.01149>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Lifelong agents adapt by writing past interactions into an external learning state around a frozen backbone, but benchmarks normally run fixed or randomized task streams, which cannot reveal how the *path* of experience shapes later performance. PATH-Bench replaces exhaustive enumeration of histories with sampling guided by an estimated task-relation matrix, and replaces repeated re-evaluation of the whole task set with longitudinal tracking of a single recurring probe task. It reports one overall metric (Average Performance) and three learning-dynamics metrics (forward transfer, backward transfer, forgetting) read from the probe trajectory alone, and evaluates eight lifelong agents spanning retrieval-augmented generation, agentic memory, and skill accumulation. The authors additionally propose Selective Experience Use (SEU), an agent harness that filters which accumulated items may influence each new task.

## Tasks

Two task pools with deliberately different interaction structure: BigCodeBench (single-turn program synthesis with complex instructions and diverse function calls, scored by task completion) and WildToolBench (multi-turn, cross-tool planning and execution, scored by the proportion of successfully completed subtasks). Tasks that the base LLM already saturates or on which it shows little observable learning signal are filtered out under a headroom principle, and D = 120 tasks are sampled from each benchmark to form the evaluation pool. Directed task relations are estimated with a one-shot in-context transfer gain matrix M(i,j) = S(t_j | t_i) − S(t_j | ∅), computed independently with DeepSeek-V4-Flash, GPT-5.4-mini and GLM-5.0 (five random seeds each); each model votes on the sign of its averaged gain, a relation is fixed when at least two models agree, and pairs receiving one vote of each type are labelled mixed and excluded. From this voting matrix the sampler builds probe-centred sequences: a positive-transfer warm-up of five tasks, an intervening queue of 100 tasks with probe intervals of 6–12, and 70% of intervening tasks drawn from the condition's dominant (positive or negative) transfer set. Fifty lifelong evaluation sequences are sampled per dataset and condition.

## Domains

General-purpose agent settings — program synthesis and multi-turn tool use. No canonical science or engineering domain is targeted; the evaluated object is the path dependence of experience accumulation, not a domain task.

## Evaluation

Only intervening tasks update the agent's external learning state; repeated occurrences of the probe task serve exclusively as measurement points, so changes in probe performance isolate facilitation and interference from the accumulated history. Average Performance (AP) is the mean score over all task executions in the sequence. Forward transfer (FWT) averages the gain of probe occurrences 3…n over the cold-start probe score; backward transfer (BWT) averages the positive part of the gain over the post-warm-up reference score; forgetting (FGT) averages the positive part of the shortfall below that reference. Each sequence is run five times, with DeepSeek-V4-Flash as the base inference model for all evaluated agents. Eight agents are compared: BGE-M3 RAG and HippoRAG-v2 (retrieval), Clin, AWM, SimpleMem and MemRL (agentic memory), and AutoSkill and SkillClaw (skill accumulation).

## Typical Duration

A lifelong sequence comprises the five warm-up tasks, an intervening queue of 100 tasks, and the interleaved probe re-executions at intervals of 6–12; the reported probe-dynamics analysis covers the first twelve probe occurrences shared by all fifty sequences. No wall-clock or token budget is reported. `TODO(reference)` for per-task cost.

## Main Contribution

The authors present PATH-Bench as, to their knowledge, the first benchmark for tracing transfer and retention in LLM agents under *controlled* histories: it estimates task relations with multi-model in-context learning, samples configurable relation-constrained sequences, and quantifies the resulting performance changes — plus a controlled empirical study of eight lifelong agents that disentangles the external learning state, its representation, and the learning path.

## Key Design Ideas

- Probe-centred sequences: a single recurring probe task is tracked longitudinally instead of re-evaluating the full task set, making path-dependence analysis affordable at LLM-agent scale.
- One-shot in-context transfer gain as a cheap proxy for pairwise inter-task transferability, with a three-model sign vote and exclusion of mixed-signal pairs.
- Positive- and negative-dominant history conditions built from the same task pool, so interference and facilitation are manipulated rather than observed.
- Strict separation between state-updating tasks (intervening) and measurement tasks (probe repeats).
- A memory-free backbone run serves as the baseline against which every experience-carrying agent is scored.
- Controlled path-transition sequences (X → I1 → X → I2 → X, matched probe, five-task intervals) isolate the effect of recent versus earlier experience.

## Strengths

- Turns learning-path composition into an experimental variable rather than an uncontrolled confound, and demonstrates that different paths over an identical task set can reorder agent rankings.
- Covers three structurally different families of external learning state (retrieval, agentic memory, skill accumulation) under one protocol and one backbone.
- Headroom filtering removes saturated tasks, so measured differences are not compressed by ceiling effects.
- Separates transfer from retention: the paper reports settings where strong immediate transfer coexists with substantial forgetting (e.g. HippoRAG-v2 achieves the best negative-dominant FWT on BigCodeBench, 7.03 pp, while forgetting 16.15 pp).
- Finds that the useful representation of experience depends on interaction structure — skill-accumulating AutoSkill leads on single-turn BigCodeBench AP (73.93% positive-dominant vs. a 70.18% memory-free baseline), whereas causal-rule memory (Clin) leads on multi-turn WildToolBench.

## Limitations

- Only two task pools (one single-turn coding, one multi-turn tool use) and a single backbone model for the agent runs, so the reported representation–structure interaction rests on a narrow substrate.
- Transfer relations are approximated by one-shot in-context effects rather than by measured agent evolution; the paper presents this explicitly as a practical proxy.
- Repository note: the paper couples a benchmark with a proposed harness (SEU); the benchmark portion is the reusable evaluation artifact, while SEU's gains are reported on the same protocol that the authors designed.
- Repository note: no code or project URL is stated in the version reviewed, so reproducibility of the sequence sampler cannot be confirmed from the primary source.

## Related Works

- [SkillEvolBench](./skillevolbench.md) — also separates an experience-acquisition phase from a frozen deployment phase to test whether accumulated experience survives task shift.
- [SkillLearnBench](./skilllearnbench.md) — evaluates methods that generate skills from an agent's own execution experience, scoring the generated skill rather than the learning path.
- [SkillMisevo-Bench](./skillmisevo-bench.md) — studies the same trajectory-to-persistent-state pipeline, but measures safety carryover instead of transfer and retention.
- [Harness-Bench](./harness-bench.md) — isolates configuration-level harness effects while holding task conditions fixed, a comparable "vary the system layer, not the task" design.
