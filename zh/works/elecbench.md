# ElecBench (2024)

> [English](../../works/elecbench.md) | **简体中文**

> **首次公开：** 2024-07-07 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2407.05365)

## Overview

ElecBench 是面向大语言模型的电力调度评估 benchmark：在通用知识与专业业务两类电力场景下，用六项核心指标——事实性、逻辑性、稳定性、安全性、公平性、表达性（细分为 24 个子指标）——评测八个 LLM。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.05365>
- **Code:** <https://github.com/xiyuan-zhou/ElecBench-a-PowerDispatch-Evaluation-Benchmark-for-Large-LanguageModels>
- **Venue:** arXiv preprint (cs.AI), 2024

## Summary

电力调度——实时保持电网稳定、安全、经济——是一个要求苛刻的决策领域，ElecBench 追问 LLM 能否对它推理。它把场景分为通用知识与专业业务两类，在一个六类框架（事实性、逻辑性、稳定性、安全性、公平性、表达性、细分为 24 个子指标）上评测八个 LLM，自我定位为电力行业 LLM 应用的标准 benchmark。其指标设计反映电网优先级：稳定性与安全性是头等考量，而非事后附加。

## Tasks

跨通用知识与专业业务场景的电力调度评估；LLM 为电网运行任务产出自然语言推理与决策，按六类/24 子指标框架评分。静态评估。

## Domains

能源系统——电力系统运行与调度：电网稳定性、安全性与经济调度决策。

## Evaluation

- 六项核心指标（事实性、逻辑性、稳定性、安全性、公平性、表达性）细分为 24 个子指标，覆盖八个 LLM。
- **报告。** 跨场景评测了八个 LLM；ElecBench 自我定位为电力行业的标准 benchmark。

## Typical Duration

单轮场景应答；无交互式设定。

## Main Contribution

一个面向电网调度的 LLM 领域评估框架，其指标分类编码了电网运行的真实要求——稳定性与安全性与事实正确性并列。

## Key Design Ideas

- 把稳定性与安全性列为显式指标类别，反映电网运行的优先级。
- 把通用知识与专业业务分开，区分回忆与运行能力。
- 24 个子指标把宽泛的评分标准变成细粒度诊断。

## Strengths

- 面向一个安全攸关运行领域的专建指标框架。
- 覆盖八个 LLM 的公开测试集。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与论文 PDF 编写（2026 年 8 月）；arXiv 元数据无发表信息，代码 URL（取自 PDF）未独立确认其有效性。

## Related Works

- [PowerAgentBench-SS](./poweragentbench-ss.md) — 同样是面向电力系统研究的 LLM 评估，考稳态预想故障分析、带重算的有效性验证。
- [HydroAgent](./hydroagent.md) — 同样是评估用于 agent 的能源/环境运行模型。
- [TeleQnA](./teleqna.md) — 同样是电气领域的知识 benchmark，考电信。
