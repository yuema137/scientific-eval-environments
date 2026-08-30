# 解释写作规范

> [English](../EXPLANATION_STYLE.md) | **简体中文**

这个仓库是给人查和读的，不是用来堆论文摘要的。读完一页以后，读者至少应该能说清三件事：这里改了哪一步、为什么要改，以及结论到哪里为止。

这套写法参考 [`dongbei-explainer`](https://github.com/yuema137/dongbei-explainer) 的 explanation workflow。我们采用的是因果结构、具体 trace、术语处理和边界检查，不是往文档里塞东北话。中文可以有一点自然对话的节奏，但文档仍然要专业，也必须让东北以外的普通话读者一眼看懂。

## 一段解释得交代什么

写 synthesis 或解释性文字时，按读者真正需要的顺序把下面几件事交代出来：

1. **它管什么事。** 这个概念或这项工作帮我们回答什么问题？
2. **原来怎么做。** 在它出现以前，evaluator 或 agent 走的是哪条路？
3. **原来的路哪里不够。** 哪些信息混在了一起、丢了，或者根本不可信？
4. **现在改了哪一步。** 谁多看了什么、单独给什么打分、改成选择什么，或者把什么存了下来？
5. **让一个具体对象走一遍。** 拿一条 task、decision、score 或 resource trace，把过程走完。
6. **它没解决什么。** 不要把「有帮助」写成「已经解决」。
7. **代价是什么。** 需要更多 annotation、compute、judge、latency 或设计假设时，要直接写出来。

这是一条思考顺序，不是要求每页打印七个标题。短 work card 可以用一段话和两个 bullet 讲完；topic synthesis 可以分成几节。

## 把参与者和动作说出来

下面这种话看着正式，其实没说清发生了什么：

> 分层评估通过多层分解实现模块化诊断。

改成具体动作以后，读者才能看懂：

> Evaluator 把「选了哪个 subgoal」和「怎样调用工具完成它」分开打分。任务失败时，我们就能看出是 planner 一开始选错了，还是 executor 把一个正确 subgoal 做坏了。

`framework`、`paradigm`、`methodology`、`alignment`、`grounding` 和 `robustness` 这些词可以用，但它们不能顶替 mechanism。

## 优先走真实 trace，别硬套比喻

尽量使用这个领域本来就有的对象，例如 trajectory、score vector、commit graph、experiment budget、task state 或 equation。

```text
只看最终分数：          task failed

分层以后：              subgoal choice      correct
                        tool selection      correct
                        parameter value     wrong
```

这条 trace 一眼就能看出：该修的是 parameter selection，不是重新训练 planner。它也顺手暴露了边界：evaluator 仍然需要在每个层级拿到站得住脚的 label。

只有在比 mechanism 更短、更容易进门时才用比喻。用了以后要立刻把每个部分对应回真实组件，映射开始不准时马上停。

## 术语怎么处理

- 标准技术术语、code、equation、work name 和 benchmark name 保留原样。
- 只在第一次真正需要时解释术语，而且只解释当前 mechanism 用得上的部分。
- 不要反复写 `term（定义）`。
- Repo 自己起的英文长标签不自动算公共术语。先说它具体负责什么，再保留名字方便查找。
- 能写精确动词时，不要只写「支持、赋能、促进、提升」。如果确实要用，下一句必须说清它怎样做到。

默认读者有一般 STEM 背景，但不一定学过计算机，也不了解这个 repo。

## 英文怎么写

- 从读者的问题开始，不要从 taxonomy label 开始。
- 多用短因果链和明确的 before/after。
- 介绍概念时，一句话尽量只承担一个主要 claim。
- 能写 actor 和 verb 时，不要让三个以上的 abstract noun 挤在一起扛整句话。
- 专家深度下必须保留 formal detail。自然的入口不能代替 equation、metric 和 assumption。
- 重要解释最后要交代最容易误解的地方、尚未解决的问题或 trade-off。

## 中文怎么写

- 根据意思重新写，不跟着英文 word order 走。
- 必要的 English jargon 可以保留，但外面的中文必须像技术同行真会说的话。
- 把 actor 和 action 写出来：谁读 trajectory、哪个 score 变了、agent 下一步选什么。
- 不要为了短而自造压缩黑话。
- 不用中文破折号 `——` 往一句话中间硬塞定义和长补充。把句子拆开。
- 可以有一点对话节奏，但不要表演方言、堆口头禅、写谐音或搞喜剧。
- 东北以外的普通话读者必须能直接看懂。

## 不同页面分别要做到什么

### Topic page

页面开头放 `先看它解决什么问题`。用几段短文依次讲清：原来的问题、evaluation 改了哪一步、一个具体例子，以及它和最近 topic 的边界。后面的 definition、literature map、table 与 open question 可以保持正式和高密度。

### Work card

Overview 和 Summary 要写清这项工作改了什么，以及 evaluation 怎样检验这个改动。不要粘贴或轻度改写 abstract。Tasks 与 Evaluation 应该让读者能把一个典型 item 从输入一直跟到 score。Strengths 与 Limitations 要写 evidence 和 boundary，不要只夸或只贬。

### Domain 与 activity page

这两类页面是 factual reference。Table 可以紧凑，但遇到特殊 column 或 scoring rule，要先说读者能拿它判断什么。不要求每一行都硬加 worked example。

## Review checklist

出现下面任意一种情况，就要退回重写：

- definition 只是换几个同义词重复标题；
- 只说方法「实现、支持、促进」了某种结果，却不说哪一步变了；
- 读者无法把一个典型 item 从 input 跟到 score；
- 明明一个小型真实例子更清楚，却硬上比喻；
- 为了显得简单，删掉了 condition、cost、equation 或 limitation；
- 中文语法没错，但技术同行平时根本不会这么说；
- 英文像 abstract phrase 一层套一层，不像在解释；
- 读者要求讲清楚，就被当成没有技术能力。

技术正确永远排在语气前面。讲清楚是把 mechanism 露出来，不是编一个听着顺的因果故事。
