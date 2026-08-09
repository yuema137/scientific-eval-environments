# 科学问题求解与推理

> [English](../../activities/scientific_problem_solving_reasoning.md) | **简体中文** · [← 全部 activities](./README.md)

## Definition

评估 agent 对科学、数学或理论问题给出答案、推导、证明或求解的能力，其核心交付物是解答本身，而非软件产物、实验或研究工作流。

## Scope

涵盖科学问答、定量与理论推理、符号运算、形式化与数学证明、研究级计算、多模态问题求解，以及以诊断为交付物的诊断推理。与以下情形相区分：核心是构建软件（→ 科学软件与工作流工程）、运行模拟（→ 模拟与科学计算），或核验其他 agent 的推理步骤（属评估方法学，而非活动）。

## Task Patterns

最大的一类是**领域知识问答**，其交付成果是对精心整理的考试或教科书题目给出正确答案。心理学在其中自成一支——[ConceptPsy](../works/conceptpsy.md) 将概念标注到章节，[CPsyExam](../works/cpsyexam.md) 把知识题与案例分析题分开，[PsychCounsel-Bench](../works/psychcounsel-bench.md) 则对标真实的执业认证及格线。工程知识问答见于 [MaScQA](../works/mascqa.md)（材料）、[TeleQnA](../works/teleqna.md)（电信）和 [ElecBench](../works/elecbench.md)（电力调度），而 [HLE](../works/hle.md) 则刻意设定了一个宽泛的、触及知识前沿的高标准。化学知识问答从 [ChemBench](../works/chembench.md) 和 [ChemEval](../works/chemeval.md)，一直延伸到侧重定量计算的 [QCBench](../works/qcbench.md) 和 [ChemIQ](../works/chemiq.md)。

第二类是**竞赛、考试及研究级别的定量物理推理**，其交付成果是符号推导，连续评分或部分给分的指标在此至关重要。[PHYBench](../works/phybench.md) 和 [HiPhO](../works/hipho.md) 评判奥赛风格的题目；[UGPhysics](../works/ugphysics.md) 和 [PHYSICS](../works/physics-benchmark.md) 覆盖本科阶段的广度；难度则经由 [CMPhysBench](../works/cmphysbench.md)、[CMT-Benchmark](../works/cmt-benchmark.md)、[TPBench](../works/tpbench.md)、[CritPt](../works/critpt.md) 和 [PRL-Bench](../works/prl-bench.md) 逐级攀升，进入真正研究级、且经过防数据污染处理的挑战。应用数学方面的对应工作包括 [HARDMath](../works/hardmath.md)（渐近分析）和 [PDE-Controller](../works/pde-controller.md)。

第三类是**多模态、以视觉为核心的问题求解**，答案的得出依赖于对示意图、光谱或显微图像的解读。物理示意图驱动了 [SeePhys](../works/seephys.md)；电路与电子工程图像驱动了 [EEE-Bench](../works/eee-bench.md) 和 [MMCircuitEval](../works/mmcircuiteval.md)；材料表征图像则支撑了 [MatCha](../works/matcha.md)、[MatVQA](../works/matvqa.md)、[MatQnA](../works/matqna.md)、[MatSciBench](../works/matscibench.md) 和 [MaCBench](../works/macbench.md)。化学结构解析是一个反复出现的多模态子主题，从 [MolPuzzle](../works/molpuzzle.md) 中分阶段的谱图判读，到 [MolQuest](../works/molquest.md) 中具备实验规划能力的智能体式解析。

第四类是**化学中的结构、图与反应推理**，其正确性可针对分子本身进行符号化验证：[MolLangBench](../works/mollangbench.md)、[MolecularIQ](../works/moleculariq.md)、[FGBench](../works/fgbench.md)、[AtomWorld](../works/atomworld.md)（晶体几何），以及面向反应与合成的 [ChemCoTBench](../works/chemcotbench.md)、[FukuyamaBench](../works/fukuyamabench.md)、[ChemCensor](../works/chemcensor.md) 和 [ChemCost](../works/chemcost.md)。与之相关的**形式化证明与验证**一支，让推理过程可被内核逐步核验：[Lean4Physics](../works/lean4physics.md)、[FVEval](../works/fveval.md) 和 [VCoT-Bench](../works/vcot-bench.md)。

