import json
from types import SimpleNamespace
import pytest
from scripts import claude_worker, repo_markdown


def test_sections_preserve_empty_missing_and_subheadings():
    text = '## Overview\n\n### Detail\nBody\n## Activities\n\n## Links\nURL\n'
    assert repo_markdown.section(text, 'Missing') is None
    assert repo_markdown.section(text, 'Activities') is not None
    assert repo_markdown.sections(text)['Overview'] == '### Detail\nBody'
    assert repo_markdown.sections(text)['Activities'] == ''


@pytest.mark.parametrize('payload', [[], {}, {'is_error': True, 'result': 'failure'},
                                      {'subtype': 'error_max_turns', 'result': 'incomplete'}])
def test_zero_exit_code_cannot_hide_worker_failure(monkeypatch, payload):
    monkeypatch.setattr(claude_worker.subprocess, 'run', lambda *a, **kw: SimpleNamespace(
        returncode=0, stdout=json.dumps(payload), stderr='private'))
    result = claude_worker.invoke('prompt', cwd='.', model='model', tools='Read', max_turns=2)
    assert not result['ok']
    assert 'private' not in str(result)


def test_worker_forwards_permissions_schema_and_success(monkeypatch):
    def run(command, **kwargs):
        assert command[command.index('--allowedTools') + 1] == 'Read'
        assert command[command.index('--permission-mode') + 1] == 'dontAsk'
        assert '--json-schema' in command
        assert kwargs['timeout'] == 1800
        return SimpleNamespace(returncode=0, stdout=json.dumps({'result': 'done', 'total_cost_usd': 0.1}), stderr='')
    monkeypatch.setattr(claude_worker.subprocess, 'run', run)
    result = claude_worker.invoke('prompt', cwd='.', model='model', tools='Read', max_turns=2, schema={'type': 'object'})
    assert result['ok'] and result['cost_usd'] == 0.1
