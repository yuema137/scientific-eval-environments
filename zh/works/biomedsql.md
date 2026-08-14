# BiomedSQL (2025)

> [English](../../works/biomedsql.md) | **简体中文**

## Overview

BiomedSQL 是一套 text-to-SQL benchmark，建在一个统一整合的生物医学知识库上，库中含基因–疾病关联、组学因果推断结果与药物审批记录；要答对一道题，模型必须自行补上问题从未言明的领域判据——全基因组显著性阈值、效应方向、试验期相筛选条件。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.20321>
- **Code:** <https://github.com/NIH-CARD/biomedsql>
- **Data:** <https://huggingface.co/datasets/NIH-CARD/BiomedSQL>
- **Venue:** COLM 2026

## Summary

论文的前提是：现有 text-to-SQL benchmark 奖励的是语法层面的转写，而一位生物医学分析师查询真实研究数据库时，首先要定下问题在操作层面究竟指什么——哪个 p 值才算全基因组显著，哪个效应方向才回答了「升高风险」，哪个试验期相才算获批。BiomedSQL 把 68,000 组「问题／SQL 查询／答案」三元组落在一个由可信生物医学资源汇聚而成的在线 BigQuery 数据库上，使得写对查询必须依赖问题留白的领域判据。作者在若干提示策略与交互范式下评测了开源与闭源 LLM，还自建了一个多步 agent BMSQL，通过中间结果与执行报错的反馈来迭代改写查询。所有配置都远不及人类专家基线，作者以此说明真正的约束是科学推理，而不是 SQL 语法。

## Tasks

68,000 组「问题／SQL 查询／答案」三元组。构造从 40 条专家撰写的种子查询起步，这些种子「随后经模板化并扩展，做法是以编程方式插入疾病、基因与 SNP 提及，使之对齐到 CARDBiomedBench 中全部 68,000 组问答对」。模型打分则在「一个 546 题的代表性测试集上进行，其采样保持了完整 benchmark 中专家撰写模板的分布」。

题目沿两条正交的轴打标签：八类 SQL 任务（Select、Distinct、Join、Multi-Filter、Threshold、Calculate、Order By、Similarity Search）与九类生物医学推理（Approval Status、Trial Phase、GWAS Significance、SMR Significance、Functional Significance、Effect、Genetic Target、Allele Frequency、Metadata）。

底层存储是「一个关系数据库，含取自可信生物医学资源的十张核心表」：阿尔茨海默病 GWAS、帕金森病 GWAS、阿尔茨海默病与帕金森病基因通路关联、神经退行性疾病 SMR 关联、神经退行性疾病等位基因频率、药物基因靶点、药物靶点适应症、药物许可与药物剂量。各表规模从数百行（通路关联）到数千万行不等（等位基因频率 7,220 万行，阿尔茨海默病 GWAS 表 2,110 万行）。

## Domains

生物学，以及医学与健康。数据库的遗传学那一半是人类基因组学数据——神经退行性疾病的 GWAS 汇总统计、SMR 因果推断结果、等位基因频率与基因–通路关联——回答这些问题要用到统计遗传学的惯例，因而归入生物学。药理学那一半——药物基因靶点、适应症、许可状态与剂量——关乎临床转化与药物审批，因而归入医学与健康。把它读作计算机科学也说得通，毕竟产出的工件是 SQL，但受评目标是检索出生物医学上正确的记录，而非通用的数据库推理。

## Evaluation

- **Execution Accuracy（EX）：** 主指标，定义为「对每道题的二值指标：生成查询的执行输出与标准执行结果完全一致时才得 1 分」。
- **Jaccard Index（JAC）：** 预测执行结果与标准执行结果的交并比，作为 EX 的部分给分搭档。
- **Syntax Error Rate（SER）：** 生成查询中无法执行的比例。
- **Response Quality Rate（RQR）与 Safety Rate（SR）：** 经 BioScore 计算的 LLM 评判指标，覆盖自然语言回答的质量以及拒答／安全行为。
- **人类基线：**「两位生物医学分析师各自独立完成了从 546 题测试集中随机抽取的 20 道题」，报告的是两位专家的均值——EX 90.0%（95% CI 约 [68%, 99%]）、JAC 90%、RQR 95%。
- **报告。** 基线提示下最强的几个模型（EX/JAC/RQR）为：Gemini-3-Pro，58.1%/62.4%/81.8%；Claude-4.5-Opus，54.8%/59.7%/80.6%；GPT-o3-mini，53.5%/60.4%/73.3%。作者的多步 agent BMSQL 配 GPT-o3-mini 达到 62.6% EX，是总体最好的结果，但仍比专家基线低约 27 个百分点。
- **对比的配置：** 基线 schema 提示、1-shot 到 40-shot 的少样本提示、样例行提示（3 行与 5 行）、显式给出领域统计阈值的指令、ReAct 提示、schema 索引、DAIL-SQL 的适配版本，以及 BMSQL 的多步改写。

