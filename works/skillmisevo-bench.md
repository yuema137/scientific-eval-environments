# SkillMisevo-Bench (2026)

> **English** | [简体中文](../zh/works/skillmisevo-bench.md)

## Overview

SkillMisevo-Bench is a frozen benchmark, paired with the lifecycle-aware harness SkillMisevo-Gym, for measuring *skill misevolution*: the failure in which a self-improving LLM agent distils an unsafe success into its persistent skill library, so that the unsafe procedure is retrieved and re-executed long after the triggering input is gone.

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A — agent-safety probe over persistent skill state; no scientific or research activity is directly evaluated.

## Links

- **Paper:** <https://arxiv.org/abs/2608.12851>
- **Code:** <https://github.com/henrymao2004/misevolve>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Skill evolution converts interaction trajectories into executable, transferable procedures, but the update objective is task outcome rather than procedure safety, so compromised experience can be generalized into reusable policy. Existing benchmarks measure current behavior or static artifacts and therefore cannot say whether risk was created at authoring, at retrieval, or only at later execution. SkillMisevo-Gym supplies the missing instrumentation — it versions the skill library across agent frameworks, isolates it from conversation, workspace, cache and native memory, records evolution inputs, diffs and retrievals, and replays a clean session in which only the agent-authored `SKILL.md` survives the reset. SkillMisevo-Bench fixes the task design and the metrics on top of that harness, and the paper adds SafeEvolve, a method-agnostic governance wrapper applied at skill write and reuse boundaries.

## Tasks

The benchmark is built from concepts discovered offline by an autoresearch procedure that pairs a falsifiable malicious mechanism with an enabling benign condition; retained concepts are instantiated as fresh malicious (M), benign (B) and persistence (P) tasks rather than by replaying prompts. AgentHazard supplies the executable validation base — its diverse operational harms, resettable CLI sandbox and trajectory judge — because its own records contain no skill-evolution or benign/persistence tasks. Each episode contains 21 tasks laid out on a fixed schedule, `MMM BBB MMM BBB MMM BBB | BBB`, with evolution running after every three-task block so that successive rounds expose cumulative malicious doses of three, six and nine before the final benign block measures contamination; the closing persistence block performs no update and reloads only the frozen `SKILL.md`. Each condition comprises 525 tasks in 25 episodes, with fixed denominators of 225 malicious, 225 benign and 75 persistence tasks — a missing task, judge result or retrieval event contributes zero rather than shrinking the denominator. Tasks, metadata and judges are frozen, and the discovery evidence remains hidden from the evaluated systems.

## Domains

General-purpose agentic operations — coding, web use, tool invocation and automation harms inherited from the AgentHazard task specification. No canonical science or engineering domain is targeted; the evaluated object is the safety of persistent skill adaptation.

## Evaluation

Nine headline metrics are absolute micro-aggregates over the frozen benchmark size, grouped by lifecycle gate. Online behavior: Benign Utility (benign completion on B), Malicious ASR (harmful completion on M), and Benign ASR / Contamination (the same harmful objective applied to B). Evolved artifact: Content Unsafety, Unsafe Generalization and Stealthiness, scored 1–5 by Kimi-K2-0905 over authored skills, with CU averaged over all artifacts and UG and Stealth averaged over those with CU ≥ 3. Post-attack, after a clean reload: Unsafe Retrieval Rate over persistence tasks, Carryover ASR and Carryover Utility. Gemini-3-Flash applies the retained harmful-trajectory rubric for the ASR metrics, and a separate benign-completion judge scores the benign and persistence objectives. The diagnostic grid crosses four target agent frameworks (Claude Code, Codex, Hermes, OpenClaw), all sharing a MiniMax-M2.7 backbone, with No Evolution plus five skill-evolution methods (EvoSkill, SkillClaw, AutoSkill, SkillsVote, SkillOpt) and Hermes' native evolution — 25 agent–method configurations in total, of which 21 evolve.

## Typical Duration

