# SCR-Bench (2026)

> **English** | [简体中文](../zh/works/scr-bench.md)

## Overview

SCR-Bench is a sandboxed benchmark for Skill Composition Risk: it scores agent behavior along *activated paths* of composed skills rather than on skills evaluated in isolation, recording downstream state changes instead of textual intent.

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — general-purpose agent safety probe over composed skill execution; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2606.15242>
- **Code:** <https://github.com/saint-viperx/SCR_Bench>
- **Venue:** arXiv preprint (cs.CR), 2026

## Summary

Skills are the capability layer through which LLM agents turn plans into actions, but vetting normally evaluates each skill on its own while real tasks invoke several skills in a shared execution context. The paper names the resulting gap Skill Composition Risk — a skill that appears benign alone becomes harmful when its outputs, trust signals, authorization cues, or side effects influence later invocations along an activated path — and builds SCR-Bench to measure it. Three sub-benchmarks isolate three composition mechanisms, and each is scored by observable downstream events in a sandbox rather than by what the agent says it will do.

## Tasks

Three sub-benchmarks in controlled, sandboxed skill environments:

- **SCR-CapFlow** (capability-flow composition) — 150 cases across permission and access control, mock reporting, device control, network configuration, and persistence scheduling, run against mock files, services, logs, schedules and state.
- **SCR-TrustLift** (trust-transfer composition) — 401 installation trials per backend in a simulated skill-market installation environment.
- **SCR-AuthBlur** (authorization-confusion composition) — 118 retained cases across security, privacy, finance, HR, supply-chain and operational-safety decisions, run under simulated approval and policy contexts.

## Domains

Agent skill ecosystems for general-purpose LLM agents; the exercised consequences are system operations, access control, device and network configuration, and organizational approval workflows. No canonical science or engineering domain is assigned.

## Evaluation

- **Path-level outcomes.** Success is credited only on an observable downstream event in the sandbox — a state change along the activated path — rather than a textual description of intent or a surface behavior classification.
- **Attack success rate (ASR)** averaged over cases and trials, defined by occurrence of the harmful state.
- **Context levels for AuthBlur:** L0 an unrelated control context, L1 a related task context, L3 an authorization-like advisory context; the risky-approval rate is the fraction of cases in which an unsafe request is approved.
- **Reported.** In SCR-CapFlow, ASR reaches 33.6% under composition against near-zero isolated baselines. In SCR-TrustLift, ASR exceeds 96.5% on four of five backends, against a control ASR near 0%. In SCR-AuthBlur, the risky-approval rate rises 71.8% relative to the L0 isolated baseline under the L1 setting, with reported averages of 15.7% (L0), 27.0% (L1) and 34.0% (L3). Nine backends are evaluated across the CapFlow conditions — GPT-5.5, GPT-5.4, Claude Opus 4.6, Claude Opus 4.5, Gemini 3.1 Pro Preview, MiniMax-M2.7, DeepSeek-V4, GLM-5.1 and GLM-5 — with five backends for TrustLift and ten for AuthBlur.

## Typical Duration

TODO(reference) — the paper reports per-case and per-trial outcome rates but not trajectory length, wall-clock, or token budgets.

## Main Contribution

Formulates Skill Composition Risk as a distinct evaluation target and supplies the first benchmark that measures it at the level of activated paths, showing that risks visible under composition are largely absent under the isolated per-skill vetting that marketplaces currently perform.

## Key Design Ideas

- Three separate composition mechanisms — capability flow, trust transfer, authorization confusion — are given their own sub-benchmark rather than folded into one aggregate risk score.
- Every sub-benchmark carries a matched isolated or control condition, so the reported effect is attributable to composition rather than to the skills themselves.
- Scoring is grounded in sandbox state changes, which removes the ambiguity of judging an agent's stated intent.
- Context is a manipulated variable in AuthBlur (L0/L1/L3), quantifying how much surrounding task context alone degrades approval discipline.

## Strengths

- The isolated-versus-composed contrast is built into the design, making the paper's central claim directly measurable.
- Backbone coverage is unusually broad (nine to ten frontier and open-weight models depending on sub-benchmark).
- Benchmark is publicly released.

## Limitations

- All environments are simulated or mocked; no result is obtained against a real skill marketplace or live system.
- The paper does not state how many distinct skills the sub-benchmarks contain — TODO(reference).
- Backend coverage differs across the three sub-benchmarks (nine, five, ten), so cross-sub-benchmark model comparisons are not like-for-like.
- Repository note: only pairwise or short activated paths are exercised by construction; the composition space grows combinatorially and the benchmark does not claim to cover it.

## Related Works

- [SLBench](./slbench.md) — Also tests skill-induced unsafe agent behavior with executable checks, targeting relations inside one skill rather than across composed skills.
- [HarmfulSkillBench](./harmfulskillbench.md) — Also evaluates agent safety with installed skills, where the skill is harmful by intent rather than benign in isolation.
- [SkillAudit](./skillaudit.md) — Also runs skills in isolated sandboxes for safety verification, auditing one package at a time.
- [Skill-Use](./skill-use.md) — Also measures whether an agent respects a skill's boundaries, per skill rather than per activated path.
