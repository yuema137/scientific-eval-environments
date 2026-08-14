# MolClaw (2026)

> [English](../../works/molclaw.md) | **简体中文**

## Overview

MolClaw 是面向药物分子评估、筛选与优化的自主 agent，建立在三层的分层 skill 架构之上，并随之发布 **MolBench**——一个覆盖分子筛选、分子优化与端到端发现挑战的 benchmark，任务跨度为 8 到 50 次以上的顺序工具调用。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** <https://arxiv.org/abs/2604.21937>
- **Venue:** arXiv preprint, April 2026（v2 于 2026 年 5 月修订）

## Summary

计算药物发现需要在多步工作流中编排数十个专用工具，论文报告当前的 AI agent 在这类高复杂度场景中普遍表现不佳。MolClaw 把 30 多个专用领域资源统一到一套含 70 个 skill 的分层 skill 架构之下：工具级 skill 把原子操作标准化，工作流级 skill 把它们组装成带质量检查与反思的受验流水线，学科级 skill 则提供在各类场景中统领规划与验证的科学原则。配套的 MolBench 评测套件分三档——筛选、优化、端到端发现——以便把临时写脚本的能力与编排工作流的能力分开。作者报告的消融显示，增益集中在需要结构化工作流的任务上，而在靠临时脚本就能解决的任务上消失；他们据此认为，工作流编排才是主要的能力瓶颈。

## Tasks

MolBench 分三档：

- **MolBench-MS（分子筛选）** — 三个子任务：性质过滤（n = 50，对 RDKit 描述符做约束满足）、结合亲和力比较（n = 37，按取自 ACNet 的 Ki 值给分子对排序）、分子对接筛选（n = 25，虚拟筛选，以 Hits@3 计分）。筛选题目取自 CARA 的 ChEMBL 子集与 ACNet 数据库。
- **MolBench-MO（分子优化）** — 两个子任务：官能团修饰（n = 39），以及面向 QED、LogP、LogS 目标的理化性质优化。优化题目改编自 ChemCoTBench，并剔除了定义不良的条目。`TODO(reference)` — 性质优化子任务的题量在所查来源中未见陈述。
- **MolBench-E2E（端到端）** — 三个多阶段发现挑战，需要 8 到 50 次以上的顺序工具调用：粗粒度构象采样加全原子重建；多轮 QED 优化（最多五轮）；以及对 Erlotinib 的结构导向先导化合物优化（最多十五轮）。

## Domains

化学与医学健康——计算药物发现：分子性质计算、结合亲和力推理、分子对接与虚拟筛选、分子编辑与性质优化，以及对一个具名药物分子的结构导向先导优化。

## Evaluation

每一档各有自己的协议：

- **MolBench-MS** — 性质过滤与结合亲和力比较用准确率（%）；分子对接筛选用 **Hits@3**，即排序前三的结果中平均出现多少个真实活性分子。
- **MolBench-MO** — 分子编辑用操作准确率；性质优化用性质增量（Δ）与成功率（%）。
- **MolBench-E2E** — 任务特定的加权 rubric，把每个挑战拆成若干判据，涵盖工具选择与调用顺序是否正确、中间推理的科学合理性、工作流各步之间的数据完整性与参数一致性、终止行为是否得当，以及输出交付物的完整性。`TODO(reference)` — 各条 rubric 的权重与 rubric judge 的身份在所查来源中未见说明。

基线覆盖九个 LLM（GPT 5.2、Claude Sonnet 4.6、Gemini 3、DeepSeek v3.2、Kimi 2.5、GLM 5、Minimax 2.5、Qwen 3.5、Intern S1）、Biomni agent，以及原生的 Claude Code 与 OpenClaw harness。MolClaw 跑在 Claude Code 上的报告结果包括：结合亲和力准确率 81.1%（较未用 MolClaw 的基线高 24.3 个百分点，Fisher 精确检验 P = 0.043）；对接命中数 0.80，而 Claude Code 为 0.56、OpenClaw 为 0.20；性质优化增量 1.724，成功率 100%。

## Typical Duration

