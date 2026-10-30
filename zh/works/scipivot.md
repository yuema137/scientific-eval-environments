# SciΠvot (2026)

> [English](../../works/scipivot.md) | **简体中文**

> **首次公开：** 2026-10-15 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2610.21082)

## Overview

研究型 agent 的 benchmark 一般只给最终产出打分，看不到这样的时刻：PI 看了 agent 的计划，说“不行，换个做法”。SciΠvot 就是用这些时刻做成的。大约六个月里，资深研究者用 LLM agent 推进了 26 个真实研究项目，并在过程中纠正 agent 的判断。每个案例都把纠正发生前的项目记录冻结下来，让模型在 agent 的原计划和人工纠正后的计划之间二选一。benchmark 衡量的是：给或不给项目记录时，模型有多大比例选中了纠正后的方案。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [Sci$\Pi$vot: Benchmarking Principal-Investigator Judgment at Pivotal Moments of Scientific AutoResearch Agents](https://arxiv.org/abs/2610.21082)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2610.21082v1>
- **Code / data:** <https://github.com/AutoResearch-Factory/SciPIvot>（248 个案例、提示词、汇总结果；项目记录稍后发布）
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

每个案例包含纠正前的项目记录（代码、实验日志、进展笔记）、LLM 的原计划，以及根据项目历史还原出来的人工纠正方案。模型要么看到两个计划加上项目记录（“project” 条件），要么只看到两个计划（“options only”），推理强度有五档可选，然后从中选一个。每个案例跑两次，两次的选项顺序相反，最后取平均；无法解析的回答按错误计，随机猜的准确率是 50%。之后还有两轮让模型重新考虑，但不告诉它上一轮对不对。只有当五个模型对这个案例的 120 条回答在两个计划之间有分歧时，案例才会被保留。所以这些分数诊断的是模型在有争议的决策上的判断力，不能用来估计 agent 平时出错的频率。

## Tasks

248 个案例来自六个领域的 26 个项目：应用数学与科学计算（8 个项目，85 个案例）、机器人与控制（4，58）、AI 与机器学习（9，59）、生物成像（1，21）、力学与材料（2，20）、地球科学（2，5）。判断类型标签（含主标签和次标签）为：规划 123、聚焦 122、异常察觉 88、调整 65、证据是否充分 47、重复 4。案例由 Grok 4.6 撰写；在 13 个共用案例上做的对照试验没有发现撰写者占优。TODO(reference)：指导这些项目的资深研究者人数。

## Domains

应用数学与科学计算、机器人与控制、AI 与机器学习、生物成像、力学与材料、地球科学；都是在 CPU 和 GPU 上进行的理论和计算研究。

## Evaluation

- **中等推理强度下的准确率，project / options only：** GPT-6 Astra 59.5% / 63.7%、Claude Opus 5 38.9% / 58.9%、GPT-5.6 Sol 35.1% / 46.8%、Grok 4.6 33.1% / 54.0%、GPT-5.6 Terra 29.2% / 55.8%。给了项目记录后，五个模型里有四个低于随机水平；五个模型的平均值在有记录时为 39.2%，没有记录时为 55.8%。
- **project 条件下的最好成绩：** 63.5%（GPT-6 Astra，xhigh 推理强度）。
- **人类基线：** 13 名初次接触这些项目的博士生和博士后为 73.4%，他们阅读项目记录，可以使用 agent 助手。
- **重新考虑：** 初始回答和两轮复查的平均准确率依次为 39.2%、44.0%、42.3%；第一轮复查改对了 422 个错误、又改错了 302 个，第二轮改对 264 个、改错 305 个。
- **按判断类型（Astra）：** 异常察觉类 72.2%，规划类 56.1%，聚焦类 54.9%。
- **统计：** 对案例做 10,000 次配对 bootstrap 得到 95% 区间，另外报告按项目聚类的区间。

## Typical Duration

每个案例做一次二选一，最多再加两轮重新考虑；推理强度是各家提供的档位，不是对齐的 token 预算。

## Main Contribution

一个由 agent 推进的研究项目中真实 PI 纠正构成的 benchmark，检验模型能否认出那个纠正性的决定；论文还测出，在中等推理强度下，加上项目记录反而会降低模型的准确率。

## Key Design Ideas

- 每个案例都截在人工纠正之前的那次提交，所以模型只能看到当时已知的信息。
- 两个计划按两种顺序各出现一次再取平均，消除位置偏差。
- 对比 project 和 options only 两个条件，单独看出继承下来的项目记录对选择的影响。
- 重新考虑的环节量出了多想一轮会改对多少、改错多少。

## Strengths

- 案例来自真实的项目历史，而不是编出来的场景，并且有实测的人类基线。
- 打分是确定性的二选一，同时给出 bootstrap 区间和按项目聚类的区间。
- 失败分析按条件、复查轮次和判断类型都做了量化。

## Limitations

- 作者说明，这个 benchmark 衡量的是能否认出纠正性的决定，不涉及生成计划或执行研究。
- 案例是在模型参与下筛选的，分数不能估计一般情况下的失败率。
- 不包括湿实验，也不包括专用商业软件。
- 不少案例来自同一个项目；地球科学只有 5 个案例，生物成像只有一个项目。
- 推理强度档位不等于相同的算力预算，各家的客户端工具也不一样。
- Repository note：没有公开每个模型的回答日志，冻结的项目记录要等以后再补上。

## Related Works

- [AI's Capability in Assisting Scientific Research II](./ai-assisting-research-ii-project-planning.md) — 同样在真实项目上评估研究计划，并以人类判断为参照。
- [Labference](./labference.md) — 同样在固定的信息范围内，只对下一步的一个决定打分。
