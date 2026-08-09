# LongDA (2026)

> [English](../../works/longda.md) | **简体中文**

## Overview

LongDA 是一个在 documentation-intensive（文档密集型）分析工作流下评估 LLM agent 的数据分析 benchmark：505 条分析查询，grounding 在覆盖 17 个公开美国全国性调查的专家撰写出版物上，配套文档平均长达 263k token。它同时发布了 LongTA——一个作为评估脚手架与 baseline 的工具增强 agent 框架。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.02598>
- **Code:** <https://github.com/Yiyang-Ian-Li/LongDA>
- **Data:** <https://huggingface.co/datasets/EvilBench/LongDA>

## Summary

与假定 schema 与输入均已良好指定的数据分析 benchmark 不同，LongDA 面向的是"导航冗长、异构文档才是首要瓶颈"的真实场景。Agent 必须先从多份非结构化文档——codebook、方法学描述、调查设计报告——中检索并整合关键信息（变量定义、调查权重、数据 schema），然后才能执行多步计算并编写可执行代码。配套的 LongTA 框架提供一个 ReAct 风格的 coding agent，带有文档阅读、关键词搜索、BM25 检索、笔记记录与沙箱化 Python 执行等工具。

## Tasks

505 条分析查询，提取自 6 个联邦机构（CDC、美国人口普查局、NSF、BLS、NCES、SAMHSA）发布的 17 个美国全国性调查所对应的 30 份官方分析出版物。每条查询由问题、答案结构与附加信息三部分组成；221 条（44%）要求单个数值，284 条（56%）要求带预定义语义元素的定长列表。出版物先经验证可从公开发布的调查数据复现，仅用于查询提取，并在评估期间对 agent 隐藏——agent 只能访问原始数据文件与调查文档。

## Domains

基于美国联邦调查数据的真实世界数据分析：公共卫生、劳动与就业、教育、科学人力。

## Evaluation

- 查询按**块（block）**呈现，每块对应一份来源出版物，使 agent 能在相关问题间复用中间理解；每块的步数预算为 100 步。
- **Coverage rate**——答案在语法上符合指定答案结构的查询比例。
- **Match rate**——容差 τ(a) = max(ε·|a|, 1)、ε = 5% 下的数值正确性，列表答案逐元素判定；模型相对排名在 1% 到 20% 的容差设置下保持稳定。
- **效率**——总 token 消耗、总运行时间与每块平均交互步数与有效性一并报告。
- 报告结果：GPT-5 (High) 达到 94.65% coverage / 68.91% match；GPT-5 为 91.09% / 69.16%；最佳开源模型 DeepSeek-V3.2 为 67.33% / 53.00%。列表类查询一致地难于标量类（跨模型平均 match rate 28.8% vs. 50.9%）。论文的结论是：成功主要取决于信息检索与工具使用策略而非纯推理能力，显式推理变体未显示明确增益。

## Typical Duration

每个出版物块内的多轮 ReAct 交互，预算 100 步；受评模型的每块平均步数从 5.5（GPT-5）到 81.17（GLM-4.7）不等。每个调查的文档平均 263k token，最长超过 735k。

## Main Contribution

第一个把 documentation-intensive 工作流作为评估对象的数据分析 benchmark，指出真实世界数据分析的主导瓶颈是长文档导航而非逻辑推断，并提供 LongTA 脚手架用于对工具增强数据分析 agent 的受控研究。

## Key Design Ideas

- 把文档导航作为被评估的能力：变量定义、样本权重与 schema 必须先从冗长的非结构化文档中发掘，然后才能写代码。
- 查询派生自经复现性验证的专家出版物，且出版物在评估时对 agent 隐藏。
- 结构化答案格式（单个数值或定长语义列表）让自动评估无歧义，同时考察指令遵循。
- 块级查询呈现贴合分析师工作流，并控制评估成本。
- 基于容差的 match rate 避免对小数值目标的轻微偏差过度惩罚。

## Strengths

- 单条查询的上下文远长于既有数据分析 benchmark：平均约 263,500 token，而论文比较的十个相关 benchmark 至多约 5,200。
- 诊断性实验（工具消融、工具使用轨迹）把性能归因于检索与工具使用策略而非推理，使该 benchmark 在排行榜之外还有解释性发现。
- 数据集、代码与 agent 框架公开发布。

## Limitations

论文自述的局限：

- 17 个美国全国性调查只代表真实世界数据分析的一小部分，可能对其他数据形态与工作流（企业私有数据、流式分析、以数据库为中心的 ETL）覆盖不足。
- 调查为固定年份快照；未测试对跨年 schema 漂移或文档版本演化的鲁棒性。
- 指标只评估最终数值，不衡量中间分析质量（代码规范、置信区间、边界情况处理）或解释质量。
- 调查设计的复杂性只被部分覆盖：不含显式考察方差估计（标准误、置信区间）的查询，因此在 LongDA 上的好成绩并不意味着具备点估计之外的复杂调查推断能力。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样是对照专家参考、基于执行打分的数据分析任务，但任务设定良好指定，而非以长文档导航为瓶颈。
- [AstaBench](./astabench.md) — 在宽泛的成本受控研究套件中把数据分析作为一个类别；LongDA 则是专门面向文档密集型场景的 benchmark。
