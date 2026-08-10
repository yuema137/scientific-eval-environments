"""Discovery source adapters (Phase 1 — lightweight metadata only).

Each adapter exposes .name and .search(query, since_iso, limit) -> list[record].
A record is a dict:
    {source, id, url, title, abstract_or_description, authors, date}
Adapters NEVER download full papers or clone/execute repositories.
Adding a new stable public source = adding one Source subclass.
"""
import os
import re
import datetime as dt
import xml.etree.ElementTree as ET

from common import http_get, config


def _parse_iso(s):
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        return dt.datetime.fromisoformat(s)
    except ValueError:
        try:
            return dt.datetime.strptime(s[:10], "%Y-%m-%d")
        except ValueError:
            return None


class Source:
    name = "base"

    def search(self, query, since_iso, limit):  # pragma: no cover - interface
        raise NotImplementedError

    def search_many(self, queries, since_iso, limit):
        """Issue queries for one taxonomy item. Default: one request per query (fallback).
        Adapters override to consolidate synonym queries into a single request. Returns
        (records, requests_issued)."""
        out, reqs = {}, 0
        for q in queries:
            for r in self.search(q, since_iso, limit):
                out.setdefault(r["id"], r)
            reqs += 1
        return list(out.values()), reqs


class ArxivSource(Source):
    name = "arxiv"
    ENDPOINT = "https://export.arxiv.org/api/query"
    NS = {"a": "http://www.w3.org/2005/Atom"}

    def search(self, query, since_iso, limit):
        return self._fetch("all:%s" % query, since_iso, limit)

    def search_many(self, queries, since_iso, limit):
        # ONE consolidated request: (all:q1) OR (all:q2) ... — the union of the per-item synonym
        # queries in a single API call (arXiv supports boolean OR). matched_profiles stays at the
        # item granularity the caller tags. Raise max_results since one call returns the union.
        expr = " OR ".join("all:%s" % q for q in queries) or "all:agent"
        return self._fetch(expr, since_iso, min(limit * max(1, len(queries)), 200)), 1

    def _fetch(self, search_query, since_iso, limit):
        r = http_get(self.ENDPOINT, params={
            "search_query": search_query,
            "start": 0,
            "max_results": limit,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        })
        since = _parse_iso(since_iso)
        out = []
        root = ET.fromstring(r.text)
        for e in root.findall("a:entry", self.NS):
            aid_url = (e.findtext("a:id", default="", namespaces=self.NS) or "").strip()
            m = re.search(r"arxiv\.org/abs/([\w.\-]+?)(v\d+)?$", aid_url)
            arxiv_id = m.group(1) if m else aid_url
            # new-work discovery keys on INITIAL submission date, not lastUpdatedDate, so a v2/v3
            # revision of an old paper is not surfaced as a new work.
            published = (e.findtext("a:published", default="", namespaces=self.NS) or "").strip()
            d = _parse_iso(published)
            if since and d and d.tzinfo:
                since_cmp = since if since.tzinfo else since.replace(tzinfo=d.tzinfo)
                if d < since_cmp:
                    continue
            authors = [a.findtext("a:name", default="", namespaces=self.NS)
                       for a in e.findall("a:author", self.NS)]
            out.append({
                "source": self.name,
                "id": arxiv_id,
                "url": "https://arxiv.org/abs/%s" % arxiv_id,
                "title": " ".join((e.findtext("a:title", default="", namespaces=self.NS) or "").split()),
                "abstract_or_description": " ".join(
                    (e.findtext("a:summary", default="", namespaces=self.NS) or "").split()),
                "authors": [a for a in authors if a],
                "date": published,
            })
        return out


