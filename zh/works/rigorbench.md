# RigorBench (2026)

> [English](../../works/rigorbench.md) | **简体中文**

## Overview

RigorBench 给自主 AI 编码 agent 打分，评的不只是结果对不对，而是**工程过程纪律**——解是怎么得到的。它把过程纪律拆成七根分别计分的支柱，从完整的执行 trajectory 上算出各支柱得分，再聚合为综合的 RigorScore。

## Topics

- [Planning & Decision-Making Evaluation](../topics/planning_decision_evaluation.md)
- [Trajectory Evaluation](../topics/trajectory_evaluation.md)
- [Skill Hierarchy](../topics/skill_hierarchy.md)

## Activities

N/A — 通用型编码 agent benchmark，未直接评估任何科学或研究活动。

## Links

- **Paper:** <https://arxiv.org/abs/2606.22678>（v2，2026 年 6 月 29 日——本卡片描述的是 v2，其任务数与支柱数与 v1 不同）
- **Code:** <https://github.com/MeherBhaskar/RigorBench>
- **Venue:** arXiv preprint (cs.SE), 2026

## Summary

论文调研了九个既有的 AI 编码 benchmark（HumanEval、MBPP、SWE-bench、BigCodeBench、DevBench、Terminal-Bench、ProjDevBench、AgentBench、LiveCodeBench），报告称没有一个测量规划质量、验证行为、恢复策略、弃答是否得当或代码库健康度——作者把这一空白称作「lab-to-production gap」。RigorBench 用三项设计来填补它：七支柱评分框架；一套任务集，其五个类别各自压测特定支柱；以及一条基于 trajectory 的评分流水线，解析状态（代码库快照）与动作（agent 操作），而不只看最终产物。评测固定基础模型、只变换 agentic harness，测的因此是 harness 对过程质量的贡献。作者明确把这项工作定位为验证评分方法学的探索性研究，而非一个已定型的 benchmark。

## Tasks

共 100 个任务，五个类别各 20 个：**Plan-Then-Build**（跨文件的功能需求；主考支柱 PF、ATI；中–难）、**Verify-Or-Die**（藏在「看着显然」的解背后的隐蔽 bug；VC、RE；中）、**Doom Loop Gauntlet**（首次尝试注定失败；RE；难）、**Know When to Fold**（不可能完成或故意含混的任务；AQ；难度不一）、**Don't Break the Build**（带检查点的多步重构；ATI、PF；难）。任务撰写遵循三条原则——可区分（不同的纪律水平会留下不同的过程痕迹）、可测量（trajectory 携带的信号足以支撑自动评分）、贴近真实（反映专业软件工程的实际模式）。每个任务附带一个起始仓库；附录给出的例子包括一个空的 Node.js/Express 骨架，一个含 12 个通过测试与 8 个隐藏边界用例测试的 Python 日期库，一个 10 个测试中有 3 个非确定性失败的 Rust 哈希校验模块，一份可证明不可能实现的排序算法规格，以及一个含 8 个 model、15 个 view 与 47 个通过测试的 Django 项目。完整的任务规格、起始仓库与评分 rubric 据称都随 benchmark 一同发布。

## Domains

软件与系统工程：在 Node.js、Python、Rust 与 Django 的起始仓库上做功能实现、bug 诊断与修复、多步重构以及测试撰写。不评估任何科学领域。

## Evaluation

