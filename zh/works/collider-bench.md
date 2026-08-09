# Collider-Bench (2026)

> [English](../../works/collider-bench.md) | **简体中文**

## Overview

Collider-Bench 是一个 benchmark，评估 LLM agent 能否仅凭公开论文和开放科学软件复现大型强子对撞机（LHC）的实验分析。首个版本包含取自 4 项 CMS 超对称搜索的 10 个 Simulation 任务，在带有公开对撞机模拟软件栈的容器化沙盒中运行，并以对照隐藏参考产额的连续直方图保真度评分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [模拟与科学计算](../activities/simulation_scientific_computing.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)
- [研究复现与重复](../activities/research_reproduction_replication.md)

## Links

- **Paper:** <https://arxiv.org/abs/2605.13950>
- **Code:** <https://github.com/dfaroughy/Collider-Bench>

## Summary

Collider-Bench 针对的空白是：现有长程 tool-use benchmark 很少刻画真实科学工作的复杂性与细微之处——公开工具链只能近似 LHC 实验合作组内部使用的软件，已发表论文又不可避免地省略了忠实重建所需的实现细节，因此 agent 必须依靠物理推理、领域知识和反复试错来填补缺口。每个任务要求 agent 将一项已发表分析转化为可执行的模拟–筛选（simulation-and-selection）流水线，并提交指定信号区域内的预测对撞事例产额，以无需手写 rubric 的直方图指标给出连续保真度得分，辅以按任务的计算成本报告和对代码库与完整会话轨迹的 LLM judge 审查。在由六个通用 coding agent 构成的能力阶梯上，平均而言没有任何 agent 能稳定超过物理学家在环（physicist-in-the-loop）方案。

## Tasks

10 个主要 Simulation 任务取自 4 项 13 TeV、积分亮度 35.9 fb⁻¹ 的 CMS 超对称搜索（CMS-SUS-16-034、CMS-SUS-16-046、CMS-SUS-16-047、CMS-SUS-16-051），每个任务固定一篇目标搜索论文、一个信号基准点、一个目标可观测量或信号区域以及一个固定输出模板；次级 Shape 任务套件去掉预测绝对事例产额的要求，难度依据物理学家在环实验由易到难分级。agent 必须阅读论文，通过公开模拟软件栈（MadGraph5、Pythia 8.313、Delphes 3.5.0，并以 Prospino 2.1 计算截面）生成信号事例，实现已发表的事例筛选，并提交预测信号产额的分箱直方图，连同分析代码、模拟配置和一份简短的方法报告。每个任务都先由领域专家借助 agent 通过同一工具链解出，证明公开软件栈能够复现已发表目标；作者说明还有至少一个数量级更多的任务可供后续版本加入。

## Domains

实验粒子物理：在大型强子对撞机上重铸（recasting）CMS 超对称搜索（简化模型信号拓扑）。

## Evaluation

- **Relative L² distance.** 主保真度指标：预测直方图与隐藏参考直方图之间的分箱级差异，按参考直方图归一化，使高产额分箱贡献更大；配套的产额归一化误差与形状–归一化分解用于区分事例筛选错误与绝对事例率错误。
- **Thresholded accuracy.** 当一次运行的 relative L² 误差低于容差 τ = 0.33 时记为通过，该阈值取物理学家在环 baseline 在全任务集上的最差 relative L² 误差——这是一个刻意宽松的判据，agent 只有追平或超过最弱的受监督复现才算通过。
- **LLM provenance judge.** Claude-Opus-4.6 检查 agent 的完整工作区与执行轨迹，将每次运行标记为 Passed、Failed 或 Fabricated，其中伪造涵盖手写回退数组、代理形状生成器、编造的效率以及从公开来源抄录的数值；judge 不给出数值得分。
- **Cost and efficiency.** API 成本、token 用量和 wall-clock 时间作为独立的效率指标报告，不折入保真度得分，将科学准确性与推理成本视为 agent 性能的两条独立轴。
- **Reported.** 六个系统——Claude Code（Opus 4.7、Sonnet 4.6、Haiku 4.5）、Codex CLI（GPT-5.5、GPT-5.4-mini）与 ForgeCode（DeepSeek-V4）——每任务各运行三次：agent 沿能力阶梯提升并形成清晰的成本–性能前沿，但即使最强系统也只通过部分任务，平均而言没有任何 agent 能稳定超过物理学家在环方案；在 364 次受审运行中 provenance judge 给出 Passed 87%、Failed 6%、Fabricated 6%，其中 Haiku 4.5 占伪造提交的多数。

## Typical Duration

每任务 2.5 小时 wall-clock 预算，以单次自主会话、最大推理强度运行，并可使用 128 个 AMD EPYC 7763 CPU 核心处理模拟负载。每个 Simulation 任务的平均运行时间介于 0.299 h（Haiku 4.5）与 1.706 h（DeepSeek-V4）之间，按 2026 年春季标价的平均 API 成本介于 $0.89（DeepSeek-V4）与 $14.21（Opus 4.7）之间。

## Main Contribution

一个将 LHC 重铸——即仅凭公开论文和开放模拟软件端到端复现已发表对撞机搜索——形式化为长程 agent 任务的 benchmark，以对照隐藏参考产额的连续直方图保真度评分，并由 LLM provenance judge 审计。

## Key Design Ideas

- 任务锚定于公开信息不足以唯一确定正确解的已发表 LHC 搜索，迫使 agent 通过物理推理和反复试错弥补合作组内部软件与被省略的实现细节留下的缺口。
- 隐藏参考产额与评估代码不进入 agent 工作区，将公开的问题规范与私有的评分目标分离，防止任务退化为从图、表或公开记录中检索信息。
- 以物理动机的连续评分——relative L² 保真度加形状–归一化分解——取代手写 rubric，并将通过阈值校准到最差的物理学家在环复现。
- 沙盒之外的 LLM provenance judge 审计提交数值是否可追溯到实际执行的模拟，而非编造的缩放因子或从文献抄录的数值。

## Strengths

- 每个任务都先由领域专家通过同一公开工具链解出，因此失败反映的是 agent 的局限，而非目标本身不可复现。
- 带物理学家校准通过阈值的连续保真度得分，在真正欠定的科学工作上给出分级信号，无需手写 rubric。
- 将数值评分与 provenance 审计分离，能捕捉仅凭保真度得分便会得到承认的伪造提交。

## Limitations

- Repository note: 首个版本仅含来自 4 项 CMS 超对称搜索、单一质心能量下的 10 个 Simulation 任务——作者声明的数量级任务扩充以及超出 SUSY 简化模型搜索的覆盖仍属未来版本。
- Repository note: 通过阈值与难度分级均来自单一的物理学家在环工作流（领域专家监督下的 Claude Code 加 Opus 4.7），因此人类参照是一次受监督复现，而非独立的专家群体。

## Related Works

- [Terminal-Bench Science](./terminal-bench-science.md) — 同样在容器化环境中评估 agent 的自然科学计算工作流，但以确定性 pytest 检查验证，而非对照已发表结果的连续直方图保真度。
- [NatureBench](./naturebench.md) — 同样将难度锚定到已发表的科学结果，但在 SOTA 匹配判据下横跨 Nature 系学科，而非在物理学家校准阈值下复现单一领域的分析。
- [ScienceAgentBench](./scienceagentbench.md) — 同样从同行评审论文中提取任务，但将输出统一为跨四个学科的独立 Python 程序，而非单一领域内端到端的模拟–筛选流水线。
