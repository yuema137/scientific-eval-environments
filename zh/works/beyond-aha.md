# Beyond 'Aha!': Toward Systematic Meta-Abilities Alignment in Large Reasoning Models (2026)

> [English](../../works/beyond-aha.md) | **简体中文**

> **首次公开：** 2025-05-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2505.10554)

## 概览

Beyond 'Aha!' 先把 deduction、induction 和 abduction 显式训练成可复用 meta-ability，再做领域 RL，不再依赖 outcome RL 偶然产生这些行为。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Skill Learning & Evolution](../topics/skill_learning_evolution.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — 测的是通用 reasoning transfer，不是 agent 执行科学或研究 workflow。

## Links

- **Preprint:** <https://arxiv.org/abs/2505.10554>
- **Paper:** <https://aclanthology.org/2026.findings-acl.1981/>
- **Venue:** Findings of ACL 2026

## 摘要

论文分别为 deduction、induction 和 abduction 构造 self-verifiable synthetic task，单独 align 三种能力，合并 parameter state，最后再做 domain-specific RL。数学、coding 和 science evaluation 用来检验：显式训练 reasoning primitive，是否比等待 self-correction、backtracking 或 verification 从 outcome reward 中随机出现更稳定。

## 任务

三套 synthetic diagnostic training set，以及七个 unseen 数学、coding 和 science benchmark，包括 MATH-500、历史 AIME、AIME 2024 与 LiveCodeBench。

## 领域

跨数学、coding 与 science benchmark 的通用 reasoning post-training，不是 scientific-agent workflow。

## 评估

七个 unseen benchmark 的 pass@1、逐 meta-ability diagnostic、parameter-merging comparison，以及 7B/32B model 继续做 domain RL 后的增益。

## Typical Duration

没有报告固定的逐题 wall-clock budget。

## 主要贡献

用 evaluation-driven 实验检验显式、可复用的 cognitive primitive 能否成为后续 reasoning optimization 的基础。

## Key Design Ideas

- 用自动生成、self-verifiable 的 task 分别训练三种 meta-ability。
- 合并各自 aligned 的 parameter，再做 domain-specific RL。

## Strengths

- 在三类 held-out task 上测 transfer，不局限于单个 dataset。
- 用 staged experiment 分开 primitive alignment、parameter merging 与 downstream RL。

## 局限

- Meta-ability 是 capability target，不是 interactive policy 每一步都要选择的 action。
- 三类 taxonomy 由人定义，可能漏掉其他有用 cognitive operation。
- Benchmark transfer 本身不能证明 agent 内部已经实现 causal modularity 或 fault localization。

## Related Works

- [MetaAct-RL](./metaact-rl.md)
- [CoLA](./cola.md)
