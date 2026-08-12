"""Production phase entrypoints, one per GitHub Actions job.

Each subcommand operates on the current checkout (repo_root = cwd) and the ./runtime state
directory, which the workflow passes between jobs as artifacts. Ordering and the final gate are
enforced by phase_state; a PR is only possible when the gate says ready_for_pr.
"""
import argparse
import json
import os
import subprocess
import sys
import time

CWD = os.path.abspath(".")
sys.path.insert(0, os.path.join(CWD, "scripts", "update_agent"))

from common import config, write_json, read_json, log   # noqa: E402
import discover as discovery                              # noqa: E402
import watermark                                          # noqa: E402
import prefilter                                          # noqa: E402
import deduplicate                                        # noqa: E402
import relevance                                          # noqa: E402
import inventory                                          # noqa: E402
import pipeline                                           # noqa: E402
import validators                                         # noqa: E402
import phase_state                                        # noqa: E402
import build_pr_body                                      # noqa: E402

RUN_DIR = os.path.join(CWD, "runtime")


def _gh_output(**kv):
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            for k, v in kv.items():
                f.write("%s=%s\n" % (k, v))


def _pending_index(rolling_branch):
    """Build an identity index from the open automated-update branch (if any) so today's run
    cannot re-propose a work already staged in the pending PR."""
    ref = "origin/%s" % rolling_branch
    if subprocess.run(["git", "cat-file", "-e", ref], capture_output=True).returncode != 0:
        return None
    tmp = os.path.join(RUN_DIR, "pending_works")
    os.makedirs(os.path.join(tmp, "works"), exist_ok=True)
    arch = subprocess.run(["git", "archive", ref, "works"], capture_output=True)
    if arch.returncode != 0:
        return None
    subprocess.run(["tar", "-x", "-C", tmp], input=arch.stdout)
    idx = inventory.build_index(tmp)
    p = os.path.join(RUN_DIR, "pending_index.json")
    write_json(p, {k: idx[k] for k in ("arxiv", "openreview", "doi", "github", "title_norm")})
    return p


