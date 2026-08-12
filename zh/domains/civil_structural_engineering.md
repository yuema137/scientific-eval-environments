# Civil & Structural Engineering

> [English](../../domains/civil_structural_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

土木与结构工程。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的土木工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| StructureClaw | 2026 | 把结构工程任务从建模一路做到验证、求解与规范校核。 | 以工件为中心的 agent 工作台上的 150 个受控场景（标准、交互、多模态重构）。 | 严格结构模型匹配加与冻结参考求解器响应的数值一致；所有断言须通过（E2E Success）。 | [→](../works/structureclaw.md) |
| ERI Benchmark | 2026 | 土木工程是其覆盖的九个领域之一，下设七个子领域：静力学、材料力学、结构分析、钢结构与混凝土设计、岩土工程、结构动力学与施工管理。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商组成的评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值。 | [→](../works/eri-benchmark.md) |

## Related Works

- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [StructureClaw](../works/structureclaw.md)
- [ERI Benchmark](../works/eri-benchmark.md)
