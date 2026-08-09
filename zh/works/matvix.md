# MatViX (2024)

> [English](../../works/matvix.md) | **简体中文**

## Overview

MatViX 评测从图文丰富的材料论文中做多模态信息抽取：324 篇全文研究论文配 1,688 个由领域专家策划的复杂结构化 JSON，视觉-语言模型须在零样本设定下从文本、表格与图中抽取成分与性质曲线。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.20494>
- **Code:** <https://github.com/ghazalkhalighinejad/matvix>
- **Project:** <https://matvix-bench.github.io/>
- **Venue:** arXiv preprint (cs.CL), 2024

## Summary

材料知识既锁在文字里，也锁在图表里，MatViX 检验 VLM 能否把它释放出来：324 篇全文论文（聚合物纳米复合材料与生物降解）映射到 1,688 个专家策划的结构化 JSON，把成分（字符串）与性质（(x,y) 曲线点列）结合。模型以零样本方式抽取，而该 benchmark 的独特之处在于——它不仅评判实体，还评判所抽取曲线的保真度。

## Tasks

对 324 篇全文论文的零样本多模态抽取，产出 1,688 个结构化 JSON 记录（成分 + 性质曲线），来自文本、表格与图；静态抽取。

## Domains

材料科学——面向聚合物纳米复合材料与生物降解的结构化数据抽取，来自图文丰富的全文论文。

## Evaluation

- 成分对齐的 F1；所抽取性质曲线的曲线相似度分（CSS）与曲线对齐分（CAS）。
- **报告。** 零样本 VLM 在基线、纯文本与文本+图三种配置下受评；各模型数字在正文中（TODO(reference)）。

## Typical Duration

以全文文档为单位的抽取；无交互式设定。

## Main Contribution

把材料抽取评估扩展到全文与曲线——评判埋在图里的 (x,y) 数据，而不只是文本中的具名实体。

## Key Design Ideas

- 曲线保真度指标（CSS、CAS）评判材料论文真正承载的图数据。
- 全文论文迫使跨版块整合（文本 + 表格 + 图）。
- 专家策划的 JSON 目标使抽取模式忠于领域。

## Strengths

- 少数评判「图派生数值曲线」的材料抽取 benchmark 之一。
- 项目、代码与专家策划的目标均公开。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；参评模型名单与各模型数字在正文中。arXiv 元数据无发表信息；写作时数据集标注为「即将发布」。

## Related Works

- [MatCha](./matcha.md) — 同样是多模态材料理解，考表征问答而非抽取。
- [ChemX](./chemx.md) — 同样是 agent 式化学/材料信息抽取，基于专家校验的数据集。
- [MatTools](./mattools.md) — 同样是模型做结构化材料计算，走工具使用。
