# LLM-SRBench (2025)

> [English](../../works/llm-srbench.md) | **简体中文**

## Overview

LLM-SRBench 是用 LLM 做科学方程发现的 benchmark，含 239 个高难度问题，专为防止简单记忆而设计：LSR-Transform 把常见物理模型改写为少见的数学表征以考察记忆之外的推理，LSR-Synth 引入需要数据驱动推理的合成发现型问题。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2504.10415>
- **Code:** <https://github.com/deep-symbolic-mathematics/llm-srbench>
- **Dataset:** <https://huggingface.co/datasets/nnheui/llm-srbench>
- **Venue:** ICML 2025 (oral)

## Summary

建立在著名方程之上的方程发现评估，奖励的是对著名方程的记忆，而非发现能力。LLM-SRBench 用横跨四个科学领域的两类问题堵上这个缺口：LSR-Transform 从常见物理模型出发、却要求在陌生的数学表征中推理；LSR-Synth 的合成问题则根本没有可记忆的答案。对使用开源与闭源 LLM 的最先进发现方法的评估显示，目前最好的系统符号准确率也只有 31.5%。

## Tasks

239 个方程发现问题，分 LSR-Transform 与 LSR-Synth 两类，横跨四个科学领域；系统需从数据中恢复支配方程。

## Domains

四个科学领域；摘要未点名。

## Evaluation

- 恢复方程对照真值的**符号准确率**。
- **报告。** 目前表现最好的系统符号准确率仅 31.5%。

## Typical Duration

每个问题为迭代方程搜索运行；预算依方法而异，为 TODO(reference)。

## Main Contribution

一个从构造上让记忆无利可图的方程发现 benchmark，把「LLM 符号回归」变成可测量的发现能力。

## Key Design Ideas

- 把已知模型变换到陌生表征，切断从回忆到答案的捷径。
- 合成的发现型问题保证存在一个彻底无记忆可依的子集。
- 单一的符号准确率指标让异构的发现方法可比。

## Strengths

- 方法无关：评测的是发现系统，而非某一种建模流派。
- 31.5% 的上限记录了 LLM 方程发现距可靠恢复的差距。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。

## Related Works

- [NewtonBench](./newtonbench.md) — 同样防范定律发现中的记忆，通过对经典定律做反事实偏移。
- [DiscoverPhysics](./discoverphysics.md) — 同样为发现的定律打分，另加交互式实验与解释评判。
- [MaD Physics](./mad-physics.md) — 同样从数据推断支配定律，在定价的观测预算之下。
