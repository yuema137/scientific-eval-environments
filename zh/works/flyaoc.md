# FlyAOC (2026)

> [English](../../works/flyaoc.md) | **简体中文**

> **首次公开：** 2026-02-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2602.09163)

## Overview

FlyAOC 是面向端到端 agentic 本体策展的 benchmark：agent 拿到的只有一个基因符号，须在 16,898 篇果蝇全文论文的语料中检索并阅读，产出以本体为锚的结构化标注，再与取自 FlyBase 的 7,397 条专家策展结果比对打分。（同一版本的 arXiv 摘要中也把该 benchmark 称作「FlyBench」；论文标题、发布的代码与仓库名用的都是 FlyAOC。）

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.09163>
- **Code:** <https://github.com/xingjian-zhang/flyaoc>

## Summary

维护一个科学知识库，靠的是专家策展员去找到相关论文、跨文献调和证据，并把结果表达为以本体为锚的标注。FlyAOC 指出，现有 benchmark 只截取了这套工作流中孤立的子任务——命名实体识别、关系抽取——它要评的则是策展员完整的工作闭环。benchmark 建立在果蝇（Drosophila melanogaster）知识库 FlyBase 之上，把一份固定的文献语料与策展员真正由此产出的专家标注配成一对。论文比较了四种基线 agent 架构，报告称架构的影响大于基座模型规模，且所有基线都留有相当大的提升空间。

## Tasks

100 个 benchmark 基因，每个都作为一道开放式策展任务，面向同一份 16,898 篇全文论文的共享语料（报告为逾 1.4 亿词，取自 PubMed Central）。计分的标注任务共三类，标准答案合计 7,397 条专家策展标注：Gene Ontology 功能条目（3,621 条标注，涉及 1,228 个不同条目）、表达模式（1,331 条标注，涉及 465 个解剖学条目与 69 个发育阶段），以及贯通数十年命名沿革的历史同义名（2,445 条标注）。论文另外划出一个「语料可及」子集——即确实能从所发布语料中还原出来的那部分标注——占 GO 条目的 28.9%、表达标注的 37.0%、同义名的 36.4%。

## Domains

生物学。任务取自 FlyBase 所策展的果蝇（Drosophila melanogaster）遗传学与分子生物学，要求阅读一手生物学文献，并把证据映射到 Gene Ontology 以及解剖学／发育阶段本体上。论文未主张任何共存领域；文中把检索增强推理这项能力说成可以迁移，但受评任务是生物学任务。

## Evaluation

预测结果按标注类型分别打分。Gene Ontology 与表达标注用 semantic recall@k：在本体的有向无环图上以 Wang 相似度为本体上相近的预测给出部分分；历史同义名则采用大小写不敏感的完全匹配，搭配标准 recall@k。论文对 GO 与同义名取 k=20，对表达取 k=10，取值大致为每个基因语料可及标注数均值的两倍。主报告指标是对所有标注等权的 micro 平均召回率。比较的四种基线架构为：记忆型（不检索）、固定流水线、单 agent 与多 agent。在每个基因 16 篇论文、基座为 GPT-5-mini 的设置下，多 agent 基线报告的 semantic recall 为 Gene Ontology 53.1%、表达 52.8%、同义名 57.3%；单 agent 基线一旦超过约 8 篇论文就因上下文溢出而退化。

## Typical Duration

未报告 wall-clock 预算。成本按每基因报告，设置为每个基因 16 篇论文、基座 GPT-5-mini：多 agent 基线约 $0.37/基因，单 agent 基线 $0.85/基因，固定流水线 $0.10/基因。

## Main Contribution

按作者的说法，这是首个在「从科学文献做端到端 agentic 本体策展」这件事上评估 AI agent 的 benchmark，而非像既有 benchmark 那样只针对孤立的抽取子任务；其依托的是一个真实、仍在维护的科学知识库及其专家策展记录。

## Key Design Ideas

- 任务输入刻意压到最少——只给一个基因符号——检索、跨文献调和与本体锚定因而全部落在受评闭环之内。
- 一份固定且公开发布的 16,898 篇全文语料使检索可复现，也让作者得以区分哪些标注能从语料还原、哪些不能。
- 本体感知的打分：semantic recall@k 配 Wang 相似度，对本体上贴近标准条目的预测给部分分，而不是把标签集当作扁平的。
- 记忆型基线（不检索）用来分离出一件事：果蝇是研究得极为充分的模式生物，agent 的输出里究竟有多少只是出自它对果蝇的参数化知识。
- 记忆型、固定流水线、单 agent、多 agent 四种架构铺开设计空间，用来把性能归因于架构还是基座规模。

## Strengths

- 标准答案是生产级知识库中真实的策展产出，而非为 benchmark 专门制作的标注。
- 语料可及子集把天花板摆到了明处，召回数字可以对照所发布语料实际支撑的上限来读。
- 本体感知的部分给分比完全匹配更适合策展任务，而同义名任务在合适之处仍保留完全匹配。
- 每基因成本与准确率一并报告，架构比较因而可以当作成本／质量权衡来读。
- 行为分析是诊断性的而非点缀：所发现的「agent 主要用检索来确认参数化知识、而不是发现新信息」是一种具体的失败模式。

## Limitations

- 只做纯文本评估；图件不在其内，而图件恰恰承载了大量表达证据。
- 语料只覆盖与 benchmark 基因相关论文的约 30%，因此绝对召回率低估了可达到的水平。
- FlyBase 的标准答案本身可能并不完整，没有匹配上的预测未必就是错的。
- 设定是完全自主的策展；真实策展所采用的人在环工作流不在评估之列。
- 果蝇是研究得最密集的模式生物之一，此处的参数化知识异常强——记忆型基线因而具有参考价值，但能否迁移到研究较少的物种尚未验证。
- Repository note: 报告的头条数字来自单一基座（GPT-5-mini）与单一检索深度；本卡片不含完整的跨模型表格。

## Related Works

- [BioKGBench](./biokgbench.md) — 同样把生物医学知识图谱放在 agent 任务的中心，但打分对象是在既有 KG 中找错，而非产出新的策展结果。
- [Frontier LLM-based agents can overcome the ontology curation bottleneck for natural phenotypes](./frontier-llm-based-agents-can-overcome-the-ontolog.md) — 受评任务相同（对照专家策展员的 agentic 本体策展），落在比较形态学而非果蝇遗传学。
- [LAB-Bench](./lab-bench.md) — 生物学研究能力套件，其文献与数据库子任务正是 FlyAOC 用来对照自身的那些孤立子任务。
- [CeProBench](./ceprobench.md) — 同样以专家标注的实体／关系为标准答案，做文档到知识图谱的抽取任务，但在另一个领域。
- [ScholarQuest](./scholarquest.md) — 单独评估 agentic 文献检索，不含下游的结构化标注环节。
