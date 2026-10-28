# AutoSciBench (2026)

> [English](../../works/autoscibench.md) | **简体中文**

> **首次公开：** 2026-10-04 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.05140)

## Overview

科学 agent 的 benchmark 构建起来很费专家时间，而且 agent 一进步就容易被做到饱和。AutoSciBench 的做法是让 agent 自己来生成 benchmark。每个任务由两部分确定：一个概念（领域、数据模态、推理方式）和一份配方（怎样构造数据、问题和参考答案）。随后由求解 agent 尝试作答，judge 阅读它们的轨迹。如果任务太简单、无法验证，或者能走捷径做出来，生成器就修改配方或概念。评测时，把求解 agent 在生成任务上的准确率，与它们在作为种子的人工 benchmark 上的准确率做对比。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)

## Links

- **Paper:** [AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents](https://arxiv.org/abs/2610.05140)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.05140v1>
- **Venue:** arXiv 预印本（cs.AI，2026）
- **Code / data:** 论文中没有找到发布链接。TODO(reference)

## Summary

生成器（在 Claude Code 中运行的 Claude Opus 4.8，或在 Codex 中运行的 GPT-5.6 Sol）根据概念和配方构建任务；随后同一个模型在看不到参考答案的情况下独立求解三次。judge LLM 审阅问题、数据、参考答案、求解答案和轨迹，评估任务能否验证、难度如何。它还会找出捷径。论文对捷径的定义是绕过预期的验证或证据整合步骤的解题路径，比如只凭一次工具输出就给出答案，不再回头检查原始数据。生成器最多修改配方 10 轮；如果连续四次修改配方仍达不到两项标准，就转而修改概念。已完成运行中总结出的经验会用来指导后面的概念生成。求解答案按指定格式写成单个值，与参考答案做精确匹配。

## Tasks

每个领域、每个生成器各生成 50 个任务，来自 10 个概念、五轮经验引导的迭代。三个领域各以一个人工整理的 benchmark 作为种子：计算生物学（CompBioBench）、材料科学（MatTools）和临床影像（MedCTA）。

## Domains

计算生物学、材料科学（计算材料工具）和临床医学影像。

## Evaluation

- **求解模型：** 十个模型（Claude Opus 5、Opus 4.8、Opus 4.7、Sonnet 5、Haiku 4.5；GPT-6 Astra、GPT-5.6 Sol、Terra、Luna；GPT-5.5）。
- **平均求解准确率（%），人工种子 / Opus 生成 / GPT 生成：** 计算生物学 79.8 / 57.4 / 74.1；材料科学 95.7 / 70.2 / 77.6；临床影像无种子数据 / 71.1 / 74.5。摘要里说的下降 22.4 和 25.5 分，是 Opus 生成任务与种子的对比。MedCTA 由 LLM 评估器打分，所以没有种子一栏。
- **单个模型的例子：** Claude Haiku 4.5 在 MatTools 上得 93.7%，在 Opus 生成的材料任务上只有 21.3%；GPT-6 Astra 在计算生物学的种子和 Opus 生成任务上分别得 98.0% 和 81.0%。
- **质量评分：** 由两个 LLM judge（Claude Opus 4.8 和 GPT-5.6 Sol）在 1–5 分制上评可验证性、有用性和适配度；摘要称三个领域中生成任务的平均评分都更高。TODO(reference)：具体评分数值。
- **消融：** 迭代修改提高了难题的比例；在材料科学上，经验引导的生成把求解成功率从 66.7% 降到 35.0%，把难题比例从 15.0% 提高到 50.0%。
- Repository note：部分种子 benchmark 的准确率取自排行榜，推理强度不是 high 或者没有说明，所以并非每组种子与生成任务的对比都在相同设置下进行。

## Typical Duration

流水线每个阶段限时 3,600 秒。每道题的生成成本：Opus 4.8 在计算生物学、材料、临床影像上分别为 58.47、22.36、24.88 美元；GPT-5.6 Sol 分别为 111.26、114.11、110.45 美元。大部分成本花在任务实现和求解上。

## Main Contribution

一个由生成器、求解器和 judge 组成的循环：构建科学 agent 的 benchmark 任务，并根据求解轨迹反复修改，直到任务可验证、足够难、没有检出捷径。这样 agent 进步之后，benchmark 可以重新生成。

## Key Design Ideas

- 概念和配方分开，循环可以先修任务的构造方式而不动科学目标；配方反复失败后才改目标。
- 捷径是从求解轨迹里找出来的，不只看最终答案。
- 已完成运行的经验会反馈给后续的概念生成。
- 答案限定为指定格式的单个值，便于精确匹配。

## Strengths

- 任务按需生成，答案不可能是从已发表的 benchmark 里背下来的。
- 结果覆盖十个求解模型在生成任务和种子任务上的表现，并给出了每个模型的分数。
- 生成成本按每道题报告，并按流水线阶段拆分。

## Limitations

- 论文没有描述对生成任务的人工专家审核；质量由 LLM judge 评定，而其中一个 judge 同时也是生成器。
- 修改任务时，生成器也负责求解自己出的题，所以难度是按这个模型校准的。
- 附录指出，benchmark 上的表现不能说明可以用于临床。
- Repository note：在生成任务上准确率更低，说明这些任务对现有求解模型更难；至于它们测的是否和种子 benchmark 是同一种能力，目前只有 LLM 质量评分作为依据。

## Related Works

- [MatTools](./mattools.md) — 材料科学领域的种子 benchmark。
- [HeurekaBench](./heurekabench.md) — 同样从已有研究成果中半自动地派生科学 agent 任务。
- [CODE2BENCH](./code2bench.md) — 同样用可重复的构建流水线生成 benchmark，以抵御数据污染。
