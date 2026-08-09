# PsychCounsel-Bench (2025)

> [English](../../works/psychcounsel-bench.md) | **简体中文**

## Overview

PsychCounsel-Bench 用专业认证题评测 LLM 的心理学水平：约 2,252 道来自美国国家咨询师认证考试（NCE）的单选题，先进模型能越过约 70% 的及格线，而较小的开源模型则远远不及。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2510.01611>
- **Code:** <https://github.com/cloversjtu/PsychCounsel-Bench>
- **Venue:** arXiv preprint (cs.AI), 2025

## Summary

PsychCounsel-Bench 把心理学评估锚定在专业标准上：约 2,252 道精选自美国国家咨询师认证考试（NCE）的单选题，对照该考试约 70% 的及格线评分。先进模型——GPT-4o、Llama3.3-70B、Gemma3-27B——轻松过线，而较小的开源模型（Qwen2.5-7B、Mistral-7B）远远不及，使该 benchmark 成为一个以及格/不及格为锚的专业心理学知识度量。

## Tasks

约 2,252 道来自美国国家咨询师认证考试的单选题；静态问答，对照约 70% 及格线评分。

## Domains

神经科学与认知科学——专业咨询心理学知识，取自一项认证考试。

## Evaluation

- 对照 NCE 约 70% 及格线的准确率，覆盖各参评模型。
- **报告。** GPT-4o、Llama3.3-70B、Gemma3-27B 越过及格线；Qwen2.5-7B、Mistral-7B 远远不及。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

把心理学知识评估锚定在真实的专业认证标准上，给出该领域随意设定的准确率分数所缺的及格/不及格参照。

## Key Design Ideas

- 认证考试同时提供题目与权威的及格线。
- 单选题形式使评分客观、无需 judge。
- 先进与小模型的分野定位出专业能力从何处涌现。

## Strengths

- 以专业标准为根基，且在 GitHub 公开发布。
- 70% 及格线这一锚点使结果超越相对排名而可解释。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息，各模型数值分数在正文中。

## Related Works

- [CPsyExam](./cpsyexam.md) — 同样是心理学考试评估，考中文考试并带案例分析轴。
- [ConceptPsy](./conceptpsy.md) — 同样是心理学知识评估，处于概念粒度。
- [MedHELM](./medhelm.md) — 同样是以专业标准的临床评估，覆盖广泛的医学分类。
