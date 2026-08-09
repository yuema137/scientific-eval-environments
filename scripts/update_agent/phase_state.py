"""Machine-readable phase state and the deterministic FINAL GATE.

A PR may be created only when compute_gate(...)['ready_for_pr'] is True. That is impossible
unless every required phase is 'pass' AND at least one card was accepted. An empty discovery
is a SUCCESSFUL no-op (run ok, no PR). Any failed phase blocks the PR.
"""
import argparse
import os

from common import write_json, read_json

# ordered; a later phase must never pass if an earlier one did not
REQUIRED_PHASES = ["discovery", "cards", "english_axes", "chinese_mirror",
                   "chinese_review", "final_validation"]


def write_phase_result(run_dir, phase, status, summary=None):
    assert status in ("pass", "fail", "skipped"), status
    obj = {"phase": phase, "status": status, "summary": summary or {}}
    write_json("%s/state/%s.json" % (run_dir, phase), obj)
    return obj


def load_states(run_dir):
    states = {}
    for p in REQUIRED_PHASES:
        fp = "%s/state/%s.json" % (run_dir, p)
        states[p] = read_json(fp)["status"] if os.path.exists(fp) else "missing"
    return states


def compute_gate(states, accepted_count):
    """Pure gate logic. states: {phase: 'pass'|'fail'|'skipped'|'missing'}."""
    gate = {p: states.get(p, "missing") for p in REQUIRED_PHASES}
    any_fail = any(states.get(p) == "fail" for p in REQUIRED_PHASES)
    empty_run = states.get("discovery") == "pass" and accepted_count == 0
    all_pass = all(states.get(p) == "pass" for p in REQUIRED_PHASES)
    ready = all_pass and accepted_count > 0 and not any_fail
    if any_fail:
        run_status = "fail"
    elif empty_run:
        run_status = "success"   # successful no-op
    elif all_pass:
        run_status = "success"
    else:
        run_status = "incomplete"
    gate.update({
        "accepted_count": accepted_count,
        "empty_run": empty_run,
        "ready_for_pr": bool(ready),
        "run_status": run_status,
    })
    return gate


def run(run_dir, accepted_count, smoke=False):
    states = load_states(run_dir)
    gate = compute_gate(states, accepted_count)
    gate["pr_creation_disabled_by_smoke_mode"] = bool(smoke)
    gate["would_open_pr"] = bool(gate["ready_for_pr"])
    if smoke:
        gate["ready_for_pr"] = False  # smoke never opens a PR
    write_json("%s/state/final_gate.json" % run_dir, gate)
    return gate


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--accepted", type=int, required=True)
    ap.add_argument("--smoke", action="store_true")
    a = ap.parse_args()
    g = run(a.run_dir, a.accepted, a.smoke)
    import json
    print(json.dumps(g, indent=2))
    # exit nonzero only on genuine failure, so a no-op run is still a green workflow
    raise SystemExit(1 if g["run_status"] == "fail" else 0)
