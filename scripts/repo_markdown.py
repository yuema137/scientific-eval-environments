"""Shared parsing primitives for the repository's stable Markdown card format."""
import re

SECTION_RE = re.compile(r'^##\s+(.+?)\s*\n(.*?)(?=^##\s|\Z)', re.M | re.S)
FIRST_APPEARED_RE = re.compile(
    r'^> \*\*First appeared:\*\* (\d{4}-\d{2}-\d{2}) · '
    r'\*\*Source:\*\* \[([^]]+)\]\((https?://[^)]+)\)$', re.M)


def section(text, heading):
    """Return the unstripped section body, or None when the heading is missing."""
    match = re.search(r'^##\s+' + re.escape(heading) + r'\s*\n(.*?)(?=^##\s|\Z)',
                      text, re.S | re.M)
    return match.group(1) if match else None


def sections(text):
    return {heading.strip(): body.strip() for heading, body in SECTION_RE.findall(text)}
