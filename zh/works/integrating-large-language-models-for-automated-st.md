# Integrating Large Language Models for Automated Structural Analysis (2025)

> [English](../../works/integrating-large-language-models-for-automated-st.md) | **简体中文**

## Overview

一个手工编制的 benchmark，含二十道二维框架的结构分析应用题（structural analysis word problems, SAWP）并附 ground-truth 解；作者用它在一个以 OpenSeesPy 为后端的框架内对比四个 LLM，并测量其中最强者在多次运行间的稳定性。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.09754>
- **Venue:** arXiv preprint (cs.SE), 2025 年 4 月 13 日

## Summary

论文提出一个框架，让 LLM 充当核心引擎：解析结构的自然语言描述，把它翻译成可执行的 Python 脚本，由脚本驱动 OpenSeesPy 做有限元分析、驱动 OpsVis 做可视化。由于公开数据集中没有一份系统地把结构描述、清晰布置图与 ground truth 配成一套，作者手工设计了一个二十题的结构分析应用题 benchmark 来做评测。基于该 benchmark 共做三组实验：四个基座模型的 best-of-three 对比、对最强模型的五次运行生成稳定性研究，以及针对专家撰写的系统指令的消融。框架为每道题产出一份结构化报告，内含题目描述、生成的代码、解释说明，以及各节点的内力及其最大值与最小值。

## Tasks

二十道二维框架的结构分析应用题（SAWP），由人工设计并配有对应的 ground-truth 示意图。每道题按统一格式给出五个组成部分：几何属性、材料属性、荷载条件、边界条件，以及结果可视化的要求。要求输出的是框架的变形与内力——轴力、剪力与弯矩。题目由三种模式从种子样例改编而来：模式 1 改变层数与跨数（从一跨一层框架一直扩展到三跨两层）；模式 2 引入不对称，例如第一跨两层、旁边第二跨一层；模式 3 添加工程实践中常见的结构构件，具体是斜杆与悬臂梁。典型算例取柱高 4 m、大梁跨度 6 m、水平集中荷载 2,000 N、竖向均布荷载 1 × 10⁴ N/m，E = 2 × 10¹¹ Pa，柱截面面积 2 × 10⁻³ m²、大梁截面面积 6 × 10⁻³ m²，惯性矩分别为 1.6 × 10⁻⁵ m⁴ 与 5.4 × 10⁻⁵ m⁴。所有支座均为固定支座。完整题集见附录 A，ground-truth 解见附录 C。

## Domains

土木与结构工程。受评目标是二维建筑框架的结构分析——柱、大梁、悬臂梁与斜杆在集中荷载与均布荷载作用下的响应——判分对象是变形与内力。作者把工作置于土木工程之内，并指出该 benchmark 瞄准的是一种基础性的结构形式，之后才谈得上扩展到高层建筑与桥梁。未指派共同领域；OpenSeesPy 与 OpsVis 是工具，而非受评目标。

## Evaluation

- **对比分析（best-of-3）。** 每道题的每组实验连续跑三次，只要三次中至少有一次给出正确响应即算解出，作为模型之间的上界对比来报告。二十道 SAWP 的结果：GPT-4o 100%，GPT-4 85%，Gemini 1.5 Pro 80%，Llama-3.3 30%。
- **生成稳定性。** 框架内的 GPT-4o 每题运行五次，准确率定义为生成出正确且完整解答的概率。九道题达到 100%（第 1、4、7、8、15、17、18、19、20 题），八道题落在 60–80% 区间（第 2、3、5、6、9、10、12、16 题），三道题只有 40%（第 11、13、14 题）。二十道题全部产出了完整且可执行的 OpenSeesPy 代码。性能下滑集中出现在不对称框架上。
- **指令消融。** 在第 20 题上，Gemini 1.5 Pro 与 GPT-4o 各在「有 / 无均布荷载方向指令」两种条件下独立运行十次。没有该指令时，Gemini 无法正确定义均布荷载，GPT-4o 达到 70%；加上之后，GPT-4o 达到 100%。论文另报告，融入领域专属指令后，结构构形不对称的题目性能提升了 30%。
- **错误分类。** 可运行脚本中的失败分两类：第一类是框架未能勾勒出所要求的结构布置（跨数或层数错误、漏掉节点、单元定义有误）；第二类是边界条件出错或荷载指派错误，例如把左侧的集中荷载施加到一层的所有节点上。

