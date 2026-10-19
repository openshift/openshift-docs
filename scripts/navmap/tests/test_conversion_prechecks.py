"""Exercise the Bash entry point with isolated, deterministic tool doubles."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'conversion-prechecks.sh'
FAKE_TOOL = r'''
import json, os, pathlib, sys
tool = pathlib.Path(sys.argv[0]).name
args = sys.argv[1:]
scenario = os.environ.get('PRECHECK_SCENARIO', '')
with open('calls.jsonl', 'a') as output:
    output.write(json.dumps([tool, args]) + '\n')
if tool == 'asciidoctor':
    if '-o' not in args:
        pathlib.Path(args[-1]).with_suffix('.html').write_text('unwanted HTML')
    if scenario == 'asciidoctor-failure':
        print('fatal renderer diagnostic', file=sys.stderr)
        sys.exit(2)
    if scenario == 'asciidoctor-error':
        print('asciidoctor: ERROR: missing include', file=sys.stderr)
elif tool == 'list-content':
    if scenario == 'discovery-failure':
        print('content discovery diagnostic', file=sys.stderr)
        sys.exit(3)
    if scenario == 'blank-content':
        print('\n')
    elif scenario != 'empty-content':
        print("modules/a topic's file.adoc\nmodules/other.adoc\nmodules/other.adoc")
elif 'sync' in args:
    if scenario == 'sync-failure':
        print('style download diagnostic', file=sys.stderr)
        sys.exit(4)
else:
    exploration = '--filter' in args
    assert args[-2:] == ["modules/a topic's file.adoc", 'modules/other.adoc'], args
    if scenario == 'vale-failure' or (exploration and scenario == 'exploration-failure'):
        sys.exit(2)  # Deliberately silent to expose output-only failure detection.
    if scenario == 'vale-findings' and not exploration:
        print('modules/other.adoc:1:1:AsciiDocDITA.Rule:issue')
        sys.exit(0 if '--no-exit' in args else 1)
    if scenario == 'suggestions' and exploration:
        print('modules/other.adoc:1:1:AsciiDocDITA.SnippetLink:suggestion')
'''


class ConversionPrechecksTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        script = self.root / 'scripts/navmap/conversion-prechecks.sh'
        script.parent.mkdir(parents=True)
        shutil.copy2(SCRIPT, script)
        self.script = script
        self.write('maps/ocp/navigation.adoc')
        self.write('maps/ocp/install.adoc')
        self.write('dita.ini')
        self.env = dict(os.environ, DITA_CONFIG=str(self.root / 'dita.ini'))
        bin_dir = self.root / 'bin'
        bin_dir.mkdir()
        for tool in ('asciidoctor', 'vale', 'list-content'):
            path = bin_dir / tool
            path.write_text(f'#!{sys.executable}\n' + FAKE_TOOL)
            path.chmod(0o755)
        self.env['PATH'] = str(bin_dir) + os.pathsep + os.environ['PATH']

    def write(self, name, text='= Example\n'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def run_checks(self, scenario='', args=('install',)):
        return subprocess.run(['bash', str(self.script), *args], cwd=self.root,
                              env=dict(self.env, PRECHECK_SCENARIO=scenario),
                              capture_output=True, text=True, timeout=15)

    def log(self, suffix):
        return (self.root / f'logs/install-{suffix}.log').read_text()

    def calls(self):
        return [json.loads(line) for line in (self.root / 'calls.jsonl').read_text().splitlines()]

    def test_clean_run_deduplicates_and_preserves_file_names(self):
        result = self.run_checks()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        calls = self.calls()
        self.assertEqual(sum(tool == 'list-content' for tool, _ in calls), 1)
        self.assertFalse(list(self.root.rglob('*.html')))
        self.assertEqual(self.log('vale'), '')

    def test_asciidoctor_execution_failure_preserves_diagnostics(self):
        result = self.run_checks('asciidoctor-failure')
        self.assertEqual(result.returncode, 1)
        self.assertIn('fatal renderer diagnostic', self.log('asciidoctor'))
        self.assertIn('status 2', self.log('asciidoctor'))

    def test_asciidoctor_errors_fail_even_with_zero_exit_status(self):
        result = self.run_checks('asciidoctor-error')
        self.assertEqual(result.returncode, 1)
        self.assertIn('missing include', self.log('asciidoctor'))

    def test_failed_discovery_fails_both_vale_checks(self):
        result = self.run_checks('discovery-failure')
        self.assertEqual(result.returncode, 1)
        for log_type in ('vale', 'exploration'):
            self.assertIn('content discovery diagnostic', self.log(log_type))
            self.assertIn('list-content failed', self.log(log_type))
        self.assertEqual(sum(tool == 'vale' for tool, _ in self.calls()), 1)

    def test_empty_discovery_is_not_a_clean_validation(self):
        for scenario in ('empty-content', 'blank-content'):
            with self.subTest(scenario=scenario):
                result = self.run_checks(scenario)
                self.assertEqual(result.returncode, 1)
                self.assertIn('No content files found', self.log('vale'))

    def test_sync_failure_is_fatal_and_logged(self):
        result = self.run_checks('sync-failure')
        self.assertEqual(result.returncode, 1)
        self.assertIn('style download diagnostic', self.log('vale'))
        self.assertIn('synchronization failed', self.log('exploration'))

    def test_silent_vale_execution_failure_is_fatal(self):
        result = self.run_checks('vale-failure')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Vale execution failed', self.log('vale'))

    def test_exploration_execution_failure_is_fatal(self):
        result = self.run_checks('exploration-failure')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Vale execution failed', self.log('exploration'))

    def test_dita_findings_fail_validation(self):
        result = self.run_checks('vale-findings')
        self.assertEqual(result.returncode, 1)
        self.assertIn('AsciiDocDITA.Rule', self.log('vale'))

    def test_exploration_suggestions_are_advisory(self):
        result = self.run_checks('suggestions')
        self.assertEqual(result.returncode, 0)
        self.assertIn('SnippetLink', self.log('exploration'))

    def test_all_syncs_once_and_discovers_once_per_product(self):
        self.write('maps/osd/navigation.adoc')
        result = self.run_checks(args=('--all',))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        calls = self.calls()
        self.assertEqual(sum(tool == 'vale' and 'sync' in args for tool, args in calls), 1)
        self.assertEqual(sum(tool == 'list-content' for tool, _ in calls), 2)
        self.assertTrue((self.root / 'logs/osd-vale.log').is_file())
        self.assertTrue((self.root / 'logs/vale.log').is_file())

    def test_all_continues_after_a_failed_product(self):
        self.write('maps/osd/navigation.adoc')
        result = self.run_checks('discovery-failure', args=('--all',))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(sum(tool == 'list-content' for tool, _ in self.calls()), 2)
        self.assertIn('list-content failed', (self.root / 'logs/osd-vale.log').read_text())

    def test_rerun_clears_stale_failure_logs(self):
        self.assertEqual(self.run_checks('discovery-failure').returncode, 1)
        self.assertEqual(self.run_checks().returncode, 0)
        self.assertEqual(self.log('vale'), '')
        self.assertEqual(self.log('exploration'), '')

    def test_product_name_takes_precedence_over_ocp_category(self):
        self.write('maps/virt/navigation.adoc')
        self.write('maps/ocp/virt.adoc')
        result = self.run_checks(args=('virt',))
        self.assertEqual(result.returncode, 0)
        self.assertTrue((self.root / 'logs/virt-vale.log').is_file())

    def test_help_needs_no_tools_or_logs(self):
        result = self.run_checks(args=('--help',))
        self.assertEqual(result.returncode, 0)
        self.assertIn('Usage:', result.stdout)
        self.assertFalse((self.root / 'logs').exists())

    def test_extra_arguments_are_rejected(self):
        result = self.run_checks(args=('install', 'ignored'))
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
