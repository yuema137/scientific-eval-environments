"""Common bounded Claude subprocess protocol for updater and monthly workers."""
import json
import subprocess


def invoke(prompt, *, cwd, model, tools, max_turns, system='', schema=None, timeout=1800):
    command = ['claude', '-p', prompt, '--output-format', 'json', '--max-turns', str(max_turns),
               '--permission-mode', 'dontAsk', '--allowedTools', tools, '--model', model]
    if system:
        command += ['--append-system-prompt', system]
    if schema:
        command += ['--json-schema', json.dumps(schema)]

    def failure(reason):
        return {'ok': False, 'error': reason, 'result': '', 'structured_output': None}

    try:
        proc = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return failure('worker timeout')
    if proc.returncode:
        # The CLI still prints its JSON result on most failures (max turns, usage limit, API
        # error); keep its own reason instead of a bare exit code.
        reason = 'claude exit %d' % proc.returncode
        try:
            data = json.loads(proc.stdout)
        except (json.JSONDecodeError, TypeError):
            data = None
        if isinstance(data, dict):
            detail = [str(data[k]) for k in ('subtype', 'api_error_status') if data.get(k)]
            if data.get('is_error') and data.get('result'):
                detail.append(str(data['result'])[:200])
            if detail:
                reason += ' (%s)' % '; '.join(detail)
        return failure(reason)
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return failure('non-JSON worker output')
    if not isinstance(data, dict):
        return failure('worker output is not an object')
    if data.get('is_error') or (data.get('subtype') or '').startswith('error'):
        return failure('Claude reported an error')
    if data.get('result') is None and data.get('structured_output') is None:
        return failure('worker returned no result')
    return {'ok': True, 'result': data.get('result', ''),
            'structured_output': data.get('structured_output'),
            'cost_usd': data.get('total_cost_usd'), 'session_id': data.get('session_id')}
