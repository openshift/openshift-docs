#!/usr/bin/env python3
"""Compare one OCP category after fetching and rebasing branches on upstream."""

import argparse
from datetime import datetime, timezone
import fcntl
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


COLUMNS = [
    'Branch', 'AsciiDoctor', 'Vale', 'Exploration', 'ConditionalCode', 'AttributeDefinition',
]
COUNTS = COLUMNS[1:]
FINDING = re.compile(r'^.+:\d+:\d+:([\w-]+\.[\w.-]+):')
ASCIIDOCTOR_ERROR = re.compile(r'^asciidoctor:\s+(?:ERROR|FATAL):', re.I)
REPO_ROOT = Path(__file__).resolve().parents[2]


def git(repo, *args):
    result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def count_logs(logs, category):
    """Count findings directly; missing or unexpected output is not a clean check."""
    counts = {field: 0 for field in COUNTS}
    errors = []
    for kind, suffix in (('AsciiDoctor', 'asciidoctor'), ('Vale', 'vale'),
                         ('Exploration', 'exploration')):
        path = logs / f'{category}-{suffix}.log'
        if not path.is_file():
            errors.append(f'Missing {suffix} log')
            continue
        with path.open(encoding='utf-8', errors='replace') as stream:
            for raw in stream:
                line = raw.strip()
                if not line:
                    continue
                if kind == 'AsciiDoctor' and ASCIIDOCTOR_ERROR.match(line):
                    counts[kind] += 1
                    continue
                finding = FINDING.match(line) if kind != 'AsciiDoctor' else None
                if not finding:
                    errors.append(f'{path.name}: {line}')
                    continue
                counts[kind] += 1
                if kind == 'Exploration':
                    for rule in ('ConditionalCode', 'AttributeDefinition'):
                        if finding[1] == 'AsciiDocDITA.' + rule:
                            counts[rule] += 1
    return counts, errors


def checked_out_branches(repo):
    return {line[len('branch refs/heads/'):]
            for line in git(repo, 'worktree', 'list', '--porcelain').splitlines()
            if line.startswith('branch refs/heads/')}


def fetch_upstream(repo, branches):
    busy = checked_out_branches(repo).intersection(branches)
    if busy:
        raise RuntimeError('Cannot rebase branches checked out in a worktree: ' +
                           ', '.join(sorted(busy)) + '. Run from a different branch.')
    print('Fetching matching branches from upstream...', file=sys.stderr, flush=True)
    refspecs = [f'+refs/heads/{branch}:refs/remotes/upstream/{branch}' for branch in branches]
    git(repo, 'fetch', '--atomic', '--no-tags', 'upstream', *refspecs)
    return {branch: git(repo, 'rev-parse', '--verify', '--end-of-options',
                        f'refs/remotes/upstream/{branch}^{{commit}}') for branch in branches}


def abort_rebase(worktree, console):
    for state in ('rebase-merge', 'rebase-apply'):
        path = Path(git(worktree, 'rev-parse', '--git-path', state))
        if not path.is_absolute():
            path = worktree / path
        if path.is_dir():
            result = subprocess.run(['git', '-C', str(worktree), 'rebase', '--abort'],
                                    stdout=console, stderr=subprocess.STDOUT)
            if result.returncode:
                raise RuntimeError(f'Could not abort rebase in {worktree}; worktree retained')
            break


