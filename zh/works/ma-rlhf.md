# MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions (2025)

> [English](../../works/ma-rlhf.md) | **简体中文**

> **首次公开：** 2024-10-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2410.02743)

## 概览

MA-RLHF 不再逐 token 更新 policy，而是把一段 token 或更高层语言结构当作 macro-action，用实验检验更粗的时间粒度能否改善 RLHF 的 credit assignment 与学习效率。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Credit Assignment](../topics/credit_assignment.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — 通用 LLM alignment 方法，没有直接评价科学或研究活动。

## Links

- **Preprint:** <https://arxiv.org/abs/2410.02743>
- **Paper:** <https://proceedings.iclr.cc/paper_files/paper/2025/hash/429d69979c22b06d6baa65caf3ab1e10-Abstract-Conference.html>
- **Code:** <https://github.com/ernie-research/MA-RLHF>
- **Venue:** ICLR 2025

## 摘要

普通 RLHF 把每个 subword token 当成一个 action，sequence reward 与要负责的 decision 相距很远。MA-RLHF 在 semi-Markov formulation 下把相邻 token 合成 macro-action。论文覆盖 summarization、dialogue、question answering 和 program synthesis，并报告达到 vanilla RLHF 同等表现所需训练时间约少 1.7–2 倍。

## 任务

使用 2B 到 27B 的 Gemma 系列模型做四类 preference optimization：文本摘要、对话、问答和程序生成。

## 领域

通用语言模型 alignment 与 reinforcement learning，不对应某个 canonical 科学或工程领域。

## 评估

任务质量与 reward 指标、training curve、达到 token-level RLHF 同等表现所需时间，以及不同 macro-action 构造、temperature 和 rejection sampling 下的稳健性。

## Typical Duration

没有统一的单样本时长；论文比较完整训练时间与收敛速度。

## 主要贡献

直接检验 RLHF 的时间粒度，说明 tokenizer 划分语言的方式不必同时决定 policy 的 decision 粒度。

## Key Design Ideas

- 在 macro-action boundary 上聚合 token log-probability 与 advantage。
- 比较 fixed-length 与 learned semantic grouping，不增加 inference cost。

## Strengths

- 基本保持标准 RLHF 的语言生成设置。
- 同时报告学习速度、最终质量和多个 model size。

## 局限

- Macro-action 可能只是一段更长的 token，并不一定具有策略语义。
- 论文测了效率与下游质量，没有测 compositional OOD strategy transfer。
- 它没有用模块化 planner–executor 架构分开策略选择与文本生成。

## Related Works

- [CoLA](./cola.md)
- [HiPER](./hiper.md)
