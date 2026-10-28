"""Discovery coverage and stability (2026-10 recall audit): chunked arXiv harvesting, the revision
filter, the missing-state-branch guard, the manual window override and watermark non-regression,
the OpenReview zero-hit warning, and full-window HuggingFace harvesting. All deterministic."""
import argparse
import json

import pytest

import discover
import sources
import watermark


def _agent_rec(aid, created="2026-08-09", title="AgentBench: a benchmark for LLM agents"):
    return {"source": "arxiv", "id": aid, "title": title,
            "abstract_or_description": "A benchmark evaluating autonomous LLM agents.",
            "authors": ["X"], "date": created, "categories": "cs.AI"}


class _ChunkFake:
    """Fake OAI source keyed by chunk start day. `plan[day]` is a list of records, or the string
    'truncated' / 'error'. Unlisted days are empty. Records every call."""
    name = "arxiv"

    def __init__(self, plan=None, pages=1):
        self.plan = plan or {}
        self.pages = pages
        self.calls = []

    def harvest(self, frm, until, max_pages=50, delay=0):
        self.calls.append((frm, until, max_pages))
        p = self.plan.get(frm, [])
        if p == "error":
            raise RuntimeError("boom")
        if p == "truncated":
            return [_agent_rec("2608.%05d" % len(self.calls))], max_pages, True
        return list(p), self.pages, False


def _run(monkeypatch, tmp_path, srcs, since, until, cfg_patch=None):
    monkeypatch.setattr(discover, "all_sources", lambda: srcs)
    monkeypatch.setattr(discover, "taxonomy",
                        lambda *a, **k: {"domains": {"Physics": "physics"}, "topics": {}, "activities": {}})
    monkeypatch.setattr(discover, "search_profiles", lambda *a, **k:
                        {"domains": {"Physics": ["LLM agent physics benchmark"]},
                         "topics": {}, "activities": {}, "global": []})
    monkeypatch.setattr(discover, "_DELAY", {"arxiv": 0, "openreview": 0, "huggingface": 0, "github": 0})
    if cfg_patch:
        base = discover.config()
        merged = dict(base)
        for k, v in cfg_patch.items():
            merged[k] = dict(base.get(k, {}), **v)
        monkeypatch.setattr(discover, "config", lambda: merged)
    return discover.run("full", str(tmp_path / "rt"), since_iso=since, now_iso=until)


# ------------------------------------------------------------ 1. chunked arXiv harvest
def test_day_chunks_cover_the_window_exactly():
    assert discover._day_chunks("2026-09-28", "2026-10-02", 1) == [
        ("2026-09-28", "2026-09-28"), ("2026-09-29", "2026-09-29"), ("2026-09-30", "2026-09-30"),
        ("2026-10-01", "2026-10-01"), ("2026-10-02", "2026-10-02")]
    assert discover._day_chunks("2026-10-01", "2026-10-07", 3) == [
        ("2026-10-01", "2026-10-03"), ("2026-10-04", "2026-10-06"), ("2026-10-07", "2026-10-07")]


def test_large_window_is_harvested_day_by_day_with_a_per_chunk_budget(tmp_path, monkeypatch):
    # A 60-day window used to share ONE 50-page cap; now every day gets its own budget.
    src = _ChunkFake({"2026-09-17": [_agent_rec("2609.21157", "2026-09-17")],
                      "2026-10-21": [_agent_rec("2610.29932", "2026-10-21")]}, pages=3)
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-08-23T00:00:00", "2026-10-21T12:00:00")
    assert len(src.calls) == 60 and src.calls[0][:2] == ("2026-08-23", "2026-08-23")
    assert src.calls[-1][:2] == ("2026-10-21", "2026-10-21")
    assert all(c[2] == 50 for c in src.calls)                       # per-chunk max_pages
    assert cov["sources"]["arxiv"] == "success" and cov["discovery_credible"] is True
    assert cov["arxiv_harvest"]["complete_through"] == "2026-10-21"
    ids = {r["id"] for r in json.loads((tmp_path / "rt" / "phase1" / "raw_hits.json").read_text())}
    assert ids == {"2609.21157", "2610.29932"}


def test_a_truncated_chunk_is_suspicious_and_names_the_complete_prefix(tmp_path, monkeypatch):
    src = _ChunkFake({"2026-10-01": [_agent_rec("2610.00001", "2026-10-01")],
                      "2026-10-02": "truncated"})
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-10-01T00:00:00", "2026-10-03T00:00:00")
    assert cov["sources"]["arxiv"] == "suspicious_empty" and cov["discovery_credible"] is False
    assert cov["arxiv_harvest"]["complete_through"] == "2026-10-01"
    assert "truncated" in cov["source_status_detail"]["arxiv"]
    assert len(src.calls) == 3                                     # later chunks still harvested


