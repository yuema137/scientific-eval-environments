# Evaluation-Driven Post-Training

> [English](../../topics/evaluation_driven_post_training.md) | **简体中文** · [← 全部 topics](./README.md)

## 先看它解决什么问题

Evaluation 经常被放在 training 最后：先训练，最后测一次，发一张表。这个 topic 看的是相反的安排。Evaluator 被放进 development loop，用结果决定下一轮该换 data、reward、fine-tuning method，还是 model update。

比如 agent 先 fine-tune 一个 base model，再跑 held-out suite。结果显示 function calling 提高了，medical reasoning 却退步了，于是下一轮改 training mixture。这才是 evaluation-driven loop。代价也很直接：反复看 evaluator 可能把改进变成 benchmark overfitting 或 reward hacking，所以 held-out test 与 contamination audit 也是方法的一部分。

## 定义

Evaluation-driven post-training 把evaluator 放进改进闭环。开发者或 agent 根据评估结果选 data、reward、fine-tuning 设置、preference update 或 reinforcement-learning experiment，然后再测一次改过的 model。

## 为什么重要

有用的信号不只是「最后的 model 分数更高了」。更重要的是，哪个被测出来的弱点引发了下一次修改，修改后有没有解决问题，又有没有把其他能力搞坏。如果一篇普通 training paper 只训一次再报 benchmark 数字，它还不在这个 topic 里。Evaluation 必须真正影响系统下一步选什么、优化什么、尝试什么。

## 现有方法

- **自动 post-training R&D。** [PostTrainBench](../works/posttrainbench.md) 给 CLI agent 一个 base model、evaluator 和固定 GPU 时间，最后评价提交模型。
- **数据策略优化。** [Curation-Bench](../works/curation-bench.md) 固定模型和 recipe，只允许修改数据选择。
- **由评估产生监督。** [SkillCoach](../works/skillcoach.md) 把经过验证的过程 rubric 变成 SFT trajectory filter。
- **Judge 作为训练 reward。** [MobileJudgeBench](../works/mobilejudgebench.md) 检验离线 judge 指标能否预测 on-policy reward 的实际效果。

## 方法对比

| Work | 被改进对象 | 允许的干预 | Evaluation 的作用 | 防止 gaming 的措施 |
|---|---|---|---|---|
| PostTrainBench | Base language model | 数据、SFT、adapter、RL、超参数 | 反复反馈与最终 objective | 规则、held-out evaluator、contamination audit |
| Curation-Bench | 数据策略与训练后的 VLM | Selection policy | 每轮 downstream feedback | 固定模型、recipe 与 suite |
| SkillCoach | 通过 SFT 改进 agent model | Trajectory selection | Process-quality filter | Validation-gated rubric evolution |
| MobileJudgeBench | 通过 RL 改进 mobile agent | Reward evaluator choice | Judge 作为 on-policy reward | 人工 ground truth 的 judge benchmark |

## 还没解决的问题

- 反复访问 evaluator 何时带来学习，何时只带来 benchmark overfitting 或 reward hacking？
- Evaluation calls、compute、data 与墙钟时间应如何联合计量？
- 哪些诊断信号会带来有用干预，而不是局部追分？
- 怎样在 held-out task 上确认提升，同时又给 agent 足够 feedback 学习？
- Agent 自动取数和修改训练代码时，需要怎样记录 provenance 和 audit trail？

## 相关工作

- [PostTrainBench](../works/posttrainbench.md)
- [Curation-Bench](../works/curation-bench.md)
- [SkillCoach](../works/skillcoach.md)
- [MobileJudgeBench](../works/mobilejudgebench.md)
- [MA-RLHF](../works/ma-rlhf.md)
- [CoLA](../works/cola.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
