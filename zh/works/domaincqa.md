# DomainCQA / AstroChart (2025)

> [English](../../works/domaincqa.md) | **简体中文**

> **首次公开：** 2025-03-25 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2503.19498)

## Overview

DomainCQA 是一套在科学领域内构建知识密集型图表问答 benchmark 的方法论，其实例化产物是 **AstroChart**——取自天文学论文的 482 张图表、1,690 组问答对——并用它评测了 21 个多模态大语言模型，同时给出人类基线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2503.19498>
- **Code:** <https://github.com/LingZhong01/DomainCQA>
- **Data:** <https://huggingface.co/datasets/yangjing0128/AstroChart>
- **Venue:** arXiv preprint，2025 年 3 月首次提交（v6，2026 年 1 月）

## Summary

作者认为，现有的图表 benchmark 大多只考表层解析——读标签、读刻度、读图例——因而说明不了模型能否像领域读者那样对一张科学图作推理。DomainCQA 给出的回答是一套三阶段构建配方（图表选取、问答对生成、专家校验），并有意区分两类问题：*Fundamental QA*（FQA）考察对图表本身的理解，*Advanced QA*（AQA）则要求整合图上并不存在的领域知识。AstroChart 把这套配方用在天文学上，图表取自 arXiv 天文论文，每一条目都经领域专家校验。21 个 MLLM 在零样本设定下受测，四位天文学研究者作答 10% 的抽样题目，给出人类参照点。

## Tasks

1,690 组问答对，覆盖从 arXiv 天文论文中抽取的 482 张不同图表，分为 1,509 组 FQA 与 181 组 AQA。

- **FQA — 视觉（Visual，602）：** 颜色（Color，211）、样式（Style，133）、文字（Text，213）、版式（Layout，45）。
- **FQA — 数据（Data，316）：** 取值（Point，130）、区间（Interval，102）、计算（Calculation，84）。
- **FQA — 推理（Inference，289）。**
- **FQA — 图表描述（Chart Description，302）。**
- **AQA — 知识依赖推理（Knowledge-Based Inference，181）。**

构建方式：以图表复杂度向量配合非参数 Gibbs 采样来选图，使样本对领域具有代表性；AQA 的图表另走一条选取路径，由一个带链式思维的「图表摘要选择器」通过跨模型多数投票识别出每篇论文的主要发现。生成的问答对随后交由领域专家独立评审，逐条标注 Valid 或 Flawed，直至达成一致。天文学之外，论文还给出生物化学、经济学、医学与社会科学的部分 AQA 试点研究；完整构建的数据集只有天文学一个。

## Domains

天文学。AstroChart 的每一条目都是天文论文中的一张图——曲线图、光谱、分布图以及导出量图——而 AQA 部分要求图面之外的天体物理知识，因此受评目标是天文图件的解读，而非通用的图表解析。试点领域（生物化学、经济学、医学、社会科学）只是用来论证构建配方可迁移的部分 AQA 研究，并未作为完整数据集发布。

## Evaluation

- **数值型答案**按相对误差打分，误差以坐标轴量程归一化；推导型答案用精确匹配。
- **开放式答案**由 LLM 评判者（DeepSeek-V3）从相关性、正确性与完整性三方面打 0–1 分。在 176 条样本上，评判者与人工标注的一致性为 Pearson r = 0.816、Spearman ρ = 0.817、MAE = 0.096。
- **辅助指标：** ROUGE-L、BLEU-4 与 L3Score。
- **协议：** 对 21 个 MLLM（闭源与开放权重）作零样本评测；四位天文学研究者作答其中 10% 的题目作为人类基线。
- **报告（选取的若干行，格式为 `Visual-All / Data-All / Inference / Chart-Desc / KB-Inference / Overall`）：**
  - Gemini-2.5-Pro — 88.22 / 72.66 / 81.31 / 81.09 / 73.65 / **81.30**
  - Pixtral-Large-124B — 86.11 / 59.38 / 78.65 / 80.93 / 70.83 / 77.23
  - GPT-4o — 86.23 / 53.19 / 75.40 / 80.96 / 73.04 / 75.84
  - 人类基线（10% 抽样） — 98.60 / 96.40 / 91.82 / 70.00 / 39.00 / 85.56

## Typical Duration

N/A — 单轮问答；论文未报告单题的墙钟时间、token 或成本预算。

## Main Contribution

一套可推广的配方，把领域论文变成知识密集型的图表问答 benchmark，并把「读懂图」与「依赖知识的推理」分开；配套的 AstroChart 是它在天文学上的实例化，附带的分析把模型失败归因于三点：图表推理（推断趋势）、数值计算（可靠地读出数值）与领域事实的整合。

## Key Design Ideas

- 题目从设计上分成两族：FQA 测模型是否读得懂图，AQA 测它能否把图与自身已有的领域知识结合起来。
- 图表选取按领域代表性采样，而不是拿到什么用什么；AQA 另有一条以源论文主要发现为锚的选取路径。
- 细粒度的 FQA 分类（Visual → Color/Style/Text/Layout；Data → Point/Interval/Calculation；Inference；Chart Description）使失败可以定位，而不是坍缩成一个准确率数字。
- 混合评分：数值用坐标轴量程归一化的相对误差，推导用精确匹配，开放式文本用 LLM 评判者，且评判者本身也对照人工分数做了验证。
- 人类基线由领域研究者在固定的 10% 抽样上作答，而非众包工人。

## Strengths

- AQA 这一划分单独隔离出依赖知识的推理，而这正是通用图表 benchmark 测不到的科学读图能力。
- 每一条目都经独立专家评审，并有明确的 Valid/Flawed 裁定直至一致。
- 不预设 LLM 评判者可靠：它与人工标注的一致性经过测量并公布。
- 模型覆盖面广（21 个 MLLM，闭源与开放权重），且给出分项拆解而非单一总分。
- 图表、问答对与代码均已公开发布。

## Limitations

- AQA 只有 181 条，相比 FQA 的 1,509 条规模偏小，因此依赖知识的那部分结论只建立在数据集中较小的一半上。
- 人类基线只由四位研究者在 10% 抽样上给出，各分项也参差不齐——Visual 与 Data 很高，但 Chart Description 只有 70.00、Knowledge-Based Inference 只有 39.00，低于若干模型。这使 85.56 的总分不足以作为可靠的上限，也提示开放式答案的评判者会奖励模型式的冗长表达。
- Repository note: 这是单轮多模态问答，不是 agent 评估——没有工具使用、没有档案访问、没有多步轨迹。收录依据是仓库对考试衍生问答的先例：题集有名称、有规模、有明确的评分协议，且比较了多个模型。
- Repository note: 天文学之外的试点只是部分 AQA 研究，因此论文关于配方可跨领域推广的主张，靠的是构建质量方面的证据，而非完整的 benchmark。

## Related Works

- [AstroMMBench](./astrommbench.md) — 最接近的邻居：同样从天文论文的图件出发、经专家评审构建多模态天文题目，但采用选择题形式，而非数值与开放式混合评分，也没有知识推理这一划分。
- [AstroMLab 1](./astromlab-1.md) — 同样是跨多模型打分的天文知识 benchmark，但只有文本，且是从综述文章衍生的选择题。
- [AstroAlertBench](./astroalertbench.md) — 同样是单轮多模态天文评测，对象是巡天警报图像切片而非论文图件。
- [MaScQA](./mascqa.md) — 收录「有规模、有明确协议、跨多模型评测的领域题集」这一做法的先例。
