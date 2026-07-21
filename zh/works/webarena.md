# WebArena (2023)

## Overview

WebArena 是一个用于构建与评估自主 agent 的真实、可复现 web 环境。它托管跨四个常见领域的完全功能网站，通过功能正确性评估语言引导的 agent 在长 horizon web 任务上的表现。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2307.13854>
- **Code:** <https://github.com/web-arena-x/webarena>

## Summary

WebArena 主张当前 agent 大多在简化的合成环境中被创建与测试，与真实世界场景脱节。它构建了一个高度真实、可复现的完全功能网站环境，涵盖四个常见领域——电子商务、社交论坛讨论、协作软件开发与内容管理——并评估通过自然语言命令执行多样、长 horizon 任务的 agent。成功以功能正确性判定。表现最佳的基于 GPT-4 的 agent 达到 14.41% 的端到端任务成功率，远低于 78.24% 的人类基准。

## Tasks

以自然语言命令下达的、镜像日常互联网活动的多样、长 horizon web 任务。任务数量：TODO(reference)——摘要未说明。

## Domains

跨四个领域的完全功能网站：电子商务、社交论坛讨论、协作软件开发与内容管理。

## Evaluation

- 功能正确性：以程序方式对照网站的结果状态检查任务完成。
- 报告：最佳的基于 GPT-4 的 agent 达 14.41% 端到端成功率，人类为 78.24%。

## Typical Duration

每个任务为长 horizon 的多步 web 交互。单任务步数预算：TODO(reference)——摘要未说明。

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

- Repository note: 任务数量与各领域分布在摘要中未说明，标注为 `TODO(reference)`。

## Related Works

- [OSWorld](./osworld.md) — 同为交互式、以执行评估的环境，但横跨整个操作系统与桌面应用，而非仅限网站。
- [GAIA](./gaia.md) — 同样需要真实 web 交互，但以答案正确性而非网站功能状态打分。
