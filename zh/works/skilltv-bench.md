# SkillTV-Bench (2026)

> [English](../../works/skilltv-bench.md) | **简体中文**

> **首次公开：** 2026-08-06 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2608.05573)

## Overview

SkillTV-Bench 是面向 skill-aware 轨迹验证的 benchmark：评估 LLM-as-a-Judge 与 Agent-as-a-Judge 方法对使用 skill 的 agent 执行的验证能力。它包含来自 50 个任务、11 个领域的 681 条真实 agent 轨迹，并配套 SkillTV-Evolve——把验证知识外化为可复用的 JudgeSkill。

## Topics

- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2608.05573>
- **Venue:** arXiv preprint, 2026

## Summary

SkillTV-Bench 度量 skill 增强执行下的轨迹验证——这一设定要求评判者具备任务相关的 skill 知识才能验证正确。SkillTV-Evolve 在误判案例上运行自动进化循环，把所得验证知识蒸馏为可复用的 JudgeSkill，使同一 agent 评判者的准确率提升 14.8 个百分点，并把离线 rollout 池选择的成功率从单 rollout 的 22.9% 提升到十个 rollout 的 45.5%。

## Tasks

681 条真实 agent 轨迹，取自 11 个领域的 50 个不同任务。

## Domains

11 个领域；摘要未逐一列出。

## Evaluation

- 在 skill 增强执行上评估 LLM-as-a-Judge 与 Agent-as-a-Judge 的评判准确率。
- 离线 rollout 池选择：随 rollout 池增大，评判者所选轨迹的成功率。
- **报告。** 精炼后的 JudgeSkill 使同一 agent 评判者准确率提升 14.8 个百分点；所选轨迹成功率从 22.9%（单 rollout）升至 45.5%（十个 rollout）。

## Typical Duration

对已完成 agent 轨迹的事后验证。

## Main Contribution

把评判者而非 agent 放上 skill 增强执行的考台，并证明验证知识本身可以外化为可复用的 skill。

## Key Design Ideas

- Skill 增强执行改变了评判者必须掌握的知识；benchmark 把这一知识要求显式化。
- 误判案例驱动进化循环，产物是可携带的 JudgeSkill 而非微调模型。
- 验证质量也以其对 best-of-n 轨迹选择的下游效果来衡量。

## Strengths

- 使用真实轨迹而非合成的验证谜题。
- 量化了评判普通执行与 skill 增强执行之间的差距。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [AgentRewardBench](./agentrewardbench.md) — 同样对照真值考察轨迹评判者，但面向无 skill 增强的 web agent。
- [Plan-RewardBench](./plan-rewardbench.md) — 同样考察评判者而非 agent，采用成对轨迹偏好。
- [Skill-Use](./skill-use.md) — 同样评估 skill 增强设定，但为执行的 agent 而非评判者打分。
