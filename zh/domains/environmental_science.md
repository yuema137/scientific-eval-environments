# Environmental Science

> [English](../../domains/environmental_science.md) | **简体中文**

## Scope

环境预测与监测。生态学折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | 对真实地域的环境预测：CO2 吸收适宜性（西班牙）、冲沟侵蚀概率与栖息地分析，经生产级地理空间 API 提供。 | 93 个任务、18 个类别，每任务给定期望工具调用、内容约束、轮次预算与领域专家真值。 | 每案例八项机械检查——期望的工具调用、必含/禁含关键词、数值容差（±2 个百分点）、图表产出、轮次预算——不用 LLM judge。 | [→](../works/geonatureagent-benchmark.md) |
| Terminal-Bench Science | 2026 | 其五大分组中 Life Sciences 分组下的生态学与 Earth Sciences 分组下的环境科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