Each episode is 21 tasks with an evolution update after every three-task block; each condition runs 25 such episodes, i.e. 525 task executions. Each task runs in a fresh sandbox with a new conversation, workspace, process namespace and tool session, so only the episode-scoped skill store advances. No wall-clock or token budget is reported. `TODO(reference)` for cost.

## Main Contribution

The paper formulates skill misevolution as a longitudinal failure of the trajectory-to-skill lifecycle and contributes the instrumentation to attribute it: a lifecycle-aware harness that preserves episode-scoped skill evolution while resetting conversation, filesystem and native agent state; a frozen benchmark running from malicious exposure to carryover tasks with concept-aligned benign tasks, an independent benign-completion judge and nine lifecycle metrics; and SafeEvolve, a governance wrapper combining critic-localized delete-only repair, lineage-risk retrieval, harmful-reuse attribution and safety-aware retirement.

## Key Design Ideas

- Only the agent-authored `SKILL.md` crosses the final reset, which is what makes "did risk survive the session?" separable from "did the agent behave badly at the time?".
- Authoring, retrieval and execution are measured as separate gates, because progression may stop at any one of them and a terminal ASR cannot distinguish a safe library from an unsafe artifact that was simply never retrieved.
- Concept-aligned benign tasks share the malicious concept's surface so that contamination of ordinary work becomes measurable.
- A frozen schedule with fixed dose points turns cumulative malicious exposure into a controlled variable rather than an artifact of task order.
- Fresh sandboxes per task and export-then-reload of the skill file prevent cache, memory or workspace leakage from being mistaken for skill carryover.
- No-Evolution conditions are run as the non-updating control on identical tasks, judges and tools.

## Strengths

- Separates three failure points that a single terminal attack-success number conflates, and shows they diverge in practice: across the grid all 21 evolved conditions author unsafe artifacts, 19 retrieve unsafe skills, 19 show contamination, but only 15 retain fresh-session harm.
- Quantifies dose–response for persistent risk: pooled carryover ASR rises from 16.0% without malicious exposure to 35.3% after one round and 41.3% at the full budget, while carryover utility rises in parallel — establishing that harmful propagation coexists with genuinely useful reuse rather than trading off against it.
- Covers four production agent frameworks and six evolution methods under one shared backbone, so framework and method effects can be read off separately.
- Judges, tasks and thresholds are fixed before evaluation and the discovery evidence is withheld from evaluated systems, limiting the benchmark's own leakage.
- Demonstrates that governance can be added at the write and reuse boundaries without retraining: SafeEvolve reduces unsafe retrieval by 26.7 points and fresh-session harm by 17.3 points while mean benign utility moves by 0.4 points.

## Limitations

- The task substrate is inherited from a single prior harmful-task specification, so coverage of operational harms is bounded by that source.
- Attack surface is deliberately narrow — the attacker may only submit instructions at bounded positions in the learning history and cannot write the skill store, alter retrieval, or inject into benign and persistence tasks — which makes the results a lower bound rather than a full threat model.
- Several metrics rely on LLM judges (a harmful-trajectory rubric judge, a benign-completion judge, and a 1–5 artifact scorer), and artifact-quality scores are undefined when no artifact is judged.
- All configurations share one backbone model, so backbone sensitivity of misevolution is not measured.
- Repository note: the benchmark and the proposed defence appear in the same paper, so SafeEvolve's reported gains are measured on the authors' own protocol.

## Related Works

- [SkillEvolBench](./skillevolbench.md) — the utility-side counterpart: whether distilled skills remain useful under task shift, rather than whether they remain safe.
- [SkillAudit](./skillaudit.md) — audits an arbitrary skill package along utility, cost and safety, but treats the artifact as static rather than tracking how it was authored.
- [PATH-Bench](./path-bench.md) — measures transfer and forgetting along a controlled experience path, the same persistent-state pipeline viewed through capability rather than risk.
- [SafeAgentBench](./safeagentbench.md) — agent-safety benchmark over supplied hazardous instructions, without a persistent artifact that survives the session.
