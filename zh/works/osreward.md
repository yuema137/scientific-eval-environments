# OSReward (2026)

> [English](../../works/osreward.md) | **简体中文**

## Overview

OSReward 是评估跨平台 computer-use 奖励模型——对 computer-using agent 轨迹做评判的视觉语言评判者——的标准化 benchmark，随之发布带推理标注的轨迹评判语料 OS-Shepherd-100K 与训练好的 OS-Shepherd 奖励模型（9B 与 35B）。

## Topics

- [Credit Assignment](../topics/credit_assignment.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.28609>
- **Venue:** arXiv preprint (work in progress), 2026

## Summary

OSReward 通过对来自多平台、多 agent backbone 的轨迹做多阶段人工标注来确立真值判定，并发现最先进模型评判者存在系统性宽松偏差。它提供三个变体——主 benchmark、面向疑难案例的 OSReward-Hard、面向细粒度效率与对齐评分的 OSReward-Multi——外加 OS-Shepherd-100K 语料与开源奖励模型，后者能以约三十到六十分之一的成本达到商业评判者的水平。

## Tasks

跨平台的多样 computer-use agent 轨迹，经多阶段人工标注；主 benchmark 外加 OSReward-Hard 与 OSReward-Multi 变体。具体实例数为 TODO(reference)。

## Domains

跨平台 computer-use 轨迹（作为奖励模型的输入被评估，而非科学领域）。

## Evaluation

- 以多阶段人工标注的真值为对照给奖励模型的判定打分。
- OSReward-Hard 分离疑难判定；OSReward-Multi 对细粒度的效率与对齐维度打分。
- **报告。** 最先进模型存在系统性宽松偏差；OS-Shepherd（9B、35B）能以约三十到六十分之一的成本达到前沿商业评判者的水平。

## Typical Duration

N/A——对已记录轨迹的事后评判。

## Main Contribution

为 computer-use 奖励模型确立标准化、以人为锚的评估，并证明开源小评判者能以极低成本达到商业评判者水平。

## Key Design Ideas

- 真值来自跨异构 agent backbone 的多阶段人工标注，使评判者在分布外受测。
- Hard 切分与多维切分把难度与粒度分开。
- 10 万条带推理标注的评判语料使评判者训练可复现。

## Strengths

- 直接度量并点名当前 VLM 评判者的宽松偏差。
- 成本对齐的比较表明，商业评判者的质量能以约三十到六十分之一的成本获得。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- 作者标注该工作仍在进行中。

## Related Works

- [CUARewardBench](./cuarewardbench.md) — 同样以专家标签考察 computer-use 奖励模型；OSReward 增加了跨平台标准化与训练好的开源评判者。
- [AgentRewardBench](./agentrewardbench.md) — 同样对照真值度量轨迹评判者的可靠性，面向 web agent。
- [ToolPRMBench](./toolprmbench.md) — 同样考察步骤级奖励模型，面向工具使用决策步骤。
