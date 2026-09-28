# AutoResearchEval (2026)

> [English](../../works/autoresearcheval.md) | **简体中文**

> **首次公开：** 2026-08-13 · **来源：** [官方数据生成流水线发布](https://github.com/PrentisAI/AutoResearchEval/commit/55bb0dbf5e7a4539f22c3ef7f7d8784adb61c4b4)

## Overview

AutoResearchEval 检查研究 agent 的论断是否符合它实际生成的代码、数据与执行日志。它分析 100 个科学任务产生的 800 条轨迹，用 ARFT 将 45 种失败模式按研究阶段与四类根因整理起来。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)

## Links

- **Paper:** [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](https://arxiv.org/abs/2608.14905)，2026 年 8 月 14 日首次提交，v3 于 8 月 25 日修订。
- **Full text:** <https://arxiv.org/html/2608.14905v3>
- **Code:** <https://github.com/PrentisAI/AutoResearchEval>
- **Data:** <https://huggingface.co/datasets/PrentisAI/AutoResearchEval>
- **Venue:** arXiv 预印本。官方任务生成流水线比论文早一天发布。

## Summary

一份写得完整的报告，可能掩盖根本没有执行的实验，也可能与 agent 自己留下的文件相矛盾。因此，评判器检查整套产物，并为每项失败诊断附上证据。三位专家经过五轮一致性检查完善分类，再由 agent 评判器将检查扩展到八种 harness 与模型组合。研究关注的是反复出现的证据核对、结论修正和研究计划调整问题，并不提供科学研究成功率排行榜。

## Tasks

作者从 5,878 篇候选论文构建 70 个开放式发现任务和 30 个有明确目标的优化任务。agent 获得已有科学背景与尚待解决的问题，看不到原论文的方法和结论。它依次完成构思、检索、执行、分析、写作和自我复查，提交 `decision.json`、报告与中间产物。只有开放式子集允许实时联网检索，优化任务容器禁用联网。两个子集的领域和贡献类型不同，论文分别分析。

附录 C.9 的超声心动图案例说明了检查路径：agent 在后台启动训练，却在交付预测结果前结束会话。评判器检查文件和日志，不把容器正常退出当成研究任务成功。

## Domains

图 2 明确标注了原始领域及任务数量：生物学 **24**（15 个发现任务 + 9 个优化任务）、医学 **15**（12 + 3）、化学 **14**（9 + 5）、科学计算 **13**（11 + 2）、材料科学 **12**（7 + 5）、物理学 **12**（7 + 5）、地球物理 **10**（9 + 1）。

附录 G 包含微生物组与细胞生物学、临床预测与生物医学建模、量子化学与生物分子结合、晶体结构与材料加工、凝聚态与引力物理，以及地震和气候研究。Repository note: 地球物理归入 Earth Science；科学计算包含多种学科任务，保留为论文的原始分类，不将其全部自动归入 Computer Science。

## Evaluation

每个任务分别在八种 harness 与模型组合下运行一次：Claude Code 搭配六种模型，Codex 搭配 gpt-5-mini，Gemini CLI 搭配 gemini-3.5-flash（表 1）。ARFT 按六个生命周期阶段及一个跨阶段层标注失败，再按证据依据、认知深度、科学诚信或工程稳健性归类。

能检查产物的评判器在 **50 条人工标注轨迹**上校准。表 2 报告模式层面的 Cohen's **κ = 0.75**、根因类别层面的 **κ = 0.83**；只读对话记录、单次调用的评判器对应为 **0.53 / 0.62**，模式召回率从 **63.5% 升至 80.7%**。质量检查器会要求证据不足的分析重写，再进入模式标注。800 份分析共记录 **12,712 次模式命中**，其中 **82.5%** 出现了意识到问题却未修正的情况。这些数值是失败标签频率，不是任务成功率。

## Typical Duration

附录 F.3 给出的轨迹运行上限为 **4 小时**，另有 **1 小时环境准备时间**。评判器分析采用独立预算，通常上限为 **90 分钟**，需要重跑验证时可延长至 **210 分钟**（附录 C.3）。这些是预算上限，不是测得的典型耗时；论文没有给出轨迹 token 上限的具体数值。

## Main Contribution

发布科学任务与轨迹语料、失败分类体系，以及经人工校准、能用执行产物核对研究论断的评判器。

## Key Design Ideas

- 分开记录失败发生的阶段与用于解释失败的类别。
- 要求评判器用文件和日志中的具体证据支持判断。
- 保留没有唯一正确结论、但研究过程仍可检查的开放式任务。

## Strengths

- 将科学报告与审查它所需的中间证据联系起来。
- 对照人工标签报告评判器的一致性与召回率。
- 公开任务构建和评判代码，并单独托管数据集。

## Limitations

- 一致性仅报告总体数值，各模式和各类别的评判误差尚未量化。
- 论文未按剩余预算拆分失败频率，也无法排除已发表原论文带来的数据污染。
- Repository note: 表 1 并未把同一组模型放到全部 harness 下交叉测试。重复出现的失败支持对这些系统的描述，但仅凭这一点不能把原因单独归到模型；论文也没有测试编排干预。
- Repository note: 评判器对比同时改变了产物访问能力和评判流程，因此不能单独分离产物访问的作用。
- 官方代码仓库不包含实验所用的 Docker/SLURM 轨迹运行编排设施。

## Related Works

- [AutoResearchBench](./autoresearchbench.md)
- [Beyond Final Scores](./beyond-final-scores.md)
- [ScienceAgentBench](./scienceagentbench.md)
- [Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap](./ara-survey.md)
