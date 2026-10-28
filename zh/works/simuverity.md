# SimuVerity (2026)

> [English](../../works/simuverity.md) | **简体中文**

> **首次公开：** 2026-10-01 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.02304)

## Overview

根据文字需求生成的 Simulink 模型，可能看着和参考模型很像，作为工程成果却不合格：编译不过，缺了必需的信号通路，或者一遇到故障工况就表现异常。SimuVerity 要求 agent 为 101 个工程系统搭建可执行的 Simulink 模型，并通过原生仿真来打分。分层评测器先过三道关：有没有交付、能不能运行、能不能通过工程资格检查；过关后才在 agent 看不到的测试场景下，从六个工程维度打分。作者用两位专家的评分检验了评测器，还检验了“和参考模型结构相似”能不能预测得分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [SimuVerity: Benchmarking Agents for Engineering-Grade Simulink Model Generation](https://arxiv.org/abs/2610.02304)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.02304v1>
- **Code and data:** <https://github.com/SimuVerity/SimuVerity>
- **Venue:** arXiv 预印本（cs.SE、cs.AI、cs.LG，2026）

## Summary

参考系统来自公开示例、工程项目、论文附带的研究成果和专家自建的模型；每个都经过重建或独立搭建，由领域专家梳理出系统特征，再据此写成任务提示。agent 在 MATLAB/Simulink R2025a 中通过 MATLAB MCP server 工作，必须交付一个 `.slx` 文件。评测器先检查文件是否存在、能否加载、编译和仿真，再用针对该任务的专家检查项核对必需的功能角色和信号通路。通过资格检查的模型会在任务的正式场景下运行，得分是六个维度的加权几何平均：准确度、输出质量、机理保真度、控制与因果完整性、鲁棒性、动态响应。最好的系统得 42.86 分，参考模型平均 96.01 分。

## Tasks

共 101 个从文字生成 Simulink 模型的任务，分布在十个工程领域：电力电子与控制 9、汽车系统 11、机械系统 11、电池系统 10、机器人 10、航空航天系统 10、热系统 11、通信系统 9、流体系统 11、生物医学系统 9。任务共带 595 个正式测试场景，分为四类：运行包络、交互与故障、时间过程、机理与因果检查。

## Domains

系统级动态建模，涉及电力电子与控制、汽车、机械、电池、机器人、航空航天、热、通信、流体和生物医学系统。

## Evaluation

- **门槛：** 交付成果（`.slx` 文件）、原生可执行性（加载、更新、编译、仿真），以及工程资格 G（专家针对功能角色、信号通路和正式场景下有效证据设置的通过/不通过检查）。
- **得分：** S_t(x) = Γ_t · H_t(v_t)，Γ_t 表示门槛，H_t 是适用维度的加权几何平均。六个维度是 A（目标准确度）、Q（输出质量）、M（机理保真度）、C（控制与因果完整性）、R（工作域鲁棒性）、D（动态响应与恢复）。权重按任务设定，比如 XAUTO-07 的权重依次是 0.25、0.10、0.25、0.20、0.10、0.10。
- **不用 LLM judge。** 两位专家用五分制给 30 个候选模型打分：加权 Cohen's κ = 0.90，评测器与专家的平均 Spearman ρ = 0.94，两位专家之间 ρ = 0.87。
- **结果（总分 / 交付率 / 可执行率 / G 通过率，每题跑三次）：** Claude Opus 4.8 + Claude Code 为 42.86 / 94.72% / 86.47% / 76.90%；GPT-5.5 + Codex 为 41.72 / 98.68% / 94.72% / 75.58%；DeepSeek-V4-Pro + Claude Code 为 28.40 / 97.03% / 88.12% / 61.39%；Qwen3.8-Max + Claude Code 为 25.01 / 89.77% / 80.86% / 53.80%；GLM-5.3-Flash + Claude Code 为 4.98 / 96.04% / 48.18% / 13.20%；Qwen3.8-27B-FP8 + Claude Code 为 1.60 / 30.36% / 13.53% / 6.27%。
- **结构相似度：** Opus 第一轮交付的 95 个候选模型中，与参考结构一致的 39 个、部分相似的 43 个、结构明显不同的 13 个，端到端平均分分别为 52.13、44.05 和 42.37。得分前四分之一的 24 个候选里有 12 个属于部分相似或结构不同，而有 7 个与参考结构一致的候选得了零分。
- **可视布局：** 不计入得分，单独用模块重叠、连线绕行和连线交叉密度来衡量；专家认为 31 个高分模型中有 8 个布局严重混乱。
- **消融：** 去掉仿真 MCP 的设置，以及只能批量运行的设置。

## Typical Duration

论文没有报告。agent 宣布完成即结束运行；推理强度设为各模型支持的最高档。

## Main Contribution

一个 Simulink 生成 benchmark：先过可执行性和专家资格两道门槛，再在 agent 看不到的场景下用原生仿真打分，并且评测器经过专家评分的检验。

## Key Design Ideas

- 测试条件、场景组合、阈值和打分逻辑在 agent 生成模型时都不可见。
- 用几何平均，一个维度严重失分就没法靠其他维度补回来。
- 追踪任务来源、对同源任务去重、筛查近似重复；示例目录和参考文件对 agent 隐藏，外网和网络工具都被禁用。作者报告没有任何一条轨迹接触到这些资源。

## Strengths

- 评测器与专家的一致性是实测出来的（κ = 0.90），不是假设的。
- 每道门槛的通过率都有报告，能把没交付、跑不起来、资格不过关和工程性能不足这几种情况分开。
- 结构相似度分析直接检验了“像参考模型”能否预测得分。

## Limitations

- 作者说明，这个 benchmark 依赖 MATLAB/Simulink，基于原生仿真的评测可能比较慢。
- 可视布局质量单独报告，不计入得分。
- Repository note：论文没有报告人类基线；96.01 是参考模型的平均分。
- Repository note：论文没有报告每题的时间、轮数或成本预算。

## Related Works

- [SimBench](./simbench.md) — 同样评测模拟器模型的生成（Chrono 数字孪生），但由 LLM judge 打分，而不是原生仿真。
- [EngDesign](./engdesign.md) — 同样包含用仿真检查的控制与系统设计任务。
