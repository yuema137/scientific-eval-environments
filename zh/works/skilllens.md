# SkillLens (2026)

> [English](../../works/skilllens.md) | **简体中文**

> **首次公开：** 2026-05-08 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2605.08386)

## Overview

SkillLens 是一种 skill 复用方法：它把 agent 的 skill 表示成四种粒度（policy、strategy、procedure、primitive），面对新任务时逐个单元决定该复用哪一层、拆开哪一层、改写哪一层。扁平的 skill library 只能二选一：要么注入整个 skill，可能带进无关的 context；要么整个改写，要多花 token。SkillLens 让一个 LLM verifier 遍历 skill 图，接受兼容的子 skill，只改写不匹配的单元；它还会定期根据失败报告修改 verifier 的路由规则，修改按「正确性减成本」的目标打分。评测在 MuLocbench 和 ALFWorld 上，把它的准确率和 token/时间成本与「全部改写」和「只改父节点」两种调整方式对比。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)

## Activities

N/A — 这是 skill 复用方法，评测对象是通用的仓库 bug 定位和文本具身任务，没有评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2605.08386>
- **Venue:** arXiv preprint (cs.AI), 2026

## Summary

对一个新 query，SkillLens 先按 embedding 相似度检索 skill 种子，再用 degree-corrected random walk with restart 向外扩展，把候选分成完全兼容、部分相关和不匹配三档。对每个部分相关的单元，verifier（GPT-5-mini）给出一个动作：accept（保留这个单元并停止）、decompose（把它的子节点放进待评估队列）、rewrite（让 writer 在局部改写这个单元）或 skip。演化阶段，每个正确性 M < 1 的任务都会生成一份差距报告（错误类型、检索到的 skill、遍历路径、路由动作、被改写的单元）；writer 据此对 verifier 的文本 registry 提出单条修改，最后提交 J(𝒮) = E[M − C]（正确性减去归一化成本）最大的那个候选。论文的成本保证建立在一个假设上：skill 与任务之间的不匹配是稀疏的。

## Tasks

N/A — SkillLens 是 skill 复用方法，不是 benchmark。评测使用：

- **MuLocbench** — 仓库级 bug 定位，分文件、模块和函数三种粒度；36 个训练仓库和 10 个测试仓库（issue 数 TODO(reference)）。
- **ALFWorld** — 文本具身任务，每个 episode 最多 50 步；训练划分用于演化和验证，valid-seen 划分用于测试（划分大小 TODO(reference)）。

Skill library 用 antigravity-awesome-skills 初始化。Agent 和 writer：Codex GPT-5.2；verifier：GPT-5-mini；检索 embedding：text-embedding-3-small。

## Domains

软件工程（仓库 bug 定位）和文本形式的具身家居任务。

## Evaluation

- **循环内部。** 演化任务用 benchmark 指标 M ∈ [0, 1] 打分；失败会生成差距报告，registry 的修改按 J = E[M − C] 选择。附录 A.4 描述的是 7:3 的演化/验证划分，用验证效果最好的版本做一次最终测试；Algorithm 2 则是在演化集上按 J 选择。
- **MuLocbench。** 在文件、模块和函数三个级别上报告 @1/@3/@5/@10 的 Accuracy、Recall 和 Precision。与无 skill 的 Vanilla agent 相比，报告的 Acc@1：文件 61.13 对 58.87，模块 59.26 对 55.56，函数 43.68 对 37.37（+6.31 pp）。只改父节点的变体在文件级（61.51）和函数级（45.79）得分更高。
- **ALFWorld。** Episode 成功率：SkillLens 51.31，Vanilla 45.00，AutoSkill 47.14，EvoSkill 47.14。
- **成本对比（MuLocbench）。** 全部改写：6,161.83 s，115.51M token；只改父节点：5,257.82 s，78.35M token；SkillLens：4,718.54 s，16.41M token。
- **Library 规模扩展。** 初始 skill 比例从 25% 增加到 100% 时，检索时间从 18.28 分钟增加到 58.72 分钟，主 agent 的 token 从 3.17M 增加到 3.89M。

## Typical Duration

ALFWorld episode 上限 50 步。在 MuLocbench 上，报告的成本对比中完整 SkillLens 运行用时 4,718.54 s，消耗 16.41M token。

## Main Contribution

作者提出把 skill 组织成四层图，并在一个逐单元路由的 verifier 控制下按混合粒度调整 skill；同时给出理论论证：在不匹配稀疏的条件下，混合粒度调整的成本是次线性的，演化式的 registry 更新会单调改善验证目标，直到局部最优。

## Key Design Ideas

- 四层 skill 层级：policy、strategy、procedure、primitive。
- 检索分档依据校准过的 degree-corrected random walk 分数，只有部分相关的 skill 才需要 verifier 花成本去遍历。
- 每个单元有四种路由动作（accept、decompose、rewrite、skip），而不是对整个 skill 做一次决定。
- 被演化的对象是一个文本形式的 verifier registry，用单条操作（Add、Del、Upd、Mrg）修改，并保留退回当前版本的选项。
- 目标函数从正确性中减去归一化成本，演化因此在准确率和调整成本之间权衡。

## Strengths

- 在准确率和 token/时间成本两方面比较了三种调整粒度（全部改写、只改父节点、混合）。
- 在三种定位粒度上报告准确率，能看出方法在哪里领先、在哪里不领先。
- 在给出命题的同时说明了理论假设。

## Limitations

- 只有两类任务，且都以英文为主；多模态、多语言和安全关键场景没有测试。
- 结果依赖初始 skill library 和 verifier 的路由；含噪声的 skill 可能引发不必要的拆分或改写，四层本体也未必适合所有领域。
- 只用了一个 agent/writer 模型系列、一个 verifier 和一个 embedder。
- 相比无 skill 的 agent，verifier 调用和 registry 维护带来额外开销；没有研究 library 长期增长的情况。
- 没有说明 verifier 的决策标准和 prompt，也没有说明 J 中成本相对正确性的权重。
- Repository note: 结果都是单次运行，没有方差或显著性检验；附录和 Algorithm 2 对基于验证的选择描述不一致。本卡片依据 arXiv 摘要和 v2 HTML 全文编写（2026 年 11 月）。

## Related Works

- [Break It Down, Pass It On](./break-it-down-pass-it-on.md) — 同样表明 skill 按什么粒度复用，会改变它是否有帮助。
- [SkillSV](./skillsv.md) — 同样处理 skill 内部的单元，但给它们估值，而不是路由。
- [SkillShapley](./skillshapley.md) — 把 credit 分配到 skill 内部的步骤，从更细的粒度看 skill 的哪些部分起作用。
- [GATE](./gate.md) — 同样在可复用的 agent 能力上构建层级结构，不过是工具图，而不是 skill 图。
