# Imaging-101 (2026)

> [English](../../works/imaging-101.md) | **简体中文**

## Overview

Imaging-101 是一个含 57 个经专家验证的计算成像任务的 benchmark，横跨六个科学领域，每个任务都以一篇同行评审论文及其开源参考实现为依托，用来评估 LLM coding agent 能否搭出完整的重建管线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** https://arxiv.org/abs/2607.10789
- **Code:** https://github.com/AI4ImagingLab/imaging-101-release
- **Project:** https://starpacker.github.io/agent-imaging-website/

## Summary

计算成像要从间接且带噪的测量中还原出隐藏的信号，而搭起一条正确的重建管线，既要懂测量物理，也要懂数值反问题求解。Imaging-101 把 57 个这样的任务统一规范成四段式管线——预处理、正向物理建模、反问题求解、可视化——于是 agent 的产出可以逐段打分。三条评估赛道（规划、函数级单元测试、端到端重建）在同一套任务上考察 agent 的不同能力。论文评估了七个前沿 LLM，报告了算法选择、物理约定处理与管线整合三方面的系统性失败——这些都是通用编码 benchmark 暴露不出来的。

## Tasks

57 个任务，横跨六个科学领域：天文、生物、化学与材料科学、地球科学、医学与物理。每个任务都以一篇同行评审论文及其开源参考实现为依托；构建采用专家在环的流程：复现参考运行，把代码重构成统一的四段式布局，用捕获的输入/输出合成单元测试，并起草任务教程。每个任务附带 `README.md`、参考方案（`plan/approach.md`、`plan/design.md`）、数据、依赖清单、带 docstring 的逐函数签名、配对的 pytest 测试套件，以及一份记录验收阈值的 `metrics.json`。天文类任务包含若干 Event Horizon Telescope 黑洞成像变体（`eht_black_hole_original`——从受增益污染的可见度数据中还原黑洞射电图像——以及动态、不确定性量化、特征提取与层析成像等变体）、`exoplanet_imaging`（从日冕仪图像序列中检出暗弱的系外行星）、`lucky_imaging`（从短曝光视频重建高分辨率月面图像）、`shack_hartmann` 与 `shapelet_source_reconstruction`。各领域确切的任务数：`TODO(reference)`。

## Domains

天文是被点名的六个领域之一，具体落到射电干涉成像（从可见度数据重建 Event Horizon Telescope 黑洞图像）、高对比度系外行星成像、大气湍流下的幸运成像、Shack–Hartmann 波前传感，以及基于 shapelet 的源重建——每一项计分的产出都是一幅天文图像或一个源估计。其余任务组带来的共同领域为生物、化学、材料科学、地球科学、医学与健康，以及物理。

## Evaluation

三条赛道跑在同样的 57 个任务上。**规划赛道：** agent 产出算法文档与模块架构，按管线的各个组件（预处理、正向物理、反问题求解）分别打分，采用人机两段式流程——领域专家在每个维度上给出二元的通过/不通过；Overall 一栏要求三个组件全部正确。**函数级赛道：** 给定 README、参考方案以及目标函数的签名与 docstring，模型在沙箱环境中反复迭代，直到通过配对的 pytest 套件或耗尽预算；结果以 Module %（某模块内全部函数通过）与 Function %（单个函数通过）报告。**端到端赛道：** 只给 README、`data/` 与 `requirements.txt`，agent 必须产出完整的 `src/` 管线、执行它，并交出满足 `metrics.json` 中阈值的重建结果，评分用归一化互相关（NCC）与归一化均方根误差（NRMSE）。七个受评模型（Claude-4.6-Opus、DeepSeek-V3、Gemini-3.1-Pro、GPT-5.4、Qwen3.6-Plus、Kimi-k2.5、GLM-5）的主要结果为：规划 Overall 最佳 30/57（52.6%），函数级 Module Overall 最佳 13/57（22.8%），端到端成功率最佳 17/57（29.8%）。

## Typical Duration

论文未报告 wall-clock 或 token 预算。函数级赛道给每个函数固定 10 轮反思的预算上限；各模型成功所需的平均轮数在 2.60 到 9.28 之间。端到端赛道报告的成功平均轮数在 1.45 到 2.75 之间。

## Main Contribution

作者把它作为第一个针对科学计算成像、面向 LLM coding agent 的 benchmark 提出：57 个经专家验证、以论文为依托的任务，统一规范成同一条四段式管线，并配三条评估赛道，把规划、模块实现与端到端重建分开考察。他们对七个前沿 LLM 的评估指出了算法选择、物理约定处理与管线整合上的能力缺口，并认为这些缺口是计算成像特有的，通用编码 benchmark 并不会暴露。

## Key Design Ideas

- 把异构的成像论文统一规范成一条固定的四段式管线（预处理 → 正向物理建模 → 反问题求解 → 可视化），使得跨领域的失败可以归因到具体的阶段。
- 同一套任务上设三条自主程度递增的赛道：规划（只做设计）、函数级（给定参考方案，对照单元测试实现单个模块）、端到端（仅凭 README 与数据搭出并跑通整条管线）。
- 每个任务都以一篇同行评审论文加其开源参考实现为依托，单元测试由捕获的参考输入/输出合成。
- 数值验收阈值逐任务写在 `metrics.json` 中，图像质量以 NCC 与 NRMSE 计分，而不是文本相似度。
- 规划采用人机协同判定：领域专家在 LLM judge 辅助下对每个管线组件给出二元通过/不通过，Overall 要求各组件全部正确。

## Strengths

- 以执行而非答案匹配来评分：端到端任务通过运行 agent 的代码、并按标定好的容差衡量重建质量来打分。
- 三赛道设计能区分模型究竟是败在算法选型、单个模块的实现，还是整条管线的集成。
- 确实是多领域的，且天文部分覆盖的是真实的、与具体仪器绑定的重建问题（干涉可见度、日冕仪、波前传感），而不是泛泛的图像复原。
- 代码与评估工具以 MIT 许可证发布，并有公开的项目页。

## Limitations

- 绝对分数偏低使信号高度集中：端到端最好成绩只有 17/57，因此这套 benchmark 目前主要在其量程的低端区分模型。
- 规划赛道由专家在 LLM judge 辅助下逐组件给出二元通过/不通过，比基于执行的赛道更粗，也更难复现。
- Repository note: 正文未给出各领域的任务数，因此天文部分相对其余五个领域的体量无法从原始文献核实。
- Repository note: 函数级赛道提供了参考方案与函数签名，所以它衡量的是「设计已经正确」前提下的实现能力，而非自主的问题形式化。

## Related Works

- [SciCode](./scicode.md) — 以研究为依托的科学编码任务，拆解成子问题并以执行判分。
- [ResearchCodeBench](./researchcodebench.md) — 为近期论文中的方法编写代码，对照参考实现判分。
- [AstroVisBench](./astrovisbench.md) — 专门评估 agent 编写的天文分析与可视化代码。
- [ScienceAgentBench](./scienceagentbench.md) — 数据驱动的科学发现任务，通过执行 agent 产出的代码判分。
