import json
import os

import prefilter
import deduplicate
import relevance
from conftest import build_mini_repo


# ------------------------------------------------------------ prefilter
def _arx(title, abstract=""):
    return {"source": "arxiv", "id": "2501.00001", "url": "", "title": title,
            "abstract_or_description": abstract, "authors": []}


def _gh(name, desc="", topics=None):
    return {"source": "github", "id": name, "url": "https://github.com/%s" % name,
            "title": name, "abstract_or_description": desc, "authors": [], "topics": topics or []}


def test_prefilter_arxiv_positive():
    assert prefilter.judge(_arx("AgentBench: A Benchmark for Evaluating LLM Agents"))[0] is True
    assert prefilter.judge(_arx("Scientific Agent Benchmark for Physics Reasoning"))[0] is True


def test_prefilter_arxiv_negative():
    assert prefilter.judge(_arx("A New Transformer Architecture for Image Classification"))[0] is False
    # a method paper that merely evaluates itself, no agent/benchmark contribution
    assert prefilter.judge(_arx("Efficient Fine-Tuning of Diffusion Models",
                                "We propose a method and evaluate it on standard datasets."))[0] is False


def test_prefilter_github_positive():
    assert prefilter.judge(_gh("org/scibench", "Benchmark for evaluating LLM agents on chemistry"))[0] is True
    assert prefilter.judge(_gh("lab/agent-eval-env", "An evaluation environment for scientific research agents"))[0] is True


def test_prefilter_github_negatives():
    # noise repo patterns
    for name, desc in [("user/awesome-agents", "A curated list of agent papers"),
                       ("me/ai-research-agent", "Autonomous research agent that scans arXiv daily"),
                       ("org/agentkit", "A framework for building LLM agents"),
                       ("x/agent-mcp-server", "MCP server exposing agent tools"),
                       ("y/llm-skills-collection", "A collection of agent skills"),
                       ("z/chatbot-template", "Template for building an agent chatbot app")]:
        keep, reason = prefilter.judge(_gh(name, desc))
        assert keep is False, (name, reason)


def test_prefilter_reduces_and_keeps_benchmarks():
    raw = [_arx("MolBench: benchmark for scientific agents"),
           _gh("org/awesome-llm"), _gh("org/foo-benchmark", "Benchmark evaluating research agents"),
           _arx("A survey of transformers")]
    kept, rej = prefilter.run(raw)
    titles = {k["title"] for k in kept}
    assert "MolBench: benchmark for scientific agents" in titles
    assert "org/foo-benchmark" in {k["id"] for k in kept}
    assert len(rej) == 2


# ------------------------------------------------------------ cross-source merge
def _dedup(tmp_path, raw):
    run = tmp_path / "run"
    (run / "phase1").mkdir(parents=True)
    (run / "phase1" / "raw_hits.json").write_text(json.dumps(raw))
    repo = build_mini_repo(str(tmp_path / "repo"), [])
    deduplicate.run(str(run), repo_root=repo)
    return json.loads((run / "phase1" / "candidates.json").read_text())


def test_merge_github_links_arxiv_via_homepage(tmp_path):
    raw = [
        {"source": "arxiv", "id": "2502.01234", "url": "https://arxiv.org/abs/2502.01234",
         "title": "CoolAgentBench", "abstract_or_description": "a benchmark", "authors": ["A. Smith"]},
        {"source": "github", "id": "acme/coolagentbench", "url": "https://github.com/acme/coolagentbench",
         "title": "acme/coolagentbench", "abstract_or_description": "code for the paper",
         "homepage": "https://arxiv.org/abs/2502.01234", "authors": ["acme"], "topics": []},
    ]
    cands = _dedup(tmp_path, raw)
    assert len(cands) == 1
    assert {r["source"] for r in cands[0]["source_records"]} == {"arxiv", "github"}


def test_merge_arxiv_openreview_title_author(tmp_path):
    raw = [
        {"source": "arxiv", "id": "2503.00001", "url": "u1", "title": "Deep Agent Evaluation Suite",
         "abstract_or_description": "x", "authors": ["Jane Roe", "John Poe"]},
        {"source": "openreview", "id": "AbC123", "url": "u2", "title": "Deep Agent Evaluation Suite!",
         "abstract_or_description": "x", "authors": ["Jane Roe"]},
    ]
    cands = _dedup(tmp_path, raw)
    assert len(cands) == 1


def test_no_merge_similar_titles_different_authors(tmp_path):
    # genuinely different works: similar-but-not-identical titles AND no shared author -> no merge
    raw = [
        {"source": "arxiv", "id": "2503.00002", "url": "u1",
         "title": "Agent Benchmark for Physics Reasoning Tasks",
         "abstract_or_description": "x", "authors": ["Alice Anderson"]},
        {"source": "arxiv", "id": "2503.00003", "url": "u2",
         "title": "Agent Benchmark for Chemistry Synthesis Problems",
         "abstract_or_description": "x", "authors": ["Bob Brown"]},
    ]
    cands = _dedup(tmp_path, raw)
    assert len(cands) == 2


