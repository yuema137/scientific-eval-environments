# A Case Study of Evaluating AI Agents on a Neuroscience Data-to-Discovery Pipeline (2026)

> [English](../../works/a-case-study-of-evaluating-ai-agents-on-a-neurosci.md) | **简体中文**

## Overview

一项实证案例研究，在一条真实的果蝇光遗传学「数据到发现」流程上评估通用编码 agent，考察它们能否自动化科学家平日手工搭建的软件工程环节，评估标准以领域专家的做法为依据。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** https://arxiv.org/abs/2606.07718
- **Code:** https://github.com/kaihorstmann/neuro-d2d-eval
- **Venue:** Third Conference on Language Modeling (COLM 2026)

## Summary

这项工作研究编码 agent 能否搭建一条神经科学研究流程的各个计算环节——该流程分析果蝇在光遗传学扰动下的行走行为。agent 需要在规模远超既有 agent benchmark 的任务与数据集上产出正确、稳健的代码，评判依据是专家的人工标注与可信的遗留代码库。研究发现，agent 能解决若干单独的流程阶段，但尚无法把它们组合成一次正确的端到端发现；研究还识别出若干失败模式——在没有预设成功判据下推理、视觉自评能力薄弱、计算资源管理、以及对留出数据的泛化——这些在以往 benchmark 中大多缺席。作者从中提炼出构造科学任务、以及为开放式问题设定严格评估标准的原则。

## Tasks

该流程被拆解为七个单阶段任务，依次为：Body Tracking、Registration、Keypoint Tracking、Behavior Feature Computation、Walking Behavior Classification、Gait Segmentation 与 Statistical Comparisons。除这七个单阶段任务外，研究还运行了提示指导程度不同（一个最简与一个最全提示）的端到端流程变体；发布的测评框架共含九个计算任务。每个 agent–任务对运行 3 次试验。任务与评测框架已公开，并声称兼容 Harbor agent 评测框架。

## Domains

神经科学——分析果蝇（*Drosophila*）在光遗传学扰动下的行走行为，涵盖基于视频的身体/关键点追踪、行为分类、步态分析，以及跨遗传驱动（GAL4）品系与遗传对照组的统计比较。

## Evaluation

每个阶段都带有以领域专家标准为依据的成功判据；agent 的解答同时对照专家人工标注与可信的遗留（科学家编写）代码库。在统计比较阶段，输出用 Mann–Whitney U 检验评估，将每个实验神经元类型与一个遗传对照相比。评估在单阶段设定下按阶段进行，在端到端设定下则对各构成阶段独立进行。在报告的运行中，73% 的 agent–任务对在 3 次试验上给出一致的通过/失败裁决。Repository note: 论文报告的部分更细粒度的按阶段通过计数无法从一手来源可靠转录，留作 TODO(reference)。

## Typical Duration

任务提示模板包含一个明确的完成时限，论文在附录中报告了各任务的 token 用量与运行时长；具体预算此处未转录。TODO(reference)。

## Main Contribution

在一条真实、专家级的神经科学数据到发现流程上，对通用编码 agent 做实证评估——所用任务与数据集大于既有 benchmark，判据以领域专家标准为依据——表明阶段级自动化可行，而正确的端到端发现尚不可行，并提炼出构造科学任务、为开放式问题设定严格评估标准的原则。

## Key Design Ideas

- 把一条真实科学流程拆解为有序阶段，每个阶段都有专家定义的成功判据，从而支持阶段级与端到端两种评估。
- 让正确性以专家人工标注与可信遗留代码库为依据，而非 agent 自报。
- 使用远大于以往 agent benchmark 的数据集（约 47 GB 果蝇行为数据，经 HuggingFace 发布），把计算资源管理与留出数据泛化暴露为评估维度。
- 评估多种 agent scaffold 与后端模型：Claude Code（claude-opus-4-6）、Codex（gpt-5.4）与 Terminus-2（分别配 claude-opus-4-6 与 gpt-5.4）。
- 分析 agent 的代码迭代轨迹，刻画它们*如何*成功或失败，包括尝试对中间输出做视觉检视以自评。

## Strengths

- 任务与数据集取自一条真实研究流程，且大于既有 agent benchmark，判据由领域专家设定。
- 分别测量单阶段与端到端表现，把组合/集成隔离为一种独立的失败模式。
- 暴露出以往 benchmark 大多缺席的评估维度：无预设成功判据下的推理、视觉自评、计算资源管理，以及对留出数据的泛化。
- 公开发布任务、评测框架与数据集。

## Limitations

- 单一流程、单一子领域（果蝇行为神经科学）的案例研究；研究本身未确立向其他科学流程的泛化。
- 报告的按阶段通过率依赖少量试验（每个 agent–任务对 3 次），部分细化的按阶段数字此处未转录（TODO(reference)）。
- Repository note: 具体的神经生物学假设（哪些神经元类型 / 多少条 GAL4 品系）在可获取文本中以操作方式描述，而非陈述为一个明确科学问题；确切计数留作 TODO(reference)。

## Related Works

- [BixBench](./bixbench.md) —— 生命科学领域另一项数据分析/发现式的 agent 评估。
- [ScienceAgentBench](./scienceagentbench.md) —— 以专家为依据的判据评估编码 agent 在数据驱动科学任务上的表现。
