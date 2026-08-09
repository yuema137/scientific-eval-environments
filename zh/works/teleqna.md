# TeleQnA (2023)

> [English](../../works/teleqna.md) | **简体中文**

## Overview

TeleQnA 是评估大语言模型电信知识的首个 benchmark 数据集：10,000 道选择题，取自标准（3GPP、IEEE）与研究文献；LLM 在通用知识上可与在职电信专业人士比肩，却在复杂的标准类问题上吃力。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2310.15051>
- **Code:** <https://github.com/netop-team/TeleQnA>
- **Venue:** arXiv preprint (cs.IT), 2023

## Summary

TeleQnA 衡量 LLM 是否懂电信：10,000 道选择题，横跨词汇、研究综述、研究论文、标准综述与标准规范五类，取自 3GPP 与 IEEE 标准及研究文献。GPT-3.5 与 GPT-4 与在职电信专业人士对照评测，论文还研究了加入电信上下文如何改变表现。结论呈现两极分化：LLM 在通用电信知识上可与专业人士比肩，却在复杂的标准相关问题上吃力。

## Tasks

10,000 道选择题，分五类（词汇、研究综述、研究论文、标准综述、标准规范）；静态知识问答。

## Domains

电气工程——电信与通信工程知识，以 3GPP/IEEE 标准与研究文献为依据。

## Evaluation

- 选择题准确率，与在职电信专业人士对照，并做上下文增强研究。
- **报告。** LLM 在通用电信知识上与专业人士比肩；在复杂的标准规范问题上吃力。

## Typical Duration

单轮问答；无交互式设定。

## Main Contribution

面向 LLM 的奠基性电信知识 benchmark——配专业人士基线，把前沿短板精确定位在标准规范上。

## Key Design Ideas

- 取材 3GPP/IEEE 标准，把难度锚定在该领域的权威文档上。
- 五个类别把词汇与综述知识同深层标准细节分开。
- 专业人士基线把「擅长电信」变成可测量的对比。

## Strengths

- 规模大（10,000），被广泛复用为电信知识的参照 benchmark，公开发布。
- 标准 vs 通用的反差是对电信 LLM 构建者直接有用的发现。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方仓库编写（2026 年 8 月）；arXiv 元数据无发表信息。各类别题数出自仓库而非摘要。
- 原论文仅评测 GPT-3.5/GPT-4；更新的模型未覆盖。

## Related Works

- [MaScQA](./mascqa.md) — 同样是与专业人士对照的专家领域知识问答，在材料科学。
- [ElecBench](./elecbench.md) — 同样是电气领域的 LLM benchmark，考电网运行。
- [SciExplore](./sciexplore.md) — 同样是以标准/文献为依据的信息获取，覆盖更广学科。
