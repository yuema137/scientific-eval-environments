# Agentic Self-Driving Microscopy Benchmarks (2026)

> [English](../../works/agentic-microscopy-benchmarks.md) | **简体中文**

## Overview

一项来自业界（Carl Zeiss Research Microscopy Solutions）的研究，为 agentic 自主（self-driving）显微术配套了 benchmark 与轨迹日志框架，并给出一个元发现：53 个 benchmark 测试、105 种 agent 配置足以支撑资格验证（qualification）、回归测试与诊断——但预测不了在未见任务上的表现。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [实验室与仪器控制](../activities/laboratory_instrument_control.md)

## Links

- **Paper:** <https://arxiv.org/abs/2608.05266>
- **Code:** <https://github.com/natertott/agentic_microscopy_benchmarks_XRM>
- **Venue:** arXiv preprint (cs.AI, cond-mat.mtrl-sci, cs.LG), 2026

## Summary

研究在 53 个显微术 benchmark 测试上共运行 1,949 次、记录 49,109 次 RAG 检索，变量覆盖一、二、三 agent 的图拓扑、五个 LLM 以及 RAG 与上下文参数，并附完整轨迹日志与时延、token 用量、成本、失败模式的比较。核心的否定性结果是：用 agent 架构与测试结果训练的代理模型无法可靠预测 agent 在全新任务上的表现——这套异质测试套件支撑资格验证，却给不出一个与任务无关的全局配置模型。

## Tasks

53 个面向仪器控制 agent 的显微术 benchmark 测试，跑遍 105 种 agent 配置（agent 图拓扑 × 五个 LLM × RAG/上下文参数），合计 1,949 次测试运行。

## Domains

显微术与材料表征仪器（cond-mat.mtrl-sci）；自主运行的科学仪器。

## Evaluation

- 带完整轨迹日志的 benchmark 测试；跨配置比较时延、token 用量、成本与失败模式。
- **报告。** 用 agent 架构与测试结果训练的代理模型无法可靠预测未见任务上的表现；benchmark 可用于资格验证、回归测试、诊断与直接比较。

## Typical Duration

每个测试为仪器控制 agent 运行；单次运行预算为 TODO(reference)。

## Main Contribution

给 agent benchmark 本身敲响的实证警钟：即使在单一领域内建起有充分测量手段的测试套件，也得不出「下一个任务该用哪种 agent 配置」的任务无关模型。

## Key Design Ideas

- 配置空间被系统地探索（拓扑 × 模型 × RAG/上下文），而非逐例尝试。
- 轨迹日志让每次运行可审计、失败模式可归类。
- benchmark 的效度本身被当作实证问题，用代理模型在留出任务上做预测来检验。

## Strengths

- 关于「benchmark 分数能泛化多远」的少见工业级证据（1,949 次运行）。
- 植根于真实仪器控制工作负载，而非合成任务。

## Limitations

- Repository note: 卡片依据 arXiv 摘要与元数据编写（2026 年 8 月）；摘要未陈述的细节有待全文校验。
- Repository note: 论文未给该 benchmark 起专名；本卡片按论文自身表述使用描述性标题。

## Related Works

- [AFMBench](./afmbench.md) — 同样在真实显微仪器上评估 agent，带命名的错误分类。
- [Harness-Bench](./harness-bench.md) — 同样发现测得的能力是配置的属性，而不只是模型的属性。
- [EnvTrace](./envtrace.md) — 同样通过执行轨迹评估仪器控制行为，在同步辐射光束线上。