- **七根支柱，各自归一到 [0, 1]。** Planning Fidelity（PF，权重 0.15）= 0.30 × 规划工件的创建 + 0.35 × 分解质量（4 分制 rubric）+ 0.35 × 计划与执行的一致性（计划步骤与实际执行步骤之间的 Kendall τ）。Verification Coverage（VC，0.15）= 0.35 × 测试创建率 + 0.30 × 覆盖率增量 + 0.35 × 需求可追溯性（对需求的召回率）。Recovery Efficiency（RE，0.20）= 0.30 × f(恢复尝试次数) + 0.35 × 策略多样性 + 0.35 × (1 − token 浪费比)，其中 f(RAC) = 1/(1 + λ·RAC)，λ = 0.2。Abstention Quality（AQ，0.10）只在不可能或含混的任务上计分，涵盖正确弃答、虚假自信与主动澄清。Atomic Transition Integrity（ATI，0.10）= 0.40 × 构建健康度 + 0.40 × 测试套件稳定性 + 0.20 × 提交卫生。Test Assertion Density（TAD，0.20）= min(1.0, meaningful_asserts / max(1, test_functions) / 5.0)。Exploration Efficiency（EE，0.10）= files_modified / (files_read + files_modified)。
- **综合分。** RigorScore = 0.15 × PF + 0.15 × VC + 0.20 × RE + 0.10 × AQ + 0.10 × ATI + 0.20 × TAD + 0.10 × EE。权重来自对十位 staff 级软件工程师的试点问卷，作者标注为初步值；±50% 的敏感性分析显示，受评 harness 的排序不随权重选择改变。
- **Trajectory 流水线。** 执行过程经过插桩，记录 agent 生成的文本、文件 diff、命令执行及其输出、每个动作的 token 消耗与时间戳；评分分三步——trajectory 解析、自动信号抽取（规划工件、测试事件、恢复循环、弃答信号、健康检查点），以及对照公开 rubric 的支柱打分。
- **反刷分校验。** 规划工件要拿分，必须有一份专门的规划文档，至少 50 个非空白字符且包含与任务相关的术语；测试创建的关联性要求测试位于标准位置，并 import 和调用被修改的模块；构建健康度与测试稳定性的检查方式是，每次文件修改后在隔离的 Docker 环境中实际运行构建与测试命令。
- **判分。** 定性子指标（如分解质量、提交卫生）用 Gemini 3.1 Pro（`gemini-3.1-pro-preview`，thinking_level "high"）作 LLM judge；客观指标以程序化方式核验。
- **单独测量的结果分。** 任务特定的正确性标准（测试通过率、功能完整度、有无回归）与过程分独立评定，从而可以做过程–结果的相关性分析。
- **报告结果（表 III，100 个任务上的均值 ± 标准差）。** Agent-Rigor 的 RigorScore 为 0.53 ± 0.08、结果分 0.83 ± 0.05；Superpowers 0.41 ± 0.09 / 0.70 ± 0.06；Agent-Skills 0.39 ± 0.09 / 0.72 ± 0.06；Baseline ReAct 0.40 ± 0.09 / 0.64 ± 0.05。四套系统跑在同一个基础模型 Gemini 3.5 Flash 上（thinking_level "medium"）。未取整的九指标表在约 410 次运行上报告的 RigorScore 为：Agent-Rigor 0.527、Superpowers 0.410、Baseline 0.395、Agent-Skills 0.387。
- **过程与结果的关系。** 线性拟合为 Outcome = 0.26 + 1.07 × RigorScore，但同一 harness 内部的任务级相关并不显著（Agent-Rigor r = 0.12，Baseline r = 0.05）；作者据此认为，过程纪律是宏观层面的能力区分因素，而非任务级的预测因子。

## Typical Duration

每次执行都在隔离的 Docker 容器中进行，任务仓库全新克隆，wall-clock 超时 60 分钟，上下文预算 200K token。每任务的平均总 token 消耗从基线的约 42,500 降到强制前置规划条件下的 37,400，减少 12%。整项研究涵盖四套系统、约 410 次任务执行。

## Main Contribution

作者把 RigorBench 呈现为首个专门测量 AI 编码 agent 工程过程纪律的 benchmark，贡献包括：以九个既有 benchmark 的调研为依据，把过程纪律的空白形式化；把过程纪律分解为七根支柱并给出综合的 RigorScore；基于 trajectory 的评分，分析完整执行路径而非最终产物；探索性证据表明，强制前置规划的 harness 相比 ReAct 基线把过程质量提高 33%，并伴随结果质量提升 30%；以及任务、评分 rubric 与 trajectory 分析工具的开放发布。

## Key Design Ideas

