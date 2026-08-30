# CoLA: Controlling Large Language Model with Latent Action (2025)

> [English](../../works/cola.md) | **简体中文**

## 概览

CoLA 为 LLM 学出一个紧凑 latent action space，使 policy 的 decision representation 不再由 token vocabulary 直接决定。

## Topics

- [Hierarchical Decision Abstraction](../topics/hierarchical_decision_abstraction.md)
- [Evaluation-Driven Post-Training](../topics/evaluation_driven_post_training.md)

## Activities

N/A — 通用 LLM 与 agent adaptation 方法，没有直接评价科学或研究活动。

## Links

- **Paper:** <https://proceedings.mlr.press/v267/jia25e.html>
- **Model:** <https://huggingface.co/LAMDA-RL/Llama-3.1-CoLA-10B>
- **Venue:** ICML 2025

## 摘要

CoLA 用面向 future token 的 inverse-dynamics model 提取 latent action，把 LLM 调成由 action 控制的 language world model，再通过 behavior cloning 或 RL 训练 action policy。实验覆盖数学、preference control、ALFWorld 和 ScienceWorld，并区分 seen 与 unseen agent task。

## 任务

数学 reasoning 与 search、可控 preference generation，以及 ALFWorld 和 ScienceWorld 中的多轮交互。

## 领域

通用语言模型控制与 embodied/text-agent environment。ScienceWorld 在这里是模拟 agent task，不是科学研究 workflow，因此不映射到 canonical science domain。

## 评估

数学 benchmark accuracy 与 pass@K、GPT-4 preference win rate、reward-hacking stress test，以及 seen/unseen ALFWorld 和 ScienceWorld task success。

## Typical Duration

不同任务没有统一的 wall-clock 或 episode 时长。

## 主要贡献

不由人手写 action taxonomy，而是把 LLM 的 RL action-space structure 本身变成学习对象。

## Key Design Ideas

- 用面向 future token 的 inverse dynamics 推断 action。
- 把 latent-action policy 与 action-conditioned language world model 分开。

## Strengths

- 同一个 representation 同时在 reasoning、preference 和 interactive agent 上测试。
- 包含 seen/unseen split 与 reward-hacking probe。

## 局限

- Latent action 不如具名 semantic action 容易解释。
- 下游结果提高不等于这些 latent dimension 对应可复用的人类策略。
- 对照实验没有把其余训练与架构选择全部固定，只改变 action granularity。

## Related Works

- [MA-RLHF](./ma-rlhf.md)
- [MetaAct-RL](./metaact-rl.md)
