"""Exercise content retention and uncertainty in tree-map removal simulations."""

import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "tree-map.py"
SPEC = importlib.util.spec_from_file_location("tree_map_comparison_tests", SCRIPT)
tree = importlib.util.module_from_spec(SPEC)
with patch.object(sys, "path", [str(SCRIPT.parent), *sys.path]):
    SPEC.loader.exec_module(tree)


class TreeMapComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content="= Example\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def fixture(self, extra=""):
        self.write("modules/shared.adoc")
        a = self.write("maps/ocp-jobs/a.adoc", extra + "include::../../modules/shared.adoc[]\n")
        b = self.write("maps/ocp-jobs/b.adoc", "include::../../modules/shared.adoc[]\n")
        category = self.write("maps/ocp/observe.adoc",
                              "include::../ocp-jobs/a.adoc[]\ninclude::../ocp-jobs/b.adoc[]\n")
        return category, a, b

    def analyze(self, category):
        return tree.MapComparison(category, self.root, tree.classify_file)

    def impact(self, analysis, *names):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            errors = analysis.print_impact(analysis.select_jobs(names))
        return output.getvalue(), errors

    def cli(self, *args):
        output = io.StringIO()
        with patch.object(sys, "argv", [str(SCRIPT), *map(str, args)]), \
                patch.object(tree, "__file__", str(self.root / "scripts/navmap/tree-map.py")), \
                contextlib.redirect_stdout(output):
            tree.main()
        return output.getvalue()

    def test_single_removal_retains_content_but_removing_both_loses_it(self):
        category, a, b = self.fixture()
        analysis = self.analyze(category)
        output, errors = self.impact(analysis, "a.adoc")
        self.assertFalse(errors)
        self.assertIn("Include targets lost: 0", output)
        self.assertIn("Keep maps/ocp-jobs/b.adoc (1 shared targets)", output)
        self.assertNotIn("Keep maps/ocp-jobs/a.adoc", output)
        output, errors = self.impact(analysis, "a.adoc", "b.adoc")
        self.assertIn("Include targets lost: 1", output)
        self.assertIn("modules/shared.adoc", output)
        self.assertNotIn("    Keep ", output)

    def test_annotations_point_to_larger_covering_job(self):
        category, a, b = self.fixture()
        self.write("modules/extra.adoc")
        b.write_text(b.read_text() + "include::../../modules/extra.adoc[]\n")
        annotations = self.analyze(category).annotations()
        self.assertIn("all also in maps/ocp-jobs/b.adoc", annotations[category, a])
        self.assertIn("1 unique include targets", annotations[category, b])

    def test_nested_jobs_modules_and_snippets_are_expanded(self):
        category, a, b = self.fixture()
        snippet = self.write("snippets/extra.adoc", "Shared text\n")
        self.write("modules/shared.adoc", "= Shared\ninclude::../snippets/extra.adoc[]\n")
        child = self.write("maps/ocp-jobs/child.adoc", "include::../../modules/shared.adoc[]\n")
        a.write_text("include::child.adoc[]\n")
        analysis = self.analyze(category)
        self.assertEqual(analysis.coverage[a].targets, analysis.coverage[b].targets)
        self.assertIn((snippet, ""), analysis.coverage[a].targets)
        output, errors = self.impact(analysis, "a.adoc")
        self.assertIn("Include targets lost: 0", output)
        self.assertIn("2 shared targets", output)

    def test_partial_include_is_not_covered_by_different_selection(self):
        category, a, b = self.fixture()
        a.write_text('include::../../modules/shared.adoc[tags="first",leveloffset=+1]\n')
        b.write_text('include::../../modules/shared.adoc[tags="second",leveloffset=+1]\n')
        analysis = self.analyze(category)
        output, errors = self.impact(analysis, "a.adoc")
        self.assertIn("Include targets lost: 1", output)
        self.assertIn("[tags=first]", output)
        self.assertIn("fragment not expanded", output)
        self.assertIn("comparison incomplete", analysis.annotations()[category, a])
        self.assertFalse(errors)  # Review findings are advisory, not graph errors.

    def test_fragmented_job_is_selectable_but_not_treated_as_its_full_contents(self):
        category, a, b = self.fixture()
        category.write_text('include::../ocp-jobs/a.adoc[tags="part"]\n'
                            'include::../ocp-jobs/b.adoc[]\n')
        analysis = self.analyze(category)
        self.assertEqual(analysis.coverage[a].targets, {(a, "tags=part")})
        output, errors = self.impact(analysis, "a.adoc")
        self.assertIn("Include targets lost: 1", output)
        self.assertIn("job fragment [tags=part] not expanded", output)
        self.assertNotIn("Keep maps/ocp-jobs/b.adoc", output)

    def test_similar_annotation_honors_cutoff_and_lists_unique_count(self):
        category, a, b = self.fixture()
        for name in ("only-a", "only-b"):
            self.write(f"modules/{name}.adoc")
        a.write_text(a.read_text() + "include::../../modules/only-a.adoc[]\n")
        b.write_text(b.read_text() + "include::../../modules/only-b.adoc[]\n")
        analysis = tree.MapComparison(category, self.root, tree.classify_file, similarity=33)
        self.assertIn("SIMILAR 33.3%", analysis.annotations()[category, a])
        self.assertIn("1 unique include targets", analysis.annotations()[category, a])
        analysis.similarity = 34
        self.assertNotIn("SIMILAR", analysis.annotations()[category, a])

    def test_comparison_ignores_comments_and_normalizes_selection_attributes(self):
        category, a, b = self.fixture()
        a.write_text('////\ninclude::missing.adoc[]\n////\n'
                     'include::../../modules/shared.adoc[tags="one,two",lines="1..2",leveloffset=+1]\n')
        b.write_text('include::../../modules/shared.adoc[lines=1..2,tags="one,two",leveloffset=+2]\n')
        analysis = self.analyze(category)
        self.assertEqual(analysis.coverage[a].targets, analysis.coverage[b].targets)
        self.assertFalse(analysis.before.errors)

    def test_failed_reference_scan_returns_failure_instead_of_a_clean_result(self):
        category, a, b = self.fixture()
        self.write("bad.adoc").write_bytes(b"\xff")
        output, errors = self.impact(self.analyze(category), "a.adoc")
        self.assertTrue(errors)
        self.assertIn("reference scan failed", output)

    def test_remote_includes_are_opaque_review_targets_rather_than_missing_local_files(self):
        category, a, b = self.fixture()
        url = "https://example.invalid/template.yaml"
        a.write_text(a.read_text() + f"include::{url}[]\n")
        b.write_text(b.read_text() + f"include::{url}[]\n")
        analysis = self.analyze(category)
        self.assertFalse(analysis.before.errors)
        self.assertIn((url, ""), analysis.coverage[a].targets)
        output, errors = self.impact(analysis, "a.adoc")
        self.assertFalse(errors)
        self.assertIn("Include targets lost: 0", output)
        self.assertIn(url, output)
        self.assertIn("not fetched; external content needs review", output)
        output, errors = self.impact(analysis, "a.adoc", "b.adoc")
        self.assertIn("Include targets lost: 2", output)

    def test_local_prose_anchors_context_notes_and_references_are_reported(self):
        category, a, b = self.fixture(""":context: inventory
// TODO: preserve this gap
// including this continuation

[id="inventory-anchor"]
= Inventory instructions
Unique guidance.
""")
        self.write("guide.adoc", "xref:maps/ocp-jobs/a.adoc#inventory-anchor[Inventory]\n")
        output, errors = self.impact(self.analyze(category), "a.adoc")
        self.assertIn("Include targets lost: 0", output)
        self.assertIn("Local content lost", output)
        self.assertIn("Unique guidance.", output)
        self.assertIn("context-dependent anchors/attributes", output)
        self.assertIn("including this continuation", output)
        self.assertIn("guide.adoc:1:", output)
        self.assertIn("REVIEW REQUIRED", output)

    def test_missing_and_cyclic_graphs_are_incomplete_and_fail_impact(self):
        for include in ("missing.adoc", "a.adoc"):
            with self.subTest(include=include):
                category, a, b = self.fixture()
                a.write_text(f"include::{include}[]\n")
                analysis = self.analyze(category)
                output, errors = self.impact(analysis, "a.adoc")
                self.assertTrue(errors)
                self.assertTrue(analysis.before.errors)
                self.assertIn("comparison incomplete", analysis.annotations()[category, a])

    def test_conditionals_are_uncertain_and_not_equivalence_proof(self):
        category, a, b = self.fixture()
        a.write_text("ifdef::optional[]\n" + a.read_text() + "endif::[]\n")
        analysis = self.analyze(category)
        self.assertIn("comparison incomplete", analysis.annotations()[category, a])
        output, errors = self.impact(analysis, "a.adoc")
        self.assertIn("conditional include needs review", output)
        self.assertFalse(errors)

    def test_conditional_prose_keeps_file_comparison_and_shows_source_locations(self):
        category, a, b = self.fixture()
        self.write("snippets/shared.adoc", "Shared snippet\n")
        self.write("modules/shared.adoc", """include::../snippets/shared.adoc[]
ifndef::openshift-rosa[]
Use cluster-admin.
endif::[]
""")
        analysis = self.analyze(category)
        self.assertFalse(analysis.coverage[a].issues)
        self.assertTrue(analysis.coverage[a].text_reviews)
        annotation = analysis.annotations()[category, a]
        self.assertIn("0 unique include targets", annotation)
        self.assertNotIn("comparison incomplete", annotation)
        self.assertIn("distro-specific or conditional text needs review", annotation)
        output = self.cli("--compare-jobs", "--no-color", category)
        self.assertIn("modules/shared.adoc:2: distro-specific or conditional text needs review", output)
        output, errors = self.impact(analysis, "a.adoc")
        self.assertFalse(errors)
        self.assertIn("distro-specific or conditional text needs review", output)

    def test_conditional_prose_in_leaf_modules_also_gets_a_review_note(self):
        category, a, b = self.fixture()
        self.write("modules/shared.adoc", "ifdef::openshift-rosa[Use dedicated-admin.]\n")
        analysis = self.analyze(category)
        self.assertFalse(analysis.coverage[a].issues)
        self.assertIn("0 unique include targets", analysis.annotations()[category, a])
        self.assertIn("distro-specific or conditional text needs review", analysis.annotations()[category, a])

    def test_ifeval_and_category_conditions_still_make_include_comparison_incomplete(self):
        for wrapper in ('ifdef::optional[]', 'ifeval::["{platform}" == "ocp"]'):
            with self.subTest(wrapper=wrapper):
                category, a, b = self.fixture()
                category.write_text(wrapper + '\n' + category.read_text() + 'endif::[]\n')
                analysis = self.analyze(category)
                self.assertIn("comparison incomplete", analysis.annotations()[category, a])
                self.assertTrue(any('conditional include needs review' in issue
                                    for issue in analysis.before.issues))
                navigation = self.write("maps/ocp/navigation.adoc", "include::observe.adoc[]\n")
                output, errors = self.impact(self.analyze(navigation), "a.adoc")
                self.assertIn("maps/ocp/observe.adoc:2: conditional include needs review", output)

    def test_symlink_aliases_resolve_to_same_content(self):
        category, a, b = self.fixture()
        alias = self.root / "modules/alias.adoc"
        alias.symlink_to(self.root / "modules/shared.adoc")
        b.write_text("include::../../modules/alias.adoc[]\n")
        output, errors = self.impact(self.analyze(category), "a.adoc")
        self.assertIn("Include targets lost: 0", output)

    def test_ambiguous_names_require_a_path_and_unknown_jobs_are_rejected(self):
        category, a, b = self.fixture()
        other = self.write("maps/other-jobs/a.adoc", "include::../../modules/shared.adoc[]\n")
        category.write_text(category.read_text() + "include::../other-jobs/a.adoc[]\n")
        analysis = self.analyze(category)
        for name in ("a.adoc", "not-present.adoc"):
            with self.assertRaises(ValueError):
                analysis.select_jobs([name])
        self.assertEqual(analysis.select_jobs(["maps/other-jobs/a.adoc"]), {other})

    def test_category_specific_annotations_and_depth_independent_impact(self):
        category, a, b = self.fixture()
        other = self.write("maps/ocp/other.adoc", "include::../ocp-jobs/a.adoc[]\n")
        navigation = self.write("maps/ocp/navigation.adoc",
                                "include::observe.adoc[]\ninclude::other.adoc[]\n")
        analysis = self.analyze(navigation)
        self.assertIn("0 unique", analysis.annotations()[category, a])
        self.assertIn("1 unique", analysis.annotations()[other, a])
        output = self.cli("--no-color", "--max-depth", "2", "--compare-jobs", navigation)
        self.assertIn("0 unique", output)
        self.assertIn("1 unique", output)
        output = self.cli("--no-color", "--max-depth", "0", "--removal-impact", "a.adoc", category)
        self.assertIn("Include targets lost: 0", output)
        self.assertIn("full selected map", output)

    def test_shared_parent_edits_list_users_in_other_maps(self):
        category, a, b = self.fixture()
        child = self.write("maps/ocp-jobs/child.adoc", "include::../../modules/shared.adoc[]\n")
        a.write_text("include::child.adoc[]\n")
        self.write("maps/ocp/elsewhere.adoc", "include::../ocp-jobs/a.adoc[]\n")
        output, errors = self.impact(self.analyze(category), "child.adoc")
        self.assertIn("maps/ocp/elsewhere.adoc:1:", output)
        self.assertIn("maps/ocp-jobs/a.adoc:1 ->", output)

    def test_direct_category_includes_and_aliased_users_are_reported(self):
        category, a, b = self.fixture()
        category.write_text("include::../ocp-jobs/a.adoc[]\ninclude::../../modules/shared.adoc[]\n")
        alias = self.root / "maps/ocp-jobs/alias.adoc"
        alias.symlink_to(a)
        self.write("maps/ocp/other.adoc", "include::../ocp-jobs/alias.adoc[]\n")
        output, errors = self.impact(self.analyze(category), "a.adoc")
        self.assertIn("Include targets lost: 0", output)
        self.assertIn("Retained at maps/ocp/observe.adoc:2", output)
        self.assertIn("maps/ocp/other.adoc:1:", output)

    def test_dynamic_and_unreadable_sources_never_prove_equivalence(self):
        category, a, b = self.fixture()
        a.write_text("include::{module-path}/shared.adoc[]\n")
        analysis = self.analyze(category)
        self.assertIn("comparison incomplete", analysis.annotations()[category, a])
        output, errors = self.impact(analysis, "a.adoc")
        self.assertIn("unresolved include {module-path}", output)
        b.write_bytes(b"\xff")
        analysis = self.analyze(category)
        self.assertTrue(analysis.before.errors)
        output, errors = self.impact(analysis, "b.adoc")
        self.assertTrue(errors)
        self.assertIn("cannot read source", output)

    def test_cli_rejects_invalid_cutoffs_and_unreachable_jobs(self):
        category, a, b = self.fixture()
        for args in (["--similarity", "80"], ["--compare-jobs", "--similarity", "0"],
                     ["--compare-jobs", "--similarity", "101"],
                     ["--removal-impact", "unknown.adoc"]):
            with self.subTest(args=args):
                result = subprocess.run([sys.executable, str(SCRIPT), *args, str(category)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)

    def distro_fixture(self):
        category, a, b = self.fixture()
        self.write("modules/other.adoc")
        self.write("maps/ocp-jobs/other.adoc", "include::../../modules/other.adoc[]\n")
        self.write("maps/ocp/optimize.adoc", "include::../ocp-jobs/other.adoc[]\n")
        navigation = self.write("maps/ocp/navigation.adoc",
                                "include::observe.adoc[]\ninclude::optimize.adoc[]\n")
        self.write("maps/rosa-hcp/navigation.adoc", "include::observe.adoc[]\n")
        self.write("maps/rosa-hcp/observe.adoc", "include::../ocp-jobs/b.adoc[]\n")
        return category, navigation

    def test_distro_shorthand_matches_explicit_navigation_and_category_paths(self):
        category, navigation = self.distro_fixture()
        self.assertEqual(self.cli("--compare-jobs", "--no-color", "ocp"),
                         self.cli("--compare-jobs", "--no-color", navigation))
        self.assertEqual(self.cli("--compare-jobs", "--no-color", "ocp", "observe"),
                         self.cli("--compare-jobs", "--no-color", category))
        self.assertEqual(self.cli("--no-color", "-l", "rosa-hcp", "observe"),
                         self.cli("--no-color", "-l", self.root / "maps/rosa-hcp/observe.adoc"))

    def test_category_flags_interspersed_options_and_suffixes_are_supported(self):
        category, navigation = self.distro_fixture()
        expected = self.cli("--compare-jobs", "--no-color", category)
        for args in (["-c", "observe", "ocp"], ["ocp", "-c", "observe.adoc"],
                     ["ocp", "--compare-jobs", "observe"],
                     ["ocp", "observe", "-c", "observe.adoc"]):
            with self.subTest(args=args):
                output = self.cli("--compare-jobs", "--no-color", *args)
                self.assertEqual(output, expected)

    def test_multiple_categories_render_separately_without_other_distro_content(self):
        category, navigation = self.distro_fixture()
        output = self.cli("--compare-jobs", "--no-color", "ocp", "observe", "optimize")
        self.assertIn("Map: maps/ocp/observe.adoc", output)
        self.assertIn("Map: maps/ocp/optimize.adoc", output)
        self.assertNotIn("navigation.adoc", output)
        self.assertNotIn("rosa-hcp", output)
        self.assertEqual(output.count("JOB COMPARISON"), 2)
        self.assertEqual(output, self.cli("--compare-jobs", "--no-color", "ocp",
                                         "-c", "observe", "-c", "optimize"))

    def test_multiple_category_removals_resolve_across_the_selected_scope(self):
        category, navigation = self.distro_fixture()
        output = self.cli("--removal-impact", "other.adoc", "--no-color", "ocp", "observe", "optimize")
        self.assertIn("No selected removal jobs occur in this map", output)
        self.assertIn("Scope: maps/ocp/optimize.adoc", output)
        self.assertIn("Include targets lost: 1", output)
        self.assertEqual(output.count("REMOVAL IMPACT"), 1)

    def test_selection_errors_list_valid_distros_and_categories_before_rendering(self):
        category, navigation = self.distro_fixture()
        cases = [
            (["unknown"], "Available distros: ocp, rosa-hcp"),
            (["ocp-jobs"], "Unknown distro"),
            (["ocp", "observe", "missing"], "Available categories: observe, optimize"),
            (["ocp", "../observe"], "Invalid category"),
            ([str(category), "-c", "observe"], "Category selection requires a distro name"),
        ]
        for args, message in cases:
            with self.subTest(args=args):
                errors, output = io.StringIO(), io.StringIO()
                with patch.object(sys, "argv", [str(SCRIPT), *args]), \
                        patch.object(tree, "__file__", str(self.root / "scripts/navmap/tree-map.py")), \
                        contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors), \
                        self.assertRaises(SystemExit) as raised:
                    tree.main()
                self.assertEqual(raised.exception.code, 2)
                self.assertIn(message, errors.getvalue())
                self.assertEqual(output.getvalue(), "")

    def test_multiple_categories_continue_after_a_failed_graph_check(self):
        category, navigation = self.distro_fixture()
        category.write_text("include::missing.adoc[]\n")
        output = io.StringIO()
        with patch.object(sys, "argv", [str(SCRIPT), "--compare-jobs", "--no-color",
                                        "ocp", "observe", "optimize"]), \
                patch.object(tree, "__file__", str(self.root / "scripts/navmap/tree-map.py")), \
                contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as raised:
            tree.main()
        self.assertEqual(raised.exception.code, 1)
        self.assertIn("Map: maps/ocp/optimize.adoc", output.getvalue())

    def test_validate_warns_about_identical_jobs_without_compare_flag(self):
        category, a, b = self.fixture()
        output = self.cli("--validate", "--no-color", category)
        self.assertIn("Identical direct include target set as maps/ocp-jobs/b.adoc", output)
        self.assertIn("maps/ocp-jobs/a.adoc", output)
        self.assertIn("Check conditional includes and include attributes before removing either job", output)
        self.assertIn("Total: 1 warning(s)", output)
        self.assertIn("2 jobs compared", output)
        self.assertNotIn("No validation issues found", output)
        self.assertNotIn("No issues found in the checks performed", output)

    def test_validate_marks_both_jobs_with_the_same_group_in_the_tree(self):
        category, a, b = self.fixture()
        output = self.cli("--validate", "--no-color", category)
        jobs = [line for line in output.splitlines() if '[JOB]' in line]
        self.assertEqual(len(jobs), 2)
        self.assertTrue(all('[IDENTICAL G1]' in line for line in jobs))
        self.assertIn('[IDENTICAL G1] Identical direct include target set as', output)
        self.assertNotIn('\033', output)
        colored = self.cli('--validate', category)
        self.assertIn(tree.Colors.WARNING + '[IDENTICAL G1]' + tree.Colors.RESET, colored)

    def test_identical_markers_group_multiple_jobs_and_keep_other_groups_distinct(self):
        category, a, b = self.fixture()
        self.write('maps/ocp-jobs/c.adoc', 'include::../../modules/shared.adoc[]\n')
        self.write('modules/other.adoc')
        for name in ('d', 'e'):
            self.write(f'maps/ocp-jobs/{name}.adoc', 'include::../../modules/other.adoc[]\n')
        category.write_text(category.read_text() + ''.join(
            f'include::../ocp-jobs/{name}.adoc[]\n' for name in ('c', 'd', 'e')))
        output = self.cli('--validate', '--no-color', category)
        jobs = [line for line in output.splitlines() if '[JOB]' in line]
        self.assertEqual(sum('[IDENTICAL G1]' in line for line in jobs), 3)
        self.assertEqual(sum('[IDENTICAL G2]' in line for line in jobs), 2)
        self.assertIn('Total: 4 warning(s)', output)

    def test_identical_markers_coexist_with_comparison_annotations_and_reuse_cached_reads(self):
        category, a, b = self.fixture()
        with patch.object(tree, 'parse_includes', wraps=tree.parse_includes) as parse:
            output = self.cli('--validate', '--no-color', category)
        self.assertEqual(parse.call_count, 3)  # Category and two jobs, once each.
        output = self.cli('--validate', '--compare-jobs', '--no-color', category)
        jobs = [line for line in output.splitlines() if '[JOB]' in line]
        self.assertTrue(all('[IDENTICAL G1]' in line and '0 unique include targets' in line for line in jobs))

    def test_validate_keeps_exact_job_matches_separate_from_containment(self):
        category, a, b = self.fixture()
        self.write("modules/extra.adoc")
        b.write_text(b.read_text() + "include::../../modules/extra.adoc[]\n")
        output = self.cli("--validate", "--no-color", category)
        self.assertNotIn("Identical direct include target set", output)
        self.assertIn("2 jobs compared", output)
        self.assertIn("No issues found in the checks performed within the traversed tree", output)
        self.assertNotIn("No validation issues found", output)
        self.assertNotIn('[IDENTICAL G1]', output)

    def test_validate_identical_job_check_respects_traversal_depth(self):
        category, a, b = self.fixture()
        shallow = self.cli("--validate", "--no-color", "--max-depth", "1", category)
        self.assertIn("0 jobs compared", shallow)
        self.assertNotIn("Identical direct include target set as", shallow)
        self.assertNotIn('[IDENTICAL G1]', shallow)
        deeper = self.cli("--validate", "--no-color", "--max-depth", "2", category)
        self.assertIn("2 jobs compared", deeper)
        self.assertIn("Identical direct include target set as", deeper)

    def test_validate_does_not_report_same_job_or_jobs_in_other_categories_as_duplicates(self):
        category, a, b = self.fixture()
        category.write_text("include::../ocp-jobs/a.adoc[]\n" * 2)
        self.write("maps/ocp/other.adoc", "include::../ocp-jobs/b.adoc[]\n")
        navigation = self.write("maps/ocp/navigation.adoc",
                                "include::observe.adoc[]\ninclude::other.adoc[]\n")
        output = self.cli("--validate", "--no-color", navigation)
        self.assertIn("2 jobs compared", output)
        self.assertNotIn("Identical direct include target set as", output)

    def test_validate_reports_direct_target_matches_despite_conditions_and_selections(self):
        category, a, b = self.fixture()
        a.write_text('ifdef::optional[]\ninclude::../../modules/shared.adoc[tags=part]\nendif::[]\n')
        output = self.cli("--validate", "--no-color", category)
        self.assertIn("Identical direct include target set as", output)
        self.assertIn("Conditions, include selections, and rendered content are not evaluated", output)
        self.assertIn("Check conditional includes and include attributes", output)

    def test_validate_ignores_empty_jobs_and_resolves_aliases(self):
        category, a, b = self.fixture()
        a.write_text("= Only prose\n")
        b.write_text("= More prose\n")
        output = self.cli("--validate", "--no-color", category)
        self.assertNotIn("Identical direct include target set as", output)
        alias = self.root / "modules/alias.adoc"
        alias.symlink_to(self.root / "modules/shared.adoc")
        a.write_text("include::../../modules/shared.adoc[]\n")
        b.write_text("include::../../modules/alias.adoc[]\n")
        output = self.cli("--validate", "--no-color", category)
        self.assertIn("Identical direct include target set as", output)


if __name__ == "__main__":
    unittest.main()
