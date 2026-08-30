# CosmoPaperQA (2025)

> [English](../../works/cosmopaperqa.md) | **简体中文**

> **首次公开：** 2025-07-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2507.07155)

## Overview

CosmoPaperQA 是一份含 105 组问答对的宇宙学问答数据集，题目取自五篇高引宇宙学论文。它用来评测九种检索增强生成（RAG）agent 配置，以专家人工评分为对照，并据此校准一个 LLM-as-a-Judge 评分器，让它充当人工评估的替代。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.07155>
- **Dataset:** <https://huggingface.co/datasets/ASTROANTS/CosmoPaperQA>
- **Code:** <https://github.com/CMBAgents/scirag>
- **Venue:** ICML 2025 Workshop on Machine Learning for Astrophysics（录用为 spotlight 报告）

## Summary

这项工作的出发点是一个观察：现有的天文问答资源大多是合成的——文中以 AstroMLab 1 的 4,425 道 AI 生成选择题和 Astro-QA 的 3,082 道题作为对照——因此它改从真实研究论文中直接提取问题。一支宇宙学专家团队撰写了 105 组问答对，分三个复杂度层级：具体参数的事实检索、需要整合多处证据的综合推理，以及需要深厚领域造诣的分析性阐释。九种 RAG 配置在同一份五篇论文的语料上运行，共产生 945 份回答，全部由一位博士级领域专家逐条人工评分。这 945 个人工评分随后用于校准两个 LLM judge；两者复现系统排名的吻合程度足够高（各评估方法之间 Pearson r > 0.99），作者据此提出把 LLM-as-a-Judge 作为专家评分的可规模化替代。

## Tasks

105 组由专家撰写的问答对，取自五篇高引宇宙学论文：Planck 2018 宇宙学参数结果、CAMELS 机器学习模拟套件、一项局域哈勃常数测量、一项「cosmology with one galaxy」分析，以及 Atacama Cosmology Telescope DR6 的约束结果。题目按三个复杂度层级组织——具体参数的事实检索、整合多处证据的综合推理，以及需要深厚领域造诣的分析性阐释。受评的九种 RAG 配置为：三个商用助手（OpenAI Assistant，用 GPT-4.1 与 text-embedding-3-large；OpenAIPDF Assistant，同一套技术栈但直接读原始 PDF；VertexAI Assistant，用 Gemini 2.5 Flash 与 text-embedding-005），两种混合的嵌入 / 生成搭配（HybridOAIGem、HybridGemGem），两个学术检索工具（PaperQA2 与经领域适配的 Modified PaperQA2），以及两个非 RAG 基线（不做检索的 Gemini Assistant 和带网页搜索的 Perplexity Assistant）。检索统一采用 top-k = 20，分块为 5,000 token、重叠 250 token，温度 0.01。

## Domains

天文学。所有问题都取自宇宙学文献——CMB 功率谱与参数结果、哈勃常数测量、宇宙学模拟，以及星系尺度的宇宙学推断——因此评测目标是天体物理领域理解，而非通用阅读理解。物理学则通过题目所考察的宇宙学参数物理，成为次级共同领域。

## Evaluation

二值评分：回答若事实准确、且抓住了标准答案的核心科学要点，记 1 分；若含有错误或遗漏核心概念，记 0 分；报告时换算到 0–100。全部 945 份回答（9 个系统 × 105 题）由一位具备博士级宇宙学造诣的领域专家逐条人工评分。随后用这些人工评分校准两个 LLM judge——OpenAI o3-mini 与 Gemini 2.5 Pro——并让它们评判同一批回答。报告的准确率为：OpenAI Assistant 91.4%、OpenAIPDF Assistant 89.5%、VertexAI Assistant 86.7%、HybridOAIGem 85.7%、HybridGemGem 84.8%、PaperQA2 81.9%、Modified PaperQA2 73.3%、Perplexity Assistant 17.1%、Gemini Assistant（无检索）16.2%。两个 judge 的偏差方向相反——OpenAI judge 比人类专家低 2–8 个百分点，Gemini judge 高 5–15 个百分点——但都保持了排名不变，而排名正是 LLM-as-a-Judge 替代方案的立论依据。

