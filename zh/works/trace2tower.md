# Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents (2026)

> [English](../../works/trace2tower.md) | **简体中文**

> **首次公开：** 2026-09-04 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.05261)

## Overview

Trace2Tower 把 LLM agent 以往的 trajectory 整理成一个三层 skill library（action skill、procedure skill、strategy skill），并用每条 trajectory 的成功或失败标签来决定哪些行为模式能进入 library。早先的经验复用方法要么检索整条 trajectory，要么写出扁平的 skill 摘要。Trace2Tower 的做法不同：结果标签直接给用来抽取 skill 的 transition graph 加权；之后对 library 的修改，也只有在任务结果的配对比较没有否决它时才会被接受。论文的检验方式是把归纳出的 skill 交给一个固定的「Skill User」模型，在 ALFWorld 和 WebShop 上运行，再和无 skill、专家手写 skill 以及其他 skill 归纳 baseline 比较成功率、步数、无效 action 数和 context 大小。

## Topics

- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 这是 skill 归纳方法，评测用的是通用的具身家居任务（ALFWorld）和网购任务（WebShop），没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2609.05261>
- **Code:** <https://github.com/FudanSELab/Trace2Tower>
- **Venue:** arXiv preprint, September 2026

## Summary

Skill Author 模型（GPT-5.4）先把每条原始 trajectory 切成规范化的 event，再建一张图，图中的边就是观察到的 event 转移。每条边综合三项信息：语义兼容度、转移频率和结果证据，而且成功 trajectory 和失败 trajectory 分开计算；主要 benchmark 分数不低于 0.999 的 trajectory 算作成功。接着用一个 contrastive transform 保留有成功支持的边权，压低集中在失败里的边权。对得到的图做 spectral clustering，得到 procedure skill；在成功边支持的 procedure 上取最大路径，就成了 strategy skill。部署时，Skill User 在 token 预算内检索 skill，按平滑后的成功可靠度排序。所有证据都来自两个模拟环境（家居和网购），horizon 为 20 步。

## Tasks

N/A — 方法论文，没有提出新的任务集。实验使用现有 benchmark：

- **ALFWorld：** 六个任务族中全部 134 个可解的 `valid_unseen` 任务。Skill 从 310 个训练任务上的 1,240 条 No-Skill trajectory 中归纳（每个任务 4 次 rollout）。
- **WebShop：** 一份固定的 100 任务测试清单。Skill 从 100 个训练任务上的 400 条 trajectory 中归纳。

## Domains

通用的具身家居交互（ALFWorld）和网购（WebShop）；没有评估任何规范的科学或工程领域。

## Evaluation

Skill User（默认是 DeepSeek-V4-Flash，temperature 0，最多 512 个输出 token）把检索到的 skill 放进 context，在环境里行动，horizon 为 20 步。ALFWorld 的每个 episode 按环境给出的完成标志判分；同时记录步数、无效 action 数、输入 token 数和 skill context 的字符数。WebShop episode 报告精确成功（官方 reward 不低于 0.999）、reward 和无效 action 数。结果为三次运行的 mean ± SD。

报告的主要结果（Trace2Tower Full）：

- **ALFWorld：** 成功率 87.31 ± 0.75%，10.35 步，0.26 个无效 action，44,651 个输入 token，3,623 个 skill 字符。对比行：No-Skill 46.27%，Expert-Crafted 71.39%，Trace2Skill (+Combined) 61.44%，SkillX 78.61%，ExpeL 81.59%。只用 strategy skill 的 High-only 变体达到 84.83%，skill 字符数为 1,966。
- **WebShop：** 精确成功 50.67 ± 2.89%，reward 0.7115，0.27 个无效 action；SkillX 49.33%，ExpeL 48.00%，Expert-Crafted 48.00%，No-Skill 40.67%。
- 在 ALFWorld 上与 SkillX 相比，论文报告输入 token 少 30.5%，skill context 少 63.9%。

ALFWorld 上的 ablation（每项都是单次 134 任务评测）：去掉转移证据得到 70.15%，去掉结果证据得到 73.88%，去掉 contrastive transform 得到 73.88%。Verifier 引导的 refinement 在两个各含 120 个任务的 ALFWorld 留出集上，把汇总成功率从 80.42%（冻结的 tower）提高到 84.58%（TF-IDF Pareto 选择）或 83.75%（embedding 选择）；这里用了 10,000 次配对 bootstrap 重采样。跨模型迁移：Skill User 用 Flash 时，GPT-5.4 写出的 tower 达到 88.06%，Flash 自己写出的 tower 为 65.67%；Skill User 换成 DeepSeek-V4-Pro 时，两者分别为 85.82% 和 79.10%（p = 0.150，不显著）。

## Typical Duration

Episode 上限为 20 步；完整方法在 ALFWorld 上平均 10.35 步。Wall-clock 时间和归纳成本为 `TODO(reference)`。

## Main Contribution

提出一种从执行 trace 中归纳多层 skill 层级的方法：它考虑 event 之间的转移，并对比成功和失败的结果；另有一个 refinement 阶段，只在配对的任务结果支持某次修改时才去改动这个层级。

## Key Design Ideas

- 边的 affinity 取语义兼容度、转移概率和结果证据的几何平均，成功和失败 trajectory 分开计算，不使用学习出来的混合权重。
- Contrastive transform `Ā_uv = (A⁺_uv)² / (A⁺_uv + A⁻_uv)` 保留有成功支持的转移，压低容易导致失败的捷径，不需要调阈值。
- 用带 eigengap 规则的 spectral clustering 为每个连通分量决定 procedure skill 的个数。
- 三个 skill 层级：规范化 event（action）、spectral cluster（procedure）、有成功支持的 procedure 路径（strategy）。
- 四种 refinement 操作（Split、Merge、Promote、Downweight）先按语义相关度、结构相关度和反馈证据做 Pareto 非支配筛选，再经过配对结果的把关；被拒的更新会回滚。
- 检索在 token 预算内最大化 `Σ log(1 + ζ·ϱ)`，其中 `ϱ = (n⁺+1)/(n+2)` 是 skill 的平滑成功可靠度。

## Strengths

- Ablation 分别拆出了转移证据、结果证据和 contrastive transform 各自的贡献（论文，ALFWorld）。
- 在报告成功率的同时报告 context 成本（输入 token、skill 字符数），可以拿收益和 prompt 大小对照着看（论文）。
- 直接比较了不同 skill 层级：两个 benchmark 上都有 High-only 与 Full 的对比（论文）。

## Limitations

- 论文指出表示质量对 Skill Author 模型很敏感；Skill User 用 Flash 时，Flash 写出的 tower 比 GPT-5.4 写出的低 22.39 个点。
- 结构 ablation 都是单次评测，没有报告运行间方差（论文）。
- 论文没有说明配对 bootstrap 把关所用的指标、阈值或显著性水平，也没有定义 refinement 使用的共享任务清单。
- 从原始资料中无法确定所用 embedding 模型的具体标识（论文）。
- Repository note: 评测只覆盖两个模拟的通用 agent 环境，没有测试任何科学或工程任务。

## Related Works

- [SkillEvolBench](./skillevolbench.md) — 评测的正是这个方法所做的那一步：把 episodic trajectory 蒸馏成可复用的 skill。
- [SkillLearnBench](./skilllearnbench.md) — 给自动生成的 skill 打分，而这正是 Trace2Tower 产出的东西。
- [HiPER](./hiper.md) — 同样在 ALFWorld 和 WebShop 上把高层和低层 agent 决策分开，但靠的是 RL 训练，而不是从 trace 中抽取 skill。
