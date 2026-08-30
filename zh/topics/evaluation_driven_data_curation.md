# Evaluation-Driven Data Curation

> [English](../../topics/evaluation_driven_data_curation.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

这个 topic 收录的是：系统根据 downstream evaluation feedback，明确修改数据选择、生成、过滤、加权、curriculum 或 mixture policy。

## Motivation

训练论文通常都会报告评估结果，但这不表示 evaluation 进入了开发 loop。这里的必要结构是：数据策略产生训练数据，训练出的模型接受评估，评估信号再改变下一版数据策略。这样可以避免把整个 data-centric ML 都吸进来。

## Existing Approaches

- **闭环数据策略研究。** [Curation-Bench](../works/curation-bench.md) 固定模型、训练 recipe 和 eval suite，让 agent 反复修改可执行的数据选择策略。
- **按过程分数筛 trajectory。** [SkillCoach](../works/skillcoach.md) 用经过验证的 skill-use rubric 筛选 SFT trajectory；论文中它优于只看终局结果的过滤方式。
- **更宽的 post-training search。** [PostTrainBench](../works/posttrainbench.md) 允许 agent 把数据修改作为完整训练策略的一部分，并审计 contamination。

## Comparison

| Work | 数据干预 | Evaluation signal | 迭代方式 | 固定项 |
|---|---|---|---|---|
| Curation-Bench | 可执行选择策略与选中子集 | Downstream VLM benchmark suite | 最多 10 轮 | 模型与 recipe |
| SkillCoach | 为 SFT 筛选 agent trajectory | 经验证的过程 rubric 与 task verifier | 离线筛选并重训 | 相同任务族和 base model |
| PostTrainBench | 数据获取、生成、过滤和格式化 | 目标 benchmark 分数 | 10 小时内开放迭代 | Base model、evaluator、GPU budget |

## Open Questions

- Loop 怎样区分真正泛化与反复查询 evaluator 后的过拟合？
- 比较噪声很大的数据策略需要多少 evaluation budget？
- 过程质量、下游准确率、多样性、成本和安全应怎样权衡？
- 学到的数据策略能否迁移到其他模型、模态和领域？
- 什么样的审计记录足以发现直接和间接 contamination？

## Related Works

- [Curation-Bench](../works/curation-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [PostTrainBench](../works/posttrainbench.md)
