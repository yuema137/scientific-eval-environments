# BAGEN (2026)

> [English](../../works/bagen.md) | **简体中文**

## Overview

BAGEN 是一个评估 benchmark，用于测试 LLM agent 是否具备预算意识（budget-aware）——即能否在执行过程中估计自身还剩多少资源预算、以及任务是否仍可完成——从而把预算当作主动的控制信号，而非事后统计的成本指标。它在四个环境中评估五个 frontier agent，并把预算意识形式化为渐进式区间估计（progressive interval estimation）：agent 在每一回合都需预测其剩余预算的上界与下界。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.00198>
- **Project:** <https://ragen-ai.github.io/bagen/>
- **Code:** <https://github.com/mll-lab-nu/BAGEN>

## Summary

BAGEN 认为，当前 agent 的成本大多只在执行结束后才被测量，因而 agent 从不会在任务仍在进行时把预算当作需要推理的对象。它沿两条轴定义预算——来自模型自身 token 生成的内部预算（internal budget），以及来自环境中动作的、多维的外部预算（external budget）——并借助 rollout-replay 协议把预算意识重新表述为渐进式区间估计。在四个环境与五个 frontier agent 上，它发现任务成功率与预算意识仅弱相关（r = 0.35），且 frontier 模型始终过度乐观，但该信号是可训练的：early stopping 在失败轨迹上可节省 28–64% 的 token。

## Tasks

四个环境提供任务：8×8 网格上的 Sokoban 推箱子、Search-R1 多跳检索、SWE-bench GitHub issue 修复，以及 Warehouse——一个由真实企业数据构建的供应链环境。前三个考察内部 token 预算，Warehouse 则考察在时间、仓储占用与累计成本上的、多维的外部预算。BAGEN 在 Sokoban、Search-R1 与 Warehouse 上为每个模型生成 128 条 rollout，在 SWE-bench 上生成 64 条；rollout-replay 协议把每个非终止回合转化为一个估计样本，每个模型–任务对共产生 2,000–3,000 个样本。

## Domains

交互式规划谜题、多跳问答、软件 issue 修复与供应链运营。

## Evaluation

- **Feasibility Macro-F1.** 对任务是否仍可完成的二分类预测，可在完整 trajectory 上（all-turn）或仅在首回合（first-turn）计算。
- **Fail-F1.** 仅限于最终失败的任务，衡量 agent 多早能检测到一次不可能完成的运行。
- **Interval Score.** 兼顾覆盖率（coverage）——即实际预算是否落入所预测的下界与上界之间——以及紧致度（tightness），后者惩罚过宽的区间。
- **Reported.** 在 GPT-5.2 Instant、Claude Opus 4.7、Claude Sonnet 4.6、Gemini 3.1 Pro 与 Qwen3-235B 上，任务成功率与预算意识的相关性仅为 r = 0.35，且这些模型始终过度乐观；early stopping 在失败轨迹上节省 28–64% 的 token，而总体成功率仅下降 1.6–4.2 个百分点；supervised fine-tuning 把受训的 Qwen-7B 的可行性判断准确率从 25.5% 提升到约 90%，但区间覆盖率在 SFT+RL 之后也仅从 10.5% 升至至多 47%。

## Typical Duration

每个任务的预算按环境设定上限：Sokoban 为 2,500 token，Search-R1 为 3,500 token，SWE-bench 为 160 回合，Warehouse 则是在时间、仓储占用与成本上的多维上限。预算耗尽即为其 horizon——任务在达到上限或 agent 自行停止时结束。

## Main Contribution

一个把 agent 资源消耗重新表述为在线预测问题的 benchmark——对剩余内部与外部预算进行渐进式区间估计——并表明由此得到的预算意识信号与任务成功率仅弱相关，却可训练到足以驱动 early stopping。

## Key Design Ideas

- 预算分为内部预算（模型自身推理新生成的 token）与外部的、D 维的预算（动作在环境中所承担的成本）。
- 预算意识被形式化为渐进式区间估计：在每一回合预测剩余预算的下界与上界，或宣告任务不可能完成。
- 一种 rollout-replay 协议，把预先收集的 trajectory 中每个非终止回合作为一个独立的估计样本来评分。
- 可训练的预算控制：先在区间目标上做 supervised fine-tuning，再用 GRPO reinforcement learning 奖励既紧致又能覆盖真值的区间。

## Strengths

- 把成本从事后统计转变为逐回合的控制信号，使 agent 原则上能在把预算花在无法取胜的任务之前就停止。
- 同时覆盖内部 token 预算与外部的多维动作预算（时间、仓储、成本），而不仅仅测量 token。
- rollout-replay 评分把预算估计与策略质量解耦，从而把预算意识作为一种可在五个 frontier 模型间测量的能力单独分离出来。

## Limitations

- Repository note: 区间校准依旧偏弱——即便经过 SFT+RL，覆盖率也只达到 47%——因此所预测的预算边界尚不可靠。
- Repository note: 可训练性结果来自单一开源模型（Qwen-7B）；五个 frontier agent 均为 zero-shot 评估，本身并未针对预算意识做微调。

## Related Works

- [CostBench](./costbench.md) — 同样把资源成本作为一等的评估目标，但衡量的是已完成 tool-use 计划的成本最优性（cost-optimality），而非 agent 对自身剩余预算的逐回合预测。
- [SimulCost](./simulcost.md) — 同样为非 token 资源定价，但对 agent 必须精打细算的物理仿真时间与实验成本计费，而非要求其预测预算耗尽区间并提前停止。
- [CATP-LLM](./catp-llm.md) — 同样面向成本感知的 agent 行为，但它是优化性能–成本权衡的 tool-planning 方法，而非探测 agent 能否在执行中估计剩余预算的 benchmark。