def test_total_page_budget_bounds_cost_and_flags_skipped_chunks(tmp_path, monkeypatch):
    src = _ChunkFake({d: [_agent_rec("2610.0000%d" % i, d)]
                      for i, d in enumerate(["2026-10-01", "2026-10-02", "2026-10-03"])}, pages=2)
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-10-01T00:00:00", "2026-10-05T00:00:00",
               cfg_patch={"arxiv_oai": {"max_total_pages": 4}})
    assert len(src.calls) == 2                                     # 2 + 2 pages, then budget is spent
    assert [c["status"] for c in cov["arxiv_harvest"]["chunks"]][2:] == ["skipped_budget"] * 3
    assert cov["sources"]["arxiv"] == "suspicious_empty"
    assert cov["arxiv_harvest"]["complete_through"] == "2026-10-02"


def test_partial_chunk_error_is_suspicious_but_all_errors_is_failure(tmp_path, monkeypatch):
    src = _ChunkFake({"2026-10-01": [_agent_rec("2610.00001", "2026-10-01")], "2026-10-02": "error"})
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-10-01T00:00:00", "2026-10-02T12:00:00")
    assert cov["sources"]["arxiv"] == "suspicious_empty" and cov["raw_by_source"]["arxiv"] == 1
    src = _ChunkFake({"2026-10-01": "error", "2026-10-02": "error"})
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-10-01T00:00:00", "2026-10-02T12:00:00")
    assert cov["sources"]["arxiv"] == "failure"


# ------------------------------------------------------------ 2. revision filter
@pytest.mark.parametrize("aid,created,expect,basis", [
    ("2610.23251", "2026-10-16", "2026-10-16", "created"),       # consistent <created> = v1
    ("2312.10986", "2026-10-23", "2023-12-31", "id_month"),      # <created> is a revision date
    ("2610.00001", "2026-09-29", "2026-09-29", "created"),       # month-boundary v1 is consistent
    ("hep-th/0101001", "", "2001-01-31", "id_month"),            # old-style id
])
def test_first_submission_estimate(aid, created, expect, basis):
    d, b = sources.first_submission_estimate(aid, created)
    assert d.isoformat() == expect and b == basis


def test_first_submission_estimate_unknown_id_is_kept():
    assert sources.first_submission_estimate("not-an-id", "2026-10-01") == (None, "unknown")


def test_revised_old_papers_are_dropped_and_recorded(tmp_path, monkeypatch):
    new = _agent_rec("2610.33624", "2026-10-24")
    revised = _agent_rec("2312.10986", "2026-10-23")              # what OAI reported on 2026-10-26
    prev_month = _agent_rec("2609.40097", "")                     # id month within the grace period
    stale = _agent_rec("2609.05818", "2026-09-05")                # consistent v1 well before window
    off_topic_new = {"source": "arxiv", "id": "2610.11111", "title": "Galaxy mergers",
                     "abstract_or_description": "We simulate galaxies.", "authors": [],
                     "date": "2026-10-24", "categories": "astro-ph", "datestamp": "2026-10-24"}
    src = _ChunkFake({"2026-10-24": [new, revised, prev_month, stale, off_topic_new]})
    cov = _run(monkeypatch, tmp_path, {"arxiv": src}, "2026-10-24T00:00:00", "2026-10-27T00:00:00")
    p1 = tmp_path / "rt" / "phase1"
    kept = {r["id"] for r in json.loads((p1 / "raw_hits.json").read_text())}
    assert kept == {"2610.33624", "2609.40097"}
    dropped = json.loads((p1 / "arxiv_revisions_dropped.json").read_text())
    assert {d["id"] for d in dropped} == {"2312.10986", "2609.05818"}
    assert {d["first_submitted_estimate"] for d in dropped} == {"2023-12-31", "2026-09-05"}
    assert all(d["matched_profiles"] for d in dropped)
    assert cov["arxiv_harvest"]["revisions_dropped_total"] == 2
    # 8. records rejected by the local-match gate are saved too (compact, no abstract)
    unmatched = json.loads((p1 / "arxiv_local_unmatched.json").read_text())
    assert [u["id"] for u in unmatched] == ["2610.11111"]
    assert "abstract_or_description" not in unmatched[0]
    assert cov["arxiv_harvest"]["local_unmatched"] == 1


# ------------------------------------------------------------ 3. missing state branch
def test_compute_window_requires_watermark_in_production():
    w = watermark.compute_window("2026-10-27T00:00:00+00:00", None, 72, 60, 3, require_watermark=True)
    assert w["missing_watermark"] is True and w["start_iso"] is None
    assert w["basis"] == "missing_watermark"


