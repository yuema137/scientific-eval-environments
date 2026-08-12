# CRAFTS (2026)

> [English](../../works/crafts.md) | **简体中文**

## Overview

CRAFTS 是一套角色分工、经微调的 LLM agent 系统，用于自动构建可执行的化工过程仿真模型；随之一同提出的还有 OpenIDAES-450——一个含 450 个案例的 IDAES 过程仿真数据集，配有留出评测划分与结构化的校验契约。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** https://arxiv.org/abs/2608.01369
- **Code:** https://github.com/Galigeigei-Z/CRAFTS-Multi-agent-for-Equation-oriented-PSE

## Summary

CRAFTS（Collaborative Role-Adaptive Fine-Tuning of LLM Agents for Chemical Process Simulation）从自然语言请求与工艺流程图（PFD）证据出发，构建可执行的 IDAES/Pyomo 过程仿真模型。任务被拆解为七个边界清晰的角色，对应化学工程师分阶段推进的工作流；阶段之间由确定性的 IDAES/Pyomo 关卡校验带类型的中间产物。工作在同篇论文提出的 450 案例 IDAES 过程仿真数据集 OpenIDAES-450 上评测，使用工作流成功契约与结构 F1 指标，在冻结的留出划分上进行。

## Tasks

OpenIDAES-450 含 450 条面向用户的化工请求，每条配有可执行的 IDAES 过程模型、中间产物与执行记录。案例涵盖单元操作选型、拓扑构建、物性包指派、规格闭合、初始化、循环流处理、求解器诊断与优化。其中 82 条请求被冻结为留出测试集，所有报告结果均基于该集合；其余 368 条只用于训练与开发，来自同一源模型或同一模板的案例被划入同一侧，重复项已剔除。每个任务都要求由自然语言请求加 PFD 证据构建出可执行的过程模型，管线沿途输出带类型的中间表示——VisualGraphIR、TopologyIR、SpecIR、BuildPlan 与 SolveReport。TODO(reference) — 论文除称这 450 个案例经过精选、可审计之外，未说明其原始出处。

## Domains

化学工程——受评目标是在 IDAES/Pyomo 中自动构建可执行的化工过程仿真模型（流程图建模），这是围绕单元操作、物流与过程拓扑展开的过程系统工程任务。

## Evaluation

评分由两部分构成。一是工作流成功（Workflow Success, WS）契约：统计通过全部必需阶段的请求占比，这些阶段包括意图解读、拓扑校验、规格闭合、BuildPlan 编译、模型构建、初始化、求解器终止被接受，以及可选的优化。二是对照参考模型计算的三项宏平均 F1 结构指标：单元记录（UC）、物流记录（SC）与有向连接对（CC）。阶段之间的晋级关卡强制检查模式有效性、实体一致性、连通性、端口兼容性、单元可用性、物性包支持、自由度闭合、初始化、求解器终止与物理一致性。在冻结的 82 条请求划分上，CRAFTS 报告 91.5% WS，UC/SC/CC 的 F1 分别为 0.815 / 0.791 / 0.782，高于对既有系统的复现基线（CeProAgents 式 74.4% WS、Sketch2Simulation 式 76.8%、Text-to-Simulation 式 68.3%）、OpenAI Agents SDK 管线（79.3%）以及单模型基线（GPT-5 mini 54.9%、Claude Sonnet 4.6 45.1%、Gemini 3.5 Flash 28.0%）。消融分别去掉角色专属微调（36.6% WS）、化学工程知识（0%）、视觉证据（25.6%）、拓扑与规格的分离（30.5%）以及 Debug 重放（18.3%）。

## Typical Duration

TODO(reference) — 论文未报告单任务的 wall-clock 时间、token 预算或步数；唯一相关的数字是 82 个留出案例中有 75 个至少需要一次调试交互。

## Main Contribution

一种协作式、角色自适应的微调方案：把化工过程模型的构建拆给七个边界清晰的 LLM agent 角色，辅以带类型的中间表示与确定性的 IDAES/Pyomo 工程关卡；同时提出 OpenIDAES-450，以及在冻结留出划分上「工作流成功 + 结构 F1」的评测协议。

## Key Design Ideas

- 把过程模型构建拆为七个边界清晰的角色——输入理解、意图、视觉、拓扑与规格五位专家，外加 Debug 与 Optimization——以 LangChain/LangGraph 工作流编排。
- 只对三个与模式（schema）强相关的角色做 LoRA 微调（Visual Descriptor 基于 Qwen3-VL-8B-Instruct，拓扑与规格 agent 基于 Qwen2.5-Coder-7B-Instruct），其余四个角色保持未微调的本地部署 Qwen，配合注入领域知识的提示词。
- 在阶段之间插入确定性的 IDAES/Pyomo 晋级关卡，中间产物先通过校验再往下走。
- 用带类型的中间表示承载工程决策（VisualGraphIR、TopologyIR、SpecIR、BuildPlan、SolveReport），只有语义产物过关之后才挂上构造器、物性包与运行器。
- 用分阶段的工作流成功契约加上单元/物流/有向连接三项 F1 判分，而非单一的端到端通过与否信号。
- 冻结一份 82 条请求的留出划分，并把共享同一源模型或模板的案例分到同一侧，以限制泄漏。

## Strengths

- 贡献了一个具名数据集（OpenIDAES-450），带冻结的留出划分与明确的判分协议，而不只是一次系统演示。
- 评估落在可执行的仿真器（IDAES/Pyomo）上，校验的是构建出的模型能否真的建成、初始化并求解。
- 单元、物流与有向连接三项结构指标，能看出模型构建究竟在哪里失败，而不止于一个总成功率。
- 对比对象覆盖既有过程仿真 agent 系统的复现、通用 agent SDK 管线与单模型基线，并含五项消融，分别隔离微调、领域知识、视觉证据、角色分离与调试重放的作用。

## Limitations

- benchmark 只针对单一仿真器：所有任务都面向 IDAES/Pyomo 的方程式模型，结果无法说明 Aspen Plus、HYSYS 这类序贯模块化仿真器上的表现。
- Repository note: 公开仓库只提供架构预览，并声明源数据、benchmark 记录、模型权重与评测参考将在后续发布，因此截至本卡片撰写时，OpenIDAES-450 无法被独立复用。
- Repository note: 既有系统的基线是作者自行复现的「-style」版本，而非原始发布的系统，这削弱了对比的说服力。
- Repository note: 未报告任何运行时或 token 成本核算，因此无法评估七角色管线相对单模型基线的代价。

## Related Works

- [FEABench](./feabench.md) — 同样是 LLM agent 对照数值求解器构建并运行工程仿真。
- [MooseBench](./moosebench.md) — 同样评估 agent 搭建可执行的多物理场仿真。
