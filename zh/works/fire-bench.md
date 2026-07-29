# FIRE-Bench (2026)

> [English](../../works/fire-bench.md) | **简体中文**

## Overview

FIRE-Bench（Full-cycle Insight Rediscovery Evaluation）是一个 benchmark，要求 agent 在仅获得已发表研究的高层研究问题的情况下，重新发现近期高影响力机器学习研究中确立的、可验证的结论。它包含 40 个完整执行的任务，以及另行发布供社区评估的 60 篇论文。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2602.02905>
- **Project:** <https://firebench.github.io>
- **Code:** <https://github.com/maitrix-org/FIRE-Bench>
- **Venue:** ICML 2026

## Summary

FIRE-Bench 认为，由于新颖发现需要代价高昂的真实世界验证，现有 benchmark 只能退而依赖对生成论文的 LLM-as-judge 评分或单一排行榜指标，两者都只是科学推理的粗糙代理。它转而要求 agent 重新发现既有结论：仅给定来自已发表研究的高层研究问题，agent 必须独立设计实验、运行实验并得出有证据支撑的结论，再对照该研究记录在案的结论计分。在以前沿模型为 backbone 的最先进 coding agent 中，即便最强者也只能取得有限的重发现成功率（低于 50 F1），且运行间方差高，并在实验设计、执行与循证推理中反复失败。

## Tasks

40 个完整执行的任务——核心集 30 个，每篇论文构造一个，来自 2024 与 2025 年发表于 ICLR、ICML 与 NeurIPS 的 LLM 行为实证研究，另加 10 个任务的跨领域扩展（5 篇来自计算机视觉与视觉–语言建模，5 篇来自神经网络分析）——以及另行发布供社区评估的 60 篇论文解析池。源论文须满足三项标准——开放输入（仅使用公开可得的数据集与模型）、轻量计算执行（可在一块 80GB A100 GPU 上于 24 小时内运行）与非平凡、可验证的洞见——最终候选由两位作者人工审核。每篇论文由 gpt-5 Pro 在 temperature 0 下解析为研究问题树：根节点是研究问题，中间节点是子问题，叶节点是锚定于论文图表结果的实验；任务 prompt 取目标叶节点的父节点，向 agent 给出研究问题而隐去原始实验设计。

## Domains

机器学习研究：执行核心集为 LLM 行为分析；扩展集为计算机视觉、视觉–语言建模与神经网络分析；社区论文池为代码生成、RAG、agent 与工具使用、安全与对齐及多语言建模。

## Evaluation

- **Claim 级 precision、recall 与 F1。** 每个 agent 的最终结论与 ground-truth 文本各自被分解为原子化、可验证的 claim 集合，遵循 RAGChecker；语义蕴含分类器对其进行匹配，将无 ground truth 支持的生成 claim 记为假阳性、未被匹配的 ground-truth claim 记为假阴性。
- **Judge 可靠性。** 同一 judge 模型（gpt-5.2）用于所有 agent；在 33% 的参考实例上进行的人工校验得到 precision 0.95、recall 0.86 与 F1 0.89。
- **诊断性错误框架。** 失败经由 16 类错误类别归因到四个研究工作流阶段——Research Planning、Implementation、Experimental Execution 与 Conclusion Formation。
- **报告结果。** 在核心 30 任务集上，Claude Code (Sonnet-4) 达到 F1 46.7±23.4，Codex (gpt-5-medium) 为 41.9±25.4，OpenHands (gpt-5) 为 37.9±23.0，OpenHands (o4-mini) 为 31.9±17.6；失败以 Research Planning 与 Conclusion Formation 为主，Codex 以合计 $2.21 的 API 成本取得该分数，而 Claude Code 为 $12.67。

## Typical Duration

未设置硬性运行时长上限，多数运行在一小时内完成；每个任务–agent 对执行三次，报告均值与标准差。未说明每任务的 step 或 token 预算；任务在构造阶段即被筛选为可在一块 80GB A100 GPU 上于 24 小时内运行，agent 在配备八块此类 GPU 的节点上的 CLI 沙箱中执行。

## Main Contribution

一种面向研究 agent 的评估范式，融合全周期执行、洞见驱动评估、有依据的参照计分与方法学探索，并以重新发现已发表、经验证的结论作为计分目标。

## Key Design Ideas

- 研究问题树抽象：将每篇论文解析为根研究问题、中间子问题与锚定于论文图表结果的叶实验，由 gpt-5 Pro 在 temperature 0 下自动提取。
- 受约束的重发现 prompt：取目标叶节点的父节点并隐去原始设计，使任务从直接复现转向探索。
- 遵循 RAGChecker 的 claim 中心计分，由单一固定的 gpt-5.2 提取器与蕴含 judge 应用于每个 agent。
- 以 living benchmark 形式发布：版本化增补、公开排行榜、社区提交表单，以及 40 个执行任务之外的 60 篇论文解析池。

## Strengths

- Ground truth 锚定于经同行评审发表的结论，而非对新颖产出的自由形式 LLM 评判，使重发现成功与否可被客观核验。
- 每个任务–agent 对运行三次并报告标准差，直接暴露运行间方差。
- 按任务难度与模型知识截止日期分层的污染分析未发现系统性污染的强证据。

## Limitations

- Repository note: 执行核心集仅覆盖 LLM 行为实证分析论文，且轻量计算筛选将参考实验限制在单块 80GB A100 GPU 的 24 小时之内，因此对近期轻量计算机器学习研究之外的重发现未被测试。
- Repository note: Claim 提取与蕴含判定均运行在单一固定模型（gpt-5.2）上，所有分数因此继承该 judge 的误差特性；论文自身的人工校验将该协议定在 F1 0.89。

## Related Works

- [ScienceAgentBench](./scienceagentbench.md) — 同样从同行评审出版物构造任务，但每个任务以单个自包含 Python 程序为目标，而非从问题到循证结论的完整研究循环。
- [Aviary](./aviary.md) — 同样在科学任务上评估 language agent，但采用带 terminal reward 的交互式 gymnasium 环境，而非对已发表结论的开放式重发现。