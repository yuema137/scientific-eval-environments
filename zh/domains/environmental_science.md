# Environmental Science

> [English](../../domains/environmental_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

环境预测与监测。生态学折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | 对真实地域的环境预测：CO2 吸收适宜性（西班牙）、冲沟侵蚀概率与栖息地分析，经生产级地理空间 API 提供。 | 93 个任务、18 个类别，每任务给定期望工具调用、内容约束、轮次预算与领域专家真值。 | 每案例八项机械检查——期望的工具调用、必含/禁含关键词、数值容差（±2 个百分点）、图表产出、轮次预算——不用 LLM judge。 | [→](../works/geonatureagent-benchmark.md) |
| Terminal-Bench Science | 2026 | 其五大分组中 Life Sciences 分组下的生态学与 Earth Sciences 分组下的环境科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ERI Benchmark | 2026 | 环境工程是其覆盖的九个领域之一，下设五个子领域：水处理、空气质量、水文学、废弃物管理与环境影响。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值。 | [→](../works/eri-benchmark.md) |

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ERI Benchmark](../works/eri-benchmark.md)
