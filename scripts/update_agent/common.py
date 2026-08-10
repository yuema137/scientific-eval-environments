"""Shared helpers for the Daily Update Agent.

Deterministic, dependency-light. The canonical taxonomy is READ FROM THE REPO
(topic/domain/activity page H1s) — never hard-coded — so the pipeline adapts as
axes evolve.
"""
import os
import re
import sys
import time
import json
import glob
import functools

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUTOMATION = os.path.join(REPO_ROOT, "automation", "update_agent")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def load_yaml(path):
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)


@functools.lru_cache(maxsize=1)
def config():
    return load_yaml(os.path.join(AUTOMATION, "config.yaml"))


def _page_title(path):
    with open(path) as f:
        for line in f:
            m = re.match(r"^#\s+(.*?)\s*$", line)
            if m:
                return m.group(1).strip()
    return os.path.basename(path)[:-3]


def taxonomy(repo_root=REPO_ROOT):
    """Return {'domains': {title: file}, 'topics': {...}, 'activities': {...}}
    discovered from the repository. Activities is empty if the axis is absent."""
    out = {}
    for axis in ("domains", "topics", "activities"):
        d = os.path.join(repo_root, axis)
        items = {}
        if os.path.isdir(d):
            for p in sorted(glob.glob(os.path.join(d, "*.md"))):
                if os.path.basename(p) == "README.md":
                    continue
                items[_page_title(p)] = os.path.basename(p)[:-3]
        out[axis] = items
    return out


def search_profiles(repo_root=REPO_ROOT):
    base = os.path.join(repo_root, "automation", "update_agent", "search_profiles")
    prof = {}
    for axis in ("domains", "topics", "activities"):
        p = os.path.join(base, axis + ".yaml")
        prof[axis] = load_yaml(p) if os.path.exists(p) else {}
    gp = os.path.join(base, "global.yaml")
    prof["global"] = (load_yaml(gp) or {}).get("queries", []) if os.path.exists(gp) else []
    return prof


def http_get(url, params=None, headers=None, timeout=None, attempts=None, backoff=None):
    """GET with bounded exponential-backoff retry. Raises after exhausting attempts.
    Distinguishes transient operational failure (raise) from empty-but-ok responses."""
    import requests
    cfg = config()
    timeout = timeout or cfg["http"]["timeout_seconds"]
    attempts = attempts or cfg["retry"]["attempts"]
    backoff = backoff or cfg["retry"]["backoff_seconds"]
    h = {"User-Agent": cfg["http"]["user_agent"]}
    if headers:
        h.update(headers)
    backoff_cap = 30           # never sleep longer than this on a single retry (avoid storms)
    last = None
    for i in range(attempts):
        wait = min(backoff * (2 ** i), backoff_cap)
        try:
            r = requests.get(url, params=params, headers=h, timeout=timeout)
            if r.status_code == 200:
                return r
            if r.status_code in (403, 429, 500, 502, 503, 504):   # incl. 403 = secondary rate limit
                last = "HTTP %d" % r.status_code
                ra = r.headers.get("Retry-After")
                if ra and ra.isdigit():
                    wait = min(int(ra), backoff_cap)
            else:
                r.raise_for_status()
                return r
        except Exception as e:  # noqa: BLE001 - transient network error
            last = str(e)
        if i < attempts - 1:
            time.sleep(wait)
    raise RuntimeError("http_get failed for %s after %d attempts: %s" % (url, attempts, last))


def normalize_title(title):
    """Lowercase, strip punctuation/whitespace for title-identity comparison."""
    t = (title or "").lower()
    t = re.sub(r"[‐-―]", "-", t)          # unicode dashes -> hyphen
    t = re.sub(r"[^a-z0-9]+", " ", t)               # drop punctuation
    return re.sub(r"\s+", " ", t).strip()


def normalize_arxiv_id(raw):
    if not raw:
        return None
    m = re.search(r"(\d{4}\.\d{4,5})(v\d+)?", raw)
    return m.group(1) if m else None


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False, sort_keys=True)
    return path


def read_json(path):
    with open(path) as f:
        return json.load(f)
