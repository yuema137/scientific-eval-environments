# DeepResearch Bench (2025)

> [English](../../works/deepresearch-bench.md) | **简体中文**

## Overview

DeepResearch Bench 是面向 Deep Research Agent（DRA）的 benchmark，由 22 个主题领域下的 100 个博士级研究任务构成，并配套两个评估框架：评价报告生成质量的 RACE，以及评价引用可靠性与检索有效性的 FACT。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2506.11763>
- **Code:** <https://github.com/Ayanami0730/deep_research_bench>

## Summary

论文指出，此前缺少针对端到端 deep research agent 的综合 benchmark：这类 agent 的内部推理与检索过程不透明，最终报告因而成为评估其能力的主要接口，而长篇报告又几乎不可能确立标准答案。该 benchmark 的主题配比来自真实需求——从 web search 增强的 LLM chatbot 交互中收集 96,147 条匿名化用户 query，过滤出 44,019 条符合 deep research 定义的 query，按 WebOrganizer taxonomy 归入 22 个主题领域，再把该分布按比例压缩为 100 个由专家撰写的任务。在任务集之上，论文提出 RACE（带动态加权的 reference-based 自适应准则评估框架）与 FACT（自动化引用核验流程），并且两者都经过人类研究验证，而非默认可靠。

## Tasks

100 个任务，中文与英文各 50 个。各领域任务数由实测的真实分布确定：96,147 条原始匿名 query 先由 DeepSeek-V3-0324 过滤为 44,019 条符合论文 deep research 定义的 query（即需要多轮 web 搜索、信息收集、分析并产出高质量报告的问题），再归入 WebOrganizer taxonomy 中选定的 22 个主题领域；该分布按比例压缩为 100 个任务，且保持相同的主题平衡。任务由博士或具备 5 年以上相关领域经验的资深从业者提出，再由团队按质量、清晰度、复杂度以及是否符合 deep research 定义进行人工筛选。

## Domains

WebOrganizer taxonomy 下的 22 个主题领域，覆盖一般性研究需求——论文列举的例子涵盖科学与技术、金融与商业、软件、艺术与设计、娱乐、历史、交通等。覆盖面由观察到的用户需求驱动，而非按科学学科体系划分。

## Evaluation

- **RACE（带动态加权的 reference-based 自适应准则评估框架）** 在四个正交的顶层维度上评价报告质量——Comprehensiveness、Insight/Depth、Instruction-Following、Readability。
  - **动态权重与自适应准则。** 对每个任务，Judge LLM 在 `T` 次试验上取平均得到维度权重 `W_d`，再为每个维度生成量身定制的准则及其权重（权重之和为 1）。
  - **基于参考报告的打分。** 孤立地给报告打分区分度不足——模型倾向于一致给出高分——因此由 Judge LLM 让目标报告与一份高质量参考报告在每条准则上同时受评，最终分数是相对值：`S_final(R_tgt) = S_int(R_tgt) / (S_int(R_tgt) + S_int(R_ref))`。这也是绝对分值都聚集在 50 附近的原因；论文明确要求关注排名与分数间的比例差异，而非绝对数值。
  - 参考报告取自 2025 年 4 月收集的 Gemini-2.5-pro 版 Deep Research 输出；Judge LLM 为 **Gemini-2.5-pro**。
- **FACT（Factual Abundance and Citation Trustworthiness）** 是一条自动化流程：从报告中抽取 statement–URL 对，对同一 URL 下陈述同一事实的重复对做去重，通过 Jina Reader API 抓取网页正文，再由 Judge LLM 给出 support / not-support 的二元判定。它报告 **Citation Accuracy（C. Acc.）** 与 **Average Effective Citations per Task（E. Cit.）** 两个指标。此处使用 Gemini-2.5-flash 作为判定模型，因其在 token 消耗巨大的引用核验任务上更经济。
- **人类验证。** 70 余名具备硕士学位与相关领域专长的标注者，对 50 个任务、4 个 agent 共 600 份报告进行标注，每个任务 3 名专家，每名标注者最多参与 3 个 query。一致性由 Pairwise Agreement Rate（PAR）、Overall Pearson Correlation（OPC）以及在 ICC ≥ 0 过滤后剩余的 37 个任务上计算的 Filtered Average Pearson / Spearman（FAP / FAS）衡量。RACE（Full）达到 PAR 71.33、OPC 99.54、FAP 60.24、FAS 59.12（总分 72.56），而 vanilla prompt 基线为 58.89 / 98.89 / 40.30 / 43.75；其 PAR 还高于专家之间 68.44 的相互一致率。消融显示参考报告是单项贡献最大的组件：去掉后 PAR 降至 66.56、FAS 降至 51.23。
- **报告结果（Table 1）。** 在 Deep Research Agent 中，Gemini-2.5-Pro Deep Research 的 RACE 总分领先，为 48.88；其次是 OpenAI Deep Research 46.98（其 Instruction-Following 反超 Gemini，49.27 对 49.18）、Perplexity Deep Research 42.25、Grok Deeper Search 40.24。而在 FACT 上排序明显不同：Perplexity Deep Research 在 DRA 中引用准确率最高，为 90.24；Gemini-2.5-Pro Deep Research 为 81.44，但每任务有效引用数遥遥领先，达 111.21，而 OpenAI Deep Research 为 40.79。在带搜索的 LLM 中，Claude-3.7-Sonnet w/Search 的 RACE 最高（40.67），Claude-3.5-Sonnet w/Search 则取得全表最高的引用准确率 94.04，但有效引用数仅 9.78。
- **Judge 模型对比（Table 3）。** Gemini 2.5 Pro Preview 总分最佳（72.56），每 query 成本 $0.13；o4-mini 最便宜，为 $0.04（71.63）；o3 为 $0.37（68.58）；Claude 3.7 Sonnet 为 $0.47（72.28）。

