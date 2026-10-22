"""Real Git fixtures exercise closed/squashed rolling branches and pending work."""
import os
from pathlib import Path
import subprocess

SCRIPT = Path(__file__).resolve().parents[2] / 'scripts/update_agent/base_branch.sh'


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def fixture(tmp_path):
    remote = tmp_path / 'remote.git'
    subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
    root = tmp_path / 'work'
    subprocess.run(['git', 'clone', str(remote), str(root)], check=True, capture_output=True)
    git(root, 'config', 'user.name', 'Fixture')
    git(root, 'config', 'user.email', 'fixture@example.test')
    git(root, 'checkout', '-b', 'main')
    (root / 'content').write_text('initial')
    git(root, 'add', '.'); git(root, 'commit', '-m', 'initial'); git(root, 'push', 'origin', 'main')
    git(root, 'checkout', '-b', 'auto/knowledge-update')
    (root / 'card').write_text('pending')
    git(root, 'add', '.'); git(root, 'commit', '-m', 'batch')
    tip = git(root, 'rev-parse', 'HEAD')
    git(root, 'push', 'origin', 'auto/knowledge-update')
    git(root, 'checkout', 'main')
    (root / 'content').write_text('latest main')
    git(root, 'add', '.'); git(root, 'commit', '-m', 'main update'); git(root, 'push', 'origin', 'main')
    binary = tmp_path / 'bin'; binary.mkdir()
    gh = binary / 'gh'
    gh.write_text('#!/bin/sh\ncase "$*" in\n*"--state open"*) printf "%s" "$TEST_OPEN_PR";;\n*) printf "%s" "$TEST_MERGED_HEAD";;\nesac\n')
    gh.chmod(0o755)
    env = dict(os.environ, PATH=str(binary) + os.pathsep + os.environ['PATH'], TEST_OPEN_PR='', TEST_MERGED_HEAD=tip)
    return root, tip, env


def test_squashed_merged_branch_uses_main_content_and_can_push(tmp_path):
    root, tip, env = fixture(tmp_path)
    # Simulate squash inclusion plus later edits/deletions: main is the canonical content.
    expected_tree = git(root, 'rev-parse', 'origin/main^{tree}')
    subprocess.run(['bash', str(SCRIPT)], cwd=root, env=env, check=True, capture_output=True)
    assert git(root, 'rev-parse', 'HEAD^{tree}') == expected_tree
    subprocess.run(['git', 'merge-base', '--is-ancestor', tip, 'HEAD'], cwd=root, check=True)
    git(root, 'push', 'origin', 'HEAD:auto/knowledge-update')


def test_open_pr_keeps_pending_work_and_updates_main(tmp_path):
    root, tip, env = fixture(tmp_path)
    env['TEST_OPEN_PR'] = '42'
    subprocess.run(['bash', str(SCRIPT)], cwd=root, env=env, check=True, capture_output=True)
    assert (root / 'card').read_text() == 'pending'
    assert (root / 'content').read_text() == 'latest main'


def test_unreviewed_or_closed_branch_is_not_discarded(tmp_path):
    root, tip, env = fixture(tmp_path)
    env['TEST_MERGED_HEAD'] = 'different-tip'
    before = git(root, 'rev-parse', 'HEAD')
    result = subprocess.run(['bash', str(SCRIPT)], cwd=root, env=env, capture_output=True)
    assert result.returncode != 0
    assert git(root, 'rev-parse', 'HEAD') == before


def test_pr_lookup_failure_is_not_treated_as_no_open_pr(tmp_path):
    root, tip, env = fixture(tmp_path)
    gh = tmp_path / 'bin' / 'gh'
    gh.write_text('#!/bin/sh\nexit 1\n')
    before = git(root, 'rev-parse', 'HEAD')
    result = subprocess.run(['bash', str(SCRIPT)], cwd=root, env=env, capture_output=True)
    assert result.returncode != 0
    assert git(root, 'rev-parse', 'HEAD') == before


def test_conflicting_pending_work_stops_instead_of_overwriting(tmp_path):
    root, tip, env = fixture(tmp_path)
    git(root, 'checkout', 'auto/knowledge-update')
    (root / 'content').write_text('conflicting pending edit')
    git(root, 'add', '.'); git(root, 'commit', '-m', 'pending edit'); git(root, 'push', 'origin', 'auto/knowledge-update')
    git(root, 'checkout', 'main')
    env['TEST_OPEN_PR'] = '42'
    result = subprocess.run(['bash', str(SCRIPT)], cwd=root, env=env, capture_output=True)
    assert result.returncode != 0
    assert git(root, 'diff', '--name-only', '--diff-filter=U') == 'content'
