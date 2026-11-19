"""Regression coverage for include traversal and validation."""

import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / 'tree-map.py'
SPEC = importlib.util.spec_from_file_location('tree_map', SCRIPT)
tree_map = importlib.util.module_from_spec(SPEC)
with patch.object(sys, 'path', [str(SCRIPT.parent), *sys.path]):
    SPEC.loader.exec_module(tree_map)


class TreeMapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text='= Example\n'):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def build(self, entry, **kwargs):
        tracker = tree_map.ValidationTracker()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            tree_map.build_tree(entry, self.root, validator=tracker,
                                check_redundancy=True, no_color=True, **kwargs)
        return tracker, output.getvalue()

    def test_redundancy_includes_later_parent_modules_and_symlink_aliases(self):
        module = self.write('modules/shared.adoc')
        parent = self.write('maps/ocp-jobs/parent.adoc',
                            'include::child.adoc[leveloffset=+1]\n'
                            'include::../../modules/shared.adoc[leveloffset=+1]\n')
        self.write('maps/ocp-jobs/child.adoc',
                   'include::modules/shared.adoc[leveloffset=+1]\n')
        (parent.parent / 'modules').symlink_to(module.parent, target_is_directory=True)
        tracker, output = self.build(parent)
        self.assertEqual(len(tracker.redundancies), 1)
        issue = tracker.redundancies[0]
        self.assertEqual((issue['parent_file'], issue['parent_line']), (parent, 2))
        self.assertEqual(issue['child_line'], 1)
        self.assertIn('[REUSED]', output)

    def test_grandparent_redundancy_without_sibling_false_positives(self):
        self.write('modules/shared.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/shared.adoc[leveloffset=+1]\n'
                           'include::middle.adoc[leveloffset=+1]\n')
        self.write('maps/ocp-jobs/middle.adoc', 'include::leaf.adoc[leveloffset=+1]\n')
        self.write('maps/ocp-jobs/leaf.adoc',
                   'include::../../modules/shared.adoc[leveloffset=+1]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.redundancies), 1)
        self.assertEqual(tracker.redundancies[0]['parent_file'], entry)
        entry.write_text('include::leaf.adoc[leveloffset=+1]\n' * 2)
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.redundancies)
        self.assertFalse(tracker.errors)

    def test_cycle_using_parent_directory_and_symlink(self):
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::alias/../ocp-jobs/root.adoc[leveloffset=+1]\n')
        (entry.parent / 'alias').symlink_to(entry.parent, target_is_directory=True)
        tracker, output = self.build(entry)
        self.assertEqual(len(tracker.errors), 1)
        self.assertIn('Circular', tracker.errors[0].message)
        self.assertEqual((tracker.errors[0].file_path, tracker.errors[0].line), (entry, 1))
        self.assertIn('circular reference', output)

    def test_omitted_offset_is_allowed_when_no_heading_is_skipped(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc', '\ninclude::../../modules/topic.adoc[]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_first_module_skipping_parent_levels_warns(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/topic.adoc[leveloffset=+4]\n')
        tracker, _ = self.build(entry)
        self.assertIn('skips a parent heading', tracker.warnings[0].message)
        self.assertEqual((tracker.warnings[0].file_path, tracker.warnings[0].line), (entry, 1))

    def test_majority_offset_does_not_make_a_valid_subsection_an_outlier(self):
        for index in range(4):
            self.write(f'modules/topic{index}.adoc')
        self.write('modules/example-intro.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/example-intro.adoc[leveloffset=+0]\n' +
                           ''.join(f'include::../../modules/topic{i}.adoc[leveloffset=+{1 if i < 3 else 2}]\n'
                                   for i in range(4)))
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)
        entry.write_text(entry.read_text().replace('topic2.adoc[leveloffset=+1]',
                                                  'topic2.adoc[leveloffset=+2]'))
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_symlinked_attributes_are_not_classified_as_categories(self):
        attributes = self.write('common-attributes.adoc')
        alias = self.root / 'maps/osd/common-attributes.adoc'
        alias.parent.mkdir(parents=True)
        alias.symlink_to(attributes)
        self.assertEqual(tree_map.classify_file(alias), 'other')
        job = self.write('maps/new-product-jobs/example.adoc')
        self.assertEqual(tree_map.classify_file(job), 'job')

    def test_redundancy_only_does_not_validate_offsets(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/topic.adoc[leveloffset=-1]\n')
        tracker, _ = self.build(entry, validate_offsets=False)
        self.assertFalse(tracker.has_issues())

    def test_offset_above_containing_document_is_advisory(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/topic.adoc[leveloffset=-1]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.errors)
        self.assertIn('above its containing document', tracker.warnings[0].message)

    def test_gap_in_heading_sequence_warns_at_include_source(self):
        self.write('modules/parent.adoc')
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/parent.adoc[leveloffset=+1]\n'
                           'include::../../modules/child.adoc[leveloffset=+3]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.warnings), 1)
        self.assertEqual(tracker.warnings[0].line, 2)
        self.assertIn('section level 1 to 3', tracker.warnings[0].message)

    def test_valid_deep_nesting_and_return_to_parent_are_quiet(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc', ''.join(
            f'include::../../modules/topic.adoc[leveloffset=+{level}]\n'
            for level in (0, 1, 2, 3, 4, 4, 2, 1)))
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_module_internal_heading_can_supply_the_parent(self):
        self.write('modules/parent.adoc', '= Parent\n\n== Subsection\n')
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/parent.adoc[leveloffset=+1]\n'
                           'include::../../modules/child.adoc[leveloffset=+3]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_module_heading_level_is_used_in_addition_to_offset(self):
        self.write('modules/child.adoc', '== Child\n')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/child.adoc[leveloffset=+1]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.warnings), 1)
        self.assertIn('section level 0 to 2', tracker.warnings[0].message)

    def test_explicit_heading_between_includes_supplies_parent(self):
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           '= Job\n\n== Parent\n'
                           'include::../../modules/child.adoc[leveloffset=+2]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_headingless_content_and_code_samples_do_not_supply_parent(self):
        self.write('modules/text.adoc', 'Text.\n\n----\n== Sample heading\n----\n')
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/text.adoc[leveloffset=+1]\n'
                           'include::../../modules/child.adoc[leveloffset=+2]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.warnings), 1)

    def test_conditional_heading_is_not_assumed_to_supply_parent(self):
        self.write('modules/parent.adoc', '= Parent\nifdef::optional[]\n== Optional\nendif::[]\n')
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/parent.adoc[leveloffset=+1]\n'
                           'include::../../modules/child.adoc[leveloffset=+3]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_conditional_attributes_do_not_hide_unconditional_headings(self):
        self.write('modules/parent.adoc', 'ifdef::platform[]\n:flag:\nendif::[]\n= Parent\n')
        self.write('modules/child.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/parent.adoc[leveloffset=+1]\n'
                           'include::../../modules/child.adoc[leveloffset=+3]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.warnings), 1)

    def test_negative_offset_is_valid_when_source_heading_is_deeper(self):
        self.write('modules/child.adoc', '=== Child\n')
        entry = self.write('maps/ocp-jobs/root.adoc',
                           'include::../../modules/child.adoc[leveloffset=-1]\n')
        tracker, _ = self.build(entry)
        self.assertFalse(tracker.warnings)

    def test_dynamic_and_partial_includes_do_not_create_false_heading_gaps(self):
        self.write('modules/parent.adoc')
        self.write('modules/child.adoc')
        for attributes in ('leveloffset={depth}', 'leveloffset=2', 'tags=part,leveloffset=+1'):
            with self.subTest(attributes=attributes):
                entry = self.write('maps/ocp-jobs/root.adoc',
                                   f'include::../../modules/parent.adoc[{attributes}]\n'
                                   'include::../../modules/child.adoc[leveloffset=+3]\n')
                tracker, _ = self.build(entry)
                self.assertFalse(tracker.warnings)

    def test_comment_blocks_are_ignored_and_quoted_offsets_parsed(self):
        entry = self.write('maps/ocp/root.adoc',
                           '////\ninclude::missing.adoc[]\n////\n'
                           '// include::ignored.adoc[]\n'
                           'include::real.adoc[tags=x, leveloffset="+2"]\n')
        includes = tree_map.parse_includes(entry)
        self.assertEqual(includes, [{'path': 'real.adoc', 'line': 5, 'leveloffset': '+2'}])

    def test_repeated_jobs_are_read_once(self):
        entry = self.write('maps/osd/root.adoc',
                           'include::../hcm-jobs/shared.adoc[leveloffset=+1]\n' * 2)
        self.write('maps/hcm-jobs/shared.adoc')
        with patch.object(tree_map, 'parse_includes', wraps=tree_map.parse_includes) as parse:
            tracker, output = self.build(entry)
        self.assertEqual(parse.call_count, 2)
        self.assertFalse(tracker.errors)
        self.assertEqual(output.count('[JOB] shared.adoc'), 2)

    def test_missing_target_fails_cli(self):
        entry = self.write('maps/ocp/root.adoc', 'include::missing.adoc[]\n')
        result = subprocess.run([sys.executable, str(SCRIPT), '--validate', '--no-color', str(entry)],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('Missing file', result.stdout)
        self.assertNotIn('\033', result.stdout + result.stderr)

    def test_missing_relative_include_is_not_resolved_from_repo_root(self):
        self.write('modules/topic.adoc')
        entry = self.write('maps/ocp-jobs/root.adoc', 'include::modules/topic.adoc[]\n')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.errors), 1)
        self.assertIn('Missing file', tracker.errors[0].message)

    def test_read_failure_is_reported(self):
        entry = self.write('maps/ocp/root.adoc')
        entry.write_bytes(b'\xff')
        tracker, _ = self.build(entry)
        self.assertEqual(len(tracker.errors), 1)
        self.assertIn('Cannot read file', tracker.errors[0].message)

    def test_negative_max_depth_is_rejected(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '-d', '-1', 'anything'],
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
