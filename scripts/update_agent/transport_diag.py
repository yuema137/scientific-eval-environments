"""Bounded transport diagnostic for arXiv access from the current execution path.

Characterizes ONE arXiv Search API request and a bounded OAI-PMH probe (Identify + one
date-bounded ListRecords page), printing only sanitized metadata — HTTP status, content type,
body size, parsed counts, a few non-sensitive headers. No credentials, no large bodies. Intended
to run from a GitHub Actions runner to compare the two arXiv access paths. Respects arXiv's legacy
API policy: single connection, >= 3s between requests.
"""
import sys
import time
import xml.etree.ElementTree as ET
import datetime as dt

import requests

UA = {"User-Agent": "sci-eval-environments-transport-diagnostic (+https://github.com/yuema137/scientific-eval-environments)"}
SEARCH = "https://export.arxiv.org/api/query"
OAI = "https://oaipmh.arxiv.org/oai"
ATOM = {"a": "http://www.w3.org/2005/Atom", "os": "http://a9.com/-/spec/opensearch/1.1/"}
OAINS = {"o": "http://www.openarchives.org/OAI/2.0/", "ax": "http://arxiv.org/OAI/arXiv/"}
_KEEP_HEADERS = ("content-type", "content-length", "server", "date", "retry-after",
                 "x-ratelimit-remaining", "x-ratelimit-limit", "cf-ray", "via", "age")


def _headers(r):
    return {k: v for k, v in r.headers.items() if k.lower() in _KEEP_HEADERS}


def _get(url, params, timeout=120):
    t0 = time.monotonic()
    r = requests.get(url, params=params, headers=UA, timeout=timeout)
    return r, round(time.monotonic() - t0, 1)


def diag_search():
    out = {"probe": "search_api", "url": SEARCH}
    try:
        r, secs = _get(SEARCH, {"search_query": "all:LLM agent benchmark OR all:scientific agent",
                                "start": 0, "max_results": 50, "sortBy": "submittedDate",
                                "sortOrder": "descending"})
        out.update({"http_status": r.status_code, "seconds": secs, "body_bytes": len(r.content),
                    "headers": _headers(r)})
        valid, total, entries = False, None, None
        try:
            root = ET.fromstring(r.text)
            valid = True
            tr = root.find(".//os:totalResults", ATOM)
            total = int(tr.text) if tr is not None and tr.text else None
            entries = len(root.findall("a:entry", ATOM))
        except ET.ParseError as e:
            out["parse_error"] = str(e)[:200]
        out.update({"valid_atom": valid, "opensearch_totalResults": total, "entries_returned": entries})
    except Exception as e:  # noqa: BLE001
        out["transport_error"] = str(e)[:200]
    return out


def diag_oai():
    results = {}
    # 1) Identify
    ident = {"probe": "oai_identify", "url": OAI}
    try:
        r, secs = _get(OAI, {"verb": "Identify"})
        ident.update({"http_status": r.status_code, "seconds": secs, "body_bytes": len(r.content),
                      "headers": _headers(r)})
        try:
            root = ET.fromstring(r.text)
            ident["repositoryName"] = (root.findtext(".//o:repositoryName", default="", namespaces=OAINS) or None)
            ident["granularity"] = (root.findtext(".//o:granularity", default="", namespaces=OAINS) or None)
            ident["valid_xml"] = True
        except ET.ParseError as e:
            ident["valid_xml"] = False
            ident["parse_error"] = str(e)[:200]
    except Exception as e:  # noqa: BLE001
        ident["transport_error"] = str(e)[:200]
    results["identify"] = ident

    time.sleep(3)
    # 2) one bounded date-window ListRecords page (1 day, to bound volume)
    lr = {"probe": "oai_listrecords", "url": OAI}
    day = (dt.datetime.utcnow() - dt.timedelta(days=1)).date().isoformat()
    lr["window"] = {"from": day, "until": day, "metadataPrefix": "arXiv"}
    try:
        r, secs = _get(OAI, {"verb": "ListRecords", "metadataPrefix": "arXiv", "from": day, "until": day})
        lr.update({"http_status": r.status_code, "seconds": secs, "body_bytes": len(r.content),
                   "headers": _headers(r)})
        try:
            root = ET.fromstring(r.text)
            recs = root.findall(".//o:record", OAINS)
            lr["records_page1"] = len(recs)
            rt = root.find(".//o:resumptionToken", OAINS)
            lr["has_resumption_token"] = bool(rt is not None and (rt.text or "").strip())
            lr["completeListSize"] = rt.get("completeListSize") if rt is not None else None
            # parse one record's canonical fields to prove the metadata we need is present
            if recs:
                meta = recs[0].find(".//ax:arXiv", OAINS)
                if meta is not None:
                    lr["sample_record"] = {
                        "id": meta.findtext("ax:id", default="", namespaces=OAINS),
                        "created": meta.findtext("ax:created", default="", namespaces=OAINS),
                        "updated": meta.findtext("ax:updated", default="", namespaces=OAINS),
                        "has_title": bool(meta.findtext("ax:title", default="", namespaces=OAINS)),
                        "has_abstract": bool(meta.findtext("ax:abstract", default="", namespaces=OAINS)),
                        "categories": meta.findtext("ax:categories", default="", namespaces=OAINS),
                        "authors": len(meta.findall(".//ax:author", OAINS)),
                    }
            lr["valid_xml"] = True
        except ET.ParseError as e:
            lr["valid_xml"] = False
            lr["parse_error"] = str(e)[:200]
    except Exception as e:  # noqa: BLE001
        lr["transport_error"] = str(e)[:200]
    results["listrecords"] = lr
    return results


def _emit(title, obj, lines):
    import json
    lines.append("### %s" % title)
    lines.append("```json")
    lines.append(json.dumps(obj, indent=2, ensure_ascii=False))
    lines.append("```")


def main():
    import json
    import os
    lines = []
    search = diag_search()
    time.sleep(3)
    oai = diag_oai()
    _emit("arXiv Search API", search, lines)
    _emit("arXiv OAI-PMH Identify", oai["identify"], lines)
    _emit("arXiv OAI-PMH ListRecords (1-day)", oai["listrecords"], lines)

    # concise verdict
    s_empty = (search.get("http_status") == 200 and search.get("valid_atom")
               and (search.get("entries_returned") == 0))
    oai_ok = (oai["identify"].get("http_status") == 200
              and (oai["listrecords"].get("records_page1") or 0) > 0)
    verdict = ("Search API empty-200: %s | OAI-PMH usable: %s" % (s_empty, oai_ok))
    lines.append("### Verdict")
    lines.append(verdict)

    text = "\n".join(lines)
    print(text)
    summ = os.environ.get("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")
    print("\nMACHINE:", json.dumps({"search": search, "oai": oai, "verdict": verdict}), file=sys.stderr)


if __name__ == "__main__":
    main()
