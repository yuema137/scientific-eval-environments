import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                                 "scripts", "update_agent")))

TEMPLATE = """# Works

```markdown
# <Work Name> (<Year>)

## Overview
## Topics
## Activities
## Links
## Summary
## Tasks
## Domains
## Evaluation
## Typical Duration
## Main Contribution
## Key Design Ideas
## Strengths
## Limitations
## Related Works
```
"""


def make_card(title, slug, topics=None, activities=None, links="- **Paper:** <https://arxiv.org/abs/2401.00001>"):
    tb = "\n".join("- [%s](../topics/%s.md)" % (t, t) for t in (topics or []))
    ab = "\n".join("- [%s](../activities/%s.md)" % (a, a) for a in (activities or [])) or \
        "N/A — evaluation methodology."
    return """# {title} (2025)

> **English** | [简体中文](../zh/works/{slug}.md)

## Overview
One line.

## Topics
{tb}

## Activities
{ab}

## Links
{links}

## Summary
Two lines.

## Tasks
Some tasks.

## Domains
Physics.

## Evaluation
Checks.

## Typical Duration
Short.

## Main Contribution
A thing.

## Key Design Ideas
- idea

## Strengths
- s

## Limitations
- l

## Related Works
- [Other](./other.md)
""".format(title=title, slug=slug, tb=tb, ab=ab, links=links)


def build_mini_repo(root, cards):
    """cards: list of dicts {slug,title,topics,activities,zh(bool),links}."""
    for sub in ("works", "topics", "activities", "domains", "zh/works"):
        os.makedirs(os.path.join(root, sub), exist_ok=True)
    with open(os.path.join(root, "works", "README.md"), "w") as f:
        f.write(TEMPLATE)
    topics, acts = set(), set()
    for c in cards:
        topics |= set(c.get("topics", []))
        acts |= set(c.get("activities", []))
    for t in topics:
        rel = "\n".join("- [%s](../works/%s.md)" % (c["title"], c["slug"])
                        for c in cards if t in c.get("topics", []))
        open(os.path.join(root, "topics", "%s.md" % t), "w").write(
            "# %s\n\n## Related Works\n\n%s\n" % (t, rel))
    for a in acts:
        rel = "\n".join("- [%s](../works/%s.md)" % (c["title"], c["slug"])
                        for c in cards if a in c.get("activities", []))
        open(os.path.join(root, "activities", "%s.md" % a), "w").write(
            "# %s\n\n## Related Works\n\n%s\n" % (a, rel))
    for c in cards:
        open(os.path.join(root, "works", "%s.md" % c["slug"]), "w").write(
            make_card(c["title"], c["slug"], c.get("topics"), c.get("activities"),
                      c.get("links", "- **Paper:** <https://arxiv.org/abs/2401.00001>")))
        if c.get("zh", True):
            zt = "# %s (2025)\n\n> [English](../../works/%s.md) | **简体中文**\n\n## Topics\n%s\n\n## Activities\n%s\n" % (
                c["title"], c["slug"],
                "\n".join("- [%s](../topics/%s.md)" % (t, t) for t in c.get("topics", [])),
                "\n".join("- [%s](../activities/%s.md)" % (a, a) for a in c.get("activities", []))
                or "N/A — evaluation methodology.")
            open(os.path.join(root, "zh", "works", "%s.md" % c["slug"]), "w").write(zt)
    return root
