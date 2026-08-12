# DrBencher (2026)

> [English](../../works/drbencher.md) | **简体中文**

## Overview

DrBencher 是一个合成式 benchmark 生成器，产出需要交织网页浏览与多步计算的问题；它以「答案优先」的方式从知识图谱链条合成问题，使得参考答案可通过对知识图谱数值执行参数化代码来验证。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A —— 通用型 deep-research 浏览+计算 benchmark 生成器，覆盖领域多为非科学领域（金融、安全、历史）；属通用网页检索与算术，而非科学/研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2604.09251>
- **Code:** <https://github.com/IBM/DrBencher>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

DrBencher 针对 deep-research agent 评估中一个被指出的盲点：既有 benchmark 往往孤立地考察浏览与计算，而真实任务会把二者交织在一起。DrBencher 不从种子文段出发，而是以「答案优先」的方式从知识图谱链条生成问题，不含出处文本。统一的流水线在五个领域上强制执行四项标准——可验证性、复杂度、难度与多样性——作者同时公开了生成流水线与一个经人工校验的 benchmark 数据集。

## Tasks

问题要求多跳实体识别、定量属性检索，以及在检索值上做领域特定计算。问题以「答案优先」方式从知识图谱链条合成（无种子文段或出处文本）。已发布的人工校验 benchmark 覆盖五个领域：生物化学、金融、地球物理、安全与历史。已发布 benchmark 的条目总数：TODO(reference)（为本卡片查阅的一手抽取在确切数量、以及人工校验后保留的数量上存在分歧）。

## Domains

五个领域：生物化学、金融、地球物理、安全与历史。各领域知识源在所有领域上都包含 Wikidata/Wikipedia，另有领域特定来源，如 PubChem、UniProt、RCSB PDB 与 ChEMBL（生物化学）、SEC EDGAR（金融），以及 NIST NVD、FIRST EPSS 与 CISA KEV（安全）。仅生物化学（化学/生物）与地球物理（地球科学）两个领域落入本仓库的科学/工程领域分类；金融、安全与历史不在其中。

## Evaluation

自动评估基于执行：参考答案由对知识图谱数值执行参数化代码算得，模型的数值回答在相对容差内（多数领域报告约 2%，历史领域为精确匹配）对照参考答案评分。所报告的「答案准确率」是回答落在容差内匹配参考值的问题比例。两阶段验证级联（先闭卷、再工具增强）过滤掉生成模型自身即可解出的问题。人工评估报告 76% 有效率，其中 35% 的错误归因于过时的知识图谱条目。

## Typical Duration

TODO(reference) —— 所查阅来源中，论文未报告标准化的单任务 token 预算或墙钟时间；任务需要交织浏览与多步计算。

## Main Contribution

一个「答案优先」、无出处的 benchmark 生成流水线：从知识图谱链条合成「浏览+计算」问题，并联合强制可验证性（可执行的参考答案）、复杂度（多跳识别、检索与计算）、难度（丢弃生成模型即可解出问题的两阶段验证级联）与多样性（贪心 max-min 嵌入过滤）。作者报告 DrBencher 相对人工构造的 benchmark（BrowseComp+、MATH-500、GPQA）取得最高的语义多样性，而所评估的最强前沿模型仅达到 20% 答案准确率。

## Key Design Ideas

- **答案优先合成。** 问题由知识图谱链条生成，无种子文段或出处文本，因此每个金标准答案在撰写自然语言问题之前就已固定。
- **构造即可验证。** 参考答案由对知识图谱数值执行参数化代码算得，而非由模型评判。
- **两阶段级联的难度过滤。** 先做闭卷验证，再做工具增强验证，丢弃生成模型已能解出的问题。
- **贪心 max-min 嵌入过滤保证多样性。** 选择过程在实体、模板与语言表达上最大化覆盖。
- **多领域知识源。** 领域特定 API/知识图谱（如 PubChem、UniProt、SEC EDGAR、NIST NVD）提供用于计算参考答案的数值。

## Strengths

- 确定性、基于执行的参考答案降低了对模型评判打分的依赖（论文）。
- 明确针对交织的浏览+计算，作者认为既有 benchmark 仅孤立评估二者（论文）。
- 同时公开生成流水线与人工校验数据集（论文；<https://github.com/IBM/DrBencher>）。

## Limitations

- 人工评估发现 76% 有效率，其中 35% 的错误源于过时的知识图谱条目——作者强调这是在演变数据上做推理的固有局限（论文）。
- Repository note: 五个领域中有三个（金融、安全、历史）落在本仓库的科学/工程领域分类之外，故该 benchmark 在范围上仅部分属于科学。
- Repository note: 已发布 benchmark 的确切规模，以及人工校验后保留的条目数，无法从本卡片查阅的来源中一致确认；这些均标记为 `TODO(reference)`。

## Related Works

- [MedBrowseComp](./medbrowsecomp.md) —— 另一个 deep-research benchmark，同样要求多跳浏览外加对结构化领域数据的检索/推理。
