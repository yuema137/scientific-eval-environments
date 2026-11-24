# MIND-Skill (2026)

> **English** | [简体中文](../zh/works/mind-skill.md)

> **First appeared:** 2026-05-09 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2605.08670)

## Overview

MIND-Skill is a skill-generation method that scores each written skill before trusting it. In a single-pass pipeline, an LLM reads one successful agent trajectory and writes a skill document, and nothing checks whether that document actually carries the procedure. MIND-Skill adds a second agent that must re-solve the same task in the live environment using only the task and the skill; three losses computed from that reconstruction (trajectory match, task outcome, and a documentation rubric) are fed back through TextGrad to rewrite the skill-writer's prompt. The resulting skills are then tested on held-out AppWorld and BFCL-v3 tasks.

## Topics


- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities


N/A — Skill-generation method evaluated on general app/API interaction and function calling (AppWorld, BFCL-v3); no scientific or research activity is evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2605.08670>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

An induction agent receives a task specification and a successful ReAct trajectory and writes a structured skill; its system prompt is the only optimized variable. A deduction agent, with a frozen prompt and no access to the original trajectory, re-executes the task in the environment from the task and the skill alone. Three textual losses then score the skill: an LLM judge compares the reconstructed and original trajectories at the tactic level (reconstruction loss, 0–10), the environment checks whether the reconstruction fails the task (outcome loss, 0–1), and an LLM judge rates the skill on five rubric dimensions (rubric loss, 0–10). A TextGrad gradient LLM turns the three feedbacks into an edit of the induction prompt, for 8 iterations per training task, keeping the best-so-far skill under lexicographic selection (outcome first, then reconstruction and rubric as tiebreakers). The method requires a successful trajectory per training task, so it cannot write skills for tasks the agent has never solved.

## Tasks

N/A as a benchmark — MIND-Skill is a skill-generation method. Its experiments use two existing benchmarks:

- **AppWorld** — 9 apps and 457 APIs; 90 training tasks used for skill extraction; evaluation on 168 Test-Normal and 417 Test-Challenge tasks.
- **BFCL-v3** (base multi-turn category) — 200 instances, randomly split into 50 training and 150 test instances.

At test time a retrieval LLM sees only each skill's name and description, selects the top K = 3 skills, and their full bodies are injected into the agent's context.

## Domains

General-purpose agent environments (app/API interaction and multi-turn function calling). No canonical science or engineering domain is targeted.

## Evaluation

Evaluation appears at two levels.

- **Inside the loop (skill quality).** For one training task, the induction agent writes skill *s* from trajectory τ; the deduction agent produces τ̂ from the task and *s*; the environment executes τ̂ and returns ℓ_outcome ∈ [0, 1] with execution feedback; an LLM judge returns ℓ_recon ∈ [0, 10] for tactic-level equivalence of τ̂ and τ; another LLM judge returns ℓ_rubric ∈ [0, 10] over ground-truth independence, actionability, transferability, completeness, and conciseness. These scores both drive the TextGrad update and select the kept skill.
- **Held-out (downstream).** AppWorld is scored with Task Goal Completion (TGC) and Scenario Goal Completion (SGC); BFCL-v3 with accuracy (ACC).
- **Reported (Qwen3.5-122B-A10B generating and using skills).** MIND-Skill reaches TGC 71.4 / SGC 55.4 on AppWorld Normal, TGC 51.8 / SGC 39.6 on AppWorld Challenge, and 77.3 ACC on BFCL-v3 (average 59.1), against ReAct 42.8, Skill-extract (single-pass induction) 51.0, ACE 56.1, and Trace2Skill 55.1 on the same average. With GPT-5.4 as skill generator the average is 58.9.
- **Loss ablation (AppWorld, Qwen).** Removing the outcome loss gives Normal TGC 68.5 / Challenge TGC 48.0; removing reconstruction gives 66.1 / 45.8; removing the rubric gives 64.3 / 46.5; the full method gives 71.4 / 51.8.

## Typical Duration

TODO(reference) — no absolute token, cost, or wall-clock figures are reported. Skill construction runs 8 TextGrad iterations per training task; the paper reports that injected skill tokens are 3–6× smaller than ACE's playbook and Trace2Skill's skill directory.

## Main Contribution

The authors frame skill writing as an optimization problem in which a skill's quality is measured by whether another agent can rebuild the original solution from it, combining reconstruction, outcome, and rubric losses into a closed loop that rewrites the skill-writer's prompt.

## Key Design Ideas

- Induction–deduction split: the agent that uses the skill never sees the trajectory it came from, so the reconstruction tests what the skill document alone conveys.
- Three complementary checks: environment execution (outcome), LLM-judged tactic equivalence (reconstruction), and LLM-judged documentation rubric.
- The optimized object is the induction prompt rather than individual skills; the gradient LLM sees the reconstruction but not the original trajectory.
- Lexicographic selection with outcome loss first and a tracked best-so-far skill, so later iterations cannot overwrite a better skill.
- The induction prompt explicitly sorts claims into procedural conventions to keep, instruction-inferable knowledge to suppress, and ground-truth leakage to suppress.

## Strengths

- Includes a single-pass ablation (Skill-extract, equal to iteration 0) so the gain from the evaluation loop is measured directly: +8.1 average points with Qwen-generated skills and +7.2 with GPT-5.4-generated skills.
- Each loss is ablated separately on both AppWorld splits.
- Reports both self-generated and cross-model (GPT-5.4 generator) settings.

## Limitations

- Requires successful trajectories as input, tying the skill library to tasks the agent can already solve; the authors note ground-truth solution scripts as a fallback.
- Two of the three losses are LLM-judged; the paper does not report validation of these judges against human ratings.
- Evaluated on two general-purpose agent benchmarks with one inference model (Qwen3.5-122B-A10B).
- Repository note: card compiled from the arXiv v1 abstract and HTML full text (November 2026); no code repository is linked from the paper.

## Related Works

- [SkillLearnBench](./skilllearnbench.md) — Benchmarks continual skill-generation methods and scores the generated skill itself, the quantity MIND-Skill optimizes.
- [SkillEvolBench](./skillevolbench.md) — Tests whether skills distilled from an agent's own trajectories hold up on shifted tasks, the transfer that MIND-Skill's held-out evaluation targets.
- [Skill Coverage](./skill-coverage.md) — Also checks a skill against agent trajectories, measuring which of the skill's constraints a trajectory exercised.
- [SkillGen](./skillgen.md) — Also gates skill generation on execution feedback, by paired with/without-skill comparison rather than trajectory reconstruction.