def _run_phase(monkeypatch, tmp_path, wm_state, env=None, discovery_stub=None):
    import run_phase
    monkeypatch.setattr(run_phase, "RUN_DIR", str(tmp_path / "runtime"))
    monkeypatch.setattr(run_phase.watermark, "read_watermark",
                        lambda: {"last_success": None, "state": wm_state})
    monkeypatch.setattr(run_phase.watermark, "now_iso", lambda: "2026-10-27T12:00:00+00:00")
    for k in ("WINDOW_START", "WINDOW_END", "GITHUB_STEP_SUMMARY", "GITHUB_OUTPUT"):
        monkeypatch.delenv(k, raising=False)
    for k, v in (env or {}).items():
        monkeypatch.setenv(k, v)
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    if discovery_stub:
        monkeypatch.setattr(run_phase.discovery, "run", discovery_stub)
    return run_phase, summary


@pytest.mark.parametrize("state", ["branch_missing", "file_missing", "unparseable", "fetch_failed"])
def test_missing_state_branch_fails_visibly_instead_of_default_lookback(tmp_path, monkeypatch, state):
    def _must_not_run(*a, **k):
        raise AssertionError("discovery must not run without a watermark")
    run_phase, summary = _run_phase(monkeypatch, tmp_path, state, discovery_stub=_must_not_run)
    with pytest.raises(SystemExit) as e:
        run_phase.cmd_discover(argparse.Namespace(mode="full"))
    assert e.value.code == 1
    st = json.loads((tmp_path / "runtime" / "state" / "discovery.json").read_text())
    assert st["status"] == "fail" and st["summary"]["needs_attention"] == "watermark state missing"
    text = summary.read_text()
    assert "needs_attention" in text and "auto/updater-state" in text and "window_start" in text


def test_override_is_the_bootstrap_path_when_state_is_missing(tmp_path, monkeypatch):
    seen = {}

    class _Stop(Exception):
        pass

    def _stub(mode, run_dir, now_iso=None, since_iso=None, until_iso=None, window_info=None):
        seen.update(since=since_iso, until=until_iso, info=window_info)
        raise _Stop()
    run_phase, _ = _run_phase(monkeypatch, tmp_path, "branch_missing",
                              env={"WINDOW_START": "2026-09-17", "WINDOW_END": "2026-09-23"},
                              discovery_stub=_stub)
    with pytest.raises(_Stop):
        run_phase.cmd_discover(argparse.Namespace(mode="full"))
    assert seen["since"].startswith("2026-09-17T00:00:00")
    assert seen["until"].startswith("2026-09-23T23:59:59")
    assert seen["info"]["override"] is True and seen["info"]["basis"] == "override"
    assert seen["info"]["watermark_state"] == "branch_missing"


def test_invalid_override_fails_visibly(tmp_path, monkeypatch):
    run_phase, summary = _run_phase(monkeypatch, tmp_path, "present",
                                    env={"WINDOW_START": "2026-13-01"})
    with pytest.raises(SystemExit) as e:
        run_phase.cmd_discover(argparse.Namespace(mode="full"))
    assert e.value.code == 1 and "invalid window override" in summary.read_text()


# ------------------------------------------------------------ 5. override parsing + non-regression
NOW = "2026-10-27T12:00:00+00:00"


def test_parse_override_unset_is_none():
    assert watermark.parse_override("", "", NOW, 60) is None
    assert watermark.parse_override(None, None, NOW, 60) is None


def test_parse_override_dates_are_inclusive_and_end_defaults_to_now():
    o = watermark.parse_override("2026-09-17", "2026-09-23", NOW, 60)
    assert o == {"start_iso": "2026-09-17T00:00:00+00:00", "end_iso": "2026-09-23T23:59:59+00:00"}
    o = watermark.parse_override("2026-10-20", "", NOW, 60)
    assert o["end_iso"] == NOW
    o = watermark.parse_override("2026-10-20", "2026-12-01", NOW, 60)   # future end is clipped
    assert o["end_iso"] == NOW


@pytest.mark.parametrize("start,end", [
    ("", "2026-10-01"),                 # end without start
    ("yesterday", ""),                  # unparseable
    ("2026-10-10", "2026-10-01"),       # reversed
    ("2026-11-01", ""),                 # starts in the future
    ("2026-07-01", "2026-10-01"),       # over the span limit
])
def test_parse_override_rejects_bad_windows(start, end):
    with pytest.raises(ValueError):
        watermark.parse_override(start, end, NOW, 60)


def _cov(end, override=False, credible=True):
    return {"discovery_credible": credible, "suspicious_empty": [] if credible else ["arxiv"],
            "search_window": {"start": "2026-09-17T00:00:00+00:00", "end": end, "override": override}}


