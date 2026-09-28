"""Bounded authentication probe with diagnostics that never print worker output."""
import json
import os
import subprocess
import sys
from pathlib import Path


def diagnose(result, stderr=""):
    text = (json.dumps(result) + " " + stderr).lower()
    for category, markers in (
        ("oauth_expired", ("token has expired", "token expired", "oauth token expired", "expired oauth")),
        ("authentication_rejected", ("401", "invalid token", "invalid api key", "authentication_error", "not logged in")),
        ("model_unavailable", ("model_not_found", "does not exist", "invalid model", "not have access to model")),
        ("rate_or_quota_limit", ("429", "rate_limit", "usage limit", "credit balance")),
        ("network_error", ("connection", "timed out", "fetch failed")),
    ):
        if any(marker in text for marker in markers):
            return category
    return "worker_failed"


def main():
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        print("::error::Claude auth smoke: missing_secret")
        return 1
    root = Path(__file__).resolve().parents[2]
    # Read the same model setting as production workers.
    import yaml
    cfg = yaml.safe_load((root / "automation/update_agent/config.yaml").read_text())
    schema = {"type": "object", "properties": {"can_read_constitution": {"type": "boolean"}},
              "required": ["can_read_constitution"]}
    try:
        proc = subprocess.run([
            "claude", "-p", "Read AGENT.md and return can_read_constitution=true in the requested JSON. Do not reproduce its contents.",
            "--output-format", "json", "--permission-mode", "dontAsk", "--allowedTools", "Read",
            "--max-turns", "4", "--model", cfg["claude"]["model"],
            "--json-schema", json.dumps(schema),
        ], cwd=root, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        print("::error::Claude auth smoke: timeout")
        return 1
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError:
        result = {}
    if not isinstance(result, dict):
        result = {}
    ok = (proc.returncode == 0 and not result.get("is_error")
          and (result.get("structured_output") or {}).get("can_read_constitution") is True)
    category = "pass" if ok else diagnose(result, proc.stderr)
    message = "Claude auth smoke: " + category
    print(message if ok else "::error::" + message)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a") as f:
            f.write("### Claude authentication\n- Result: " + category + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
