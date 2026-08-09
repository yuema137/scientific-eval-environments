# MedBrowseComp (2025)

> [English](../../works/medbrowsecomp.md) | **简体中文**

## Overview

MedBrowseComp 评测医学 deep research 与 computer use：1,000 余道由医生整理的问题，要求 agent 从实时的领域知识库——临床试验、一手研究、监管文件与费用数据——检索并综合多跳医学事实。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.14963>
- **Code:** <https://github.com/shan23chen/MedBrowseComp>
- **Dataset:** <https://huggingface.co/datasets/AIM-Harvard/MedBrowseComp>
- **Project:** <https://moreirap12.github.io/mbc-browse-app/>
- **Venue:** arXiv preprint (cs.CL), 2025

## Summary

真实的临床问题很少只住在一个来源里：MedBrowseComp 由医生整理的问题迫使 agent 在实时知识库间调和零散甚至相互矛盾的信息——试验注册库、一手文献、FDA 批准与独占期记录、药物专利与医疗费用数据——得出最新的结论。发布的切分（官方数据集）包括 MedBrowseComp-50、MedBrowseComp-605 与 computer-use 切分 MedBrowseComp-CUA（484）。agent 在最难设定下的表现最低仅约一成。

## Tasks

1,000 余道由医生整理、跨实时医学知识库的多跳问题，覆盖 deep-research 与 computer-use 两种设定（据官方数据集分为 50、605 与 484 三个切分）。

## Domains

临床与监管医学：临床试验、药理学、FDA 批准与独占期、药物专利与医疗费用数据。

## Evaluation

- 对照人工整理的标准答案评估多跳检索与综合；判分实现细节为 TODO(reference)。
- **报告。** agent 在最难设定下的表现最低仅约一成。

## Typical Duration

每题为实时浏览 / computer-use 回合。

## Main Contribution

把医学 deep-research 评估锚定在临床医生实际查阅的、实时且零散的来源上——被测的技能是时效与调和，而不是记忆。

## Key Design Ideas

- 实时知识库使答案随时间变化，检索无法被记忆替代。
- 多跳构造强制跨来源调和，包括相互矛盾的记录。
- CUA 切分把同一批问题扩展到 computer-use agent。

## Strengths

- 医生整理的题目覆盖多数 benchmark 忽视的监管与经济来源。
- 实时来源的设计天然兼作持续的防污染机制。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [BioKGBench](./biokgbench.md) — 同样是面向验证的生物医学知识源导航，基于整理好的知识图谱。
- [AutoResearchBench](./autoresearchbench.md) — 同样是开放网络的多跳发现评估，面向科学文献。
- [MedHELM](./medhelm.md) — 同样是医生锚定的医学评估，基于静态任务套件。
