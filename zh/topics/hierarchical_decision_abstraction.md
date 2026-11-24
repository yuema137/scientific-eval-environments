# Hierarchical Decision Abstraction

> [English](../../topics/hierarchical_decision_abstraction.md) | **简体中文** · [← 全部 Topics](./README.md)

## 先看它解决什么问题

同一条 agent trajectory 可以按几种有用的尺度来描述。自动驾驶系统先选 route，再决定是否 change lane，最后才输出 steering、throttle 和 brake control。把这些全都只叫 action，就看不出究竟是哪一层错了。

科研 agent 也一样。`Diagnose the data pipeline` 可以是一条 high-level action，下面再展开成读 log、查 distribution、跑一个能区分假设的 test。如果 diagnosis 本身合理，只是 script 用错了 column，就修 executor；如果 command 都跑对了，diagnosis 却一开始就选错了，就修 planner。Hierarchy 只有在每层 interface 清楚、score 也站得住脚时，才能真的帮助 diagnosis。

## 定义

Agent 会在不同尺度上做决定：先选目标和策略，再选子目标、推理动作和工具，最后才落到 token 或底层控制。Hierarchical decision abstraction 要决定这些边界画在哪里，以及每一层怎样表示、打分和改进。它先问的不是「这个 decision 好不好」，而是「多大一段行为才算一个 decision」。

## 为什么重要

只给整条 trajectory 一个最终分数，会把策略和执行混在一起。自动驾驶中，选路线、决定变道、转方向盘是三个不同尺度的决定。科研 agent 也一样：先选诊断策略，再选实验，然后调工具并写代码。把这四层压成一条 trace，就看不出到底是哪一层坏了。

层级一旦可见，evaluation 就能分清「子目标选对了，但执行失败」和「子目标选错了，但执行得很漂亮」。Training 可以把 reward 给到真正负责的层级，开发者也可以单独修 planner、executor、skill 或 controller，不用把整个系统推倒重训。这套 hierarchy 把诊断直接连到了可模块化的改进。

它和 [Skill Hierarchy](./skill_hierarchy.md) 不同，后者问一项任务需要哪些能力。它和 [Planning & Decision-Making Evaluation](./planning_decision_evaluation.md) 也不同，后者问选出的 decision 好不好。这里问的是 decision 的粒度：路线、操作、控制信号，还是别的层级。

## 现有方法

- **Token macro-action。** [MA-RLHF](../works/ma-rlhf.md) 把一段 token 或更高层的语言结构合成 macro-action，缩短 action 与 reward 之间的有效距离。
- **Learned latent action。** [CoLA](../works/cola.md) 用面向未来 token 的 inverse dynamics 学出紧凑 action space，不要求人先写死 action vocabulary。
- **语义 reasoning action。** [MetaAct-RL](../works/metaact-rl.md) 把推理写成 meta-action 的选择与执行，例如 forward reasoning、critique 和 refinement。
- **由 policy 选择认知动作。** [PG-HAP](../works/pg-hap.md) 只训练一个选择具名 reasoning action 的轻量 planner，同时冻结 executor，因此可以单独检验 action selection 的价值。
- **从 subgoal 到执行的层级。** [HiPER](../works/hiper.md) 把提出 subgoal 的高层 planner 与执行多个环境 action 的低层 policy 分开，并在两层分别计算 advantage。
- **Plan 引导的 token reasoning。** [PTA-GRPO](../works/pta-grpo.md) 从 solution trace 中提炼短 plan，同时奖励 plan 质量和最终推理结果。
- **可复用 meta-ability。** [Beyond 'Aha!'](../works/beyond-aha.md) 先显式训练 deduction、induction 和 abduction，再做领域 RL，不再等这些能力偶然出现。

另一类工作不改模型权重，而是从存下来的 trajectory 里提炼出层级。这里的抽象是一份 memory 或 skill artifact，放进一个 frozen agent 的 context。比较不同层级时，让同一个 agent 在同一批任务上分别带着不同的 artifact 去跑。

