# RoboFAC (2025)

> [English](../../works/robofac.md) | **简体中文**

## Overview

RoboFAC 是机器人失败分析与纠正的综合框架：9,440 条错误操作轨迹、78,623 个 QA 对、53 个场景，覆盖模拟与真实世界环境，失败类型经系统归类；配有覆盖八个 QA 维度的 benchmark，以及专用模型 RoboFAC-7B——其失败分析准确率比 GPT-4o 高 34.1%。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.12224>
- **Code:** <https://github.com/MINT-SJTU/RoboFAC>
- **Dataset:** <https://huggingface.co/datasets/MINT-SJTU/RoboFAC-dataset>
- **Venue:** arXiv preprint (cs.RO), 2025

## Summary

RoboFAC 覆盖失败理解的完整管线——任务理解、失败分析、失败纠正——数据取自 ManiSkill、ReplicaCAD、AI2-THOR 模拟与真实世界环境中的错误操作轨迹。Benchmark 含八类 QA，分别针对失败理解与纠正的不同侧面。配套的轻量模型 RoboFAC-7B 的失败分析准确率比 GPT-4o 高 34.1%；作为外部监督者接入真实世界 VLA 控制管线后，在四个任务上带来 29.1% 的相对提升，且延迟远低于 GPT-4o。

## Tasks

对 9,440 条错误轨迹（78,623 个 QA 对、53 个场景，模拟 + 真实）的失败分析与纠正 QA；benchmark 侧为静态 QA，另在真实机器人 VLA 管线中作为外部监督者在线使用。

## Domains

机器人学——横跨模拟与真实世界环境的机器人操作失败分析，作为实时监督者部署进物理 VLA 控制管线。

## Evaluation

- 按八类 QA 分维度评分；以失败分析准确率为头条指标。
- **报告。** RoboFAC-7B：失败分析准确率比 GPT-4o 高 34.1%；在四个真实管线任务上相对提升 29.1%，且延迟更低。

## Typical Duration

按轨迹的 QA；监督者部署则持续运行在机器人控制循环内。

## Main Contribution

把失败理解扩展成一门有监督的学问——一个足够大的分类失败语料，既能评测前沿模型，又能训出一个胜过它们的小专家。

## Key Design Ideas

- 八个 QA 维度把「知道失败了」与「知道哪里、为何、如何修」区分开。
- 混合的模拟 + 真实采集使语料不至于过拟合模拟器伪影。
- 监督者部署在最要紧的地方——在线、在环、有延迟约束——检验失败分析。

## Strengths

- 本处所录工作中最大的分类机器人失败 QA 语料。
- 「小专家胜过 GPT-4o」的结果量化了领域失败数据的价值。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；这些来源无法核实任何发表信息。Benchmark、数据集与模型共用 RoboFAC 之名；本卡片以 benchmark/数据集为中心。

## Related Works

- [AHA](./aha.md) — 同样用微调 VLM 做失败检测与推理，数据来自程序化失败生成。
- [REFLECT / RoboFail](./robofail.md) — 失败解释的奠基性表述与数据集。
- [LabRobFail](./labrobfail.md) — 同样用领域专用 VLM 做失败分析，面向实验室机器人。
