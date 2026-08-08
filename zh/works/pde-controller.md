# PDE-Controller (2025)

> [English](../../works/pde-controller.md) | **简体中文**

## Overview

PDE-Controller 把 LLM 引入 PDE 控制的自动形式化与推理：把非正式的自然语言指令转化为形式规格（信号时序逻辑 STL），再通过推理与规划提升热方程与波动方程系统的控制效用。其数据集——人工撰写案例加 200 万合成样本——与评估指标构成本卡片记录的 benchmark 部分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Links

- **Paper:** <https://arxiv.org/abs/2502.00963>
- **Code:** <https://github.com/delta-lab-ai/pde-controller>
- **Dataset:** <https://huggingface.co/datasets/delta-lab-ai/pde-controller>
- **Project:** <https://pde-controller.github.io/>
- **Venue:** ICML 2025（据官方项目页）

## Summary

PDE 控制问的不是「解是什么」，而是「什么输入能让系统按规格行事」。论文搭起完整管线——Translator 做自然语言到 STL 的自动形式化，Controller 提出 STL 子目标，Coder 产出可执行程序——并为评估发布人工撰写案例与 200 万合成样本，配推理、自动形式化与程序合成三方面的新指标，报告 PDE 控制效用增益最高提升 62%。

## Tasks

热方程与波动方程系统 PDE 控制的自动形式化、推理与程序合成任务；人工撰写案例加 200 万合成样本。

## Domains

应用数学：信号时序逻辑规格下对 PDE 支配系统（热方程与波动方程）的控制。

## Evaluation

- 覆盖推理、自动形式化与程序合成的指标；所得 PDE 控制的效用增益；指标定义为 TODO(reference)。
- **报告。** PDE 控制效用增益最高提升 62%。

## Typical Duration

每条指令为「形式化-规划-合成」管线；非交互式环境。

## Main Contribution

为 LLM 驱动的 PDE 控制建立数据集与指标——评估模型能否从非正式意图走到对物理系统形式化规格下的可执行控制。

## Key Design Ideas

- 以 STL 为中间表示，使控制意图可被形式化检验。
- 效用增益给控制结果打分，而不是给计划的文字打分。
- 合成规模（200 万）与人工撰写案例并存以保效度。

## Strengths

- 本仓库记录的唯一面向 LLM 的 PDE 控制评估资源。
- ICML 录用，代码与数据开源。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与官方项目材料编写（2026 年 8 月）；此外的细节有待全文校验。ICML 2025 的 venue 信息来自官方项目页；arXiv 元数据未载明。
- Repository note: PDE-Controller 框架（Translator/Controller/Coder，经 RLHF 训练）是论文的头号贡献，超出本仓库范围；本卡片记录其数据集与评估。

## Related Works

- [Lean4Physics](./lean4physics.md) — 同样以自动形式化为中心的物理评估，目标是证明助手而非时序逻辑。
- [CodePDE](./codepde.md) — 同样是面向 PDE 系统的 LLM 代码生成，用于求解而非控制。
- [MaD Physics](./mad-physics.md) — 同样与 PDE 支配的模拟系统交互，目的为发现而非控制。
