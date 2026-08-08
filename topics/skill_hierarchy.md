# Skill Hierarchy

> **English** | [简体中文](../zh/topics/skill_hierarchy.md) · [← All topics](./README.md)

## Definition

Skill hierarchy refers to the decomposition of a complex agent capability into a structured set of narrower capabilities or subskills, together with evaluation protocols that score each subskill separately. Benchmarks in this space share the design commitment that a single aggregate score conflates too much: to understand what an agent can and cannot do, evaluation must probe multiple levels of the capability tree.

## Motivation

Aggregate leaderboards obscure the shape of an agent's competence. Two agents with the same overall score may fail on entirely different subskills, and a single-metric ranking does not tell a downstream user which agent to trust for which sub-task. Skill-hierarchy benchmarks address this by producing a per-capability profile.

Skill hierarchy is closely related to but distinct from [Credit Assignment](./credit_assignment.md). Skill hierarchy asks *which subskill an agent has*; credit assignment asks *which step of a trajectory drove a success or failure*. They can be pursued together — score each subskill along the trajectory — but they answer different questions.

## Existing Approaches

- **Task-subgoal decomposition.** [AgentBoard](../works/agentboard.md) annotates every task with a chain of subgoals and reports a progress rate — effectively a per-subgoal capability signal.
- **Capability-subprocess decomposition (tool use).** [T-Eval](../works/t-eval.md) decomposes tool use into six subprocesses (instruction following, planning, reasoning, retrieval, understanding, review) and evaluates each on isolated tasks.
- **Capability-subprocess decomposition (environment configuration).** [Enconda-bench](../works/enconda-bench.md) decomposes software environment configuration into planning / error diagnosis / repair / execution.
- **Capability axes as an organizing principle.** [UniClawBench](../works/uniclawbench.md) structures its 400-task benchmark around five capability axes (Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination) and uses these axes as the primary reporting dimension.
- **Cross-benchmark control-decision taxonomy.** [AgentAtlas](../works/agentatlas.md) does not decompose per-task or per-capability but instead classifies the *control decisions* an agent makes into a six-way taxonomy applied across 15 benchmarks — providing a skill-hierarchy signal that transfers across the tasks it audits.
- **Competence-depth tiers within one domain.** [CFDLLMBench](../works/cfdllmbench.md) decomposes CFD competence by *depth* rather than by subprocess: knowledge (CFDQuery), numerical and physical reasoning (CFDCodeBench), and practical workflow implementation (FoamBench), each a separate task set. Because the tiers are nested in difficulty rather than parallel, the profile they produce reads as a ceiling — strong knowledge scores coexist with near-zero end-to-end simulation success.
- **Tool-evolution framework (out-of-scope placement).** [GATE](../works/gate.md) is included here for completeness but its actual subject is graph-based tool making for LLMs, not skill decomposition. See the card for a full explanation.

## Comparison

| Benchmark | Year | Decomposition granularity | Axes | Card |
|---|---|---|---|---|
| AgentBoard | 2024 | Per-task subgoal chain | Task-specific (annotated) | [→](../works/agentboard.md) |
| T-Eval | 2023 | Cross-task capability subprocesses | 6 tool-use subprocesses | [→](../works/t-eval.md) |
| Enconda-bench | 2025 | Cross-task capability subprocesses | 4 env-configuration subprocesses | [→](../works/enconda-bench.md) |
| UniClawBench | 2026 | Benchmark-level organizing axes | 5 proactive-agent capabilities | [→](../works/uniclawbench.md) |
| AgentAtlas | 2026 | Per-control-decision (cross-benchmark overlay) | 6 control-decision types | [→](../works/agentatlas.md) |
| GATE | 2026 | *Tool-evolution framework, not skill decomposition — see card* | Hierarchical tool graph | [→](../works/gate.md) |
| CFDLLMBench | 2025 | Nested competence tiers within one domain | 3 depth tiers (knowledge / numerical reasoning / workflow implementation) | [→](../works/cfdllmbench.md) |

## Open Questions

- **Task-specific vs. cross-task decomposition.** AgentBoard decomposes each task individually into subgoals; T-Eval / Enconda-bench decompose the capability itself into subprocesses shared across tasks; AgentAtlas decomposes across benchmarks via control-decision types. Which yields more transferable capability profiles?
- **Choice of axes.** T-Eval's six, Enconda-bench's four, UniClawBench's five, and AgentAtlas's six axes all reflect legitimate decompositions. Is there a canonical minimal set, or is the axis choice necessarily domain-dependent?
- **Composition.** Given per-subskill scores, how should they be composed into an overall capability estimate without losing the profile that motivated decomposition?
- **Overlay vs. embedded decomposition.** Should skill-hierarchy signal be produced by the underlying benchmark (embedded, as in AgentBoard/T-Eval/Enconda-bench/UniClawBench) or applied as an overlay across benchmarks (as in AgentAtlas)?

## Related Works

- [AgentBoard](../works/agentboard.md)
- [T-Eval](../works/t-eval.md)
- [Enconda-bench](../works/enconda-bench.md)
- [UniClawBench](../works/uniclawbench.md)
- [AgentAtlas](../works/agentatlas.md)
- [GATE](../works/gate.md) — Included for completeness; its actual subject is tool making for LLMs, not skill-hierarchy evaluation.
- [CFDLLMBench](../works/cfdllmbench.md)

## Further Reading

- Yehudai, Eden, Li, Uziel, Zhao, Bar-Haim, Cohan, Shmueli-Scheuer. *Survey on Evaluation of LLM-based Agents*. arXiv 2503.16416, 2025. <https://arxiv.org/abs/2503.16416>
