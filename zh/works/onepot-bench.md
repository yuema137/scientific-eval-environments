# onepot-Bench 0 (2026)

> [English](../../works/onepot-bench.md) | **简体中文**

## Overview

onepot-Bench 0 是一套私有的、面向实验室现实的化学 benchmark 套件，分三部分：ChemAbacus（不借助工具的化学信息学素养与数值推理）、SynthRefusal（在良性、管制与设计毒品类目标上刻画安全与拒答行为）、SynthBench（用作者实验室产生的私有实验数据评估反应结果预测与催化剂选择）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.02595>
- **Venue:** arXiv preprint (cs.LG), 2026

## Summary

这套套件的出发点是：公开的化学评测可能早已进入模型训练语料，因此 onepot-Bench 0 把最硬的部分锚定在不可能泄漏的数据上——作者自己实验室做出的实验。ChemAbacus 探测模型不借助工具能对分子算出什么；SynthRefusal 刻画模型在从良性到设计毒品合成目标的谱系上把安全线画在哪里；SynthBench 要求预测只有私有实验记录才能证实的反应结果与催化剂选择。

## Tasks

三项互补评估——化学信息学/数值问题（无工具）、跨目标类别的拒答探测、对照私有实验数据的反应结果/催化剂选择预测；静态预测，非交互。任务数量为 TODO(reference)——摘要未载明。

## Domains

化学——合成化学与化学信息学，含催化剂选择与湿实验产生的真值。

## Evaluation

- 分组件评估：素养/数值评分（ChemAbacus）、拒答行为刻画（SynthRefusal）、对照私有实验结果的预测（SynthBench）。
- **报告。** 摘要未给出头条数字。

## Typical Duration

三个子组件下的单轮问题与预测。

## Main Contribution

一个构造上即防泄漏的评估锚点：在作者实验室里测得的反应结果不可能出现在任何训练语料中，无论模型的知识截止在哪。

## Key Design Ideas

- 私有实验数据从源头解决污染，而非事后过滤。
- 能力（ChemAbacus）与安全（SynthRefusal）捆绑，在同一批模型上同时评这两轴。
- 「面向实验室现实」：真值来自实验台上的化学，而非数据库。

## Strengths

- 私有数据设计给出了公开 benchmark 无法企及的防污染保证。
- 在分级目标谱系上刻画拒答行为，这在化学评估中很少见。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要之外的细节有待全文校验。这套套件明确为私有——无公开代码、数据与任务数量——独立复现与横向比较因此受限。

## Related Works

- [ChemIQ](./chemiq.md) — 同样是不借助工具的化学信息学与数值推理，但是公开 benchmark。
- [LABBench2](./labbench2.md) — 同样以实验室为根基，对照实验现实评估模型。
- [BioXArena](./bioxarena.md) — 同样用私有/隐藏测试数据堵住泄漏渠道。
