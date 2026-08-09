# The Tool Decathlon / Toolathlon (2025)

> [English](../../works/toolathlon.md) | **简体中文**

## Overview

The Tool Decathlon（Toolathlon）是一个面向多样、真实、长 horizon 任务执行的 language agent benchmark：108 个任务覆盖 32 个真实软件应用与 604 个工具，配以真实的初始环境状态，并用严格可验证的、基于状态的评估脚本打分。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

N/A — 通用型 agent 基准，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2510.25726>
- **Project:** <https://toolathlon.xyz/>
- **Code:** <https://github.com/hkust-nlp/toolathlon>
- **Venue:** ICLR 2026

## Summary

Toolathlon 针对的是狭窄或简化的 tool-use benchmark 与需要在众多应用间切换的真实工作流之间的差距。工具来自作者精选并修复或自行实现的 32 个 Model Context Protocol（MCP）server，外加 7 个本地工具包，覆盖日常平台（Google Calendar、Notion、Gmail）与专业平台（Snowflake、Kubernetes、WooCommerce、BigQuery）。与只保证功能真实性但环境状态多样性有限的既有工作不同，环境用来自真实软件的状态初始化（例如有几十名学生的 Canvas 课程、真实的财务表格），并将远程应用与本地容器化的开源替代（用 Poste.io 替代邮件服务、Canvas、Kubernetes、WooCommerce）结合。任务指令刻意写得模糊，以模拟真实用户请求，但真实意图可以从环境状态中确定性地推断出来。

## Tasks

108 个人工采集或编写的任务，覆盖七个类别（Research、Campus、Finance、Tech、Business、Daily、E-commerce），需要与多个应用交互，平均约 20 轮完成。每个任务平均暴露 69.9 个工具（最少 28、最多 128）；108 个任务中有 72 个（67%）从初始化的环境状态出发。任务由作者按三条原则采集——真实用户需求、多应用编排、两阶段的多样性驱动采集——单个任务的实现需 4–6 小时研究生工作量，质量检查由 5–6 位有经验的作者执行，每轮每任务约 5 小时人力。

## Domains

通用软件工作流：教育/课程管理、金融、电商、集群与数据库运维、邮件与日历协调、研究与日常生产力。

## Evaluation

- 每个任务配有一个独特的、人工编写的确定性评估脚本，直接检查最终环境状态——或对照静态 ground-truth 快照做鲁棒匹配，或沿参考执行流程动态获取实时信息（例如 NVIDIA 当前股东数据）。论文明确主张用基于状态的确定性评估取代对轨迹的 LLM-as-judge 打分。
- 每个任务只暴露必要的 MCP server（少于 10 个），但所选 server 内的全部工具都会加载，因此 agent 必须忽略干扰工具；交互上限为 100 轮。
- 指标：三次运行平均的 pass@1（带标准差）、pass@3、pass^3（三条轨迹全部正确）以及平均轮数。
- 执行与评估在独立容器中隔离，支持并行评测——用 10 个并行进程跑完 Claude-4.5-Sonnet 的全部 108 个任务约需 70 分钟。
- 报告结果：最佳模型 Claude-4.5-Sonnet 达到 38.6% ± 2.7 pass@1（pass@3 为 51.9，pass^3 为 20.4），平均 20.2 轮；最佳开源权重模型 DeepSeek-V3.2-Exp 为 20.1% ± 1.2。增加推理强度没有收益（GPT-5 vs. GPT-5-high），且 15–35% 的轨迹会遇到超长工具输出，使多数模型成功率下降。

## Typical Duration

平均约 20 轮的多轮工具调用工作流（上限 100 轮）；按平均执行轮数划分的难度组大致覆盖 4 到 53 轮。

## Main Contribution

一个同时具备应用多样性（32 应用 / 604 工具）、来自真实软件的环境状态初始化、模糊但可确定性验证的任务指令、以及可靠的基于执行的评估的 language-agent benchmark——论文的对比表显示此前没有任何 tool-use benchmark 同时具备这些性质。

## Key Design Ideas

- 工具来自真实的 MCP server，由作者精选修复，而非 mock 实现或模拟 API。
- 真实的初始环境状态，通过容器化远程服务的开源对应物（Poste.io 对应 Gmail、WooCommerce 对应 Shopify）实现可扩展的搭建。
- 模糊任务指令模拟真实用户请求，同时保证真实意图可从环境状态中确定性推断。
- 每任务一个基于状态的确定性评估脚本，涉及实时信息的任务采用动态 ground-truth 生成。
- POMDP 任务形式化，且每任务的工具配置中包含所暴露 MCP server 内的干扰工具。

## Strengths

- 同时具备多样性、真实环境状态、可验证执行、跨应用任务与模糊 prompt——论文将这些维度与 14 个既有 tool-use benchmark 逐一对照。
- 确定性、可复现的打分，不用 LLM judge，对基于实时真实数据的任务也是如此。
- 提升空间充足：最佳模型 pass@1 不足 40%，且 pass@3 / pass^3 的差距把可靠性（一致性）暴露为独立短板。
- Benchmark 与环境完全开源；并行容器化评测的速度足以支撑开发者的反馈循环。

## Limitations

- Repository note: 论文自身的难度分析发现其 Medium 与 Hard 轮数组之间没有显著差距，并把失败部分归因于过早结束任务而非 horizon 长度本身——成功取决于对观察的探索、工具调用错误的处理与长上下文管理。
- Repository note: 平均轮数统计以单一模型（Claude-4-Sonnet）作为复杂度代理测得，因此 horizon 估计依赖于模型。

## Related Works

- [Gaia2](./gaia2.md) — 同样在带 write 动作验证的真实感多应用环境中为 agent 打分，但采用模拟智能手机世界而非真实软件应用。
- [AgentBench](./agentbench.md) — 更早的单一框架多环境 agent 评估；Toolathlon 用经 MCP 工具暴露的真实应用取代了彼此独立的 benchmark 环境。
