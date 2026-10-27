# DISCERN (2026)

> [English](../../works/discern.md) | **简体中文**

> **首次公开：** 2026-09-27 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.33357)

## Overview

DISCERN 检查研究 agent 在生命科学工作流的三个阶段能否做出可靠判断：审核数据、核查分析、提出假设。每个阶段有各自的任务和分数，某一阶段表现好，不会掩盖另一阶段的失误。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [实验设计与科学发现](../activities/experiment_design_discovery.md)

## Links

- **Paper:** [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](https://arxiv.org/abs/2609.33357)
- **Full text:** <https://arxiv.org/html/2609.33357v1>
- **Project:** <https://discern-benchmark.github.io/discern-website/>（见 arXiv v2 的 comments 字段，2026-10-26）
- **Data:** <https://huggingface.co/datasets/discern-bench-anon/discern-benchmark>
- **Venue:** arXiv 预印本（2026）

## Summary

论文指出，以往的基准通常把分析任务的完成情况和假设生成分开评分。DISCERN 在公开数据集中设置受控问题，同时提供配对的干净对照。agent 漏掉缺陷会扣分，把正常数据判为有问题也会扣分。到了假设阶段，agent 要先说出自己的预期，然后才能看到证据。只有当证据与这一预期冲突时，反事实证据包才会保留下来。agent 在 Level 1、Level 2、Level 3 评测中拿到满分的比例分别只有 60.8%、34.2% 和 0.6%。

## Tasks

共 203 个任务：79 个 Level 1 数据完整性任务（58 种任务类型），102 个 Level 2 分析核查任务（分属 24 个分析类别），以及 22 个 Level 3 假设证据包。Level 1 的问题包括基因组版本不一致和环境 RNA 污染。Level 2 在干净或扰动条件下运行分析，其中埋有数据混杂、工具或流程上的失效方式以及统计陷阱。例如在组蛋白任务中，默认的窄峰设置会把宽的 H3K27me3 区域切碎。22 个证据包中，8 个是证据与预期一致的真实对照，6 个是利用数据中原本就存在的意外关系构建的原生反事实，8 个是改动一个已有充分研究的关系、再重新生成一致统计量的注入反事实。参与排名的模型共八个；Claude Fable 5 因覆盖不完整而单独报告。

## Domains

生命科学，共八个方向：全基因组关联研究、临床变异解读、bulk RNA-seq、单细胞 RNA-seq、CRISPR 扰动筛选、增强子活性、染色质调控，以及蛋白质稳定性与结构。论文将它们归入遗传学、转录组学、调控基因组学、表观基因组学和蛋白质生物物理五个领域。量热和核衰变两个方向单独报告，不计入 203 个任务，也不计入得分。

## Evaluation

- Level 1 依据 agent 的代码、执行输出和报告评分，部分诊断或部分修复可得部分分。遇到干净对照时，只有接受数据才得满分；没有依据的警报、拒收数据或编造缺陷都会扣分。
- Level 2 对四个维度取平均：分析正确性、问题识别、方法应对和结果校准。
- Level 1 和 Level 2 采用确定性评分，并由一个独立的 LLM 验证器复核；两者意见不一致时，由人对照记录下来的证据逐一裁定。
- Level 3 的回答先经过三轮对抗式评审，评审模型为 GLM-4.6、Gemini 3.1 Flash-Lite Preview 和 DeepSeek Reasoner。随后由 LLM judge 按 rubric 给证据忠实度、科学推理和新颖性打分，作者再逐一核验。这里的新颖性指提出了从给定结果中看不出来的实质性想法，并不对照文献检查。放弃作答可得到有上限的部分分，但不得新颖性分。
- 每个方向的综合分是三个 Level 得分的几何平均；Overall Score（0–100）是八个方向综合分的平均值，范围从 39.8（GPT-4.1）到 78.1（GPT-6 Astra）。
- 在 64 次 Level 1 干净对照评测中，只有 19 次（29.7%）正确接受了数据。在提交的 94 个假设中，46.8% 没有得到新颖性分。
- 分数旁边同时报告输入和输出 token、API 调用次数和估算费用，不包括评分和评审过程的开销。token 效率定义为每百万 token 对应的 Overall Score；由于没有记录缓存折扣，美元数字都是上限。

## Typical Duration

未报告实际运行时长。Level 1 和 Level 2 在封闭的 Python 沙箱中运行，执行步数上限为 20，不能联网。Level 3 允许 agent 先走三到六步，然后进行三轮评审。

## Main Contribution

在同一组生命科学方向上，把数据审核、分析核查和假设生成作为不同 Level 分别评分，并用干净对照惩罚过度拒收。

## Key Design Ideas

- 在相同指令下，把受控数据缺陷与配对的干净对照放在一起测试。
- 先让 agent 说出预期，再展示证据；只有证据与预期冲突时才保留反事实证据包。
- 用几何平均合并各 Level，某一 Level 偏弱会直接拉低该方向的综合分。

## Strengths

- 报告失败类型的占比。例如在含有问题的 Level 1 评测中，找错原因的占 21.7%，诊断正确却没有处理的占 7.9%。
- 按论文写明的统计规则（2026-08-24 冻结）报告 token、调用次数和费用。

## Limitations

- 任务有明确边界，各 Level 也是分别构建的，因此不能说明 agent 可以自主完成端到端研究；假设也没有经过实验证实。
- 只覆盖部分生命科学方向。模型可能已经熟悉这些公开数据集或已发表的现象，相关任务之间也共用数据集。
- Level 3 的分数依赖 LLM judge 和作者核验，评分仍有一定不确定性。
- v1 论文说明，在单独的公开发布冻结之前，Hugging Face 仓库和不可变的发布标识都只是占位。
- Repository note: 2026-10-27 查看时，Hugging Face 数据集页面已有完整的数据集说明（任务清单、提示词、模型输出、评分和人工裁定记录），但页面上的数据预览无法加载；项目主页没有链接单独的代码仓库。

## Related Works

- [GeneBench-Pro](./genebench-pro.md) — 在模拟数据上为多阶段基因组分析评分。
- [HeurekaBench](./heurekabench.md) — 依据已发表研究提出开放式单细胞研究问题。
- [BixBench](./bixbench.md) — 评测计算生物学数据分析。