def cmd_discover(a):
    cfg = config()
    # ---- watermark-driven window + scheduled due-check (production only) ----
    since_override = None
    now_iso = watermark.now_iso()
    if a.mode == "full":
        wm_iso = watermark.read_watermark_iso()
        event = os.environ.get("GITHUB_EVENT_NAME", "workflow_dispatch")
        if event == "schedule" and not watermark.is_due(now_iso, wm_iso,
                                                         cfg["watermark"]["min_interval_hours"]):
            phase_state.write_phase_result(RUN_DIR, "discovery", "pass",
                                           {"skipped": "not due", "watermark": wm_iso})
            _gh_output(candidates=0, discovery="pass", not_due="true")
            _summary("Discovery", ["Scheduled run not due yet (< %dh since last success) — no-op."
                                   % cfg["watermark"]["min_interval_hours"]])
            sys.exit(0)
        win = watermark.compute_window(now_iso, wm_iso, cfg["watermark"]["overlap_hours"],
                                       cfg["watermark"]["max_catchup_days"], cfg["lookback_days"])
        if win["catch_up_exceeded"]:
            phase_state.write_phase_result(RUN_DIR, "discovery", "fail",
                                           {"needs_attention": "catch-up window exceeded",
                                            "backlog_days": win.get("backlog_days"),
                                            "max_catchup_days": cfg["watermark"]["max_catchup_days"]})
            _gh_output(candidates=0, discovery="fail")
            _summary("Discovery", ["needs_attention: %d-day backlog exceeds max_catchup_days=%d — "
                                   "not deep-reviewing a backlog. Investigate."
                                   % (win.get("backlog_days", 0), cfg["watermark"]["max_catchup_days"])])
            sys.exit(1)
        since_override = win["start_iso"]
        log("discovery window %s -> %s (basis=%s)" % (since_override, now_iso, win["basis"]))
    cov = discovery.run(a.mode, RUN_DIR, now_iso=now_iso, since_iso=since_override)
    tm = dict(cov.get("timing", {}))
    # 1) deterministic source-aware prefilter
    _t = time.monotonic()
    raw = read_json(os.path.join(RUN_DIR, "phase1", "raw_hits.json"))
    kept, pre_rej = prefilter.run(raw)
    write_json(os.path.join(RUN_DIR, "phase1", "raw_prefiltered.json"), kept)
    write_json(os.path.join(RUN_DIR, "phase1", "prefilter_rejected.json"), pre_rej)
    tm["prefilter_s"] = round(time.monotonic() - _t, 2)
    # 2) cross-source merge + existing/pending dedup (on the prefiltered set)
    _t = time.monotonic()
    pending = _pending_index(cfg["pr"]["rolling_branch"])
    deduplicate.run(RUN_DIR, pending, CWD,
                    raw_path=os.path.join(RUN_DIR, "phase1", "raw_prefiltered.json"))
    merged = read_json(os.path.join(RUN_DIR, "phase1", "candidates.json"))
    write_json(os.path.join(RUN_DIR, "phase1", "merged_candidates.json"), merged)
    cross_merged = sum(1 for c in merged if len({r["source"] for r in c["source_records"]}) > 1)
    tm["merge_dedup_s"] = round(time.monotonic() - _t, 2)
    # 3) metadata relevance scoring + ranked admission (triage, not truncation)
    _t = time.monotonic()
    cap = cfg["limits"]["max_deep_review_candidates"]
    decisions = relevance.score(merged, cfg)
    admitted, rep = relevance.admit(merged, decisions, cap)
    tm["relevance_s"] = round(time.monotonic() - _t, 2)
    # Budget deferral is a transparent bounded-coverage policy: record every overflow candidate as
    # deferred_by_budget in its own artifact (never a silent drop, never a persistent auto-backlog).
    deferred = rep.pop("deferred_candidates", [])
    write_json(os.path.join(RUN_DIR, "phase1", "deferred_by_budget.json"), deferred)
    write_json(os.path.join(RUN_DIR, "phase1", "relevance.json"),
               {"report": rep, "decisions": decisions, "timing": tm})
    write_json(os.path.join(RUN_DIR, "phase1", "candidates.json"), admitted)  # admitted = deep-review queue
    ok, errs = validators.validate_discovery(RUN_DIR)
    n = len(admitted)
    phase_state.write_phase_result(RUN_DIR, "discovery", "pass" if ok else "fail",
                                   {"sources": cov["sources"], "raw": cov["raw_hit_count"],
                                    "prefiltered": len(kept), "cross_source_merged": cross_merged,
                                    "relevance": rep, "admitted": n, "errors": errs[:20]})
    _gh_output(candidates=n, discovery=("pass" if ok else "fail"))
    rbs = cov.get("raw_by_source", {})
    win = cov.get("search_window", {})
    _summary("Discovery funnel", [
        "Window: %s -> %s" % (win.get("start", "?")[:10], win.get("end", "?")[:10]),
        "Raw: arXiv %d, OpenReview %d, GitHub %d (total %d)"
        % (rbs.get("arxiv", 0), rbs.get("openreview", 0), rbs.get("github", 0), cov["raw_hit_count"]),
        "Deterministic prefilter -> %d" % len(kept),
        "Cross-source merged: %d" % cross_merged,
        "Relevance: deep_review=%d, uncertain=%d (admitted %d, github-only excluded %d), rejected=%d"
        % (rep["deep_review"], rep["uncertain_total"], rep["uncertain_admitted"],
           rep.get("uncertain_github_only_excluded", 0), rep["rejected_low_relevance"]),
        "Sent to Phase 2: %d (budget %d) | deferred_by_budget: %d%s"
        % (n, cap, rep.get("deferred_by_budget", 0),
           " (budget exceeded — top-%d admitted by confidence, rest deferred)" % cap
           if rep.get("budget_exceeded") else ""),
        "Sources: %s" % "  ".join(
            "%s=%s%s" % (s, cov.get("sources", {}).get(s, "?"),
                         (" (%s)" % cov.get("source_status_detail", {}).get(s, ""))
                         if cov.get("sources", {}).get(s) in ("degraded_success", "suspicious_empty")
                         else "")
            for s in ("arxiv", "openreview", "github")),
        "Discovery credible: %s%s" % (
            cov.get("discovery_credible", True),
            "" if cov.get("discovery_credible", True)
            else " — suspicious_empty: %s (watermark will NOT advance)" % ",".join(cov.get("suspicious_empty", []))),
        "",
        "Timing:",
        "  arXiv     %5ss (%s req, %s raw)" % (tm.get("arxiv", {}).get("wall_s", "?"),
            tm.get("arxiv", {}).get("requests", "?"), tm.get("arxiv", {}).get("raw_hits", "?")),
        "  OpenReview%5ss (%s req, %s raw)" % (tm.get("openreview", {}).get("wall_s", "?"),
            tm.get("openreview", {}).get("requests", "?"), tm.get("openreview", {}).get("raw_hits", "?")),
        "  GitHub    %5ss (%s req, %s raw)" % (tm.get("github", {}).get("wall_s", "?"),
            tm.get("github", {}).get("requests", "?"), tm.get("github", {}).get("raw_hits", "?")),
        "  (sources run concurrently -> retrieval wall = %ss)" % tm.get("discovery_wall_s", "?"),
        "  prefilter %ss | merge+dedup %ss | relevance %ss"
        % (tm.get("prefilter_s", "?"), tm.get("merge_dedup_s", "?"), tm.get("relevance_s", "?"))])
    sys.exit(0 if ok else 1)


