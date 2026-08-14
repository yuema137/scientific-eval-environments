# PEOA (2024)

> **English** | [简体中文](../zh/works/peoa.md)

## Overview

PEOA (Process Engineering Operations Assistant) is a modular LLM-agent framework for chemical and process engineering problem-solving that is released together with two custom benchmark datasets — MathComp and ChemProc — and a staged tool-learning evaluation protocol used to compare the framework against proprietary LLMs.

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

- [Scientific Problem Solving & Reasoning](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** https://arxiv.org/abs/2408.14494
- **Venue:** Accepted for publication by the Association for the Advancement of Artificial Intelligence, Fall Symposium Series

## Summary

PEOA is organized as an "LLM operating system": a meta-agent coordinates an action generator that decomposes a user query into sub-tasks and routes each to an instruction-tuned small-scale expert model. Retrieval runs over a labeled property graph built from parsed scholarly PDFs and stored in Neo4j, feeding a Graph Retrieval-Augmented Code Generation (GRACG) loop under ReAct-style iterative task solving with error handling. Because no tool-integrated solution trajectories existed for the domain, the authors used GPT-4 (Omni) as a teacher model to synthesize step-by-step trajectories for instruction-tuning the student models. To measure the resulting system, they constructed two domain datasets and evaluated the framework against leading proprietary models across the four stages of tool learning plus a human study.

## Tasks

Two custom benchmark datasets were built. MathComp contains over 8,500 question-answer pairs on mathematical modeling and numerical algorithms, covering differential equations, linear algebra, optimization, and related tasks. ChemProc contains over 7,000 question-answer pairs on chemical engineering topics: mass and energy balances, thermodynamics, heat transfer, reaction kinetics, fluid mechanics, separation processes, and process control. Both were compiled from publicly available scholarly sources, including textbooks ranging from basic to advanced levels, and were split 70% training / 15% validation / 15% test. Each item is solved as a multi-step tool-integrated trajectory in which the agent plans sub-tasks, selects tools, calls them with extracted parameters, and synthesizes a final response.

## Domains

Chemical Engineering is the central domain: the ChemProc dataset targets core chemical and process engineering subject matter — mass and energy balances, thermodynamics, heat transfer, reaction kinetics, fluid mechanics, separation processes, and process control — and the paper frames the framework's purpose as designing, optimizing, and troubleshooting industrial chemical processes. The companion MathComp dataset supplies general mathematical-modeling and numerical-methods content (differential equations, linear algebra, optimization) that supports the engineering calculations rather than constituting a separate evaluated field.

## Evaluation

Scoring is decomposed across the four stages of tool learning rather than applied only to the final answer. Task planning uses Tool Usage Awareness (share of queries correctly identified as needing an external tool), Pass Rate (share of tasks successfully completed), and Accuracy (share of generated plans matching a gold-standard solution). Tool selection uses Recall@K, NDCG@K, and COMP@K against a ground-truth tool set, with graded relevance scores assigned by human evaluators. Tool calling uses Consistency with Stipulations, Correctness of Parameter Extraction, and Error Handling. Response generation uses BLEU, ROUGE-L, and Exact Match against reference responses. A separate user-centric evaluation rates eight human-judged aspects — user satisfaction, usability, task completion, response quality, context awareness, adaptability, error handling, and qualitative feedback — on 1–5 Likert scales (task completion as Yes/No, qualitative feedback as High / Medium-High / Medium). Baselines are GPT-4 Turbo-preview, GPT-4-1106-preview, Claude-3 Opus, Claude-3 Sonnet, Claude-3 Haiku, and Google Gemini Pro; results are reported as ensemble averages over multiple independent runs. The paper's stated finding is that the framework performs effectively across the evaluation stages and closely matches proprietary LLMs, with a slight remaining performance gap.

## Typical Duration

N/A — the paper reports no per-task wall-clock, trajectory-length, or token-budget figures. TODO(reference)

## Main Contribution

The authors present PEOA as a framework that automates multi-step problem-solving in chemical and process engineering by combining a meta-agent orchestrator with instruction-tuned small-scale expert models, property-graph knowledge modeling for retrieval, and a teacher-student transfer-learning pipeline for domain adaptation. Alongside the framework they contribute the MathComp and ChemProc benchmark datasets and a staged evaluation protocol, which they describe as supplying the domain-specific knowledge, computational problem-solving skills, and rigorous evaluation framework absent from more general existing datasets.

## Key Design Ideas

- Meta-agent as central coordinator over an action generator plus a set of instruction-tuned small-scale expert models, so a complex query is decomposed into sub-tasks and each sub-task is routed to a specialist.
- Knowledge modeling as a labeled property graph in Neo4j, with nodes for text, images, tables, and code extracted by a custom PDF parsing pipeline, and edges capturing their relationships; the graph serves as both ontology and schema.
- Graph Retrieval-Augmented Code Generation (GRACG) instead of flat-text RAG, motivated by the claim that preserving graph topology supports multi-hop reasoning and reduces hallucination.
- Teacher-student transfer learning with GPT-4 (Omni) generating tool-integrated solution trajectories as synthetic instruction-tuning data, addressing the absence of any pre-existing trajectory corpus for the domain.
- Iterative task solving (rather than one-step planning) so the agent can correct tool outputs from feedback; DeepSeek-Coder-7B-Instruct and DeepSeek-Math-7B-Instruct are fine-tuned with the Hugging Face PEFT library using QLoRA.
- Stage-decomposed evaluation over planning, selection, calling, and generation, which localizes where a trajectory breaks rather than reporting a single end-task score.

## Strengths

- Evaluation is trajectory-aware: the four-stage metric family scores intermediate planning and tool-use decisions against gold plans and ground-truth tool sets, not only the final response.
- The ChemProc dataset spans the core chemical engineering curriculum breadth (balances, thermodynamics, transport, kinetics, separations, process control) rather than a single sub-topic.
- Comparison covers six proprietary model configurations across three vendors, with ensemble averages over multiple independent runs.
- The automated metrics are complemented by an eight-aspect human evaluation, including deliberately injected errors to probe self-correction.

## Limitations

- The paper reports no public release of the MathComp or ChemProc datasets, nor a code repository; the arXiv page lists no code or data links. TODO(reference)
- Response-generation quality is measured largely by surface-overlap metrics (BLEU, ROUGE-L, Exact Match) against reference responses, which are weak proxies for numerical correctness in engineering calculations.
- Repository note: the same datasets are used both to instruction-tune the framework and to evaluate it (70/15/15 split), so the comparison against proprietary baselines is between an in-domain fine-tuned system and zero-shot models on the fine-tuning distribution.
- Repository note: the items are textbook-style question-answer pairs, so the evaluation covers process-engineering *calculations* rather than executable process-systems tasks such as flowsheet construction, simulator-in-the-loop design, or plant-operations decision-making.
- Repository note: per-category task counts within each dataset are not reported, so it is not possible to tell how much of ChemProc falls on any individual chemical engineering topic.

## Related Works

- [T-Eval](./t-eval.md) — likewise decomposes tool-use evaluation into separately scored subprocesses rather than a single end-task score.
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — evaluates LLMs on chemical-engineering thermodynamics problems, overlapping ChemProc's subject matter.
- [MaScQA](./mascqa.md) — another exam/textbook-derived engineering question-answering dataset used to probe LLM domain knowledge.
