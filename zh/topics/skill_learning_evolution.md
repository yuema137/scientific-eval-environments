# Skill Learning & Evolution

> [English](../../topics/skill_learning_evolution.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Agent 看过 solution 以后做对一次，不代表它学会了 reusable skill。它可能只是把原 trajectory 重放了一遍。真正的 test 是：拿走原 trace，再改 context、task wording 或 skill composition，剩下的东西还能不能用。

一条 evaluation loop 可以先让 agent 解 example，再写成 skill file，把文件冻结，最后放到 held-out task 上。然后比较 frozen skill、raw-trajectory reuse 和 no-memory baseline。如果换任务还能迁移，artifact 才可能抓住了 reusable procedure；如果只会做 near-duplicate，它只是压缩了经验，没有学到通用方法。

## 定义

Skill learning 问 agent 能不能把经验变成可复用流程。经验可以来自 trajectory、demonstration 或 evaluator feedback，结果可以是 skill file、policy、memory item 或其他 artifact。Evolution 再问 agent 失败后能不能修改这份 artifact。最后要用新 task、新 context 或新组合来测它还能不能用。

## 为什么重要

在 acquisition example 上成功，只能证明 agent 做对了这道题。它可能只是把原 trajectory 重放了一遍，并没有学到方法。更有用的 evaluation 会冻结 skill，拿掉原 trace，再放到 held-out condition 上测 transfer。这和 Skill Hierarchy 不同，后者拆解已有能力，不研究 skill 怎样学到、修改和复用。

## 现有方法

- **冻结后部署。** [SkillEvolBench](../works/skillevolbench.md) 将生成的 skill 与原始 trajectory、人工 seed 对照，并测试 context shift、adversarial shortcut 和 composition。
- **分别评价 artifact、trajectory 与 outcome。** [SkillLearnBench](../works/skilllearnbench.md) 不只看任务成功，也直接检查生成 skill 的质量。
- **从评估得到过程监督。** [SkillCoach](../works/skillcoach.md) 根据真实 rollout 演化 skill-use rubric，再用它筛选训练 trajectory。
- **生命周期安全。** [SkillMisevo-Bench](../works/skillmisevo-bench.md) 分开测量不安全 skill 的写入、检索、执行和跨 session 保留。
- **可复用能力结构。** [GATE](../works/gate.md) 演化的是分层 tool graph，而不是文字 skill 文件。

[EvoHarnessBench](../works/evoharnessbench.md)在外围能力集合变化后继续测试已学到的产物。分别计算旧能力保留和新任务适应，可以避免新题进步掩盖旧题退步。

有三项具身工作测试 agent 能不能从先前的尝试中学习，任务在仿真的家务和机器人操作场景里。[EmbodiedCLBench](../works/embodiedclbench.md)在一个没见过的进阶任务上比较三种情况：没有经验、保留两个基础任务的完整轨迹、保留这些轨迹的书面技能摘要。任一种经验都能把成功率从 3–12% 提到 16–52%，但学习样本超过一个之后，再多也没有稳定的额外提升。[PhysRSI-eval](../works/physrsi-eval.md)给 agent 一个持久工作区，里面有代码、工具、技能和笔记，每个任务最多做 17 次带评分的机器人尝试。在 GPT-6 Astra 六个任务的消融实验中，去掉历史后，后期轮次的成功次数从 15/36 降到 3/36；冻结的工作区放到没见过的布局上，60 次尝试仍有 25 次成功。[RobotAgentBench](../works/robotagentbench.md)让一个 coding agent 在十轮迭代中保留并改进自己的控制工具，它在家务任务上的平均分从 31.0 升到 42.3。

有一组方法论文改的是候选 skill 或 memory 条目入库前的那一步。早期的 induction 流程总结完一条 trajectory 就直接存下，不做测试。这些方法在写出来和存进去之间加了一道 evaluation，彼此的区别在于这道 evaluation 具体跑什么。

- **带与不带 skill 的成对测试。** [SkillGen](../works/skillgen.md) 在一个验证子集上分别带着和不带候选 skill 重跑，分开统计修好的题和退步的题，只有两者之差超过阈值才部署这个 skill。这一步筛选很关键：第 8 轮最新的候选在 held-out split 上平均 −3.1 pp，经过验证的最佳候选是 +8.1 pp。[Trace2Tower](../works/trace2tower.md) 对已有 skill library 的修改也用了类似的成对结果门槛，被拒的修改会回滚。
- **在来源任务上重跑。** [SKILL-KD](../works/skill-kd.md) 对比弱 student 的失败和强 teacher 的运行，据此写一个 patch，只有 student 随后在这道题上成功才提交。这道门槛只能说明 patch 修好了一道题，不能说明它能泛化。
- **由第二个 agent 重建。** [MIND-Skill](../works/mind-skill.md) 让另一个 agent 在看不到原始 trajectory 的情况下，只凭 skill 重新解这道题。然后根据环境结果、LLM judge 给出的 trajectory 匹配度和一份文档 rubric，去修改负责写 skill 的 prompt。
- **给每个存储条目记结果统计。** [MACLA](../works/macla.md) 为每个 procedure 的成功率维护一个 Beta posterior，按 expected utility 选择；只有当一个 procedure 至少攒到三次成功和三次失败可以对比时，才去改写它。[Agent Workflow Memory](../works/agent-workflow-memory.md) 在 online 模式下只从 LM evaluator 判为成功的 trajectory 里收 workflow，所以 evaluator 判错的内容也可能进入 memory。[STAIR](../works/stair.md) 不按结果筛选单个节点；它存下抽象后的修复 trajectory，检索出的节点再交给一个 LLM verifier 过滤。
- **演化的是复用 policy，不是 skill 本身。** [SkillLens](../works/skilllens.md) 不改 skill 内容，而是根据失败报告修改 verifier 的路由规则；只有当修改提高了「correctness 减去归一化成本」时才保留。

另有两项研究检验了这些收益背后的假设。[Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) 发现，按整个任务写出的 skill 会让 success 掉到不带 memory 的 baseline 以下；它还提出一个 utility score，在跑任何任务之前就能用 embedding 算出来。[LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md) 把插入的经验清空、打乱或替换，发现扰动压缩后的经验时，分数常常不变。所以，加了 memory 之后 success 上升，本身并不能说明 agent 用上了存下的 skill；要确认这一点，需要对 memory 内容做干预。

## 方法对比

| Work | 学到的 artifact | Feedback | 迁移测试 | 关键区分 |
|---|---|---|---|---|
| SkillEvolBench | 文字 skill library | Verifier feedback | Context shift、adversarial、composition | Skill 与原始 trajectory 复用 |
| SkillLearnBench | 自动生成的 skill | 无、自我、教师、creator pipeline | 留出的 skill-dependent tasks | Artifact、trajectory、outcome |
| SkillCoach | 持续修订的 skill-use rubric | Rollout 证据与 validation gate | 留出的任务族 | 过程质量与结果 |
| SkillMisevo-Bench | 可能不安全的演化 skill | 在线 evolution 更新 | 新 session persistence | 写入、检索与伤害 |
| GATE | 分层 tool graph | 执行经验 | 使用演化 graph 的新任务 | 结构化能力 artifact |
| [EvoHarnessBench](../works/evoharnessbench.md) | 持久保存的技能、提示词或代码 | 适应集任务的执行经验 | 在扩大的 harness 下测试新旧任务 | 新任务收益与旧能力保留分开计算 |
| [EmbodiedCLBench](../works/embodiedclbench.md) | 上下文内的完整轨迹，或一份书面 Markdown 技能摘要 | 在两个相关基础任务上的交互经验 | 组合 2–4 个基础任务类别的未见进阶任务 | 轨迹、技能摘要与无经验三者对比 |
| [PhysRSI-eval](../works/physrsi-eval.md) | 由策略代码、工具、技能和笔记组成的持久工作区 | 每次物理尝试后的原生评分、成功标记和失败原因 | 冻结工作区放到未见布局；三个跨任务案例 | 首次尝试与失败后的改进分开 |
| [RobotAgentBench](../works/robotagentbench.md) | coding agent 创建并改进的可复用机器人控制工具 | 十轮迭代中的执行反馈 | 除同一批任务和场景外没有报告 | 纯代码 agent 有无自我改进的对比 |
| [Trace2Tower](../works/trace2tower.md) | 三级 skill library（action、procedure、strategy） | 用成功/失败标签给 transition graph 加权；对 library 修改设成对结果门槛 | Held-out 的 ALFWorld 和 WebShop 任务；跨模型的 author/user 迁移 | 按结果对比的 skill 归纳 vs. 扁平归纳；各组件 ablation |
| [STAIR](../works/stair.md) | 从过去修复中得到的多层 plan tree | 不按节点筛选；由 LLM verifier 过滤检索出的节点 | 同一仓库里之后的 SWE-bench Verified issue；迁移到 mini-SWE-agent v2 | 原始 trajectory vs. 单一抽象层级 vs. 混合层级 |
| [MACLA](../works/macla.md) | 供 frozen LLM 使用的 procedure 和 meta-procedure | 环境结果更新每个 procedure 的 Beta posterior | 四个 benchmark 的 test split | Bayesian 选择、对比式改写和 meta-procedure 分别 ablation |
| [Agent Workflow Memory](../works/agent-workflow-memory.md) | 带占位值的可复用 workflow | 标注样例（offline）；LM evaluator 对自身测试 trajectory 给出的成功标签（online） | Mind2Web 的跨任务、跨网站和跨领域 split | Offline vs. online 归纳；文本 vs. 代码 workflow |
| [MIND-Skill](../works/mind-skill.md) | 通过优化后的 induction prompt 写出的 skill 文档 | 重建匹配度（LLM judge）、环境结果、文档 rubric（LLM judge） | Held-out 的 AppWorld 和 BFCL-v3 任务 | 三项 loss 分别 ablation |
| [SkillGen](../works/skillgen.md) | 每个 base agent 一条自然语言 skill | 带与不带 skill 成对重跑，统计修好和退步的题 | 11 个 benchmark 的 held-out split；跨模型复用 | 验证后的最佳候选 vs. 最新候选 vs. 不用 skill |
| [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) | 任务级或子任务级 skill，文本或代码形式 | 只有有序任务流中的任务完成情况 | 同一任务流中后面的任务 | 粒度和格式 vs. 不带 memory 的 baseline |
| [SkillLens](../works/skilllens.md) | 文本形式的 verifier 规则表，负责路由四层 skill graph | Benchmark 分数减去归一化成本；失败任务的缺口报告 | MuLocbench 和 ALFWorld 上 7:3 的演化/验证 split | 混合粒度适配 vs. 全部改写和只用父节点 |
| [SKILL-KD](../works/skill-kd.md) | 给 frozen student agent 用的 patch 型 skill 文件 | 每次对照 teacher 写出 patch 后，student 重跑是否成功 | 五个 benchmark 的 held-out split，两种 student–teacher 设置 | 仅 student、仅 teacher、批量和成对获取；有无合并步骤 |
| [LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md) | N/A — 诊断四个现有框架中的原始经验和压缩经验 | 对插入经验做受控干预 | 每种干预下的同一批环境 | 原始 vs. 压缩经验；内容 vs. prompt 结构的对照 |

## 还没解决的问题

- 什么证据能证明 agent 做了抽象，而不是重放记住的 trajectory？
- Skill 本身、检索和执行应如何分开打分？
- Evaluator feedback 何时会引起递归漂移、过拟合或不安全泛化？
- 怎样用冻结部署测长期迁移，又不阻断合理的在线适应？
- 哪种 skill 表示便于跨 harness 组合、检查和维护？

## 相关工作

- [RobotAgentBench](../works/robotagentbench.md)
- [PhysRSI-eval](../works/physrsi-eval.md)
- [EmbodiedCLBench](../works/embodiedclbench.md)
- [Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents](../works/trace2tower.md)
- [EvoHarnessBench](../works/evoharnessbench.md)
- [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](../works/stair.md)
- [SKILL-KD](../works/skill-kd.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [MIND-Skill](../works/mind-skill.md)
- [SkillGen](../works/skillgen.md)
- [SkillLens](../works/skilllens.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [LLM Agents Are Not Always Faithful Self-Evolvers](../works/faithful-self-evolvers.md)
- [MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](../works/macla.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [GATE](../works/gate.md)
- [Agent Workflow Memory](../works/agent-workflow-memory.md)
