# MedHELM (2025)

## Overview

MedHELM 将 Stanford CRFM 的 HELM（Holistic Evaluation of Language Models）扩展到医疗任务。它把由医生共同验证的分类体系、一个覆盖广泛的 benchmark 套件与一种显式与医生评分对齐的 LLM-jury 评估方法结合在一起。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2505.23802>

## Summary

MedHELM 论文指出：临时的医疗 benchmark 无法覆盖临床工作的广度。它提出了一个由医生共同验证的分类体系，与跨 35 个 benchmark 的聚合方案（17 个已有 + 18 个新构造），并引入了一种 LLM-jury 评估方法，同时明确报告其与医生评分的一致性。

## Tasks

121 个任务，组织在由 29 位医生共同验证的分类体系下：5 个大类、22 个子类。

## Domains

医疗 / 临床任务。摘要提到的类别示例包括 Clinical Note Generation、Administration & Workflow。

## Evaluation

- 聚合覆盖 35 个 benchmark（17 个已有 + 18 个新构造）。
- LLM-jury 评估方法。
- 报告的与医生一致性：ICC = 0.47；优于 ROUGE-L、BERTScore 等自动 baseline。
- 测试 9 个 frontier LLM，包括 DeepSeek R1、o3-mini、Claude 3.5 Sonnet。
- 报告的领域范围：Clinical Note Generation 0.73–0.85；Administration & Workflow 0.53–0.63。
- 成本调整后的比较：Claude 3.5 Sonnet 以约 40% 更低的计算成本给出可比结果。

## Typical Duration

按任务评估；摘要未给出具体 horizon。

## Main Contribution

一个由医生共同验证的医疗评估分类体系，配以 35 个 benchmark 的聚合与一种显式测量与医生一致性（ICC = 0.47）的 LLM-jury 评估方法。

## Key Design Ideas

- 医生共同设计的分类：5 大类 → 22 子类 → 121 任务，由 29 位医生参与。
- 覆盖 35 个 benchmark 的聚合评估（17 个已有 + 18 个新构造）。
- LLM-jury 作为主要评分机制，并以医生评分为对齐参考。
- 成本调整后的 frontier 模型比较。

## Strengths

- 分类由医生直接 grounding。
- 广泛的 benchmark 聚合降低了对任意单一评分范式的依赖。
- 显式给出与医生的一致性数值（ICC = 0.47），使 LLM-jury 方法的可靠性可评估。
- 成本调整后的比较揭示了一个独立的实用性维度。

## Limitations

- Repository note: LLM-jury 与医生的一致性只是中等（ICC = 0.47）；基于此方法的排行榜继承了这一可靠性上限。
- Repository note: 领域限定于医学——分类不直接迁移至其他科学领域。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样是科学领域 benchmark，但以覆盖 5 个科学领域的可执行计算工作流为中心，而非医生共同验证的任务分类。