## Typical Duration

未设置单任务的步数或 wall-clock 预算——被测系统是商业 deep research 产品与带搜索的 LLM，均运行至完成，其中带搜索工具的 LLM 统一把 `search_context_size` 设为 high。产出规模可由人类研究反映：单份报告可长达数十页，专家完整审阅一份通常需要 30–60 分钟。

## Main Contribution

第一个专门面向 Deep Research Agent 的端到端评估 benchmark，其任务分布由实测的真实用户需求导出，并配套 RACE 与 FACT 两个评估框架——论文对二者的人类一致性做了验证，而非直接假定其可靠。

## Key Design Ideas

- 任务分布由 96,147 条真实匿名用户 query 导出，而非自上而下拟定，因此主题配比反映的是观察到的真实需求。
- 报告质量*相对参考报告*打分，因为对长篇报告做绝对式 LLM-as-a-Judge 打分区分度不足。
- 评判准则与维度权重按任务生成而非固定，因此无需用单一 rubric 去套 22 个领域。
- 检索能力通过对照实时网页核验引用来评估，并把 grounding 拆成精确性（Citation Accuracy）与丰富度（Effective Citations）两个指标，而不是压成一个分数。
- 评估框架本身也被放上考台——与人类专家对比、与消融变体对比、并在若干候选 Judge LLM 之间对比且报告成本。
- 作者指出 RACE 与 FACT 并不限于 deep research 场景：RACE 可作为通用的文本生成评估框架，FACT 可用于评估检索信息的覆盖度与可靠性。

## Strengths

- 用大规模真实 query 语料确定主题分布，使任务配比有实证依据，而非出于作者主观。
- 就该场景而言人类研究规模可观（600 份报告、70 余名合格标注者），且在多个互补指标上报告一致性，其中还包含一个控制了低评分者一致性的过滤子集。
- RACE 与专家的成对一致率高于专家彼此之间的一致率。
- FACT 把引用精确性与引用丰富度分开；实测结果显示这两种排序确实与 RACE 排名分道扬镳。
- 报告 Judge LLM 成本与质量并列，使评估自身的运行开销可见。

## Limitations

- 作者指出 benchmark 规模受专家撰写流程限制——100 个任务限制了统计稳健性与主题覆盖度，在保持质量的前提下扩展被列为优先事项。
- 作者指出团队内部策划可能引入领域覆盖偏差，并计划引入具备专门领域知识的外部评审。
- 作者指出人类评估吞吐量是主要瓶颈：50 个任务、每任务 3 名专家的规模被描述为有限，且易受个体差异影响。
- 作者指出所评估商业 agent 的迭代周期并不透明，因此结果被绑定到明确说明的数据采集时间窗口。
- Repository note: 两个框架都是 LLM judge 流程——RACE 经由 Gemini-2.5-pro 打分，FACT 的 support 判定经由 Gemini-2.5-flash——因此测得的质量继承了这些 judge 的可靠性；此外 reference-based 设计还把分数与 2025 年 4 月收集的那批特定参考报告绑定在一起。
- Repository note: 评估对象是最终报告及其引用，而非 agent 的动作序列；论文说明这是有意为之，因为商业 DRA 的内部检索与推理过程不可观测。

## Related Works

- [TRACE](./trace.md) — 同样评估 deep research agent，但用 hierarchical utility function 对 trajectory 打分，而非评价最终报告。Repository note: TRACE 的配套任务集另行命名为 "DeepResearch-Bench"；尽管名称相同，二者是不同的工作。
- [AutoResearchBench](./autoresearchbench.md) — 同样面向 web 上的 agentic 研究，但范围限于答案集大小未知的文献发现，而非报告生成。
- [TELBench](./telbench.md) — 对 deep research agent 的互补视角：在 trajectory 内部做 span 级错误定位，而非评价终端报告质量。
- [GAIA](./gaia.md) — 面向工具使用型助手的"短答案、唯一无歧义答案"范式，正是本类报告生成 benchmark 有意避开的路径。
