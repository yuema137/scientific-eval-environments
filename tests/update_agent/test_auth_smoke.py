import json
from types import SimpleNamespace
import auth_smoke


def test_failed_json_classifies_expired_token_without_printing_it(monkeypatch, capsys):
    monkeypatch.setenv('CLAUDE_CODE_OAUTH_TOKEN', 'secret-value')
    monkeypatch.setattr(auth_smoke.subprocess, 'run', lambda *a, **kw: SimpleNamespace(
        returncode=1, stdout=json.dumps({'is_error': True, 'result': 'OAuth token has expired secret-value'}), stderr=''))
    assert auth_smoke.main() == 1
    output = capsys.readouterr().out
    assert 'oauth_expired' in output
    assert 'secret-value' not in output


def test_valid_auth_probe(monkeypatch):
    monkeypatch.setenv('CLAUDE_CODE_OAUTH_TOKEN', 'secret-value')
    monkeypatch.setattr(auth_smoke.subprocess, 'run', lambda *a, **kw: SimpleNamespace(
        returncode=0, stdout=json.dumps({'structured_output': {'can_read_constitution': True}}), stderr=''))
    assert auth_smoke.main() == 0


def test_success_exit_with_api_error_is_rejected(monkeypatch):
    monkeypatch.setenv('CLAUDE_CODE_OAUTH_TOKEN', 'secret-value')
    monkeypatch.setattr(auth_smoke.subprocess, 'run', lambda *a, **kw: SimpleNamespace(
        returncode=0, stdout=json.dumps({'is_error': True, 'result': '401 authentication_error'}), stderr=''))
    assert auth_smoke.main() == 1


def test_organization_policy_failure_is_distinct_from_expired_token():
    result = {'result': 'Your organization has disabled Claude subscription access for Claude Code'}
    assert auth_smoke.diagnose(result) == 'organization_subscription_disabled'
