#!/usr/bin/env python3
"""One offline repository gate for local development and CI; report every failure."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    'profiles', 'axes', 'cards-all', 'bilingual-all', 'zh-activity-labels',
    'zh-headings', 'matrix-ordering', 'topic-explanations', 'first-appearance',
)


def commands(include_tests=True):
    checks = [(name, [sys.executable, 'scripts/update_agent/validators.py', name]) for name in CHECKS]
    checks += [
        ('counts', [sys.executable, 'scripts/update_counts.py', '--check']),
        ('monthly-reports', [sys.executable, 'scripts/monthly_report.py', 'validate-all']),
    ]
    if include_tests:
        checks.append(('tests', [sys.executable, '-m', 'pytest', 'tests/', '-q']))
    return checks


def validate(include_tests=True):
    failed = []
    for name, command in commands(include_tests):
        print(f'Checking {name}', flush=True)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            failed.append(name)
    print('Repository validation: ' + ('FAIL (' + ', '.join(failed) + ')' if failed else 'PASS'))
    return 1 if failed else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-tests', action='store_true', help='Run all content checks without pytest')
    args = parser.parse_args()
    sys.exit(validate(include_tests=not args.skip_tests))
