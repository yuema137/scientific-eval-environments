# SafeAgentBench (2024)

> [English](../../works/safeagentbench.md) | **简体中文**

## Overview

SafeAgentBench 评测具身 LLM agent 是否会安全地规划：750 个可执行任务，覆盖 10 类潜在危险与 3 种任务类型，运行在 SafeAgentEnv——一个带底层控制器、支持 17 个高层动作的通用具身环境——里，最有安全意识的基线也只拒绝 10% 的详细危险任务。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 评估的是 agent 的元属性（成本、安全性或鲁棒性），而非科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2412.13178>
- **Code:** <https://github.com/shengyin1224/SafeAgentBench>
- **Dataset:** <https://huggingface.co/datasets/safeagentbench/SafeAgentBench>
- **Venue:** arXiv preprint (cs.CR), 2024

## Summary

一个老老实实执行「把毛巾放炉子上加热」的具身 agent 是隐患，不是帮手。SafeAgentBench 把危险与安全任务成对给出——750 个精心策划的任务，覆盖 10 个危险类别与 3 种任务类型——并在 SafeAgentEnv 中执行计划，支持多 agent，含 9 个最先进基线。评估同时从执行与语义两个角度进行。结论令人警醒：最有安全意识的基线对详细危险任务只有 10% 的拒绝率，而更换底层 LLM 并不能显著改善安全意识。

## Tasks

在 SafeAgentEnv 中，用 17 个高层动作与底层控制器规划并执行的 750 个可执行具身任务（危险与安全；10 类危险、3 种任务类型）。交互式；仅模拟。

## Domains

具身家居模拟——不在本仓库的科学/工程领域轴之内；因其安全评估方法学而收录。

## Evaluation

- 执行角度与语义角度的评估；以任务成功率与拒绝率为核心指标。
- **报告。** 最佳基线对详细危险任务只有 10% 拒绝率；更换驱动 LLM 无显著安全改善。

## Typical Duration

每个任务一段规划-执行回合。

## Main Contribution

用可执行（而非假想）的危险量化具身 LLM agent 的安全意识差距——并表明这一差距是架构性的，换模型解决不了。

## Key Design Ideas

- 危险/安全任务成对，把「拒绝的校准」与「任务能力」分开。
- 可执行的危险把安全评估锚定在 agent 实际做了什么，而非它说了什么。
- 执行 + 语义的双重评估同时抓住不安全的动作与不安全的意图。

## Strengths

- 具身 LLM 安全的参考危险分类法，环境与数据集均公开。
- 「换模型无效」的负面结果把安全投入从选模型引向系统设计。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；这些来源无法核实任何发表信息。仓库 README 报告的是较旧的基线数字（安全任务 69% 成功率、5% 拒绝率），与当前摘要不同；以摘要数字为准。
- 危险仅存在于模拟中；物理世界的风险迁移未做评估。

## Related Works

- [BadRobot](./badrobot.md) — 同样是具身 LLM 安全，从攻击方一侧越狱到物理动作。
- [ASIMOV](./asimov.md) — 同样是机器人安全评估，处于「语义合意性」层面并借助宪法。
- [EmbodiedBench](./embodiedbench.md) — 同样是多基线的具身 LLM 评估，考能力而非安全。
