# Skill Learning & Evolution

> [English](../../topics/skill_learning_evolution.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Agent 看过 solution 以后做对一次，不代表它学会了 reusable skill。它可能只是把原 trajectory 重放了一遍。真正的 test 是：拿走原 trace，再改 context、task wording 或 skill composition，剩下的东西还能不能用。

一条 evaluation loop 可以先让 agent 解 example，再写成 skill file，把文件冻结，最后放到 held-out task 上。然后比较 frozen skill、raw-trajectory reuse 和 no-memory baseline。如果换任务还能迁移，artifact 才可能抓住了 reusable procedure；如果只会做 near-duplicate，它只是压缩了经验，没有学到通用方法。

## Definition

这个 topic 研究 agent 能否把经验、trajectory、示范或 evaluator feedback 变成可复用的程序性 skill，并检验任务、上下文或组合方式改变后，这些 skill 是否仍然有效。

## Motivation

Agent 在 acquisition 阶段完成任务，不表示它学到了可复用 skill。评估需要区分 episodic replay 与真正抽象、skill 写作与 skill 检索、原题复做与冻结后的迁移。这和 Skill Hierarchy 不同：后者把能力拆开测量，这里研究 skill 如何学到、如何修改。

## Existing Approaches

- **冻结后部署。** [SkillEvolBench](../works/skillevolbench.md) 将生成的 skill 与原始 trajectory、人工 seed 对照，并测试 context shift、adversarial shortcut 和 composition。
- **分别评价 artifact、trajectory 与 outcome。** [SkillLearnBench](../works/skilllearnbench.md) 不只看任务成功，也直接检查生成 skill 的质量。
- **从评估得到过程监督。** [SkillCoach](../works/skillcoach.md) 根据真实 rollout 演化 skill-use rubric，再用它筛选训练 trajectory。
- **生命周期安全。** [SkillMisevo-Bench](../works/skillmisevo-bench.md) 分开测量不安全 skill 的写入、检索、执行和跨 session 保留。
- **可复用能力结构。** [GATE](../works/gate.md) 演化的是分层 tool graph，而不是文字 skill 文件。

## Comparison

| Work | 学到的 artifact | Feedback | 迁移测试 | 关键区分 |
|---|---|---|---|---|
| SkillEvolBench | 文字 skill library | Verifier feedback | Context shift、adversarial、composition | Skill 与原始 trajectory 复用 |
| SkillLearnBench | 自动生成的 skill | 无、自我、教师、creator pipeline | 留出的 skill-dependent tasks | Artifact、trajectory、outcome |
| SkillCoach | 持续修订的 skill-use rubric | Rollout 证据与 validation gate | 留出的任务族 | 过程质量与结果 |
| SkillMisevo-Bench | 可能不安全的演化 skill | 在线 evolution 更新 | 新 session persistence | 写入、检索与伤害 |
| GATE | 分层 tool graph | 执行经验 | 使用演化 graph 的新任务 | 结构化能力 artifact |

## Open Questions

- 什么证据能证明 agent 做了抽象，而不是重放记住的 trajectory？
- Skill 本身、检索和执行应如何分开打分？
- Evaluator feedback 何时会引起递归漂移、过拟合或不安全泛化？
- 怎样用冻结部署测长期迁移，又不阻断合理的在线适应？
- 哪种 skill 表示便于跨 harness 组合、检查和维护？

## Related Works

- [Beyond 'Aha!'](../works/beyond-aha.md)
- [SkillEvolBench](../works/skillevolbench.md)
- [SkillLearnBench](../works/skilllearnbench.md)
- [SkillCoach](../works/skillcoach.md)
- [SkillMisevo-Bench](../works/skillmisevo-bench.md)
- [GATE](../works/gate.md)