# ------------------------------------------------------------ relevance interface (mocked scorer)
def _cands(n, prefix="c"):
    return [{"candidate_id": "%s%d" % (prefix, i), "title": "t%d" % i,
             "abstract_or_description": "", "authors": [], "source_records": [{"source": "arxiv"}],
             "matched_profiles": []} for i in range(n)]


def _mock_worker(decision, conf=0.9):
    def w(agent, kind, prompt, cwd, max_turns, schema=None, model=None):
        cands = json.loads(prompt.split("CANDIDATES:\n", 1)[1])
        return {"ok": True, "structured_output": {"results": [
            {"candidate_id": c["candidate_id"], "decision": decision, "confidence": conf,
             "reason": "mock"} for c in cands]}}
    return w


def test_relevance_decisions(monkeypatch):
    for dec in ("deep_review", "reject_low_relevance", "uncertain"):
        monkeypatch.setattr(relevance, "run_worker", _mock_worker(dec))
        d = relevance.score(_cands(5), batch_size=3, max_workers=2)
        assert all(v["decision"] == dec for v in d.values()) and len(d) == 5


def test_relevance_op_failure_is_uncertain_not_reject(monkeypatch):
    monkeypatch.setattr(relevance, "run_worker",
                        lambda *a, **k: {"ok": False, "error": "boom", "structured_output": None})
    d = relevance.score(_cands(4), batch_size=2, max_workers=2)
    assert all(v["decision"] == "uncertain" and v["source"] == "fail_open" for v in d.values())


def test_relevance_malformed_output_is_uncertain(monkeypatch):
    monkeypatch.setattr(relevance, "run_worker",
                        lambda *a, **k: {"ok": True, "structured_output": None, "result": "not json"})
    d = relevance.score(_cands(3), batch_size=3, max_workers=1)
    assert all(v["decision"] == "uncertain" for v in d.values())


# ------------------------------------------------------------ admission / cap
def test_admit_under_cap():
    cands = _cands(35)
    dec = {c["candidate_id"]: {"decision": "deep_review", "confidence": 0.9} for c in cands}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    assert len(admitted) == 35 and rep["overflow"] is False


def test_admit_overflow_keeps_all_deep_for_needs_attention():
    cands = _cands(45)
    dec = {c["candidate_id"]: {"decision": "deep_review", "confidence": 0.9} for c in cands}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    assert len(admitted) == 45 and rep["overflow"] is True   # Phase 2 cap check will fail -> no PR


def test_admit_uncertain_fills_remaining_budget_by_confidence():
    cands = _cands(50)
    dec = {}
    for i, c in enumerate(cands):
        if i < 30:
            dec[c["candidate_id"]] = {"decision": "deep_review", "confidence": 0.9}
        else:
            dec[c["candidate_id"]] = {"decision": "uncertain", "confidence": (i / 100.0)}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    assert len(admitted) == 40 and rep["uncertain_admitted"] == 10 and rep["overflow"] is False


# ------------------------------------------------------------ watermark
import watermark


def test_watermark_no_wm_uses_default_lookback():
    w = watermark.compute_window("2026-08-10T00:00:00+00:00", None, 24, 14, 3)
    assert w["basis"] == "default_lookback" and w["catch_up_exceeded"] is False
    assert w["start_iso"].startswith("2026-08-07")


def test_watermark_recent_uses_overlap():
    w = watermark.compute_window("2026-08-10T00:00:00+00:00", "2026-08-07T00:00:00+00:00", 24, 14, 3)
    assert w["basis"] == "watermark" and w["catch_up_exceeded"] is False
    assert w["start_iso"].startswith("2026-08-06")   # 2026-08-07 minus 24h overlap


def test_watermark_catch_up_exceeded_needs_attention():
    w = watermark.compute_window("2026-08-30T00:00:00+00:00", "2026-08-01T00:00:00+00:00", 24, 14, 3)
    assert w["catch_up_exceeded"] is True and w["basis"] == "catch_up_exceeded"


def test_is_due():
    assert watermark.is_due("2026-08-10T00:00:00+00:00", None, 72) is True                 # first run
    assert watermark.is_due("2026-08-10T00:00:00+00:00", "2026-08-06T00:00:00+00:00", 72) is True   # 96h
    assert watermark.is_due("2026-08-10T00:00:00+00:00", "2026-08-09T12:00:00+00:00", 72) is False  # 12h


