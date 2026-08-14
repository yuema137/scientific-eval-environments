# SkillCoach (2026)

> **English** | [简体中文](../zh/works/skillcoach.md)

## Overview

SkillCoach is a self-evolving rubric framework for process-level evaluation of agentic skill-use: it derives skill-grounded rubrics from real rollouts and scores trajectories along four dimensions — skill selection, skill following, skill composition, and skill-grounded reflection — while keeping the external verifier as a separate outcome signal.

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent-skill evaluation methodology; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2607.01874>
- **Venue:** arXiv preprint, 2026

## Summary

The motivating observation is that in realistic skill repositories, overlapping skills make reliable skill-use hard, and final verifier success is too coarse a signal: an agent can pass by trial and error while selecting distractor skills, skipping required steps, composing workflows incorrectly, or omitting final checks. SkillCoach builds an initial rubric from the task instruction, the gold skills, and oracle solutions, then evolves it against real rollouts under a validation gate. Because process quality is scored separately from the outcome verifier, accidental task success can be told apart from correct procedure — and the evolved rubrics are reused as process supervision to select training trajectories.

## Tasks

Experiments use skill-dependent tasks filtered from existing skill benchmarks (SkillsBench and SkillLearnBench) by skill-dependency thresholds: 18 training task families and 10 held-out test task families, 28 families in total. Per-family instance counts are TODO(reference).

## Domains

General agent-skill repositories with overlapping and distractor skills. No canonical science or engineering domain is targeted.

## Evaluation

- **Skill selection** — set-level F1 between the skills the trajectory actually reads and the gold skill set, penalising both missed required skills and selected distractors.
- **Skill following** — a weighted sum over key steps, each credited only when its completion is supported by visible trajectory evidence.
- **Skill composition** — scored against precedence dependencies stating which step or skill must be completed before which.
- **Skill-grounded reflection** — whether expected checks were performed, such as validating output files, schemas, formats, or task-specific constraints.
- Rubric evolution is validation-gated: a separate arbitration model proposes a local patch, and the patch is accepted only if it does not reduce coverage, improves quality above a threshold, and changes at least one matched item. The arbitration model cannot inspect validation rollouts, accept its own patch, bypass the verifier, or delete critical key steps.
- **Reported.** Rubric evolution raises gold-keypoint coverage from 71.56 to 83.70, drives the hallucination rate from 2.00 to 0.00, and raises filtering consistency from 82.00 to 96.00. Using the evolved rubrics to filter SFT trajectories lifts Qwen3.5-9B final accuracy from 14.0% to 32.0%, against 18.0% for outcome-only filtering.

## Typical Duration

N/A — no per-task step, time, or token budget is reported.

## Main Contribution

Making process quality in skill-use measurable independently of outcome success, by inducing skill-grounded rubrics from rollouts under a validation gate rather than hand-writing them, and showing that the resulting process signal is a stronger training filter than terminal accuracy.

## Key Design Ideas

- Rubrics are derived from real rollouts rather than authored once, so they track the failure modes that actually occur.
- The external verifier is deliberately kept outside the rubric, so process score and outcome score can disagree.
- Four dimensions chosen to match distinct failure modes of skill-use rather than a generic quality scale.
- Evidence extraction from the trajectory (skill reads, gold and distractor signals, tool calls, file edits, script executions) grounds each rubric judgement in something observable.
- Structural safeguards on rubric evolution — the arbitrator cannot see validation rollouts or self-accept — to keep the rubric from drifting toward whatever the current agent does.

## Strengths

- The rubric artifact itself is validated (coverage, hallucination, filtering consistency), not merely assumed useful.
- Distractor-scaling analysis probes the realistic-repository condition directly; high-similarity distractors are reported to reduce GPT-5.5 selection F1 from 0.84 to 0.59.
- Demonstrates a downstream use for the evaluation signal, closing the loop from measurement to trajectory selection.

## Limitations

- Experiments cover a selected set of skill-dependent tasks from existing skill benchmarks; the authors note the scale remains smaller than production skill repositories.
- The training study is offline supervised fine-tuning only; no on-policy reinforcement learning or long-term deployment feedback is reported.
- No code or project URL is stated in the paper.
- Repository note: the paper's second half is a training contribution, which falls outside this repository's scope; the card covers the evaluation framework and the validation of the rubrics.
- Repository note: card compiled from the arXiv abstract and the v1 full text (August 2026); per-family instance counts and full result tables await direct validation.

## Related Works

- [SkillTV-Bench](./skilltv-bench.md) — Also evaluates judging of skill-augmented trajectories, treating the judge's skill knowledge as the measured object.
- [Skill-Use](./skill-use.md) — Shares the facet decomposition of skill-use (triggering, compliance, boundaries) but scores agents on a fixed suite rather than evolving rubrics.
- [AgentProcessBench](./agentprocessbench.md) — Also targets process-level rather than outcome-level judgement of agent trajectories.
- [SkillEvolBench](./skillevolbench.md) — Also derives a reusable artifact from rollouts, a skill library rather than a rubric.
- [SkillAudit](./skillaudit.md) — Also constructs evaluation material automatically around skills, per skill package rather than per rollout.
