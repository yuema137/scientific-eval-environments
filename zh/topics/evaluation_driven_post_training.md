# Evaluation-Driven Post-Training

> [English](../../topics/evaluation_driven_post_training.md) | **简体中文** · [← 全部 topics](./README.md)

## Definition

这个 topic 研究 evaluation 如何作为一等 objective、feedback signal、selection mechanism 或实验环境，通过 fine-tuning、RL、preference learning 等方式改进模型或 agent。

## Motivation

Evaluation 不只在开发结束时打分，也可以直接指导开发。这里关注完整闭环：评估、诊断、干预、再评估。普通训练论文如果只在最后报告 benchmark 分数，仍然不在范围内；evaluation 必须真正决定选什么、优化什么或下一步尝试什么。

## Existing Approaches

- **自动 post-training R&D。** [PostTrainBench](../works/posttrainbench.md) 给 CLI agent 一个 base model、evaluator 和固定 GPU 时间，最后评价提交模型。
- **数据策略优化。** [Curation-Bench](../works/curation-bench.md) 固定模型和 recipe，只允许修改数据选择。
- **由评估产生监督。** [SkillCoach](../works/skillcoach.md) 把经过验证的过程 rubric 变成 SFT trajectory filter。
- **Judge 作为训练 reward。** [MobileJudgeBench](../works/mobilejudgebench.md) 检验离线 judge 指标能否预测 on-policy reward 的实际效果。

## Comparison

| Work | 被改进对象 | 允许的干预 | Evaluation 的作用 | 防止 gaming 的措施 |
|---|---|---|---|---|
| PostTrainBench | Base language model | 数据、SFT、adapter、RL、超参数 | 反复反馈与最终 objective | 规则、held-out evaluator、contamination audit |
| Curation-Bench | 数据策略与训练后的 VLM | Selection policy | 每轮 downstream feedback | 固定模型、recipe 与 suite |
| SkillCoach | 通过 SFT 改进 agent model | Trajectory selection | Process-quality filter | Validation-gated rubric evolution |
| MobileJudgeBench | 通过 RL 改进 mobile agent | Reward evaluator choice | Judge 作为 on-policy reward | 人工 ground truth 的 judge benchmark |

## Open Questions

- 反复访问 evaluator 何时带来学习，何时只带来 benchmark overfitting 或 reward hacking？
- Evaluation calls、compute、data 与墙钟时间应如何联合计量？
- 哪些诊断信号会带来有用干预，而不是局部追分？
- 怎样在 held-out task 上确认提升，同时又给 agent 足够 feedback 学习？
- Agent 自动取数和修改训练代码时，需要怎样记录 provenance 和 audit trail？

## Related Works

- [PostTrainBench](../works/posttrainbench.md)
- [Curation-Bench](../works/curation-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
