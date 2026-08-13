# AI Cosplaying as Astrophysicists: A Controlled Synthetic-Agent Study of AI-Assisted Astrophysical Research Workflows (2026)

> **English** | [简体中文](../zh/works/ai-cosplaying-as-astrophysicists-a-controlled-synt.md)

## Overview

A controlled evaluation study in which LLM-simulated astrophysics researchers complete everyday astrophysics
research assignments under five different AI-assistance policies, producing 12,960 rubric-scored episodes
that measure where assistance helps, where it is neutral, and where it raises the rate of confident but wrong
results.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)
- [Literature Search & Evidence Synthesis](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** https://arxiv.org/abs/2603.29039
- **Code:** https://github.com/ChunHuangPhy/agent_astro

## Summary

The study replaces human subjects with role-conditioned LLM "synthetic researchers" so that the same
assignment can be run under every assistance policy with everything else held fixed, which is not possible in
a human trial. Each episode pairs a researcher persona with an astrophysics task and an assistance policy,
and an LLM judge grades the output against a family-specific rubric on task quality, completion, and
catastrophic failure. The headline result is that no assisted policy universally beat unassisted work in the
primary run, and that derivation-and-reasoning tasks became markedly more fragile under assistance. The whole
protocol was re-run with a different actor model to test how much of the map is model-specific.

## Tasks

A released bank of 3,000 astrophysics tasks organised into six workflow families of 500 tasks each: writing
and editing (for example rewriting an urgent X-ray follow-up request while preserving scientific rigour),
extraction and synthesis (summarising revision changes from inference outputs), code debugging (identifying
unit mismatches such as arcmin versus arcsec in a catalog cross-match), derivation and reasoning (computing
Eddington ratios from black hole masses and luminosities), creative problem solving (advising on follow-up
strategy for a transient candidate), and verification and critique (weighing a new-physics claim against a
systematics explanation). Each task carries metadata for difficulty (0.22–0.63), verifiability (0.68–0.96),
and ambiguity (0.12–0.46). 2,592 distinct assignments were drawn from this bank; each was executed under all
five assistance policies, giving 12,960 scored episodes (144 personas × 18 tasks each × 5 policies). The 144
personas are defined by career stage (early graduate student, late graduate student, postdoc, faculty), AI
awareness (three levels), and verification willingness (three levels).

## Domains

Astronomy is the sole domain. The task bank is drawn entirely from astrophysics research practice and spans
exoplanets, stellar astrophysics, galaxies, active galactic nuclei, high-energy phenomena, cosmology, compact
objects, gravitational waves, and instrumentation; the concrete task examples are astronomical throughout
(X-ray follow-up requests, Eddington-ratio derivations, catalog cross-match debugging, transient follow-up
strategy).

## Evaluation

Each episode is graded by an LLM judge against a rubric specific to its task family: preservation of
scientific meaning for writing, retention of operational content without fabrication for extraction, correct
algebra, arithmetic and units for derivation, concrete next steps rather than vague advice for creative
problem solving, identification of real inferential gaps rather than repetition for verification, and valid
bug repairs for code. The judge emits a continuous task score on [0,1], a binary success indicator, a binary
catastrophic-failure flag for severe but fluent reasoning errors, and verification notes that must describe
checks actually performed rather than generic caution. The primary outcome is a composite utility
`U = 0.55 × task_score + 0.25 × completion − 0.35 × catastrophic_failure + 0.10 × (0.5 − difficulty) +
0.05 × b_policy`, where the policy bonus (0.03–0.12) credits speed differences. The five compared policies
are solo, cautious_assisted, low_verification, verification_heavy, and overtrusting. The production run used
Qwen 3:8B as both actor and judge; a replication swapped the actor to DeepSeek-R1:8B with the judge held
constant. In the Qwen run mean utility was essentially neutral (+0.0017, 95% CI [−0.0042, +0.0077]) while
catastrophic failure rose by +0.0112 (95% CI [+0.0050, +0.0174]); derivation and reasoning was the fragile
family (−0.0832 utility, +0.0648 catastrophic failure), and creative problem solving benefited most (+0.047
utility). The DeepSeek replication instead showed a clear positive utility gain (+0.0184, 95% CI [+0.0113,
+0.0255]) with the derivation fragility largely gone.

## Typical Duration

`TODO(reference)` — episodes are single-pass with extended reasoning mode disabled, but no per-episode step,
wall-clock, or token budget is reported.

## Main Contribution

The author frames the work as a numerical protocol for estimating matched within-task contrasts between
assistance policies under fixed and auditable conditions — a controlled substitute for a human productivity
trial — together with the released astrophysics task bank, episode dataset, and reproduction scripts.

## Key Design Ideas

- Matched within-task contrasts: the same assignment is run under all five assistance policies, so policy
  effects are not confounded by task difficulty.
- Researcher personas parameterised on three explicit axes (career stage, AI awareness, verification
  willingness) so that assistance effects can be broken down by user type rather than averaged away.
- A catastrophic-failure channel separate from task score, targeting fluent-but-wrong outputs that a mean
  quality score would hide.
- Verification notes required to describe concrete checks performed, which prevents an agent from scoring on
  performative caution.
- A full actor-swap replication with the judge held fixed, which distinguishes stable qualitative patterns
  from model-specific rankings.
- Task metadata for difficulty, verifiability, and ambiguity, enabling stratified analysis.

## Strengths

- Evaluation is the entire contribution, with a released 3,000-task astrophysics bank, all 12,960 scored
  episodes, and reproduction scripts.
- The actor-swap replication is run and reported rather than left as future work, and it reverses the
  headline sign — an unusually honest robustness check.
- Confidence intervals are reported for every headline effect.
- Family-level breakdown localises the risk to derivation and reasoning rather than asserting a global claim.

## Limitations

- The subjects are LLM simulations of researchers, not researchers; the author states the paper does not
  measure human astrophysicist productivity.
- Both actor models are 8B-class (Qwen 3:8B, DeepSeek-R1:8B) with extended reasoning disabled, so the results
  do not speak to frontier-scale assistance.
- The judge is an LLM and, in the primary run, the same model family as the actor.
- The utility metric's weights and the definition of catastrophic failure are design choices the author
  acknowledges could change the quantitative details.
- The author notes that most quantitative rankings are model-dependent, and the two runs disagree on the
  overall sign of the assistance effect.
- Repository note: single-author preprint with no venue verified at time of carding; the tasks are executed
  under a fixed single-pass protocol without literature search, code execution, or iterative revision, so it
  measures assisted single-turn output quality rather than agentic research workflow.

## Related Works

- [Stargazer](./stargazer.md) — astronomy research agent evaluation on concrete astronomical analysis tasks.
- [ReplicationBench](./replicationbench.md) — evaluates agents on reproducing astrophysics paper results.
- [The Replay Gap](./the-replay-gap.md) — another study whose contribution is evaluation methodology rather
  than a task suite.
- [VESTA / DAWN](./vesta-dawn.md) — astrophysical model-fitting evaluation, a task-level complement to this
  workflow-level study.
