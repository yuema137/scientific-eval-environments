# Evaluating Plan Compliance in Autonomous Programming Agents (2026)

> [English](../../works/from-plan-to-action.md) | **简体中文**

> **首次公开：** 2026-04-13 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2604.12147)

## Overview

一项关于编程 agent *计划遵从性*的系统实证分析：被要求遵循任务专属计划的编码 agent 是否真的照做，以及偏离与任务成功之间有何关系。研究分析了四个 LLM、两个 SWE-bench 套件、八种计划变体下的 SWE-agent 轨迹，并提出量化 agent 轨迹对所指示计划忠实程度的指标。论文最初以 "From Plan to Action: How Well Do Agents Follow the Plan?" 发布，后更名为 "Evaluating Plan Compliance in Autonomous Programming Agents"。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

N/A —— 针对编码 agent 轨迹的计划遵从性评估方法学；度量的是遵从性指标，而非某个被评估的科学/研究任务。

## Links

- **Paper:** <https://arxiv.org/abs/2604.12147>
- **Venue:** arXiv preprint (cs.SE)，2026（2026 年 4 月 13 日提交；8 月 7 日修订）
- **Authors:** Shuyang Liu、Saman Dehghan、Jatin Ganhotra、Martin Hirzel、Reyhaneh Jabbarvand（伊利诺伊大学厄巴纳-香槟分校；IBM）

## Summary

编程 agent 通常会拿到一份任务专属计划作指导，但它们在多大程度上遵从此类计划尚未被度量。这项工作对编程 agent 的计划遵从性做了广泛分析，在 SWE-bench Verified 与 SWE-bench Pro 上、八种计划设定下考察了四个 LLM 的 16,991 条 SWE-agent 轨迹。研究报告：在没有明确计划时，agent 会退回到内化的工作流，而这些工作流常常不完整、过拟合或应用不一致；给出标准计划能提升 issue 解决率；周期性的计划提醒可缓解计划违背并提升任务成功率；一份糟糕的计划带来的损害可能比没有计划更大；在早期插入额外的任务相关阶段，若与模型内部的解题策略不吻合，反而会拖累表现。作者将偏离部分归因于计划显著性随轨迹历史增长而衰减，以及 agent 局部条件化、由反馈驱动的动作选择。

## Tasks

通过编辑仓库代码库解决真实世界的 GitHub issue，经由 SWE-agent scaffold 运行。受评实例取自 SWE-bench Verified（全部 500 个实例）与 SWE-bench Pro（266 个 Python 实例）。每次 agent 运行都被指示采用八种计划设定之一，其产生的轨迹按对所指示计划的遵从性评分。

## Domains

软件工程——通过一个自主编码 agent 解决真实开源软件仓库中的 issue。

## Evaluation

- **测试平台。** SWE-agent scaffold，覆盖四个 LLM：GPT-5 mini、DeepSeek-V3、DeepSeek-R1 与 Devstral-small。Benchmark：SWE-bench Verified（500 个实例）与 SWE-bench Pro（266 个 Python 实例）。
- **计划设定（八种）。**（1）默认/标准计划，（2）无计划，（3）移除复现阶段的计划，（4）移除验证阶段的计划，（5）增补回归测试阶段的计划，（6）增补变更摘要阶段的计划，（7）步骤重排，（8）计划提醒（周期性地重新注入计划）。
- **遵从性指标。** Plan Phase Compliance (PPC)、Plan Order Compliance (POC) 与 Plan Phase Fidelity (PPF)；整体遵从性得分报告为三个分量的几何平均。
- **结果指标。** issue 解决成功率（SWE-bench 式的补丁验证，对照仓库测试套件），跨计划设定比较。
- **报告的方向性结论。** 给出标准计划相对无计划提升 issue 解决率；周期性计划提醒减少计划违背并提升成功率；糟糕的计划可将表现压到无计划基线之下；在早期增加任务相关阶段可能拖累表现。具体的按模型成功率为 TODO(reference)。

## Typical Duration

TODO(reference) —— 论文报告了轨迹级分析，但在所查阅材料中未给出每任务的 wall-clock 或步数时长。

## Main Contribution

对编程 agent 的计划遵从性做了广泛、系统的度量——定义计划遵从性指标（PPC、POC、PPF），并用八种计划变体下的 16,991 条 SWE-agent 轨迹，刻画 agent 何时、为何偏离所指示的计划，以及遵从性与任务成功的关系。

## Key Design Ideas

- 把计划遵从性拆解为三个可度量维度——阶段覆盖（PPC）、阶段排序（POC）与逐阶段忠实度（PPF）——以几何平均聚合。
- 沿八种受控设定变动所指示的计划（移除、增补、重排、提醒，以及无计划基线），以隔离计划内容与结构对遵从性和成功率的影响。
- 在两个 SWE-bench 套件上跨四个 LLM 运行同一 scaffold（SWE-agent），从而把计划效应与模型、benchmark 效应分离开。

## Strengths

- 大规模轨迹语料（16,991 条），横跨四个 LLM、两个 benchmark 与八种计划设定。
- 引入显式、分解的计划遵从性指标，而不只是度量终任务成功。

## Limitations

- 局限于 SWE-agent scaffold 与 SWE-bench Verified / SWE-bench Pro 的 issue 解决任务；研究本身未确立向其他 scaffold 或任务类型的泛化。
- Repository note: 首个 arXiv 版本以原标题报告了更大的轨迹数（21,120）；本卡片的数字采用修订版（16,991 条轨迹，八种计划设定）。按模型成功率与确切遵从性得分此处未记录，标记为 TODO(reference)。

## Related Works

- [SWE-bench](./swe-bench.md)
