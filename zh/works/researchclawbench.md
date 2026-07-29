# ResearchClawBench (2026)

> [English](../../works/researchclawbench.md) | **简体中文**

## Overview

ResearchClawBench 是一个面向端到端自主科学研究的 benchmark，agent 需要仅凭任务描述、相关文献与原始数据，重新发现一篇被隐藏的已发表论文的研究结果。它包含 40 个专家构建的任务，覆盖 10 个科学领域，并依据锚定目标论文科学产物（artifact）的加权多模态 rubric 进行评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.07591>
- **Project:** <https://internscience.github.io/ResearchClawBench-Home/>
- **Code:** <https://github.com/InternScience/ResearchClawBench>

## Summary

ResearchClawBench 针对 AI 编码 agent 端到端自主研究能力难以验证的问题。每个任务以一篇真实已发表论文为基础，提供相关文献与原始数据但隐藏论文本身；专家构建的多模态 rubric 将目标论文的科学产物分解为加权判据，从而在为新发现留出空间的同时对达到目标论文水平的重新发现进行评分。在统一协议下评测的 7 个自主研究 agent 与经轻量级 ResearchHarness 运行的 17 个原生 LLM 中，最强 agent Claude Code 平均得分 21.5，最强 harness LLM Claude-Opus-4.7 平均得分 20.7，LLM frontier 均值仅为 26.5。

## Tasks

40 个任务，每个任务以一篇真实已发表论文为基础，打包提供任务描述、相关文献与原始数据；目标论文在评估期间保持隐藏。专家按六步流程构建任务：筛选问题清晰、数据可得且研究价值高的论文；将核心问题改写为可执行的任务描述；整理相关文献与原始数据；从目标论文的关键科学产物构建 rubric；将材料打包为标准化任务；交叉检查以修正问题并过滤不合适的样本。

## Domains

10 个科学领域：天文、化学、地球、能源、信息、生命、材料、数学、神经科学与物理。

## Evaluation

- **Reference-Anchored Discovery Score (RADS).** 基于 rubric 的 0–100 分度量，50 分表示达到参照水平的科学证据；低于 50 分表示发现潜力不足，高于 50 分表示超越参照的证据。
- **专家构建的多模态 rubric。** 每条 rubric 条目围绕隐藏目标论文中的一个具体科学产物构建，类型为 text 或 image，并给出判据、供 judge 核验的技术关键词以及反映条目重要性的权重；GPT-5.1 依据 rubric 为最终报告评分。
- **附加报告维度。** 在 rubric 之外，报告还沿四个附加维度评估：Comprehensiveness、Depth、Instruction Following 与 Professionalism。
- **错误分类。** 六类失败类型：Experiment Design Mismatch、Evidence Mismatch、Scientific Core Missing、Goal Misalignment、Reliability / Reporting Failure 与 Execution Failure；失败集中于前三类。
- **报告结果。** 最强自主 agent Claude Code（Claude-Opus-4.6）平均得分 21.5；最强 ResearchHarness LLM Claude-Opus-4.7 平均得分 20.7；LLM frontier 均值为 26.5。

## Typical Duration

未规定每任务的步数、token 或 wall-clock 上限；论文以平均任务成本与运行时长同平均 rubric 得分的关系刻画资源使用，并指出 Claude Code 兼具高分、高成本与长运行时间。ResearchHarness 为长程多步任务提供自动上下文压缩，默认在 128k token 时触发。

## Main Contribution

一个以论文为基础的端到端自主科学研究 benchmark，其 Reference-Anchored Discovery Score 依据专家构建的加权 rubric 度量达到目标论文水平的重新发现，同时为新发现留出空间。

## Key Design Ideas

- 任务以真实已发表论文为基础，提供相关文献与原始数据，而目标论文在评估期间保持隐藏。
- 多模态 rubric 以 text 与 image 两类条目锚定目标论文中的具体科学产物，每条附带判据、供 judge 核验的技术关键词与重要性权重。
- 在 0–100 的 RADS 量表上以 50 为参照锚点，区分发现潜力不足与超越参照的证据。
- ResearchHarness——一个带有网络、本地文件与执行工具并支持自动上下文压缩的轻量级 ReAct 式 harness，使原生 LLM 能与完整自主 agent 一同参加评测。

## Strengths

- 在提供输入材料的同时隐藏目标论文，使已发表的研究结果成为具体的重新发现目标，而非开放式的报告题目。
- 统一协议横跨 7 个自主 agent 与 17 个经 harness 运行的 LLM，支持在同一批 40 个任务上直接比较 agent 脚手架与原生模型。
- 六类错误分类将失败定位到具体环节——实验设计、证据与科学核心——而非只报告一个总分。

## Limitations

- Repository note: 评分依赖单一专有 judge（GPT-5.1）解读加权 rubric，得分复现因此绑定于该模型的可用性与行为。
- Repository note: 目标论文均为已发表作品，评估时隐藏论文并不能将其从模型的预训练语料中移除；所述构建流程筛选的是问题清晰度、数据可得性与研究价值，而非发表时间的新近性。

## Related Works

- [NatureBench](./naturebench.md) — 同样从真实已发表论文中提炼任务，但以每篇源论文报告的 state of the art 为评分标准，而非用锚定论文的 rubric 评判完整研究报告。
- [ScienceAgentBench](./scienceagentbench.md) — 同样取材于同行评审论文，但以执行类指标为生成的独立程序评分，而非评判对隐藏目标论文的端到端重新发现。
- [AIRS-Bench](./airs-bench.md) — 同样度量端到端研究能力，但覆盖 20 个源自 state-of-the-art 机器学习论文的任务，而非跨 10 个科学领域、以隐藏论文为目标的 40 个任务。
