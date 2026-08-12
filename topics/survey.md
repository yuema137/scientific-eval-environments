# Survey

> **English** | [简体中文](../zh/topics/survey.md) · [← All topics](./README.md)

## Definition

Survey papers and position papers on LLM-agent evaluation and the future direction of agentic systems. Unlike a benchmark, a survey does not add a task suite or a scoring protocol; it organizes the literature and identifies gaps. This topic acts as an index of such references for the rest of the repository.

## Motivation

A repository organized around benchmarks and topic-level literature reviews still needs a home for meta-level references — surveys that catalog the field, and position papers that argue for direction. Rather than scattering them as footnotes, this topic collects them so that a reader looking for a "start with a survey" entry point can find one, and so that individual topic pages can cite them from one canonical location.

## Existing Approaches

- **General LLM-agent evaluation surveys.** [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md) (Yehudai et al., 2025) organizes evaluation across foundational capabilities, domain-specific benchmarks, generalist agents, benchmark core dimensions, and evaluation frameworks; identifies cost-efficiency, safety, robustness, and scalable evaluation methodologies as gaps. [Evaluation and Benchmarking of LLM Agents: A Survey](../works/agent-evaluation-benchmarking-survey.md) (Mohammadi et al., 2025) organizes the same field along a two-dimensional taxonomy — evaluation objectives (what to evaluate) vs. evaluation process (how to evaluate) — and foregrounds enterprise-specific challenges (role-based access, reliability, compliance).
- **Holistic LLM-agent surveys.** [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md) (Wang et al., 2023) surveys LLM-based autonomous agents across construction, application, and evaluation; proposes a four-module construction framework (profiling, memory, planning, action) and reviews evaluation as subjective vs. objective strategies. Its focus is agent construction rather than evaluation, so it is indexed here for completeness.
- **Verifiability audits of a subfield.** [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](../works/ara-survey.md) (2026) codes 35 autonomous-research-agent systems along seven audit dimensions and quantifies the verification gap: 83% of systems release code but only 38% release seeds or execution traces, only 38% report any novelty-verification method, and no LLM-era system in the corpus demonstrates an externally validated in-loop oracle. A reviewer checklist operationalizes the audit for reuse.
- **Position papers on the shift toward persistent agents.** [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md) (Zhang et al., 2026) argues that LLMs are shifting from conversational generators to integrated systems capable of reasoning, action, memory, and self-improvement — conceptualizing the shift along inference-time deliberation and persistent workstation systems with reusable skills.
- **Methodology surveys of credit assignment.** [From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models](../works/from-reasoning-to-agentic.md) (2026) synthesizes 69 papers on credit-assignment methods spanning reasoning and agentic RL, adding a six-diagnostic framework that maps assumption breaks to identification barriers, estimators, and evaluation controls, plus a reusable "CA-ID Card" for provenance and falsification. See also [Credit Assignment](./credit_assignment.md).

## Comparison

| Reference | Year | Type | Focus | Card |
|---|---|---|---|---|
| A Survey on Large Language Model based Autonomous Agents | 2023 | Survey | Holistic agent construction, application, evaluation | [→](../works/llm-autonomous-agents-survey.md) |
| Survey on Evaluation of LLM-based Agents | 2025 | Survey | LLM-agent evaluation taxonomy (5 perspectives) | [→](../works/agent-evaluation-survey.md) |
| Evaluation and Benchmarking of LLM Agents: A Survey | 2025 | Survey | Objectives-vs-process taxonomy; enterprise challenges | [→](../works/agent-evaluation-benchmarking-survey.md) |
| From Chatbot to Digital Colleague | 2026 | Position paper | Paradigm shift toward persistent autonomous AI | [→](../works/from-chatbot-to-digital-colleague.md) |
| Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap | 2026 | Survey | Seven-dimension verifiability audit of 35 AI-scientist systems | [→](../works/ara-survey.md) |
| From Reasoning to Agentic: Credit Assignment in RL for LLMs | 2026 | Survey | Credit-assignment methods across reasoning and agentic RL; six-diagnostic framework and CA-ID Card | [→](../works/from-reasoning-to-agentic.md) |

## Open Questions

- **Coverage cadence.** Agent evaluation moves fast; a survey published in 2025 will already miss 2026 developments. What is the right cadence for the field to publish updated surveys, and for this repository to add new ones?
- **Position papers as evidence.** Position papers argue for a direction rather than establish facts. How should this repository weight them relative to survey and benchmark papers when synthesizing across topics?

## Related Works

- [From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models](../works/from-reasoning-to-agentic.md)
- [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md) — Holistic survey of LLM-based autonomous agents (construction, application, evaluation).
- [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md) — Comprehensive 5-perspective taxonomy of LLM-agent evaluation.
- [Evaluation and Benchmarking of LLM Agents: A Survey](../works/agent-evaluation-benchmarking-survey.md) — Two-dimensional (objectives vs. process) taxonomy of LLM-agent evaluation with enterprise focus.
- [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md) — Position paper on the paradigm shift toward persistent autonomous AI.
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](../works/ara-survey.md) — Seven-dimension verifiability audit of autonomous research agents.
