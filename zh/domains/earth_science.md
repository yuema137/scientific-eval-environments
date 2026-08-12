# Earth Science

> [English](../../domains/earth_science.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

地球科学：大气、海洋与地质科学。GIS 与地理空间分析折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| GeoNatureAgent Benchmark | 2026 | 通过对生产级 API 的结构化工具调用，对西班牙与葡萄牙做环境地理空间分析；API 经 16 个工具提供三类环境指标。 | 93 个任务、18 个类别：市镇分析、空间推理、跨指标综合、多语言查询，以及必须婉拒的刻意不可解任务。 | 每案例八项机械检查——期望的工具调用、必含/禁含关键词、数值容差（±2 个百分点）、图表产出、轮次预算——不用 LLM judge。 | [→](../works/geonatureagent-benchmark.md) |
| ScienceAgentBench | 2024 | 地理信息科学任务——其 102 个任务中的 27 个——提取自经同行评审的数据驱动发现工作流。 | 每个任务要求生成一个自包含的 Python 程序，复现真实论文中的分析。 | 有效执行加逐任务手写的成功检查器，对照专家标注参考；图形输出由 GPT-4o 评判。 | [→](../works/scienceagentbench.md) |
| Terminal-Bench Science | 2026 | 其五大分组中 Earth Sciences 分组下的大气、环境、地质与海洋科学任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Earth 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |
| HydroAgent | 2026 | 率定美国国家气象局用于山洪预报的业务化 CREST 分布式水文模型。 | 在流域面积 329–40,792 km² 的四个留出测站上迭代「模拟-调整」率定，二十轮取最优；九个前沿 agent。 | 留出测站上对照人类专家率定参照的 Nash–Sutcliffe 效率。 | [→](../works/hydroagent.md) |
| SciVisAgentBench | 2026 | 地球系统科学数据的科学可视化与数据分析——其七个应用领域之一——把自然语言意图翻译为对多变量场及时变场的可执行可视化操作。 | 108 个专家精心设计的 SciVis 案例，横跨七个科学领域与 15 类可视化操作，通过 CLI、MCP 服务器与 Python API 在 ParaView、napari 等平台上运行。 | 以结果为中心的多模态管线，结合一个 MLLM judge（报告为 Claude-Opus-4.6；与人类评分 Pearson 0.808）与确定性评估器——图像指标（PSNR、SSIM、LPIPS）、代码检查器，以及基于规则/逐案例的验证器。 | [→](../works/scivisagentbench.md) |
| DrBencher | 2026 | 地球物理领域（折并入地球科学）中「网页浏览 + 计算」交织的问题——从知识图谱来源做多跳实体识别与定量地球物理属性检索，再做领域特定计算。 | 由知识图谱链合成的答案优先问题，要求多跳识别、定量属性检索与多步计算；横跨五个领域（生物化学、地球物理、金融、安全、历史），地球物理是其一。 | 基于执行：金标准答案由对知识图谱数值执行参数化代码算得，以约 2% 相对容差评分；两阶段难度级联；76% 经人工验证有效。 | [→](../works/drbencher.md) |

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [HydroAgent](../works/hydroagent.md)
