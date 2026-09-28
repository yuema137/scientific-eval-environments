# Development

[简体中文](zh/DEVELOPMENT.md)

Use Python 3.11 or newer (CI uses 3.11) and Node.js for the website syntax check. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests/ -q
python scripts/update_counts.py --check
python scripts/monthly_report.py validate-all
node --check site/app.js
```

`requirements.txt` pins the direct runtime dependencies; `requirements-dev.txt` adds the test runner. GitHub Actions installs these same files. Update the pins here when upgrading dependencies. Site export itself uses the Python standard library.

Local deterministic tests require no credentials. Live discovery and generation additionally require the Claude Code CLI and the credentials described in [the updater guide](automation/update_agent/README.md). Keep credentials outside the repository.
