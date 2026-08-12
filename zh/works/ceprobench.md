# CeProBench (2026)

> [English](../../works/ceprobench.md) | **简体中文**

## Overview

CeProBench 是一个化工过程开发 benchmark，随 CeProAgents 一同提出——后者是一套面向化工过程开发自动化的分层多智能体系统。它按化学工程的三大支柱——知识、概念、参数——组织评估，设六类任务，涵盖从文档到知识图谱的抽取、工艺流程图（PFD）的解析与设计，以及 Aspen Plus 参数优化。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** <https://arxiv.org/abs/2603.01654>
- **Code:** <https://github.com/kronos7777777/CeProAgents>

## Summary

论文提出 CeProAgents：一个分层多智能体系统，三组 agent 分别对应过程开发中的知识、概念与参数三个侧面，每组都把动态 agent 讨论组与结构化的 agentic 工作流结合起来。为评估该系统，作者构建了 CeProBench——围绕同样三大支柱搭建的多维 benchmark，用六种任务类型端到端地考察过程开发能力。论文对所报告结果的定位有两层：既是所提架构的证据，也是对当前大语言模型在工业化工任务上能力边界的一次测量。

## Tasks

CeProBench 含 6 类任务，合计「243 道问题与 235 项具体任务」。六类任务分别是：Knowledge Extract（把非结构化技术文献转成形式化的知识图谱）、Knowledge Augment（为工程场景检索并综合专业上下文）、Concept Parse（把工艺流程图数字化为语义图）、Concept Complete（从欠定的拓扑中推断缺失的单元操作）、Concept Design（由自然语言描述生成 PFD）、Parameter Optimize（闭环细化操作参数）。

各维度的构建方式不同。知识维度取自 70 篇核心技术文档构成的精选语料，从中抽取出 4,406 个实体与 4,967 条关系，并按工艺路线选择、催化剂选择、生产方法与分离技术分层。概念维度使用 113 份源自全国大学生化工设计竞赛的 PFD，标注了拓扑结构，共含 986 个设备单元与 1,172 条连接。参数维度由 20 个高保真 Aspen Plus 备份文件与配套的结构化约束描述构成，覆盖 91 个可调参数与 65 个优化目标。

## Domains

化学工程。每个维度都是过程系统工程任务：围绕工艺路线、催化剂、生产方法与分离技术的文献；工艺流程图的解析、补全与设计；以及在 Aspen Plus 中验证的操作参数优化。化学在这里只是过程知识的背景学科——受评的目标是过程设计与装置操作决策，而非分子或反应预测。

## Evaluation

评分按维度分别设计。知识维度把正确性、合理性、清晰度、完整性四项推理质量判断与图谱完整性度量结合起来，后者包括实体 F1、召回率与准确率，以及针对抽取图结构的 Mapping-based Edge Connectivity（MEC）与 Mapping-based Edge Distance（MED）。概念维度中，解析任务对照专家标注计算设备与连接的准确率和召回率，补全任务对照真实单元操作计算 Top-K 准确率，设计任务则用体现工程逻辑校验的 Valid Rate 与 Correct Rate。参数维度把候选参数配置放进 Aspen Plus 执行，由此校验化学与热力学可行性，再汇总产率、纯度、成本、Effective Score 与 Comprehensive Score，同时以总迭代次数与取得最优结果的迭代次数来衡量收敛效率。

共评测五个基础模型：Gemini-3.0-Pro、GPT-5.0、Claude-4.5-Opus、Qwen-3.0-Max 与 DeepSeek-V3。报告称 Gemini-3.0-Pro 在多数维度上最强。

## Typical Duration

TODO(reference) — 论文未报告单任务的 wall-clock 时间、轨迹长度或 token 预算。参数维度报告的是以优化迭代次数计的收敛效率（总迭代次数与取得最优结果的迭代次数），而非时间或 token 预算。

## Main Contribution

按作者的表述，贡献有两项：CeProAgents——把化工过程开发拆解为知识、概念、参数三组 agent 的分层多智能体系统，每组都混合使用动态 agent 讨论组与结构化的 agentic 工作流；以及 CeProBench——围绕化学工程三大核心支柱组织、用六种任务类型整体考察过程开发能力的多维 benchmark。

## Key Design Ideas

- 把化工过程开发拆为知识、概念、参数三大支柱，并对称地用于 agent 架构与 benchmark 两侧。
- 六类任务贯穿开发全流程，而非单一问答形式：知识图谱抽取、检索增强的知识综合、PFD 解析、拓扑补全、PFD 生成与闭环参数优化。
- 参数维度采用仿真器落地的评分：候选操作参数在 Aspen Plus 中实际执行，由化学与热力学可行性而非文本相似度决定分数。
- 知识（实体/关系）与概念（设备单元/连接）两侧都以图结构作为标准答案，从而支持实体 F1、MEC/MED、连接准确率这类结构化指标。
- PFD 任务取自全国性化工设计竞赛而非合成生成，拓扑因此贴近工业化的设计实践。

## Strengths

- 端到端覆盖过程开发工作流，而非只考孤立的问答：六类任务分布在作者声明的三个维度上。
- 参数任务在 Aspen Plus 中执行落地，给出纯文本判分无法提供的客观可行性检验。
- 明确报告各维度的规模（70 篇文档、4,406 个实体 / 4,967 条关系；113 份 PFD，含 986 个设备单元与 1,172 条连接；20 个参数文件，含 91 个可调参数与 65 个目标）。
- 知识与参数数据集连同 CeProAgents 代码一并在项目仓库公开。

## Limitations

- 概念维度的数据取自全国大学生化工设计竞赛，并未公开发布；论文称可在合理请求下向通讯作者索取，这限制了这三分之一 benchmark 的完全可复现性。
- 参数维度的评测依赖有授权的 Aspen Plus 安装，环境无法自由复现。
- 绝对规模不大——六类任务共 243 道问题、235 项任务，参数场景只有 20 个——相对于所声明的三个维度要覆盖的范围，显得单薄。
- 知识维度的若干判分标准（正确性、合理性、清晰度、完整性）属于主观评判，而非执行验证的结果。
- Repository note: 该 benchmark 出自一篇以 CeProAgents 架构为主要主张的系统论文，因此所报告的数字是在作者自家的 agent 脚手架下产生的，而非来自与脚手架无关的评测框架。

## Related Works

- [FEABench](./feabench.md) — 同样把评估落在通过 API 驱动商业仿真软件上，与参数维度是同一种执行验证模式。
- [CFDLLMBench](./cfdllmbench.md) — 多层级的工程仿真 benchmark，从领域知识一直覆盖到端到端的仿真器配置。
- [Using Large Language Models for Solving Thermodynamic Problems](./llm-thermodynamics.md) — 同为化学工程评估，但聚焦热力学解题而非过程开发。
- [Simona](./simona.md) — 评估把过程描述自动转换为可收敛仿真流程图的能力，与概念、参数两个维度有重叠。
