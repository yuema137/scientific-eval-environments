# MedAgentGym (2025)

> [English](../../works/medagentgym.md) | **简体中文**

> **首次公开：** 2025-06-04 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2506.04405)

## Overview

MedAgentGym 是面向生物医学数据科学中以代码为中心推理的可扩展 agentic 环境：72,413 个任务实例、129 个类别，派生自 12 个真实生物医学场景，每个任务封装在带交互反馈与可验证真值的可执行沙箱中。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.04405>
- **Code:** <https://github.com/wshi83/MedAgentGym>
- **Project:** <https://wshi83.github.io/MedAgentGym-Page>
- **Dataset:** <https://huggingface.co/MedAgentGym>
- **Venue:** ICLR 2026（据官方仓库）

## Summary

MedAgentGym 兼具 benchmark 与训练环境两种身份：沙箱任务带详细规格、交互反馈机制、可验证的真值标注，以及面向离线与在线强化学习的可扩展轨迹生成。论文在该套件上评测 29 个 LLM，并训练出 Med-Copilot——离线 RL 增益 +43.02%、在线 RL 增益 +45.28%——作为一种成本更低、可保护隐私、性能可与专有模型竞争的替代方案。部分底层数据集需 PhysioNet 认证访问（据官方仓库）。

## Tasks

72,413 个编码任务实例、129 个类别，来自 12 个真实生物医学数据科学场景，均在带交互反馈的可执行沙箱中运行。

## Domains

生物医学数据科学，含 EHR 相关场景（据官方仓库为 MIMIC-III、eICU 等）。

## Evaluation

- 可验证的真值标注在可执行沙箱中检验。
- **报告。** 29 个 LLM 受评；配套的 Med-Copilot 经离线 RL 提升 +43.02%、在线 RL 提升 +45.28%。

## Typical Duration

沙箱中的多轮编码回合；预算为 TODO(reference)。

## Main Contribution

把可验证、沙箱执行的评估带到五位数规模的生物医学数据科学编码上，且同一环境既可评测也可做基于轨迹的 agent 训练。

## Key Design Ideas

- 每个任务都可执行、真值可验证，规模扩大并不稀释判分严格性。
- 交互反馈让沙箱成为真正的环境，而非静态测试集。
- 同一基础设施同时服务评估与 RL 训练，读者应把这两种用途区分开。

## Strengths

- 129 个类别、7.2 万实例，是本仓库记录的最大可验证生物医学编码套件。
- 29 个模型的评测给出宽广的前沿覆盖。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: Med-Copilot 与 RL 训练流水线属于 agent 训练贡献，超出本仓库范围；本卡片记录其 benchmark 环境。

## Related Works

- [MedAgentBench](./medagentbench.md) — 同样是交互式医疗 agent 环境，基于 FHIR 虚拟 EHR 而非编码沙箱。
- [SciAgentArena](./sciagentarena.md) — 同样是带按领域逐步验证的生物医学研究任务评估。
- [BioXArena](./bioxarena.md) — 同样是标准化算力、隐藏标签下的端到端生物医学 ML 任务。
