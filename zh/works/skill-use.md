# Skill-Use (2026)

> [English](../../works/skill-use.md) | **简体中文**

## Overview

Skill-Use 是追问 LLM agent 能否真正在 agentic harness 中使用 skill 的 benchmark：79 个真实 skill、177 个可执行任务，横跨九个领域，任务锚定真实文件并在隔离的 Docker 沙箱中运行。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.04828>
- **Venue:** arXiv preprint (cs.CL), 2026

## Summary

Skill-Use 度量 skill 使用的三个可分离侧面——触发（agent 是否调用相关 skill）、流程遵从（是否忠实执行规定流程）、边界遵守（是否避免被禁止的操作）——合并为 SU 分数，其中执行只有在 skill 被触发后才计分。最强配置的 SU 仅 0.613，触发与流程遵从表现为相互独立的瓶颈，且随 harness 不同而变化。

## Tasks

79 个真实 skill 配 177 个可执行任务，横跨九个领域，任务锚定真实文件，在隔离 Docker 沙箱中执行。

## Domains

九个领域；摘要未逐一列出。

## Evaluation

- **SU 分数**覆盖三个侧面：Trigger（调用相关 skill）、Compliance（忠实遵循规定流程）、Boundary（避免被禁止的操作）；执行仅在触发后计分。
- **报告。** 最强配置的 SU 仅 0.613；触发与流程遵从是相互独立的瓶颈，且随 agent harness 不同而变化。

## Typical Duration

每个 skill–任务对在沙箱中的可执行回合。

## Main Contribution

把 skill 使用分解为触发 / 遵从 / 边界三个侧面并证明它们各自独立失效——这是任何聚合任务成功率都无法揭示的能力画像。

## Key Design Ideas

- 使用真实 skill 与真实文件，而非合成的 skill 描述。
- 以触发为计分门槛，防止给无视 skill 的执行记分。
- 跨 harness 比较表明 skill 使用是模型–harness 对的属性。

## Strengths

- 干净地分开“知道 skill 存在”、“照着做”与“守住边界”。
- 以可执行、沙箱化的验证取代主观判定的遵从度。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。

## Related Works

- [SkillTV-Bench](./skilltv-bench.md) — 同样针对 skill 增强设定，但考察的是评判 skill 使用执行的评判者而非执行的 agent。
- [UniClawBench](./uniclawbench.md) — 同样围绕能力轴组织评估，但在 benchmark 层面而非逐 skill。
- [Harness-Bench](./harness-bench.md) — 同样发现 harness 会实质改变测得能力，面向通用工作流而非 skill 使用。
