# Electrical Engineering

> [English](../../domains/electrical_engineering.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

电气与电子工程。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Engineering Sciences 分组下的电气工程任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| VerilogEval | 2023 | 生成满足功能规格的 Verilog RTL。 | 156 个 HDLBits 问题；LLM 生成 RTL，经与参考解仿真检验。 | 与参考解仿真对比的功能正确性；pass@k。 | [→](../works/verilogeval.md) |
| RTLLM | 2023 | 从自然语言指令生成完整设计级 RTL。 | 29 个手工设计（v2.0 为 50 个），按三个递进目标判分。 | 语法、功能、设计质量目标；在 GPT-3.5 上评估 self-planning 提示。 | [→](../works/rtllm.md) |
| RTL-Repo | 2024 | 补全契合大型多文件设计项目的 Verilog 代码。 | 4,000+ 来自公开 GitHub 的 Verilog 样本，每个附完整仓库上下文。 | 相对参考补全的编辑相似度与精确匹配。 | [→](../works/rtl-repo.md) |
| VHDL-Eval | 2024 | 据问题描述生成功能正确的 VHDL。 | 202 个问题（Verilog 翻译 + 汇总公开），配自验证测试台。 | 零样本、上下文学习与 PEFT 设定下的功能正确性。 | [→](../works/vhdl-eval.md) |
| CVDP | 2025 | 求解综合的 RTL 设计、验证与调试问题。 | 783 问题 / 13 类别（NVIDIA），兼有非 agent 与 agent 格式。 | 容器化开源 EDA 环境中的 pass@1；代码生成 SOTA ≤34%。 | [→](../works/cvdp.md) |
| AssertionBench | 2024 | 为数字设计生成功能正确的硬件断言。 | 100 个 OpenCores Verilog 设计，配经形式验证的参考断言。 | 对照 GoldMine/HARM 参考的功能正确断言比例。 | [→](../works/assertionbench.md) |
| FVEval | 2024 | 为数字硬件执行形式验证任务。 | 三个子任务（NL2SVA-Machine、NL2SVA-Human、Design2SVA），配预生成数据集。 | 用 Cadence Jasper 形式工具校验断言/测试台的正确性。 | [→](../works/fveval.md) |
| HLS-Eval | 2025 | 生成并优化高层综合硬件代码。 | 94 个配自然语言描述与测试台的 HLS 设计；两类任务。 | 在 Vitis HLS 上的可解析/可编译/可运行/可综合 + pass@k。 | [→](../works/hls-eval.md) |
| AnalogCoder | 2024 | 经免训练的 Python 代码生成设计模拟电路。 | 精选模拟设计任务集（官方仓库 24 个任务）。 | 按解出任务数排名的 Pass@1/Pass@5；20 个电路对 GPT-4o 的 15 个。 | [→](../works/analogcoder.md) |
| AnalogXpert | 2024 | 据设计需求综合模拟电路拓扑。 | 30 个真实 + 2,000 个合成拓扑案例；SPICE 代码表示。 | 单次结构正确性（程序化 + 人工评审）；40%/23% 对 GPT-4o 3%。 | [→](../works/analogxpert.md) |
| EEE-Bench | 2024 | 求解需理解电路与框图的多模态 EE 问题。 | 横跨 10 个 EE 子领域的 2,860 个问题，含复杂电路/系统框图影像。 | 17 个 LLM/LMM 的准确率（平均 19.48–46.78%）；「偷懒」文本压过视觉分析。 | [→](../works/eee-bench.md) |
| MMCircuitEval | 2025 | 回答跨 EDA 设计流程的电路问题。 | 横跨数字与模拟电路及 EDA 阶段的 3,614 个多模态问答对。 | 按设计阶段、电路类型、所测能力与难度的准确率。 | [→](../works/mmcircuiteval.md) |
| TeleQnA | 2023 | 回答以标准为依据的电信知识问题。 | 取自 3GPP/IEEE 标准与研究文献的 10,000 道选择题。 | 对照在职电信专业人士基线的选择题准确率。 | [→](../works/teleqna.md) |
| ControlAgent / ControlEval | 2024 | 设计满足稳定性与性能规格的控制器。 | 500 个控制设计任务（ControlEval），横跨一/二阶、时滞与高阶系统。 | 对照设计判据、相对「工具箱+人工」基线的平均与 agent 成功率。 | [→](../works/controleval.md) |
| PDAgent-Bench | 2026 | VLSI 物理设计 / 电子设计自动化——芯片后端实现，涵盖布图规划、供电规划、布局、时钟树综合、布线、静态时序分析与工程变更单。 | 353 个精选的任务级问题，横跨五个能力维度（基础知识、报告理解、根因分析、静态时序分析、脚本生成），另加 10 个全流程设计项目，使用 TSMC 28nm / Nangate 45nm 及 Cadence Innovus、Synopsys ICC2/PrimeTime、OpenROAD 等工具；11 个模型。 | 任务级 pass@1/pass@5：脚本解经执行检查、概念性答案对照三位专家验证的参考评分；工作流级全流程运行则按 TinyRISCV、AES-256、Ethernet MAC 等设计上的时序收敛与 DRC 违规结果评估。 | [→](../works/pdagent-bench.md) |
| ERI Benchmark | 2026 | 电气工程是其覆盖的九个领域之一，下设六个子领域：电路、电子学、信号与系统、电力系统、电磁学与控制系统。 | 按「领域 × 子领域 × 意图 × 难度」的受控组合生成 57,750 条指令–回答记录（共 1,155 种组合，每种 50 对），各领域的均分单独报告。 | 先由自动检查筛出拒答、缺最终答案与可机器解析的约束违规，再由三家厂商的模型组成评审团（Claude Haiku 4.5、GPT-4.1 Mini、Mistral Small 3）按 rubric 打分并逐题取均值。 | [→](../works/eri-benchmark.md) |
| EngDesign | 2025 | 把电气与电子设计写成带目标、约束与性能要求的规格——控制设计、数字硬件设计、模拟 IC 设计与信号处理。 | 九个工程方向共 101 项设计任务、473 个可评分条目，其中控制设计 18 项、信号处理 18 项、数字硬件设计 17 项、模拟 IC 设计 5 项；101 项中有 48 项需要 MATLAB、Cadence 等商业领域软件。 | 模型输出结构化结果，由逐任务脚本调用相应仿真器（MATLAB、SPICE/Cadence）执行，返回二元通过/不通过、0–100 的部分给分与评估日志；模拟 IC 设计被报告为九个方向中最弱的一个。 | [→](../works/engdesign.md) |

## Capability Matrix

同一批工作的清单视图：每项工作把什么纳入了评测，又漏掉了什么。它回答的问题与上面的 Comparison 表不同——不是**考的是什么科学**，而是**一套评测设置覆盖了哪些维度**。

**符号。** `✔` 具备 · `✘` 明确不具备 · `◐` 部分具备、可选，或只在部分任务上成立 · `?` 卡片与原始文献均未说明。`?` 表示原文没有交代，不等于"没有"；它是一份待核实清单，不能当作默认值。 `Domain`、`Verif`、`Scale` 与 `Fail` 不是是非列——见下文。

**`Domain`** 列出该工作实际评测的电子电气工程子领域，取自卡片的 `## Domains` 段落。这套缩写只属于本页——每个 domain 页各自定义，毕竟一个领域的子领域和另一个领域的彼此说不上话。

`DIG` 数字设计与 RTL 代码生成 · `VER` 硬件验证与断言 · `HLS` 高层次综合 · `EDA` EDA 工具链与 VLSI 物理设计 · `ANA` 模拟与数模混合电路设计 · `SS` 信号与系统、信号处理 · `COMM` 通信与电信 · `CTRL` 控制系统 · `GEN` 覆盖整个课程体系或未具体说明，无单一子领域

**两个分，不是一个。** 各列分成**覆盖面**——评测设置把什么纳入了考察——与**严谨度**——它报出来的东西有多可信。两者分开求和，因为它们方向相反：一个 benchmark 可以什么都考一点却什么都没验扎实，而一个刻意收窄的 benchmark 反而可能是本页最可信的。各行按 `Cov` 从高到低排，`Cov` 相同时比 `Rig`，仍相同则保持 Comparison 表原序。以覆盖面领先排序，是因为读者扫表时先问的就是这件事——*这个 benchmark 到底有没有把我关心的问题纳入考察*——`Rig` 随后回答它报出的东西能信到什么程度。

### 覆盖面（`Cov`，满分 7）

是非列，按稀缺程度排序——做到的工作越少排得越靠前，因此这一组的左侧就是该领域的薄弱处。几乎人人都满足的性质不设列：*是否编写并运行代码* 就是因此删去的。

- **Net** — 允许联网或实时外部检索；给定的固定语料库不算。
- **E2E** — 端到端研究：只给问题或目标，不提供源论文、参考实现或分步规范，整个研究过程由 agent 自己推进。
- **Cost** — 预算或资源成本被计入评分或明确定价，仅有步数上限不算。
- **MM** — 多模态内容是承重的，要么必须作为输入，要么作为产出物被打分。
- **Repro** — 以某项已发表结果为准，agent 需要复现或还原它。
- **Real** — 使用真实实验或观测数据，而非合成或仿真数据（数字孪生算仿真）。
- **Inter** — 交互式：agent 对环境、工具或仿真器多次动作，并根据反馈决定下一步。

### 严谨度（`Rig`，满分 13）

- **Human** — 有实测的人类专家基线或人类参考表现为整个量表定锚。若锚点只是一篇已发表结果或专家参考实现，而非实际跑出来的人类成绩，记 `◐`。
- **Rubric** — 专家撰写的 rubric 或官方评分标准，带具名维度或权重；连续型自动指标不算 rubric。
- **Contam** — 有刻意设计的机制让答案无法靠记忆得到：取材于训练截止之后、未发表或新撰写的题目、反事实改写、按需生成，或做过泄漏筛查。评测时把一篇已发表论文藏起来记 `◐`——藏起来并不能把它从预训练语料里去掉。
- **Verif** `0`–`3` — 这个分数要在多大程度上依赖对某个模型的信任。`0` 仅由 LLM judge 或 rubric 打分，且该判分器未经验证 · `1` judge/rubric 打分，且报告了与人类专家的一致性 · `2` 确定性校验与 judge/rubric 并用 · `3` 完全确定性——执行、测试、与参考解做数值比对、符号检查或证明内核，全程无 judge 介入。它取代了原先"有无确定性验证"的是非列：那一列 85% 的工作都满足，因而区分不出任何东西；做成阶梯后区分度很高。另有一个 `Judge` 列因与 `Verif` < 2 几乎等价而删去。
- **Scale** `0`–`3` — **本领域内**受评的条目数：`0` 少于 10 · `1` 10–99 · `2` 100–999 · `3` 1,000 及以上 · `?` 原文未给出逐领域计数。它数的是条目而非工作量：30 个论文复现任务远比 3,000 道考试题费力，这一列看不见这一点。
- **Fail** `0`–`4` — 失败分析做到多深，因为"论文有失败分析"这句话的跨度太大——从一句话带过到专门设计的对照实验都算。`0` 除成绩外没有任何失败分析 · `1` 只有关于模型薄弱环节的叙述性评论，未给出类别 · `2` 有具名的错误类别或示例性案例分析，但没有计数或占比 · `3` 定量的失败刻画：带逐类计数或占比的分类体系，或能分离出特定失败条件的实测拆分 · `4` 在第 3 级之上，另有专门设计的对照实验或消融，用来检验失败*为何*发生。

### 怎么读这两个分

是非列按 `✔` 1 分、`◐` 0.5 分、`✘` 0 分、`?` 0 分计；分级列直接计其数值，`?` 计 0 分。`Domain` 不计分。

三点要留意。`?` 与 `✘` 的代价完全相同，所以两个分都是"该工作*可查证地*做到了多少"的下界，而不是对它的判决。两个分也都不是质量排名：`Cov` 高而 `Rig` 低，说的是这个 benchmark 什么都想够到却什么都没钉死；`Cov` 低而 `Rig` 高，说的是它把一件窄事量得很仔细——哪一种才是对的设计，完全取决于要回答什么问题。还有，`Cov` 描述的是*评测设置*而非科学本身：一份工作可以排在本表末尾，同时是它那个子领域最重要的论文。

跨领域套件的行按本领域的切片来写，与上面的 Comparison 表一致。
| Work | Domain | Net | E2E | Cost | MM | Repro | Real | Inter | Cov | Human | Rubric | Contam | Verif | Scale | Fail | Rig |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PDAgent-Bench | EDA | ✘ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | **3** | ✘ | ✔ | ◐ | 2 | 2 | 3 | **8.5** |
| EngDesign | CTRL, DIG, ANA, SS | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✔ | **1.5** | ✘ | ◐ | ✔ | 3 | 1 | 3 | **8.5** |
| AnalogXpert | ANA | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✔ | **1.5** | ✘ | ✘ | ✘ | 3 | 3 | 2 | **8** |
| ControlAgent / ControlEval | CTRL | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | ✔ | **1.5** | ◐ | ✘ | ✘ | 3 | 2 | 1 | **6.5** |
| RTL-Repo | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✔ | 3 | 3 | 3 | **10** |
| EEE-Bench | GEN | ✘ | ✘ | ✘ | ✔ | ✘ | ✘ | ✘ | **1** | ✘ | ✘ | ✘ | 2 | 3 | 4 | **9** |
| AssertionBench | VER | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ | **1** | ✘ | ✘ | ✘ | 3 | 2 | 2 | **7** |
| AnalogCoder | ANA | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 1 | 2 | **6** |
| Terminal-Bench Science | GEN | ? | ✘ | ✘ | ✘ | ✘ | ? | ✔ | **1** | ✘ | ✘ | ✘ | 3 | 0 | 0 | **3** |
| CVDP | DIG, VER | ? | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | **0.5** | ✘ | ✘ | ✔ | 2 | 2 | 3 | **8** |
| FVEval | VER | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ◐ | ✘ | ◐ | 3 | 2 | 2 | **8** |
| MMCircuitEval | DIG, ANA, EDA | ✘ | ✘ | ✘ | ◐ | ✘ | ✘ | ✘ | **0.5** | ✘ | ✘ | ✘ | 2 | 3 | 3 | **8** |
| HLS-Eval | HLS | ✘ | ✘ | ✘ | ✘ | ✘ | ◐ | ✘ | **0.5** | ✘ | ✘ | ✘ | 3 | 1 | 0 | **4** |
| TeleQnA | COMM | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✔ | ✘ | ✘ | 3 | 3 | 3 | **10** |
| ERI Benchmark | GEN | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✔ | ✔ | 2 | 2 | 3 | **9** |
| VHDL-Eval | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ◐ | 3 | 2 | 1 | **6.5** |
| VerilogEval | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ✘ | ✘ | ✘ | 3 | 2 | 1 | **6** |
| RTLLM | DIG | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | ✘ | **0** | ◐ | ✘ | ✘ | 3 | 1 | 1 | **5.5** |
Repository note: 有两行不属于其余各列所预设的 agent 场景。RealPDEBench 评的是科学机器学习代理模型而非 agent，其"任务设定"几列描述的是一套离线训练与评测流程。SciVQR 是静态多模态问答，没有 agent、工具调用或环境交互。

Repository note: 几乎所有未知都集中在两列。`Net` 在 47 行中有 35 行为 `?`，这也正是它排在覆盖面一组最前的原因——本领域几乎没有工作被明确记载允许实时检索，而大多数干脆不提；为核这一列，其中十一篇的全文都读过，没有一篇给出说法。`Scale` 有 12 行为 `?`，无一例外都是跨领域套件：给了任务总数，却不给逐领域拆分。两列都如实记录这种沉默，而不靠推断把它填掉；而在两列上，沉默都实实在在地扣掉了这些工作的分数。另有两格仍为 `?`：SciCode 与 Terminal-Bench Science 的 `Real`。

## Related Works

- [PDAgent-Bench](../works/pdagent-bench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [VerilogEval](../works/verilogeval.md)
- [RTLLM](../works/rtllm.md)
- [RTL-Repo](../works/rtl-repo.md)
- [VHDL-Eval](../works/vhdl-eval.md)
- [CVDP](../works/cvdp.md)
- [AssertionBench](../works/assertionbench.md)
- [FVEval](../works/fveval.md)
- [HLS-Eval](../works/hls-eval.md)
- [AnalogCoder](../works/analogcoder.md)
- [AnalogXpert](../works/analogxpert.md)
- [EEE-Bench](../works/eee-bench.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [TeleQnA](../works/teleqna.md)
- [ControlAgent / ControlEval](../works/controleval.md)
- [ERI Benchmark](../works/eri-benchmark.md)
- [EngDesign](../works/engdesign.md)
