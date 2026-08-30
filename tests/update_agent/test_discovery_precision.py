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
    assert prefilter.judge(_arx(
        "Can Generalist Agents Automate Data Curation?",
        "Agents iteratively revise data policies using downstream evaluation feedback."
    ))[0] is True
    assert prefilter.judge(_arx(
        "Hierarchical Action Abstraction for LLM Agents",
        "A high-level planner selects semantic subgoals and an executor carries them out over multiple tool actions."
    ))[0] is True


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


def test_prefilter_closes_eval_sci_without_agent_floodgate():
    # science + benchmark but NO agent and NO LLM -> now rejected (was the EVAL+SCI floodgate)
    assert prefilter.judge(_arx("GraphBench: A Benchmark for Molecular Property Prediction",
                                "We introduce a benchmark evaluating GNN models on chemistry datasets."))[0] is False
    # a scientific LLM benchmark (SCI + LLM, no agent) stays IN scope
    assert prefilter.judge(_arx("SciEval: Benchmarking Large Language Models on Physics Problems",
                                "An evaluation benchmark for LLMs on physics reasoning."))[0] is True
    # closing that path must NOT open an EVAL+LLM floodgate: generic NLP LLM benchmark, no science,
    # no agent -> still rejected
    assert prefilter.judge(_arx("GLUEBench: A Benchmark for Language Model Text Classification",
                                "We benchmark language models on sentiment and entailment."))[0] is False
    # agent benchmark still passes (EVAL+AGENT)
    assert prefilter.judge(_arx("AgentArena: A Benchmark for Evaluating Autonomous Agents"))[0] is True


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


def test_relevance_scorer_routes_to_configured_model(monkeypatch):
    # the metadata scorer must call run_worker with the configured relevance_model (Sonnet), not
    # silently inherit the deep-work model; structured output must still parse.
    captured = {}

    def w(agent, kind, prompt, cwd, max_turns, schema=None, model=None):
        captured["agent"], captured["model"] = agent, model
        cands = json.loads(prompt.split("CANDIDATES:\n", 1)[1])
        return {"ok": True, "structured_output": {"results": [
            {"candidate_id": c["candidate_id"], "decision": "uncertain", "confidence": 0.5} for c in cands]}}

    monkeypatch.setattr(relevance, "run_worker", w)
    import common
    d = relevance.score(_cands(3), cfg=common.config())
    assert captured["agent"] == "relevance-scorer"
    assert captured["model"] == common.config()["claude"]["relevance_model"] == "claude-sonnet-5"
    assert len(d) == 3


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


# ------------------------------------------------------------ admission / budget + deferral
def test_admit_under_budget_processes_all():
    cands = _cands(35)
    dec = {c["candidate_id"]: {"decision": "deep_review", "confidence": 0.9} for c in cands}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    assert len(admitted) == 35 and rep["budget_exceeded"] is False and rep["deferred_by_budget"] == 0


def test_admit_over_budget_selects_exactly_cap_and_defers_rest():
    # 45 deep_review, distinct confidences -> admit the 40 highest, defer the 5 lowest (no silent drop)
    cands = _cands(45)
    dec = {c["candidate_id"]: {"decision": "deep_review", "confidence": i / 100.0}
           for i, c in enumerate(cands)}
    admitted, rep = relevance.admit(cands, dec, cap=40)
    assert len(admitted) == 40
    assert rep["budget_exceeded"] is True and rep["deferred_by_budget"] == 5
    # the 5 deferred are the 5 LOWEST confidence (ids c0..c4), all marked deferred_by_budget
    deferred_ids = {d["candidate_id"] for d in rep["deferred_candidates"]}
    assert deferred_ids == {"c0", "c1", "c2", "c3", "c4"}
    assert all(d["reason"] == "deferred_by_budget" for d in rep["deferred_candidates"])
    # nothing silently disappears: admitted ∪ deferred == all deep_review candidates
    admitted_ids = {c["candidate_id"] for c in admitted}
    assert admitted_ids | deferred_ids == {c["candidate_id"] for c in cands}
    assert not (admitted_ids & deferred_ids)


def test_admit_budget_selection_is_deterministic():
    cands = _cands(45)
    dec = {c["candidate_id"]: {"decision": "deep_review", "confidence": 0.9} for c in cands}  # ties
    a1, r1 = relevance.admit(cands, dec, cap=40)
    a2, r2 = relevance.admit(cands, dec, cap=40)
    assert [c["candidate_id"] for c in a1] == [c["candidate_id"] for c in a2]      # stable tie-break
    assert {d["candidate_id"] for d in r1["deferred_candidates"]} == {d["candidate_id"] for d in r2["deferred_candidates"]}