def check_branch(repo, worktree, destination, category, branch, commit, tools,
                 upstream_commit=None):
    destination.mkdir()
    result = {'branch': branch, 'commit': commit, 'category': category,
              'started_utc': datetime.now(timezone.utc).isoformat(), 'errors': []}
    row = {column: '' for column in COLUMNS}
    row.update(Branch=branch, Category=category)
    added = False
    rebased = False
    with (destination / 'run.log').open('w') as console:
        try:
            if upstream_commit is None:
                git(repo, 'worktree', 'add', '--detach', str(worktree), commit)
            else:
                # An attached worktree lets Git update this branch normally and
                # prevents another checkout from using it during the rebase.
                git(repo, 'worktree', 'add', str(worktree), branch)
            added = True
            if upstream_commit is not None:
                result['original_commit'] = git(worktree, 'rev-parse', 'HEAD')
                result['upstream_commit'] = upstream_commit
                result['commit'] = result['original_commit']
                print(f'Rebasing {branch} onto upstream/{branch}...', file=sys.stderr, flush=True)
                update = subprocess.run(
                    ['git', '-C', str(worktree), '-c', 'rebase.updateRefs=false',
                     'rebase', '--no-autostash', upstream_commit],
                    stdout=console, stderr=subprocess.STDOUT,
                )
                if update.returncode:
                    raise RuntimeError(f'Rebase onto upstream/{branch} failed; see run.log')
                rebased = True
                commit = git(worktree, 'rev-parse', 'HEAD')
                result['commit'] = commit
            print(f'Checking {category}: {branch} ({commit[:10]})', file=sys.stderr, flush=True)
            if not (worktree / 'maps' / 'ocp' / f'{category}.adoc').is_file():
                raise RuntimeError(f'Category map is absent on {branch}')
            # Use one checker snapshot even when a branch has no checker of its own.
            for relative, content in tools.items():
                target = worktree / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
            checks = subprocess.run(
                ['bash', str(worktree / 'conversion-prechecks'), f'maps/ocp/{category}.adoc'],
                cwd=worktree, stdout=console, stderr=subprocess.STDOUT,
            )
            result['precheck_exit_code'] = checks.returncode
            logs = worktree / 'logs'
            counts, errors = count_logs(logs, category)
            row.update(counts)
            result['errors'].extend(errors)
            if checks.returncode not in (0, 1):
                result['errors'].append(f'Precheck exited with status {checks.returncode}')
            if checks.returncode and not any(counts.values()) and not result['errors']:
                result['errors'].append('Precheck failed without conversion findings; see run.log')
            # Operational failures cannot be interpreted as zero findings.
            if result['errors']:
                for field in COUNTS:
                    row[field] = ''
                row['Remarks'] = 'Run incomplete: ' + '; '.join(dict.fromkeys(result['errors']))
        except (OSError, RuntimeError, ValueError) as error:
            result['errors'].append(str(error))
            for field in COUNTS:
                row[field] = ''
            row['Remarks'] = 'Run incomplete: ' + str(error)
        finally:
            # Preserve raw logs before removing our worktree.
            try:
                logs = worktree / 'logs'
                if logs.is_dir():
                    shutil.copytree(logs, destination / 'logs', dirs_exist_ok=True)
            finally:
                if added:
                    try:
                        if upstream_commit is not None and not rebased:
                            abort_rebase(worktree, console)
                        git(repo, 'worktree', 'remove', '--force', str(worktree))
                    except RuntimeError as error:
                        result['errors'].append(f'Could not remove temporary worktree {worktree}: {error}')
                        print(result['errors'][-1], file=sys.stderr, flush=True)
    result['finished_utc'] = datetime.now(timezone.utc).isoformat()
    result['counts'] = {field: row[field] for field in COUNTS}
    return row, result


def write_snapshot(output, category, rows):
    markdown_path = output / f'{category}-comparison.md'
    table = [
        '| ' + ' | '.join(COLUMNS) + ' |',
        '|---|' + '---:|' * (len(COLUMNS) - 1),
    ]
    for row in rows:
        table.append('| ' + ' | '.join(
            str(row[column]).replace('|', '\\|') if row[column] != '' else 'N/A'
            for column in COLUMNS
        ) + ' |')
    snapshot = '\n'.join(table) + '\n'
    markdown_path.write_text(snapshot, encoding='utf-8')
    return markdown_path, snapshot


def completed_run(path, category):
    if path.is_symlink() or not path.is_dir():
        return False
    try:
        metadata = json.loads((path / 'run-metadata.json').read_text())
    except (OSError, ValueError):
        return False
    return isinstance(metadata, dict) and metadata.get('category') == category and bool(metadata.get('finished_utc'))


def publish_latest(repo, output_root, output, category):
    registered = [Path(line[len('worktree '):]).resolve()
                  for line in git(repo, 'worktree', 'list', '--porcelain').splitlines()
                  if line.startswith('worktree ')]

    def has_worktree(path):
        resolved = path.resolve()
        return any(tree == resolved or resolved in tree.parents for tree in registered)

    if output.parent != output_root or not completed_run(output, category) or has_worktree(output):
        raise RuntimeError(f'Cannot publish incomplete output or an active worktree: {output}')
    latest = output_root / 'latest'
    backup = None
    if output != latest and (latest.exists() or latest.is_symlink()):
        if not completed_run(latest, category) or has_worktree(latest):
            raise RuntimeError(f'Cannot replace an unrecognized or active latest directory: {latest}')
        backup = output_root / ('.previous-' + output.name)
        latest.rename(backup)
    if output != latest:
        try:
            output.rename(latest)
        except OSError:
            if backup is not None:
                backup.rename(latest)
            raise
    for previous in output_root.iterdir():
        if previous == latest:
            continue
        # Delete only completed output belonging to this category. Preserve
        # unrelated directories, symlinks, unfinished runs, and registered worktrees.
        owned_name = re.fullmatch(r'\d{8}T\d{6}Z-[\w-]+', previous.name)
        owned_name = owned_name or previous.name.startswith(('.previous-', '.running-'))
        if owned_name and completed_run(previous, category) and not has_worktree(previous):
            shutil.rmtree(previous)
    return latest


