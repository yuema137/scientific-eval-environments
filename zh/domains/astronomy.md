# Astronomy

> [English](../../domains/astronomy.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

天文学与天体物理，包括基于观测数据的推断。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Stargazer | 2026 | 从径向速度时间序列推断系外行星系统：提出能解释观测恒星信号的行星数量与轨道参数，并基于逐项反馈迭代。 | 120 个模型拟合任务——100 个合成任务分三个难度层，另有 20 个来自 NASA Exoplanet Archive 与 VizieR 的真实档案系统，行星数 1–7。 | 四项物理判据须同时满足：残差 RMS ≤ 1.5× 测量不确定度、相对常数零模型的 ΔBIC 为正、匈牙利算法匹配的行星恢复 ≥ 0.8、行星数完全正确。 | [→](../works/stargazer.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的天文任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Astronomy 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [Stargazer](../works/stargazer.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
