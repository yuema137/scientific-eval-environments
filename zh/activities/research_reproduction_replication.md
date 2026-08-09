# 研究复现与重复

> [English](../../activities/research_reproduction_replication.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 复现、重建、验证或重复已有科学结果的能力——重现已发表的分析、重实现某方法以匹配其结果，或从公开信息重建结果。

## Scope

有意跨活动，常与模拟、数据分析或科学软件与工作流工程共现。仅当复现/重复本身即为任务时才归入此类，而不因 benchmark 将输出与参考答案对照就归入。

## Task Patterns

有一批成员针对 **ML/AI 研究论文**进行复现或复制，任务难度从让现有代码库能够跑起来，到完全从零开始的复制不等。[SUPER](../works/super.md) 聚焦于运行真实 ML/NLP 代码库时"配置与执行"这一瓶颈环节，[PaperBench](../works/paperbench.md) 要求依据由论文作者共同参与制定的评分细则，从零复制 ICML 2024 的论文，而 [FIRE-Bench](../works/fire-bench.md) 则要求 agent 仅凭一个研究问题，重新发现已发表的 ML 研究成果。这些工作与 Scientific Software、Data Analysis 高度共现，并普遍依赖 LLM-as-judge 的评分方式。

第二类工作借助开源软件和专用工具链，复现 **physics、astro 和 materials 领域的结论**，与 Simulation、Scientific Software 强烈共现。[ReplicationBench](../works/replicationbench.md) 面向 astrophysics 论文的复制，[PRBench](../works/prbench.md) 从零重新实现 physics 算法以匹配已发表的数值结果，[Collider-Bench](../works/collider-bench.md) 将 LHC 搜索实验重构到一套公开的仿真技术栈中，并以直方图的拟合度打分，而 [AutoMat](../works/automat.md) 则跨 DFT/MD/ML 工作流复现 computational materials science 的结论。

第三类工作**基于提供的代码与数据来复现研究结果**，或对标已发表的 SOTA。[CORE-Bench](../works/core-bench.md) 利用论文自身公开发布的代码与数据，在 CS、social science 和 medicine 领域重新运行已发表的研究，而 [NatureBench](../works/naturebench.md) 则超越了单纯的复现，力求在六大领域匹配 Nature 系列论文所发表的 SOTA 水平。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| CORE-Bench | 2024 | 基于公开的代码与数据复现已发表的研究结果 | 来自 90 篇论文的 270 个任务，3 个难度等级，涵盖 language 与 vision | 计算可复现性准确率（最高难度约 21%） | [卡片](../works/core-bench.md) |
| SUPER | 2024 | 从真实研究代码库中配置并执行任务 | 45 个端到端 + 152 个子任务 + 602 个自动生成的 ML/NLP GitHub 问题 | 端到端成功率（GPT-4o 16.3%） | [卡片](../works/super.md) |
| PaperBench | 2025 | 从零复制 SOTA AI 论文 | 20 篇 ICML 2024 论文，8,316 个评分细则任务，sandbox | 按评分细则打分的复制得分（最高 21.0%） | [卡片](../works/paperbench.md) |
| ReplicationBench | 2025 | 复制 astrophysics 论文的核心贡献 | 覆盖 20 篇论文的 111 个任务，计算 sandbox | 忠实度 + 正确性得分（最高 <20%） | [卡片](../works/replicationbench.md) |
| AutoMat | 2026 | 端到端复现 computational materials science 的结论 | 85 个由 SME 精选的结论，具备 HPC 代表性、资源受控的环境 | 可复现性得分 / 成功率（最高 54.1%） | [卡片](../works/automat.md) |
| Collider-Bench | 2026 | 基于公开软件重构已发表的 LHC 对撞机搜索实验 | 10 个 Simulation 任务，四项 CMS SUSY 搜索，容器化技术栈 | 相对隐藏参考产额的连续直方图拟合度 | [卡片](../works/collider-bench.md) |
| FIRE-Bench | 2026 | 从 ML 论文中重新发现已确立的研究成果 | 40 个可执行任务 + 60 篇论文的题库，24 小时/A100 的轻量算力 | 基于参考的重新发现得分（最高 <50 F1） | [卡片](../works/fire-bench.md) |
| NatureBench | 2026 | 匹配 Nature 系列论文发表的 SOTA | 90 个任务，六大领域，经评审把关的 NatureGym 流水线 | 在信息隔离墙下达到或超越已发表的 SOTA | [卡片](../works/naturebench.md) |
| PRBench | 2026 | 复现 physics 论文，从零实现算法 | 30 个专家精选任务，11 个子领域，sandbox | 与论文匹配的定量结果（最高 34%） | [卡片](../works/prbench.md) |

## Related Works

- [CORE-Bench](../works/core-bench.md)
- [SUPER](../works/super.md)
- [PaperBench](../works/paperbench.md)
- [ReplicationBench](../works/replicationbench.md)
- [AutoMat](../works/automat.md)
- [Collider-Bench](../works/collider-bench.md)
- [FIRE-Bench](../works/fire-bench.md)
- [NatureBench](../works/naturebench.md)
- [PRBench](../works/prbench.md)
