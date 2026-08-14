# SkillCoach (2026)

> [English](../../works/skillcoach.md) | **简体中文**

## Overview

SkillCoach 是面向 agent skill 使用的过程级评估框架，其 rubric 会自我演化：rubric 从真实 rollout 中归纳而来，沿四个维度为轨迹打分——skill 选择、skill 遵循、skill 组合，以及基于 skill 的反思——同时把外部 verifier 保留为独立的结果信号。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型 agent skill 评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2607.01874>
- **Venue:** arXiv preprint, 2026

## Summary

出发点的观察是：真实的 skill 仓库里 skill 彼此重叠，可靠地使用 skill 因而很难，而最终 verifier 的成败又是过于粗糙的信号——agent 完全可能靠反复试错通过，同时选中干扰 skill、跳过必需步骤、把工作流组合错，或者省掉最后的检查。SkillCoach 先由任务指令、gold skill 与 oracle 解构造出初始 rubric，再在验证门控下对照真实 rollout 演化这套 rubric。由于过程质量与结果 verifier 分开计分，侥幸完成任务与流程正确得以区分开来；演化后的 rubric 还会复用为过程监督信号，用来筛选训练轨迹。

## Tasks

实验任务取自既有的 skill benchmark（SkillsBench 与 SkillLearnBench），按 skill 依赖度阈值筛出依赖 skill 的那些任务：18 个训练任务族与 10 个留出测试任务族，共 28 族。每族的实例数量为 TODO(reference)。

## Domains

含重叠 skill 与干扰 skill 的通用 agent skill 仓库；不针对任何规范科学或工程领域。

## Evaluation

- **skill 选择** — 轨迹实际读取的 skill 集合与 gold skill 集合之间的集合级 F1，既惩罚漏掉必需 skill，也惩罚选中干扰项。
- **skill 遵循** — 对关键步骤的加权求和，某一步只有在轨迹中能找到可见证据支持其完成时才计分。
- **skill 组合** — 对照前置依赖关系打分，这些依赖规定了哪一步或哪个 skill 必须先于另一个完成。
- **基于 skill 的反思** — 是否执行了预期的检查，例如校验输出文件、schema、格式或任务特定约束。
- rubric 的演化受验证门控：由一个独立的仲裁模型提出局部补丁，只有当补丁不降低覆盖率、把质量提升到阈值以上，并且至少改动一个已匹配条目时才被接受。仲裁模型不能查看验证 rollout、不能自行通过补丁、不能绕过 verifier，也不能删除关键步骤。
- **报告。** rubric 演化把 gold 关键点覆盖率从 71.56 提到 83.70，把幻觉率从 2.00 压到 0.00，把筛选一致性从 82.00 提到 96.00。用演化后的 rubric 筛选 SFT 轨迹，Qwen3.5-9B 的最终准确率从 14.0% 提升到 32.0%，而只按结果筛选为 18.0%。

## Typical Duration

N/A — 未报告任何逐任务的步数、时间或 token 预算。

## Main Contribution

让 skill 使用中的过程质量可以脱离结果成败单独测量：rubric 不靠人工编写，而是在验证门控下从 rollout 中归纳出来；并且证明由此得到的过程信号，作为训练数据的筛选器强于终局准确率。

## Key Design Ideas

- rubric 来自真实 rollout，而非一次性写死，因此能跟上实际发生的失败模式。
- 外部 verifier 被刻意排除在 rubric 之外，过程分与结果分因此可以彼此不一致。
- 四个维度是照着 skill 使用的几种不同失败模式选的，而不是一把通用的质量尺子。
- 从轨迹中抽取证据（skill 读取、gold 与干扰信号、工具调用、文件编辑、脚本执行），让每一条 rubric 判断都落在可观察的东西上。
- 对 rubric 演化设了结构性约束——仲裁者既看不到验证 rollout，也不能自行通过补丁——以免 rubric 朝着当前 agent 的实际行为漂移。

## Strengths

- rubric 这一产物本身经过验证（覆盖率、幻觉、筛选一致性），而不是默认它有用。
- 对干扰项规模的分析直接触及真实仓库的条件；报告显示高相似度干扰项会把 GPT-5.5 的选择 F1 从 0.84 拉低到 0.59。
- 展示了评估信号的下游用途，把从测量到轨迹筛选的回路闭合起来。

## Limitations

- 实验覆盖的是从既有 skill benchmark 中挑出的一批依赖 skill 的任务；作者也指出其规模仍小于生产环境中的 skill 仓库。
- 训练部分只做了离线监督微调，未报告 on-policy 强化学习或长期部署反馈。
- 论文未给出代码或项目地址。
- Repository note: 论文后半是训练方面的贡献，超出本仓库范围；卡片只覆盖评估框架及对 rubric 的验证。
- Repository note: 卡片依据 arXiv 摘要与 v1 全文编写（2026 年 8 月）；每族实例数与完整结果表有待直接校验。

## Related Works

- [SkillTV-Bench](./skilltv-bench.md) — 同样评估对 skill 增强轨迹的评判，把评判者的 skill 知识当作受测对象。
- [Skill-Use](./skill-use.md) — 同样把 skill 使用拆成若干侧面（触发、遵从、边界），但在固定套件上为 agent 打分，而非演化 rubric。
- [AgentProcessBench](./agentprocessbench.md) — 同样面向 agent 轨迹的过程级判断而非结果级判断。
- [SkillEvolBench](./skillevolbench.md) — 同样从 rollout 中提炼可复用的产物，只不过产物是 skill 库而非 rubric。
- [SkillAudit](./skillaudit.md) — 同样围绕 skill 自动构造评估材料，粒度是每个 skill 包而非每次 rollout。