def test_admit_uncertain_fills_remaining_budget_then_defers():
    cands = _cands(50)
    dec = {}
    for i, c in enumerate(cands):
        dec[c["candidate_id"]] = ({"decision": "deep_review", "confidence": 0.9} if i < 30
                                  else {"decision": "uncertain", "confidence": (i / 100.0)})
    admitted, rep = relevance.admit(cands, dec, cap=40)
    # 30 deep + 10 highest-confidence uncertain = 40; remaining 10 uncertain deferred_by_budget
    assert len(admitted) == 40 and rep["uncertain_admitted"] == 10
    assert rep["budget_exceeded"] is False and rep["deferred_by_budget"] == 10


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

        def harvest(self, frm, until, max_pages=50, delay=0):   # arxiv OAI path
            _t.sleep(0.4)
            return ([{"source": "arxiv", "id": "arxiv-1",
                      "title": "AgentBench: a benchmark for LLM agents",
                      "abstract_or_description": "A benchmark evaluating autonomous LLM agents.",
                      "authors": [], "date": "2026-01-02", "categories": "cs.AI"}], 1, False)

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

    # (2) the client-side date filter (now keyed on odate = first-public) is honored: every record a
    # windowed query returns respects the lower bound. We do NOT assert the window is non-empty — the
    # documented limitation is that /notes/search is relevance-ranked with no server-side date sort, so
    # a short window legitimately returns zero (recent submissions rarely sit in the relevance top-N).
    since = (_dt.datetime.utcnow() - _dt.timedelta(days=180)).replace(microsecond=0).isoformat()
    recent, _ = src.search_many(["agent benchmark", "LLM evaluation", "scientific agent"], since, 60)
    assert all(r["date"][:10] >= since[:10] for r in recent if r["date"]), "odate filter not honored"
    assert all(r["title"] for r in recent)


# ------------------------------------------------------------ suspicious-empty / zero-storm
def _rec(i):
    return {"source": "arxiv", "id": "a%d" % i, "title": "AgentBench: a benchmark for LLM agents",
            "abstract_or_description": "A benchmark evaluating autonomous LLM agents.",
            "authors": ["X"], "date": "2026-08-09", "categories": "cs.AI"}


class _OaiFake:
    """Fake arXiv OAI source: returns self.pages[call] records on each harvest() call (clamped)."""
    name = "arxiv"

    def __init__(self, pages, truncated=False):
        self.calls = 0
        self.pages = pages
        self.truncated = truncated

    def harvest(self, frm, until, max_pages=50, delay=0):
        i = min(self.calls, len(self.pages) - 1)
        self.calls += 1
        return (list(self.pages[i]), 1, self.truncated)


def _discover_arxiv(monkeypatch, tmp_path, src):
    monkeypatch.setattr(discover, "all_sources", lambda: {"arxiv": src})
    monkeypatch.setattr(discover, "taxonomy",
                        lambda *a, **k: {"domains": {"Physics": "physics"}, "topics": {}, "activities": {}})
    monkeypatch.setattr(discover, "search_profiles", lambda *a, **k:
                        {"domains": {"Physics": ["LLM agent physics benchmark"]},
                         "topics": {}, "activities": {}, "global": []})
    monkeypatch.setattr(discover, "_DELAY", {"arxiv": 0})
    return discover.run("full", str(tmp_path / "rt"), since_iso="2026-08-07T00:00:00")


def test_arxiv_oai_zero_storm_unresolved_is_suspicious(tmp_path, monkeypatch):
    # harvest empty on both the initial pass and the bounded canary re-harvest -> not credible
    cov = _discover_arxiv(monkeypatch, tmp_path, _OaiFake(pages=[[]]))
    assert cov["sources"]["arxiv"] == "suspicious_empty"
    assert cov["suspicious_empty"] == ["arxiv"] and cov["discovery_credible"] is False


def test_arxiv_oai_zero_storm_canary_recovers_is_credible(tmp_path, monkeypatch):
    # initial harvest empty -> canary recovers -> credible, records present
    cov = _discover_arxiv(monkeypatch, tmp_path, _OaiFake(pages=[[], [_rec(1)]]))
    assert cov["discovery_credible"] is True and cov["suspicious_empty"] == []
    assert cov["raw_by_source"].get("arxiv", 0) > 0


def test_arxiv_oai_truncated_harvest_is_suspicious(tmp_path, monkeypatch):
    # hit max_pages with records still pending -> coverage incomplete -> not credible
    cov = _discover_arxiv(monkeypatch, tmp_path, _OaiFake(pages=[[_rec(1)]], truncated=True))
    assert cov["sources"]["arxiv"] == "suspicious_empty" and cov["discovery_credible"] is False


