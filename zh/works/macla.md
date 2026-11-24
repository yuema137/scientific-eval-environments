# MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement (2025)

> [English](../../works/macla.md) | **简体中文**

> **首次公开：** 2025-12-22 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2512.18950)

## Overview

MACLA 不动 LLM 本身，而是维护一个外部的两层 procedure library 来改进 agent：procedure 从 agent 的 trajectory 中提取，每个 procedure 按它过去成功的频率打分。参数训练类方法用 trajectory 去更新模型；MACLA 则为每个 procedure 记录一个关于成功率的 Beta 后验，按这个后验下的期望效用来选择 procedure，并让 LLM 对照这个 procedure 成功和失败的执行记录去改写它。论文在 ALFWorld、WebShop、TravelPlanner 和 InterCodeSQL 上，与 prompt 类和微调类 baseline 做比较，并对 Bayesian 选择、对比式 refinement 和 meta-procedure 层分别做了 ablation。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)

## Activities

N/A — 这是 agent memory 方法，评测用的是通用的家居、网购、旅行规划和 SQL benchmark，没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2512.18950>
- **Code:** <https://github.com/S-Forouzandeh/MACLA-LLM-Agents-AAMAS-Conference>
- **Venue:** AAMAS 2026（据 arXiv 备注已录用）

## Summary

冻结的 LLM 把每条 trajectory 切成若干子任务；每一段变成一个 procedure ⟨goal, preconditions, abstracted action sequence, postconditions⟩，如果它和已有 procedure 的 embedding 余弦相似度超过 0.85，就合并进去。由至少三个 procedure 组成、并且按稳定顺序反复成功的序列，会升级成一个 meta-procedure（「playbook」），配一个控制 policy，在继续、跳过、重复、中止之间选择。每次执行的结果都会更新对应 procedure 的 Beta(α, β) 后验，初始为 Beta(1, 1)。在决策点，agent 选期望效用最高的候选；如果最高效用低于置信阈值，就退回 zero-shot 推理。一个 procedure 积累到至少三次成功和三次失败后，LLM 会比较这两组记录，修改 preconditions、actions 和 postconditions，必要时把它拆成几个更专门的变体。

## Tasks

N/A — 方法论文，没有提出新的任务集。实验使用现有 benchmark：ALFWorld（2,851 训练，274 测试）、WebShop（1,624 训练，200 测试）、TravelPlanner（1,000 训练，180 验证，45 测试）和 InterCodeSQL（划分大小 `TODO(reference)`）。

## Domains

通用的家居交互、网购、旅行规划和 SQL 查询生成；没有评估任何规范的科学或工程领域。

## Evaluation

Backbone 是 Llama-2-7B（通过 Ollama 做 4-bit 量化，temperature 0.7，冻结）。每个 benchmark 按其任务 reward 或质量分在 0–100 的尺度上计分；TravelPlanner 使用 Commonsense 分数。用于后验更新的成功和失败反馈来自任务环境；论文没有给出明确的成功阈值。

选择时使用的期望效用为

`EU = Rel · α/(α+β) · R_max − Risk · β/(α+β) · C_fail + λ_info · H[Beta(α, β)]`，其中 `λ_info = 0.1`，`C_fail = 0.5`。

报告的结果（MACLA）：WebShop 70.2，InterCodeSQL 59.3，TravelPlanner 83.3，ALFWorld seen 87.2 / unseen 90.3，平均 78.1。最强的对比行包括 IPR（WebShop 71.3，InterCodeSQL 61.3，ALFWorld unseen 74.7）和 Qwen2.5-72B（平均 75.6，TravelPlanner 63.8），所以 MACLA 在 WebShop 和 InterCodeSQL 上不是最高。构建 memory 在一张 RTX 3090 上用时 56 秒（0.016 GPU 小时），IPR 则需要 44.8 GPU 小时；2,851 条 trajectory 被压缩成 187 个 procedure。

ALFWorld 上的 ablation（seen / unseen）：完整方法 87.1 / 90.3；去掉 Bayesian 选择 79.4 / 81.2；去掉对比式 refinement 83.6 / 85.7；去掉 meta-procedure 81.2 / 78.4；去掉 ontology 82.8 / 84.1。

## Typical Duration

多步交互 episode；论文把 50 步以上的长 episode 作为成本问题来讨论。单任务 wall-clock 时间为 `TODO(reference)`。

## Main Contribution

为冻结的 LLM agent 提供一个外部的分层程序性 memory，执行结果同时驱动选择（Bayesian 可靠度和期望效用）和修订（基于成功集与失败集对 procedure 做对比式 refinement）。

## Key Design Ideas

- 两个层级：原子 procedure，以及由它们组成、带控制 policy 的 meta-procedure。
- 每个 procedure 维护一个 Beta 后验，把执行结果变成带不确定度的可靠度估计。
- 按期望效用选择时，在估计的成功率、失败代价和对不确定 procedure 的信息奖励之间权衡。
- 对比式 refinement 只在成功和失败都积累够了（各至少三次）以后才触发。
- Memory 有上限（200 个 procedure，50 个 meta-procedure），按一个加权效用剪枝：可靠度 0.5、频率 0.3、新近性 0.2。

## Strengths

- Ablation 分开了 Bayesian 选择、对比式 refinement 和 meta-procedure 层各自的作用（论文）。
- 报告了 memory 构建成本，并与参数训练 baseline 对比（论文）。
- 分析了表现最弱的 benchmark（InterCodeSQL），把原因归结为 procedure 复用率低（51%）、可靠度低（0.64）以及 meta-procedure 用得少（18%）（论文）。

## Limitations

- 作者列出的问题包括：precondition 有歧义（例如推断出一个并不需要的冷却步骤）、长 episode 中打分成本不断累积、在 200 个 procedure 的上限下可能遗忘少见的 skill，以及基于 LLM 的 precondition 提取会臆造依赖关系。
- 在报告的表格中，MACLA 在 WebShop 和 InterCodeSQL 上并不领先（论文）。
- 论文在不同位置对同一个量给出的数字略有出入（例如 ALFWorld seen 有 87.1 和 87.2 两个值）。
- Repository note: 论文把「一次执行算成功还是失败」的规则描述为环境反馈，没有给出明确阈值，而后验更新依赖这个判定。

## Related Works

- [Trace2Tower](./trace2tower.md) — 同样利用成功和失败证据从 trajectory 中归纳多层 skill，并按平滑后的成功可靠度给 skill 排序。
- [Agent Workflow Memory](./agent-workflow-memory.md) — 从 trajectory 中归纳可复用的子流程，用 LM evaluator 过滤在线经验，而不是为每个 procedure 维护后验。
- [SkillEvolBench](./skillevolbench.md) — 评测把 episodic trajectory 蒸馏成可复用程序性 skill 的能力。
