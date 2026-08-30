# Explanation Style Guide

> **English** | [简体中文](./zh/EXPLANATION_STYLE.md)

This repository is a reference for readers, not a storage format for paper abstracts. A page is successful only when a technically curious reader can explain what changes, why it matters, and where the claim stops.

The style is adapted from the explanation workflow developed in [`dongbei-explainer`](https://github.com/yuema137/dongbei-explainer). We adopt its causal structure, concrete traces, terminology discipline, and preservation of boundaries. English pages do not imitate Chinese wording or regional voice.

## The explanation contract

For synthesis and explanatory prose, establish these points in a natural order:

1. **The job.** What question does this concept or work help answer?
2. **The old path.** What did an evaluator or agent do before this idea was introduced?
3. **The failure.** What information was lost, conflated, or made unreliable?
4. **The changed step.** Who now observes, scores, selects, stores, or executes something differently?
5. **One concrete trace.** Move one task, decision, score, or resource through the mechanism.
6. **The boundary.** State what the method does not establish or solve.
7. **The cost.** Name added annotation, compute, judge dependence, latency, or design assumptions when relevant.

This is a reasoning order, not a mandatory seven-heading template. A short card may cover it in one paragraph and two bullets. A topic synthesis may use several sections.

## Use actors and changed steps

Avoid sentences in which abstract nouns do all the work:

> Hierarchical evaluation enables modular diagnosis through multi-level decomposition.

Prefer the actual change:

> The evaluator scores the selected subgoal separately from the tool actions used to carry it out. A failed run can therefore show whether the planner chose the wrong subgoal or the executor mishandled a good one.

Words such as *framework*, *paradigm*, *methodology*, *alignment*, *grounding*, and *robustness* are allowed, but they cannot replace the mechanism.

## Prefer a real trace to a decorative analogy

Use the domain's natural objects: a trajectory, score vector, commit graph, experiment budget, task state, or equation. For example:

```text
terminal score only:       task failed

hierarchical score:        subgoal choice      correct
                           tool selection      correct
                           parameter value     wrong
```

This trace shows why the developer should repair parameter selection rather than retrain the planner. It also shows the limit: the evaluator still needs a defensible label at each level.

Use an analogy only when it is shorter than the mechanism, map every part back immediately, and stop before the mapping breaks.

## Terminology

- Preserve established technical terms, code, equations, work names, and benchmark names.
- Explain a term at its first meaningful use only when the target reader may not know the part of its mechanism needed here.
- Do not repeatedly write `term (definition)`.
- A project-local label is not shared vocabulary merely because it is English. First state its concrete responsibility.
- Do not replace precise verbs with generic claims such as *supports*, *enables*, *facilitates*, or *improves* unless the next clause says how.

The default reader has general STEM literacy but may not know computer science or this repository.

## English prose

- Start from the reader's question, not a taxonomy label.
- Prefer short causal chains and explicit before/after comparisons.
- Keep one main claim per sentence when a paragraph is introducing a concept.
- Do not stack three or more abstract nouns where actors and verbs are available.
- Preserve formal detail at expert depth. Conversational structure is an entrance, not a substitute for equations, metrics, or assumptions.
- End important explanations with the easiest misconception, unresolved question, or trade-off.

## Chinese prose

- Write the Chinese page from the meaning, not from English word order.
- Put necessary English jargon inside Chinese that a technically competent person would naturally say aloud.
- Prefer actors and actions: say who reads a trace, which score changes, or what the agent selects next.
- Do not invent compressed Chinese technical slang merely to make a sentence shorter.
- Do not use the Chinese em dash `——` to wedge a definition or long aside into a sentence. Split the thought.
- A light conversational rhythm is welcome; dialect performance, catchphrases, phonetic spellings, and comedy are not.
- A reader outside Northeast China must be able to understand the page immediately.

## Genre-specific expectations

### Topic pages

Open with `Start Here` / `先看它解决什么问题`. In a few short paragraphs, show the problem, the changed evaluation step, one concrete example, and the nearest-topic boundary. The later definition, literature map, tables, and open questions can remain formal and dense.

### Work cards

The Overview and Summary must say what the work changes and how its evaluation tests that change. Do not paste or lightly paraphrase an abstract. Tasks and Evaluation should let one representative item be traced from input to score. Strengths and Limitations must name evidence and boundaries rather than praise or dismiss the work.

### Domain and activity pages

These are factual reference pages. Keep tables compact, but introduce specialized columns or scoring rules by saying what decision a reader can make from them. Do not force a worked example into every row.

## Review checklist

Reject or revise a page when any of these are true:

- the definition restates its own label;
- the prose says a method “enables” an outcome without identifying the changed step;
- a reader cannot trace one representative item from input to score;
- a metaphor is doing work that a small real example would do better;
- simplification removed a condition, cost, equation, or limitation;
- the Chinese is grammatical but would not be spoken naturally by a technical peer;
- the English reads like a chain of abstract-paper phrases rather than an explanation;
- the page assumes that asking for clarity means the reader lacks technical ability.

Technical correctness always outranks tone. Clarity must expose the mechanism, not invent a plausible story.