- **单一层级和混合层级的 ablation。** [STAIR](../works/stair.md) 把过去修 issue 的 trajectory 抽象成 plan tree，节点分为低、中、高三个层级。在 125 个 SWE-bench Verified 实例上固定一个 backbone，直接用原始 trajectory 解决 72 个，只用单一层级解决 73 到 80 个，混合层级解决 100 个。[Trace2Tower](../works/trace2tower.md) 从一张按结果加权的 transition graph 中归纳出 action、procedure 和 strategy 三级 skill。在 ALFWorld 上，只保留 strategy 的版本达到 84.83%，完整三级 skill library 是 87.31%；两者占用的 skill context 分别是 1,966 和 3,623 个字符。
- **把粒度当成唯一的变量。** [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) 用同一个 induction prompt，只改变 skill 是按整个任务写还是按子任务写。在 11 个模型上取平均，任务级的文本 skill 低于不带 memory 的 baseline（20.9% 对 22.1%），子任务级的文本 skill 则高于它（26.7% 对 24.8%）。也就是说，抽象单位选在哪一层，决定了效果是正还是负。
- **子流程和 meta-procedure。** [Agent Workflow Memory](../works/agent-workflow-memory.md) 归纳出带占位值的子任务 workflow，后面的 workflow 可以把前面的当作 sub-goal 复用。它还比较了两种用法：把 workflow 放进 context，或者把 workflow 做成可调用的 action。[MACLA](../works/macla.md) 把反复出现的 procedure 组合成 meta-procedure，并配一个 continue/skip/repeat/abort 的控制 policy。去掉 meta-procedure 这一层后，ALFWorld unseen 的 success 从 90.3 降到 78.4。
- **复用时按单元决定用哪一层。** [SkillLens](../works/skilllens.md) 把 skill 存成 policy、strategy、procedure 和 primitive 四层，由一个 verifier 逐个单元决定是接受、往下拆、改写还是跳过。它和「全部改写」「只用父节点」两种适配方式做了对比，同时报告 accuracy 和适配成本。
- **用抽象来分析和指导。** [ATLAS](../works/atlas-agent-strategies.md) 把每个 action-observation 对映射成一个抽象符号，再在多次运行的符号 trace 上学出一条 Markov chain。分析者从这条链里读出策略和失败循环；同一条链也拿来指导更小的 executor 模型。在 penetration-testing 机器上，这些模型没有指导时的 success 是 5.0% 和 1.7%，在 dynamic 模式下升到 28.3% 和 38.3%。

这些工作衡量的是：某个层级能不能在推理时帮到一个固定的 agent。它们都没有在新层级上训练 agent，所以说明不了同样的层级能不能帮到一个专门在上面优化过的 policy。

## 对比

