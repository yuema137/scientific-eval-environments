# A Survey on Large Language Model based Autonomous Agents (2023)

## Overview

*A Survey on Large Language Model based Autonomous Agents* is a comprehensive survey of LLM-based autonomous agents that proposes a unified agent-construction framework, catalogs applications across social science, natural science, and engineering, and reviews the evaluation strategies used for such agents. It is included here as a reference paper, not a benchmark contribution; its primary subject is agent construction rather than evaluation (see the repository note under Limitations).

## Topics

- [Survey](../topics/survey.md)

## Links

- **Paper:** <https://arxiv.org/abs/2308.11432>

## Summary

The survey reviews the field of LLM-based autonomous agents from a holistic perspective across three pillars: construction, application, and evaluation. For construction it proposes a unified framework composed of a profiling module, a memory module, a planning module, and an action module. It then overviews applications in social science, natural science, and engineering, and reviews the evaluation strategies commonly used for LLM-based autonomous agents, distinguishing subjective evaluation (based on human judgements) from objective evaluation (quantifiable performance metrics). It closes with challenges and future directions.

## Tasks

N/A — survey paper.

## Domains

Cross-domain coverage: LLM-based autonomous agents applied across social science, natural science, and engineering.

## Evaluation

N/A — survey paper. The survey itself reviews evaluation strategies for LLM-based autonomous agents, taxonomizing them into subjective evaluation (based on human judgements) and objective evaluation (quantifiable performance metrics).

## Typical Duration

N/A.

## Main Contribution

A holistic survey of LLM-based autonomous agents organized around a unified construction framework, an application taxonomy across three domain families, and a review of subjective vs. objective evaluation strategies.

## Key Design Ideas

- Unified agent-construction framework with four modules: profiling, memory, planning, and action.
- Application taxonomy spanning social science, natural science, and engineering.
- Evaluation reviewed as subjective (human-judgement-based) vs. objective (metric-based) strategies.

## Strengths

- Broad, early holistic survey of the LLM-based autonomous-agent literature.
- The four-module construction framework provides a common vocabulary for comparing agent designs.
- Covers construction, application, and evaluation together rather than in isolation.

## Limitations

- Repository note: The survey's primary contribution is agent *construction* (architecture, applications), with evaluation reviewed as one of three pillars rather than being the paper's focus. It is included under Survey for completeness; readers seeking an evaluation-centric survey should start from [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md).
- Repository note: Survey papers freeze the state of the field at publication time; as an August 2023 survey, it predates most works documented in this repository.

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — Also a survey reference paper, but focused specifically on LLM-agent *evaluation* rather than agent construction and applications.
- [From Chatbot to Digital Colleague](./from-chatbot-to-digital-colleague.md) — Also a meta-level reference paper; a position paper arguing a direction rather than a survey cataloguing the field.
