# SWE-RPG (2026)

> [English](../../works/a-unified-issue-resolution-benchmark-for-requireme.md) | **简体中文**

## Overview

SWE-RPG 是一个仓库级 issue 解决 benchmark，把可执行的补丁评估与「需求澄清」（Requirement Clarification）和「实现规划」（Implementation Planning）的经验证真值参考配对，从而支持对完整 coding-agent 轨迹做阶段对齐的诊断，而不只是通过/失败式打分。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities


N/A — 通用仓库级软件工程 issue 解决 benchmark（SWE-RPG）；作为一般应用软件工程被排除。

## Links

- **Paper:** https://arxiv.org/abs/2608.09072
- **Venue:** arXiv 预印本（cs.SE；cs.AI），2026 年

## Summary

既有仓库级编码 benchmark 通常只评估最终补丁是否通过测试，无法刻画一条失败轨迹如何偏离得到正确补丁所需的需求与实现过程。SWE-RPG 在可执行补丁评估之外，为两个上游阶段补充了中间真值参考（GT）——恢复显式与隐式需求（需求澄清）以及制定扎根于仓库的实现计划（实现规划）。这些中间 GT 支持对完整轨迹（澄清、规划、代码生成、产物提交）做回溯式、GT 对齐的诊断。该 benchmark 由取自 31 个 Python 与 Java 仓库的 163 个任务构成，并用于评估三个 coding agent 在六个 LLM 后端上的表现。

## Tasks

163 个任务，取自 31 个 Python 与 Java 仓库，含 113 个缺陷修复与 50 个特性新增。每个任务都带一套可执行的评估 harness（fail-to-pass 与 pass-to-pass 测试），外加两个经验证的中间真值参考：

- **需求澄清 GT** —— 从基仓库、issue 与 PR 讨论、开发者补丁及选定测试中派生的问答式信息点，组织在一套实践者引导的六类分类法（C1–C6）下：功能意图、业务语义、技术语境、接口/协议、代码结构/约定，以及数据结构语义。该分类法参考了对十位资深软件工程师的研讨式访谈。合成 agent 以种子示例作为少样本示范生成候选问答对；一个验证 agent 对照仓库、开发者补丁与已验证计划检查每一对，确认其有证据支撑、跨阶段一致，且不泄漏实现细节。
- **实现规划 GT** —— 从原始 issue、基仓库与已合并 PR 中恢复的一串有序模块化步骤。每一步都经功能可复现性验证：一个 coding agent 按该步骤生成补丁，评估器判断它是否与对应的参考子补丁语义等价，未通过的步骤由一个差距分析与消解 agent 修订。

构建流水线中的 agent 组件用 GPT-5.4 实例化。两位作者独立评审了每一条澄清参考与每一份计划，确认其有证据支撑且跨阶段一致。

## Domains

软件与系统工程——在真实 Python 与 Java 软件项目（31 个仓库）中的仓库级缺陷修复与特性新增。

## Evaluation

- **解决率（主结果指标）：** 一个任务只有当其补丁成功应用、所有 fail-to-pass 测试通过且没有任何 pass-to-pass 测试回归时，才算被解决。
- **失败归因：** 一个 LLM judge（GPT-5.6-Sol）把每次失败归到最早偏离的阶段——需求理解、规划、实现或其他；所报告的阶段归因准确率在 50 例样本上为 92%。
- **澄清覆盖率：** 对每次运行，一个 LLM judge（GPT-5.6-Sol）判断轨迹是否覆盖每个 GT 信息点，并按类别/维度计算覆盖率。在 50 例样本上，judge 的覆盖判定与人类共识在 96% 的情形一致。
- **规划覆盖率：** 轨迹对照五个规划维度评估——目标、目标位置、实现思路、约束与验证策略——评估的是语义上的实现职责，而非计划的逐字匹配。

## Typical Duration

TODO(reference) — 所查阅的主要来源未给出逐任务的轨迹长度、wall-clock 时间或 token 预算。

## Main Contribution

一个仓库级 benchmark，把可执行的补丁评估与「需求澄清」和「实现规划」的经验证中间真值参考结合起来，从而支持对完整 coding-agent 轨迹（澄清 → 规划 → 代码生成 → 产物提交）做回溯式、GT 对齐的诊断，而非仅做通过/失败式评估，并配一项定位 coding agent 在何处失败的实证研究。

## Key Design Ideas

- 为每个可执行的 issue 解决任务附上需求与规划阶段的经验证中间真值，使一条轨迹可以对照参考过程被诊断，而不只是对照最终结果。
- 把澄清参考扎根于一套源自实践者、由十位软件工程师访谈得出的六类信息分类法。
- 以功能可复现性验证规划步骤——由每一步重新生成补丁并检查其与参考子补丁的语义等价——而非靠表面的计划匹配。
- 采用「合成 + 验证」的 agentic 构建流水线，显式检查证据支撑、跨阶段一致性与实现细节泄漏，并辅以两位作者的独立人工评审。
- 把评估分解为结果解决率指标，加上 LLM-judge 的阶段归因与逐阶段覆盖率指标，并对照人类共识做校准。

## Strengths

- 超越通过/失败的补丁打分，把失败定位到澄清、规划与实现各阶段（论文）。
- 中间 GT 同时经过自动验证与两位作者的独立人工评审（论文）。
- 基于 judge 的覆盖与归因判定对照人类共识做校准（覆盖 96% 一致；50 例样本上阶段归因准确率 92%）（论文）。
- 覆盖两种语言（Python 与 Java）、31 个仓库，兼含缺陷修复与特性新增（论文）。

## Limitations

- 受评 coding agent 的平均解决率仅为 31.5%，最佳配置（OpenCode–MoonshotAI-Kimi-K3）达到 49.7%（论文）。
- 失败归因与覆盖评估依赖 LLM judge（GPT-5.6-Sol）；虽在样本上对照人类共识做了校准，但这些判断并非确定性验证器（论文）。
- Repository note: 相对真实世界仓库的空间，其规模适中（163 个任务、31 个仓库），且在主要来源中未评估对 Python 与 Java 之外的泛化。

## Related Works

- [SWE-bench Pro Max](./swe-bench-promax.md) — 另一个仓库级 coding-agent issue 解决 benchmark。
