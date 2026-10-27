# AlphaIdeaBench (2026)

> [English](../../works/alphaideabench.md) | **简体中文**

> **首次公开：** 2026-10-24 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.33644)

## Overview

AlphaIdeaBench 给自动构思系统写出的研究提案打分，并把明确的资源预算纳入评分。每个任务都写明可用的 GPU、API 额度、日历时间和标注工时，LLM judge 检查提案中的计划是否放得进这些限制。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [AlphaIdeaBench: Benchmarking Automated Research Idea Generation under Feasibility Constraints with Peer Review Alignment](https://arxiv.org/abs/2610.33644)
- **Full text:** <https://arxiv.org/html/2610.33644v1>
- **Code:** <https://github.com/SHUNCHAOZHOU/AlphaIdeaBench>（只含评审部分，MIT 许可证）
- **Venue:** arXiv 预印本（2026）

## Summary

构思 harness 拿到一个任务和一份预算，返回一个 JSON 提案，其中包含从标题到资源计划共十个必填字段。judge 在十二个维度上打分，其中包括预算可行性。它给出的新颖性分数，会与根据 600 篇论文的同行评审意见得出的分数对比。八个 harness 共用同一个基础模型，另有八个基础模型在同一个 harness 中运行，因此 harness 的影响和模型的影响可以分开测量。

## Tasks

100 个任务分两组，每组 50 个：一组来自 NeurIPS、ICML 和 ICLR 在 2023–2025 年的 workshop 征稿说明，另一组来自 50 篇综述中写明的开放问题。任务分布在九个机器学习方向，最多的是 LLM 与推理（22 个），最少的是图与几何、持续学习（各 6 个）。主设置采用学术实验室预算：四张 A100 40GB GPU、200 GPU 小时、200 美元 API 额度、八周日历时间和 40 小时标注工时。学生档和实验室档分别在此基础上缩小和放大。被评测的 harness 是 CoI-Agent、SciMON、AI-Researcher、Virtual-Scientists、ResearchAgent、AI-Scientist-V1、AgentLaboratory 和 AI-Scientist-V2。

## Domains

机器学习研究构思。100 个任务全部来自机器学习 workshop 和综述，其中 13 个标为 AI for science。论文指出，湿实验研究上的结果可能不同。

## Evaluation

- Gemini 3.7 Flash 在十二个维度上按 1–5 分打分：有效性（四项）、新颖性（问题、方法、场景、洞见）和可行性（技术、数据、预算、验证）。检查预算时，它可以查询 API 和 GPU 的价格。
- judge 校验：Gemini 3.7 Flash 先把 600 篇论文（ICLR 2026、NeurIPS 2025 和 ICML 2025 各 200 篇）的评审意见转换成 1–5 分的新颖性分数，judge 再只根据标题和摘要给每篇论文打分。按会议统计，问题新颖性的 ±1 分以内一致率约为 94.5–97.4%，方法新颖性约为 95.9–96.8%。场景新颖性降到约 80.6–87.5%，judge 在这一项上比评审人更严格。
- 有效性和可行性没有人工参照。
- 使用 Gemini 3.7 Flash 时，各 harness 的总分在 4.02 到 4.31 之间；CoI-Agent 最高，SciMON（4.29）以微弱差距位居其后。所有 harness 的场景新颖性都不超过 1.87。为 CoI-Agent 更换基础模型后，总分从 4.31（Gemini 3.7 Flash）降到 1.84（Llama 4 Scout）。
- 用 GPT-5 mini 重新评分来检查排名：harness 排名的 Spearman ρ 为 0.81，基础模型排名为 0.83。

## Typical Duration

未报告生成提案所需的时间。在一个综述任务上，单次构思消耗的 token 从 9,968（2 次调用，AI-Scientist-V2）到 279,759（50 次调用，ResearchAgent）不等。任务预算描述的是提案中的研究计划，不是 harness 本身的运行开销。

## Main Contribution

把资源预算写进每个构思任务，并依据预算给提案的可行性打分。

## Key Design Ideas

- 固定的提案格式让不同的 harness 可以按同样的字段评分。
- 不同档位的预算让同一个任务可以在不同资源条件下评判。
- 新颖性拆成四个方面，judge 的一致率逐项报告。

## Strengths

- 通过两组对照实验，把 harness 的影响和基础模型的影响分开。
- 报告了 judge 一致率最弱的方面，而不是只给一个合并后的数字。

## Limitations

- 提案不会被执行，分数是对书面计划的判断。
- 作为参照的新颖性分数由 Gemini 3.7 Flash 从评审意见转换而来，它与正式评分所用的 judge 是同一个模型；有效性和可行性没有与人工判断对照。
- 在 100 个任务的实验中，每个维度只评一次。
- 公开代码只包含评审部分，八个 harness 都是外部系统。

## Related Works

- [IdeaBench](./ideabench.md) — 为依据论文上下文生成的研究想法打分。
- [AgentIdeaBench](./agentideabench.md) — 比较提供整理好的文献与由 agent 自行收集文献对假设生成的影响。
- [MLR-Bench](./mlr-bench.md) — 评测从想法到论文的机器学习研究。
