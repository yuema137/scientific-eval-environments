# MolecularIQ (2026)

> [English](../../works/moleculariq.md) | **简体中文**

## Overview

MolecularIQ 是只收录「符号可验证」任务的分子结构推理 benchmark：每个答案都能对照分子图本身检验，从而摆脱大多数化学 benchmark 里引入泄漏与偏差的文献标签、代理标签和选择题形式。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2601.15279>
- **Code:** <https://github.com/ml-jku/moleculariq>
- **Leaderboard:** <https://huggingface.co/spaces/ml-jku/molecularIQ_leaderboard>
- **Venue:** ICLR 2026（据官方仓库；arXiv 元数据未载明发表信息）

## Summary

MolecularIQ 的出发点是：分子的性质由其分子图编码的组成与结构决定，因此对分子的推理必须以真正解析分子图为前提。它的任务经过筛选，正确性可以符号化验证——不依赖有泄漏风险的文献或代理标签，也不用选择题。细粒度评估把模型失败定位到具体任务与具体分子结构上，为当前化学 LLM 画出能力「指纹」。

## Tasks

符号可验证的分子图推理任务；静态评估。任务与实例数量为 TODO(reference)——摘要与仓库 README 均未载明。

## Domains

化学——分子结构与图层面的推理，是性质预测与反应预测底下的基座能力。

## Evaluation

- 对照分子图做符号验证；细粒度拆分把失败定位到具体任务与结构类型。
- **报告。** 摘要未给出头条数字；官方维护公开排行榜。

## Typical Duration

单轮任务；无交互式设定。

## Main Contribution

对「化学 LLM 是否真的会解析分子结构」的抗泄漏测量——验证只需要分子本身，不需要任何外部标签。

## Key Design Ideas

- 把符号可验证性作为任务的准入标准，而非事后补充。
- 失败可定位到结构类型，使 benchmark 具有诊断性而不止于排名。
- 用能力指纹取代单一分数的排序。

## Strengths

- 构造上即免疫标签泄漏与标注偏差。
- 诊断粒度可以指导模型开发，而不仅是模型选型。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；规模数字在这些来源中未载明，仍为 TODO(reference)。

## Related Works

- [MolLangBench](./mollangbench.md) — 同样用化学信息学工具验证结构任务，并延伸到编辑与生成。
- [ChemIQ](./chemiq.md) — 同样是无 judge 的化学评估，以规范结构匹配判分。
- [FGBench](./fgbench.md) — 同样以结构为根基的性质推理，粒度在官能团层面。
