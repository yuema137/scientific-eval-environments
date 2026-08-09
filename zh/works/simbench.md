# SimBench (2024)

> [English](../../works/simbench.md) | **简体中文**

## Overview

SimBench 评估并诊断 LLM 的数字孪生生成能力：面向仿真的 LLM 通过多轮交互为开源 Chrono 仿真器构建数字孪生——多体动力学、有限元分析、车辆动力学、机器人动力学与传感器仿真——由带预定义规则与人在环指导的 LLM judge 打分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2408.11987>
- **Code:** <https://github.com/uwsbel/SimBench>
- **Venue:** arXiv preprint；据官方仓库为 IEEE Access 2026

## Summary

SimBench 追问 LLM 能否从对话中搭起一个能用的物理系统仿真：33 个以上开源与闭源「面向仿真的 LLM」在五个物理领域的 Chrono 数字孪生生成上受比较，由 judge LLM 依预定义规则与人在环指导打分。据官方仓库，套件覆盖 34 个物理系统上的 102 个演示任务、3,000 余段专家评分的多轮对话（另有 280 题的配套 PyChronoBench），项目现已更名为 ChronoBench；设计上可扩展到 ANSYS、ABAQUS、OpenFOAM 等仿真器。

## Tasks

面向 Chrono 多物理场仿真器的多轮数字孪生生成；据官方仓库为 34 个物理系统上的 102 个演示任务。

## Domains

多物理场仿真工程：多体动力学、有限元分析、车辆动力学、机器人动力学与传感器仿真。

## Evaluation

- LLM-as-a-judge 按预定义规则与人在环指导对多轮生成打分。
- **报告。** 比较了 33 个以上面向仿真的 LLM；具体排名数字为 TODO(reference)。

## Typical Duration

每个数字孪生任务为多轮对话回合。

## Main Contribution

首个把 LLM 当作数字孪生工程师的系统性比较，把多轮仿真代码生成——而非一次性脚本——确立为受评技能。

## Key Design Ideas

- 数字孪生生成把几何、动力学与求解器配置捆绑成一件真实的交付物。
- 多轮交互贴合仿真工程师实际的迭代方式。
- 规则引导加人工监督的 LLM 评判在规模与判分保真间取得平衡。

## Strengths

- 五个物理领域、33+ 模型的广度。
- 由 Chrono 开发团队维护，任务与真实仿真器保持同步。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。仓库已更名为 ChronoBench 并引用 IEEE Access 2026 发表；arXiv 页面本身未载明 venue。

## Related Works

- [FEABench](./feabench.md) — 同样通过语言接口驱动专业仿真软件（COMSOL）。
- [CFDLLMBench](./cfdllmbench.md) — 同样是多层级的仿真代码评估，专精 CFD 并带物理检验。
- [SciConvBench](./sciconvbench.md) — 同样关注仿真设定的对话一侧，通过澄清不适定的请求。
