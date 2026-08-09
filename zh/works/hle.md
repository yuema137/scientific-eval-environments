# Humanity's Last Exam (2025)

> [English](../../works/hle.md) | **简体中文**

## Overview

Humanity's Last Exam（HLE）是位于人类知识前沿的多模态 benchmark，定位为同类封闭式学术评测的「最后一份考卷」：2,500 道题目横跨数十个学科——数学、人文与自然科学——由全球领域专家共同出题。它是通用学术 benchmark 而非 agent benchmark（见 Limitations 中的 repository note）。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2501.14249>
- **Project:** <https://lastexam.ai>
- **Publication:** <https://www.nature.com/articles/s41586-025-09962-4>
- **Venue:** Nature, 2025

## Summary

HLE 直面 benchmark 饱和问题——LLM 在 MMLU 等主流套件上已超过 90%——把题目难度推到专家级人类知识的前沿。2,500 道选择与简答题每道都有已知、无歧义、易验证的答案，适合自动判分，却无法通过快速联网检索得到。最先进的 LLM 在 HLE 上准确率与校准度都很低，从而量化了当前模型与专家级人类前沿在封闭式学术问题上的差距。

## Tasks

2,500 道专家出题的选择与简答题，横跨数十个学科，含数学、人文与自然科学；静态问答。

## Domains

横跨数学、人文与自然科学的数十个学科；该 benchmark 刻意追求学科广度，不属于任何单一领域。

## Evaluation

- 对照已知、无歧义的答案自动判分；在准确率之外同时测量校准度。
- **报告。** 最先进的 LLM 在 HLE 上准确率与校准度均低。

## Typical Duration

单题作答；非交互式 agent 设定。

## Main Contribution

一份由全球专家出题的封闭式学术评测天花板：难到重新拉开了提升空间、可自动判分、且从构造上抗检索。

## Key Design Ideas

- 题目必须无歧义、可验证，又不能靠快速联网检索作答。
- 全球专家出题，把难度推到各学科的前沿。
- 校准度与准确率并列报告，前沿上的过度自信本身也被测量。

## Strengths

- 在主流 benchmark 饱和之处重新建立了可测的提升空间。
- 公开发布加自动判分，使前沿比较可复现。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。
- Repository note: HLE 是通用的封闭式学术 benchmark，既非 agent benchmark 也非科学专属；收录于此是因为它是研究级科学 benchmark 用来定位自身难度的前沿参照点。

## Related Works

- [Agents' Last Exam](./agents-last-exam.md) — 名称呼应的 agentic 对应物：长 horizon 职业工作流，而非封闭式问答。
- [CritPt](./critpt.md) — 同样是前沿难度、防猜测的学术评测，专精于研究级物理。
- [GAIA](./gaia.md) — 同样以对抗 benchmark 饱和为出发点，但用需要工具的助手式问题而非专家知识。
