# MatTools (2025)

> [English](../../works/mattools.md) | **简体中文**

## Overview

MatTools 评测大语言模型使用材料科学工具的能力：69,225 个问答对考察对 pymatgen 代码库的理解，另有一套 49 个真实任务（138 个子任务），要求模型生成并执行可运行的 Python 代码来回答材料性质问题。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.10852>
- **Venue:** arXiv preprint (cond-mat.mtrl-sci), 2025

## Summary

正确使用材料软件本身是一项技能，MatTools 分两部分测量它：一个从 pymatgen 代码库与文档派生的 69,225 对问答 benchmark（模型懂不懂这些工具？），以及一个含 49 个任务、138 个子任务的真实 benchmark（模型须写出并运行可用的 Python 来算出答案）。跨模型的发现有违直觉：通用模型胜过专用模型、更大的模型在 AI 相关任务上更好（「AI 懂 AI」），而更简单的方法常常胜过繁复的（「少即是多」）。

## Tasks

两部分：对 pymatgen 的 69,225 对工具理解问答，以及 49 个真实任务（138 个子任务），要求生成并执行可运行的 Python；带执行的代码生成 benchmark，非多轮 agent 循环。

## Domains

材料科学——计算材料工具使用：理解并编程 pymatgen 库以做性质计算。

## Evaluation

- 工具理解问答准确率，加真实代码生成成功率（生成并执行）。
- **报告。** 通用模型胜过专用模型；更大的模型在 AI 相关任务上更好；更简单的方法常胜过繁复的。摘要无单一头条数字。

## Typical Duration

按题的问答与按任务的代码生成回合；经执行验证。

## Main Contribution

对「LLM 能否真正操作材料软件」的两级测量——把「懂工具」与「写出能用工具的可运行代码」分开。

## Key Design Ideas

- 把理解与代码生成分开，定位工具使用在哪里失效。
- 带执行的真实 pymatgen 任务使正确性客观。
- 「通用胜过专用」的发现挑战了「领域微调」的惯性。

## Strengths

- 大规模理解集（69,225 对）加经执行验证的真实任务。
- 对构建材料编码助手有可落地的元结论。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与 Comments 编写（2026 年 8 月）；arXiv 页面无官方代码/数据集 URL，各模型数字在正文中。arXiv 元数据无发表信息。

## Related Works

- [MatViX](./matvix.md) — 同样是模型做结构化材料计算，走抽取而非工具代码。
- [LLM4Mat-Bench](./llm4mat-bench.md) — 同样是 LLM 面向材料性质，走直接预测而非工具使用。
- [AutoDFT / VASPBench](./vaspbench.md) — 同样是 LLM agent 驱动材料计算，在 DFT 工作流层面。
