# MaD Physics (2026)

## Overview

MaD Physics（Measuring and Discovering Physics）是一个 benchmark，用于评估 agent 能否在固定的成本预算下规划信息量大的测量，并根据收集到的数据推断底层的物理定律。它涵盖三个模拟环境——经典力学、流体力学和量子力学——每个环境还提供经过改动的物理定律，以控制记忆性知识的影响。

## Topics

- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.10820>
- **Project:** <https://mad-physics.github.io/>

## Summary

MaD Physics 认为，现有的科学发现 benchmark 要么考察静态的知识回忆，要么考察不受约束的实验设计，因而忽视了 agent 在约束下进行测量与规划的能力。它将发现过程刻画为两个阶段：在每个 trial 中，agent 用固定预算对系统进行测量——每次观测都按其保真度定价——随后推断底层定律以预测系统的未来状态。在三个基于不同物理定律的环境上，并配以改动物理定律的变体以缓解记忆性知识带来的污染，作者用四个 Gemini 模型进行评测，报告了它们在结构化探索与数据收集能力上的不足。

## Tasks

三个模拟环境，每个都建立在一条不同的物理定律上：经典力学（D 维空间中的 N 个粒子）、流体力学（二维不可压缩黏性流体）和量子力学（二维盒子中的两个粒子）。每个环境都以正常配置以及若干改动物理定律的配置呈现——就经典力学而言，包括各向异性惯性、改动的 1/r 引力定律以及涟漪势——此外还有一个同时施加多种改动的组合设置。所有环境均用 JAX 实现，agent 通过对模拟器发出测量代码来收集数据。

## Domains

横跨三种体系的模拟实验物理：经典力学、流体动力学和量子力学。

## Evaluation

- **Two-phase protocol.** 在测量阶段，agent 反复查询模拟器，直到耗尽预算；在预测阶段，它推断定律并预测被查询时刻的系统状态。
- **Fidelity-priced measurements.** 每次观测对 Low、Medium、High 三个保真度级别分别花费 2、5、10 的成本——噪声分别为 0.1、0.01、0.001——总花费受每个 trial 的预算限制，经典与流体环境为 200，量子环境为 30。
- **Prediction error.** 相对真实未来状态的预测误差是主要指标，越低越好：经典力学用 normalized RMSE，流体与量子力学分别用涡量与概率密度上的 L2 误差，每项都在 33 个随机初始化上取平均。
- **Prompting conditions.** 每个模型都用一个基础 prompt 和一个带策略的 prompt 运行。
- **Reported.** 在正常的经典力学配置、基础 prompt 下，预测误差为 Gemini 2.5 Flash Lite 6.61、Gemini 2.5 Flash 5.97、Gemini 2.5 Pro 1.93、Gemini 3 Flash 0.29；在改动物理定律的配置下，较小模型的误差急剧上升，且未报告人类基线。

## Typical Duration

没有固定的步数或 wall-clock 上限；一个 trial 的长度由测量预算界定——经典与流体为 200，量子每个 trial 为 30。生成的测量代码运行时间限制为 30 秒，最多重试 5 次，模型的 thinking budget 设为 4,000 个 token。

## Main Contribution

一个将科学发现刻画为有预算约束的测量的 benchmark——按保真度为每次观测定价并对总花费设上限——使得 agent 必须在资源约束下同时推断一条未知的、有时被改动的物理定律并规划其数据收集。

## Key Design Ideas

- 两阶段 trial：先是有预算约束的测量阶段，再是推断与预测阶段。
- 按保真度定价的观测，成本随精度严格递增，因此在固定预算下测量质量与数量直接相互权衡。
- 改动的物理定律——各向异性惯性、改动的引力、速度与涡量调制、纠缠标度——以削弱记忆性教科书物理带来的污染。
- 面向经典、流体与量子系统的可微 JAX 模拟器，通过 agent 生成的测量代码进行查询。

## Strengths

- 将测量质量与数量之间的权衡变成一个显式的、可评分的约束，而非事后统计量。
- 改动物理定律的变体将真正的信息寻求与对标准定律的记忆区分开来。
- 横跨三种物理体系的可执行模拟器提供确定性、可复现的评分。

## Limitations

- Repository note: 每个环境都是带有人为设定的合成成本函数的模拟物理系统；在该预算下的表现能否迁移到真实实验的成本结构，未被评估。
- Repository note: 报告的结果仅涵盖四个 Gemini 模型，没有人类或非 Gemini 的 baseline，因此绝对难度与跨模型族的普适性尚未确立。

## Related Works

- [SimulCost](./simulcost.md) — 同样对 token 之外的科学资源定价，但其单位是物理模拟时间与实验资源，而非 agent 为揭示未知定律而花费的测量保真度。
- [CATP-LLM / OpenCATP](./catp-llm.md) — 同样把资源成本作为 agent 优化的显式目标，但针对的是一般任务规划中的 tool-use 成本，而非固定物理预算下的测量保真度。
- [CostBench](./costbench.md) — 同样考察成本感知的决策，但针对的是通用 tool-use 中的 tool-call 预算，而非物理模拟器内部的实验测量。