- 把「过程」分与「结果」分分开，并在同一批运行上同时测量，使两者的相关性成为研究对象，而不是默认前提。
- 所有受评系统固定同一个基础模型，使差异可归因于 harness 而非模型。
- 让任务类别对准特定支柱——不可能完成的任务与含混任务存在的唯一理由，就是让弃答变得可测。
- 只要指标允许，就优先用程序化的信号抽取（跑构建、跑测试、看文件 diff、记 token 账），把 LLM judge 限制在真正定性的子指标上。
- 把反刷分阈值直接写进打分器（规划文档最短长度、测试与模块的关联），让敷衍的合规拿不到分。
- 论证 trajectory 评估天然比结果评估更难被污染，并把任务设计成有多条有效解路。

## Strengths

- 测量的是只看结果的 benchmark 在结构上看不见的维度，并以明确的调研确证这一空白在九个既有 benchmark 上都存在。
- 每根支柱都给出明确的子指标公式与权重，综合分因此可复现，而不只是 rubric 的概述。
- 受控比较设计：四套系统用同一基座模型、同一容器、同一超时与 token 预算。
- 对权重做了 ±50% 的敏感性检验并如实报告，结果显示排序对权重的选择稳健。
- 作者把利益冲突写在显著位置，并描述了近似预注册的保障措施：100 个任务及其确定性评测规则在 Agent-Rigor 运行之前就已定稿，竞品系统则以各自公开的默认配置运行。
- 不利与不方便的发现也照实报告，包括得分最高的 harness 在 Test Assertion Density 上反而**最差**（0.311，基线为 0.349），以及单靠结构化工具框架（Agent-Skills 0.387、Superpowers 0.410）几乎撼动不了基线（0.395）。

## Limitations

- 100 个任务（每类 20 个）相对于动辄上千实例的编码 benchmark 而言偏小；作者把这项工作定位为探索性的，并计划先扩充再宣称正式 benchmark 地位。
- **构念偏倚与循环论证。** 两位共同作者都是得分最高的 harness Agent-Rigor 的共同开发者，其中一位持有它的公开仓库。作者承认 Agent-Rigor 在 Planning Fidelity 上的优势「部分是构造出来的」，因为这些支柱度量的正是它在架构上就要求做到的行为，并呼吁独立复现。
- **LLM-as-judge 的循环性。** 定性子指标依赖单一 LLM judge，而该 judge 存在已记录的长度偏倚与自我偏好偏倚；未做任何 judge 与人类一致性的验证。
- **两根支柱的方差被压缩。** Abstention Quality 在所有 harness 上都聚在 0.56–0.57，因为 80 个非弃答任务一律记默认的中性值 0.50；Recovery Efficiency 被压缩，则是因为许多任务中的恢复实际上是二值的——要么立刻恢复，要么陷入循环直到超时。
- 过程与结果的相关只在 harness 之间显著，在同一 harness 内的任务之间并不显著，因此该 benchmark 并未表明「在某个任务上过程更好，就会提高该任务的成功概率」。
- 作为「有纪律」条件的只有一套纪律框架（Agent-Rigor），结果未必能推广到 AGENTS.md 配置或 Cursor Rules 等其他框架。
- 弃答任务里包含教科书式的不可能问题（如停机问题），作者指出这类问题很容易靠预训练里见过的模式直接匹配出来，因而作为真正认知谦逊的检验偏弱。
- *Repository note:* 论文标注日期为 2026 年 6 月，却两次声明结果与 agent 配置反映的是 agent「截至 2025 年 6 月」的状态；正文未解释这一出入。
- *Repository note:* arXiv v1 摘要描述的是 30 个任务、五根支柱，v2 描述的则是 100 个任务、七根支柱。凡引用本工作的数字，都应注明版本。

## Related Works

- [Harness-Bench](./harness-bench.md) — 同样是固定任务条件、变换外围系统，从而把 harness 这一层单独隔离出来。
- [Plan Compliance in Programming Agents](./from-plan-to-action.md) — 度量编码 agent 是否照给定计划行事，是 Planning Fidelity 支柱最接近的既有对应物。
- [AgentProcessBench](./agentprocessbench.md) — 对 agent trajectory 做 step 级过程评估，对照的是人工标注而非支柱 rubric。
- [SWE-bench](./swe-bench.md) — RigorBench 用以对照定位自身的、只看结果的编码 benchmark。
