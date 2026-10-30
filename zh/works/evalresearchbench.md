# EvalResearchBench (2026)

> [English](../../works/evalresearchbench.md) | **简体中文**

> **首次公开：** 2026-10-03 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.04184)

## Overview

能自我改进的 agent 需要反馈信号，而常用的信号是一批大型 benchmark，每改一次都重跑，又慢又贵。EvalResearchBench（ERB）想知道 agent 能不能自己搭一个便宜的替代品。一个 “researcher” agent 拿到目标 benchmark 的说明、允许使用的任务来源、计量的模型 API，以及固定的时间和经费预算，要为编程、协同办公和推理三个方向冻结一个可执行的评测器。随后用这个冻结的评测器给一组候选模型打分，看这些分数和排序与候选模型在 14 个目标 benchmark 上的成绩有多接近，其中包括 researcher 从没见过的目标。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

N/A — researcher agent 为通用的编程、协同办公和推理能力设计评测器，不评估科学研究任务。

## Links

- **Paper:** [EvalResearchBench: Can AI Agents Build Their Own Feedback for Recursive Self-Improvement?](https://arxiv.org/abs/2610.04184)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.04184v1>
- **Project:** <https://mercury7353.github.io/self-evaluation-bench/>
- **Code:** <https://github.com/Mercury7353/self-evaluation-bench>
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

researcher 有三小时，自身推理预算 100 美元，试跑候选模型的预算也是 100 美元。它能看到开发用的目标 benchmark，以及四个开发候选模型在这些目标上的参考分数；另外八个封存目标和九个封存候选模型，要等评测器冻结后才公开。它要挑选或编写至少 100 道计分题目，实现评分程序，设定汇总权重，试跑之后全部冻结。接着由独立评估在所有候选模型上运行这个冻结的评测器（总额上限 120 美元，每个候选模型 30 美元）。每个方向的分数用两种方式与目标参考分数比较。一是 100 × Lin 一致性系数，它不光看排序，还看分数的水平和离散程度是否对得上；二是成对一致率，即在参考分数不打平的模型对中，评测器排对顺序的比例，评测器给出平局记半分。一个给所有模型都打同样分的常数评测器，Score 为 0，成对一致率为 50%。

## Tasks

只有一个任务，每个 researcher 跑一次：为三个方向搭一个精简的评测器。14 个目标分为六个开发可见的（DeepSWE、SciCode、SWE-bench Multilingual、GDPval、AdvancedIF、HLE）和八个封存的（Terminal-Bench 2.1、ProgramBench、SWE-bench、BrowseComp、Harvey LAB-AA、AA-Briefcase、AA-LCR、CritPt）。13 个候选模型分为四个开发用和九个封存的。共评测九个 researcher，每个在 Codex 或 Claude Code 中跑一轮。

## Domains

编程、协同办公和推理方面的通用模型能力。SciCode 和 CritPt 也在目标之列，但 researcher 的任务是设计评测器，不是做科学工作。

## Evaluation

- **总 Score / 成对一致率（14 个目标等权）：** GPT-6 Astra 22.79 / 69.54%、Grok 4.7 22.59 / 74.87%、Fable 5.1 21.96 / 67.80%、Opus 5 21.79 / 64.88%、Kimi K3 18.03 / 74.58%、GPT-5.6 Sol 16.99 / 63.32%、GLM-5.3 14.27 / 64.72%、DeepSeek V4 Pro 10.49 / 63.50%。
- **上限：** 一个已知标签的 oracle 成对一致率为 91.20%，这是目标 benchmark 彼此之间的分歧所决定的上限。
- **人工选题基线（Random120）：** 按来源分层抽取 120 道公开题目（每个方向 40 道），在 12 个候选模型上得到 13.10 / 68.29%；在相同的模型组上，八个 agent 搭的评测器中有七个 Score 超过它，但成对一致率超过它的只有四个。
- **开发与封存：** 在开发目标上 Score 最高的是 Fable 5.1（23.40），在封存目标上最高的是 Grok 4.7（26.14）。
- **失败案例：** Opus 5 的开发诊断中，102 条回复有 36 条触到回答长度上限，其中 32 条是空的；Fable 5 只完成 20 个（共 39 个）“候选模型 × 方向”分数就用光了评估预算，所以它那一行是插补出来的情景；Grok 4.7 的 20 道协同办公题里，有 6 道占了该方向 93.87% 的权重。

## Typical Duration

每个 researcher 有三小时研究时间，推理预算 100 美元，开发测试 100 美元，评估最多 120 美元。

## Main Contribution

一个把“搭建评测器”本身当作 agent 任务的 benchmark，用评测结果与留出 benchmark 成绩的一致程度打分，把对可见目标的拟合和向封存目标的迁移分开衡量。

## Key Design Ideas

- 评测器冻结之前，封存的目标和候选模型都不可见，所以能量出对可见参考分数的过拟合。
- Lin 一致性系数会惩罚排序对了、但分数水平或离散程度不对的评测器。
- 研究、试跑和评估三块预算是固定的，并分开计量。
- 人工抽样的公开题目和常数评测器为分数提供了参照点。

## Strengths

- 结果把开发目标和封存目标分开报告，显示在可见目标上拟合得最好，不等于迁移得最好。
- 计算并报告了由目标之间分歧决定的一致率上限。
- 失败案例按 researcher 自己的诊断结果计数。

## Limitations

- 每个 researcher 只跑一轮，测不出不同运行之间的波动。
- 参考分数是来自不同评测协议的公开快照，各目标的分数尺度并不完全可比。
- 部分成本来自合作者的报告而非实际计量，Fable 5 那一行依赖插补。
- Repository note：v1 全文的标题是 “EvalResearchBench: Can AI Agents Design Their Own Evaluations?”，arXiv 页面上的标题见 Links。本卡片的数字都以 v1 为准。

## Related Works

- [PTA-IRT](./pta-irt.md) — 同样用较小的评测预测完整套件的结果，并在留出的 agent 上验证预测。
- [AutoSciBench](./autoscibench.md) — 同样让 agent 构建 benchmark 任务，面向科学领域。
- [SciCode](./scicode.md) — 开发目标之一。
