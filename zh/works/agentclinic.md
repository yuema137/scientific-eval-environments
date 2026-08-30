# AgentClinic (2024)

> [English](../../works/agentclinic.md) | **简体中文**

> **首次公开：** 2024-05-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2405.07960)

## Overview

AgentClinic 是模拟临床环境中评估 AI 的多模态 agent benchmark：医生 agent 须通过连续的医患交互、不完全信息下的多模态数据采集与工具使用得出诊断——覆盖九个医学专科与七种语言。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.07960>
- **Code:** <https://github.com/samuelschmidgall/agentclinic>
- **Project:** <https://agentclinic.github.io/>
- **Publication:** <https://www.nature.com/articles/s41746-026-02674-7>
- **Venue:** npj Digital Medicine, 2026

## Summary

AgentClinic 把静态医学问答改造成序贯决策：环境提供患者、检查与主持 agent（据官方项目页为四个 agent 与 24 种被建模的认知与隐性偏倚），受评的医生 agent 须问诊、开检查并作出诊断，可用工具包括经验学习、自适应检索、反思循环与一本跨病例持久保存的笔记本。同样的问题一旦变成序贯形式，诊断准确率可跌到静态问答的十分之一以下；Claude 3.5 系的 agent 在多数设定下领先，Llama-3 借笔记本工具获得最高 92% 的相对提升。该 benchmark 由真实 EHR 与一项临床阅读者研究支撑。

## Tasks

模拟临床环境中的多轮医患接诊，覆盖九个医学专科与七种语言，含多模态数据采集与工具使用；病例数为 TODO(reference)。

## Domains

覆盖九个专科的临床医学；多语言临床照护；由 EHR 支撑的病例材料。

## Evaluation

- 在有主持 agent 的多 agent 接诊中评估诊断准确率，含对患者与医生 agent 的偏差扰动与以患者为中心的指标；由真实电子病历与临床阅读者研究支撑。
- **报告。** 序贯交互使诊断准确率跌至静态问答水平的十分之一以下；Claude 3.5 系 agent 在多数设定领先；笔记本工具为 Llama-3 带来最高 92% 的相对提升。

## Typical Duration

每个病例为多轮临床接诊。

## Main Contribution

证明静态医学问答的分数乐观了一个数量级：同样的知识，一旦作为不完全信息下的序贯临床工作来评估，大多会崩塌。

## Key Design Ideas

- 患者、检查与主持 agent 让「环境」而非「题目」成为评估单元。
- 对认知与隐性偏差的建模把「抗偏差鲁棒性」变成可测的轴。
- 持久化工具（跨病例笔记本）让 benchmark 能测量跨病例的学习。

## Strengths

- 「静态到序贯的崩塌」是临床 agent 评估中被引用最多的发现之一。
- 多语言、多专科的广度，背后有临床阅读者研究支撑。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。npj Digital Medicine 的发表信息来自官方项目页；arXiv 元数据未载明。

## Related Works

- [MedAgentBench](./medagentbench.md) — 同样是交互式临床 agent 评估，对象是 FHIR 虚拟 EHR 而非模拟接诊。
- [SDBench](./sdbench.md) — 同样是序贯诊断，带信息门控与显式成本核算。
- [MedHELM](./medhelm.md) — 其设计所挑战的静态、医生验证的对应物。