# ------------------------------------------------------------ source-aware admission
def test_admit_excludes_github_only_uncertain():
    cands = [
        {"candidate_id": "p1", "source_records": [{"source": "arxiv"}]},
        {"candidate_id": "g1", "source_records": [{"source": "github"}]},
        {"candidate_id": "pg", "source_records": [{"source": "arxiv"}, {"source": "github"}]},
    ]
    dec = {"p1": {"decision": "uncertain", "confidence": 0.5},
           "g1": {"decision": "uncertain", "confidence": 0.9},   # high conf but github-only -> excluded
           "pg": {"decision": "uncertain", "confidence": 0.4}}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    ids = {c["candidate_id"] for c in admitted}
    assert "g1" not in ids and "p1" in ids and "pg" in ids
    assert rep["uncertain_github_only_excluded"] == 1


# ------------------------------------------------------------ discovery performance/concurrency
def test_arxiv_search_many_consolidates_to_one_or_query(monkeypatch):
    import sources
    captured = {}
    src = sources.ArxivSource()
    monkeypatch.setattr(src, "_fetch", lambda sq, since, limit: captured.setdefault("q", sq) or [])
    recs, reqs = src.search_many(["LLM agent physics", "scientific agent physics"], "2026-01-01", 60)
    assert reqs == 1
    assert captured["q"] == "all:LLM agent physics OR all:scientific agent physics"


def test_openreview_search_many_single_request(monkeypatch):
    import sources
    calls = {"n": 0}
    src = sources.OpenReviewSource()
    monkeypatch.setattr(src, "search", lambda q, since, limit: calls.__setitem__("n", calls["n"] + 1) or [])
    recs, reqs = src.search_many(["a", "b", "c"], "2026-01-01", 40)
    assert reqs == 1 and calls["n"] == 1


def test_sources_run_concurrently(monkeypatch):
    import time as _t
    import discover

    class _Fake:
        def __init__(self, name):
            self.name = name

        def search_many(self, queries, since, limit):
            _t.sleep(0.4)
            return ([{"source": self.name, "id": self.name + "-1", "title": "t",
                      "abstract_or_description": "", "authors": [], "date": ""}], 1)

    monkeypatch.setattr(discover, "all_sources",
                        lambda: {n: _Fake(n) for n in ("arxiv", "openreview", "github")})
    monkeypatch.setattr(discover, "taxonomy", lambda *a, **k: {"domains": {"Physics": "physics"},
                                                               "topics": {}, "activities": {}})
    monkeypatch.setattr(discover, "search_profiles", lambda *a, **k:
                        {"domains": {"Physics": ["q1"]}, "topics": {}, "activities": {}, "global": []})
    monkeypatch.setattr(discover, "_DELAY", {"arxiv": 0, "openreview": 0, "github": 0})
    import tempfile
    rd = tempfile.mkdtemp()
    t0 = _t.monotonic()
    cov = discover.run("full", rd, since_iso="2026-01-01T00:00:00")
    wall = _t.monotonic() - t0
    # three 0.4s sources in parallel finish in < 0.9s (serial would be ~1.2s)
    assert wall < 0.9, wall
    assert set(cov["sources"]) == {"arxiv", "openreview", "github"}
    assert cov["timing"]["discovery_wall_s"] < 0.9


# ------------------------------------------------------------ source status tri-state + gate
import discover
import validators
import pytest


class _StubSrc:
    """Deterministic source stub: raises for any query in fail_on (a transient per-query failure);
    otherwise returns one record. Lets us exercise the success/degraded_success/failure logic."""

    def __init__(self, name="arxiv", fail_on=()):
        self.name = name
        self.fail_on = set(fail_on)

    def search_many(self, queries, since, limit):
        if any(q in self.fail_on for q in queries):
            raise RuntimeError("transient boom")
        return ([{"source": self.name, "id": "%s-%s" % (self.name, queries[0]), "title": "t",
                  "abstract_or_description": "", "authors": [], "date": ""}], 1)


def _run_n(n_items, fail_idx=(), global_fail=False):
    """Run _search_source over n_items single-query domains; fail the item queries at fail_idx
    (and/or the global catch-all). Exercises the bounded degraded-success threshold."""
    items = ["D%d" % i for i in range(n_items)]
    prof = {"domains": {it: ["q%d" % i] for i, it in enumerate(items)}, "topics": {}, "activities": {}}
    fail_on = {"q%d" % i for i in fail_idx}
    if global_fail:
        fail_on.add("glob-q")
    return discover._search_source(
        "arxiv", _StubSrc("arxiv", fail_on), {"domains": items}, ["glob-q"],
        prof, "2026-01-01", 10, 0, None, None, "2026-08-10T00:00:00")


def test_source_status_success_when_all_ok():
    res = _run_n(5)
    assert res["status"] == "success" and res["status_detail"] == ""


