# Hierarchical Decision Abstraction

> [English](../../topics/hierarchical_decision_abstraction.md) | **简体中文** · [← 全部 Topics](./README.md)

## 定义

Hierarchical decision abstraction 研究一个 agent 的行为应该怎样分层表示、评价和优化。层级可以包括目标、策略、子目标、推理动作、工具调用、token chunk、primitive action 和连续控制。它追问的不只是「这个 decision 好不好」，还包括「多大的一段行为应该算一个 decision」。

## 动机

如果只对 token、tool call 或 raw control 组成的整条 trajectory 给一个最终分数，策略选择和执行质量就混在了一起。自动驾驶中，选哪条路线、是否变道，以及具体怎样转方向盘或踩刹车，处在不同时间尺度上。科研 agent 也一样：选择诊断策略、决定做哪个实验、调用工具和生成代码，不应该被压成一个看不出内部结构的黑箱。

把这些层级显式写出来以后，evaluation 才能指出该改哪里。系统可以区分「子目标选对了，但执行失败」和「子目标选错了，但执行得很漂亮」；训练时也能把 reward 给到真正负责的层级。开发者因此可以单独修 planner、executor、skill 或 controller，而不必把整个系统推倒重训。这个 topic 连接了 measurement 与 evaluation-driven improvement。

它不同于 [Skill Hierarchy](./skill_hierarchy.md)。Skill Hierarchy 问的是一项任务需要哪些能力；它也不同于 [Planning & Decision-Making Evaluation](./planning_decision_evaluation.md)，后者问选出的 decision 是否合理。Hierarchical Decision Abstraction 问的是：应该在哪个粒度上定义和评分这个 decision。

## 现有方法

- **Token macro-action。** [MA-RLHF](../works/ma-rlhf.md) 把一段 token 或更高层的语言结构合成 macro-action，缩短 action 与 reward 之间的有效距离。
- **Learned latent action。** [CoLA](../works/cola.md) 用面向未来 token 的 inverse dynamics 学出紧凑 action space，不要求人先写死 action vocabulary。
- **语义 reasoning action。** [MetaAct-RL](../works/metaact-rl.md) 把推理写成 meta-action 的选择与执行，例如 forward reasoning、critique 和 refinement。
- **由 policy 选择认知动作。** [PG-HAP](../works/pg-hap.md) 只训练一个选择具名 reasoning action 的轻量 planner，同时冻结 executor，因此可以单独检验 action selection 的价值。
- **从 subgoal 到执行的层级。** [HiPER](../works/hiper.md) 把提出 subgoal 的高层 planner 与执行多个环境 action 的低层 policy 分开，并在两层分别计算 advantage。
- **Plan 引导的 token reasoning。** [PTA-GRPO](../works/pta-grpo.md) 从 solution trace 中提炼短 plan，同时奖励 plan 质量和最终推理结果。
- **可复用 meta-ability。** [Beyond 'Aha!'](../works/beyond-aha.md) 先显式训练 deduction、induction 和 abduction，再做领域 RL，不再等这些能力偶然出现。

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

## 开放问题

- **Transfer 还是重新打包。** 更高层的 action space 能否带来 compositional OOD transfer，还是只把熟悉的 trajectory 压缩成一套新模板？
- **怎样选择层级。** 一个环境适合什么粒度？怎样避免 agent 把重要 decision 藏进过大的 macro-action？
- **Action discovery。** 人工 action 可解释，但会带入设计者的 ontology；learned latent action 可能发现新结构，也可能重新造出一个黑箱。
- **分层 ground truth。** 多种策略都可能有效，而且往往只能看到下游结果。这时怎样判定一个高层 decision 错了？
- **跨层 credit。** 子目标正确、执行失败时，怎样分开 reward 与责任，又不武断地假设 planner 和 executor 相互独立？
- **接口错误。** 两个模块可能各自有能力，却在层级转换时失败。Evaluation 需要区分 planner error、executor error 与 grounding/interface error。
- **严格对照实验。** 目前还缺少这样的实验：固定 model、data、reward、compute 和 environment，只改变 action representation，再同时测 IID success、OOD transfer、composition、sample efficiency、strategy diversity 和 decision cost。

## Related Works

- [MA-RLHF](../works/ma-rlhf.md)
- [CoLA](../works/cola.md)
- [MetaAct-RL](../works/metaact-rl.md)
- [PG-HAP](../works/pg-hap.md)
- [HiPER](../works/hiper.md)
- [PTA-GRPO](../works/pta-grpo.md)
- [Beyond 'Aha!'](../works/beyond-aha.md)
