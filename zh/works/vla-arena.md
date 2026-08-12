# VLA-Arena (2025)

> [English](../../works/vla-arena.md) | **简体中文**

## Overview

VLA-Arena 是一个开源 benchmark 与工具链，用于评估视觉-语言-动作（VLA）模型作为通用机器人操作策略的表现，采用一套结构化的任务设计框架，沿三个正交轴调节难度。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型机器人操作（VLA）benchmark；评估的是通用具身控制，而非某项科学或研究活动。

## Links

- **Paper:** https://arxiv.org/abs/2512.22539
- **Project:** https://vla-arena.github.io
- **Code:** https://github.com/PKU-Alignment/VLA-Arena
- **Venue:** ICML 2026 (arXiv preprint, December 2025)

## Summary

VLA-Arena 提出一套结构化的任务设计框架，沿三个正交轴——Task Structure、Language Command、Visual Observation——量化任务难度，使操作任务能以细粒度、可控的难度构建。该 benchmark 报告，其对最新 VLA 的大规模评估揭示了反复出现的局限：以记忆代替泛化、浮于表面的视觉感知、以及对安全约束的忽视。作者还报告，模型排名在难度等级 L0–L2 之间发生反转，并据此认为每个等级都给出非冗余的诊断信息。完整框架、数据集与端到端工具链一并公开以支撑可复现性。

## Tasks

该 benchmark 由 **11 个任务套件、共 170 个任务**组成，按四个维度组织：Safety、Distractor、Extrapolation 与 Long Horizon。GitHub README 报告的划分为 Safety（5 套件、75 个任务）、Distractor（2 套件、30 个任务）、Extrapolation（3 套件、45 个任务）与 Long Horizon（1 套件、20 个任务）。每个套件跨 **三个难度等级（L0–L2）**，微调仅限于 L0，以考察对未见的更难等级的泛化。与任务结构正交，可对任意任务施加 **语言扰动（W0–W4）** 与 **视觉扰动（V0–V4）** 作为诊断探针，意在把稳健的语义 grounding 与浮于表面的模式匹配区分开来。任务套件构建于 RoboSuite、LIBERO 与 VLABench 框架之上（如仓库所致谢）。发布三种微调数据集变体：VLA-Arena-S、VLA-Arena-M 与 VLA-Arena-L。

## Domains

Robotics — 仿真环境中的机器人操作与控制，评估 VLA 模型作为机器人策略的表现。`Repository note:` 一手来源描述的是基于仿真的评估，未报告真实机器人实验。

## Evaluation

评估使用两个主要指标：**Success Rate (SR)** 与 **Cumulative Cost (CC)**。据项目页，Safety 任务同时报告 SR 与 CC，其他任务类别仅报告 SR。发布的框架为多个 VLA 模型提供评估配置，包括 OpenVLA、OpenVLA-OFT、UniVLA、SmolVLA 与 Openpi（`openpi`）。`TODO(reference)` — 论文报告了各模型的精确数值结果，此处未转录。

## Typical Duration

`TODO(reference)` — 一手来源未报告每任务的 wall-clock 时间或步数预算。`Repository note:` Long Horizon 套件（20 个任务）需要较长的多步操作序列，而其他套件由较短的 episode 组成。

## Main Contribution

一个带新颖结构化任务设计框架的 benchmark，把操作难度分解为三个正交轴（Task Structure、Language Command、Visual Observation），从而能系统性地分级任务（L0–L2），并以正交的语言/视觉扰动探针精确测量 VLA 的能力边界与失败模式，随附一套完整的开源工具链发布。

## Key Design Ideas

- 将任务难度分解为三个正交轴（Task Structure、Language Command、Visual Observation），使难度可独立、可诊断地调节。
- 将 170 个任务组织为四个能力维度——Safety、Distractor、Extrapolation 与 Long Horizon。
- 将微调限制在最简单等级（L0），并在更难等级（L1–L2）上测试，以度量泛化而非记忆。
- 将语言（W0–W4）与视觉（V0–V4）扰动作为可施加于任意任务的事后诊断探针。
- 在 Success Rate 之外纳入基于代价的指标（Cumulative Cost），尤其用于 Safety 任务。

## Strengths

- 受控、因子化的难度设计使失败可归因于具体轴（结构、语言或视觉），而非笼统的任务难度（论文）。
- 作者报告，模型排名在 L0–L2 之间的反转表明每个等级贡献非冗余的诊断信号（论文）。
- 开源的端到端工具链、多种规模的微调数据集与排行榜共同支撑可复现性（论文、项目页）。

## Limitations

- `Repository note:` 一手来源描述的是基于仿真的评估，未报告物理机器人部署，因此所审来源并未确立所报发现的 sim-to-real 迁移。
- `TODO(reference)` — 确切的受评模型集合及其数值分数在论文中，但本卡片未转录。

## Related Works

- [CaP-X](./cap-x.md) — 另一个在仿真机器人控制上按难度分层评估 VLA/操作模型的 benchmark。
- [ManipBench](./manipbench.md) — 评估 VLM/VLA 对底层机器人操作的推理。
