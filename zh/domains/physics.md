# Physics

> [English](../../domains/physics.md) | **简体中文** · [← 全部 domains](./README.md)

## Scope

以物理定律、物理仿真或实验物理为基础的评估环境。粒子物理、核物理、量子物理与流体物理折并于此。

## Comparison

| Work | 年份 | 科学问题 | 任务形式与规模 | 领域内验证 | Card |
|---|---|---|---|---|---|
| MaD Physics | 2026 | 推断支配模拟系统的未知——有时被刻意改变的——物理定律，覆盖经典力学（D 维中的 N 粒子）、2D 不可压缩粘性流体与 2D 势箱中的两个量子粒子。 | 在三个模拟环境中交互实验；每次观测按保真度级别花费 2 / 5 / 10，受固定的单 trial 预算约束。 | 相对真实未来状态的预测误差：经典力学用归一化 RMSE，流体/量子用涡量/概率密度上的 L2 误差，在 33 个随机初始化上取平均。 | [→](../works/mad-physics.md) |
| NewtonBench | 2025 | 重新发现一条隐藏物理定律：对 12 条经典定律（万有引力、库仑、傅里叶、Snell 等）的表达式树做反事实变异得到。 | 324 个交互任务（108 条变异定律 × 3 个模型系统）；agent 通过 `run_experiment` 工具设计实验，以符号表达式提交定律。 | 与真值定律的二元符号等价（LLM judge；与人类专家一致率 98.3%），辅以所发现方程预测的 RMSLE。 | [→](../works/newtonbench.md) |
| PRBench | 2026 | 端到端复现已发表的物理研究——理解论文方法、从零实现算法、复现其定量结果——覆盖从 QCD 到凝聚态的 11 个子领域。 | 30 个专家整理的论文复现任务，来自 20 余个课题组，在沙箱执行环境中运行，输出标准化 CSV。 | 每任务由专家撰写的加权 rubric 评分（数据复现准确性权重 0.60）；端到端成功要求每个维度 >0.9——目前所有 agent 均为零。 | [→](../works/prbench.md) |
| Collider-Bench | 2026 | 复现 LHC 实验分析：通过公开仿真栈（MadGraph5、Pythia、Delphes）为 CMS 超对称搜索生成信号事例，并实现论文发表的事例筛选。 | 10 个 Simulation 任务，取自 13 TeV 下四项 CMS SUSY 搜索；agent 提交预测信号产额的分 bin 直方图、分析代码与方法报告。 | 与隐藏参考直方图的相对 L² 距离，通过阈值由 physicist-in-the-loop 基线设定；另有 LLM 溯源评判标记造假工作流。 | [→](../works/collider-bench.md) |
| SimulCost | 2026 | 在 13 个物理仿真器上调节仿真参数以达到目标物理结果，并计入仿真时间与实验资源成本。 | 2,947 个单轮与 1,931 个多轮参数调优任务。 | 预算约束下的成功率，并分层报告更严格的精度要求。 | [→](../works/simulcost.md) |
| NatureBench | 2026 | 达到 Nature 系列 Physical Modeling 研究的已发表 SOTA——其 90 个任务中的 13 个——只给目标算法的输入，不给其操作或输出。 | 经评审门控流水线与信息防火墙构建的 code-agent 任务；每任务平均约 3.7 个主指标。 | 在论文自身主指标上的 SOTA 归一化相对差距 g；报告 Match-SOTA（g ≥ 0）与 Surpass-SOTA（g > 0.1）比率，另有 judge 标记捷径运行。 | [→](../works/naturebench.md) |
| Terminal-Bench Science | 2026 | 五大分组的终端科学工作流套件中，Physical Sciences 分组下的物理任务。 | 容器化终端任务（发布时五大分组共 8 个，目标 100+），社区贡献并经三重审批验证门。 | 容器化执行环境中的确定性 pytest 验证。 | [→](../works/terminal-bench-science.md) |
| ResearchClawBench | 2026 | 从任务描述、相关文献与原始数据中重新发现一篇隐藏已发表论文的结论——Physics 是其 10 个领域之一（共 40 个任务）。 | 端到端自主研究任务，每个任务锚定一篇评估期间保持隐藏的真实论文；agent 产出最终研究报告。 | Reference-Anchored Discovery Score（0–100；50 为参考文献级证据），对照锚定隐藏论文工件的专家多模态 rubric，由 GPT-5.1 评判。 | [→](../works/researchclawbench.md) |

## Related Works

- [MaD Physics](../works/mad-physics.md)
- [NewtonBench](../works/newtonbench.md)
- [PRBench](../works/prbench.md)
- [Collider-Bench](../works/collider-bench.md)
- [SimulCost](../works/simulcost.md)
- [NatureBench](../works/naturebench.md)
- [Terminal-Bench Science](../works/terminal-bench-science.md)
- [ResearchClawBench](../works/researchclawbench.md)