## Typical Duration

基线与少样本配置都是面向 schema 的单轮生成。BMSQL 则是一条迭代式 text-to-SQL 循环，借中间结果与执行报错改写查询。`TODO(reference)` — 所查阅的一手来源未给出单任务的步数上限、wall-clock 预算或 token 预算。

## Main Contribution

作者把 BiomedSQL 定位为「首个明确面向真实世界生物医学知识库、用于评估 text-to-SQL 生成中科学推理能力的 benchmark」，以区别于只考 schema 映射的 text-to-SQL 套件。其自陈的贡献在于把一个生产级、统一整合的生物医学数据库，与一批「不靠领域知识就无法唯一确定正确译法」的问题配到一起，再加上一条实测的专家基线来量化尚存的差距。

## Key Design Ideas

- 题目的写法刻意让起作用的筛选条件保持*隐含*：模型必须自己知道全基因组显著性阈值、效应方向的含义，或者哪些试验期相算数，而不是从提示里读出来。
- 两轴标签把 SQL 结构难度（八类查询形态）与生物医学推理需求（九类推理）分开，失败因而可以归到其中某一条轴上。
- 数据库是一个真实的 BigQuery 存储，把异构的公开生物医学资源统一整合到一起，规模也是真实的，而不是合成或缩微的 schema。
- 从 40 条专家撰写的种子查询经程序化模板扩展放大，换来一个 68,000 条目的 benchmark，同时每个条目都仍可追溯到某个专家写的形式；546 题的测试集采样时保持了这一模板分布。
- 指标是分层的：完全执行匹配（EX）作头条指标，Jaccard 给部分分，语法错误率把「写坏了」与「写错了」分开，再用 LLM 评判的回答质量与安全率覆盖自然语言答案。
- benchmark 之外另配了一个专门构建的 agent（BMSQL），用来确认迭代执行反馈究竟能补上多少差距。

## Strengths

- 落在一个真实运行、规模达数千万行的生物医学数据库上，难度因而贴近分析师的实际工作，而不是精修过的玩具 schema。
- 隐含判据的设计隔离出了一种语法型 text-to-SQL benchmark 无法暴露的失败模式，两轴标签又让它可诊断。
- 实测而非假定的人类专家基线，为报告的差距提供了锚点。
- 配置覆盖面广——提示策略、少样本规模、ReAct、schema 索引、DAIL-SQL 与多步 agent——表明这一差距并非提示写得不好造成的假象。
- benchmark、数据库与 agent 代码均已公开发布。

## Limitations

- 专家基线建立在两位分析师完成的 20 道题之上，作者自己给出的置信区间也很宽（约 [68%, 99%]），因此 90.0% 这个天花板估得很松。
- 68,000 组三元组是 40 条种子查询的模板扩展，条目多样性因而受限于这些种子；实际不同的问题形态数远少于头条数字。
- Repository note: 该数据库局限于神经退行性疾病遗传学与药物审批记录，测得的性能未必能迁移到其他生物医学查询领域。
- Repository note: RQR 与 SR 经 BioScore 由 LLM 评判，继承了评判者偏差，而 EX 与 JAC 有执行作依托；两族指标的可靠性并不对等。
- Repository note: 所查阅的一手来源未报告任何单任务的步数、时延或 token 预算，因此 BMSQL agent 相对单轮提示的准确率增益究竟花了多少成本，此处无从量化。

## Related Works

- [ALeRCE Text-to-SQL](./alerce-text-to-sql.md) — 同一种问题形态（在真实科学数据库上把自然语言转成 SQL，标准查询由专家撰写），落在天文学而非生物医学。
- [BioKGBench](./biokgbench.md) — 同样把生物医学知识结构作为被查询的底座，但为 agent 在图中找错打分，而不是为把问题译成查询打分。
- [MedBrowseComp](./medbrowsecomp.md) — 生物医学事实检索，答案须从结构化记录中拼出，按完全正确评判。
- [MedAgentGym](./medagentgym.md) — 可执行环境中的生物医学数据科学任务，共享同一套以代码执行为准的评分模式。
