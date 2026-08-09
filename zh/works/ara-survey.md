# Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap (2026)

> [English](../../works/ara-survey.md) | **简体中文**

## Overview

一篇关于自主研究 agent（“AI scientist”）的综述，聚焦验证缺口：系统完成研究任务的能力，与学界验证其宣称的能力之间的落差。从 125 篇候选筛出 35 篇收录，其中 26 篇做了全文编码，覆盖七个审计维度。

## Topics

- [Survey](../topics/survey.md)

## Activities

N/A — 综述或立场论文，无受评任务。

## Links

- **Paper:** <https://arxiv.org/abs/2608.05179>
- **Venue:** arXiv preprint (cs.CY, cs.AI), 2026

## Summary

综述沿七个审计维度为系统编码——生命周期阶段、自主等级、评估方法、发布工件、人在环节点、新颖性验证、结果挑选的披露情况。发现 83% 的系统发布代码，但仅 38% 发布随机种子或执行轨迹、仅 38% 报告任何新颖性验证方法；九个闭环 L4 系统中七个仅靠机械重跑验证、一个仅有作者自述而无外部检查；语料中没有任何 LLM 时代的系统展示过经外部验证的在环 oracle。一份审稿人清单使该审计可操作化。

## Tasks

N/A——综述论文。语料：筛查 125 篇候选，收录 35 篇，26 篇全文编码（24 个可运行系统、2 篇立场/研究论文）。

## Domains

跨科学领域的自主研究 agent；综述本身领域无关。

## Evaluation

- N/A——综述论文。贡献是七维审计协议与编码语料。
- **报告。** 83% 发布代码；38% 发布种子或执行轨迹；38% 报告任何新颖性验证方法；没有 LLM 时代系统展示经外部验证的在环 oracle。

## Typical Duration

N/A——综述论文。

## Main Contribution

点名并量化了自主研究 agent 的验证缺口，并把审计转化为可复用的审稿人清单。

## Key Design Ideas

- 验证工件（种子、轨迹、oracle）与能力宣称分开审计。
- 自主等级对照生命周期阶段映射，使“闭环”宣称可以逐阶段核查。
- 结果挑选的披露情况被作为一等审计维度。

## Strengths

- 用逐系统的编码证据为一个普遍存在的担忧提供实证依据。
- 审稿人清单使该审计可被他人重复。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [Survey on Evaluation of LLM-based Agents](./agent-evaluation-survey.md) — 同样综述 agent 评估全景；本综述则针对研究 agent 子领域审计其可验证性。
- [EXP-Bench](./exp-bench.md) — 把验证关切落为 benchmark：带可执行检查的完整实验复现。
- [ResearchClawBench](./researchclawbench.md) — 其隐藏论文设计直接回应了本综述记录的验证问题。