MolBench-E2E 的挑战每个任务需要 8 到 50 次以上的顺序工具调用，其中两个优化挑战分别最多跑五轮与十五轮。`TODO(reference)` — 所查来源未报告每任务的 wall-clock 时间与 token 预算。

## Main Contribution

一套提升 agent 在多工具药物发现工作流上可靠性的分层 skill 架构，配上 MolBench——一个具名、分档的评测套件，覆盖分子筛选、分子优化与端到端发现——以及一个有消融支撑的论断：AI 驱动药物发现的主要瓶颈是工作流编排能力，而不是化学知识或写脚本的能力。

## Key Design Ideas

- 三层 skill 层级：工具级 skill 标准化原子操作，工作流级 skill 把它们组装成带质量检查与反思的受验流水线，学科级文档提供全领域通用的规划与验证科学原则。
- 工具级 skill 模板刻意做得细粒度，以便在同时加载大量 skill 时限制上下文污染。
- benchmark 的分档（筛选 → 优化 → 端到端）是特意选的，好让消融能区分「靠临时脚本就能解」的任务与「必须有结构化工作流」的任务。
- 端到端档采用基于 rubric 的评分，给过程性质记分——调用顺序、参数一致性、终止行为——而不只看最终交付物。
- 筛选与优化的题目取自既有的精选化学资源（CARA/ChEMBL、ACNet、ChemCoTBench），而非从零撰写。
- 一套 skill 结晶流程，把新出现的执行轨迹转成持久可复用的 skill，初始带一个未经验证的置信度评级，再经一次次通过验证的执行逐步升格。

## Strengths

- 随 agent 一同发布具名 benchmark 与文档化的评分协议，系统的主张因此可核查，而不只是靠案例演示（论文）。
- 消融设计直接检验论文的核心论断：增益集中在需要结构化工作流之处，在不需要之处则消失（论文）。
- 基线面很广，涵盖九个 LLM 加一个领域 agent（Biomni）与两个通用编码 harness（论文）。
- 端到端档评测的是真正长的工具调用链（8 到 50 次以上），而非一问一答式的化学问答（论文）。

## Limitations

- 作者声明所有端到端结果都是纯计算的；对接分数的提升不保证实验上的亲和力提升，湿实验验证仍不可或缺。
- 三个 E2E 挑战样本有限；作者指出，要谈泛化性还须扩展到多样的靶点类别（GPCR、离子通道、蛋白酶）。
- 作者报告了一次注意力偏倚失误：某个挑战中 AMES 致突变性恶化了 +180% 却未被标记出来，尽管 agent 一直在跟踪 13 项 ADMET 终点指标。
- skill 层是静态的——作者指出 agent 不会从既往执行中学习，并举出反复出现的「乙炔基固着」（ethynyl fixation）作为无法从负反馈中泛化的例子——而那 70 份 skill 文档需要专家策展，因此可扩展性取决于论文并未给出的自动 skill 发现。
- 上下文窗口的限制可能使各层 skill 无法同时加载，优化循环的收敛判据也仍是启发式的（论文）。
- `Repository note:` 所查来源未给出 MolBench 的公开仓库或数据地址，因此第三方能否复用该 benchmark 无从核实。
- `Repository note:` 这套 skill 层级是 agent 的*架构*，而不是一种评估分解——MolBench 并不报告逐 skill 的能力画像，因此本卡片不归入 Skill Hierarchy 索引。

## Related Works

- [ChemCoTBench](./chemcotbench.md) — MolBench-MO 分子优化题目的来源，也是把分子变换表述为模块化化学操作的最接近的既有 benchmark。
- [MolQuest](./molquest.md) — 另一个 agentic 多轮化学 benchmark，针对的是结构解析而非筛选与优化。
- [TOMG-Bench](./tomg-bench.md) — 基于文本的开放分子生成，是 MolBench 多轮优化的单步对应物。
- [BioAgent Bench](./bioagent-bench.md) — 多工具生物医学 agent 评测，工具调用时程与之相当。
- [AtomWorld](./atomworld.md) — 面向原子与分子结构操作的 agent 评测。