def test_arxiv_oai_local_match_keeps_relevant_drops_irrelevant(tmp_path, monkeypatch):
    good = _rec(1)
    bad = {"source": "arxiv", "id": "bad", "title": "A study of galaxy formation",
           "abstract_or_description": "We simulate galaxy mergers.", "authors": [],
           "date": "2026-08-09", "categories": "astro-ph"}
    _discover_arxiv(monkeypatch, tmp_path, _OaiFake(pages=[[good, bad]]))
    ids = {r["id"] for r in json.loads((tmp_path / "rt" / "phase1" / "raw_hits.json").read_text())}
    assert "a1" in ids and "bad" not in ids


def test_arxiv_oai_parses_record_fields(monkeypatch):
    import sources
    xml = ('<?xml version="1.0"?>'
           '<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"><ListRecords><record>'
           '<header><identifier>oai:arXiv.org:2508.01234</identifier><datestamp>2026-08-10</datestamp></header>'
           '<metadata><arXiv xmlns="http://arxiv.org/OAI/arXiv/">'
           '<id>2508.01234</id><created>2026-08-07</created><updated>2026-08-09</updated>'
           '<authors><author><keyname>Doe</keyname><forenames>Jane</forenames></author></authors>'
           '<title>AgentBench Sci</title><categories>cs.AI cs.LG</categories>'
           '<abstract>A benchmark for scientific agents.</abstract>'
           '</arXiv></metadata></record></ListRecords></OAI-PMH>')

    class _R:
        text = xml

    monkeypatch.setattr(sources, "http_get", lambda *a, **k: _R())
    recs, reqs, trunc = sources.ArxivOAISource().harvest("2026-08-07", "2026-08-10", max_pages=1, delay=0)
    assert reqs == 1 and trunc is False and len(recs) == 1
    r = recs[0]
    assert r["id"] == "2508.01234" and r["date"] == "2026-08-07"      # date = created (submission)
    assert r["datestamp"] == "2026-08-10" and r["updated"] == "2026-08-09"
    assert r["title"] == "AgentBench Sci" and r["authors"] == ["Jane Doe"]
    assert r["abstract_or_description"].startswith("A benchmark") and r["source"] == "arxiv"


@pytest.mark.skipif(os.environ.get("RUN_LIVE_SMOKE") != "1",
                    reason="live network smoke; set RUN_LIVE_SMOKE=1 to run")
def test_arxiv_oai_live_smoke():
    import datetime as _dt
    import sources
    day = (_dt.datetime.utcnow() - _dt.timedelta(days=1)).date().isoformat()
    recs, reqs, trunc = sources.ArxivOAISource().harvest(day, day, max_pages=1, delay=0)
    assert reqs == 1 and len(recs) > 0
    r = recs[0]
    assert r["id"] and r["title"] and r["date"]      # created (submission date) present


def test_watermark_should_advance_requires_credible_discovery():
    assert watermark.should_advance({"discovery_credible": True}) is True
    assert watermark.should_advance({"discovery_credible": False}) is False
    assert watermark.should_advance({}) is True          # backward-compatible (flag absent)


def test_watermark_advances_despite_budget_deferral_but_not_on_incredible():
    # a credible run may advance even when candidates were intentionally deferred by the budget policy
    assert watermark.should_advance({"discovery_credible": True, "suspicious_empty": []}) is True
    # a source-credibility failure still blocks advancement regardless of deferral
    assert watermark.should_advance({"discovery_credible": False, "suspicious_empty": ["arxiv"]}) is False


def test_validate_discovery_accepts_suspicious_empty(tmp_path):
    # a suspicious_empty source does NOT fail discovery (run proceeds green); the watermark gate holds
    run = tmp_path / "run" / "phase1"
    run.mkdir(parents=True)
    (run / "coverage.json").write_text(json.dumps(
        {"sources": {"arxiv": "suspicious_empty", "openreview": "success", "github": "success"},
         "axes": {"domains": {"Physics": {"status": "success"}}}}))
    (run / "candidates.json").write_text(json.dumps([]))
    ok, errs = validators.validate_discovery(str(tmp_path / "run"))
    assert ok, errs


