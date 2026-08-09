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

## Related Works

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
