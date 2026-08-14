# From Queries to Criteria: Understanding How Astronomers Evaluate LLMs (2025)

> [English](../../works/from-queries-to-criteria-understanding-how-astrono.md) | **简体中文**

## Overview

一项实证研究，考察领域专家在真实工作现场究竟如何评判一个 LLM 系统：作者把一个天文文献 RAG 机器人四周部署期内的 368 条真实提问与 11 次访谈作归纳编码，提炼出一套提问类型学与五条评价准则，再据此构建并公开了一个 40 道题、由专家撰写答案的天文 benchmark，其自动打分协议已对照用户评分完成校验。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2507.15715>
- **Code:** <https://huggingface.co/datasets/jhu-clsp/astro-llms-benchmark-dataset>
- **Venue:** Conference on Language Modeling (COLM) 2025

## Summary

作者把 `@Ask-astro-ph` 部署给 Space Telescope Science Institute 的天文学家使用。这是一个 Slack 上的检索增强生成机器人，语料为约 30 万篇天体物理 arXiv 论文（截至 2023 年 7 月），先用 bge-small-en-v1.5 检索出最相关的五篇，再交由 GPT-4o 生成回答。四周之内（2024 年 5 月 29 日至 6 月 24 日），43 位招募到的参与者中有 35 位共提出 368 条提问，事后另有 11 人接受访谈。对提问作归纳编码，得到九类提问的类型学；访谈则归纳出天文学家评判回答时所用的五条准则——现有的天文选择题 benchmark 基本捕捉不到这些准则。这些发现被转化为具体的 benchmark 构建建议，并落实为一个 40 题、附专家撰写标准答案的 benchmark；它的自动相关性得分与真实用户的点赞/点踩评分的 Pearson 相关系数达到 0.82。

## Tasks

benchmark 由 40 组问答对构成，取自部署期真实提问日志的抽样，分布大致是：具体事实类知识查询约 55%、深度知识（综合与高阶推理）22%、宽泛描述 17%。七位天文学家各自挑出与自己专长匹配的问题，撰写引用 2–5 篇 arXiv 论文的自由文本标准答案，每题约花 30 分钟；另有一位天文学家负责质量复核。作为底层研究语料的，是 368 条提问的完整去标识日志，编码为九类：具体事实类知识查询（33%）、深度知识类（21%）、主题类文献计量检索（14%）、宽泛描述类知识查询（13%）、压力测试（7%）、询问机器人能力（5%）、流程类知识查询（2%）、指定论文或作者的文献计量检索（2%），以及未明确主题（2%）。该编码的 Krippendorff's alpha 为 0.51。

## Domains

天文——受评的部署系统、参与者群体（Space Telescope Science Institute 的天文学博士）、检索语料（天体物理 arXiv），以及每一道 benchmark 题目与标准答案，全都是天文的。作者预期这套评估思路可以推广到其他观测型、半可验证的科学，但实际评估的材料自始至终是天文。

## Evaluation

分两层。第一层是这项研究自身的工具：对提问与访谈作归纳式定性编码，得出提问类型学与五条评价准则——总体正确性（术语准确、引文相关且够新、对检索到的来源如实概括）、不确定性表达与限定（该保留时保留、拒答要说明理由；用户批评回答过于自信）、回答的具体性与清晰度、对提问的正确理解（上下文、领域术语的消歧、意图），以及更广泛的影响（节省时间、发现价值、对科研实践与公平性的影响）。第二层是公开的 benchmark：机器人的回答对照专家标准答案，由 LLM 给出 0–1 区间的相关性得分，并辅以与人类回答的贴近度度量（嵌入与 BERTScore）、面向不确定性表达这条准则的认知标记检测，以及用自然语言推理做的引文准确性蕴含检验。

- **报告：** benchmark 的相关性得分与真实用户点赞/点踩评分的 Pearson 相关系数为 0.8239，作者以此佐证自动打分协议确实追踪着从业者的判断。
- 作者明确指出，更广泛影响这一条准则无法由任何静态数据集捕捉，只能借助用户研究。

## Typical Duration

为期四周的线上部署；与机器人的交互是单轮的提问—回答。撰写标准答案每题约耗费专家 30 分钟。原始来源未给出逐条提问的 token 或延迟预算。

## Main Contribution

以实证方式刻画出领域专家在真实科研工作中评估 LLM 系统所依据的准则，并把这些准则转化为 benchmark 设计建议与一个已公开、经校验的天文 benchmark；作者据此指出，当下主流的天文选择题 benchmark 只覆盖了正确性中很窄的一段。

## Key Design Ideas

- 评价准则来自线上部署中观察到的从业者行为，而不是 benchmark 设计者的直觉。
- 提问日志与事后访谈配对，用户问了什么、又为何认为某个回答好，两边都留有记录。
- 用一张表把提问类型、评价准则与候选指标串起来，benchmark 构建的论证因此具体且可核查。
- 标准答案由在职天文学家在自己的专长范围内撰写，并强制引用 arXiv 文献，而不是交给 LLM 生成。
- 自动打分协议要对照部署期的真实用户评分做校验，而不是自说自话。
- 指标与准则一一对应：引文准确性用蕴含模型，不确定性表达用认知标记检测，贴近度用嵌入相似度——而不是压成一个总分。
- 去标识的完整提问日志与 benchmark 一并公开。

## Strengths

- 立足于 35 位天文学博士的真实科研使用，而非合成任务或众包任务。
- 产出的不只是结论，还有实物：一个公开的 benchmark 加一份公开的提问语料。
- 打分协议带有对照用户评分的显式外部校验。
- 点出了一个评价维度（更广泛的影响），并坦承静态 benchmark 够不到它。
- 经 COLM 2025 同行评审。

## Limitations

- 只覆盖美国一家研究所，参与者全为博士，且系自愿报名；样本可能漏掉不感兴趣的用户、学生与天文爱好者。
- benchmark 只有 40 道题，且都来自单次部署的提问分布。
- 结论针对的是一个特定机器人（语料冻结于 2023 年 7 月的 GPT-4o RAG 系统）；换成别的工具，评价策略未必相同。
- 四周的窗口未必足以捕捉用户预期的长期变化。
- 提问类型学的标注者间一致性只算中等（Krippendorff's alpha 0.51），作者归因于标注者背景多样。
- Repository note: 受评系统是单轮 RAG 助手，而非会用工具的 agent；其贡献是评估方法学加一个小规模 benchmark，而不是一个 agent 任务环境。

## Related Works

- [AstroMLab 1](./astromlab-1.md) — 本文所批评其覆盖过窄的那个天文选择题 benchmark。
- [Stargazer](./stargazer.md) — 同为天文评测，但带可执行的任务环境，而非文献问答。
- [ScholarQuest](./scholarquest.md) — 同样评测文献检索与证据综合，规模更大，但落在计算机科学。
- [AI's Capability in Assisting Scientific Research I: Literature Review](./ai-assisting-research-i-literature-review.md) — 互补的一项天文/天体物理评测，把 AI 文献检索与人类专家正面对比。
