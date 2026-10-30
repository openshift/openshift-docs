"""Exercise branch comparisons with real Git worktrees and offline tool doubles."""

import fcntl
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / 'scripts/navmap/compare-ocp-prechecks.py'
FAKE_TOOL = r'''
import json
from pathlib import Path
import sys

tool = Path(sys.argv[0]).name
args = sys.argv[1:]
data = json.loads(Path('modules/topic.adoc').read_text())
scenario = data.get('scenario', '')

def finding(rule):
    return ('modules/topic.adoc:1:1:AsciiDocDITA.' + rule +
            ':mentions AsciiDocDITA.ConditionalCode: and AsciiDocDITA.AttributeDefinition:')

if tool == 'asciidoctor':
    if scenario == 'renderer-failure':
        print('renderer execution failed', file=sys.stderr)
        sys.exit(2)
    for _ in range(data.get('asciidoctor', 0)):
        print('asciidoctor: ERROR: modules/topic.adoc: line 1: incomplete table')
elif tool == 'list-content':
    if scenario != 'empty-content':
        print('modules/topic.adoc')
elif 'sync' in args:
    if scenario == 'sync-failure':
        print('style synchronization failed', file=sys.stderr)
        sys.exit(2)
else:
    if scenario == 'vale-failure':
        sys.exit(2)
    if scenario == 'unrecognized-output':
        print('unexpected output without a finding location')
    elif '--filter' in args:
        for key, rule in (('conditional', 'ConditionalCode'),
                          ('attributes', 'AttributeDefinition'),
                          ('includes', 'IncludeDirective')):
            for _ in range(data.get(key, 0)):
                print(finding(rule))
    else:
        for _ in range(data.get('vale', 0)):
            print(finding('TaskInclude'))
'''


class ComparePrechecksTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='compare prechecks ')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / 'docs'
        self.repo.mkdir()
        self.env = dict(
            os.environ, HOME=str(self.base / 'empty-home'),
            DITA_CONFIG=str(self.base / 'dita.ini'),
            GIT_AUTHOR_NAME='Fixture', GIT_AUTHOR_EMAIL='fixture@example.invalid',
            GIT_COMMITTER_NAME='Fixture', GIT_COMMITTER_EMAIL='fixture@example.invalid',
            PYTHONDONTWRITEBYTECODE='1',
        )
        (self.base / 'dita.ini').write_text('')
        tools = self.base / 'tools'
        tools.mkdir()
        for tool in ('asciidoctor', 'list-content', 'vale'):
            executable = tools / tool
            executable.write_text(f'#!{sys.executable}\n' + FAKE_TOOL)
            executable.chmod(0o755)
        self.env['PATH'] = str(tools) + os.pathsep + os.environ['PATH']
        self.git('init', '--quiet')
        # Build fixture commits directly, without invoking global commit hooks.
        empty_tree = self.git('mktree', input='')
        commit = self.git('commit-tree', empty_tree, '-m', 'Launcher')
        self.git('update-ref', 'refs/heads/launcher', commit)
        self.git('symbolic-ref', 'HEAD', 'refs/heads/launcher')
        for relative in (
            '.gitignore', 'compare-ocp-prechecks', 'conversion-prechecks',
            'scripts/navmap/compare-ocp-prechecks.py',
            'scripts/navmap/conversion-prechecks.sh',
        ):
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        self.module = runpy.run_path(str(SCRIPT))

    def git(self, *args, input=None):
        result = subprocess.run(
            ['git', '-C', str(self.repo), *args], input=input,
            env=self.env, capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def branch(self, name, data=None, category='integrate', parent=None):
        if data is None:
            tree = self.git('mktree', input='')
        else:
            if parent is not None:
                self.git('read-tree', parent)
            for relative in (f'maps/ocp/{category}.adoc', 'modules/topic.adoc'):
                path = self.repo / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(data))
            self.git('add', '--', 'maps', 'modules')
            tree = self.git('write-tree')
        parents = ['-p', parent] if parent is not None else []
        commit = self.git('commit-tree', tree, *parents, '-m', name)
        self.git('update-ref', 'refs/heads/' + name, commit)
        return commit

    def upstream(self, branches):
        remote = self.base / 'upstream.git'
        self.git('clone', '--bare', '--quiet', str(self.repo), str(remote))
        self.git('remote', 'add', 'upstream', str(remote))
        for branch, commit in branches.items():
            self.git('--git-dir', str(remote), 'update-ref', 'refs/heads/' + branch, commit)
        return remote

    def compare(self, *branches, category='integrate', extra=()):
        return subprocess.run(
            [str(self.repo / 'compare-ocp-prechecks'), category, *branches, *extra],
            cwd=self.base, env=self.env, capture_output=True, text=True, timeout=30,
        )

    def output(self, category='integrate'):
        return self.repo / 'logs/category-comparisons' / category

    def results(self, category='integrate'):
        return json.loads((self.output(category) / 'latest/run-metadata.json').read_text())['results']

    def assert_no_temporary_worktrees(self):
        worktrees = self.git('worktree', 'list', '--porcelain')
        self.assertEqual(worktrees.count('worktree '), 1, worktrees)
        self.assertFalse(list(self.repo.glob('logs/category-comparisons/*/.running-*')))

    def test_committed_branches_use_shared_checker_and_print_six_columns(self):
        commits = {
            'release/a': self.branch('release/a', {'vale': 2, 'includes': 3}),
            'release-b': self.branch('release-b', {'asciidoctor': 1, 'conditional': 2, 'attributes': 1}),
            'release-clean': self.branch('release-clean', {}),
        }
        # Uncommitted content in the launch checkout must not affect the comparison.
        (self.repo / 'modules/topic.adoc').write_text(json.dumps({'vale': 999}))
        status = self.git('status', '--porcelain')
        result = self.compare(*commits, extra=('--no-rebase-upstream',))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.splitlines(), [
            '| Branch | AsciiDoctor | Vale | Exploration | ConditionalCode | AttributeDefinition |',
            '|---|---:|---:|---:|---:|---:|',
            '| release-clean | 0 | 0 | 0 | 0 | 0 |',
            '| release/a | 0 | 2 | 3 | 0 | 0 |',
            '| release-b | 1 | 0 | 3 | 2 | 1 |',
        ])
        latest = self.output() / 'latest'
        self.assertEqual((latest / 'integrate-comparison.md').read_text(), result.stdout)
        self.assertEqual(self.git('symbolic-ref', 'HEAD'), 'refs/heads/launcher')
        self.assertEqual(self.git('status', '--porcelain'), status)
        self.assertFalse(list(latest.rglob('*.csv')))
        self.assertFalse(list(latest.rglob('*DITA-Conversion*')))
        self.assertEqual(len(list(latest.glob('*/logs/integrate-vale.log'))), 3)
        for item in self.results():
            self.assertEqual(item['commit'], commits[item['branch']])
            self.assertEqual(item['errors'], [])
        self.assert_no_temporary_worktrees()

    def test_repeated_run_replaces_latest_snapshot_and_logs(self):
        self.branch('release', {'vale': 1})
        self.assertEqual(self.compare('release', extra=('--no-rebase-upstream',)).returncode, 0)
        new_commit = self.branch('release', {'vale': 3})
        result = self.compare('release', extra=('--no-rebase-upstream',))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('| release | 0 | 3 | 0 | 0 | 0 |', result.stdout)
        self.assertEqual([p.name for p in self.output().iterdir() if p.is_dir()], ['latest'])
        log = self.output() / 'latest/01-release/logs/integrate-vale.log'
        self.assertEqual(len(log.read_text().splitlines()), 3)
        self.assertEqual(self.results()[0]['commit'], new_commit)
        self.assert_no_temporary_worktrees()

    def test_tool_failures_are_na_and_do_not_stop_other_branches(self):
        for scenario in ('vale-failure', 'renderer-failure', 'empty-content',
                         'sync-failure', 'unrecognized-output'):
            with self.subTest(scenario=scenario):
                self.branch('failed', {'scenario': scenario})
                self.branch('clean', {})
                result = self.compare('failed', 'clean', extra=('--no-rebase-upstream',))
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn('| failed | N/A | N/A | N/A | N/A | N/A |', result.stdout)
                self.assertIn('| clean | 0 | 0 | 0 | 0 | 0 |', result.stdout)
                self.assertIn('Run incomplete:', result.stderr)
                self.assertTrue(self.results()[0]['errors'])
                self.assert_no_temporary_worktrees()

    def test_missing_category_is_not_zero_findings(self):
        self.branch('missing')
        self.branch('clean', {})
        result = self.compare('missing', 'clean', extra=('--no-rebase-upstream',))
        self.assertEqual(result.returncode, 1)
        self.assertIn('| missing | N/A | N/A | N/A | N/A | N/A |', result.stdout)
        self.assertIn('Category map is absent', result.stderr)
        self.assert_no_temporary_worktrees()

    def test_invalid_reference_preserves_previous_latest(self):
        self.branch('release', {})
        self.assertEqual(self.compare('release', extra=('--no-rebase-upstream',)).returncode, 0)
        report = self.output() / 'latest/integrate-comparison.md'
        previous = report.read_bytes()
        self.assertEqual(self.compare('no-such-branch', extra=('--no-rebase-upstream',)).returncode, 1)
        self.assertEqual(report.read_bytes(), previous)
        self.assert_no_temporary_worktrees()

    def test_what_s_new_and_custom_output_directory(self):
        self.branch('release', {'attributes': 1}, category='what-s-new')
        output = self.base / 'custom output'
        result = self.compare('release', category='what-s-new',
                              extra=('--no-rebase-upstream', '--output-dir', str(output)))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((output / 'latest/what-s-new-comparison.md').exists())
        self.assertIn('| release | 0 | 0 | 1 | 0 | 1 |', result.stdout)

    def test_concurrent_run_is_rejected(self):
        self.branch('release', {})
        self.output().mkdir(parents=True)
        with (self.output() / '.compare.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            result = self.compare('release')
        self.assertEqual(result.returncode, 1)
        self.assertIn('already running', result.stderr)
        self.assertFalse((self.output() / 'latest').exists())

    def test_default_fetches_upstream_and_checks_updated_branch(self):
        original = self.branch('release', {'vale': 1})
        updated = self.branch('upstream-seed', {'vale': 4}, parent=original)
        self.upstream({'release': updated})
        status = self.git('status', '--porcelain')
        result = self.compare('release')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('| release | 0 | 4 | 0 | 0 | 0 |', result.stdout)
        self.assertEqual(self.git('rev-parse', 'release'), updated)
        self.assertEqual(self.git('rev-parse', 'upstream/release'), updated)
        self.assertEqual(self.git('symbolic-ref', 'HEAD'), 'refs/heads/launcher')
        self.assertEqual(self.git('status', '--porcelain'), status)
        item = self.results()[0]
        self.assertEqual(item['original_commit'], original)
        self.assertEqual(item['upstream_commit'], updated)
        self.assertEqual(item['commit'], updated)
        metadata = json.loads((self.output() / 'latest/run-metadata.json').read_text())
        self.assertTrue(metadata['rebase_upstream'])
        self.assert_no_temporary_worktrees()

    def test_explicit_rebase_upstream_remains_supported(self):
        original = self.branch('release', {'vale': 1})
        updated = self.branch('upstream-seed', {'vale': 4}, parent=original)
        self.upstream({'release': updated})
        result = self.compare('release', extra=('--rebase-upstream',))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('| release | 0 | 4 | 0 | 0 | 0 |', result.stdout)
        self.assertEqual(self.git('rev-parse', 'release'), updated)
        self.assert_no_temporary_worktrees()

    def test_no_rebase_checks_snapshot_without_fetching_or_updating_branches(self):
        original = self.branch('release', {'vale': 1})
        updated = self.branch('upstream-seed', {'vale': 4}, parent=original)
        self.upstream({'release': updated})
        self.git('update-ref', 'refs/remotes/upstream/release', original)
        for reference in ('release', 'upstream/release', original):
            with self.subTest(reference=reference):
                result = self.compare(reference, extra=('--no-rebase-upstream',))
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn(f'| {reference} | 0 | 1 | 0 | 0 | 0 |', result.stdout)
                self.assertEqual(self.git('rev-parse', 'release'), original)
                self.assertEqual(self.git('rev-parse', 'upstream/release'), original)
                metadata = json.loads((self.output() / 'latest/run-metadata.json').read_text())
                self.assertFalse(metadata['rebase_upstream'])
                self.assert_no_temporary_worktrees()

    def test_rebase_preserves_local_commits_on_updated_upstream(self):
        base = self.branch('release', {'vale': 1})
        (self.repo / 'local-note.adoc').write_text('Keep this local commit\n')
        self.git('add', '--', 'local-note.adoc')
        tree = self.git('write-tree')
        local = self.git('commit-tree', tree, '-p', base, '-m', 'Local note')
        self.git('update-ref', 'refs/heads/release', local)
        updated = self.branch('upstream-seed', {'vale': 3}, parent=base)
        self.upstream({'release': updated})
        result = self.compare('release')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('| release | 0 | 3 | 0 | 0 | 0 |', result.stdout)
        self.assertEqual(self.git('show', 'release:local-note.adoc'), 'Keep this local commit')
        self.assertEqual(self.git('rev-list', '--count', f'{updated}..release'), '1')
        self.assertEqual(self.git('merge-base', updated, 'release'), updated)
        self.assertEqual(self.results()[0]['original_commit'], local)
        self.assertNotEqual(self.results()[0]['commit'], local)
        self.assert_no_temporary_worktrees()

    def test_rebase_conflict_aborts_and_preserves_local_branch(self):
        base = self.branch('release', {'vale': 1})
        local = self.branch('release', {'vale': 2}, parent=base)
        updated = self.branch('upstream-seed', {'vale': 3}, parent=base)
        clean = self.branch('clean', {})
        self.upstream({'release': updated, 'clean': clean})
        status = self.git('status', '--porcelain')
        result = self.compare('release', 'clean')
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('| release | N/A | N/A | N/A | N/A | N/A |', result.stdout)
        self.assertIn('| clean | 0 | 0 | 0 | 0 | 0 |', result.stdout)
        self.assertIn('Rebase onto upstream/release failed', result.stderr)
        self.assertEqual(self.git('rev-parse', 'release'), local)
        self.assertEqual(self.git('status', '--porcelain'), status)
        log = self.output() / 'latest/01-release/run.log'
        self.assertIn('CONFLICT', log.read_text())
        self.assertFalse((log.parent / 'logs').exists())
        self.assert_no_temporary_worktrees()

    def test_rebase_rejects_branches_checked_out_elsewhere(self):
        release = self.branch('release', {})
        self.upstream({'release': release})
        busy = self.base / 'busy-worktree'
        self.git('worktree', 'add', str(busy), 'release')
        try:
            result = self.compare('release')
            self.assertEqual(result.returncode, 1)
            self.assertIn('branches checked out in a worktree: release', result.stderr)
            self.assertEqual(self.git('rev-parse', 'release'), release)
            self.assertFalse((self.output() / 'latest').exists())
        finally:
            self.git('worktree', 'remove', str(busy))

    def test_rebase_fetch_failure_preserves_previous_results(self):
        original = self.branch('release', {})
        self.assertEqual(self.compare('release', extra=('--no-rebase-upstream',)).returncode, 0)
        report = self.output() / 'latest/integrate-comparison.md'
        previous = report.read_bytes()
        self.git('remote', 'add', 'upstream', str(self.base / 'missing-upstream.git'))
        result = self.compare('release')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(report.read_bytes(), previous)
        self.assertEqual(self.git('rev-parse', 'release'), original)
        self.assert_no_temporary_worktrees()

    def test_rebase_requires_local_branch_names(self):
        release = self.branch('release', {})
        result = self.compare(release)
        self.assertEqual(result.returncode, 1)
        self.assertIn('requires an existing local branch', result.stderr)
        self.assertFalse((self.repo / 'logs').exists())

    def test_help_and_invalid_arguments_do_not_create_logs(self):
        result = subprocess.run([str(self.repo / 'compare-ocp-prechecks'), '--help'],
                                env=self.env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('(default)', result.stdout)
        self.assertIn('--no-rebase-upstream', result.stdout)
        result = self.compare('release', extra=('--rebase-upstream', '--no-rebase-upstream'))
        self.assertEqual(result.returncode, 2)
        for branches, category in ((('release', 'release'), 'integrate'),
                                   (('release',), '../integrate')):
            result = self.compare(*branches, category=category)
            self.assertEqual(result.returncode, 2)
        self.assertFalse((self.repo / 'logs').exists())

    def test_cleanup_preserves_unrelated_and_active_directories(self):
        output = self.base / 'output'
        output.mkdir()

        def run(name, category='integrate', finished=True):
            path = output / name
            path.mkdir()
            (path / 'run-metadata.json').write_text(json.dumps({
                'category': category, 'finished_utc': 'now' if finished else None,
            }))
            return path

        old = run('20261029T100000Z-old')
        foreign = run('20261029T100000Z-foreign', category='storage')
        unfinished = run('.running-unfinished', finished=False)
        unrelated = run('my-documents')
        active = run('20261029T100000Z-active')
        link = output / '20261029T100000Z-symlink'
        link.symlink_to(foreign, target_is_directory=True)
        new = run('.running-new')
        publish = self.module['publish_latest']
        with patch.dict(publish.__globals__, {'git': lambda *args: f'worktree {active}/tree'}):
            latest = publish(self.repo, output, new, 'integrate')
        self.assertEqual(latest, output / 'latest')
        self.assertFalse(old.exists())
        for path in (foreign, unfinished, unrelated, active, link):
            self.assertTrue(path.exists(), path)

    def test_failed_publish_restores_previous_latest(self):
        output = self.base / 'output'
        output.mkdir()
        for name in ('latest', '.running-new'):
            path = output / name
            path.mkdir()
            (path / 'run-metadata.json').write_text(json.dumps({
                'category': 'integrate', 'finished_utc': 'now',
            }))
            (path / 'marker').write_text(name)
        original_rename = Path.rename

        def fail_publish(path, target):
            if path == output / '.running-new':
                raise OSError('Simulated rename failure')
            return original_rename(path, target)

        with patch.object(Path, 'rename', fail_publish):
            with self.assertRaises(OSError):
                self.module['publish_latest'](self.repo, output, output / '.running-new', 'integrate')
        self.assertEqual((output / 'latest/marker').read_text(), 'latest')


if __name__ == '__main__':
    unittest.main()
