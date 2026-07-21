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

369 个真实计算机任务，涉及真实 web 与桌面应用、操作系统文件 I/O 与多应用工作流。

## Domains

跨操作系统的开放式真实计算机使用：Ubuntu、Windows 与 macOS。

## Evaluation

- 每个任务包含详细的初始状态设置配置与自定义的基于执行的评估脚本，以实现可靠、可复现的评估。
- 报告：人类完成超过 72.36% 的任务；最佳模型达 12.24%。

## Typical Duration

每个任务为开放式的多应用工作流。单任务的步数 / 时间预算：TODO(reference)——摘要未说明。

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

- Repository note: 单任务时长与步数预算在摘要中未说明，标注为 `TODO(reference)`。

## Related Works

- [WebArena](./webarena.md) — 同为交互式、以执行评估的环境，但仅限网站而非整个操作系统。
- [GAIA](./gaia.md) — 同样评估通用助手能力，但以答案正确性而非在计算机环境内执行。