| Work | Decision unit | 抽象从哪里来 | 低层 executor | 怎样评价这个抽象 |
|---|---|---|---|---|
| MA-RLHF | Token macro-action | 固定长度或 learned grouping | 同一个 LLM policy | Reward、任务质量、收敛速度 |
| CoLA | 紧凑 latent action | Learned inverse dynamics | Language world model | 数学、preference 与 agent task；seen/unseen split |
| MetaAct-RL | Forward reasoning、critique、refinement | 人工定义的语义 action set | 同一模型输出 action 与内容 | 六个 reasoning benchmark、action diversity、sampling efficiency |
| PG-HAP | Analysis、decomposition、reasoning、coding、verification、knowledge、final answer | 人工 action set 与 transition graph | Frozen LLM | Accuracy、重复程度、action-sequence diversity |
| HiPER | Subgoal | Planner 生成 | 低层 agent policy 执行环境 action | Success，以及 planner/executor 两层的 advantage 分析 |
| PTA-GRPO | 简短 high-level guidance | 从 solution trace 提炼 | 同一 LLM 生成细粒度 reasoning | 十个 reasoning benchmark 与 plan-quality reward |
| Beyond 'Aha!' | Deduction、induction、abduction | 人工 meta-ability taxonomy 与 synthetic task | 领域 reasoning model | Held-out 数学、coding 和 science transfer |
| [STAIR](../works/stair.md) | Plan-tree 节点：针对具体 artifact 的 sub-goal、与项目无关的 strategy，或跨项目的原则 | 由 LLM 对过去的修复 trajectory 分组和抽象，按修复阶段切分 | Frozen coding agent（Lingxi；迁移实验用 mini-SWE-agent v2），每个阶段在 prompt 里收到对应 plan | SWE-bench Verified Pass@1；125 个实例上比较原始 trajectory、各单一层级和混合层级 |
| [Trace2Tower](../works/trace2tower.md) | Action、procedure 或 strategy skill | 对过去 trajectory 构建按结果对比的 transition graph，再做 spectral clustering | 固定的 Skill User 模型，在 token budget 内检索 skill | ALFWorld 和 WebShop 的 success、步数、无效 action 和 context 大小；strategy-only 版本与各组件 ablation |
| [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md) | 任务级或子任务级 skill，写成文本或代码 | 同一个 induction prompt，分别在每个任务或每个子任务之后调用 | 同一个 LLM agent，按 embedding 相似度检索 skill | 在 11 个模型和三个 benchmark 上，比较各层级与不带 memory 的 baseline 的 success；不需要运行任务的 utility score |
| [Agent Workflow Memory](../works/agent-workflow-memory.md) | 带占位值的子任务 workflow，可在后续 workflow 中复用 | 由 LM 从标注样例归纳（offline），或从 LM evaluator 判为成功的测试 trajectory 归纳（online） | 同一个 web agent，workflow 放在 memory 里或作为可调用 action | WebArena 和 Mind2Web 的 success 与步数；文本 vs. 代码、context vs. action space 的 ablation |
| [MACLA](../works/macla.md) | Procedure，以及带 continue/skip/repeat/abort 控制 policy 的 meta-procedure | Frozen LLM 切分 trajectory，再按 embedding 相似度合并 | Frozen Llama-2-7B | 四个 benchmark 上的分数；去掉 meta-procedure 层的 ablation |
| [SkillLens](../works/skilllens.md) | Policy、strategy、procedure 或 primitive skill 单元 | 四层 skill graph | 主 agent，接收经 verifier 接受、拆分或局部改写后的单元 | MuLocbench 和 ALFWorld 上的 accuracy，以及与「全部改写」「只用父节点」相比的时间和 token 成本 |
| [ATLAS](../works/atlas-agent-strategies.md) | （action 类别, observation 类别）符号；学到的 Markov-chain 状态 | LLM 对 trace 分类和归一化，再用 Alergia 做 automata learning | 阅读模型的分析者；由提取出的策略指导的小 executor 模型 | 定性检查学到的模型；五种指导模式下 executor 在 60 次运行中的成功次数 |

## 开放问题

- **Transfer 还是重新打包。** 更高层的 action space 能否带来 compositional OOD transfer，还是只把熟悉的 trajectory 压缩成一套新模板？
- **怎样选择层级。** 一个环境适合什么粒度？怎样避免 agent 把重要 decision 藏进过大的 macro-action？
- **Action discovery。** 人工 action 可解释，但会带入设计者的 ontology；learned latent action 可能发现新结构，也可能重新造出一个黑箱。
- **分层 ground truth。** 多种策略都可能有效，而且往往只能看到下游结果。这时怎样判定一个高层 decision 错了？
- **跨层 credit。** 子目标正确、执行失败时，怎样分开 reward 与责任，又不武断地假设 planner 和 executor 相互独立？
- **接口错误。** 两个模块可能各自有能力，却在层级转换时失败。Evaluation 需要区分 planner error、executor error 与 grounding/interface error。
- **严格对照实验。** 目前还缺少这样的实验：固定 model、data、reward、compute 和 environment，只改变 action representation，再同时测 IID success、OOD transfer、composition、sample efficiency、strategy diversity 和 decision cost。STAIR 和 Break It Down, Pass It On 固定了 agent 和任务，只改变存储 artifact 的层级，但它们不涉及训练，报告的也只是任务 success，不是上面整套指标。

## 相关工作

- [Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents](../works/trace2tower.md)
- [Break It Down, Pass It On](../works/break-it-down-pass-it-on.md)
- [ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning](../works/atlas-agent-strategies.md)
- [STAIR: Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](../works/stair.md)
- [SkillLens](../works/skilllens.md)
- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [MACLA: Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](../works/macla.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
- [CoLA](../works/cola.md)
- [MA-RLHF](../works/ma-rlhf.md)
- [Agent Workflow Memory](../works/agent-workflow-memory.md)
