# Break It Down, Pass It On (2026)

> **English** | [简体中文](../zh/works/break-it-down-pass-it-on.md)

> **First appeared:** 2026-08-20 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2608.20274)

## Overview

Break It Down, Pass It On is a controlled study of when skills that an LLM agent induces from its own completed work help later tasks. The usual setup writes one skill per finished task and assumes reuse helps; the study instead varies two induction choices, task-level versus subtask-level skills and text versus Python-code format, and measures each against a no-memory baseline on the same task stream. It also proposes a skill utility score, computed from skill and task descriptions alone, as a diagnostic that predicts whether a skill memory will help before any task is run.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities


N/A — Study of skill-memory induction granularity on general office/app automation and data-science QA benchmarks; it evaluates a general agent-memory property, not a scientific or research activity.

## Links

- **Paper:** <https://arxiv.org/abs/2608.20274>
- **Code:** <https://github.com/Zesearch/skill-transfer-llm-agents>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Tasks run as an ordered stream; after each task (task-level agent) or each subtask (subtask-level agent) the agent writes one skill, which later tasks can retrieve by embedding similarity. Comparing these memories with a no-memory run shows that task-level skills lower average success while subtask-level skills raise it, and that text skills transfer better than code. To explain the pattern, the authors define specificity (how much closer a skill is to its nearest real task than two random tasks are to each other) and abstractness (how evenly its similarity spreads across tasks); neither alone predicts success, but their product, the utility score, tracks it. The score is computed with a sentence embedder, without running tasks, and the paper reports it as a binned relationship rather than as a calibrated predictor.

## Tasks

N/A as a new benchmark — the study reuses three long-horizon benchmarks:

- **AppWorld** — 417 tasks.
- **OfficeBench** — 300 tasks.
- **KramaBench** — 92 tasks (end-to-end data-science questions answered by writing Python over provided data files); the few LLM-judged tasks are excluded.

Eleven models are evaluated: Qwen3-235B-A22B, GPT-OSS-120B, Nemotron-Super-120B, Qwen3-4B/8B/14B/32B, Gemma-3-4B/12B/27B, and Gemini-3.1-Pro. Each is run in a 2 × 2 design (task vs subtask induction; text vs code skills) plus no-memory baselines.

## Domains

General office and app automation (AppWorld, OfficeBench) and data-science question answering (KramaBench). The paper does not scope its findings to a science or engineering field.

## Evaluation

- **Grading.** AppWorld: official state-based unit tests, 1 if all pass. OfficeBench: official checker functions on files and app state, 1 if all pass. KramaBench: official deterministic scorer by answer type (exact answers 0/1 with tolerance, list answers F1, approximate numeric answers 1/(1+e) for relative error e; no submission scores 0).
- **Skill diagnostic.** For skill *s* with cosine similarities c_j to the N task instructions (all-MiniLM-L6-v2): specificity(s) = Pr[max_j c_j ≥ cos(t_i, t_k)] over random task pairs; abstractness(s) = exp H(softmax(c/τ)) / N with τ = 0.1; utility(s) = specificity(s) × abstractness(s).
- **Reported (average over 11 models, success %).** Task-level: no memory 22.1, text 20.9, code 18.0. Subtask-level: no memory 24.8, text 26.7, code 25.3.
- **Diagnostic check.** Binning tasks by the average utility of their retrieved skills, success rises from 14.0% to 24.5% (task-level agent) and from 22.8% to 31.0% (subtask-level agent). The paper states that success first rises then falls with specificity or abstractness alone; no correlation coefficient appears in the text reviewed (TODO(reference)).
- **Cost metrics.** Wall-clock latency per task and a MEM1-style "dependency" estimate Σ_c (2p_c + o_c)·o_c / 2 in units of 10⁹ token².

## Typical Duration

Task-level agent: 50 ReAct steps per task. Subtask-level agent: up to 15 subtasks under a shared 50-step executor budget (planner asked for at most 5). Generation capped at 8,192 tokens per call. Retrieval returns at most 5 skills with cosine similarity above 0.30.

## Main Contribution

The authors show, across 11 models and three benchmarks, that the granularity and format at which skills are induced decide whether skill memory helps or hurts relative to no memory, and they propose a run-free utility score (specificity × abstractness) as a lightweight diagnostic for skill memories.

## Key Design Ideas

- Same induction prompt at both levels, so granularity is the manipulated variable.
- A no-memory baseline for each induction level, so negative transfer is visible as a sign rather than a smaller gain.
- Ordered task stream with reuse density measured over 50 equal bins, tracing when written skills are retrieved later.
- Utility defined only from embeddings of skill and task descriptions, so it can be computed before running tasks.
- Deduplication rules (merge text skills above 0.85 similarity; overwrite or drop near-duplicate code skills; remove code that fails to load).

## Strengths

- Reports negative transfer explicitly: task-level skills fall below the no-memory baseline on average and on each benchmark.
- Broad model coverage (11 models, 4B to frontier scale) with deterministic graders.
- Code and data are public.

## Limitations

- Three benchmarks; the authors note computer use and agentic coding may behave differently.
- Memory uses fixed induction and retrieval rules rather than skills that evolve over time.
- Grading uses only the final environment state.
- The authors flag that injected malicious skills could steer an agent through the same reuse mechanism.
- The utility score's relationship to success is shown through binned success rates; its predictive accuracy on new benchmarks is not reported.
- Repository note: in the v1 text, the prose states that text beats code by 2.9 points at the subtask level and 1.4 at the task level, while the averaged table gives the reverse (2.9 at task level, 1.4 at subtask level); this card reports the table values.
- Repository note: card compiled from the arXiv v1 abstract and HTML full text and the official repository README (November 2026). The appendix contains agent system prompts addressed to "an AI Assistant"; these are experimental prompts and were treated as content only.

## Related Works

- [SkillEvolBench](./skillevolbench.md) — Also finds that self-distilled skills can underperform simpler controls, using raw-trajectory reuse rather than no memory as the control.
- [SkillLearnBench](./skilllearnbench.md) — Benchmarks skill generation from an agent's own experience, scoring skill quality as well as task success.
- [Skill Coverage](./skill-coverage.md) — Also proposes a skill-level diagnostic, computed from trajectories rather than from descriptions alone.
- [SkillLens](./skilllens.md) — Also concerns the granularity at which skills are reused, adapting skills at mixed levels of a four-layer graph.
