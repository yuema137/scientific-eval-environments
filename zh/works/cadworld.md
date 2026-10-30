# CADWorld (2026)

> [English](../../works/cadworld.md) | **简体中文**

> **首次公开：** 2026-09-14 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.16251)

## Overview

text-to-CAD 类 benchmark 给生成的脚本或形状打分，跳过了工程师实际的工作方式：在 GUI 里一步步把零件建出来，草图、约束、装配和分析设置都保存在项目文件里。CADWorld 把这个 GUI 交给 computer-use agent。agent 读取指令和参考图，通过截图和鼠标键盘操作 FreeCAD，然后保存成果。之后由宿主机上的脚本打开保存的 `.FCStd` 文件，检查几何、结构和建模历史；所有检查都通过，任务才算成功。

## Topics

- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)
- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** [CADWorld: Computer-Use Benchmark for Long-Horizon Computer-Aided Design](https://arxiv.org/abs/2609.16251)，2026 年预印本。
- **Full text:** <https://arxiv.org/html/2609.16251v1>
- **Project:** <https://cad-world.github.io>
- **Venue:** arXiv 预印本（cs.AI，2026）

## Summary

FreeCAD 运行在一台 Ubuntu 虚拟机里（8 核、8 GB 内存、1920×1080 屏幕）。每一步 agent 拿到指令、当前截图、可选的参考图和最近 10 轮记录，然后发出白名单内的 pyautogui 风格操作，或者 `WAIT`、`DONE`、`FAIL`；FreeCAD 脚本和直接访问文件系统都被禁止。最多 100 步之后，评测器读取保存的文件。草图任务检查图元、约束、尺寸、轮廓面积、周长和质心；装配任务检查关节类型；CAM 任务检查材料去除量以及过切和欠切比例；FEM 任务检查分析对象、材料、边界条件、网格、求解器和导出的结果。整个过程不用 LLM judge，也不用人工检查。任务的目标明确、素材已经给好，所以不涉及开放式的设计权衡。

## Tasks

200 个任务，涉及 183 个概念，分为 11 类工作流：Part 77、Sketch 63、Assembly 25、CAM 15、FEM 3、Appearance 3、点云 3、Macro 3、Measure 3、Mesh 3、TechDraw 2。任务依据 FreeCAD 工作台的功能、教程、文档和常见的机械设计流程编写；编写任务、准备初始文件、设计评测器和人工检查，总共花了约三个月、1,300 人时。TODO(reference)：任务编写者的人数和背景。

## Domains

机械 CAD：带约束的草图，零件建模（凸台、凹槽、旋转、放样、扫掠、圆角），带旋转副、滑动副和齿轮齿条关节的装配，CAM 刀具路径，有限元分析设置（Gmsh 加 CalculiX），网格处理，以及工程图。

## Evaluation

- **打分方式：** 对保存的项目文件和辅助输出做确定性检查；只算成败，不给部分分。体积误差、包围盒 IoU、质心距离等连续诊断指标会记录下来，但不计入分数。每个失败的轮次都会被确定性地归入 11 种失败原因之一，比如没有输出文件、文档结构错误、建模过程错误。
- **成功率 / 完成率：** 专家参考 87.0% / 100%；GPT-5.4（CUA）17.5% / 62.5%；Opus 4.8（CUA）16.0% / 49.5%；Kimi K2.6 7.5% / 20.5%；OpenCUA 1.5% / 8.0%；Holo 3.1 0.5% / 21.5%；Qwen3.6 0.0% / 3.0%；MiniMax M3 0.0% / 2.5%。
- 所有模型在 CAM、FEM 和 TechDraw 任务上都是 0%。
- **失败规律：** 较弱的 agent 大多在保存出有效文件之前就失败了，经常陷入重复操作的循环；较强的 agent 更多是在结构、几何或建模过程上出错。各类失败原因的数量在图中给出。
- **只用终端的消融（50 个任务）：** 不带 computer-use harness 的 GPT-5.4 一个任务也没完成，失败大多是文档结构错误。
- Repository note：v1 引言里说最强 agent 的成功率是 25.0%，还提到一个 60 题的预算受控子集，而摘要和结果表给出的是在完整 benchmark 上的 17.5%；本卡片以结果表为准。

## Typical Duration

每个任务最多 100 步 GUI 操作，每步默认最多输出 512 个 token。没有规定实际时间预算。TODO(reference)：每个任务的平均步数或耗时。

## Main Contribution

一个在 FreeCAD 中做机械 CAD 的长时程 computer-use benchmark，覆盖草图、建模、装配、CAM 和 FEM 等工作流，完全通过对保存的项目文件做可执行检查来打分。

## Key Design Ideas

- 打分读取的是保存的项目文件，所以不光最终形状要对，模型的结构和建模历史也要对，任务才算通过。
- 禁用脚本和文件系统访问，agent 只能通过 GUI 得到结果。
- 连续的几何诊断指标和成败分数分开记录，专门用于失败分析。
- 失败原因由评测器的输出确定性地判定。

## Strengths

- 打分完全确定，不用 judge。
- 有实测的专家参考操作作为成功率的参照。
- 失败分类把“没保存出文件”和“保存的文件结构或几何不对”区分开。

## Limitations

- 作者说明，任务目标明确、素材已给，不涉及需求挖掘和设计权衡。
- 只用了 FreeCAD，能否迁移到商业 CAD 软件没有测试。
- 人类这一行只是一次专家参考操作，不是对照的人类被试研究。
- FEM 只有 3 个任务，TechDraw 只有 2 个，这两类的结果依据的题目很少。
- 不同模型的接口、上下文长度和服务延迟各不相同，会影响效率上的比较。

## Related Works

- [EngiWorld](./engiworld.md) — 同样在专业软件里对 CAD、CAM 和 CAE 工作打分，并用程序检查产出文件。
- [OSWorld](./osworld.md) — 通用的 computer-use 环境，动作接口同样是截图加 pyautogui。
- [OSWorld-Science](./osworld-science.md) — 同样是面向科学和工程软件的 computer-use benchmark。