def main():
    parser = argparse.ArgumentParser(prog='compare-ocp-prechecks', description=__doc__)
    parser.add_argument('category', help='OCP category, for example integrate')
    parser.add_argument('branches', nargs='+',
                        help='Local branches (other Git commit references require --no-rebase-upstream)')
    parser.add_argument('--repo', type=Path, default=REPO_ROOT,
                        help='Repository to check (defaults to the checkout containing this script)')
    parser.add_argument('--output-dir', type=Path,
                        help='Category output directory containing latest/ (defaults to repository logs)')
    rebase = parser.add_mutually_exclusive_group()
    rebase.add_argument('--rebase-upstream', action='store_true', default=True,
                        help='Fetch upstream and rebase each named local branch before checking it (default)')
    rebase.add_argument('--no-rebase-upstream', dest='rebase_upstream', action='store_false',
                        help='Check existing local commit references without fetching or rebasing')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', args.category):
        parser.error('Category must be a map basename such as integrate')
    if len(set(args.branches)) != len(args.branches):
        parser.error('Specify each branch only once')
    repo = args.repo.resolve()
    tools = {
        'conversion-prechecks': (repo / 'conversion-prechecks').read_bytes(),
        'scripts/navmap/conversion-prechecks.sh': (repo / 'scripts/navmap/conversion-prechecks.sh').read_bytes(),
    }
    commits = []
    for branch in args.branches:
        reference = f'refs/heads/{branch}' if args.rebase_upstream else branch
        try:
            commit = git(repo, 'rev-parse', '--verify', '--end-of-options', reference + '^{commit}')
        except RuntimeError:
            if args.rebase_upstream:
                raise RuntimeError(f'Upstream rebasing requires an existing local branch: {branch}. '
                                   'Use --no-rebase-upstream to check other commit references.')
            raise
        commits.append((branch, commit))
    output_root = (args.output_dir or repo / 'logs/category-comparisons' / args.category).resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    # Hold the lock until main returns, so two runs cannot replace the same latest output.
    output_lock = (output_root / '.compare.lock').open('a')
    try:
        fcntl.flock(output_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise RuntimeError(f'A comparison is already running in {output_root}')
    upstream = fetch_upstream(repo, args.branches) if args.rebase_upstream else {}
    started = datetime.now(timezone.utc)
    output = Path(tempfile.mkdtemp(prefix='.running-', dir=output_root))
    worktrees = output / 'worktrees'
    worktrees.mkdir()
    rows = []
    results = []
    manifest = {
        'category': args.category, 'repository': str(repo),
        'started_utc': started.isoformat(), 'results': results,
        'rebase_upstream': args.rebase_upstream,
        'note': ('Fetched upstream and rebased the selected local branches before checking.'
                 if args.rebase_upstream else
                 'References were resolved once before checking. Local refs were not fetched or updated.'),
    }
    print(f'Results directory: {output_root / "latest"}', file=sys.stderr, flush=True)
    for index, (branch, commit) in enumerate(commits):
        label = re.sub(r'[^A-Za-z0-9._-]', '_', branch)
        token = f'{index + 1:02d}-{label}'
        row, result = check_branch(repo, worktrees / token, output / token,
                                   args.category, branch, commit, tools, upstream.get(branch))
        rows.append(row)
        results.append(result)
        (output / 'run-metadata.json').write_text(json.dumps(manifest, indent=2) + '\n')
    rows.sort(key=lambda row: (row['ConditionalCode'] == '', int(row['ConditionalCode'] or 0), row['Branch']))
    markdown_path, snapshot = write_snapshot(output, args.category, rows)
    manifest['finished_utc'] = datetime.now(timezone.utc).isoformat()
    (output / 'run-metadata.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if not any(worktrees.iterdir()):
        worktrees.rmdir()
    output = publish_latest(repo, output_root, output, args.category)
    markdown_path = output / markdown_path.name
    print(snapshot, end='', flush=True)
    print(f'Snapshot: {markdown_path}', file=sys.stderr, flush=True)
    for row in rows:
        if row.get('Remarks'):
            print(f"{row['Branch']}: {row['Remarks']}", file=sys.stderr, flush=True)
    return 1 if any(result['errors'] for result in results) else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, RuntimeError, ValueError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
