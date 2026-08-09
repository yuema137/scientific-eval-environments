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
