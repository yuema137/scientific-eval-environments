# SciVisAgentBench (2026)

> [English](../../works/scivisagentbench.md) | **简体中文**

## Overview

SciVisAgentBench 是一个 benchmark，评估把自然语言意图转化为可执行的科学数据分析与可视化（SciVis）任务的 agent，覆盖多步骤、贴近真实的分析场景。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2603.29139
- **Project:** https://scivisagentbench.github.io/
- **Code:** https://github.com/KuangshiAi/SciVisAgentBench
- **Venue:** IEEE Transactions on Visualization and Computer Graphics (IEEE VIS 2026)，据官方项目页

## Summary

SciVisAgentBench 是一个全面、可扩展的 benchmark，在贴近真实的多步骤分析场景中评估科学可视化 agent。它以一套结构化分类法为基础，横跨四个维度——应用领域、数据类型、复杂度级别与可视化操作——并为任务套件配上一条多模态、以结果为中心的评估流水线，将 LLM 评判与确定性验证器相结合。作者还与 SciVis 专家做了一项效度研究，考察人类与 LLM judge 之间的一致性，并为代表性的 SciVis agent 与通用编码 agent 报告了初步基线。它被定位为一个用于系统比较与失败模式诊断的「living benchmark」。

## Tasks

108 个专家精心制作的案例，覆盖多样的 SciVis 场景。案例按四维分类法组织：

- **应用领域：** 天文学、医学、生物学、物理学、地球系统科学、数学、化学。
- **数据类型：** 标量、矢量与张量场；多变量与时变数据。
- **复杂度级别：** operations（基本过程）、tasks（结构化操作序列）与 workflows（多阶段相互关联的任务）。
- **可视化操作：** 15 个类别，包括颜色与不透明度映射、数据采样与分辨率控制、场计算、体渲染，以及科学洞见提炼。

该 benchmark 横跨多个可视化平台/工具（如 ParaView、基于 napari 的生物影像工具、分子动力学工具与拓扑工具），并支持不同交互范式（CLI、MCP 协议、Python API）。Repository note: 官方项目页报告的划分是 74 个 task 级与 34 个 workflow 级案例；论文的三级复杂度分类法（operations/tasks/workflows）在所查阅来源中未与这一两分划分完全对齐。

## Domains

科学可视化，横跨天文学、医学、生物学、物理学、地球系统科学、数学与化学。

## Evaluation

一条多模态、以结果为中心的评估流水线，将 LLM（多模态 LLM）评判与确定性验证器相结合：

- **基于图像的指标：** PSNR、SSIM、LPIPS，并有考虑任务完成率与多视角渲染的缩放变体。
- **代码检查器：** 对代码生成解的脚本验证与执行。
- **基于规则的验证器：** 对离散输出的确定性评估。
- **case 专属评估器：** 定制脚本（如拓扑任务、坐标验证、可视化状态校验）。

一项有 12 位 SciVis 专家参与的效度研究考察人类–LLM judge 一致性。报告数字包括人类间 Krippendorff's α 为 0.719（剔除离群值后），以及 LLM judge（报告为 Claude-Opus-4.6）与人类评分之间 0.808 的 Pearson 相关，judge 稳定性得分为 0.975。

## Typical Duration

TODO(reference) —— 所查阅来源未给出每案例的轨迹长度、wall-clock 时间或 token 预算，尽管跨 agent 比较了 token 用量（如 token 效率比较）。

## Main Contribution

一个有原则、可复现且可扩展的 benchmark，用于评估科学数据分析与可视化 agent：它把 108 个专家精心制作案例的结构化四维分类法，与一条多模态、以结果为中心的评估流水线以及一项人类–LLM judge 效度研究结合起来，建立初步基线并揭示能力差距。

## Key Design Ideas

- 结构化四维分类法（应用领域、数据类型、复杂度级别、可视化操作），组织 108 个案例。
- 多模态、以结果为中心的评估，将 LLM/MLLM judge 与确定性验证器（图像指标、代码检查器、基于规则的验证器、case 专属评估器）相结合。
- 考虑任务完成率与多个渲染视角的图像指标缩放。
- 人类–LLM judge 对齐研究，为 LLM 评判提供依据。
- 平台与范式无关的测评框架，支持 CLI、MCP 服务器与 Python API，案例以 YAML 配置。
- 定位为一个「living」/可扩展的 benchmark。

## Strengths

- 覆盖多个科学领域、数据类型与 15 类可视化操作，范围广泛（论文）。
- 将主观的 LLM 评判与确定性的、基于执行与图像的验证器相结合，而非依赖单一评分方式（论文）。
- 含一项显式的人类–LLM judge 效度研究，并报告一致性统计（论文）。
- 同时评估专用 SciVis agent 与通用编码 agent（论文）。

## Limitations

- 受评基线既含专用 SciVis agent（ChatVis、ParaView-MCP、GMX-VMD-MCP、BioImage-Agent、TopoPilot），也含通用编码 agent（Claude Code、Codex）；报告结果表明通用编码 agent 在多数任务套件上优于专用 agent，而部分专用 agent 更省 token（论文）。
- Repository note: 若干报告数字（每案例时长/token 预算、确切的 task/workflow 划分）在所查阅来源中未完全给定，标记为 `TODO(reference)` 或作为项目页数字。

## Related Works

- TODO(reference) —— 相关的 SciVis / agent 评估工作，待对应卡片存在后链接。
