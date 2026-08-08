# RoCo / RoCoBench (2023)

> [English](../../works/rocobench.md) | **简体中文**

## Overview

RoCoBench 是一个 6 任务的多机器人协作 benchmark，其中每台机器人都由 LLM 驱动：机器人之间用自然语言对话商量任务策略，生成子任务计划与任务空间路径点，并借环境反馈迭代改进——随 RoCo 协作方法一同发布。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2307.04738>
- **Code:** <https://github.com/MandiZhao/robot-collab>
- **Project:** <https://project-roco.github.io>
- **Venue:** arXiv preprint (cs.RO), 2023

## Summary

RoCo 给每条机械臂配一个 LLM，让协作从对话中涌现：agent 们协商分工、提出路径点方案，被碰撞检查否决后再修订计划。RoCoBench 把这一切打包为 MuJoCo 中的 6 个协作操作任务，任务语义可变以测试适应能力；另有 RoCoBench-Text——269 道推理题，覆盖自我认知、记忆、沟通与适应四类（官方项目页）。该方法还在真实 UR5 机械臂上完成了带人类协作者的演示。

## Tasks

MuJoCo 模拟中的 6 个多机器人协作操作任务，带语义变体；另有 269 题的 RoCoBench-Text 推理集；真实 UR5 机械臂演示。

## Domains

机器人学——多机器人操作与控制：LLM 协商出的子任务计划与路径点在模拟中执行，并在物理 UR5 机械臂上演示。

## Evaluation

- RoCoBench 上的任务成功率、任务语义变体下的适应性，以及 RoCoBench-Text 上的问答。
- **报告。** 摘要无数值结果；数字有待全文校验。

## Typical Duration

每个协作任务一段多轮「对话 + 重规划」回合。

## Main Contribution

证明并使之可测量：机器人之间的自然语言对话可以充当多机器人操作的协调基座。

## Key Design Ideas

- 以对话为协调通道，协作过程可解释、可探查。
- 环境反馈（碰撞检查）为 LLM 提出的动作闭环。
- 语义任务变体测的是适应，而非背下来的角色分配。

## Strengths

- LLM 多机器人协作的奠基性 benchmark，公开材料异常完整。
- RoCoBench-Text 把推理成分从控制成分中隔离出来。

## Limitations

- Repository note: 该论文的头号贡献是 RoCo 协作方法；RoCoBench 是其配对 benchmark，本卡片覆盖 benchmark。流传的 ICRA 2024 说法无法从 arXiv 元数据或官方页面核实——发表信息栏保持 arXiv preprint。
- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；数值结果有待全文校验。

## Related Works

- [PARTNR](./partnr.md) — 同样是具身多 agent 协作评测，规模达 10 万任务并有人类搭档。
- [VIKI-Bench](./viki-bench.md) — 同样是多机器人协作评估，跨形态分层结构化。
- [CaP-X](./cap-x.md) — 同样让 LLM 产出可执行的机器人控制，走代码合成而非对话。
