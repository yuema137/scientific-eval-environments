"""Discovery source adapters (Phase 1 — lightweight metadata only).

Each adapter exposes .name and .search(query, since_iso, limit) -> list[record].
A record is a dict:
    {source, id, url, title, abstract_or_description, authors, date}
Adapters NEVER download full papers or clone/execute repositories.
Adding a new stable public source = adding one Source subclass.
"""
import os
import re
import time
import datetime as dt
import xml.etree.ElementTree as ET

from common import http_get, config, log


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


class ArxivOAISource(Source):
    """arXiv incremental discovery via OAI-PMH (the officially preferred bulk-metadata path).

    Instead of fanning out ~38 Search-API queries (one per taxonomy item — which trips arXiv's
    request-volume throttle from shared-cloud runners, yielding empty-200 feeds), we do a small
    number of paginated OAI-PMH harvests over a date window and match the taxonomy LOCALLY. The OAI
    `datestamp` (metadata last-modified) is the harvest cursor, NOT the paper date; the canonical
    submission date comes from the record's <created> field. Old papers resurfacing on a metadata
    update are harmless — existing-work dedup drops them.
    """
    name = "arxiv"
    ENDPOINT = "https://oaipmh.arxiv.org/oai"
    NS = {"o": "http://www.openarchives.org/OAI/2.0/", "ax": "http://arxiv.org/OAI/arXiv/"}

    def harvest(self, from_date, until_date, max_pages=50, delay=3.0, timeout=90):
        """Harvest arXiv metadata records with datestamp in [from_date, until_date] (YYYY-MM-DD),
        following resumptionToken pagination up to max_pages. Returns (records, requests, truncated).
        `truncated` is True if max_pages was hit with a token still pending (coverage incomplete)."""
        records, requests, token, truncated = [], 0, None, False
        for page in range(max_pages):
            params = ({"verb": "ListRecords", "resumptionToken": token} if token else
                      {"verb": "ListRecords", "metadataPrefix": "arXiv",
                       "from": from_date, "until": until_date})
            r = http_get(self.ENDPOINT, params=params, timeout=timeout)
            requests += 1
            root = ET.fromstring(r.text)
            err = root.find(".//o:error", self.NS)
            if err is not None:
                if err.get("code") == "noRecordsMatch":
                    break                                   # genuinely empty window
                raise RuntimeError("OAI error %s: %s" % (err.get("code"), (err.text or "")[:120]))
            for rec in root.findall(".//o:record", self.NS):
                hdr = rec.find("o:header", self.NS)
                if hdr is not None and hdr.get("status") == "deleted":
                    continue
                meta = rec.find(".//ax:arXiv", self.NS)
                if meta is not None:
                    records.append(self._parse(meta, hdr))
            rt = root.find(".//o:resumptionToken", self.NS)
            token = (rt.text or "").strip() if rt is not None else ""
            if not token:
                break
            if delay:
                time.sleep(delay)
        else:
            truncated = bool(token)                         # loop exhausted with a token still pending
        return records, requests, truncated

    def _parse(self, meta, hdr):
        ax = self.NS

        def t(tag):
            return (meta.findtext("ax:%s" % tag, default="", namespaces=ax) or "").strip()
        authors = []
        for a in meta.findall(".//ax:author", ax):
            nm = (" ".join([a.findtext("ax:forenames", default="", namespaces=ax) or "",
                            a.findtext("ax:keyname", default="", namespaces=ax) or ""])).strip()
            if nm:
                authors.append(nm)
        aid = t("id")
        return {
            "source": self.name,
            "id": aid,
            "url": "https://arxiv.org/abs/%s" % aid,
            "title": " ".join(t("title").split()),
            "abstract_or_description": " ".join(t("abstract").split()),
            "authors": authors,
            "date": t("created"),                            # canonical submission date (new-work signal)
            "updated": t("updated"),
            "categories": t("categories"),
            "datestamp": (hdr.findtext("o:datestamp", default="", namespaces=ax) if hdr is not None else ""),
        }


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
            # `odate` = when the note FIRST became public — the correct new-work signal, since a
            # submission can be created privately months before it is made visible (a paper made
            # public in Aug must be discoverable in Aug, not by its private-creation cdate). Fall
            # back to creation date only when odate is absent.
            pubdate = n.get("odate") or n.get("cdate") or n.get("tcdate")
            d = dt.datetime.utcfromtimestamp(pubdate / 1000.0) if pubdate else None
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


