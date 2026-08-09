"""Hardened wrapper around headless `claude -p` for automation workers.

Security posture:
  * Bash/code-execution is NEVER in the allowed-tool set (candidate code is never run).
  * The token is read from the CLAUDE_CODE_OAUTH_TOKEN env var only; never logged.
  * The agent system prompt (which carries the untrusted-data / prompt-injection rules) is
    supplied via --append-system-prompt so external source text can only be *data*.
  * Structured JSON output is required; downstream never greps prose.
"""
import json
import os
import subprocess

from common import config, log, AUTOMATION, REPO_ROOT

AGENTS_DIR = os.path.join(AUTOMATION, "agents")

# tool sets per worker kind — Bash is intentionally absent everywhere
TOOLSETS = {
    "card": "Read,Write,Edit,WebFetch,WebSearch",
    "axis": "Read,Write,Edit",
    "translate": "Read,Write,Edit",
    "review": "Read,Write,Edit",
    "audit": "Read",
    "score": "Read",
}


def run_worker(agent, kind, prompt, cwd, max_turns, schema=None, model=None):
    """Invoke a headless Claude worker. Returns dict with keys:
    {ok, result, structured_output, cost_usd, raw}."""
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        return {"ok": False, "error": "CLAUDE_CODE_OAUTH_TOKEN not set", "result": "",
                "structured_output": None}
    cfg = config()
    agent_file = os.path.join(AGENTS_DIR, "%s.md" % agent)
    system = open(agent_file).read() if os.path.exists(agent_file) else ""
    cmd = [
        "claude", "-p", prompt,
        "--output-format", "json",
        "--max-turns", str(max_turns),
        "--permission-mode", "dontAsk",        # deny-by-default: only allowed tools run
        "--allowedTools", TOOLSETS[kind],
        "--model", model or cfg["claude"]["model"],
    ]
    if system:
        cmd += ["--append-system-prompt", system]
    if schema:
        cmd += ["--json-schema", json.dumps(schema)]
    log("  claude worker: agent=%s kind=%s turns<=%d cwd=%s" % (agent, kind, max_turns, cwd))
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=60 * 30)
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": "worker timeout", "result": "", "structured_output": None}
    if proc.returncode != 0:
        # never echo full stderr (could contain context); surface a short tail only
        tail = (proc.stderr or "")[-400:]
        return {"ok": False, "error": "claude exit %d: %s" % (proc.returncode, tail),
                "result": "", "structured_output": None}
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"ok": False, "error": "non-JSON worker output", "result": proc.stdout[-400:],
                "structured_output": None}
    return {
        "ok": True,
        "result": data.get("result", ""),
        "structured_output": data.get("structured_output"),
        "cost_usd": data.get("total_cost_usd"),
        "session_id": data.get("session_id"),
    }


def parallel(tasks, max_workers):
    """tasks: list of callables returning a dict. Bounded concurrency. Returns list."""
    from concurrent.futures import ThreadPoolExecutor
    out = [None] * len(tasks)
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(t): i for i, t in enumerate(tasks)}
        for f in futs:
            i = futs[f]
            try:
                out[i] = f.result()
            except Exception as e:  # noqa: BLE001
                out[i] = {"ok": False, "error": str(e)}
    return out
