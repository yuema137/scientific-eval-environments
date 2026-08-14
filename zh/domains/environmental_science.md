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
| LLM-EPANET | 2025 | 市政供水管网的水质行为——余氯输移、水龄与水源追踪——以及同一批管网的水力模拟。 | 在标准的 Net1、Net3 与 L-Town 管网上提出 69 条自然语言查询，分五个复杂度类别，其中 Quality 类别必须做水质模拟；每条查询都配一份手写的确定性参考脚本。 | 以返回数值与执行后的 EPyT 参考实现是否功能等价为准，执行失败以及聚合、索引、单位错误一律判错；在七个模型上按类别报告准确率，总体 56–81%。 | [→](../works/llm-epanet.md) |
| Hydro-SE Bench | 2025 | 水科学与水利工程中的水资源管理，与该基准的水文学、河流动力学、气象学等子领域并列。 | 覆盖九个子领域的 4,000 道中文单选与多选题，每题标注认知层级，取材于教科书、行业标准、法律法规与统计年鉴，每题至少经三位专家独立审核；16 个模型。 | 零样本思维链、温度 0 提问，选项字母由另一个 LLM 抽取；准确率按总体以及子领域、题型、认知层级分别报告，模型在偏科学基础的子领域上得分高于偏规范条文的工程子领域。 | [→](../works/hydro-se-bench.md) |
| OntoLearner | 2026 | 为生态与环境——它的本体集合覆盖的 22 个领域之一——构建本体结构：给术语定类型、恢复类型之间的 is-a 层级、抽取非分类关系。 | 覆盖 22 个领域的 180 个机器可读本体，为三项本体学习任务备好可直接接入流水线的 train/dev/test 切分；共评测 22 个检索模型与 12 个 LLM，设定是单次结构化预测而非 agentic 循环。 | 以归一化的成对与三元组匹配对照金标准本体结构计算 precision、recall 与 F1；卡片中逐领域、逐模型的分数为 `TODO(reference)`，因论文的结果章节无法获取。 | [→](../works/ontolearner.md) |

## Related Works

- [GeoNatureAgent Benchmark](../works/geonatureagent-benchmark.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [LLM-EPANET](../works/llm-epanet.md)
- [Hydro-SE Bench](../works/hydro-se-bench.md)
- [OntoLearner](../works/ontolearner.md)
