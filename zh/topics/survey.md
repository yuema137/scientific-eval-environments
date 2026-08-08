# Survey

> [English](../../topics/survey.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

关于 LLM-agent 评估与 agentic 系统未来方向的综述与立场论文。与 benchmark 不同，综述不引入新的任务集或评分协议——它组织文献、指出空缺。此 topic 页作为仓库其他部分对这类参考文献的索引。

## Motivation

一个围绕 benchmark 与 topic 级文献综述组织的仓库，仍然需要一个安放**元层次**引用的位置：综述用于给整个领域编目、立场论文用于主张方向。与其把它们零散地当作脚注，不如集中在此 topic，让希望"从综述入门"的读者能找到入口，也让各 topic 页在需要引用时能指向唯一的标准位置。

## Existing Approaches

- **通用 LLM-agent 评估综述。** [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md)（Yehudai 等，2025）沿 foundational capabilities、domain-specific benchmarks、generalist agents、benchmark core dimensions、evaluation frameworks 五个视角组织评估；指出 cost-efficiency、safety、robustness 与可扩展的评估方法学是当前空缺。[Evaluation and Benchmarking of LLM Agents: A Survey](../works/agent-evaluation-benchmarking-survey.md)（Mohammadi 等，2025）沿二维分类法组织同一领域——evaluation objectives（评估什么）对 evaluation process（如何评估）——并突出面向企业的挑战（role-based access、reliability、compliance）。
- **整体性 LLM-agent 综述。** [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md)（Wang 等，2023）沿构建、应用、评估三方面综述 LLM-based 自主 agent；提出四模块构建框架（profiling、memory、planning、action），并将评估回顾为 subjective 与 objective 两类策略。其重心是 agent 构建而非评估，此处为完整性索引。
- **关于持久 agent 转变的立场论文。** [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md)（Zhang 等，2026）主张 LLM 正从对话式生成器转向具备推理、行动、记忆和自改进能力的集成系统——沿"通过推理时计算 / 反思达成的深思推理"与"具备可复用技能与状态管理的持久 workstation 系统"两个维度概念化这一转变。

## Comparison

| Reference | Year | Type | Focus | Card |
|---|---|---|---|---|
| A Survey on Large Language Model based Autonomous Agents | 2023 | Survey | 整体性的 agent 构建、应用、评估 | [→](../works/llm-autonomous-agents-survey.md) |
| Survey on Evaluation of LLM-based Agents | 2025 | Survey | LLM-agent 评估分类（五视角） | [→](../works/agent-evaluation-survey.md) |
| Evaluation and Benchmarking of LLM Agents: A Survey | 2025 | Survey | objectives 对 process 二维分类；企业挑战 | [→](../works/agent-evaluation-benchmarking-survey.md) |
| From Chatbot to Digital Colleague | 2026 | Position paper | 向持久自主 AI 的范式转变 | [→](../works/from-chatbot-to-digital-colleague.md) |

## Open Questions

- **覆盖节奏。** Agent 评估的推进很快；一篇 2025 年发表的综述已经会错过 2026 年的进展。该领域应以怎样的节奏发布更新版综述？本仓库应以怎样的节奏纳入新的综述？
- **立场论文作为证据。** 立场论文主张方向，而不确立事实。在跨 topic 综合时，本仓库应如何权衡立场论文与综述、benchmark 论文之间的分量？

## Related Works

- [A Survey on Large Language Model based Autonomous Agents](../works/llm-autonomous-agents-survey.md) — LLM-based 自主 agent 的整体性综述（构建、应用、评估）。
- [Survey on Evaluation of LLM-based Agents](../works/agent-evaluation-survey.md) — LLM-agent 评估的五视角分类综述。
- [Evaluation and Benchmarking of LLM Agents: A Survey](../works/agent-evaluation-benchmarking-survey.md) — LLM-agent 评估的二维（objectives 对 process）分类综述，侧重企业场景。
- [From Chatbot to Digital Colleague](../works/from-chatbot-to-digital-colleague.md) — 立场论文，主张向持久自主 AI 的范式转变。
