# MedAgentBench (2025)

> [English](../../works/medagentbench.md) | **简体中文**

## Overview

MedAgentBench 是评测医疗 LLM agent 的真实感虚拟 EHR 环境：300 个由人类医生撰写、面向具体患者的临床任务（10 个类别），运行在 100 位患者、逾 70 万数据元素的真实感档案之上，环境符合 FHIR 标准且可交互。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.14654>
- **Code:** <https://github.com/stanfordmlgroup/MedAgentBench>
- **Publication:** <https://ai.nejm.org/doi/full/10.1056/AIdbp2500144>
- **Venue:** NEJM AI, 2025

## Summary

MedAgentBench 让 agent 面对医院实际运行的接口：agent 通过现代 EMR 系统使用的标准 FHIR API 与通信基础设施规划并调用工具，完成医生撰写的患者级任务。任务成功与否在环境内对照参考解程序化检验。最佳模型 Claude 3.5 Sonnet v2 的成功率为 69.67%，且各任务类别间差异显著。

## Tasks

300 个面向具体患者的任务，分 10 个由医生撰写的类别，运行在 100 位真实感患者档案（70 万+ 数据元素）之上；环境为 Docker 化的 FHIR 兼容虚拟 EHR。

## Domains

临床信息学：电子病历、EMR 互操作（FHIR）与临床任务自动化。

## Evaluation

- 在 FHIR 环境内对照参考解程序化检验成功率（据官方仓库，参考解需访问授权）。
- **报告。** 最佳模型 Claude 3.5 Sonnet v2 成功率 69.67%，各任务类别差异显著。

## Typical Duration

每个任务为对虚拟 EHR 的多步工具调用回合。

## Main Contribution

把医疗 agent 评估搬到生产级医疗标准上：agent 若操作不了 FHIR，就操作不了医院——无论考试分数多高。

## Key Design Ideas

- FHIR 兼容使 benchmark 环境与已部署的 EMR 系统同构。
- 医生撰写的任务把难度锚定在临床现实而非 API 覆盖率上。
- 程序化验证使判分不依赖 judge。

## Strengths

- 每个任务背后都是真实感规模（100 位患者、70 万+ 元素）。
- 类别间差异指出了哪些临床工作流仍未被自动化。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。NEJM AI 的发表信息由官方仓库引用（标题略有缩短）；arXiv 元数据未载明。

## Related Works

- [MedAgentGym](./medagentgym.md) — 同样是沙箱化的生物医学 agent 评估，核心是基于代码的数据科学任务。
- [AgentClinic](./agentclinic.md) — 同样是交互式临床评估，走模拟接诊而非 EHR API。
- [Gaia2](./gaia2.md) — 同样在有状态应用环境中程序化验证 agent 的写操作。
