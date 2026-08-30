# CPsyExam (2024)

> [English](../../works/cpsyexam.md) | **简体中文**

> **首次公开：** 2024-05-16 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2405.10212)

## Overview

CPsyExam 是用考试题评测 LLM 心理学知识的中文 benchmark：从 22,000 道题的题库中精选出 4,000 道构成 benchmark，沿两条轴组织——心理学知识与案例分析。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2405.10212>
- **Venue:** COLING 2025

## Summary

CPsyExam 把心理学考试题整理成结构化的 LLM benchmark：从 22,000 道题的题库中提炼出 4,000 道、学科覆盖均衡的 benchmark，沿两条轴组织——心理学知识（回忆与理解）与案例分析（把心理学应用到情境）。它在多个粒度上比较开源与 API 型 LLM，把心理学当作知识领域来考，而非测试模型是否具备心理特质。

## Tasks

覆盖心理学各学科的 4,000 道考题（取自 22,000 道题库），分为心理学知识与案例分析两轴；静态问答。

## Domains

神经科学与认知科学——通过中文考试题评估的心理学知识与案例分析。

## Evaluation

- 跨学科与两轴（心理学知识、案例分析）的准确率，在多个粒度上比较各 LLM。
- **报告。** 在多个粒度上比较 LLM；各模型数值结果为 TODO(reference)——摘要未载明。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

一个把回忆与案例应用分开的结构化心理学知识 benchmark——将心理学作为科学领域来测量，区别于「LLM 心理学」这类能力探针文献。

## Key Design Ideas

- 知识/案例分析的划分把事实回忆与应用推理分开。
- 从 22k 提炼到均衡的 4k，保持学科覆盖均衡。
- 考试来源把难度锚定在公认标准上。

## Strengths

- 发表信息经核实（COLING 2025），是较大的专门心理学知识 benchmark 之一。
- 两轴设计让应用推理的短板与回忆分开显现。

## Limitations

- Repository note: 卡片依据 arXiv 摘要编写（2026 年 8 月）；学科数量与各模型结果在正文中（TODO(reference)），arXiv 页面无法确认代码 URL。

## Related Works

- [ConceptPsy](./conceptpsy.md) — 同样是中文心理学知识 benchmark，按概念全面性组织。
- [PsychCounsel-Bench](./psychcounsel-bench.md) — 同样是心理学考试评估，考美国咨询师认证题。
- [MaScQA](./mascqa.md) — 同样是考试来源的领域知识 benchmark，在材料科学。
