# TELBench (2026)

## Overview

TELBench 是一个针对 deep-research agent trajectory 的 span 级错误定位 benchmark，考察模型能否在正常探索、失败检索、试探性假设与无害噪声之中挑出有害的 error span。它包含 1,000 个经核验的 trajectory 实例（600 个 easy / 400 个 hard），取自由 2,790 条真实 agent 运行构成的语料，每条被切分为带二元 error / non-error 标签的有序语义 span。

## Topics

- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Links

- **Paper:** <https://arxiv.org/abs/2606.02060>

## Summary

TELBench 主张，对 deep-research agent 的结果级评估只能说明一次运行是否成功，却无法指出 trajectory 的哪一部分最先使答案变得不可靠。它由覆盖三个 deep-research benchmark、三个 backbone 模型与两个 agent 框架的 2,790 条真实 trajectory 构建，将原始日志转换为有序语义 span，并要求模型在良性探索、失败检索与噪声之中定位有害的 error span。论文同时提出 DRIFT——一个以 claim 为中心的审计框架，在 span 级错误定位与 first-error accuracy 上相比 bare-LLM prompting 最多提升 30 个百分点。

## Tasks

1,000 个经核验实例（600 个 easy / 400 个 hard），每个都是一条完整 agent trajectory，被切分为平均 11.95 个有序语义 span，模型须逐一标注 error 或 non-error。这些实例挖掘自 2,790 条 trajectory——它们由 GPT-5、Gemini-2.5-Pro 与 Claude-Sonnet-4.5 在 MiroFlow 与 OAgent 框架下、针对来自 GAIA-val、XBench 与 BrowseComp-test 的 465 个任务运行生成（BrowseComp 下采样至 200 个任务）。两名 frontier-LLM 标注者提出的候选 error span 由专家标注者核验——七名专家各投入超过 300 小时——语料再经 1,890 条含错 trajectory（占语料 67.7%）过滤，最终保留边界清晰、且含足够良性干扰 span 的 1,000 条。

## Domains

Deep-research agent trajectory——网页检索、浏览、tool use、证据检查与答案综合——取自 GAIA、XBench 与 BrowseComp 的任务分布。

## Evaluation

- **Span-level localization.** 每个语义 span 都是一个二元 error / non-error 目标，用宏平均的 precision、recall 与 F1 在 error span 上评分。
- **First-error accuracy (FEA).** 衡量最早预测的 error span 是否与最早标注的错误一致，将时间定位能力从总体检测中分离出来。
- **Splits and repeats.** 结果在完整的 Verified-1K 集合及其 600 个 easy / 400 个 hard 划分上报告，每种配置运行三次。
- **Reported.** DRIFT 在每个 backbone 模型上都取得最佳的整体宏 F1：将 Claude-Sonnet-4.6 从 21.89 提升到 54.91、DeepSeek-V3.2 从 22.46 到 50.51、GPT-5.4 从 33.93 到 52.48、Gemini-2.5-Pro 从 31.01 到 48.41，均优于 Bare LLM、Codex 与 Claude Code 基线；first-error accuracy 仍低得多，Claude-Sonnet-4.6 整体仅达 24.10（较 11.30 提升）。

## Typical Duration

不设固定的步数或 wall-clock 预算；每个实例是一条完整 trajectory，平均 11.95 个语义 span。审计成本以 token 计：DRIFT 在 DeepSeek、GPT 与 Claude backbone 上平均每条 trajectory 消耗 17,653–22,643 个 token，Gemini-2.5-Pro 为 53,043 个（其 thinking 占主导），而 bare-LLM 基线为 5,649–14,307。

## Main Contribution

一个用于 deep-research agent trajectory 中 span 级错误定位的 benchmark 与以 claim 为中心的审计框架，将可靠性评估重构为寻找最先使答案变得不可靠、未被支持的 commitment，而非仅判断最终答案。

## Key Design Ideas

- 以语义 span 作为分析单元：原始日志被归一化，并在检索目标、候选集合、时间范围、验证标准或推理目标发生变化处切分。
- 二元 error / non-error 标签以是否危害答案路径来定义，因此正常探索、失败检索、试探性假设、已恢复的失误与工具噪声本身不算错误。
- 一套由数据归纳出的机制分类：一个八阶段的操作 schema，外加归入六个 fault family 的 18 种主要 fault（Constraint Handling、Search and Retrieval、Evidence Grounding、Entity Mapping、Information Processing、Process Control），仅用于分析。
- DRIFT 以 claim 为中心的流水线——Claim Keeper 账本、为支持指派 direct / weak / missing / conflicting 状态的 Support Seeker，以及标记那些对未被支持的 claim 做出承诺或复用的 span 的 Dependency Tracer。

## Strengths

- 语义 span 切分给出的单元，既粗到足以跨异构、框架相关的日志进行比较，又细到足以定位最先的有害承诺。
- 标签来自 LLM 提议加专家裁决的两阶段流程（七名标注者，各超过 300 小时），针对具体的有害承诺，而非笼统地标记失败运行。
- 将 span 级 F1 与 first-error accuracy 分开，揭示出检测到某处错误与精确定位最早错误是不同的能力，而后者即便对最强的审计器也依然困难。

## Limitations

- Repository note: 所有 trajectory 均来自三个 deep-research QA benchmark（GAIA、XBench、BrowseComp），在两个框架与三个 backbone 模型下运行，因此其错误模式与归纳出的 fault 分类未必能迁移到其他 agent 场景。
- Repository note: 这 1,000 个实例被筛选为错误边界清晰可核验、且良性干扰充足者，使该集合成为经过策划的诊断子集，而非 2,790 条 trajectory 语料的代表性抽样。

## Related Works

- [TRACE](./trace.md) — 同样对 deep-research agent trajectory 做过程级评估，但评的是多维 trajectory 质量，而非定位离散的 error span 与最早错误。
- [FinTrace](./fintrace.md) — 同样是多维 trajectory 评估，但面向金融 agent 工作流，而非 deep-research 浏览。
- [AgentBoard](./agentboard.md) — 同样关注最终答案成功率之下的中间行为，但通过跨任务族的细粒度 subgoal 进展率，而非 span 级错误定位。
