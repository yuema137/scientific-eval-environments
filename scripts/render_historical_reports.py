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
        en.append(f"### [{title}](../topics/{slug}.md)" if slug else f"### {title}")
        zh.append(f"### [{title}](../../topics/{slug}.md)" if slug else f"### {title}")
        en.append(""); zh.append("")
        en.append("This cluster changes what evaluators can see and act on:")
        zh.append("把这组工作放一块看，变化不只是多了几个分数，而是 evaluator 能看见、能诊断的东西变多了：")
        en.append(""); zh.append("")
        for w in subset:
            en.append(f"- [{w['title']}](../works/{w['slug']}.md): {w['overview']}")
            zt=(ROOT/"zh"/"works"/(w["slug"]+".md")).read_text(); zo=m._section(zt,"Overview").replace("——", "：")
            zh.append(f"- [{w['title']}](../../works/{w['slug']}.md)：{zo}")
        en += ["", "Together, these works move the discussion from a single headline result toward a more explicit account of the behavior, evidence, or development step being evaluated.", ""]
        zh += ["", "说白了，这批工作共同往前推了一步：不能只看最后成没成，还得把行为、证据或改进环节摊开，才能知道下一步该改哪儿。", ""]
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
        if not (en.exists() and zh.exists()): render(month)
m._update_indexes()
