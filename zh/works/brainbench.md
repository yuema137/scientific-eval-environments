# BrainBench (2024)

> [English](../../works/brainbench.md) | **简体中文**

## Overview

BrainBench 是面向神经科学的前瞻式 benchmark，出自论文《Large language models surpass human experts in predicting neuroscience results》：给定一篇 Journal of Neuroscience 的原始摘要与一篇改动了结果但保持连贯的版本，模型须辨认哪一篇报告的是真实结果。这是静态二选一任务，不是 agent benchmark（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2403.03230>
- **Code:** <https://github.com/braingpt-lovelab/BrainBench>
- **Dataset:** <https://huggingface.co/datasets/BrainGPT>
- **Venue:** Nature Human Behaviour, 2024

## Summary

BrainBench 测的是模型是否内化了「神经科学实验会得出什么结果」：200 个测试用例（官方数据集）把真实的 Journal of Neuroscience 摘要与连贯改动版配对，覆盖该刊五个栏目——行为/认知、系统/环路、疾病神经生物学、细胞/分子、发育/可塑性/修复。LLM 以困惑度比较作答；人类专家作答并附信心与专长评级。LLM 在预测实验结果上超过人类专家，其信心与准确率之间有校准关系，而在神经科学文献上微调的 BrainGPT 表现更好。

## Tasks

原始摘要与改动版摘要之间的二选一强制选择；据官方数据集为 200 个测试用例；静态、单次前向评估。

## Domains

覆盖 Journal of Neuroscience 五个栏目的神经科学：行为/认知、系统/环路、疾病神经生物学、细胞/分子、发育/可塑性/修复。

## Evaluation

- LLM 以两篇摘要上的困惑度比较计分；人类专家按选择计分并附信心与专长评级；校准性单独分析。
- **报告。** LLM 在预测实验结果上超过人类专家；LLM 信心越高准确率越高；神经科学微调的 BrainGPT 表现更好。数值准确率为 TODO(reference)。

## Typical Duration

单次强制选择判断；非交互式 agent 设定。

## Main Contribution

评估前瞻性而非回顾性的科学知识——模型能否预判一项实验会发现什么——并表明通用 LLM 已在这件事上胜过领域专家。

## Key Design Ideas

- 改动结果的摘要对在控制文风与连贯性的同时测试结果预测。
- 基于困惑度的计分无需答案抽取，也无需 judge。
- 校准性作为一等属性分析——预报者的信心只有在校准时才有用。

## Strengths

- 少见的测「科学预见」而非「科学回忆」的 benchmark，且专家队列强。
- Nature Human Behaviour 的发表与广泛讨论使其成为「模型作为科学预报者」的参照点。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: BrainBench 是静态强制选择 benchmark，并非 agent 评估；收录是因为其评估方法学（带校准分析的结果预测）与科学 agent 的评判相关。论文微调的 BrainGPT 属于建模贡献，超出范围。

## Related Works

- [MetaSyn](./metasyn.md) — 同样把评估锚定于已发表的生物医学文献，走协议忠实的综合路线。
- [Humanity's Last Exam](./hle.md) — 同样是与前沿专家在封闭式问题上的比较，覆盖全部学科。
- [FormalRewardBench](./formalrewardbench.md) — 同样评估某个信号能否在真品与篡改品之间选对，在形式化证明中。