## Typical Duration

`N/A — the paper reports no per-task wall-clock, token, or cost budget.` 论文只提到大多数基于 API 的任务能在每次请求几秒内完成。重复采样的预算是：模型对比每题三次，稳定性研究每题五次，指令消融每题十次。

## Main Contribution

作者提出首个把 LLM 与结构分析软件系统性整合起来做自动化分析的框架，并给出一个精心编制、附带 ground truth 的二十题结构分析应用题 benchmark——正好填上他们指出的那处空白：没有公开数据集系统地把结构描述、清晰布置图与 ground-truth 解配成一套。

## Key Design Ideas

- benchmark 由三种具名的生成模式构建（扩展层数与跨数、引入不对称、加入斜杆与悬臂），难度因此沿着明确的结构维度变化，而不是随意堆砌。
- 每道题都用同一套五组成部分的标准化描述格式，并同时准备 ground-truth 示意图用于校验输出。
- 两个不同的问题各用一套协议：模型间的能力上界对比用 best-of-three，单个模型的生成稳定性则用五次独立运行。
- 系统指令被当作一个由结构工程师撰写的实验变量，拆解为方向推理、数量推理与空间合理性推理，其作用单独测量。
- 上下文学习提示被模板化为四个带标签的块（通用模板、任务专属模板、ICL 示例、问题），并以单个参考样例带动模式泛化。
- 泛化能力的探查方式是只给框架一个参考样例——一跨一层框架——看它能否推广到样例中没有的多跨多层、悬臂与斜杆构形。

## Strengths

- best-of-three 与五次运行两套协议，把「模型能做到什么」与「模型能稳定做到什么」分开，而且稳定性结果是逐题报告的，不是一个平均值。
- 指令消融是一次干净的受控对比：单道题、每种条件十次独立运行，隔离出一条专家撰写的指令。
- ground-truth 解与完整题集都收入附录，因此该 benchmark 仅凭论文本身即可复现。
- 错误分类把布置错误与边界及荷载错误区分开来，作者也正确地把部分失败归因于框架纯文本的接口——模型看不到自己画出来的东西。

## Limitations

- 二十道题，且都是相对简单的二维框架，作者自己也说这些题对结构工程专业人员而言并不难。
- 只做平面框架的静力线弹性分析；三维体系、非线性、动力问题与设计决策均未涉及。
- 题集部分借助 LLM 生成——作者由人工定义的题目描述让 LLM 生成代码，再复核结果——因而 ground truth 的一部分负担压在人工审核上。
- 正确与否是对照事先准备的示意图与预期输出来判定的，而非依靠一套自动化的数值比对协议，论文也未给出容差阈值。
- 模型覆盖止步于 GPT-4o、GPT-4、Gemini 1.5 Pro 与 Llama-3.3，都是 2025 年初的当红模型。
- Repository note: 论文未说明代码或数据集的公开情况，不过题集与 ground-truth 解见于附录。

## Related Works

- [A Lightweight Large Language Model-Based Multi-Agent System for 2D Frame Structural Analysis](./a-lightweight-large-language-model-based-multi-age.md) — 另一团队独立提出的同期工作，同为 20 题、同样面向 OpenSeesPy 的二维框架 benchmark。
- [A Large Language Model-Empowered Agent for Reliable and Robust Structural Analysis](./a-large-language-model-empowered-agent-for-reliabl.md) — 同样测量结构分析中多次运行间的稳定性，在梁上给出了形式化的可靠性与鲁棒性指标。
- [StructureClaw](./structureclaw.md) — 同样评估 agent 在 OpenSees 支撑下做结构分析，规模为工作台级，并采用冻结的参考求解器响应。
- [FEM-Bench](./fem-bench.md) — 同样为有限元代码生成判分，粒度是课程级的单个函数，而非整模型构建。
