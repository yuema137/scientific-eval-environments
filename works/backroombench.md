# BACKROOMBench (2026)

> **English** | [简体中文](../zh/works/backroombench.md)

> **First appeared:** 2026-07-29 · **Source:** [arXiv initial submission](https://arxiv.org/abs/2607.27484)

## Overview

BACKROOMBench is a verified testbed, built on the BACKTRACE evaluation framework, that measures whether a skill-augmented language agent's *stated* skill use matches the skill's *intervention-measured* causal influence on its answer.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — evaluation-methodology work; the logic and mathematics items serve as a controlled substrate for measuring skill provenance, and no scientific or research activity is itself the evaluated object.

## Links

- **Paper:** <https://arxiv.org/abs/2607.27484>
- **Venue:** arXiv preprint (cs.AI, cs.MA), 2026

## Summary

Evaluators of skill-augmented agents normally infer skill use from the agent's visible reasoning or from its own self-attribution, but those signals report what the agent *appears* to use rather than whether the skill changed the decision. BACKTRACE closes that gap by pairing every skill-conditioned answer with a matched no-skill counterfactual, intervening on the skill's meaning, wording, identity, content, and assignment, and eliciting the agent's attribution only after the answer has been committed. BACKROOMBench instantiates the framework over controlled logic and competition mathematics, across single-agent and multi-agent settings and several model families. The authors name the resulting phenomenon the *Reasoning Backroom*: a systematic divergence between stated skill use and measured causal reliance.

## Tasks

583 instances in total: 300 controlled PrOntoQA-style logic problems and 283 natural MATH-500 problems. Each item is run under seven skill conditions — none (baseline), correct, paraphrase, misleading, name swap, content swap, and irrelevant — so that intervention on skill meaning, wording, identity, content, and assignment can be separated. Twelve models are evaluated on the logic split (Qwen2.5-Instruct 7B/14B/32B, DeepSeek-R1-Distill-Qwen 7B/14B/32B, GPT-4.1 nano/mini, GPT-5 nano/mini, GPT-5.4 nano/mini), with a six-model intersection carried through the mathematics split. Multi-agent configurations are evaluated in addition to single-agent ones.

## Domains

No canonical science or engineering domain is assigned. The two task sources — PrOntoQA-style synthetic logic and MATH-500 competition problems — are used as controlled substrates chosen for verifiability, and the measured quantity is the provenance of skill influence rather than mathematical or logical competence. Assigning Mathematics on the basis of the substrate would over-extend the domain axis.

## Evaluation

- **Reliance (R_v)** — an indicator that the answer under skill condition *v* differs from the no-skill answer, i.e. `1[d_v != d_∅]`.
- **Signed utility (u_v)** — whether the change helped or harmed relative to the reference answer, `1[d_v = d*] - 1[d_∅ = d*]`.
- **Attribution Fidelity Score (AFS)** — overlap between measured reliance and claimed use, computed as `2·n11 / (2·n11 + n10 + n01)`.
- **Backroom Gap (Γ_v)** — the disagreement rate between claimed and intervention-measured dependence.
- Observational detectors are meta-evaluated against these causal measures: direct skill-use claims, text mentions of the skill, trace similarity, and an LLM judge.
- **Reported.** Eight models claim skill use despite zero deletion reliance under perfect baseline accuracy. AFS on the logic split ranges from .01 to .72 across model–condition pairs; on mathematics no model–condition pair exceeds .43. In multi-agent settings, skill influence can survive communication after its source is lost, and no-skill teams still name skills and sources that were never supplied, with a false provenance rate near 1.00.

## Typical Duration

TODO(reference) — the paper reports no per-item wall-clock or token budget. Cost scales with the seven-condition design, since every item is answered once per skill condition plus a no-skill counterfactual.

## Main Contribution

Establishes that stated skill use is not evidence of skill influence, and frames the Reasoning Backroom as a general AI provenance problem whose audit requires intervention rather than observation.

## Key Design Ideas

- Every skill-conditioned answer is paired with a matched no-skill counterfactual, so influence is measured by difference rather than asserted from the transcript.
- Interventions are factored along five separable axes — meaning, wording, identity, content, assignment — which lets behavioral effects be traced to procedural content rather than to the displayed skill name.
- Attribution is elicited only *after* the answer is committed, preventing the request for attribution from shaping the decision.
- Observational detectors are treated as objects of evaluation, not as ground truth, and are scored against the intervention-measured signal.
- Multi-agent settings are included so that provenance loss through communication can be observed separately from provenance loss within one agent.

## Strengths

- Separates two things routinely conflated in skill evaluation: that an agent mentions a skill, and that the skill changed the outcome.
- Signed utility distinguishes silent uptake (uncredited help) from performative use (credited non-help), rather than collapsing both into a single "used / not used" bit.
- Verifiable task sources with deterministic reference answers make the counterfactual comparison well-defined.
- Negative results on four detector families give a concrete warning about self-report and judge-based skill-use audits.

## Limitations

- The task substrate is deliberately narrow — synthetic logic and competition mathematics — so the findings do not directly cover long-horizon or tool-executing skill use.
- No code or dataset URL is stated in the paper; released per-instance records and run manifests are referenced but not located.
- Repository note: figures in this card were read from the arXiv full text (v1, July 2026); no peer-reviewed version was located at the time of writing.
- Repository note: the seven-condition design multiplies inference cost per item, which is a practical constraint on applying BACKTRACE to larger or more expensive task suites.

## Related Works

- [Skill-Use](./skill-use.md) — Also makes skill use the measured object, decomposing it into trigger / compliance / boundary facets rather than testing whether the skill was causally responsible.
- [SkillTV-Bench](./skilltv-bench.md) — Also questions whether observers of skill-augmented executions can tell what happened, from the trajectory judge's side.
- [SkillSV](./skillsv.md) — Also uses counterfactual removal of skill content, to value a skill's internal units rather than to audit provenance claims.
- [SkillShapley](./skillshapley.md) — Also measures the causal contribution of skill content by counterfactual evaluation, at the level of individual skill steps.
- [AgentAtlas](./agentatlas.md) — Also argues that what an agent's transcript displays is not a reliable read on what drove its decisions.