## Typical Duration

N/A — 在固定的五篇论文语料上做单轮问答，没有多步轨迹，也未报告 wall-clock 或 token 预算。论文只提到 OpenAI Assistant 有 4,096 token 的文档处理限制；附录 E 报告的是每次查询的成本而非延迟：VertexAI 每次查询 $0.000357，基于 OpenAI 的系统则为 $0.048798（相差 136.7 倍），完整跑一遍 105 道题分别是 $0.037 与 $5.12。

## Main Contribution

一份问题从真实研究论文中提取、而非模型合成的宇宙学问答数据集；在统一检索设置下对九种 RAG 配置所做的系统性横向比较；以及以 945 份人工评分为真值校准出的 LLM-as-a-Judge 评分器——作者将其作为专家人工评估的稳健替代。

## Key Design Ideas

- 题目由宇宙学专家依据真实论文撰写，而不是由模型生成，以避开作者归因于 AstroMLab 1 与 Astro-QA 的合成题偏差。
- 三个刻意划分的复杂度层级，把参数查找、多源综合与阐释性推理区分开。
- 九种配置共享同一语料、同一分块方式（5,000 token，重叠 250 token）、同一检索深度（top-k = 20）与同一温度（0.01），因此比较隔离出的是嵌入与生成模型的选择。
- 两个非 RAG 基线——裸的 Gemini 助手和带网页搜索的 Perplexity 助手——为「准确率中有多少来自对这几篇特定论文的检索」划定了边界。
- judge 校准是实证的：两个 LLM judge 对照的是全部 945 个人工评分，而非抽样，且其绝对偏差与排名保真度都被报告出来。
- 混合配置刻意跨厂商组合（OpenAI 嵌入配 Gemini 生成，反之亦然），把嵌入模型的贡献与生成模型的贡献分离开。

## Strengths

- 评分真值是人类专家把每一份回答都完整过了一遍，而不是抽样或自动代理指标。
- judge 校准结果连同其失效模式一并报告，而不是只给一个一致性数字：两个 judge 在绝对分值上都有系统性偏差，作者只主张排名可以迁移。
- 无检索基线与网页搜索基线只有 16–17%，使得可归因于语料检索的差距异常清晰。
- 数据集与流水线均已公开（HuggingFace 与 SciRag 仓库），比较结果可复现。
- 成本与准确率并列报告，暴露出准确率相差不到五个百分点的配置之间，单次查询成本却相差 136.7 倍。

## Limitations

- 作者指出，许多题目明确点到了其来源论文，这可能因为提供了检索线索而系统性地抬高 RAG 表现。
- 五篇论文的语料远小于真实研究场景——那里系统需要在成千上万篇论文中检索；作者预期准确率会随规模上升而下降。
- 人工评估限制了可扩展性，这既是做 judge 校准的动机，也意味着真值无法低成本地扩充。
- Repository note: 945 个评分全部出自同一位专家，因此这套二值评分细则的标注者间一致性无从衡量。
- Repository note: 受评系统是回答单个问题的检索助手，而非执行多步轨迹的 agent，因此结果反映的是检索与作答质量，而非规划、工具使用或错误恢复能力。
- Repository note: 报告的准确率都是单次运行的结果，尽管温度设得接近确定性但并不为零，论文并未给出重复运行的方差。

## Related Works

- [LAB-Bench](./lab-bench.md) — 其 LitQA2 子任务是最接近的对应物，同样是面向科学 agent 的文献依据型问答，只是落在生物学而非宇宙学。
- [ScholarQuest](./scholarquest.md) — 同样评测面向文献的 agent，但打分对象是开放文献检索，而非固定语料上的作答准确率。
- [ReplicationBench](./replicationbench.md) — 同属天体物理领域，评测的是 agent 复现论文结果，而非回答关于论文的问题。
- [Stargazer](./stargazer.md) — 天文 agent 评测，考察定量模型拟合，与本工作的知识检索侧重互为补充。
