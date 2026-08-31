# Evaluation-Driven Data Curation

> [English](../../topics/evaluation_driven_data_curation.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

大多数 training paper 先把 data 选好，训练结束以后才做 evaluation。这条流程里，score 只能描述成品 model，不能决定下一轮该换什么 data。

这里把 loop 闭上了。Curation policy 先选 10,000 条样本，固定 recipe 训练一个 model，held-out evaluation 暴露薄弱行为，下一轮 policy 再改 mixture 或 filter。Evaluation 因此成了 data selection 的控制信号。只试几个 dataset、最后报告最高分，还不能自动算进这个 topic；feedback 必须真的改变后续 curation。

## 定义

Evaluation-driven data curation 用下游评估结果决定下一轮训练数据。系统可以选择、生成、过滤、加权、调整顺序或重新混合样本。真正的分界线在于：evaluation 的结果有没有改变下一次数据决策。

## 为什么重要

几乎所有 training paper 都会报一个最终分数，但这还没有形成闭环。在这里，data policy 先组出训练集，固定的 recipe 训出 model，held-out evaluation 暴露薄弱点，policy 再据此改变下一轮选哪些数据。只有保留这条 feedback path，才不会把普通 dataset 对比和整个 data-centric ML 都收进来。

## 现有方法

- **闭环数据策略研究。** [Curation-Bench](../works/curation-bench.md) 固定模型、训练 recipe 和 eval suite，让 agent 反复修改可执行的数据选择策略。
- **按过程分数筛 trajectory。** [SkillCoach](../works/skillcoach.md) 用经过验证的 skill-use rubric 筛选 SFT trajectory；论文中它优于只看终局结果的过滤方式。
- **更宽的 post-training search。** [PostTrainBench](../works/posttrainbench.md) 允许 agent 把数据修改作为完整训练策略的一部分，并审计 contamination。

## 方法对比

| Work | 数据干预 | Evaluation signal | 迭代方式 | 固定项 |
|---|---|---|---|---|
| Curation-Bench | 可执行选择策略与选中子集 | Downstream VLM benchmark suite | 最多 10 轮 | 模型与 recipe |
| SkillCoach | 为 SFT 筛选 agent trajectory | 经验证的过程 rubric 与 task verifier | 离线筛选并重训 | 相同任务族和 base model |
| PostTrainBench | 数据获取、生成、过滤和格式化 | 目标 benchmark 分数 | 10 小时内开放迭代 | Base model、evaluator、GPU budget |

## 还没解决的问题

- Loop 怎样区分真正泛化与反复查询 evaluator 后的过拟合？
- 比较噪声很大的数据策略需要多少 evaluation budget？
- 过程质量、下游准确率、多样性、成本和安全应怎样权衡？
- 学到的数据策略能否迁移到其他模型、模态和领域？
- 什么样的审计记录足以发现直接和间接 contamination？

## 相关工作

- [SkillCoach](../works/skillcoach.md)
- [Curation-Bench](../works/curation-bench.md)
- [PostTrainBench](../works/posttrainbench.md)
