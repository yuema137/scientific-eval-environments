from types import SimpleNamespace
from scripts import validate_repository as gate


def test_failed_content_check_does_not_skip_monthly_or_tests(monkeypatch):
    calls = []
    def run(command, **kwargs):
        calls.append(command)
        return SimpleNamespace(returncode=1 if command[-1] == 'axes' else 0)
    monkeypatch.setattr(gate.subprocess, 'run', run)
    assert gate.validate() == 1
    assert any('scripts/monthly_report.py' in c for c in calls)
    assert any('pytest' in c for c in calls)


def test_content_only_still_checks_monthly_reports(monkeypatch):
    calls = []
    def run(command, **kwargs):
        calls.append(command)
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(gate.subprocess, 'run', run)
    assert gate.validate(include_tests=False) == 0
    assert any('scripts/monthly_report.py' in c for c in calls)
    assert not any('pytest' in c for c in calls)
