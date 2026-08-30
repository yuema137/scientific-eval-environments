# CritPt (2025)

> [English](../../works/critpt.md) | **简体中文**

## Overview

CritPt（Complex Research using Integrated Thinking – Physics Test，读作「critical point」）是含 71 个复合、未发表的研究级物理挑战的 benchmark，可分解为 190 个更简单的检查点任务，由 50 余位活跃物理研究者在 11 个以上子领域中全新创作。

## Topics

- [Benchmark Design, Validity & Contamination](../topics/benchmark_design_validity_contamination.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.26574>
- **Code:** <https://github.com/CritPt-Benchmark/CritPt>
- **Dataset:** <https://huggingface.co/datasets/CritPt-Benchmark/CritPt>
- **Project:** <https://critpt.com>
- **Venue:** arXiv preprint (cs.AI, cond-mat, hep-th, quant-ph), 2025

## Summary

CritPt 模拟入门级别的完整研究项目：每个挑战都未曾发表，并被精心整理成防猜测、可机器验证的答案形式，由一条为高等物理专用输出格式深度定制的自动判分流水线打分。挑战分解出的 190 个检查点任务能定位推理在哪一步失守。基础模型的最高平均准确率仅 5.7%（GPT-5, high），配备编码工具后仅温和升至约 10%。

## Tasks

71 个复合研究挑战外加 190 个分解出的检查点任务，由 50 余位活跃物理研究者创作；答案未发表、防猜测、可机器验证。

## Domains

11 个以上物理子领域：凝聚态、量子物理、原子分子与光物理、天体物理、高能物理、数学物理、统计物理、核物理、非线性动力学、流体力学与生物物理。

## Evaluation

- 为高等物理专用输出格式深度定制的自动判分流水线；答案设计为防猜测且可机器验证。
- **报告。** 基础模型最高平均准确率 5.7%（GPT-5, high）；配备编码工具约 10%。

## Typical Duration

复合研究挑战回合，可选配编码工具；非交互式环境。

## Main Contribution

把评估标准设在未发表的入门研究级问题上，同时保持判分全自动——并展示前沿模型在此收敛到个位数准确率。

## Key Design Ideas

- 未发表、研究者原创的挑战从结构上杜绝了数据污染。
- 防猜测的答案格式堵死了困难 QA 中靠运气得分的通道。
- 「挑战 → 检查点」的分解把失败定位到研究工作流内部，而不只在终点。

## Strengths

- 50 余位活跃研究者按自身工作水平出题。
- 5.7%→10% 的工具差值清晰量化了编码工具在研究级物理上的增益。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。流传的会议录用说法无法从论文 arXiv 页面证实。

## Related Works

- [CMT-Benchmark](./cmt-benchmark.md) — 同样是研究者出题、机器判分的专家级物理，但限于凝聚态理论。
- [PRL-Bench](./prl-bench.md) — 同样是前沿物理研究评估，取材于最新 PRL 论文而非未发表挑战。
- [PhySciBench](./physcibench.md) — 同样是专家整理的物理科学评估，在 deep-research 而非研究入门层级。