class OpenReviewSource(Source):
    name = "openreview"
    ENDPOINT = "https://api2.openreview.net/notes/search"

    # Verified API2 contract (live-audited 2026-08): /notes/search is a RELEVANCE-ranked full-text
    # endpoint that offers NO reliable server-side new-work window.
    #   * sort=cdate:desc / sort=tmdate:desc  -> accepted (HTTP 200) but NOT honored (results stay
    #                                            relevance-ordered, not date-descending);
    #   * sort=pdate:desc / sort=mdate:desc   -> HTTP 400 (no such sortable field);
    #   * mintcdate / mincdate / mindate      -> accepted but silently ignored (still returns old notes).
    # The date-filterable /notes GET endpoint, conversely, has no full-text term search. So there is
    # no way to combine "matches our taxonomy terms" with "created in the last N days" server-side.
    # Smallest recall-safe strategy: fetch a bounded-depth relevance page restricted to submission
    # (forum) notes, then filter by CREATION date (cdate) client-side. cdate = new-work semantics; we
    # deliberately do NOT sort/filter by tmdate, which would surface recently-MODIFIED old works.
    # Because submissions arrive in venue-deadline BURSTS (ICLR/NeurIPS windows), a short window
    # legitimately yields few/zero hits — expected, not a failure (arXiv is the primary recency source).
    # `source=forum` also drops reviews/comments/decision notes, which have no title and are discarded.
    def search_many(self, queries, since_iso, limit):
        # one request per item using an OR term; the endpoint treats the whole term as full-text.
        # Scan a bounded-depth relevance page so recent matches present in the ranking survive the
        # client-side cdate filter.
        term = " OR ".join(queries) if queries else ""
        recs = self.search(term, since_iso, min(limit * 2, 100))
        return recs, 1

    def search(self, query, since_iso, limit):
        r = http_get(self.ENDPOINT, params={"term": query, "limit": limit, "source": "forum"})
        since = _parse_iso(since_iso)
        out = []
        for n in (r.json().get("notes") or []):
            c = n.get("content") or {}

            def _v(k):
                v = c.get(k)
                return v.get("value") if isinstance(v, dict) else v
            cdate = n.get("cdate") or n.get("tcdate")
            d = dt.datetime.utcfromtimestamp(cdate / 1000.0) if cdate else None
            if since and d and d < (since.replace(tzinfo=None) if since.tzinfo else since):
                continue
            nid = n.get("id", "")
            title = _v("title") or ""
            if not title:
                continue
            out.append({
                "source": self.name,
                "id": nid,
                "url": "https://openreview.net/forum?id=%s" % nid,
                "title": " ".join(str(title).split()),
                "abstract_or_description": " ".join(str(_v("abstract") or "").split()),
                "authors": _v("authors") or [],
                "date": d.isoformat() if d else "",
            })
        return out


class GitHubSource(Source):
    name = "github"
    ENDPOINT = "https://api.github.com/search/repositories"

    def _headers(self):
        h = {"Accept": "application/vnd.github+json"}
        tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
        if tok:
            h["Authorization"] = "Bearer %s" % tok
        return h

    def search(self, query, since_iso, limit):
        # new-work discovery keys on repository CREATION date (a standalone repo), not pushed/updated,
        # so an old repo with a recent commit is not surfaced as a new work.
        since_day = (since_iso or "")[:10]
        q = query
        if since_day:
            q = "%s created:>=%s" % (query, since_day)
        r = http_get(self.ENDPOINT, params={
            "q": q, "sort": "updated", "order": "desc", "per_page": min(limit, 50),
        }, headers=self._headers())
        out = []
        for it in (r.json().get("items") or [])[:limit]:
            out.append({
                "source": self.name,
                "id": it.get("full_name", ""),
                "url": it.get("html_url", ""),
                "title": it.get("full_name", ""),
                "abstract_or_description": " ".join((it.get("description") or "").split()),
                "authors": [(it.get("owner") or {}).get("login", "")],
                "date": it.get("created_at") or it.get("pushed_at") or "",
                "created_at": it.get("created_at") or "",
                "topics": it.get("topics") or [],
                "homepage": it.get("homepage") or "",
                "stars": it.get("stargazers_count", 0),
            })
        return out


def all_sources():
    return {s.name: s for s in (ArxivSource(), OpenReviewSource(), GitHubSource())}
