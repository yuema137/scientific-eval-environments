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
| Hydro-SE Bench | 2025 | 水文与水资源、水力学与河流动力学、气象学——水科学与水利工程九个子领域中的三个。 | 覆盖九个子领域的 4,000 道中文单选与多选题，取材于教科书、行业标准、法律法规与统计年鉴，由专家范例引导的半自动流水线生成，每题至少经三位专家审核；16 个模型。 | 零样本思维链、温度 0 提问，答案抽取交由另一个 LLM 完成；准确率按总体以及子领域、题型、认知层级分别报告。论文指出，模型在这几个偏科学基础的子领域上强于偏规范条文的工程子领域。 | [→](../works/hydro-se-bench.md) |
| ScienceBoard | 2025 | 通过 GRASS GIS 驱动的地理空间分析——它是承载各领域的六款专业软件之一。 | 单台 Ubuntu 虚拟机中 169 个人工整理的计算机使用任务：38 个纯 GUI、33 个纯 CLI、98 个 GUI+CLI 混合；逐软件任务数未公布。 | 通过支持精确匹配、区间判定与数值容差的模板，程序化检查关键中间输入/输出与虚拟机的最终状态；GIS 在所有受评 agent 上都属最弱的领域之一。 | [→](../works/scienceboard.md) |
| Imaging-101 | 2026 | 地球科学计算成像——它明列的六个领域之一——通过完整的重建流程，从间接且带噪的测量中恢复隐藏信号。 | 57 个以论文为依据的任务横跨六个领域，每个都规整为预处理 → 正向物理建模 → 逆问题求解 → 可视化，并在规划、函数级与端到端三条赛道上评测；逐领域任务数为 `TODO(reference)`。 | 端到端重建实际执行，用归一化互相关与 NRMSE 对照各任务 `metrics.json` 中的验收阈值评分；函数级工作由从捕获的参考输入/输出合成的配套 pytest 测试集检查。 | [→](../works/imaging-101.md) |
| SciVQR | 2026 | 地理学科中的多模态科学推理——六个顶层计分学科之一——其子领域包括地质学、地貌学、水文学、气候学与制图学。 | 3,254 道配图的竞赛与考试题目，横跨六个学科、54 个子领域（2,545 道选择题、709 道自由作答；分 easy/medium/hard 三档）；15 个多模态模型零样本受评，并对比用与不用 CoT。各学科的题目数量未公布。 | 按学科报告零样本准确率，另有五维 rubric（忠实性、信息量、冗余、幻觉、步骤缺失）对照专家撰写的解题过程为生成的推理打分。 | [→](../works/scivqr.md) |
| HiSciBench | 2025 | 贯穿各层级的地理学科：对地学论文做文献问答，外加由模型自行编写并执行 Python 分析代码的数据驱动发现。 | 8,735 个实例中地理学科占 737 个——200 个通用科学问答、500 个单语文献问答、10 个综述选题与 27 个数据驱动发现任务；18 个模型受评。 | 按层级选取指标：问答层用准确率，文献 OCR 用词级准确率，翻译用 BLEU；综述层由 LLM judge 按 1–5 分 rubric 评 Coverage、Structure、Relevance、Synthesis 与 Critical Analysis，另计引文可核验性、元数据准确性、忠实性与时效性；发现层用基于执行的 Success Rate，生成的程序跑不起来即计零分。 | [→](../works/hiscibench.md) |

## Related Works

- [DrBencher](../works/drbencher.md)
- [SciVisAgentBench](../works/scivisagentbench.md)
- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [ScienceAgentBench](../works/scienceagentbench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
- [HydroAgent](../works/hydroagent.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [ScienceBoard](../works/scienceboard.md)
- [Imaging-101](../works/imaging-101.md)
- [SciVQR](../works/scivqr.md)
- [HiSciBench](../works/hiscibench.md)
