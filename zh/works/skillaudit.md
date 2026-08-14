# SkillAudit (2026)

> [English](../../works/skillaudit.md) | **简体中文**

## Overview

SkillAudit 是一套端到端的评估框架：输入任意一个 agent skill 包，自动产出一份涵盖效用、效率/成本与安全的多维部署报告——任务不再取自固定套件，而是由 skill 工件本身生成。

## Topics

- [Skill Hierarchy](../topics/skill_hierarchy.md)
- [Resource-aware Evaluation](../topics/resource_aware_evaluation.md)

## Activities

N/A — 面向通用 agent skill 的评估方法学，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.22613>
- **Code:** <https://github.com/SkillAudit/skillaudit>
- **Project:** <https://skillaudit.github.io/>
- **Venue:** arXiv preprint, 2026

## Summary

框架的立论是：固定套件会把 skill 的边际贡献与骨干模型自身的强弱混为一谈，而当任务落在 skill 的既定范围之外时，又看不出这个 skill 的价值。为此，SkillAudit 直接从 skill 包生成能力对齐的任务，在隔离沙箱中运行以收集执行证据，再把规则检查与 LLM 判定结合起来，产出可稽核的逐 skill 报告。效用与效率建立在基线对照原则之上——带 skill 与不带 skill 两次运行的指令、输入、环境与评判标准完全一致；安全则采用两段式范式：先做静态语义分析，再做动态运行时验证。

## Tasks

任务是逐 skill 生成的，而非从套件中抽取。每个受审 skill 得到三个代表性场景，每个场景再编译成一对配对的效用任务（带 skill 与不带 skill）；识别出的每个风险探针另外生成一个带 skill 的风险任务。论文报告的这次运行在 Codex / GPT-5.4 配置下保留了 643 个有效场景。受审语料是从公开 skill 仓库收集的 226 个排名靠前的真实 skill 包，横跨 23 个职业品类。

## Domains

来自公开 skill 市场、横跨 23 个职业品类的通用 agent skill 包。不针对任何规范的科学或工程领域；受评对象是 skill 工件本身，而非某个领域任务。

## Evaluation

- **效用：** 配对的带 skill 与不带 skill 两次运行之间的通过率增益（PRG）。
- **效率/成本：** Efficiency Gain（agent 执行时间的相对节省）与 Cost Gain（有效输入 token 的相对节省），各自截断到 [-1, 1]，再合成 Efficiency-Cost Gain（ECG）。
- **安全：** 由静态与动态发现按置信度加权扣分汇总而成、取值落在 [10, 100] 的分数，分档为 Pass（100）、Caution（80–99）、Risky（<80）。
- **报告。** 226 个 skill 中有 17 个（7.5%）被标为 Risky；在 Codex / GPT-5.4 配置下，静态扫描器在这 226 个 skill 上共产出 83 条高危、59 条中危与 99 条低危发现。
- 效用与效率使用六种 agent–模型配置（Codex/GPT-5.4、Codex/GPT-5.1、Claude Code/Sonnet 4.6、Claude Code/Sonnet 4、OpenCode/GPT-5.4、OpenCode/Sonnet 4.6）；安全在其中三种上评估。

## Typical Duration

N/A — 未报告逐任务的步数或 token 上限；执行时间是作为结果来测量的（Efficiency Gain），而不是作为预算强加的。

## Main Contribution

把 skill 评估的问法从「这套任务套件能打多少分」改成「这个具体的 skill 值不值得部署」，并配上一条自动化流水线，把一个 skill 包变成它自己的评估，同时报告效用、成本与安全。

## Key Design Ideas

- 任务由 skill 自带的文档与打包内容合成，因此覆盖面跟着 skill 声明的适用范围走，而不是跟着固定套件走。
- 配对的带 skill / 不带 skill 任务，把 skill 的边际贡献从骨干模型的强弱中剥离出来。
- 基于 Docker 的隔离沙箱负责收集执行证据，证据随后交由判定，而不是径直采信。
- 两段式安全检测把静态语义分析与动态运行时验证配对，声明的行为与观察到的行为都要过一遍。
- 以浏览器扩展的形式交付，让审计结果出现在发现 skill 的那一刻——也正是真正做采纳决策的时刻。

## Strengths

- 把成本与安全和效用并列为一等报告维度，而不是当作事后统计。
- 在生态规模上应用于真实发布的 skill，给出了高风险包占比的具体数字。
- 中间轨迹与评估工件开源，单次审计可供检视。

## Limitations

- 作者指出只覆盖了 226 个公开 skill，agent–模型配置也只是一小组。
- 每种条件只跑一次配对运行，因而未能刻画运行间的方差。
- 安全检查只限于扫描器与探针覆盖到的模式，对未覆盖的风险无从置评。
- Repository note: 生成式任务流水线意味着，对两个不同 skill 的审计并非在可比任务上打分；逐 skill 的效用数字是把该 skill 与它自己的无 skill 基线相比，而不是与其他 skill 相比。

## Related Works

- [SkillSV](./skillsv.md) — 同样追问一个 skill 值多少，但把价值归因到内部单元，而非端到端地审计它。
- [Skill-Use](./skill-use.md) — 在固定的真实 skill 套件上评估 agent，正是 SkillAudit 所反对的范式。
- [SkillEvolBench](./skillevolbench.md) — 关心的是 skill 能否从经验中形成；SkillAudit 关心的是一个已有 skill 该不该采用。
- [HarnessOpt-Bench](./harnessopt-bench.md) — 同样在受信执行环境中计量资源消耗，同时为 agent 的外围工件打分。
