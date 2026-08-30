# AstroMLab 1 (2024)

> [English](../../works/astromlab-1.md) | **简体中文**

> **首次公开：** 2024-07-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2407.11194)

## Overview

AstroMLab 1 提出了首个天文学专用的 LLM 评测数据集——从《Annual Review of Astronomy and Astrophysics》生成的 4,425 道选择题——并以此为 47 个闭源与开放权重模型的天文学知识打分，同时附上成本效率与置信度校准分析。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2407.11194>
- **Code:** <https://github.com/AstroMLab>
- **Venue:** Astronomy and Computing, vol. 51, 100893 (2025); DOI 10.1016/j.ascom.2024.100893

## Summary

论文的出发点是：通用 benchmark 说明不了模型对天文学掌握到什么程度。作者由此构建了一个领域 benchmark——取 1963–2023 年间发表的 885 篇《Annual Review of Astronomy and Astrophysics》综述文章，让 Gemini-1.5-Pro 为每篇写出五道四选一的选择题，共得 4,425 题。47 个模型（25 个闭源、22 个开放权重）按准确率打分并给出 Wilson 得分区间，结果再按六个天体物理子领域和五种受测能力交叉拆分。除排行榜外，研究还测量了成本效率（在 astro-ph 语料规模下每单位推理价格换得的准确率）与置信度校准，发现最强模型的置信度与正确性相关系数高于 0.9。该文自我定位为 AstroMLab 系列的第一篇，数据集的详细说明留给配套论文。

## Tasks

4,425 道天文学与天体物理学四选一选择题。构建方式：先用 Nougat OCR 从 885 篇《Annual Review of Astronomy and Astrophysics》文章（1963–2023）中抽取文本，再让 Gemini-1.5-Pro 针对每篇内容出五道可依据该文内容作答的题目；提示中明确要求题目具体、具有普遍性（避免只涉及单篇论文的琐碎细节）、各选项长度均衡，生成器还须给出解释和支撑引用。人类专家审阅了生成题目的一个子集，认为质量达标。题目另按六个天体物理子领域和五种受测能力分类。评测设定为单轮闭卷问答，检索增强生成被有意排除在评测范围之外。

## Domains

天文学与天体物理学——题目全部源自天文学综述文献，覆盖恒星天体物理、系外行星、银河系与河外星系天文学、宇宙学、高能天体物理与仪器。受评的目标是天文学知识与推理，而非套着天文学词汇的通用知识探测。

## Evaluation

在 4,425 道题上的准确率，Wilson 得分区间约为 ±0.6–0.8 个百分点。模型拒答的题目按模型逐个剔除（对最强模型而言至多影响 0.2% 的题目）。准确率排名之外还有两项辅助分析：成本效率分析，给出每 0.1M token 与每 3B token（astro-ph 归档的规模）的价格；校准分析，将模型自报的置信度与正确性做相关。

- **报告。** 闭源模型中 Claude-3.5-Sonnet 以 85.0% 领先，Claude-3.0-Opus 82.7%，GPT-4o 80.4%。开放权重模型中 LLaMA-3-70B 以 80.6% 领先，Qwen-2-72B 与 Mixtral-8x22B 并列 77.7%。
- **报告（成本）。** 分数每提高 3.5 分，推理成本大约要涨十倍。
- **报告（校准）。** 头部模型的置信度与正确性相关系数高于 0.9。

## Typical Duration

单轮选择题作答；无交互环境、工具使用或多步轨迹。

## Main Contribution

首个天文学专用的 LLM benchmark，也是首次大范围跨模型测量天文学知识，为 AstroMLab 模型线及后续天文 LLM 工作确立了报告结果时的参照标尺。

## Key Design Ideas

- 题目取自一套经过策划的综述系列（《Annual Review of Astronomy and Astrophysics》）而非任意论文，使题目反映的是已成共识的领域知识。
- 由强模型在明确的提示约束（具体性、普遍性、选项长度均衡）下出题，让 4,425 题规模的自动化构建变得可行。
- 要求生成器为每道题输出解释与支撑引用，便于人类评审高效抽查质量。
- 以 astro-ph 语料规模报告单位准确率的成本，使 benchmark 不只用于排名，也能支撑部署决策。
- 在准确率之外纳入置信度校准，把自我评估的可靠性当作一项独立的受评属性。
- 同时大规模覆盖闭源与开放权重模型（共 47 个），使闭源/开源差距可被度量。

## Strengths

- 领域题库规模大，单次评测的模型覆盖面也罕见地广。
- 经同行评议并发表于领域期刊《Astronomy and Computing》。
- 成本效率与校准分析让 benchmark 的诊断价值超出单一准确率数字。
- 子领域与能力维度的拆分支持比总分更细粒度的比较。

## Limitations

- 题目由 LLM 生成、仅有一个子集经人工核验；作者承认这是「一种折中」，部分题目可能表述含糊，且出自较早综述的题目可能编码了过时的天文学认识——因此所报告的准确率「肯定是一个下限」。
- 静态闭卷选择题：不评测 agent、工具使用、任务环境或自由作答式推理，RAG 也被明确排除。
- 论文并未随文发布数据集，其详细说明与发布被推迟到即将发表的配套论文。
- Repository note: 对综述文献的选择题式回忆测的是知识，而不是执行天文研究任务的能力；本卡片依照仓库收录考试类与问答类 benchmark 的先例予以纳入。

## Related Works

- [LLM-IOAA](./llm-ioaa.md) — 同样是天文学知识评估，但采用自由作答的奥赛题、按官方评分细则判分，而非选择题。
- [Stargazer](./stargazer.md) — 处在天文评估光谱另一端：交互式的模型拟合任务环境，而非静态问答。
- [From Queries to Criteria](./from-queries-to-criteria-understanding-how-astrono.md) — 直接论证了选择题式天文 benchmark 只捕捉到天文学家评价工作时很窄的一部分。
- [MaScQA](./mascqa.md) — 材料科学中同类的领域知识问答 benchmark。
- [EEE-Bench](./eee-bench.md) — 电气工程中同类的大规模领域问答 benchmark，模型覆盖同样很广。