最后，还有一类**临床诊断与交互式生物学研究**，它把交付成果视为在信息不完整条件下得出的诊断或发现：[AgentClinic](../works/agentclinic.md) 和 [SDBench](../works/sdbench.md) 中的序贯诊断，以及 [LAB-Bench](../works/lab-bench.md)、[BAISBench](../works/baisbench.md)、[BioProBench](../works/bioprobench.md)、[BioKGBench](../works/biokgbench.md) 和 [Aviary](../works/aviary.md) 中的生物学研究能力。诸如 [SciCode](../works/scicode.md)、[CFDLLMBench](../works/cfdllmbench.md)、[PhySciBench](../works/physcibench.md)、[SciConvBench](../works/sciconvbench.md)、[BrainBench](../works/brainbench.md)、[OpenXRD](../works/openxrd.md) 和 [onePot-Bench](../works/onepot-bench.md) 等跨领域基准，则让这一活动更加完整。

## Comparison

| Work | Year | Activity instantiation | Task form / environment | Deliverable or success target | Card |
|---|---|---|---|---|---|
| ConceptPsy | 2023 | 回答按概念/章节标注的心理学题目 | 静态问答，12 个科目，1,383 个概念 | 按概念统计的准确率 | [卡片](../works/conceptpsy.md) |
| MaScQA | 2023 | 求解材料科学/冶金学考试题目 | 静态问答，650 道 GATE 题目，4 种题型，14 个主题 | 答案准确率（GPT-4 约 62%） | [卡片](../works/mascqa.md) |
| TeleQnA | 2023 | 回答电信领域知识题目 | 静态选择题，10,000 道题，5 个类别 | 与电信从业者相比的准确率 | [卡片](../works/teleqna.md) |
| AgentClinic | 2024 | 通过与患者的序贯交互得出诊断 | 模拟诊所，9 个专科，7 种语言，多模态 | 诊断准确率 | [卡片](../works/agentclinic.md) |
| Aviary | 2024 | 求解多步骤的分子生物学/文献研究任务 | 语言智能体环境（SeqQA、LitQA2、蛋白质稳定性） | 相较于专家的任务完成度 | [卡片](../works/aviary.md) |
| BioKGBench | 2024 | 核验生物医学知识图谱中的论断并发现错误 | SCV+KGQA（2,000+）外加智能体式 KGCheck（225） | 错误检测准确率 | [卡片](../works/biokgbench.md) |
| BrainBench | 2024 | 判断哪篇神经科学摘要报告的是真实结果 | 二选一强制选择，200 个测试案例 | 相较于专家的预测准确率 | [卡片](../works/brainbench.md) |
| ChemBench | 2024 | 回答化学知识/推理题目 | 静态问答，2,700+ 组，无需工具 | 相较于人类化学家的准确率 | [卡片](../works/chembench.md) |
| ChemEval | 2024 | 求解跨能力维度的化学任务 | 42 项任务，4 个层级，12 个维度，静态 | 任务准确率 | [卡片](../works/chemeval.md) |
| CPsyExam | 2024 | 回答心理学知识题与案例分析题 | 静态问答，4,000 道考试题 | 答案准确率 | [卡片](../works/cpsyexam.md) |
| EEE-Bench | 2024 | 依据电路图求解多模态电子工程题目 | 2,860 道题，10 个子领域，图文结合 | 求解准确率（19-47%） | [卡片](../works/eee-bench.md) |
| ElecBench | 2024 | 对电网调度场景进行推理 | 自然语言推理/决策，通用+业务场景 | 六项指标/24 项子指标评分 | [卡片](../works/elecbench.md) |
| FVEval | 2024 | 生成 SystemVerilog 断言/测试平台 | 三个子任务，工具验证 | 通过 Jasper 形式化工具验证 | [卡片](../works/fveval.md) |
| HARDMath | 2024 | 求解应用数学的渐近逼近题目 | 自动生成，HARDMath-mini 366 道 + 40 道应用题 | 与数值标准答案的匹配度 | [卡片](../works/hardmath.md) |
| LAB-Bench | 2024 | 求解生物学研究实践任务 | 2,400+ 道选择题，8 个类别，可选用工具 | 相较于专家生物学家的准确率 | [卡片](../works/lab-bench.md) |
| MaCBench | 2024 | 解读化学/材料实验室图像 | 多模态 VLM，3 个方面，静态 | 各方面的任务准确率 | [卡片](../works/macbench.md) |
| MolPuzzle | 2024 | 从谱图解析分子结构 | 200 个实例，3 个阶段，多模态 | 结构精确匹配（GPT-4o 1.4%） | [卡片](../works/molpuzzle.md) |
| SciCode | 2024 | 求解科研级编程科学问题 | 80 个主问题 / 338 个子问题，16 个子领域 | 通过参考测试用例（Claude 4.6%） | [卡片](../works/scicode.md) |
| AtomWorld | 2025 | 操作晶态原子结构 | 10 种操作，4 类建模，可验证 | 经验证的结构正确性 | [卡片](../works/atomworld.md) |
| BAISBench | 2025 | 标注细胞类型并回答发现类问题 | 15 个单细胞数据集 + 193 道选择题 | 相较于人类的标注+发现准确率 | [卡片](../works/baisbench.md) |
| BioProBench | 2025 | 对生物湿实验方案进行推理 | 523,784 个实例，5 种任务类型，静态 | Accuracy/F1/tau/BLEU 指标 | [卡片](../works/bioprobench.md) |
| CFDLLMBench | 2025 | 回答 CFD 知识、编写求解器、运行 OpenFOAM | 三个层级，240 项任务 | 可执行性、数值误差、收敛性 | [卡片](../works/cfdllmbench.md) |
| ChemCoTBench | 2025 | 以模块化操作链形式求解分子任务 | 1,495 个样本，22 项任务，静态 | 分步推理正确性 | [卡片](../works/chemcotbench.md) |
| ChemIQ | 2025 | 回答有机化学构造类题目 | 816 道简答题，8 个类别，无需工具 | 程序化验证的准确率 | [卡片](../works/chemiq.md) |
| CMPhysBench | 2025 | 求解研究生级凝聚态计算题目 | 520+ 道题，生成完整解答 | SEED 部分给分评分 | [卡片](../works/cmphysbench.md) |
| CMT-Benchmark | 2025 | 求解专家级凝聚态理论问题 | 50 道题，涉及符号算符处理 | 相较于标准答案的程序化评分 | [卡片](../works/cmt-benchmark.md) |
| CritPt | 2025 | 求解研究级物理挑战 | 71 项挑战 / 190 个检查点，11+ 个子领域 | 机器验证的准确率（约 6%） | [卡片](../works/critpt.md) |
| FGBench | 2025 | 对官能团的性质效应进行推理 | 625K 个问题（7K 基准），245 种官能团 | 回归/分类准确率 | [卡片](../works/fgbench.md) |
| HiPhO | 2025 | 求解物理奥赛考试题目 | 13 场近期奥赛考试，文字+示意图 | 官方评分标准评分，奖牌门槛 | [卡片](../works/hipho.md) |
| Humanity's Last Exam | 2025 | 回答学术前沿题目 | 2,500 道专家级选择题/简答题，涵盖众多学科 | 答案准确率 + 校准度 | [卡片](../works/hle.md) |
| Lean4Physics / LeanPhysBench | 2025 | 产出形式化的 Lean4 物理证明 | 200 条手工构造的命题，配套 PhysLib | 内核核验的证明（最佳 35%） | [卡片](../works/lean4physics.md) |
| MatCha | 2025 | 回答材料表征图像类问题 | 1,500 道题，4 个阶段，21 项任务 | 相较于人类专家的准确率 | [卡片](../works/matcha.md) |
| MatQnA | 2025 | 解读十种材料表征方法 | 选择题+主观题，多模态 | 准确率（前沿约 90%） | [卡片](../works/matqna.md) |
| MatSciBench | 2025 | 求解大学水平的材料科学题目 | 1,340 道题（315 道含图），文字+多模态 | 推理准确率 | [卡片](../works/matscibench.md) |
| MatVQA | 2025 | 对显微/衍射图像进行推理 | 1,325 道题，4 项结构-性质任务 | 抗捷径的准确率 | [卡片](../works/matvqa.md) |
| MMCircuitEval | 2025 | 回答贯穿设计流程的电路/EDA 问题 | 3,614 组多模态问答，数字+模拟 | 按设计阶段统计的准确率 | [卡片](../works/mmcircuiteval.md) |
| MolLangBench | 2025 | 识别、编辑、生成分子结构 | 3 个族系，涵盖字符串/图像/图 | 自动/专家核验的准确率 | [卡片](../works/mollangbench.md) |
| OpenXRD | 2025 | 回答 XRD/晶体学问题 | 217 道题，闭卷/开卷，74 个模型 | 问答准确率 | [卡片](../works/openxrd.md) |
| PDE-Controller | 2025 | 为 PDE 控制进行自动形式化与推理 | 人工案例 + 200 万条合成数据，热/波系统 | 相较于基线的效用提升 | [卡片](../works/pde-controller.md) |
| PHYBench | 2025 | 求解原创物理题目 | 500 道题，从高中到奥赛，符号化 | EED 评分 / 准确率 | [卡片](../works/phybench.md) |
| PHYSICS | 2025 | 求解大学水平的物理题目 | 1,297 道题，六大核心领域 | 自动化答案验证 | [卡片](../works/physics-benchmark.md) |
| PsychCounsel-Bench | 2025 | 回答心理咨询执业认证题目 | 2,252 道 NCE 单选题，静态 | 相较于约 70% 及格线的准确率 | [卡片](../works/psychcounsel-bench.md) |
| QCBench | 2025 | 求解定量化学计算 | 350 道题，7 个子领域，3 个层级，无需工具 | 分步数值准确率 | [卡片](../works/qcbench.md) |
| SDBench | 2025 | 通过有预算约束的序贯信息采集进行诊断 | 304 例 NEJM-CPC 病例，守门式查询 | 准确率-成本前沿 | [卡片](../works/sdbench.md) |
| SeePhys | 2025 | 求解以视觉为核心的物理题目 | 2,000 道题，7 个领域，21 种示意图类型 | 准确率（最佳不足 60%） | [卡片](../works/seephys.md) |
| TPBench | 2025 | 求解新颖的理论物理题目 | 57 道题，高能物理/宇宙学，可自动验证 | 经验证的答案准确率 | [卡片](../works/tpbench.md) |
| UGPhysics | 2025 | 求解本科物理题目 | 5,520 道双语题，13 个科目，7 种答案类型 | MARJ 评判的准确率（最佳 49.8%） | [卡片](../works/ugphysics.md) |
| ChemCensor / CREED | 2026 | 提出合理的逆合成前体 | 单步逆合成，合理性评分 | 化学合理性指标 | [卡片](../works/chemcensor.md) |
| ChemCost | 2026 | 通过检索基准信息与报价为反应定价 | 1,427 项任务，冻结快照，使用工具 | 误差 25% 以内的准确率（50.6%） | [卡片](../works/chemcost.md) |
| FukuyamaBench | 2026 | 推演基元反应机理路径 | 源自教科书的分步机理任务 | 路径精确匹配（8.3%） | [卡片](../works/fukuyamabench.md) |
| LABBench2 | 2026 | 求解贴近实际的生物学研究任务 | 1,900 项任务，含 PDF/图像/生物信息学文件 | 准确率（较 LAB-Bench 下降 26-46%） | [卡片](../works/labbench2.md) |
| MolecularIQ | 2026 | 对分子图进行符号化推理 | 可符号验证的任务，静态 | 经验证的正确性 / 指纹 | [卡片](../works/moleculariq.md) |
| MolQuest | 2026 | 通过多轮实验规划解析结构 | 交互式谱图采集回合 | 结构准确率（约 50%） | [卡片](../works/molquest.md) |
| onepot-Bench 0 | 2026 | 化学信息学、拒答、反应结果预测 | 三个部分，含私有实验室数据，静态 | 准确率 / 拒答行为 | [卡片](../works/onepot-bench.md) |
| PhySciBench | 2026 | 回答物理科学深度研究问题 | 200 道精选题，物理+化学，6 个类别 | 答案正确性 | [卡片](../works/physcibench.md) |
| PRL-Bench | 2026 | 求解前沿物理研究任务 | 100 项任务，取自近期 PRL 论文，5 个子领域 | 可验证评分（最佳 <50/100） | [卡片](../works/prl-bench.md) |
| SciConvBench | 2026 | 澄清表述不清的计算科学请求 | 多轮对话，4 个领域 | 消歧/一致性求解（52.7%） | [卡片](../works/sciconvbench.md) |
| VCoT-Bench | 2026 | 完成 Verus 验证的思维链 | 1,988 项任务，源自 150 个 Verus 程序 | 证明块补全准确率 | [卡片](../works/vcot-bench.md) |

