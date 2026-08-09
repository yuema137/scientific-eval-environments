# WebArena (2023)

> [English](../../works/webarena.md) | **简体中文**

## Overview

WebArena 是一个用于构建与评估自主 agent 的真实、可复现 web 环境。它托管跨四个常见领域的完全功能网站，通过功能正确性评估语言引导的 agent 在长 horizon web 任务上的表现。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2307.13854>
- **Code:** <https://github.com/web-arena-x/webarena>

## Summary

WebArena 主张当前 agent 大多在简化的合成环境中被创建与测试，与真实世界场景脱节。它构建了一个高度真实、可复现的完全功能网站环境，涵盖四个常见领域——电子商务、社交论坛讨论、协作软件开发与内容管理——并评估通过自然语言命令执行多样、长 horizon 任务的 agent。成功以功能正确性判定。表现最佳的基于 GPT-4 的 agent 达到 14.41% 的端到端任务成功率，远低于 78.24% 的人类基准。

## Tasks

来自 241 个模板的 812 个实例化任务意图（平均每个模板实例化 3.3 次），以自然语言命令下达。部分意图被刻意设为不可完成并标注为 N/A——agent 须识别其不可行，而非臆造结果。

## Domains

四个完全功能、自托管的网站——电子商务（OneStopShop/Magento 商城）、内容管理 / 后台站点、社交论坛（Postmill/Reddit 风格）与协作软件开发（GitLab）——外加辅助工具（地图、计算器、便签）与知识资源（Wikipedia、手册）。

## Evaluation

成功由作用于网站结果状态的程序化奖励函数判定，而非 trajectory 匹配，分两类任务：

- **信息检索类** — agent 的文本答案由 `exact_match`（与参照完全一致）、`must_include`（包含所需事实 / 关键词）或 `fuzzy_match`（GPT-4 判定语义等价）打分。
- **站点导航 / 配置类** — 定位器通过数据库查询、站点 API 调用或 JavaScript 元素选择取回与意图相关的关键状态，并在其中核对标注的必需内容（exact / must_include，外加 URL 与元素状态检查）。
- **不可完成任务**也被纳入并标注 N/A；agent 须回答任务不可行，以检验其是否避免臆断。

执行至多允许 **30 次状态转移**，若某动作重复超过三次或连续三次非法动作则提前终止。报告：最佳 GPT-4 配置达 14.41% 端到端成功率（带不可完成提示时为 11.70%），人类为 78.24%（信息检索类 74.68%、导航 / 配置类 81.32%）。

## Typical Duration

长 horizon 的多步 web 交互，每任务上限 30 次状态转移（动作重复或非法时提前停止）。人工研究中，5 名计算机研究生在 170 个抽样任务上平均每题约 110 秒。

## Main Contribution

一个由完全功能真实网站构成的真实、可复现 web 环境，使自主 agent 在长 horizon 任务上得以进行功能正确性评估，而非在简化的合成设定中。

## Key Design Ideas

- 完全功能、自托管的网站，兼顾可复现性与真实性。
- 四个日常 web 领域，覆盖常规任务的广度。
- 基于结果状态的功能正确性评估，而非表层字符串匹配。
- 需要多步导航与操作的长 horizon 任务。

## Strengths

- 通过自托管功能网站获得高真实性与可复现性。
- 功能正确性评分反映真实任务结果。
- 巨大的人–模型差距（78.24% 对 14.41%）给出清晰 headroom。

## Limitations

- Repository note: 论文报告 812 个意图总数，但各网站分布仅以图（Figure 6）呈现，未给出精确的逐站计数；跨站任务作为一类存在，但未给出数量。

## Related Works

- [OSWorld](./osworld.md) — 同为交互式、以执行评估的环境，但横跨整个操作系统与桌面应用，而非仅限网站。
- [GAIA](./gaia.md) — 同样需要真实 web 交互，但以答案正确性而非网站功能状态打分。
