# A Framework for Evaluating Agentic Skills at Scale (2026)

> [English](../../works/a-framework-for-evaluating-agentic-skills-at-scale.md) | **简体中文**

> **首次公开：** 2026-06-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2606.17819)

## Overview

一套评估方法学，让 skill 作者把自己的 skill 变成带评分量规的真实可执行任务，并在大规模上应用于约 500 个真实 agent skill、1,000 个生成任务和 19 种 agent–模型配置。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 面向通用 agent skill 的评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.17819>
- **Code:** <https://huggingface.co/datasets/tesslio/task-evals-for-skills>
- **Venue:** arXiv preprint, 2026

## Summary

论文的前提是：agent skill 是增强 LLM agent 的一类结构化、可复用知识工件，它在工业界的普及已经跑在了任何一套可复用的单 skill 评估方法学前面。该框架是一条五阶段流水线：从 skill 内容中抽取使用场景，搭建能满足其执行依赖的环境，生成带定制量规的真实任务，校验任务的可执行性与量规是否泄漏，最后让求解 agent 分别在有 skill 与无 skill 两种条件下运行，并对照隐藏量规评分。大规模应用的结果显示，各模型对 skill 中所写指令的贴合程度差异很大，而相较无 skill 基线，能否用上 skill 会实质改变模型行为。

## Tasks

从约 500 个各不相同的真实 skill 生成了约 1,000 个真实可执行任务，每个任务都带有从 skill 内容派生的任务完成量规与指令遵循量规。共收集到约 38,000 条有效轨迹。每个任务解两遍——一遍不给 skill，一遍明确告知相关 skill 已安装。一项聚类分析把这些 skill 归入 15 个内容簇，最大的几个是 Web & UI Design（14.3%）、Machine Learning & AI（13.6%）、Testing/QA（10.2%）、Finance & Crypto（9.9%）与 Infrastructure & DevOps（8.3%）；Scientific Computing 占 7.5%。

## Domains

这批 skill 语料明确是跨领域的，但按作者自己的说法偏向软件工程内容，因为目前公开发布的 skill 大多出自那里。Scientific Computing 簇占 skill 的 7.5%，不足以把受评任务归为某个科学或工程领域的套件，故不指派规范领域。

## Evaluation

- 每个任务有两族量规：指令遵循（是否贴合 skill 中所写的偏好）与目标完成（所产出结果是否正确）。量规条目逐条按 1–10 打分，再按类别归一化到 100 分，总分为加权平均。
- 头条量是 skill delta——同一任务、同一模型下有 skill 与无 skill 两个分数之差。
- 评分采用 LLM-as-judge：所有实验统一由 Claude Code harness 中的 Sonnet 4.6 担任唯一评判者，对照隐藏量规打分，并可查阅求解方的日志。
- **报告。** 用上 skill 带来的相对增益因模型而异，介于 5.5 到 22 分之间；此范围之外的逐模型、逐簇数值为 TODO(reference)。

## Typical Duration

未报告步数或 token 上限。论文把逐场景的金钱成本也作为一个分析维度来报告；具体数字为 TODO(reference)。

## Main Contribution

一套面向作者、可复用的单 skill 评估方法学——而非一个固定基准——外加一份公开的生成式可执行任务与量规数据集，使跨模型的 skill 评估得以复现。

## Key Design Ideas

- 任务与量规都从 skill 自身的内容派生，因此评估瞄准的正是该 skill 声称能做的事。
- 设有显式的环境搭建阶段来解决执行依赖，并把依赖归入一组固定的类别。
- 一个校验 agent 负责检查可执行性、一致性，以及量规有没有泄漏进任务描述。
- 把指令遵循与目标完成分开，从而暴露出那种「任务做成了、却无视 skill 规定流程」的模型。
- 以同一批任务上配对的有 skill / 无 skill 运行作为测量单位。

## Strengths

- 规模：约 500 个 skill、1,000 个任务、19 种 agent–模型配置，兼含闭源与开源模型。
- 双量规的切分让一种具体而本来看不见的失败模式变得可测——把任务的字面要求做到了，却把 skill 撇在一边。
- 生成出的任务与量规数据集已公开发布。

## Limitations

- 有 skill 的条件会向 agent 挑明这个 skill 与任务相关；而真实使用中，skill 可能装了却从未被选用。
- 评估依赖单一评判模型（Sonnet 4.6），作者也把评判偏差列为一项顾虑，尤其是在审美或风格类的标准上。
- 数据集偏向软件工程领域。
- 环境难以复现的 skill（数据库、MCP 服务器、多轮交互、需预置状态）被过滤掉，因而排除了真实世界 skill 中不小的一块。
- Repository note: 该框架本身没有简短名称，故卡片以截短标题作为 slug 归档。

## Related Works

- [Skill-Use](./skill-use.md) — 同样区分 skill 使用中的触发与遵从等侧面，但基于人工精选的固定套件而非生成任务。
- [SkillAudit](./skillaudit.md) — 同样从 skill 包出发生成逐 skill 的评估，另外还加上了成本与安全维度。
- [SkillEvolBench](./skillevolbench.md) — 评估的是 skill 能否从经验中形成，而非一个已写好的 skill 价值几何。
- [SkillSV](./skillsv.md) — 把一个 skill 测得的增益归因到它的内部单元。
