# OSWorld (2024)

## Overview

OSWorld 是一个面向多模态 agent 的可扩展真实计算机环境，支持跨 Ubuntu、Windows 与 macOS 的任务设置、基于执行的评估与交互式学习。它提供 369 个真实计算机任务，涵盖 web 与桌面应用、操作系统文件 I/O 与多应用工作流。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2404.07972>
- **Code:** <https://github.com/xlang-ai/OSWorld>

## Summary

OSWorld 针对现有 benchmark 要么缺乏交互环境、要么局限于特定应用或领域、无法反映真实计算机使用多样性的问题。它引入首个此类的、面向多模态 agent 的可扩展真实计算机环境，支持跨多个操作系统的任务设置、基于执行的评估与交互式学习。在 369 个真实计算机任务上，人类完成超过 72.36%，而最佳模型仅达 12.24%。

## Tasks

369 个真实计算机任务。按类别：OS 24、Office（Calc/Impress/Writer）117、Daily（Chrome/VLC/Thunderbird）78、Professional（VS Code/GIMP）49，以及多应用 Workflow 101（27.4%）。其中 30 个为不可完成任务（agent 须正确预测失败）；全套覆盖 302 个不同的初始状态。

## Domains

跨操作系统的开放式真实计算机使用：Ubuntu、Windows 与 macOS。

## Evaluation

- **基于执行的奖励 R ∈ [0, 1]。** 在最后一步给出逐任务奖励——达成记 1、部分达成记 0–1 间的小数、对不可完成任务正确预测失败亦记正分，其余记 0——因此打分并非严格二元，尽管多数任务是通过 / 失败。报告指标为 Success Rate，即全套任务上 R 的均值。
- **逐任务的 JSON 配置驱动四个阶段：**（1）初始状态设置（VM 快照、下载文件、打开应用——任务刻意从中间状态而非干净启动开始）；（2）后处理（如激活窗口、保存文件）；（3）getter，抽取待检查的产物（文件、cookie、无障碍树元素，或经爬虫取实时值）；（4）evaluator 函数，将取回状态与 gold 比较——如对表格区间的 `compare_table`、`is_cookie_deleted`、`check_a11y_tree`。共 134 个人工编写的评估函数（每任务约 2 小时）。
- **报告（表 5）。** 最佳模型 GPT-4（无障碍树输入）总体达 12.24%（OS 20.83%、Office 3.58%、Daily 25.64%、Professional 26.53%、Workflow 2.97%），人类总体 72.36%；多应用 Workflow 任务最难（2.97%）。

## Typical Duration

每任务上限 15 个交互步与 30 分钟 wall-clock。人工操作者每题中位约 112 秒，部分任务可达 900 秒以上。

## Main Contribution

一个面向多模态 agent 的可扩展真实计算机环境，配以逐任务的设置与基于执行的奖励脚本，使跨操作系统的开放式评估可复现。

## Key Design Ideas

- 真实的操作系统环境（Ubuntu、Windows、macOS），而非特定应用的沙盒。
- 逐任务的初始状态设置加自定义的基于执行的评估脚本，保证可复现性。
- 开放式、多应用的任务工作流。
- 既支持交互式学习也支持评估。

## Strengths

- 反映真实、多样的计算机使用，而非单一应用领域。
- 基于执行的逐任务脚本给出可复现、客观的打分。
- 巨大的人–模型差距（72.36% 对 12.24%）预示大量 headroom。

## Limitations

- Repository note: 基于执行的奖励定义在 [0, 1]（允许部分得分），但结果以单一 Success Rate 报告；逐任务的部分得分值未单独列出。

## Related Works

- [WebArena](./webarena.md) — 同为交互式、以执行评估的环境，但仅限网站而非整个操作系统。
- [GAIA](./gaia.md) — 同样评估通用助手能力，但以答案正确性而非在计算机环境内执行。
