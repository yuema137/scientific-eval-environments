# SkillShapley (2026)

> [English](../../works/skillshapley.md) | **简体中文**

## Overview

SkillShapley 是面向 agent skill 的步骤级归因框架：把 skill 内部每一步的贡献建模为 Shapley 值，并用一套针对离散化 benchmark 奖励设计的边界自适应采样方案来估计这些值。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 归因方法学，任何科学或研究活动本身都不是受评对象。

## Links

- **Paper:** <https://arxiv.org/abs/2608.13173>
- **Venue:** arXiv preprint, 2026

## Summary

agent skill 是一套程序性说明，让语言 agent 得以完成文档处理、编码这类长任务；它们或由人工编写，或从执行轨迹中蒸馏而来——两种来源都几乎没有留下证据说明其中哪些步骤真正要紧。SkillShapley 把 skill 步骤归因表述为在步骤联盟上估计 Shapley 值贡献，再分两个阶段完成估计，依据是两条经验观察：benchmark 奖励是离散化的，因而会形成陡峭的性能悬崖；步骤之间的交互大体可加，而非协同。预热阶段先建起一个分层覆盖面广的缓存，并找出哪些层仍不确定；自适应阶段随后反复挑出信息量最大的那个尚未评估的配置去评估——信息量按它与缓存中已有配置之间能形成多少条高优先级的一位翻转边来打分。

## Tasks

N/A — 归因方法，而非任务套件。所用 skill 取自 SkillsBench，该 benchmark 把 agent skill 形式化为结构化的程序性知识，并在多样任务上提供经过整理、配有确定性 verifier 的 skill。实验共分析三个 skill：`offer-letter-generator`、`manufacturing-fjsp-optimization` 与 `dialogue-parser`。

## Domains

无规范科学或工程领域。受测 skill 覆盖文档生成、柔性作业车间调度优化与对话图解析——都是通用的 agent 流程，而非某个科学或工程领域内的任务；而受评对象是归因估计器本身，不是这些 skill 的主题内容。

## Evaluation

- **相对精确 Shapley 值的平均绝对误差** — 在固定评估预算下，估计器复原真值归因的接近程度。
- **删除验证曲线** — 按估计器给出的排序依次删除步骤，检验 skill 性能是否如预测那样下降。
- 基线包括：individual scores、Leave-One-Out、随机删除、LeastCore、Monte Carlo Shapley、quasi-Monte Carlo Shapley、paired Monte Carlo Shapley 与 size-*k*-truncated Shapley。
- **报告。** 在 99 个不重复配置的预算下，边界自适应的第一阶段产出 206 条可复用的一位翻转边际边，而 Monte Carlo 置换采样只得到 130 个置换边际观测，其中仅 115 个不重复。其余关键数值为 TODO(reference)。

## Typical Duration

N/A — 对已完成的 skill 执行做事后估值；成本以所评估的不重复 skill 配置数为预算来报告，而非墙钟时间或 token 开销。

## Main Contribution

把 Shapley 值形式的 credit 分配下沉到 agent skill 的单个*步骤*，并让采样策略去适配 agentic benchmark 实际呈现的结构——悬崖状的离散奖励与近乎可加的步骤交互——而不是假定一个平滑、强交互的价值函数。

## Key Design Ideas

- 把 skill 步骤归因表述为步骤子集上的联盟价值估计，于是一个步骤的价值由它在众多上下文中的边际效应定义，而非由一次消融决定。
- 论文以两条经验前提——离散奖励造成陡峭悬崖、步骤交互大体可加——论证采样预算应集中在信息量大的边界附近，而不是均匀地采置换。
- 采样会复用已评估的配置：每个新配置都按它与缓存之间能形成多少条高优先级的一位翻转边来挑选，于是一次昂贵的 rollout 能贡献好几个边际观测。
- 验证从两面进行：在能算出精确 Shapley 值的地方比对一致性，算不出的地方则做行为层面的删除测试。

## Strengths

- 归因做到步骤粒度，比 skill 级或单元级估值更细，对 skill 的撰写与剪枝可直接落地。
- 采样效率是对照精确 Shapley 值测出来的，估计器的近似质量因此是一个报告出来的量，而不是一个假设。
- 对比集既含经典的数据估值方法，也含 Shapley 的方差缩减变体，而不只是朴素的留一法。

## Limitations

- 实验只覆盖三个 skill；论文并未确立可加交互这一前提在更广的 skill 家族上同样成立。
- 可加性与悬崖假设只是启发性的经验观察，而非保证，因此自适应采样器的优势未必迁移得到奖励稠密或强协同的 benchmark 上。
- 论文未说明会发布代码。
- Repository note: 卡片依据 arXiv v1 全文编写（2026 年 8 月）；撰写时未找到同行评议版本。
- Repository note: 归因是相对宿主 benchmark 的 verifier 测出来的，因此某一步被判为低价值，是*对那个 verifier 而言*低价值，未必对底层任务也如此。

## Related Works

- [SkillSV](./skillsv.md) — 最接近的姊妹工作：同样对 skill 内部做 Shapley 估值，但作用于编译后的单元、依赖与层级，而非单个步骤。
- [Skill-Use](./skill-use.md) — 同样把 skill 当作一等评估对象，但为 agent 对 skill 的使用打分，而非为 skill 各部分的价值打分。
- [QVal](./qval.md) — 同样把步骤级 credit 信号本身而非 agent 当作受评对象。
- [BACKROOMBench](./backroombench.md) — 同样以反事实干预确立 skill 的影响，但作用在整个 skill 的层面，而非其内部步骤。
- [GATE](./gate.md) — 同样分析结构化的 skill/工具工件，采用基于图的工具演化而非 credit 估值。
