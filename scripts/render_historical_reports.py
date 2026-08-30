#!/usr/bin/env python3
"""Deterministic fallback renderer for the one-time 2024+ archive bootstrap."""
import importlib.util
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("monthly_report", ROOT / "scripts/monthly_report.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def links(items, prefix="../"):
    return ", ".join("[%s](%s%s/%s.md)" % (x["name"], prefix, "topics" if "topic" in x["url"] else "domains", x["slug"]) for x in items) or "—"


def intro_lines(topic, count):
    if topic == "Scientific Agent Benchmarks":
        return (
            "This group asks what counts as a defensible scientific benchmark once a field's artifacts, tools, and verification constraints stop looking like generic QA.",
            "这组工作主要在回答一个更硬的问题：进到真实 scientific workflow 以后，benchmark 到底该怎么做，才不至于只是在测一层表面问答。")
    if topic == "General Long-Horizon Agent Benchmarks":
        return (
            "These papers push on the same bottleneck from different sides: once an agent must keep state across many steps, the benchmark has to expose where progress stalls.",
            "这组工作盯住的是同一个难点：一旦 agent 得跨很多步维持状态，benchmark 就得把卡住的位置露出来。")
    if topic == "Trajectory Evaluation":
        return (
            "Here the unit of judgment is no longer just the final answer. The trajectory itself becomes evidence about what the agent saw, decided, and missed.",
            "这一组不再只盯最后答案。整条 trajectory 本身就是证据，能看出 agent 当时看见了啥、怎么决定的、又漏掉了啥。")
    if topic == "Skill Hierarchy":
        return (
            "These works stop treating capability as a single score and instead separate the stack of subskills that a result depends on.",
            "这组工作不把能力压成一个总分，而是把结果背后的几层 subskill 拆开来看。")
    if topic == "Credit Assignment":
        return (
            "The common move here is to ask which interior step deserves blame or credit, instead of letting a final reward smear across the whole run.",
            "这一组关心的是，功劳和责任到底该落在哪一步，而不是让一个最终分数把整段过程全糊成一片。")
    if topic == "Resource-aware Evaluation":
        return (
            "These papers make efficiency part of the evaluation target, so success only counts when the agent reaches it without spending blindly.",
            "这组工作把资源也算进分里，所以不是成了就行，还得看 agent 是不是花得有章法。")
    if topic == "Benchmark Design, Validity & Contamination":
        return (
            "The key question in this cluster is whether the score can still be trusted once leakage, construction bias, and grader design are put under scrutiny.",
            "这组工作真正追问的是：一旦把泄漏、构造偏差和 grader 设计都摆上台面，这个分数还信不信得过。")
    if topic == "Planning & Decision-Making Evaluation":
        return (
            "These works look upstream of execution and ask whether the chosen next step was good at the moment of choice.",
            "这组工作往执行前面再退一步，看的是 agent 当时选的下一步到底对不对。")
    if topic == "Hierarchical Decision Abstraction":
        return (
            "The shared question here is not just whether the agent acts well, but at which level of abstraction those decisions should be represented and judged.",
            "这组工作问的不只是 agent 做得好不好，还在问这些决策到底该按哪个抽象层来表示和评。")
    if topic == "Evaluation-Driven Post-Training":
        return (
            "This cluster treats evaluation as a training control signal: the benchmark does not sit at the end of the loop, it helps decide the next update.",
            "这一组把 evaluation 当成训练环里的控制信号，不是最后给个成绩单就完事。")
    if topic == "Evaluation-Driven Data Curation":
        return (
            "These papers use downstream evaluation to decide what data should be kept, filtered, or generated next.",
            "这组工作拿下游 evaluation 反过来管数据：哪些该留，哪些该筛，下一批该补什么。")
    if topic == "Agent Harnesses & Scaffolding":
        return (
            "The shift here is from judging a base model in isolation to judging the surrounding harness that makes its behavior usable or brittle.",
            "这组工作的转向很明确：不再只看 base model 本身，而是连外面的 harness 一起评。")
    return (
        "A useful way to read this cluster is to ask which hidden part of evaluation it makes visible.",
        "把这组工作放一块看，关键是看它把 evaluation 里原来藏着的哪一层给掀出来了。")

def render(month):
    manifest, _ = m.build_manifest(month, "first-appearance")
    works = manifest["works"]
    if not works: return
    tc = Counter(x["name"] for w in works for x in w["topics"])
    dc = Counter(x["name"] for w in works for x in w["domains"])
    top_topics = [x for x,_ in tc.most_common(3)]
    top_domains = [x for x,_ in dc.most_common(3)]
    label = manifest["month_label"]
    en = [f"# {label} Monthly Report", "", f"> **English** | [简体中文](../zh/monthly/{month}.md)", "", f"> **Coverage:** First appearances during {month}", "", "## Month at a Glance", "", f"{len(works)} works first appeared this month. The strongest concentrations were " + (", ".join(top_topics) if top_topics else "cross-cutting benchmark work") + ".", "", "## What Changed This Month", ""]
    zh = [f"# {month} 月度报告", "", f"> [English](../../monthly/{month}.md) | **简体中文**", "", f"> **覆盖范围：** {month} 首次公开的工作", "", "## 本月概览", "", f"本月共有 {len(works)} 项工作首次公开。先看文献最集中的方向：" + ("、".join(top_topics) if top_topics else "跨领域 benchmark") + "。", "", "## 这个月到底变了什么", ""]
    groups = top_topics or [None]
    for topic in groups:
        subset = [w for w in works if topic is None or any(x["name"]==topic for x in w["topics"])][:5]
        if not subset: continue
        title = topic or "Cross-cutting evaluation"
        slug = next((x["slug"] for w in subset for x in w["topics"] if x["name"]==topic), None)
        intro_en, intro_zh = intro_lines(topic, len(subset))
        en.append(f"### [{title}](../topics/{slug}.md)" if slug else f"### {title}")
        zh.append(f"### [{title}](../../topics/{slug}.md)" if slug else f"### {title}")
        en.append(""); zh.append("")
        en.append(intro_en)
        zh.append(intro_zh)
        en.append(""); zh.append("")
        for w in subset:
            en.append(f"- [{w['title']}](../works/{w['slug']}.md): {w['overview']}")
            zt=(ROOT/"zh"/"works"/(w["slug"]+".md")).read_text(); zo=m._section(zt,"Overview").replace("——", "：")
            zh.append(f"- [{w['title']}](../../works/{w['slug']}.md)：{zo}")
        en.append("")
        zh.append("")
    if top_topics:
        en += ["## Selected Topic Developments", "", "Active topics this month: " + ", ".join(f"[{t}](../topics/{next(x['slug'] for w in works for x in w['topics'] if x['name']==t)}.md)" for t in top_topics) + ".", ""]
        zh += ["## 值得展开的 Topic", "", "本月最活跃的 Topic 包括：" + "、".join(f"[{t}](../../topics/{next(x['slug'] for w in works for x in w['topics'] if x['name']==t)}.md)" for t in top_topics) + "。", ""]
    if top_domains:
        en += ["## Selected Domain Developments", "", "The month's work was most concentrated in " + ", ".join(top_domains) + ". Domain pages provide the broader field context.", ""]
        zh += ["## 值得展开的 Domain", "", "本月工作主要集中在 " + "、".join(top_domains) + "。想看这些方法放进具体领域以后受什么约束，可以顺着 Domain 页面继续查。", ""]
    en += ["## Complete Monthly Index", "", "| Work | First appeared | Added as | Topics | Domains |", "|---|---|---|---|---|"]
    zh += ["## 本月完整索引", "", "| Work | 首次公开 | 加入状态 | Topics | Domains |", "|---|---|---|---|---|"]
    for w in works:
        en.append(f"| [{w['title']}](../works/{w['slug']}.md) | {w['first_appeared']} | New release | {links(w['topics'])} | {links(w['domains'])} |")
        zh.append(f"| [{w['title']}](../../works/{w['slug']}.md) | {w['first_appeared']} | 当月新发布 | {links(w['topics'],'../../')} | {links(w['domains'],'../../')} |")
    (ROOT/"monthly"/(month+".md")).write_text("\n".join(en)+"\n")
    (ROOT/"zh"/"monthly"/(month+".md")).write_text("\n".join(zh)+"\n")

for year in range(2024,2027):
    for number in range(1,13):
        month=f"{year:04d}-{number:02d}"
        if month>"2026-08": continue
        en=ROOT/"monthly"/(month+".md"); zh=ROOT/"zh"/"monthly"/(month+".md")
        if en.exists() and zh.exists():
            render(month)
            continue
        render(month)
m._update_indexes()
