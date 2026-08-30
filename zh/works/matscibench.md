# MatSciBench (2025)

> [English](../../works/matscibench.md) | **简体中文**

> **首次公开：** 2025-10-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2510.12171)

## Overview

MatSciBench 评测大语言模型在材料科学中的推理能力：1,340 个大学水平问题横跨该领域的核心子学科，其中 946 个配详细参考解、315 个带图像——DeepSeek-R1 在纯文本题上以 75.22% 领先，GPT-5 在图像题上以 53.02% 领先。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.12171>
- **Code:** <https://github.com/Jun-Kai-Zhang/MatSciBench>
- **Dataset:** <https://huggingface.co/datasets/JunkaiZ/MatSciBench>
- **Venue:** KDD 2026（据官方仓库；arXiv 元数据无发表信息）

## Summary

MatSciBench 把材料评估从知识回忆推进到多步推理：1,340 个大学水平问题横跨材料的核心子学科，其中 946 个配详细参考解、315 个以图像形式给出。评测覆盖领先的思考型与非思考型 LLM，按模态划分的结果颇具启示——DeepSeek-R1 在纯文本题上达 75.22%，而图像题最好的 GPT-5 只有 53.02%，把多模态材料推理标记为更难的前沿。

## Tasks

横跨材料子学科的 1,340 个大学水平问题（946 个配参考解、315 个带图像）；静态文本与多模态问答。

## Domains

材料科学——横跨该领域核心子学科的大学水平推理。

## Evaluation

- 纯文本题与图像题的准确率，参考解支持过程级错误分析。
- **报告。** DeepSeek-R1 纯文本 75.22%；GPT-5 图像题 53.02%。

## Typical Duration

单轮问题；无交互式设定。

## Main Contribution

一个以推理为中心、带参考解的材料 benchmark，其文本/图像划分量化了多模态材料推理落后于文本推理多少。

## Key Design Ideas

- 参考解使评估可到过程级，而不止于答案级。
- 文本/图像划分分离出多模态推理缺口。
- 广泛的子学科覆盖防止窄主题过拟合。

## Strengths

- 发表信息经核实（KDD 2026），代码与数据集全公开。
- 75% 对 53% 的模态差距是清晰、可引用的能力标尺。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；参评 LLM 的确切数量摘要未载明。KDD 2026 是仓库声明，arXiv 元数据未载明。

## Related Works

- [MaScQA](./mascqa.md) — 同样是材料知识问答，为考试规模、不带参考解判分。
- [MatVQA](./matvqa.md) — 同样是多模态材料推理，聚焦表征影像。
- [AtomWorld](./atomworld.md) — 同样是材料推理，考可验证的晶体结构操作。
