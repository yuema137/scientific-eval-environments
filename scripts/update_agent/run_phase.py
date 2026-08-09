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

CWD = os.path.abspath(".")
sys.path.insert(0, os.path.join(CWD, "scripts", "update_agent"))

from common import config, write_json, read_json, log   # noqa: E402
import discover as discovery                              # noqa: E402
import deduplicate                                        # noqa: E402
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
    cov = discovery.run(a.mode, RUN_DIR)
    pending = _pending_index(cfg["pr"]["rolling_branch"])
    d = deduplicate.run(RUN_DIR, pending, CWD)
    ok, errs = validators.validate_discovery(RUN_DIR)
    n = d["candidates"]
    phase_state.write_phase_result(RUN_DIR, "discovery", "pass" if ok else "fail",
                                   {"sources": cov["sources"], "raw": cov["raw_hit_count"],
                                    "candidates": n, "errors": errs[:20]})
    _gh_output(candidates=n, discovery=("pass" if ok else "fail"))
    _summary("Discovery", ["Sources: %s" % cov["sources"], "Raw hits: %d" % cov["raw_hit_count"],
                           "Deduplicated candidates: %d" % n])
    sys.exit(0 if ok else 1)


def cmd_english(a):
    cfg = config()
    candidates = read_json(os.path.join(RUN_DIR, "phase1", "candidates.json"))
    ok2, r2 = pipeline.phase2(RUN_DIR, CWD, candidates, cfg)
    if not ok2:
        _gh_output(accepted=0, english="fail")
        sys.exit(1)
    accepted = r2["slugs"]
    _summary("Cards", ["Reviewed: %d" % len(candidates), "Accepted: %d" % len(accepted),
                       "Rejected: %d" % len(r2["rejected"])])
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
    _summary("Chinese", ["Translated files: %d" % len(r.get("zh_files", [])),
                         "Parity gate: %s" % ("PASS" if ok else "FAIL")])
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
                     ("review", cmd_review), ("finalize", cmd_finalize)]:
        p = sub.add_parser(name); p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
