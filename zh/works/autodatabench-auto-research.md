# AutoDataBench (2026)

> [English](../../works/autodatabench-auto-research.md) | **简体中文**

> **首次公开：** 2026-09-30 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.40097)

## Overview

评测自动化 ML 研究 agent 时，通常看的是它改代码、改模型、调超参之后的效果，于是它改进训练数据本身的能力就和其他改动混在一起了。AutoDataBench 固定模型、训练流程和评测，只允许 agent 改数据。三个任务分别是：修复一份被破坏的工具调用数据集，为 embedding 模型构造对比学习样本对，以及编写问答样例来注入训练截止日期之后的知识。agent 改完数据就去训练，看分布内得分，再接着改，最多 20 轮。最后，它最好的 checkpoint 会在一个看不到的分布外测试集上打分。

## Topics

- [Evaluation-Driven Data Curation](../topics/evaluation_driven_data_curation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [建模与预测](../activities/modeling_prediction.md)

## Links

- **Paper:** [AutoDataBench: A Data-centric Testbed for Accelerating Auto Research](https://arxiv.org/abs/2609.40097)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2609.40097v1>
- **Code:** <https://github.com/AutoDataBench/AutoDataBench>
- **Data:** <https://huggingface.co/AutoDataBench>
- **Venue:** arXiv 预印本（cs.CL，2026）
- **同名提示：** 另一篇论文 arXiv:2609.35025 也叫 AutoDataBench；本卡片只对应 arXiv:2609.40097，所以文件名用 `autodatabench-auto-research`。

## Summary

以工具调用任务为例：agent 拿到约 4 万条单轮函数调用样例，来源是 xLAM-function-calling-60k，并被七种破坏算子动过手脚。agent 可以过滤、去重、合成、重新配比，最多选出 1.6 万条，再由固定的 LoRA 流程训练 Qwen2-1.5B-Instruct。每个训练出的 checkpoint 都在 2,000 条分布内样例上按 AST 准确率打分，agent 看到分数后再决定下一轮怎么改。运行结束后，分布内得分最高的 checkpoint 会在看不到的 BFCL 子集上评测。成绩和两条参考线对比：基线（从被破坏的数据池里随机抽 1.6 万条），以及专家参考（在破坏前的数据池上做 schema 校验、去重和按比例抽样）。

## Tasks

三个优化任务，每个都固定基础模型、训练流程和评测：

- **工具调用（诊断与修复）：** Qwen2-1.5B-Instruct 加 LoRA；分布内为 2,000 条样例的宏平均 AST 准确率；分布外为 BFCL 单轮子集（10 类）。
- **检索（数据组织）：** 用 InfoNCE 训练 6 层 MiniLM，样本对取自 RLHN 数据集（超过 81.8 万对），每次试验用 60 万对；分布内为 ArguAna、FEVERHardNegatives、FiQA2018、HotpotQAHardNegatives、SCIDOCS 上的平均 nDCG@10；分布外为 ClimateFEVERHardNegatives、CQADupstackGamingRetrieval、CQADupstackUnixRetrieval、Touche2020Retrieval.v3、TRECCOVID。
- **知识注入（数据构造）：** Talkie 13B，用离线前向 KL 蒸馏；根据 1,000 条截止日期之后的事实，最多构造 1 万条“上下文-问题-答案”样例；分布内为 Novel 准确率，分布外为 1930 年以前知识的 Retention 准确率。

agent 不能逐条手工处理样例。

## Domains

机器学习研究：为工具调用语言模型、文本 embedding 检索模型改进训练数据，以及向语言模型注入知识。

## Evaluation

- **得分：** 训练后得到的分布内和分布外指标绝对值，乘以 100；Overall 是三个任务分布内均值的简单平均。共七个 LLM，每个 LLM 在每个任务上跑三次标准运行（共 63 次）。
- **参考线（Overall；工具 分布内/分布外；检索 分布内/分布外；知识 分布内/分布外）：** 基线 47.98；70.45/55.18；34.38/31.13；39.10/47.84。专家 56.89；81.65/60.23；40.62/34.76；48.40/48.55。
- **agent（Overall）：** Kimi-3 为 60.68，GLM-5.2 为 59.10，GPT-5.6-Sol 为 58.85，Qwen-3.8-Max 为 58.56，Claude-4.7 为 58.31，Qwen-3.7-Max 为 56.80，DeepSeek-V4-Flash 为 55.20。工具任务的分布内均值都在 80.82 到 81.98 之间。检索任务里，GPT-5.6-Sol 分布内第一（40.46），分布外却垫底（26.15）。
- **预测检查：** GPT-5.6-Sol 和 Kimi-3 在每个任务上各做一次开启预测的运行，每次训练评测之前先写下预测分数、不确定区间和理由；在检索任务上，两者的平均绝对误差分别为 0.64 和 1.55 分。
- **轨迹复用：** 把 800 万 token 的 AutoDataBench 轨迹（上采样到 8,000 万，占 50 亿 token 预算的 1.6%）加入 Qwen2.5-Coder-14B 的中期训练，之后做相同的 SFT。结果：MBPP Base 从 85.45 到 86.24，CRUXEval Input 从 72.00 到 74.12，LiveCodeBench v5 从 44.89 到 45.80，SWE-bench Multilingual 从 27.67 到 33.33。

## Typical Duration

每次运行一块 NVIDIA A800 GPU，墙钟时间上限 24 小时，包括 API 调用、数据处理、训练和评测；最多 20 轮训练加评测。

## Main Contribution

一个把 agent 诊断、组织和构造训练数据的能力单独拎出来测的测试平台：固定所有和数据无关的因素，用训练出的模型在分布内反馈和隐藏的分布外测试集上的表现来打分。

## Key Design Ideas

- 每个任务都只改数据；基础模型、训练配方和评测始终不变。
- agent 优化时看的是分布内得分，最终报告的分布外得分对它不可见，所以能看出它有没有对着反馈信号过拟合。
- 基线和专家流程给每个任务的得分划出上下两条参考线。
- 可以要求 agent 在看到每次训练结果之前先做预测。

## Strengths

- 分布内和分布外分开报告，检索任务上的排名反转因此显现出来。
- 专家参考流程给每个任务提供了一个人工设计的锚点。
- 所有分数都来自真实的训练和评测，不依赖任何 judge。

## Limitations

- 只覆盖三个任务。
- 作者说明，轨迹带来的提升和逐轮改进的例子都没有分离出每项改动的因果贡献；被选中的运行也不代表算力用量相同。
- 参考结果没有重复运行的不确定性估计；预测分析每个模型-任务组合只跑了一次。
- Repository note：v1 全文中没有单独的局限性章节。

## Related Works

- [Curation-Bench](./curation-bench.md) — 同样固定模型和训练配方，只让 agent 改变训练数据的选择，对象是视觉语言模型。
- [PostTrainBench](./posttrainbench.md) — agent 对基础模型做后训练，数据只是允许的几种干预之一。
- [MLAgentBench](./mlagentbench.md) — 同样让 agent 围绕目标指标反复改进 ML 流程，但没有把数据单独隔离出来。
