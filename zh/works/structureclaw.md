# StructureClaw (2026)

> [English](../../works/structureclaw.md) | **简体中文**

> **首次公开：** 2026-07-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2607.14896)

## Overview

StructureClaw 把一个可追溯的结构工程 LLM agent 工作台与一个可执行 benchmark 配对：150 个受控场景横跨标准工作流、交互鲁棒性与多模态结构模型重构，以严格的结构模型匹配与「对照冻结参考求解器响应的数值一致性」验证。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.14896>
- **Code:** <https://github.com/structureclaw/structureclaw>
- **Venue:** arXiv preprint (cs.SE, cs.AI, cs.MA), 2026

## Summary

agent 在以工件为中心的工作台上操作——受治理的工程技能、带类型的工具、共享工件状态与本地分析后端（据官方仓库含 OpenSees）——把任务从结构模型一路做到验证、求解、规范校核与报告。一次试验只有在每条 fixture 要求的断言都通过时才算成功：结构模型一对一匹配，加上与冻结参考响应的数值一致；交互类算例还须给出澄清或恢复的正面证据，并在恰当时安全地不执行。在九种文本 agent 配置中，仅通用执行的配置有 87.0% 通过模型工件检查，端到端成功率却只有 22.0%；自动化的 StructureClaw 配置达到 82.9%。

## Tasks

150 个受控结构工程场景，分三族：标准工作流、交互鲁棒性（澄清/恢复/安全拒绝）与多模态结构模型重构。

## Domains

结构工程：结构分析工作流、模型验证、求解执行与规范符合性校核。

## Evaluation

- 结构模型一对一严格匹配，加上与冻结参考求解器输出的数值响应一致性；所有 fixture 断言须全部通过（E2E Success）；交互算例须有澄清/恢复证据或安全不执行。
- **报告。** 仅通用执行：模型工件检查通过 87.0%，但 E2E Success 仅 22.0%；自动化 StructureClaw 达 82.9%（九种文本 agent 配置）。

## Typical Duration

每个场景为多步工作台会话，含交互式澄清算例。

## Main Contribution

表明在涉及安全的工程里，「产出一个像样的模型工件」（87%）与「把工程活干对」（22%）是天差地别的两回事——而受治理的工具链能弥合大部分差距。

## Key Design Ideas

- 冻结的参考求解器响应让数值一致性来裁定，而不是交给 judge。
- 「安全地不执行」是被计分的正确行为，把拒绝引入工程评估。
- 带类型的工具与共享工件状态为每一步留下可审计痕迹。

## Strengths

- 87% 对 22% 的工件/端到端落差是对浅层成功指标的鲜明警示。
- 用的是真实分析后端而非模拟求解器。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: StructureClaw 工作台是与 benchmark 配对的系统贡献；本卡片记录其 benchmark。

## Related Works

- [FEABench](./feabench.md) — 同样是语言驱动的有限元工程，经 COMSOL 的 API。
- [Frontier-Eng](./frontier-eng.md) — 同样是仿真器反馈与硬约束下的真实工程评估。
- [MooseBench](./moosebench.md) — 同样验证生成的模拟工件是否编码了预期的物理。
