# Science Edge Evaluation (SEE) (2026)

> [English](../../works/science-edge-evaluation.md) | **简体中文**

## Overview

Science Edge Evaluation（SEE）是一个多模态 benchmark，题目由专家整理，锚定化学、生物与材料科学的同行评审文献与实验实践；旨在检验多模态大语言模型能否从真实实验室科学数据中做出有依据、受证据边界约束的推断。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.06931>
- **Code:** <https://github.com/SKYLENAGE-AI/science-edge-evaluation>
- **Venue:** arXiv preprint（2608.06931v1，2026-08-07 提交）

## Summary

SEE 在专家级科学问题上评估多模态大语言模型（MLLM），这些问题要求对实验数据进行推理，而非回忆既有概念。题目由同行评审论文、近期研究文献中的图表与数据，以及领域专家贡献的第一手实验数据构建。作者报告：即便表现最好的模型在标准设定下也仅达到 48.7% 准确率；通用模型平均优于科学专用模型；在视觉智能体设定中加入工具使用，只把最佳准确率小幅提升到 52.7%——他们据此认为瓶颈在于受证据边界约束的推理纪律，而非获取更多信息。

## Tasks

该 benchmark 由 1,116 道题目组成，覆盖 3 个学科（化学、生物、材料科学）与所报告的 17 个子领域。题目采用选择题与数值填空两种格式，由同行评审论文、近期研究文献中的图表与数据、以及来自专家的第一手实验数据构建，随后经过一条多阶段质量控制流水线（标准化、AI 辅助检查、专家科学准确性评审，以及图像消融检查以确认每题确实需要其视觉输入）。GitHub 公开发布说明其中 1,049 道题目已对外公开。

## Domains

化学、生物与材料科学。视觉输入包括生物活性测量、冷冻电镜结构、Western blot 与凝胶电泳图像、谱图（红外、NMR、质谱）、显微图像（SEM、TEM、AFM）、X 射线衍射图样，以及热分析曲线。

## Evaluation

答案对照专家标准真值评分：选择题答案必须与标准答案精确匹配，数值填空答案则按专家给定的容差评估。采用严格的二元 LLM-as-judge 协议，以 Gemini 3.1 Pro 为主评判者。在视觉智能体评估中，模型可在给出最终答案前迭代调用网页检索与代码解释器。

## Typical Duration

TODO(reference) —— 论文未报告单题的轨迹长度、墙钟时间或 token 预算。

## Main Contribution

一个多模态、专家整理的 benchmark，专门隔离出「受证据边界约束、对实验结果的科学推理」；结果表明当前 MLLM——包括工具增强的视觉智能体——无法可靠地从实验数据中得出有依据、受证据边界约束的推断，最佳模型仅达 48.7% 准确率（用工具时 52.7%）。

## Key Design Ideas

- 题目锚定真实的实验图表与数据（谱图、显微图像、印迹、衍射图样），而非教科书概念，针对对实验证据的推断。
- 整理阶段用图像消融检查，确认每题确实依赖其视觉输入。
- 多阶段质量控制，结合标准化、AI 辅助检查与专家科学评审。
- 一个赋予网页检索与代码解释器的视觉智能体设定，实现工具增强与无工具准确率的受控对比。
- 同时覆盖通用与科学专用 MLLM（共 19 个模型：15 个通用、4 个科学专用）。

## Strengths

- 题目锚定于三个实验学科的同行评审文献与第一手实验数据（据论文）。
- 图像消融检查防止出现无需视觉输入即可作答的题目（据论文）。
- 在同一 benchmark 上直接对比无工具与工具增强（网页检索 + 代码解释器）两种设定（据论文）。

## Limitations

- 论文未报告人类专家基线，故模型准确率未与专家表现校准。
- Repository note: 论文报告 1,116 道题，而 GitHub 公开发布说明公开了 1,049 道；完整 benchmark 大于公开子集。
- Repository note: 主 LLM 评判者（Gemini 3.1 Pro）本身也是被评估的通用模型之一，论文未就评判者偏差单独分析。

## Related Works

- [MaCBench](./macbench.md) —— 另一个面向 (M)LLM 的多模态化学与材料科学 benchmark。
- [SciVisAgentBench](./scivisagentbench.md) —— 另一个在科学视觉/实验数据上评估 agent 的 benchmark。
