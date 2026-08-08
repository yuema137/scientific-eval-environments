# AHA (2024)

> [English](../../works/aha.md) | **简体中文**

## Overview

AHA 是检测并推理机器人操作失败的开源视觉-语言模型，把失败检测框定为自由形式的自然语言推理；其训练数据 AHA 数据集——大规模机器人失败轨迹集——由 FailGen 框架对成功的模拟演示做程序化扰动生成，成绩超过 GPT-4o 上下文学习 10.3%。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2410.00371>
- **Code:** <https://github.com/NVlabs/AHA>
- **Project:** <https://aha-vlm.github.io/>
- **Venue:** ICLR 2025（据官方仓库与项目页；arXiv 元数据未载明发表信息）

## Summary

FailGen 通过程序化扰动——抓取滑脱、平移与旋转偏移、顺序错误——把 RLBench 的成功演示改造成失败，得到覆盖 79 个操作任务的 AHA 数据集（官方仓库；项目页写 50+，两个官方来源存在出入）。在这些数据上微调的 AHA 检测失败并用自由语言解释，且能泛化到真实世界失败数据集与未见任务：比 GPT-4o 上下文学习高 10.3%，比六个对比模型的平均值高 35.3%。接入下游管线（奖励精化、任务与运动规划、子任务验证）后，相比 GPT-4 系模型平均提升任务成功率 21.4%。评估划分（AHA 测试集、ManiSkill FailGen 数据、RoboFail）随三项指标一并发布。

## Tasks

对机器人操作轨迹做失败检测与自由形式的失败推理；训练数据由模拟生成，评估延伸到真实世界失败数据集与未见任务。按轨迹的静态推理，另有 agent 化的下游集成。

## Domains

机器人学——横跨模拟（RLBench、ManiSkill）与真实世界失败数据的机器人操作失败检测，并作为评判器（critic）部署进机器人任务管线。

## Evaluation

- 发布的评估划分，按 LLM 模糊语义相似度、ROUGE-L 与二元成功三项指标（仓库术语）评分。
- **报告。** 比次优模型（GPT-4o ICL）高 10.3%；比六模型平均高 35.3%；三项下游集成平均提升任务成功率 21.4%。

## Typical Duration

按轨迹的失败分析；下游集成运行在更长的机器人任务循环内。

## Main Contribution

证明失败理解可以规模化训练：程序化扰动制造出真实机器人很少记录的失败数据，一个不大的微调 VLM 在「解释哪里出错」上胜过前沿模型。

## Key Design Ideas

- 把成功扰动成失败，等于免费获得密集、带标注的失败数据。
- 输出用自由形式推理（而非分类），可直接被规划器与奖励生成器消费。
- 下游集成用「有没有用」而不只是「准不准」来衡量失败理解。

## Strengths

- 「规模化失败数据」的配方可迁移到任何模拟器。
- 从模拟训练到真实失败数据集的跨域泛化是实测的，不是假设的。

## Limitations

- Repository note: 该论文的头号贡献是 AHA 模型与 FailGen 生成器；评估 benchmark 是次要贡献，本卡片覆盖发布的数据集/评估一侧。ICLR 2025 与 79 任务数字由官方页面声明而非 arXiv 元数据；官方来源之间任务数不一致（79 vs 50+）。
- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）。

## Related Works

- [REFLECT / RoboFail](./robofail.md) — 机器人失败解释的奠基性表述，其数据集被 AHA 用于评估。
- [RoboFAC](./robofac.md) — 同样是大规模失败分析与纠正 QA，配专用 7B 模型。
- [LabRobFail](./labrobfail.md) — 同样以程序化失败注入起量，专攻实验室机器人。
