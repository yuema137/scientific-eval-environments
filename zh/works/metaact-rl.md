# MetaAct-RL: Training Language Models for Reasoning Through Meta-Action-Based Reinforcement Learning (2026)

> [English](../../works/metaact-rl.md) | **简体中文**

## 概览

MetaAct-RL 把语言模型推理写成一串语义 meta-action 的选择与执行，例如 forward reasoning、critique 和 refinement。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)
- [Credit Assignment](../topics/credit_assignment.md)

## Activities

N/A — 通用数学与文字推理方法，没有直接评价科学或研究活动。

## Links

- **Paper:** <https://ojs.aaai.org/index.php/AAAI/article/view/40694>
- **Venue:** AAAI 2026

## 摘要

该方法围绕高层 thinking action 标注并训练 reasoning trace，再用 length reward、regularization 和 key-state restart 做 RL，促使模型使用更多样的 action。六个 benchmark 上，论文报告 Llama-3.2-1B 相对 vanilla RL 平均提高 7.99 分，Llama-3.1-8B 提高 7.17 分；Qwen2.5-1.5B 在 AIME 2024 上提高 7.5 分。

## 任务

AQuA、GSM8K、MATH、MathQA、SVAMP、TheoremQA，以及额外的 AIME 2024/2025 evaluation。

## 领域

通用语言模型 reasoning 与 post-training，不对应某个 canonical 科学或工程领域。

## 评估

Answer accuracy、response length、meta-action distribution/diversity、sampling efficiency，以及 reward 与 restart component ablation。

## Typical Duration

没有报告固定的逐题 wall-clock budget。

## 主要贡献

把语义 thinking operation 变成显式 policy decision，不再只靠 outcome-only token RL 偶然产生 critique 与 refinement。

## Key Design Ideas

- 合成带显式 meta-action boundary 的 trace。
- 用 length regularization 与 key-state restart 保持 action diversity。

## Strengths

- 除 answer accuracy 外，还测行为多样性。
- 覆盖多个 model family、scale 与更难的 held-out benchmark。

## 局限

- 人工 action vocabulary 会把设计者的 reasoning ontology 带进模型。
- 熟悉 reasoning suite 上的提升不能证明它会迁移到陌生工程 workflow。
- Action label 与具体 reasoning 仍由同一个 autoregressive system 生成，模块级 fault isolation 仍不完整。

## Related Works

- [PG-HAP](./pg-hap.md)
- [Beyond 'Aha!'](./beyond-aha.md)
