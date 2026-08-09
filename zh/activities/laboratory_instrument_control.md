# 实验室与仪器控制

> [English](../../activities/laboratory_instrument_control.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 执行或控制实验系统的能力——实验室机器人、仪器/显微镜/光束线控制、实验自动化，以及其正确性由物理系统行为定义的控制代码。

## Scope

涵盖真实硬件操作，以及明确表征仪器或实验室运行的高保真数字孪生。不含通用软件工具使用，也不含并非实验室或仪器操作的一般机器人操控。

## Task Patterns

这类活动呈现出两种不同的形式。第一种是直接操作真实仪器：agent 通过厂商 API 驱动物理硬件，完成一整套实验流程，其正确性由机器上实际发生的行为来判定。[AFMBench](../works/afmbench.md) 正是这一形式的典型代表，它要求 LLM agent 在真实的 Nanosurf DriveAFM 上完成从实验设计到分析的 100 项任务的物理执行；而 [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md) 则对多种 agent 配置下的 agentic 显微镜控制进行考察，并完整记录运行轨迹。

第二种形式评估的是仪器控制*代码*本身，衡量对象是高保真数字孪生而非真实硬件，代码的含义体现在它随时间推移所表现出的物理行为上。[EnvTrace](../works/envtrace.md) 将候选控制代码运行在同步辐射光束线控制逻辑的数字孪生之上，通过对齐执行轨迹来评判语义等价性，用轨迹层面的比较取代了无状态的单元测试。在这两种形式中，反复被强调的都是与时间和状态相关的正确性，以及由行为定义的成功标准——这些都是静态 QA 或单元测试无法捕捉的。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AFMBench | 2025 | LLM agent 端到端操作一台真实的原子力显微镜 | 通过 Python API 在 Nanosurf DriveAFM 上执行 100 项精选任务，运行 3 次 | 任务完成度；最佳模型整体 65%，文档+分析环节 23.3% | [卡片](../works/afmbench.md) |
| EnvTrace | 2025 | 评估 LLM 生成的光束线仪器控制代码 | 相对同步辐射光束线数字孪生进行轨迹对齐；覆盖 30 多个 LLM | 多维度的功能正确性评分；顶尖模型接近人类水平 | [卡片](../works/envtrace.md) |
| Agentic Self-Driving Microscopy Benchmarks | 2026 | 对 agentic 自动驾驶显微镜控制进行基准测试并记录轨迹日志 | 53 项测试 x 105 种 agent 配置，共 1,949 次运行（Zeiss 研究） | 支持资格认证/回归测试；无法实现与任务无关的配置预测 | [卡片](../works/agentic-microscopy-benchmarks.md) |

## Related Works

- [AFMBench](../works/afmbench.md)
- [EnvTrace](../works/envtrace.md)
- [Agentic Self-Driving Microscopy Benchmarks](../works/agentic-microscopy-benchmarks.md)
