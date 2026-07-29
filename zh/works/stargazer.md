# Stargazer (2026)

## Overview

Stargazer 是一个可扩展的 benchmark 环境，用于在径向速度（RV）时间序列上评估 AI agent 的动态、迭代、物理约束的模型拟合（model-fitting）任务。它包含 120 个任务——100 个按三个难度层级由模拟器生成，外加 20 个匿名化的真实档案系统——并在每次提交后返回内置的逐判据反馈。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.15664>
- **Project:** <https://aips-uoft.github.io/Stargazer/>
- **Code:** <https://github.com/AIPS-UofT/Stargazer>

## Summary

Stargazer 的出发点是：在研究工作中评估 agent，需要在有科学依据的任务上提供内置反馈的动态 benchmark 环境。各 agent 通过 Python REPL 与提交接口对 RV 时间序列迭代拟合开普勒轨道模型，评估器在每次提交后返回逐判据的通过 / 未通过诊断及可选提示。在八个 frontier agent 中，最好的通过率从 Easy 层级的 80.0%（GPT-5.3-codex）降至 Hard 层级的 5.8%（GPT-5.2），在 20 个真实档案系统上所有 agent 均为 0.0%，良好的统计拟合经常与错误的物理参数并存。增加 test-time compute 只带来边际收益，过量的 token 用量往往反映的是递归失败循环，而非有意义的探索。

## Tasks

120 个任务：100 个合成 RV 模型拟合任务，分为三个难度层级——Easy（20）、Medium（40）、Hard（40）——另有 20 个真实档案系统，取自 NASA Exoplanet Archive 与 VizieR 的已发表数据集，行星数从一到七不等。合成场景覆盖从高 SNR 单行星系统到需要低 SNR 分析的多行星构型。

## Domains

天体物理：基于径向速度时间序列的系外行星系统推断。

## Evaluation

只有当四个评估判据同时满足时，任务才算被解决：

- **残差质量（ok_rms）。** 提交拟合的残差 RMS 不得超过该序列测量不确定度中位数的 1.5 倍。
- **模型选择（ok_delta_bic）。** 所提模型相对加权均值常数零模型的逐点 ΔBIC 必须为正。
- **物理恢复（ok_match）。** 通过匈牙利算法将所提行星与真值行星匹配，所得匹配分数不得低于 0.8。
- **行星数目（ok_count）。** 所提行星数必须等于真实数目。
- **报告结果（Table 1）。** 通过率在三次独立运行上取平均：GPT-5.3-codex 在 Easy 层级以 80.0% 领先八个受评 agent，而经典 Lomb-Scargle + 开普勒拟合流水线为 95.0%；GPT-5.2 在 Hard 层级以 5.8% 领先；没有任何 agent——o3-mini、GPT-5-mini、GPT-5.2、Kimi-K2.5、Qwen-3.5-Plus、Gemini-3.1-Pro、Claude-Sonnet-4.6、GPT-5.3-codex——通过 20 个真实档案任务中的任何一个（0.0%）。

## Typical Duration

各层级预算：Easy 为 200K token 与 600 s wall-clock、3 次提交机会，Medium 为 450K token 与 900 s、5 次，Hard 为 900K token 与 1,500 s、10 次；达到任一上限，episode 即终止。

## Main Contribution

一个可扩展、模拟驱动的环境，用于评估 AI agent 的迭代式物理约束模型拟合，提供逐判据的物理一致性反馈，作者认为其设计方法可推广到其他科学领域的模型拟合问题。

## Key Design Ideas

- 模拟器驱动的任务生成：单一随机种子控制轨道参数采样、观测调度、噪声注入，以及通过 Rebound 进行的 N-body 信号生成。
- 交互式拟合循环：用于执行分析代码的 Python REPL 加上 `submit_action` 提交接口，每次提交后返回逐判据通过 / 未通过诊断及可选提示。
- 以物理一致性作为成功门槛：统计判据（残差 RMS、逐点 ΔBIC）必须与物理参数恢复和正确行星数同时满足。
- 匿名化的真实数据子集：20 个档案系统，移除了目标与仪器标识，以防范来自已发表解的污染。

## Strengths

- 基于种子的模拟器生成带来可扩展的任务池，每个合成系统都有精确的 ground truth。
- 逐判据诊断将统计拟合质量与物理参数恢复区分开，使二者之间的差距可以被直接度量。
- 经典 baseline（Lomb-Scargle + 开普勒拟合流水线与嵌套采样）将难度尺度锚定在标准方法上。

## Limitations

- Repository note: 单一科学基底——全部 120 个任务都是径向速度模型拟合，作者关于该模拟驱动设计可推广到其他模型拟合领域的提法在论文中未经演示。
- Repository note: 四判据成功规则不给部分得分，且经典 baseline 未在 20 个真实档案任务上运行，因此 agent–经典方法的比较仅覆盖合成层级。

## Related Works

- [Aviary](./aviary.md) — 同样是为科学 agent 提供程序化奖励的交互式环境套件，但横跨多个领域的五个 language-grounded 环境，而非单一的物理模型拟合问题。
- [ScienceAgentBench](./scienceagentbench.md) — 同样评估 agent 的数据驱动科学分析，但以静态指标为独立生成的程序打分，而非运行带逐判据反馈的迭代拟合循环。
- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是可执行的科学 agent 任务，但由领域专家在五个领域中编写，而非在单一天体物理场景内由模拟器生成。