def cmd_advance_watermark(a):
    """Advance the durable watermark to this run's search-window end (called only on production
    success — a legitimate PR or a successful no-op). Failed runs never reach here."""
    cov = read_json(os.path.join(RUN_DIR, "phase1", "coverage.json")) \
        if os.path.exists(os.path.join(RUN_DIR, "phase1", "coverage.json")) else {}
    # Credibility invariant: the trusted watermark advances ONLY after a discovery run whose mandatory
    # source coverage is credible. An operationally-green run with an unresolved suspicious_empty source
    # must NOT advance the watermark — otherwise a silent source outage would permanently skip the
    # interval it failed to ingest. (Absent key -> treat as credible, for backward compatibility.)
    if not watermark.should_advance(cov):
        print("watermark NOT advanced: discovery not credible (suspicious_empty: %s)"
              % ",".join(cov.get("suspicious_empty", []) or ["?"]))
        return
    ts = (cov.get("search_window") or {}).get("end") or cov.get("started_at") or watermark.now_iso()
    subprocess.run(["bash", os.path.join(CWD, "scripts", "update_agent", "advance_watermark.sh"), ts],
                   check=False)
    print("watermark advance requested for", ts)


def cmd_english(a):
    cfg = config()
    candidates = read_json(os.path.join(RUN_DIR, "phase1", "candidates.json"))
    ok2, r2 = pipeline.phase2(RUN_DIR, CWD, candidates, cfg)
    if not ok2:
        _gh_output(accepted=0, english="fail")
        sys.exit(1)
    accepted = r2["slugs"]
    rate = (100.0 * len(accepted) / len(candidates)) if candidates else 0.0
    _summary("Cards", ["Reviewed: %d" % len(candidates), "Accepted: %d" % len(accepted),
                       "Rejected: %d" % len(r2["rejected"]),
                       "Phase-2 acceptance rate (discovery-precision proxy): %.0f%%" % rate])
    if not accepted:
        # successful no-op
        _gh_output(accepted=0, english="pass")
        sys.exit(0)
    ok3, _ = pipeline.phase3(RUN_DIR, CWD, accepted, cfg)
    _gh_output(accepted=len(accepted), english=("pass" if ok3 else "fail"))
    _summary("English axes", ["Accepted: %d" % len(accepted),
                              "English gate: %s" % ("PASS" if ok3 else "FAIL")])
    sys.exit(0 if ok3 else 1)


def cmd_chinese(a):
    cfg = config()
    ok, r = pipeline.phase4(RUN_DIR, CWD, cfg)
    lines = ["Expected mirror files: %d" % len(r.get("zh_files", [])),
             "Missing: %d" % len(r.get("missing", [])),
             "Parity gate: %s" % ("PASS" if ok else "FAIL")]
    for w in r.get("failed_workers", []):
        lines.append("worker %s: %s (retried=%s) missing=%s"
                     % (w["worker_id"], w["error_category"], w["retried"],
                        ",".join(w["missing_files"][:3]) or "-"))
    _summary("Chinese", lines)
    sys.exit(0 if ok else 1)


def cmd_review(a):
    cfg = config()
    # zh files = current changed zh/*.md in the working tree
    zh = [f for f in pipeline.changed_files(CWD) if f.startswith("zh/") and f.endswith(".md")]
    ok5, r5 = pipeline.phase5(RUN_DIR, CWD, zh, cfg)
    accepted = read_json(os.path.join(RUN_DIR, "phase2", "accepted.json"))
    slugs = [x["card_slug"] for x in accepted]
    okc, ec = validators.validate_cards(CWD, slugs)
    oka, ea = validators.validate_axes(CWD)
    okb, eb = validators.validate_bilingual(CWD, slugs)
    okf = ok5 and okc and oka and okb
    phase_state.write_phase_result(RUN_DIR, "final_validation", "pass" if okf else "fail",
                                   {"cards": ec[:10], "axes": ea[:10], "bilingual": eb[:10]})
    _summary("Chinese review + final validation",
             ["Reviewed: %d" % r5.get("reviewed", 0), "Edited: %d" % r5.get("edited", 0),
              "Final validation: %s" % ("PASS" if okf else "FAIL")])
    sys.exit(0 if okf else 1)


def cmd_finalize(a):
    accepted = read_json(os.path.join(RUN_DIR, "phase2", "accepted.json")) \
        if os.path.exists(os.path.join(RUN_DIR, "phase2", "accepted.json")) else []
    gate = phase_state.run(RUN_DIR, len(accepted), smoke=False)
    body = build_pr_body.build(RUN_DIR)
    open(os.path.join(RUN_DIR, "pr_body.md"), "w").write(body)
    _gh_output(ready_for_pr=str(gate["ready_for_pr"]).lower(),
               run_status=gate["run_status"], accepted=len(accepted))
    print(json.dumps(gate, indent=2))
    _summary("Final gate", ["ready_for_pr: %s" % gate["ready_for_pr"],
                            "run_status: %s" % gate["run_status"]])
    # a no-op / empty run is still a green workflow; only a genuine failure is red
    sys.exit(1 if gate["run_status"] == "fail" else 0)


def _summary(title, lines):
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "### %s\n%s\n" % (title, "\n".join("- %s" % x for x in lines))
    if path:
        with open(path, "a") as f:
            f.write(text)
    log(text)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("discover"); d.add_argument("--mode", default="full"); d.set_defaults(fn=cmd_discover)
    for name, fn in [("english", cmd_english), ("chinese", cmd_chinese),
                     ("review", cmd_review), ("finalize", cmd_finalize),
                     ("advance-watermark", cmd_advance_watermark)]:
        p = sub.add_parser(name); p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