def test_source_status_degraded_on_global_only_failure():
    # the exact production case: every per-item query succeeds; only the global catch-all fails
    res = _run_n(20, global_fail=True)
    assert res["status"] == "degraded_success" and "global" in res["status_detail"]


def test_source_status_degraded_on_small_bounded_item_failure():
    # 2 of 20 item queries fail (<=2 AND <=10%) -> degraded_success, with lost coverage recorded
    res = _run_n(20, fail_idx=[0, 1])
    assert res["status"] == "degraded_success"
    assert "2/20" in res["status_detail"] and "lost:" in res["status_detail"]


def test_source_status_failure_when_item_failures_exceed_count_tolerance():
    # 3 of 30 item queries fail: within 10% but > 2 absolute -> failure (bounded count wins)
    res = _run_n(30, fail_idx=[0, 1, 2])
    assert res["status"] == "failure" and "exceeds degraded tolerance" in res["status_detail"]


def test_source_status_failure_when_item_failures_exceed_fraction_tolerance():
    # 2 of 10 item queries fail: within count 2 but 20% > 10% -> failure (bounded fraction wins)
    res = _run_n(10, fail_idx=[0, 1])
    assert res["status"] == "failure"


def test_source_status_failure_when_all_items_fail():
    res = _run_n(3, fail_idx=[0, 1, 2])
    assert res["status"] == "failure" and "all 3" in res["status_detail"]


def _write_cov(tmp_path, sources, axes=None, cands=None):
    run = tmp_path / "run" / "phase1"
    run.mkdir(parents=True)
    cov = {"sources": sources,
           "axes": axes if axes is not None else {"domains": {"Physics": {"status": "success"}}}}
    (run / "coverage.json").write_text(json.dumps(cov))
    (run / "candidates.json").write_text(json.dumps(cands if cands is not None else
        [{"candidate_id": "c1", "title": "t", "source_records": [{"source": "arxiv"}]}]))
    return str(tmp_path / "run")


def test_gate_allows_degraded_success(tmp_path):
    rd = _write_cov(tmp_path, {"arxiv": "degraded_success", "openreview": "success", "github": "success"})
    ok, errs = validators.validate_discovery(rd)
    assert ok, errs


def test_gate_blocks_source_failure(tmp_path):
    rd = _write_cov(tmp_path, {"arxiv": "failure", "openreview": "success", "github": "success"})
    ok, errs = validators.validate_discovery(rd)
    assert not ok and any("arxiv" in e for e in errs)


def test_gate_blocks_axis_coverage_loss_even_if_all_sources_degraded(tmp_path):
    # all sources degraded_success (allowed), BUT a taxonomy item lost all cross-source coverage
    # -> still blocked. This is the guarantee that a degraded source never silently drops an item.
    rd = _write_cov(tmp_path,
                    {"arxiv": "degraded_success", "openreview": "degraded_success",
                     "github": "degraded_success"},
                    axes={"domains": {"Physics": {"status": "success"},
                                      "Chemistry": {"status": "failed"}}})
    ok, errs = validators.validate_discovery(rd)
    assert not ok and any("Chemistry" in e for e in errs)


# ------------------------------------------------------------ OpenReview adapter live smoke (opt-in)
@pytest.mark.skipif(os.environ.get("RUN_LIVE_SMOKE") != "1",
                    reason="live network smoke; set RUN_LIVE_SMOKE=1 to run")
def test_openreview_live_smoke():
    """Bounded live demonstration of the OpenReview adapter's three required properties."""
    import datetime as _dt
    import sources
    src = sources.OpenReviewSource()

    # (1) known matching submissions are returned over a wide validation window
    wide, reqs = src.search_many(["agent benchmark", "LLM evaluation"], "2024-01-01T00:00:00", 40)
    assert reqs == 1
    assert len(wide) > 0, "no records for a broad query over a wide window"

    # (3) source=forum excludes reviews/comments/decision notes -> every record is a titled submission
    assert all(r["title"] for r in wide), "a non-forum (title-less) note leaked through"
    assert all(r["source"] == "openreview" for r in wide)

    # (2) a recent-window query retrieves recent matching submissions when they exist. Uses a 180-day
    # window (bounded-but-non-trivial): submissions arrive in venue bursts, so this proves the
    # relevance-page + client-side cdate-filter path surfaces recent matches, while honoring the filter.
    since = (_dt.datetime.utcnow() - _dt.timedelta(days=180)).replace(microsecond=0).isoformat()
    recent, _ = src.search_many(["agent benchmark", "LLM evaluation", "scientific agent"], since, 60)
    assert len(recent) > 0, "recent-window query returned nothing despite recent matches existing"
    assert all(r["date"][:10] >= since[:10] for r in recent if r["date"]), "cdate filter not honored"
    assert all(r["title"] for r in recent)