## Related Works

- [ConceptPsy](../works/conceptpsy.md)
- [MaScQA](../works/mascqa.md)
- [TeleQnA](../works/teleqna.md)
- [AgentClinic](../works/agentclinic.md)
- [Aviary](../works/aviary.md)
- [BioKGBench](../works/biokgbench.md)
- [BrainBench](../works/brainbench.md)
- [ChemBench](../works/chembench.md)
- [ChemEval](../works/chemeval.md)
- [CPsyExam](../works/cpsyexam.md)
- [EEE-Bench](../works/eee-bench.md)
- [ElecBench](../works/elecbench.md)
- [FVEval](../works/fveval.md)
- [HARDMath](../works/hardmath.md)
- [LAB-Bench](../works/lab-bench.md)
- [MaCBench](../works/macbench.md)
- [MolPuzzle](../works/molpuzzle.md)
- [SciCode](../works/scicode.md)
- [AtomWorld](../works/atomworld.md)
- [BAISBench](../works/baisbench.md)
- [BioProBench](../works/bioprobench.md)
- [CFDLLMBench](../works/cfdllmbench.md)
- [ChemCoTBench](../works/chemcotbench.md)
- [ChemIQ](../works/chemiq.md)
- [CMPhysBench](../works/cmphysbench.md)
- [CMT-Benchmark](../works/cmt-benchmark.md)
- [CritPt](../works/critpt.md)
- [FGBench](../works/fgbench.md)
- [HiPhO](../works/hipho.md)
- [Humanity's Last Exam](../works/hle.md)
- [Lean4Physics / LeanPhysBench](../works/lean4physics.md)
- [MatCha](../works/matcha.md)
- [MatQnA](../works/matqna.md)
- [MatSciBench](../works/matscibench.md)
- [MatVQA](../works/matvqa.md)
- [MMCircuitEval](../works/mmcircuiteval.md)
- [MolLangBench](../works/mollangbench.md)
- [OpenXRD](../works/openxrd.md)
- [PDE-Controller](../works/pde-controller.md)
- [PHYBench](../works/phybench.md)
- [PHYSICS](../works/physics-benchmark.md)
- [PsychCounsel-Bench](../works/psychcounsel-bench.md)
- [QCBench](../works/qcbench.md)
- [SDBench](../works/sdbench.md)
- [SeePhys](../works/seephys.md)
- [TPBench](../works/tpbench.md)
- [UGPhysics](../works/ugphysics.md)
- [ChemCensor / CREED](../works/chemcensor.md)
- [ChemCost](../works/chemcost.md)
- [FukuyamaBench](../works/fukuyamabench.md)
- [LABBench2](../works/labbench2.md)
- [MolecularIQ](../works/moleculariq.md)
- [MolQuest](../works/molquest.md)
- [onepot-Bench 0](../works/onepot-bench.md)
- [PhySciBench](../works/physcibench.md)
- [PRL-Bench](../works/prl-bench.md)
- [SciConvBench](../works/sciconvbench.md)
- [VCoT-Bench](../works/vcot-bench.md)