def test_openreview_prefers_odate_over_cdate(monkeypatch):
    import datetime as _dt
    import sources
    odate_ms = int(_dt.datetime(2026, 6, 1).timestamp() * 1000)   # first public: 2026
    cdate_ms = int(_dt.datetime(2025, 1, 1).timestamp() * 1000)   # private creation: 2025

    class _Resp:
        def json(self):
            return {"notes": [{"id": "x", "cdate": cdate_ms, "odate": odate_ms,
                    "content": {"title": {"value": "T"}, "abstract": {"value": "a"},
                                "authors": {"value": ["A"]}}}]}

    monkeypatch.setattr(sources, "http_get", lambda *a, **k: _Resp())
    recs = sources.OpenReviewSource().search("q", "2000-01-01T00:00:00", 10)
    assert recs and recs[0]["date"].startswith("2026"), recs[0]["date"]


# ---------------------------------------------------------------- HuggingFace daily-papers source

def _hf_payload(pid="2608.13331", title="Training AI Scientists to Replicate Research",
                published="2026-08-13T00:00:00.000Z"):
    return [{"title": title, "publishedAt": published,
             "paper": {"id": pid, "title": title, "summary": "A replication task space.",
                       "publishedAt": published, "upvotes": 42,
                       "authors": [{"name": "Damon Falck"}, {"name": "Anya Sims"}],
                       "projectPage": "https://example.org/replica"}}]


def test_huggingface_is_a_registered_source():
    import sources
    assert "huggingface" in sources.all_sources()


def test_huggingface_maps_paper_fields(monkeypatch):
    import sources

    class _Resp:
        def json(self):
            return _hf_payload()

    monkeypatch.setattr(sources, "http_get", lambda *a, **k: _Resp())
    recs = sources.HuggingFaceSource().search("agent benchmark", "2000-01-01T00:00:00", 10)
    assert len(recs) == 1
    r = recs[0]
    assert r["source"] == "huggingface"
    assert r["id"] == "2608.13331"                      # HF id IS the arXiv id
    assert r["url"] == "https://arxiv.org/abs/2608.13331"
    assert r["title"] == "Training AI Scientists to Replicate Research"
    assert r["abstract_or_description"].startswith("A replication")
    assert r["authors"] == ["Damon Falck", "Anya Sims"]
    assert r["date"].startswith("2026-08-13") and r["upvotes"] == 42


def test_huggingface_term_search_filters_by_date(monkeypatch):
    # ?q= has no server-side window, so stale hits must be dropped client-side.
    import sources

    class _Resp:
        def json(self):
            return _hf_payload(pid="2401.00001", published="2024-01-05T00:00:00.000Z")

    monkeypatch.setattr(sources, "http_get", lambda *a, **k: _Resp())
    assert sources.HuggingFaceSource().search("q", "2026-08-01T00:00:00", 10) == []


def test_huggingface_daily_feed_keeps_late_promoted_papers(monkeypatch):
    # A paper published before the window but promoted to the daily feed inside it must SURVIVE:
    # surfacing exactly these is why the curated feed is worth harvesting alongside arXiv.
    import sources
    calls = []

    class _Resp:
        def json(self):
            return _hf_payload(pid="2607.09999", published="2026-07-31T00:00:00.000Z")

    def _get(url, params=None, **k):
        calls.append(params or {})
        return _Resp()

    monkeypatch.setattr(sources, "http_get", _get)
    src = sources.HuggingFaceSource()
    recs, _ = src._daily_window("2026-08-14T00:00:00")
    assert [r["id"] for r in recs] == ["2607.09999"]
    assert all("date" in c for c in calls)             # daily mode, not term mode


def test_huggingface_daily_window_is_memoized(monkeypatch):
    # discovery calls search_many once per taxonomy item; without memoization the same day
    # requests would be re-issued dozens of times per run.
    import sources
    n = {"c": 0}

    class _Resp:
        def json(self):
            return _hf_payload()

    def _get(url, params=None, **k):
        n["c"] += 1
        return _Resp()

    monkeypatch.setattr(sources, "http_get", _get)
    src = sources.HuggingFaceSource()
    src.search_many(["a"], "2026-08-16T00:00:00", 10)
    first = n["c"]
    src.search_many(["b"], "2026-08-16T00:00:00", 10)
    assert n["c"] == first + 1, "second call must issue only the term search"


def test_huggingface_tolerates_empty_and_failing_days(monkeypatch):
    # Weekends return HTTP 200 with []; a single unreachable day must not sink the source.
    import sources

    class _Empty:
        def json(self):
            return []

    def _get(url, params=None, **k):
        if (params or {}).get("date", "").endswith("1"):
            raise RuntimeError("transient")
        return _Empty()

    monkeypatch.setattr(sources, "http_get", _get)
    recs, _ = sources.HuggingFaceSource()._daily_window("2026-08-14T00:00:00")
    assert recs == []


