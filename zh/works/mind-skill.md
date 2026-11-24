# MIND-Skill (2026)

> [English](../../works/mind-skill.md) | **简体中文**

> **首次公开：** 2026-05-09 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.08670)

## Overview

MIND-Skill 是一种 skill 生成方法：每写出一个 skill，都先打分，再决定能不能信任它。在单遍 pipeline 里，LLM 读一条成功的 agent trajectory，写出一份 skill 文档，之后没有任何环节检查这份文档是否真的承载了那套做法。MIND-Skill 加了第二个 agent：它只拿到任务和 skill，必须在真实环境里把同一个任务重新做一遍。根据这次重建算出三项 loss（trajectory 匹配、任务结果和文档 rubric），再通过 TextGrad 反馈回去，改写写 skill 的那个 agent 的 prompt。得到的 skill 随后在 AppWorld 和 BFCL-v3 的留出任务上测试。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 这是 skill 生成方法，评测对象是通用的应用/API 交互和 function calling（AppWorld、BFCL-v3），没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2605.08670>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

Induction agent 拿到任务说明和一条成功的 ReAct trajectory，写出一份结构化 skill；它的 system prompt 是唯一被优化的变量。Deduction agent 的 prompt 固定，也看不到原始 trajectory，只凭任务和 skill 在环境里重新执行任务。接着用三项文本 loss 给 skill 打分：一个 LLM judge 在策略层面比较重建 trajectory 和原始 trajectory（reconstruction loss，0–10）；环境检查重建是否没能完成任务（outcome loss，0–1）；另一个 LLM judge 按五个 rubric 维度评价 skill（rubric loss，0–10）。TextGrad 的 gradient LLM 把这三份反馈变成对 induction prompt 的一次修改，每个训练任务迭代 8 次，并按字典序选择保留目前最好的 skill（先看 outcome，reconstruction 和 rubric 依次用来打破平局）。这个方法要求每个训练任务都有一条成功 trajectory，所以 agent 从没做成过的任务，它写不出 skill。

## Tasks

N/A — MIND-Skill 是 skill 生成方法，不是 benchmark。实验使用两个现有 benchmark：

- **AppWorld** — 9 个应用、457 个 API；用 90 个训练任务提取 skill；在 168 个 Test-Normal 和 417 个 Test-Challenge 任务上评测。
- **BFCL-v3**（base multi-turn 类别）— 200 个实例，随机分成 50 个训练和 150 个测试实例。

测试时，一个检索用的 LLM 只看每个 skill 的名称和描述，选出 top K = 3 个 skill，再把它们的完整内容注入 agent 的 context。

## Domains

通用 agent 环境（应用/API 交互和多轮 function calling）。不针对任何规范的科学或工程领域。

## Evaluation

评测分两个层面。

- **循环内部（skill 质量）。** 对一个训练任务：induction agent 根据 trajectory τ 写出 skill *s*；deduction agent 根据任务和 *s* 产生 τ̂；环境执行 τ̂，返回 ℓ_outcome ∈ [0, 1] 和执行反馈；一个 LLM judge 就 τ̂ 与 τ 在策略层面是否等价给出 ℓ_recon ∈ [0, 10]；另一个 LLM judge 按 ground-truth independence、actionability、transferability、completeness 和 conciseness 给出 ℓ_rubric ∈ [0, 10]。这些分数既驱动 TextGrad 更新，也用来决定保留哪个 skill。
- **留出集（下游）。** AppWorld 用 Task Goal Completion（TGC）和 Scenario Goal Completion（SGC）计分；BFCL-v3 用准确率（ACC）。
- **报告结果（Qwen3.5-122B-A10B 既生成也使用 skill）。** MIND-Skill 在 AppWorld Normal 上 TGC 71.4 / SGC 55.4，在 AppWorld Challenge 上 TGC 51.8 / SGC 39.6，在 BFCL-v3 上 ACC 77.3（平均 59.1）；同一平均口径下，ReAct 为 42.8，Skill-extract（单遍归纳）为 51.0，ACE 为 56.1，Trace2Skill 为 55.1。用 GPT-5.4 生成 skill 时，平均为 58.9。
- **Loss ablation（AppWorld，Qwen）。** 去掉 outcome loss，Normal TGC 68.5 / Challenge TGC 48.0；去掉 reconstruction，66.1 / 45.8；去掉 rubric，64.3 / 46.5；完整方法为 71.4 / 51.8。

## Typical Duration

TODO(reference) — 没有报告 token、成本或 wall-clock 的绝对数字。构建 skill 时每个训练任务跑 8 次 TextGrad 迭代；论文报告注入的 skill token 数比 ACE 的 playbook 和 Trace2Skill 的 skill 目录小 3–6 倍。

## Main Contribution

作者把写 skill 看成一个优化问题：skill 好不好，取决于另一个 agent 能否凭它重建出原来的解法。他们把 reconstruction、outcome 和 rubric 三项 loss 组合成一个闭环，用来改写写 skill 的那个 agent 的 prompt。

## Key Design Ideas

- Induction 与 deduction 分离：使用 skill 的 agent 从来看不到 skill 所依据的 trajectory，因此重建检验的是 skill 文档本身传达了什么。
- 三项互补的检查：环境执行（outcome）、LLM 判定的策略等价（reconstruction）、LLM 判定的文档 rubric。
- 被优化的是 induction prompt，而不是单个 skill；gradient LLM 能看到重建结果，但看不到原始 trajectory。
- 字典序选择，outcome loss 优先，并记录目前最好的 skill，后面的迭代不会覆盖掉更好的 skill。
- Induction prompt 明确把内容分成三类：程序性约定要保留；能从指令里推出来的知识不写进去；泄漏 ground-truth 的内容也不写进去。

## Strengths

- 包含单遍 ablation（Skill-extract，相当于第 0 次迭代），因此能直接量出评估循环带来的收益：Qwen 生成的 skill 平均 +8.1 分，GPT-5.4 生成的 skill 平均 +7.2 分。
- 每项 loss 都在两个 AppWorld 划分上单独做了 ablation。
- 既报告了自生成的设定，也报告了跨模型（GPT-5.4 作为生成器）的设定。

## Limitations

- 需要成功的 trajectory 作为输入，skill library 因此只能覆盖 agent 已经会做的任务；作者提到可以退而使用 ground-truth 解题脚本。
- 三项 loss 中有两项由 LLM 判定；论文没有报告这些 judge 与人工评分的对照验证。
- 只在两个通用 agent benchmark 上、用一个推理模型（Qwen3.5-122B-A10B）做了评测。
- Repository note: 本卡片依据 arXiv v1 摘要和 HTML 全文编写（2026 年 11 月）；论文没有给出代码仓库链接。

## Related Works

- [SkillLearnBench](./skilllearnbench.md) — 评测持续 skill 生成方法，并直接给生成的 skill 打分，而这正是 MIND-Skill 优化的量。
- [SkillEvolBench](./skillevolbench.md) — 检验从 agent 自身 trajectory 蒸馏出的 skill 在任务偏移后是否还站得住，这正是 MIND-Skill 留出集评测想看的迁移。
- [Skill Coverage](./skill-coverage.md) — 同样拿 agent trajectory 来检查 skill，测量一条 trajectory 实际用到了 skill 中的哪些约束。
- [SkillGen](./skillgen.md) — 同样用执行反馈来把关 skill 生成，做法是对比有无 skill 的配对结果，而不是重建 trajectory。
