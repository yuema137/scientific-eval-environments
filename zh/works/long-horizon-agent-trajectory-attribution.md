# Long-Horizon Agent Trajectory Attribution (2026)

> [English](../../works/long-horizon-agent-trajectory-attribution.md) | **简体中文**

> **首次公开：** 2026-08-07 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.06909)

## Overview

一个用于 *trajectory attribution*（轨迹归因）的 benchmark 与细粒度标注框架——即识别长 horizon LLM-agent 轨迹中的哪个组件（用户指令、工具调用、观测、记忆等）对某一观察到的结果（如任务对齐动作、不安全动作或安全拒答）负主要责任。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 面向任意 agent 轨迹（AgentDojo、Agent3Sigma）的轨迹归因 / 诊断方法学；作用于轨迹本身，而非某项科学/研究任务。

## Links

- **Paper:** https://arxiv.org/abs/2608.06909
- **Code:** https://github.com/chenjing-2024/agent-trajectory-attribution
- **Venue:** arXiv preprint (2026)

## Summary

现有 agent benchmark 主要评估行为结果，对细粒度归因分析的支持很有限。该工作提出轨迹归因这一任务，并为其构建一个 benchmark 加标注框架。异质的 agent 轨迹被组织于一套统一的组件 schema 之下，每条轨迹都标注其主要归因组件，并在适用处标注攻击链与执行链。该 benchmark 以取自 AgentDojo，以及 Agent3Sigma 的 Stage 与 Canary 设定的轨迹实例化，并定义两项带参考基线的评估任务。作者还发布了一套可复用的标注 skill，使来自新 agent 模型的轨迹能在同一归因框架下被标准化并标注。

## Tasks

该 benchmark 由 **1,351 条标注轨迹**组成。

按来源：
- AgentDojo：640 条轨迹
- Agent3Sigma（Stage 设定）：495 条轨迹
- Agent3Sigma（Canary 设定）：216 条轨迹

按结果类别：
- 任务对齐动作：409 条（30.3%）
- 不安全动作：532 条（39.4%）
- 安全拒答：410 条（30.3%）

轨迹被组织于一套统一组件 schema 之下，其中每个组件有一个 *role*（system、user、assistant 或 tool）与 *content*（用户指令、推理轨迹、工具调用、工具观测、检索到的记忆、以及最终动作）；工具调用及其观测被视为复合单元。每条轨迹都标注其主要归因组件，并在适用处标注攻击链与执行链。

定义两项评估任务：
- **主归因定位** — 识别标注的根因组件。
- **归因链恢复** — 在主因之外，恢复构成归因链的其他组件。

## Domains

N/A — 该 benchmark 评估的是通用 LLM-agent 轨迹（来自 AgentDojo 的工具使用 agent 与 Agent3Sigma 的安全设定），而非某个科学或工程学科。

## Evaluation

两项任务以排序指标计分：主归因定位使用 **Hit@1** 与 **Mean Reciprocal Rank (MRR)**；归因链恢复使用 **Recall@K** 与 **Mean Average Precision (MAP)**。

提供两个参考基线：
- **Incremental（轨迹贡献）** — 按轨迹展开过程中似然的变化为组件打分。
- **Leave-One-Out（组件级扰动）** — 以移除某组件的效应估计其重要性。

所报的跨全部目标的 micro 平均结果：Incremental——Hit@1 = 0.369、MRR = 0.616；Leave-One-Out——Hit@1 = 0.537、MRR = 0.713。论文指出，不同归因设定（局部、长程与结构化链归因）之间存在显著性能差异，给出对该 benchmark 难度的初步刻画。

## Typical Duration

所报的轨迹平均长度从 6.58 到 21.69 个组件不等，最长轨迹可达 97 个组件。归因距离（主组件与目标之间的间隔）平均为 2.41–3.93 个组件，最大可达 23 个组件。

## Main Contribution

将轨迹归因引入为长 horizon LLM-agent 的一项评估任务，并提供一套统一组件 schema、一个细粒度标注框架、一个含 1,351 条标注轨迹的 benchmark、两项带参考基线的评估任务，以及一套可复用的标注 skill，用于把该 benchmark 扩展到新 agent 模型的轨迹。

## Key Design Ideas

- **统一组件 schema**，以 role/content 字段表示异质的 agent 轨迹（指令、工具调用/观测、记忆、配置、skill 上下文），并把工具调用–观测对视为复合单元。
- **主组件标注加攻击链与执行链**，将单一根因与更广的贡献组件链区分开来。
- **两项归因任务**（定位与链恢复），以排序指标（Hit@1、MRR、Recall@K、MAP）计分。
- **基于扰动与似然的基线**（增量贡献与留一法）作为参考归因方法。
- **覆盖多样的归因设定**——在任务对齐、不安全与拒答三类结果上的局部、长程与结构化链归因。
- **可复用的标注 skill**，将构建协议可操作化，使新 agent 模型的轨迹能被一致地标准化与标注。

## Strengths

- 提供细粒度、组件级的归因标注，超越仅看结果的 agent benchmark（据论文）。
- 覆盖多个轨迹来源与结果类型（任务对齐、不安全、安全拒答），使归因分析能同时覆盖良性与安全相关行为（据论文）。
- 随附一套可扩展的标注协议/skill，意在标准化由新 agent 模型生成的轨迹（据论文）。

## Limitations

- 参考基线在不同归因设定间显示出显著性能差距，表明归因——尤其是长程与结构化链的情形——仍具挑战性（据论文）。
- Repository note: 该 benchmark 以两个上游来源（AgentDojo 与 Agent3Sigma）实例化，聚焦工具使用的安全/安保轨迹；对其他 agent 设定的覆盖取决于日后对所发布标注 skill 的使用。

## Related Works

- [MLE-Dojo](./mle-dojo.md) — 另一个 agent 评估环境，但聚焦机器学习工程任务，而非轨迹级归因。