def test_override_never_advances_an_existing_watermark():
    ok, _, why = watermark.advance_decision(_cov("2026-10-27T12:00:00+00:00", override=True),
                                            "2026-10-20T00:00:00+00:00", "present")
    assert ok is False and "override" in why


def test_override_seeds_an_absent_watermark():
    for state in ("branch_missing", "file_missing"):
        ok, ts, _ = watermark.advance_decision(_cov("2026-09-23T23:59:59+00:00", override=True),
                                               None, state)
        assert ok is True and ts == "2026-09-23T23:59:59+00:00"


def test_regular_run_never_moves_the_watermark_backwards():
    ok, _, _ = watermark.advance_decision(_cov("2026-10-19T00:00:00+00:00"),
                                          "2026-10-20T00:00:00+00:00", "present")
    assert ok is False
    ok, ts, _ = watermark.advance_decision(_cov("2026-10-27T00:00:00+00:00"),
                                           "2026-10-20T00:00:00+00:00", "present")
    assert ok is True and ts == "2026-10-27T00:00:00+00:00"


def test_advance_refuses_incredible_or_unreadable_state():
    assert watermark.advance_decision(_cov("2026-10-27T00:00:00+00:00", credible=False),
                                      "2026-10-20T00:00:00+00:00")[0] is False
    for state in ("fetch_failed", "unparseable"):
        assert watermark.advance_decision(_cov("2026-10-27T00:00:00+00:00"), None, state)[0] is False


# ------------------------------------------------------------ 6. OpenReview zero-hit warning
class _EmptyOR:
    name = "openreview"

    def search_many(self, queries, since, limit, until_iso=None):
        return [], 1


def test_openreview_zero_hits_over_a_real_window_is_a_visible_nonblocking_warning(tmp_path, monkeypatch):
    srcs = {"arxiv": _ChunkFake({"2026-10-20": [_agent_rec("2610.30000", "2026-10-20")]}),
            "openreview": _EmptyOR()}
    cov = _run(monkeypatch, tmp_path, srcs, "2026-10-20T00:00:00", "2026-10-27T00:00:00")
    assert cov["sources"]["openreview"] == "success"                   # does not block the run
    assert cov["discovery_credible"] is True                           # nor hold the watermark
    w = cov["source_warnings"]["openreview"]
    assert len(w) == 1 and w[0].startswith("0 records across 1 request(s) for a 7-day window")


def test_openreview_zero_hits_over_a_trivial_window_is_quiet(tmp_path, monkeypatch):
    srcs = {"arxiv": _ChunkFake({"2026-10-26": [_agent_rec("2610.30000", "2026-10-26")]}),
            "openreview": _EmptyOR()}
    cov = _run(monkeypatch, tmp_path, srcs, "2026-10-26T00:00:00", "2026-10-27T00:00:00")
    assert "openreview" not in cov["source_warnings"]


# ------------------------------------------------------------ 7. HuggingFace covers the whole window
class _EmptyResp:
    def json(self):
        return []


def _hf_days(monkeypatch):
    days = []

    def _get(url, params=None, **k):
        days.append((params or {}).get("date"))
        return _EmptyResp()
    monkeypatch.setattr(sources, "http_get", _get)
    return days


def test_huggingface_daily_feed_covers_a_bounded_backfill_window(monkeypatch):
    days = _hf_days(monkeypatch)
    src = sources.HuggingFaceSource()
    src._daily_window("2026-09-06T00:00:00", "2026-10-05T23:59:59")
    assert days[0] == "2026-09-06" and days[-1] == "2026-10-05" and len(days) == 30
    assert src.warnings() == []


def test_huggingface_reports_days_it_did_not_fetch(monkeypatch):
    days = _hf_days(monkeypatch)
    monkeypatch.setattr(sources, "config", lambda: {"huggingface": {"max_days": 9}})
    src = sources.HuggingFaceSource()
    src._daily_window("2026-09-01T00:00:00", "2026-09-30T00:00:00")
    assert len(days) == 10 and days[0] == "2026-09-21"
    assert src.warnings() == ["daily feed limited to the last 10 of 30 days; 2026-09-01..2026-09-20 not fetched"]


def test_huggingface_warnings_reach_the_discovery_report(tmp_path, monkeypatch):
    class _HF(sources.HuggingFaceSource):
        def search_many(self, queries, since, limit, until_iso=None):
            self._warnings = ["daily feed unreachable for 1 day(s): 2026-10-21"]
            return [], 1
    srcs = {"arxiv": _ChunkFake({"2026-10-20": [_agent_rec("2610.30000", "2026-10-20")]}),
            "huggingface": _HF()}
    cov = _run(monkeypatch, tmp_path, srcs, "2026-10-20T00:00:00", "2026-10-22T00:00:00")
    assert cov["source_warnings"]["huggingface"] == ["daily feed unreachable for 1 day(s): 2026-10-21"]
