# SkillGen (2026)

> **English** | [简体中文](../zh/works/skillgen.md)

> **First appeared:** 2026-05-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.10999)

## Overview

SkillGen is a method that writes one reusable natural-language skill for a base agent and accepts it only after a paired test. Summarizing trajectories into a skill gives no evidence that the skill helps, and an average accuracy gain can hide cases the skill breaks. SkillGen treats the skill as an intervention: it runs each verification instance with and without the skill, counts repairs (baseline fail, skill pass) and regressions (baseline pass, skill fail), refines the skill on that feedback, and deploys it only if the net gain clears a threshold. The accepted skills are then tested on held-out splits of 11 benchmarks with 8 base agents.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities


N/A — General-purpose skill-synthesis method across 11 mostly general agent benchmarks; the few science-grounded ones (ChemLLMBench, PubMedQA, ScienceWorld) are incidental test beds, not an evaluated scientific activity.

## Links

- **Paper:** <https://arxiv.org/abs/2605.10999>
- **Code:** <https://github.com/yccm/SkillGen>
- **Venue:** NeurIPS 2026 (stated in the official repository README)

## Summary

The base agent first runs on an induction subset, splitting its trajectories into successes and failures, and its no-skill outcomes are cached on a separate verification subset (70/30 split of the skill-training data). An auxiliary model (GPT-5.4-Mini) in induction, generation, and verification roles pairs each failure with its nearest same-task success, summarizes success patterns, failure modes, and contrastive observations, and writes a candidate skill with task context, success patterns, and failure-avoidance patterns. The verification agent reruns the verification subset with the skill and computes net gain G_m = n₀₁ − n₁₀; repairs, regressions, and unresolved failures become keep/remove/add/emphasize instructions for the next round. After up to eight rounds the best candidate by G_m is kept, and it becomes active only if G_m ≥ max{2, ⌈0.05·m⌉, 1}; otherwise the empty skill is deployed. Verification only covers the evaluated task distribution, so an accepted skill can still regress on shifted tasks.

## Tasks

N/A as a benchmark — SkillGen is a skill-synthesis method. Construction/test instance counts on the benchmarks used:

- τ-Bench retail 30/30; ALFWorld in-distribution 500/150 and out-of-distribution 500/255; ChemLLMBench property and yield 30/30; LiveCodeBench 50/150; MCPBench all-tools 64/40 and single-tool 40/16; Mind2Web 100/100; PubMedQA 150/100; ScienceWorld 150/100; SocialMaze FTS and UPI 60/50 each.
- Base agents in the main results: Gemma-4-26B, Llama-3.1-8B, Mistral-Nemo, Qwen-2.5-7B, Claude-Haiku-4.5, GPT-5.4-Nano, GPT-5.4-Mini, Grok-4-Fast.

## Domains

Mostly general-purpose agent environments (web, tool use, code, social reasoning, text-based embodied tasks). Some benchmarks are science-grounded: ChemLLMBench (chemical property and reaction-yield prediction), PubMedQA (biomedical question answering), and ScienceWorld (text-based science experiments).

## Evaluation

- **Inside the loop.** A trace for one verification instance: cached no-skill outcome = 0, skill-augmented outcome = 1 → counted in n₀₁ (repair). An instance with 1 → 0 is counted in n₁₀ (regression). The round's score is G_m = n₀₁ − n₁₀; Δ̂ = G_m / m. Up to 30 baseline-success guard checks are also run.
- **Held-out.** Accuracy on each benchmark's test split, reported as paired Δ (percentage points) against the same base agent without a skill.
- **Reported.** Average accuracy rises for all 8 base agents, from +3.27 pp (Gemma-4-26B, 58.49% → 61.76%) to +10.08 pp (GPT-5.4-Nano, 54.27% → 64.35%). Of 80 held-out benchmark–split–model entries, 50 improve, 25 are unchanged, and 5 regress.
- **Effect of selection.** The latest round-8 candidate averages Δ = −3.1 pp, while the best verified candidate reaches +8.1 pp.
- **Transfer.** Skills reused across models on ALFWorld OOD, ScienceWorld, Mind2Web, and SocialMaze FTS (100 held-out instances each): of 120 off-diagonal pairs, 70% are non-negative and 42% exceed +5 pp.
- **Baselines.** Trace2Skill, SkillX, EvoSkill, and CoEvoSkills, adapted to a single natural-language skill without tools, on ALFWorld IOD/OOD and ScienceWorld; per-method values appear only in a figure (TODO(reference)).
- **Ablations.** No refinement, no verification gate, no failure lessons, 3-shot ICL instead of a skill, and plain-text skill without scripts; the full system is reported best on every ALFWorld OOD and ChemLLMBench yield dataset–model pair (exact values TODO(reference)).

## Typical Duration

Skill construction averages 5.6M tokens, from 2.2M (ScienceWorld) to 10.2M (τ-Bench), about $8.2 per generated skill at GPT-5.4-Mini prices. Per-call input averages 3,589 tokens without a skill and 4,537 with one. Wall-clock time is not reported.

## Main Contribution

The authors frame a skill as an intervention whose effect is measured on matched instances, so that both repaired failures and broken successes are counted, and they use that paired measurement to refine, select, and gate skills synthesized from contrasted successful and failed trajectories.

## Key Design Ideas

- Contrastive induction pairs each failure with its nearest same-task success by embedding distance.
- Paired with/without-skill evaluation on cached baseline outcomes separates repairs from regressions instead of reporting one accuracy number.
- Best-of-K selection plus an acceptance threshold; a skill that does not clear it is replaced by no skill.
- Refinement instructions are built from the repair, regression, and unresolved-failure sets.
- A fixed auxiliary model writes skills for every base agent, so the base agent only performs rollouts.

## Strengths

- The gap between the last refinement round (−3.1 pp) and the verified best candidate (+8.1 pp) directly shows what the verification gate contributes.
- Covers 8 base agents, including small open models, across 11 benchmarks, and reports regressions explicitly.
- Reports construction cost in tokens and dollars.
- Code is public.

## Limitations

- Accepted skills can still overgeneralize; for example, Llama-3.1-8B on ALFWorld OOD drops from 67.45% to 65.10%.
- Verification covers only the evaluated task distribution; the authors recommend added safety evaluation and human review.
- Baselines were adapted to a single natural-language skill, which the authors note does not measure their native multi-skill capability.
- Reported failure modes include incomplete procedure execution in interactive tasks, wrong reaction-role grounding in chemistry tasks, and missing global structure in code tasks.
- Repository note: card compiled from the arXiv v1 abstract and HTML full text and the official repository README (November 2026); values shown only in figures are left as TODO(reference).

## Related Works

- [MIND-Skill](./mind-skill.md) — Also uses execution feedback to control skill generation, by reconstructing the source trajectory rather than comparing with/without-skill outcomes.
- [SkillEvolBench](./skillevolbench.md) — Compares skill conditions against no-skill controls on frozen deployment tasks, the same contrast SkillGen uses as its acceptance test.
- [SkillLearnBench](./skilllearnbench.md) — Benchmarks automatic skill-generation methods of the kind SkillGen implements.
- [SKILL-KD](./skill-kd.md) — Also accepts a skill edit only after rerunning the agent, using teacher–student trajectory contrast.
