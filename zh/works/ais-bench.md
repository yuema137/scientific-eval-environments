# AIS-Bench (2026)

> [English](../../works/ais-bench.md) | **简体中文**

> **首次公开：** 2026-09-18 · **来源：** [OpenReview 投稿](https://openreview.net/forum?id=RT78MFtfKQ)

## Overview

AIS-Bench 评估 AI Scientist 系统，也就是会提出假设、实现方法并报告发现的 agent。它不只看最终的稿件，而是分阶段打分。每个条目都来自一篇附有可执行代码的已发表机器学习论文，并被拆成四部分：背景（context）、想法（idea）、参考代码和论文本身。系统要在三个阶段分别接受评分：根据背景还原出想法、把想法实现成代码、报告结果。这样一来，端到端结果不好时，就能查到具体是哪个阶段的产物出了问题。在对齐的条目上，实现阶段的得分最低。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Evaluator Reliability & Validation](../topics/evaluator_reliability_validation.md)

## Activities

- [端到端研究](../activities/end_to_end_research.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** [AIS-Bench: An AI Scientist Benchmark for Autonomous Scientific Discovery](https://openreview.net/forum?id=RT78MFtfKQ)，ICLR 2027 投稿 39831（PDF：<https://openreview.net/pdf?id=RT78MFtfKQ>）。作者：TODO(reference)。
- **Venue:** ICLR 2027 在审投稿，主领域为 datasets and benchmarks；OpenReview 页面显示日期为 2026 年 9 月 18 日，修改于 2026 年 10 月 5 日；许可证 CC BY 4.0。
- **Code:** TODO(reference)

## Summary

现有的 AI Scientist 评估要么单独测某一项能力，要么只评最终产物，中间产物都没人检查。AIS-Bench 为每个条目固定一个 <Context, Idea, Code, Paper> 四元组，并独立评估三个阶段：Reference-Conditioned Idea Reconstruction（系统根据背景给出想法）、Code Implementation（系统写出代码，与可执行的参考实现对照）以及 Controlled Reporting（系统根据指定的证据撰写结论）。各阶段指标中依赖 judge 的部分，用留出的人工判断做了校验。在一个统一的、经人工校准的产物有效性标准下，三个阶段中实现阶段得分最低；在配对 bootstrap 区间和其他汇总方式下，这个排序都保持不变。

## Tasks

753 个对齐的 <Context, Idea, Code, Paper> 四元组，都带有可执行的参考实现，由构建流程从 3,174 篇机器学习论文中得到。每个四元组对应三个阶段任务：以参考背景为条件的想法还原、代码实现和受控报告。构建时的过滤条件、各阶段的具体输入以及每个阶段的条目数为 TODO(reference)。

## Domains

机器学习研究（源论文都是机器学习论文）。

## Evaluation

- **分阶段指标：** 每个阶段独立评分；指标定义为 TODO(reference)。
- **Judge 校验：** 依赖 judge 的部分用留出的人工判断做了校验；一致性统计为 TODO(reference)。
- **评估的系统：** 13 个系统，包括 prompting 策略、专用系统和端到端 agent；系统名称和各自得分为 TODO(reference)。
- **阶段比较：** 在对齐的四元组上，按统一的、经人工校准的产物有效性标准，实现阶段得分最低；配对 bootstrap 区间和其他汇总方式都保持这一排序。各阶段的具体分数为 TODO(reference)。
- **审计：** 在已分类的实现失败中，功能逻辑偏差占多数；在报告阶段，即使给定了证据，夸大指标和引用无法核实的问题依然存在。审计计数为 TODO(reference)。

## Typical Duration

TODO(reference)

## Main Contribution

一个诊断框架：在由论文得到、附有可执行参考代码的四元组上，把自动化研究拆成三个独立评分的阶段（想法还原、代码实现、受控报告），而不是只评单项能力或最终稿件。

## Key Design Ideas

- 四元组构建时让背景、想法、代码和论文都来自同一项源工作，所以每个阶段都有自己的参考答案。
- 以参考为条件的想法还原，让想法阶段有一个固定目标，而不必做开放式的新颖性评判。
- 受控报告会提供证据，这样报告阶段的错误（夸大指标、引用无法核实）就能和实现阶段的错误分开。
- 统一的、经人工校准的产物有效性标准，让各阶段分数可以在对齐的条目上相互比较。

## Strengths

- 分阶段评分能定位自动化研究在哪里出错；摘要报告实现是最弱的阶段。
- 依赖 judge 的部分用留出的人工判断做了核对。
- 阶段排序的稳健性用配对 bootstrap 区间和其他汇总方式做了检验。

## Limitations

- Repository note: 本卡片只依据 OpenReview 投稿页面撰写；论文全文无法获取，所以指标、系统名称、分数以及作者自述的局限都是 TODO(reference)。
- Repository note: 首次公开日期取的是 OpenReview 投稿页面上显示的发布日期；无法核实这份投稿在那天是否已经公开可见，也没有找到更早的公开版本（arXiv 或代码发布）。
- Repository note: 所有源论文都是机器学习论文，所以报告的阶段排序只针对 ML 研究。

## Related Works

- [PaperBench](./paperbench.md) — 同样用 ML 论文构建任务，但对照层级化 rubric 给整篇论文的复现打分，而不是分别评想法、代码和报告三个阶段。
- [ResearchCodeBench](./researchcodebench.md) — 同样评估把研究论文的贡献实现为可执行代码的能力，这正是 AIS-Bench 报告为最弱的阶段。
- [AI-Researcher](./ai-researcher.md) — 其中的 Scientist-Bench 同样让每个任务对应一篇真实论文，但通过成对的 LLM 评审给最终稿件打分，而不是分别评想法、代码和报告。
