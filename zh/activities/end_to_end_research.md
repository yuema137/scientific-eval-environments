# 端到端研究

> [English](../../activities/end_to_end_research.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 贯穿宽泛、多阶段研究生命周期（而非单一环节）的能力——跨越问题提出、文献调研、假设生成、方法设计、实验、分析、解读与汇报中的若干阶段。

## Scope

保守使用，仅当 benchmark 明确评估跨越多个主要研究阶段的实质性多阶段研究流程时才归入。仅有长时程难度或使用大量工具并不足以归入此类。

## Task Patterns

这些 benchmark 评估的是 agent 在科学研究全流程中的表现，而非某个孤立的环节。[MLGym](../works/mlgym.md) 和 [MLR-Bench](../works/mlr-bench.md) 覆盖了完整的 ML 研究闭环——想法与假设生成、数据构建、方法实现、实验、分析以及论文撰写，其中 MLR-Bench 明确划分出四个阶段（想法、提案、实验、写作）。[AIRS-Bench](../works/airs-bench.md) 和 [ResearchClawBench](../works/researchclawbench.md) 则更进一步，不提供 baseline 代码或目标论文，迫使 agent 从零开始提出问题、调研文献、设计方法并开展实验。[AstaBench](../works/astabench.md) 把端到端的科学发现（E2E-Bench、E2E-Bench-Hard）与文献、代码、数据分析等 benchmark 并置在一起，在更宽泛的评测套件中单独考察多阶段科学发现的能力。

这些任务与单一环节任务的根本区别在于，成功与否取决于能否将多个环环相扣的研究阶段串联起来：agent 无法仅靠调调超参数或回答一个检索问题就完成任务，而必须提出问题、生成假设、搭建并运行实验，再对结果加以解读或汇报——评判往往依据专家评分细则、隐藏的目标论文，或是对整条流程而非孤立产出进行打分的自动化评审。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| AstaBench | 2025 | 在更宽泛的研究辅助套件中进行端到端科学发现 | 涵盖 11 个 benchmark、2,400+ 个问题的套件；其中 E2E-Bench/E2E-Bench-Hard 面向科学发现 | 公开 leaderboard 上经成本控制的综合得分 | [卡片](../works/astabench.md) |
| MLGym | 2025 | 构思、数据、方法实现、实验、分析、迭代 | Gym 环境，MLGym-Bench：13 个开放式 AI 研究任务（CV/NLP/RL/博弈论） | 在完整研究闭环中全面超越所提供的 baseline | [卡片](../works/mlgym.md) |
| MLR-Bench | 2025 | 想法生成、提案、实验、论文撰写 | 来自 NeurIPS/ICLR/ICML 的 201 个开放式 ML 任务；MLR-Agent 脚手架 | MLR-Judge 评分细则打分，逐阶段与端到端并重 | [卡片](../works/mlr-bench.md) |
| AIRS-Bench | 2026 | 完整研究生命周期，无 baseline 代码，工作流从零搭建 | 涵盖 language modeling、数学、bioinformatics、时间序列的 20 个前沿任务 | 设计并执行端到端的研究工作流 | [卡片](../works/airs-bench.md) |
| ResearchClawBench | 2026 | 问题提出、文献调研、实验、从原始数据中重新发现 | 40 个专家精选任务，10 个领域；隐藏的目标论文、相关文献与原始数据 | 依据加权多模态评分细则给出 Reference-Anchored Discovery Score | [卡片](../works/researchclawbench.md) |

## Related Works

- [AstaBench](../works/astabench.md)
- [MLGym](../works/mlgym.md)
- [MLR-Bench](../works/mlr-bench.md)
- [AIRS-Bench](../works/airs-bench.md)
- [ResearchClawBench](../works/researchclawbench.md)
