# EngiWorld (2026)

> [English](../../works/engiworld.md) | **简体中文**

> **首次公开：** 2026-09-29 · **来源：** [arXiv 首次提交](https://arxiv.org/abs/2609.37686)

## Overview

给语言模型做的工程类 benchmark，通常检查的是算出来的答案或生成的脚本。可真实的工程工作，最后交付的是某个专业软件里做出来的文件：SolidWorks 里的实体模型，Abaqus 里的网格和载荷工况，KiCad 里的电路板布局。EngiWorld 让 agent 通过图形界面或命令行操作 26 款专业软件，再由 verifier 打开 agent 产出的文件，检查几何、物理可行性和设计规则。只有全部验收条件都通过才算完成任务，所以一次运行哪怕最后写了一份像样的报告，只要文件不合格，得分就是零。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)
- [General Long-Horizon Agent Benchmarks](../topics/long_horizon_evaluation.md)

## Activities

- [优化与工程设计](../activities/optimization_engineering_design.md)
- [模拟与科学计算](../activities/simulation_scientific_computing.md)

## Links

- **Paper:** [EngiWorld: What Can Frontier Agents Deliver in Professional Engineering Environments?](https://arxiv.org/abs/2609.37686)，2026 年预印本（v2 发布于 2026-10-09）。
- **Full text:** <https://arxiv.org/html/2609.37686v1>
- **Project:** <https://engiworld.github.io>
- **Venue:** arXiv 预印本（cs.AI、cs.CL，2026）

## Summary

领域专家从软件文档、教程和工程资料里挑出实际工作流程，写成可执行的任务说明；每个最终任务都在对应软件里实际跑过并经过审核。agent 拿到任务说明后，要么用 PyAutoGUI 在 1920×1080 的桌面上操作，要么用终端命令和脚本完成。agent 宣布完成后，程序化的 verifier 会读取产出文件（比如借助 CadQuery/OCCT、IfcOpenShell 或 Abaqus odbAccess），检查尺寸、拓扑、材料和载荷设置、仿真结果是否在误差范围内，以及多个文件之间是否一致。定量设计任务要先过可行性门槛，才能拿部分分。在评测子集上，最好的 agent 得 44.3 分（满分 100），跨软件任务 168 次尝试只成功了 6 次。

## Tasks

共 1,301 个专家整理的任务，覆盖六个领域（CAD、CAE、CAM、BIM、EDA 和 3D 可视化）和 26 款软件，任务与软件的对应关系共 1,723 条。CLI 任务 691 个，GUI 任务 610 个。按类型分：单软件 931、多软件 60、软件选择 140、定量设计 40、基于图像的建模 120、开放式 10。软件包括 CAD（FreeCAD、AutoCAD、SolidWorks、BRL-CAD、OpenSCAD、LibreCAD、SolveSpace）、CAE（ANSYS、Abaqus、OpenFOAM、FEniCS、CalculiX、FLORIS、OpenFAST）、CAM（FreeCAD Path、SolidCAM）、BIM（Archicad、Bonsai、OpenStudio、Revit）、EDA（Cadence OrCAD、EAGLE、Altium Designer、KiCad）和 3D 可视化（Blender、ZBrush）。模型评测用的是其中 300 个任务的子集（CLI 152 个，GUI 148 个）。TODO(reference)：各领域任务数，以及专家人数和资历。

## Domains

机械设计与制造（CAD 实体建模、CAM 刀具路径）、计算机辅助工程分析（有限元和 CFD 求解器）、建筑信息模型、电路板的电子设计自动化，以及 3D 可视化。

## Evaluation

- **二值任务：** 所有验收条件都通过才算成功。
- **定量任务：** 不可行的输出记 0 分；可行的输出得 Qᵢ = clip₀₋₁((m − m_base) / (m_ref − m_base))。
- **EngiScore：** 在评测任务上计算 100/|D| × (二值任务成功数之和 + 定量任务得分之和)。
- **不用 LLM 或 VLM 做 judge。** verifier 的验证结果：96 个参考文件全部通过，40 + 40 + 5 个另行构造的合格文件被接受，21 + 21 个有缺陷的提交（空文件或只有指标）被拒绝。预期结果的标注由第二位标注者独立复核，但论文没有给出一致性统计。
- **结果（EngiScore 总分 / GUI / CLI）：** Claude Opus 5 为 44.3 / 40.5 / 47.9；GPT-5.6 Sol 为 38.0 / 28.6 / 47.1；Qwen 3.8 Max 为 25.8 / 16.6 / 34.7；DeepSeek V4.1 Flash 为 25.5 / 2.0 / 48.3；Gemini 3.7 Flash 为 25.3 / 14.2 / 36.1；Kimi K3 为 24.1 / 16.7 / 31.3；Qwen 3.8 Flash 为 16.1 / 1.0 / 30.8。对所有模型来说，CAM 都是最难的领域。
- **失败分析：** 失败分为五类：宣布完成但得零分（DONE）、决策轮数用尽、明确报告失败、超出运行时间，以及桌面意外关闭。其中 DONE 零分和轮数用尽两类合计占 94.1%；在 GPT 的失败里 DONE 占 87.0%，在 Claude 的失败里占 73.9%。轮数用尽在 GUI 失败中占 55.3%，在 CLI 失败中占 36.6%。
- Repository note：arXiv 摘要页（当前版本）写的最好成绩是 44.7，v1 结果表里是 44.3。

## Typical Duration

决策轮数上限为 GUI 200 轮、CLI 100 轮，多软件任务和开放式任务放宽到 300 和 150 轮；运行时间上限为五小时，有 28 次 DeepSeek 运行和 9 次 Claude 运行碰到了这个上限。每题步数从 54.9（GPT）到 120.5（Qwen 3.8 Flash）不等，每题成本从 0.45 美元（Qwen 3.8 Flash）到 19.02 美元（Claude）不等。

## Main Contribution

一个按 agent 在专业 GUI 和 CLI 软件里做出的工程文件来打分的 benchmark，用领域 verifier 代替答案比对或 judge。

## Key Design Ideas

- 同一套任务同时支持 GUI 和 CLI 两种操作方式，同一个模型在两种界面下的得分可以直接比较。
- verifier 检查的是文件本身（实体是否有效、实体与空腔的占位、边界条件、仿真输出），而不是 agent 对文件的描述。
- 定量设计任务先过可行性门槛，再给部分分。
- 多软件任务和软件选择任务考察 agent 能否在不同工具之间接续工作。

## Strengths

- 验证是程序化的，并且用参考文件、其他合格文件和有缺陷文件做过检验。
- GUI 和 CLI 分开报告，暴露出有些模型两者差距很大（DeepSeek V4.1 Flash：GUI 2.0，CLI 48.3）。
- 失败统计显示，大多数失败是 agent 宣布成功但文件不合格，或者轮数用完了。

## Limitations

- 模型只在 300 个任务的子集上评测，没有跑完全部 1,301 个任务。
- 论文没有报告各领域任务数、人类基线，也没有说明防污染措施。
- 论文指出，看上去正确的文件仍可能没法用，所以能测到什么取决于 verifier 的验收条件。
- Repository note：v1 全文中没有单独的局限性章节。

## Related Works

- [EngDesign](./engdesign.md) — 同样用基于仿真的检查给工程设计结果打分，但通过脚本而不是专业软件完成。
- [AEC-Bench](./aec-bench.md) — 同样评测 agent 在建筑、工程和施工领域产出的文件。
- [PDAgent-Bench](./pdagent-bench.md) — 同样评测 agent 操作 EDA 工具。
