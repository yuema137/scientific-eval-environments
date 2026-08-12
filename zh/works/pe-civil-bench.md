# PE Civil Bench (2026)

> [English](../../works/pe-civil-bench.md) | **简体中文**

## Overview

PE Civil Bench 是一个开放 benchmark，收录 150 道执业资格考试风格的土木工程题目，题型仿照 NCEES 的 Fundamentals of Engineering 与 Professional Engineering Civil 两项考试。它在十三个前沿及开放权重 LLM 上横向对比三种做法——基础 prompt、向量检索增强生成（vector RAG）与 agentic RAG——并配套一条 agent 化的钢筋混凝土构件设计管线，其输出对照有限元分析验证。

## Topics

- [Scientific Agent Benchmarks](../topics/scientific_agents.md)

## Activities

- [科学问题求解与推理](../activities/scientific_problem_solving_reasoning.md)
- [优化与工程设计](../activities/optimization_engineering_design.md)

## Links

- **Paper:** https://doi.org/10.1016/j.cacaie.2026.100126
- **Code:** https://github.com/komal-blkmmb/Benchmarking_agentic-design_and_evaluation
- **Venue:** Computer-Aided Civil and Infrastructure Engineering, vol. 49, art. 100126 (2026)

## Summary

土木工程一直缺少一套标准化语料来评测 LLM 与各类增强策略，作者拿数学、医学领域已经成熟的数据集与之对照，凸显这块空白。PE Civil Bench 就用执业资格考试题目补上这份语料，每题按分支专业、难度、题型与推理需求作标注，并给出十三个模型在基础 prompt、向量 RAG 与 agentic RAG 三种条件下的基线成绩。第二项贡献是一套多 agent 框架，它以规范检索、计算、校验与迭代修正的流程自动完成钢筋混凝土构件设计，同时输出透明的推理轨迹。该框架在 33 组梁配置上运行，随后无需重新编程就扩展到柱设计；此外还有一个自主评估器，对照传统评估方法作了标定。

## Tasks

150 道 FE 与 PE 风格题目：110 道 FE 风格选择题，考察概念推理、计算与规范解读；40 道 PE 风格开放式数值题，要求多步建立求解式并作出工程判断。公开数据集覆盖八个分支专业——施工、工程伦理、岩土、数学、结构、测量、交通与水资源。题目由休斯顿大学 Structures and Artificial Intelligence Lab 的执业工程师精选，并逐题人工标注四个维度：分支专业、难度、题型与推理需求。构件设计赛道另配一份 PE Civil Design 数据集，内含参数化输入（跨度、梁宽与梁高、混凝土强度、钢筋屈服强度、恒载与活载、净保护层厚度），并以 ETABS 的有限元输出作为 ground truth；设计实验共报告 33 组梁配置。两份数据集均以 CC-BY-4.0 发布。

## Domains

土木与结构工程。受评对象是执业资格考试所考察的土木工程实务，考题分支涵盖结构分析与设计、岩土工程、交通、水资源、测量与施工——按本仓库的分类，这些都是土木工程的标准分支，一并归入本领域；其中水资源类题目考的是水利基础设施，而非环境过程科学，同样归入此处。设计赛道则明确属于结构：钢筋混凝土梁与柱的截面尺寸拟定与配筋构造，须通过设计规范符合性审查，并与有限元结果交叉验证。未指派共同领域。

## Evaluation

同一套题目在三种配置下评分——不作任何增强的基线 prompt、在检索语料上做的向量 RAG，以及把推理 agent 与迭代检索耦合起来的 agentic RAG——这样 benchmark 就不只是给模型排名，而能分离出每种增强策略各自的贡献。选择题按答案正确与否判分；开放式数值题必须给出多步推导出的数值。设计赛道方面，生成的钢筋混凝土设计先作规范符合性审查，再把算得的各项数值与有限元分析结果作相关分析，在 33 组梁配置上报告的一致性为 r ≥ 0.90。另有一个自主 LLM 评估器单独对照传统评估方法作标定，一致性达 r = 0.976。十三个系统在三种配置下的逐模型准确率：TODO(reference) — 出版方全文无法获取。

## Typical Duration

N/A — 可获取的文献记录未报告单任务的 wall-clock 时间、轨迹长度或 token 预算。

## Main Contribution

作者把 PE Civil Bench 定位为首个以 Fundamentals of Engineering 与 Professional Engineering Civil 考题构建的 benchmark，给出十三个前沿模型在基础、检索增强与多 agent 三类 prompt 策略下的基线成绩；同时展示了一套可扩展的 agent 框架，其产出的钢筋混凝土设计既符合规范，又与有限元分析吻合，并且无需重新编程即可从梁设计推广到柱设计。

## Key Design Ideas

- 以执业资格考试作为题目来源，题目本身已经过专业相关性与难度校准的把关，作者不必另行发明一套难度标尺。
- 刻意混用两种作答形式：选择题用来探查概念推理与规范解读，开放式数值题则迫使解题者一步步把求解式建立起来，答案无从蒙猜。
- 四维人工标注（分支专业、难度、题型、推理需求）使结果可以按题目的实际要求来切分。
- 增强策略与模型身份一样是一等实验因子：同一套 benchmark 在基础、向量 RAG 与 agentic RAG 三种条件下各跑一遍。
- 构件设计赛道用一次外部物理校核闭环，把 agent 产出的设计与 ETABS 有限元 ground truth 作相关分析，而不是对照一份评分细则。
- 设计管线在架构上就为扩展留了余地，从梁设计转到柱设计无需重新编程即是佐证。

## Strengths

- 覆盖八个土木分支专业，跨度之广在同时提供可执行设计赛道的领域 benchmark 中并不多见。
- 题目集与设计数据集都以宽松许可公开发布，并附有配套的 notebook 代码。
- 模型覆盖十三个前沿及开放权重系统，铺开了一条可用的谱系，而非两模型对比。
- 设计结果由独立的有限元工具验证，而不是靠 agent 自己的计算。
- 自主评估器在被采信之前先对照常规评估作了验证，而非默认可靠。

## Limitations

- 150 道题相对于所跨的八个分支专业偏少，分到每个专业的样本很稀薄。
- 设计赛道只在单一构件类别上验证——钢筋混凝土梁，外加柱的扩展——而非完整结构体系。
- Repository note: 该文属混合开放获取，但出版方全文对自动抓取返回 HTTP 403，因此逐模型分数、agentic RAG 相对向量 RAG 的增益，以及检索语料的构成，在此均记为未核实。
- Repository note: 考题在已知标准答案下考察知识回忆与闭式计算，衡量的是职业胜任层面的推理，而非长 horizon 的 agent 行为；只有设计赛道涉及多步、以工具为中介的工作。

## Related Works

- [StructureClaw](./structureclaw.md) — 结构工程 agent benchmark，用可执行求解器验证，与这里的考题形式互为补充。
- [MASSE](./masse.md) — 结构工程多 agent 系统，在真实咨询工作流上按评分细则打分，同样以规范符合性与承载力校核为目标。
- [ERI Benchmark](./eri-benchmark.md) — 跨工程领域的指令 benchmark，其分类体系含土木工程一门。
- [EEE-Bench](./eee-bench.md) — 电气与电子领域的专业考试型工程 benchmark，同一评测形式换了个学科。
- [ChemEBench](./chemebench.md) — 领域工程 benchmark，按专业工程技能层级组织，而非取材于考试。
