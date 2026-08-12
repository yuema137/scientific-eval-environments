# Robotics

> [English](../../domains/robotics.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

在物理机器人平台与机器人控制上的评估。具身家居模拟器与 computer-use 环境不归入本领域。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| RoCo / RoCoBench | 2023 | 通过 LLM 协商的计划与路径点，协调多条机械臂完成共享的操作任务。 | MuJoCo 中 6 个带语义变体的协作操作任务，另有 269 题推理集；真实 UR5 演示。 | 任务成功率与语义变体下的适应性；计划在 MuJoCo 中执行并在物理 UR5 机械臂上演示。 | [→](../works/rocobench.md) |
| VIKI-Bench | 2025 | 协调异质机器人团队：选择激活哪些机器人、规划多 agent 动作、感知运动轨迹。 | 三层级的层级化视觉推理任务，覆盖 20,000+ 样本、100 个场景、6 种机器人形态（人形、四足、轮式机械臂）。 | 分层准确率与轨迹指标（RMSE、Hausdorff、方向性 Fourier），在模拟多机器人场景（RoboCasa、ManiSkill3）上。 | [→](../works/viki-bench.md) |
| REFLECT / RoboFail | 2023 | 从多传感器经验解释机器人操作失败，并引导纠正规划。 | 对注入失败场景的任务的失败解释与纠正回合（RoboFail）。 | 失败解释质量与纠正规划成功率，在模拟与真实世界机器人任务上评估。 | [→](../works/robofail.md) |
| AHA | 2024 | 以自由形式自然语言检测并推理机器人操作失败。 | 对程序化生成失败轨迹（79 个 RLBench 任务）的失败检测/推理；在真实世界失败数据上评估。 | 模糊语义匹配、ROUGE-L 与二元成功评分；泛化到真实世界失败数据集与未见任务。 | [→](../works/aha.md) |
| RoboFAC | 2025 | 跨理解、分析、纠正三环节分析并纠正机器人操作失败。 | 9,440 条错误轨迹、78,623 个 QA 对、53 个场景（模拟 + 真实）；八个 QA 维度。 | 按维度的失败分析准确率；作为监督者部署进真实世界 VLA 控制管线。 | [→](../works/robofac.md) |
| LabRobFail | 2026 | 跨控制、物理、语义层级分析化学自主实验室中的机器人失败。 | 20,000+ 条模拟轨迹、70+ 场景、5 个失败类别 / 11 种类型（Isaac Sim）。 | 六项能力分数，含检测（90.83%）与时间定位（77.21%）；作为监督者提升下游成功率 4–16 个百分点。 | [→](../works/labrobfail.md) |
| BadRobot | 2024 | 越狱具身 LLM 栈，使其执行恶意物理动作。 | 针对 Code-as-Policies、ProgPrompt、VoxPoser 等的 277 条恶意查询，覆盖六个危害类别。 | 操纵成功率（平均 68.57%）与危害性评分；在真实 UR3e 与 myCobot 机械臂上执行。 | [→](../works/badrobot.md) |
| ASIMOV | 2025 | 为充当机器人大脑的 VLM 评判情境与动作的语义安全。 | 对以伤害报告与视觉场景为依据的数据的静态安全判断，配生成的机器人宪法。 | 与人类偏好（合意性与安全性）的对齐率；使用生成宪法时最高 84.3%。 | [→](../works/asimov.md) |
| RoboSpatial | 2024 | 从真实场景理解机器人视角的空间关系——配置、语境、兼容性。 | 1M 图像、5K 3D 扫描、3M 空间关系；2D 与 3D 就绪评估集。 | 对照基线的下游空间任务表现；真实机械臂抓取成功率（52.6% vs 基线 23.7%）。 | [→](../works/robospatial.md) |
| PAC Bench | 2025 | 从任务可执行性角度理解操作前提——物体属性、affordance、约束。 | 30,000+ 条标注：673 张真实图像（115 类）、100 个人形机器人第一视角场景、120 个模拟约束场景。 | 前沿与开源 VLM 上按类别的准确率；真实机器人视角（Unitree G1）图像。 | [→](../works/pac-bench.md) |
| Robo2VLM | 2025 | 从机器人传感器上下文推理操作场景——空间、目标条件、交互。 | 取自 176K 条真实遥操作轨迹的 684,710 个选择题，覆盖 463 个场景、3,396 个任务。 | 由传感器（位姿、夹爪、力）导出真值、无需人工标注的选择题准确率。 | [→](../works/robo2vlm.md) |
| ManipBench | 2025 | 推理底层机器人动作，含物体间交互与可变形物体。 | 取自真实机器人数据、织物场景与模拟环境的 12,617 个选择题；33 个 VLM。 | 与真实世界操作任务表现相关联的选择题准确率。 | [→](../works/manipbench.md) |
| PhysBench | 2025 | 理解物理世界的属性、关系、场景与动力学，作为机器人 agent 的感知底座。 | 4 个领域、19 个子类、8 个能力维度的 10,002 条交错视频-图像-文本；75 个 VLM。 | 选择题准确率；演示向 MOKA 具身 agent 的迁移（静态 VQA，非机器人控制）。 | [→](../works/physbench.md) |
| CaP-X | 2026 | 通过合成并执行「感知 + 控制原语」的程序来控制机器人操作。 | 187 任务套件内的 7 个核心任务（+30 LIBERO-PRO、+2 BEHAVIOR）；12 个前沿模型跨抽象层级。 | 每个任务、每个抽象层级 100 次试验相对人类专家程序的成功率；配套方法迁移到真实 Franka Panda 与 AgiBot G1。 | [→](../works/cap-x.md) |
| VLA-Arena | 2025 | 把视觉-语言-动作模型作为通用机器人操作策略来评估，沿任务结构、语言指令与视觉观测三轴分解任务难度，以区分稳健的 grounding 与死记硬背。 | 四个维度（安全、干扰物、外推、长时程）下的 11 个任务套件 / 170 个模拟操作任务，各设三个难度级别（L0–L2），并带语言（W0–W4）与视觉（V0–V4）扰动探针；构建于 RoboSuite、LIBERO 与 VLABench 之上。 | 模拟中的成功率与累计成本；微调限于 L0、在未见的 L1–L2 上测试以衡量泛化。Repository note: 仅限模拟，未报告真实机器人实验。 | [→](../works/vla-arena.md) |
| RoboGraphBench | 2026 | 把 agentic 基础模型作为长时程具身任务（桌面操作与室内导航）的高层规划器来评估，以任务状态视野——agent 必须追踪、探索并更新的任务相关状态转移的跨度——刻画难度。 | 84 个家居场景上的 588 个 episode（399 个桌面 + 189 个室内导航），每个含一个基线加六种干预条件；RoboGraph 把任务编译为符号场景图（平均 18.4 个节点、14.3 个子目标）；15 个 agentic 模型。 | 统一闭环 harness（最多 100 步；目标谓词 + 停止动作），在语义与视觉两种模式（RoboTwin 2.0、RoboCasa）下运行；成功率与 SSAL，加上状态管理（维护/探索/更新）与恢复检测/grounding 指标。Repository note: 评估高层规划而非底层控制；仅限模拟。 | [→](../works/compiling-and-benchmarking-task-state-horizons-for.md) |

## Related Works

- [VLA-Arena](../works/vla-arena.md)
- [RoboGraphBench](../works/compiling-and-benchmarking-task-state-horizons-for.md)
- [RoCo / RoCoBench](../works/rocobench.md)
- [VIKI-Bench](../works/viki-bench.md)
- [REFLECT / RoboFail](../works/robofail.md)
- [AHA](../works/aha.md)
- [RoboFAC](../works/robofac.md)
- [LabRobFail](../works/labrobfail.md)
- [BadRobot](../works/badrobot.md)
- [ASIMOV](../works/asimov.md)
- [RoboSpatial](../works/robospatial.md)
- [PAC Bench](../works/pac-bench.md)
- [Robo2VLM](../works/robo2vlm.md)
- [ManipBench](../works/manipbench.md)
- [PhysBench](../works/physbench.md)
- [CaP-X](../works/cap-x.md)
