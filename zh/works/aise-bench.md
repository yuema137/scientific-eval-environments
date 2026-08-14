# AISE-Bench (2026)

> [English](../../works/aise-bench.md) | **简体中文**

## Overview

AISE-Bench 是面向学术知识图谱上学术信息检索的全流程标注 benchmark：1,133 组问答对，随附查询分类法、完整的 API 执行轨迹、经校验的参数，以及带参考链接、可溯源的答案，过程与结果一并计分。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)

## Activities

- [文献检索与证据综合](../activities/literature_evidence_synthesis.md)

## Links

- **Paper:** <https://arxiv.org/abs/2607.20498>
- **Code:** <https://aise-bench.github.io/>
- **Venue:** KDD 2026 (Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Jeju Island, Republic of Korea) — DOI 10.1145/3770855.3817492

## Summary

现有面向学术图谱信息检索的工具使用 benchmark 依赖合成模板、简化的解空间，或狭窄的以论文为中心的任务，于是真实用户意图、多步 API 规划、丰富的参数填充、可溯源的答案，以及过程与结果的联合评估这五个方面都探索不足。AISE-Bench 对每个实例做端到端标注——查询、计划、已执行的 API 调用及其经校验的参数，以及带引用的答案——从而同时补上这五点。为让这样的标注切实可行，作者搭建了一套定制的 agent 工作流（Planner、Task Executor、Synthesizer），供标注者规划、执行并修订复杂的 API 工作流；他们还在一套协议下评估了 14 种方法，该协议对答案质量、引用溯源、API 规划正确性与执行成功率分别打分。

## Tasks

1,133 组问答对，其中 250 个实例经双人评审、883 个经单人评审。任务在 AMiner 与 Google Scholar 两个学术平台上调用 9 个 API，通过实体检索与实体详情两类 API 覆盖论文、作者、会议期刊、机构四种实体类型。查询分类法沿四个维度报告：用户意图（检索论文 / 作者 / 会议期刊 / 机构）、知识层级（记忆型对理解型，后者又分举例、比较、理解与摘要几个子类）、规划步数（2 到 5+ 次 API 调用），以及一级学科。各类别的具体数量为 TODO(reference)。

## Domains

在跨一级学科的学术知识图谱上做学术信息检索；被查询的对象是论文、作者、会议期刊与机构，而非任何单一领域的科学内容。该 benchmark 在设计上就与学科无关，因此不分配任何规范的科学或工程领域。

## Evaluation

一套包含三组指标的协议，过程与结果兼顾：

- **引用 / 格式：** 引用精确率、引用召回率与格式合规性。
- **API 过程：** agent 计划与标注计划之间的 Planning Graph Edit Distance、参数准确率与执行成功率。
- **答案内容：** 正确性、完整性、忠实度与 F1-LM。
- **报告。** 共评估 14 种方法，分属三个族——定制 agent 工作流下的六个 LLM、四个使用 API 的 agent 框架，以及编程 / deep research 系统。最好的结果是 PLAY2PROMPT，F1-LM 为 0.6104；Gemini-3-Pro 在定制工作流一族中领先，F1-LM 为 0.5606；CodeAct 达到 0.5130，Perplexity 为 0.3952。多数方法的部分完成分数很高（0.82–0.95），参数准确率却明显偏低，作者将其认定为主要瓶颈。

## Typical Duration

任务按规划深度分层，每条查询 2 到 5+ 次 API 调用。wall-clock 时间与 token 预算为 TODO(reference)。

## Main Contribution

一个面向学术知识图谱上多步 API 使用 agent 的真实、全流程标注 benchmark：每个实例携带的不只是标准答案，还有为过程评分所需的、经校验的计划、参数与执行轨迹——外加一套让这类监督信号得以规模化产出的标注工作流。

## Key Design Ideas

- 标注是全流程的：查询分类法、执行轨迹、经校验的 API 参数与带引用溯源的答案统统记录在案，因此过程指标有标准答案可比，而不必依赖启发式。
- 规划质量以对照标注计划的图编辑距离来测量，从而容忍严格序列匹配会判错的顺序差异。
- 参数填充被当作一等指标计分，隔离出一种被最终答案准确率掩盖的失败模式。
- 定制的、面向标注者的 agent（Planner / Task Executor / Synthesizer）用作标注基础设施，而非被测系统。
- 查询按规划深度与知识层级分层，使难度成为受控维度而非涌现属性。

## Strengths

- 舍弃合成模板，改用经人工评审、意图真实的精选查询。
- 过程与结果分开报告，因此「计划错了却答对」的情况不会被掩盖。
- 答案必须溯源到出处并附参考链接，使忠实度可核查。
- 代码与数据已发布，且工作经 KDD 2026 同行评审。

## Limitations

- 1,133 个实例中只有 250 个经双人评审，其余 883 个仅有一轮标注。
- benchmark 绑定在 AMiner 与 Google Scholar 的 API 接口上，因此分数取决于这些线上服务，也取决于其 API 随时间的稳定性。
- 四维查询分类法中各类别的具体数量未报告，为 TODO(reference)。
- Repository note: 学术知识图谱是 agent 查询的底座；该 benchmark 并不评估图谱本身的构建、策划与维护。

## Related Works

- [ScholarQuest](./scholarquest.md) — 同样对 agent 式学术文献检索做 benchmark，但面向开放文献检索而非结构化图谱 API。
- [MedBrowseComp](./medbrowsecomp.md) — 同样要求从线上领域知识库做多跳检索并可核验溯源，设定在医学。
- [BioKGBench](./biokgbench.md) — 同样评估在知识图谱上行动的 agent，但核查的是图谱事实，而非通过 API 检索信息。
- [Toolathlon](./toolathlon.md) — 同样把多步真实 API 使用作为核心受测能力。
