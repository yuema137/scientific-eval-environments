# Survey

## Definition

Survey papers and position papers on LLM-agent evaluation and the future direction of agentic systems. Unlike a benchmark, a survey does not add a task suite or a scoring protocol; it organizes the literature and identifies gaps. This topic acts as an index of such references for the rest of the repository.

## Motivation

A repository organized around benchmarks and topic-level literature reviews still needs a home for meta-level references — surveys that catalog the field, and position papers that argue for direction. Rather than scattering them as footnotes, this topic collects them so that a reader looking for a "start with a survey" entry point can find one, and so that individual topic pages can cite them from one canonical location.

## Existing Approaches

- **General LLM-agent evaluation surveys.** [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md) (Yehudai et al., 2025) organizes evaluation across foundational capabilities, domain-specific benchmarks, generalist agents, benchmark core dimensions, and evaluation frameworks; identifies cost-efficiency, safety, robustness, and scalable evaluation methodologies as gaps.
- **Holistic LLM-agent surveys.** [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md) (Wang et al., 2023) surveys LLM-based autonomous agents across construction, application, and evaluation; proposes a four-module construction framework (profiling, memory, planning, action) and reviews evaluation as subjective vs. objective strategies. Its focus is agent construction rather than evaluation, so it is indexed here for completeness.
- **Position papers on the shift toward persistent agents.** [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md) (Zhang et al., 2026) argues that LLMs are shifting from conversational generators to integrated systems capable of reasoning, action, memory, and self-improvement — conceptualizing the shift along inference-time deliberation and persistent workstation systems with reusable skills.

## Comparison

| Reference | Year | Type | Focus | Card |
|---|---|---|---|---|
| A Survey on Large Language Model based Autonomous Agents | 2023 | Survey | Holistic agent construction, application, evaluation | [→](../works/llm-autonomous-agents-survey.md) |
| Survey on Evaluation of LLM-based Agents | 2025 | Survey | LLM-agent evaluation taxonomy | [→](../works/agent-evaluation-survey.md) |
| From Chatbot to Digital Colleague | 2026 | Position paper | Paradigm shift toward persistent autonomous AI | [→](../works/from-chatbot-to-digital-colleague.md) |

## Open Questions

- **Coverage cadence.** Agent evaluation moves fast; a survey published in 2025 will already miss 2026 developments. What is the right cadence for the field to publish updated surveys, and for this repository to add new ones?
- **Position papers as evidence.** Position papers argue for a direction rather than establish facts. How should this repository weight them relative to survey and benchmark papers when synthesizing across topics?

## Related Works

- [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md) — Holistic survey of LLM-based autonomous agents (construction, application, evaluation).
- [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md) — Comprehensive 5-perspective taxonomy of LLM-agent evaluation.
- [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md) — Position paper on the paradigm shift toward persistent autonomous AI.
