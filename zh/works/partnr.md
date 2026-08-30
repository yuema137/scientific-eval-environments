# PARTNR (2024)

> [English](../../works/partnr.md) | **简体中文**

> **首次公开：** 2024-10-31 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2411.00081)

## Overview

PARTNR 以空前的规模评测具身多 agent 任务——家居活动中的人机协作——中的规划与推理：Habitat 3.0 中横跨 60 栋房屋、5,819 个独特物体的 100,000 个自然语言任务，从规划、感知与技能执行三条轴分析 LLM 规划器。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2411.00081>
- **Code:** <https://github.com/facebookresearch/partnr-planner>
- **Project:** <https://aihabitat.org/partnr/>
- **Venue:** ICLR 2025（据官方仓库；arXiv 元数据未载明发表信息）

## Summary

PARTNR 用 LLM 半自动生成 10 万个任务，并在生成环节引入模拟做接地与验证，随后反过来评测 LLM 作为协作规划器的表现。主要发现颇为清醒：与真人搭档时，LLM agent 所需步数是两人协作的 1.5 倍——甚至比一个人单干还多 1.1 倍。模型侧则有一个积极结果：用规划数据微调的小模型能追平 9 倍大的模型，推理还快 8.6 倍。

## Tasks

Habitat 3.0 中的 100,000 个自然语言人机协作任务（无约束、空间、时间、异质四类），覆盖 60 栋房屋与 5,819 个物体；LLM 规划器与模拟或真人搭档协作。仅模拟，含人类在环评估。

## Domains

具身家居模拟（Habitat）——按其范围界定不在本仓库的科学/工程领域轴之内；因其评估方法学而收录。

## Evaluation

- 沿规划、感知、技能执行三条轴分析；与「人-人协作」的人类在环对照。
- **报告。** LLM + 真人：步数为两人协作的 1.5 倍、单人的 1.1 倍；微调小模型匹敌 9 倍大模型，推理快 8.6 倍。

## Typical Duration

与（模拟或真实）人类搭档并行的多步协作回合。

## Main Contribution

测量 LLM 规划器是否真的帮到了人——「LLM 搭档目前还不如自己单干」这一协作开销结论。

## Key Design Ideas

- LLM 生成、模拟验证的任务生成，在不牺牲可靠性的前提下换来规模。
- 与真人配对把「协作」从模拟构造变成被测成本。
- 任务类型分别隔离空间、时间与异质约束的处理能力。

## Strengths

- 比既有具身协作 benchmark 大出数个量级，且经过接地验证。
- 「1.1 倍于单人」是少见的、直接影响决策的负面结果。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；ICLR 2025 由仓库声明，arXiv 元数据未载明。
- 机器人仅存在于模拟中；物理部署层面的结论不在范围内。

## Related Works

- [RoCo / RoCoBench](./rocobench.md) — 同样是 LLM 多机器人协作，机器人 agent 间对话并有真实机械臂演示。
- [VIKI-Bench](./viki-bench.md) — 同样是具身多 agent 协作，按机器人形态分层分解。
- [EmbodiedBench](./embodiedbench.md) — 同样是大规模具身 MLLM 评估，单 agent 设定。