class HuggingFaceSource(Source):
    name = "huggingface"
    ENDPOINT = "https://huggingface.co/api/daily_papers"

    # Verified API contract (live-audited 2026-08). One endpoint, two modes:
    #   * ?date=YYYY-MM-DD -> the CURATED daily-papers feed for that calendar day. Complete for the
    #                         day (no relevance cutoff). Days with no feed return HTTP 200 and an
    #                         EMPTY list — weekends and holidays legitimately do this, so an empty
    #                         day is not a failure. An out-of-range date returns HTTP 400.
    #   * ?q=<terms>       -> relevance-ranked full-text search over papers, default 50, honours
    #                         `limit`. No server-side date window, so we filter by date client-side.
    # Both modes are used and unioned: the daily feed is the high-signal community-curated channel
    # this source exists for, while the term search covers taxonomy items whose papers were never
    # promoted to a daily feed.
    #
    # Records carry `paper.id`, which IS the arXiv id — so a HuggingFace record dedups against the
    # arXiv record for the same work via the ("arxiv", id) identity key (see deduplicate._ids).
    # Expect heavy overlap with arXiv; that is intended, and dedup collapses it for free.
    #
    # The daily-feed harvest depends only on the window, not on the query, so it is memoized per
    # `since_iso`: discovery calls search_many once per taxonomy item, and without memoization the
    # same handful of day requests would be re-issued dozens of times.
    def __init__(self):
        self._daily_cache = {}

    def _max_days(self):
        try:
            return int(config().get("huggingface", {}).get("max_days", 14))
        except Exception:
            return 14

    def _daily_window(self, since_iso):
        """Harvest the curated daily feed for every date in [since, today]. Memoized per window."""
        if since_iso in self._daily_cache:
            return self._daily_cache[since_iso], 0
        since = _parse_iso(since_iso)
        today = dt.datetime.utcnow().date()
        start = (since.date() if since else today)
        span = (today - start).days
        # Bound the harvest. The watermark's max_catchup_days already fails the run on a larger
        # backlog; this is a second, local guard so a bad watermark cannot fan out unboundedly.
        span = max(0, min(span, self._max_days()))
        out, reqs = {}, 0
        for i in range(span + 1):
            day = (today - dt.timedelta(days=span - i)).isoformat()
            try:
                r = http_get(self.ENDPOINT, params={"date": day})
                reqs += 1
            except Exception as e:
                # A single unreachable day must not sink the whole source; the term search and the
                # remaining days still run. Surfaced in the log so a systematic outage is visible.
                log("  ! huggingface daily feed %s failed: %s" % (day, e))
                continue
            for rec in self._records(r.json(), None):
                out.setdefault(rec["id"], rec)
        self._daily_cache[since_iso] = list(out.values())
        return self._daily_cache[since_iso], reqs

    def _records(self, payload, since):
        out = []
        for item in (payload or []):
            p = (item.get("paper") or {}) if isinstance(item, dict) else {}
            pid = p.get("id") or ""
            title = p.get("title") or (item.get("title") if isinstance(item, dict) else "") or ""
            if not pid or not title:
                continue
            d = _parse_iso(p.get("publishedAt") or (item.get("publishedAt") if isinstance(item, dict) else ""))
            if since and d:
                dd = d.replace(tzinfo=None) if d.tzinfo else d
                ss = since.replace(tzinfo=None) if since.tzinfo else since
                if dd < ss:
                    continue
            authors = [a.get("name", "") for a in (p.get("authors") or []) if isinstance(a, dict)]
            out.append({
                "source": self.name,
                "id": pid,
                "url": "https://arxiv.org/abs/%s" % pid,
                "title": " ".join(str(title).split()),
                "abstract_or_description": " ".join(str(p.get("summary") or "").split()),
                "authors": authors,
                "date": d.isoformat() if d else "",
                # Community-curation signal, kept for downstream triage. Not used for filtering
                # here: upvotes accrue over days, so gating on them would penalise fresh papers.
                "upvotes": p.get("upvotes", 0),
                "homepage": p.get("projectPage") or "",
            })
        return out

    def search(self, query, since_iso, limit):
        r = http_get(self.ENDPOINT, params={"q": query, "limit": limit})
        return self._records(r.json(), _parse_iso(since_iso))

    def search_many(self, queries, since_iso, limit):
        # Daily feed (memoized, window-scoped) unioned with ONE consolidated term search.
        recs, reqs = self._daily_window(since_iso)
        out = {r["id"]: r for r in recs}
        term = " ".join(queries) if queries else ""
        if term:
            for r in self.search(term, since_iso, limit):
                out.setdefault(r["id"], r)
            reqs += 1
        return list(out.values()), reqs


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
    # arXiv discovery uses OAI-PMH incremental harvesting (ArxivOAISource); the legacy Search-API
    # ArxivSource is retained only as a fallback/reference and is not used in production discovery.
    return {s.name: s for s in (ArxivOAISource(), OpenReviewSource(),
                                HuggingFaceSource(), GitHubSource())}
