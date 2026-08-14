# gammapyGPT (2025)

> [English](../../works/gammapygpt.md) | **简体中文**

## Overview

一个能在受控执行环境中为地基伽马射线天文学编写、执行并验证 Gammapy 分析代码的 agent，并配有一套伽马射线分析任务的 benchmark，其数值输出会与预期值核对。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [数据分析与统计推断](../activities/data_analysis_statistical_inference.md)
- [科学软件与工作流工程](../activities/scientific_software_workflow_engineering.md)

## Links

- **Paper:** <https://arxiv.org/abs/2509.26110>
- **Demo:** <https://majestix-vm8.zeuthen.desy.de>
- **Venue:** ICRC 2025 proceedings, PoS(ICRC2025)753

## Summary

像 Gammapy 这样的专用科学库，既没有基础模型在流行框架上所依赖的文档量与示例语料，API 也不够稳定，因此针对它们生成的代码常常过时或出错。这项工作为 Gammapy 解决该问题：agent 把用户提示扩展成一段受管控的对话历史，产出单个 Python 脚本，在只带一个数据指针的精简环境中执行该脚本、并对执行设有硬性时间上限，再把简明的错误摘要回灌到下一轮迭代，直到脚本通过验证或尝试次数用尽。检索增强生成是可选项，在有资料时注入 top-k 教程片段。整个贡献打包成一个小型 Python 包（`gammapygpt`），附带一个极简网页 demo 与一套 benchmark 测评框架。

## Tasks

四个领域专属的 Gammapy 任务：**ObservationList**（为给定源筛选观测并报告观测数目）、**ReflectedSignificance**（计算某源的反射区显著性）、**ReflectedSpectrum**（做反射区能谱提取并报告总能流与谱指数），以及 **Source3DAnalysis**（把某源全部可用的观测归约为一个 `MapDataset` 并拟合空间—能谱模型）。任务定义在通过数据指针（`PHOTON_STORAGE`）取得的真实观测数据之上，而非合成的测试数据。

## Domains

天文学——具体是地基伽马射线天文与高能天体物理，处在 Cherenkov Telescope Array Observatory 的分析语境中。被打分的量都是天文结果（观测数目、区域显著性、能流、谱指数、空间—能谱源拟合），经由 Gammapy 分析库得到，因此即便 agent 的产出形式是代码，评测目标仍是天文数据分析。

## Evaluation

- 生成的脚本在受控环境中执行；验证逐任务进行，判据随任务复杂度分级。ObservationList 要求整数精确匹配；能谱类任务把浮点数与预期值在容差内比较；Source3DAnalysis 只要脚本能在超时前端到端跑完即算通过，作者把这一放宽归因于该任务的复杂度。
- 测评框架会记录异常类别、一小段回溯尾部、输入 / 缓存输入 / 输出 / 推理的 token 数，以及验证通过时的尝试序号——因此每一次通过都连同「花了几轮纠错」一并记录在案。
- **报告。** 两个 OpenAI 推理模型（o3 与 GPT-5）在可用的最高推理强度下运行；在规模较小的逐源任务上，作者的实验中两者都达到 100% 通过率，较新的模型略快一些。

## Typical Duration

每个任务一次 agent 会话，内含「纠错—重试」的迭代循环，受尝试次数预算（未给数值）与每次脚本执行的硬性 wall-clock 上限（未给数值）约束。一次典型的成功运行记录到 7.3k 输出 token，其中约 6.5k 是推理 token。

## Main Contribution

为一个基础模型处理得很差的科学库，给出一个以执行为依据的代码生成 agent，并附上一套 benchmark——它验证的是 agent 的**数值分析结果**，而不是代码看上去是否合理。

## Key Design Ideas

- 验证是循环的控制器：判定一次尝试是否通过、以及用什么错误摘要开启下一次尝试的，是执行输出而非模型的自我评估。
- 通过判据按任务难度分级——整数精确匹配、带容差的浮点比较，以及最难任务的端到端执行。
- 埋点记录验证通过时的尝试序号，把首次尝试即成功与出错纠正后才成功区分开。
- 教程片段的检索做成一个可选开关，从而把 RAG 的贡献与基座模型的贡献分离。
- 脚本在只带一个数据指针的精简环境中运行，让被执行的任务保持可复现且有边界。

## Strengths

- 打分建立在真实观测数据上的真实 Gammapy 输出之上，而不是代码相似度或判定出来的合理性。
- token 与回溯日志让失败模式与开销在每次尝试的粒度上可见，而不只体现在汇总通过率里。
- 瞄准的是一个真实缺口：一个仍在活跃开发、文档单薄的仪器分析库，恰是模型先验最弱的地方。

## Limitations

- 只有四个任务，且全是单源 Gammapy 分析；相对该库的分析面而言，套件规模偏小。
- 最难的任务（Source3DAnalysis）按能否执行完成打分，而非按拟合出的空间—能谱模型是否正确，因此一次通过的运行未必在科学上正确。
- 只评测了两个闭源推理模型，且两者在较小的任务上都打满了 100%，就报告结果而言几乎没有留下区分度空间。
- 论文说明配套代码在发表时尚未公开，因此该 benchmark 能否被第三方复用尚未确认。
- Repository note: 这是一篇简短的会议论文集投稿（ICRC 2025），明确以介绍设计与当前进展为目的；测评框架的若干参数，包括尝试次数预算与执行超时，都只有定性描述而没有数值。

## Related Works

- [gwBenchmarks](./gwbenchmarks.md) — 同样用外部验证框架、而非 agent 的自我报告，为 coding agent 在天体物理领域的数值输出打分。
- [Stargazer](./stargazer.md) — 同样在天文分析上评测 agent，带明确的物理通过判据。
- [SciCode](./scicode.md) — 同样评测科学代码生成，在研究级任务上以执行来检查正确性。
- [SUPER](./super.md) — 同样考察 agent 能否在受控环境中让真实的研究代码正确跑起来。
