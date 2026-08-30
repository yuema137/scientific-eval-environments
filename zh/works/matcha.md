# MatCha (2025)

> [English](../../works/matcha.md) | **简体中文**

> **首次公开：** 2025-09-11 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2509.09307)

## Overview

MatCha 是材料表征的多模态 benchmark：1,500 个问题横跨材料研究的四个关键阶段、共 21 个不同任务，覆盖真实表征成像数据，揭示多模态 LLM 与人类专家之间的显著差距。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.09307>
- **Code:** <https://github.com/FreedomIntelligence/MatCha>
- **Dataset:** <https://huggingface.co/datasets/FreedomIntelligence/MatCha>
- **Venue:** EMNLP 2025 Findings（据官方仓库；arXiv 元数据无发表信息）

## Summary

论文题为「Can Multimodal LLMs See Materials Clearly?」。MatCha 追问 MLLM 能否承担材料表征中「感知与解读」的工作。其 1,500 个问题横跨材料研究的四个关键阶段、共 21 个不同任务，以真实表征成像数据为依据。模型与人类专家存在显著差距，在需要更高专业深度的问题上退化，且简单的少样本或链式思维提示都救不回来。

## Tasks

覆盖真实表征影像、横跨材料研究四个阶段共 21 个任务的 1,500 个问题；静态多模态问答。

## Domains

材料科学——贯穿研究工作流的材料表征，基于真实表征成像数据。

## Evaluation

- 21 个任务上的准确率，配人类专家基线对照。
- **报告。** 与人类专家差距显著；在更高专业度问题上退化；少样本与链式思维提示无法缓解这些局限。

## Typical Duration

单轮多模态问题；无交互式设定。

## Main Contribution

一个按阶段组织的表征 benchmark，勾画出 MLLM 材料感知在哪里失效——并表明这一失效是专业深度问题，靠提示技巧修不好。

## Key Design Ideas

- 四个研究阶段按「表征用在工作流何处」为任务排序。
- 人类专家基线把「难」变成可测量的差距。
- 显式测试少样本与 CoT，排除了廉价的修补手段。

## Strengths

- 真实表征影像，任务跨度广（21 个）。
- 「提示无济于事」的发现让缺陷诊断更清晰。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；EMNLP 2025 Findings 是仓库声明，arXiv 元数据未载明。摘要未逐一列出表征模态（如 SEM/TEM/XRD）。

## Related Works

- [MatVQA](./matvqa.md) — 同样是多模态材料表征推理，带抗捷径构造。
- [MatQnA](./matqna.md) — 同样是表征问答，明确按十种表征方法组织。
- [MaCBench](./macbench.md) — 同样是多模态的化学/材料评估。