def test_merge_huggingface_arxiv_same_paper(tmp_path):
    # The same work reaching us from both sources must collapse to ONE candidate.
    raw = [
        {"source": "arxiv", "id": "2608.13331", "url": "https://arxiv.org/abs/2608.13331",
         "title": "Training AI Scientists to Replicate Research",
         "abstract_or_description": "x", "authors": ["Damon Falck"]},
        {"source": "huggingface", "id": "2608.13331", "url": "https://arxiv.org/abs/2608.13331",
         "title": "Training AI Scientists to Replicate Research",
         "abstract_or_description": "x", "authors": ["Damon Falck"]},
    ]
    cands = _dedup(tmp_path, raw)
    assert len(cands) == 1
    assert {r["source"] for r in cands[0]["source_records"]} == {"arxiv", "huggingface"}
    # arXiv stays the primary record (canonical metadata), HF is the corroborating one
    assert cands[0]["source_records"][0]["source"] == "arxiv"


def test_prefilter_treats_huggingface_as_a_paper_source():
    # Must NOT fall through to "unknown source kept": the daily feed is all of ML, and passing it
    # through unfiltered would crowd out the deep-review cap.
    keep, reason = prefilter.judge({
        "source": "huggingface", "id": "2608.00001",
        "title": "A Benchmark for Evaluating Scientific Agents on Chemistry Tasks",
        "abstract_or_description": "We introduce a benchmark that evaluates LLM agents on "
                                   "chemistry experiment tasks with an automated verifier."})
    assert keep and reason != "unknown source kept"

    drop, _ = prefilter.judge({
        "source": "huggingface", "id": "2608.00002",
        "title": "Fast Text-to-Image Diffusion with Latent Consistency",
        "abstract_or_description": "We propose a distillation method for faster image generation."})
    assert not drop


# ---------------------------------------------------------------- placeholder false positives

def test_placeholder_does_not_match_inside_ordinary_words():
    # REGRESSION: `FILL[_ ]?ME` was case-insensitive with no word boundaries, so it matched
    # "fillme" inside "Task Fu-fillme-nt". On 2026-08-19 that failed a production run which had
    # produced 24 valid cards with zero worker failures, because one card named an evaluation
    # dimension "Task Fulfillment".
    import validators
    for prose in ("Process-level evaluation along Task Fulfillment (TF), Calculator Selection (CS)",
                  "fulfilment of the specification",
                  "a self-fulfilling prophecy",
                  "the preprint lists the venue as TBD"):
        assert not validators._has_placeholder(prose), prose


def test_placeholder_still_catches_real_template_residue():
    import validators
    for residue in ("TODO(card)", "FIXME: rewrite this", "FILL_ME", "FILLME",
                    "lorem ipsum dolor", "<placeholder>", "{{ TITLE }}", "**Venue:** TBD"):
        assert validators._has_placeholder(residue), residue


# ---------------------------------------------------------------- slug collision safety

def _cand(cid, title, url):
    return {"candidate_id": cid, "title": title,
            "source_records": [{"source": "arxiv", "url": url}]}


def test_new_card_never_overwrites_an_existing_slug(tmp_path):
    # REGRESSION: on 2026-08-20 a new work titled "Vero" (2608.13522) was written straight over the
    # existing "VeRO / VeRO-Bench" card (2602.22480), destroying it. Different works, same slug.
    import pipeline
    works = tmp_path / "works"
    works.mkdir()
    (works / "vero.md").write_text("# VeRO / VeRO-Bench (2026)\n")
    taken = {p.stem for p in works.glob("*.md")}
    slug = pipeline._unique_card_slug(_cand("c1", "Vero", "https://arxiv.org/abs/2608.13522"), taken)
    assert slug != "vero"
    assert slug == "vero-2608-13522"       # stable, identifier-derived, not a bare counter


def test_two_new_candidates_with_the_same_stem_do_not_collide():
    import pipeline
    taken = set()
    a = pipeline._unique_card_slug(_cand("a", "Atlas: a benchmark", "https://arxiv.org/abs/2601.00001"), taken)
    b = pipeline._unique_card_slug(_cand("b", "Atlas", "https://arxiv.org/abs/2602.00002"), taken)
    assert a == "atlas"
    assert b == "atlas-2602-00002"
    assert a != b


def test_unique_slug_falls_back_when_no_arxiv_id_is_available():
    import pipeline
    taken = {"toolbench"}
    c = {"candidate_id": "x", "title": "ToolBench",
         "source_records": [{"source": "github", "url": "https://github.com/acme/toolbench"}]}
    assert pipeline._unique_card_slug(c, taken) == "toolbench-2"
