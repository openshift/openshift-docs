"""Regression coverage for job comparison and the existing module report."""

import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "audit-module-duplicates.py"
SPEC = importlib.util.spec_from_file_location("audit_modules", SCRIPT)
audit = importlib.util.module_from_spec(SPEC)
with patch.object(sys, "path", [str(SCRIPT.parent), *sys.path]):
    SPEC.loader.exec_module(audit)


class JobComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def report(self, *args):
        options, distros, categories = audit.parse_args(["audit-modules", *args])
        output = io.StringIO()
        with patch.object(audit, "REPO_ROOT", self.root), contextlib.redirect_stdout(output):
            audit.audit_distro(distros[0], options, categories)
        return output.getvalue()

    def dashboard_fixture(self):
        self.write("maps/ocp/observe.adoc", """include::ocp-jobs/dashboard.adoc[]
include::ocp-jobs/inventory.adoc[]
include::ocp-jobs/utilization.adoc[]
include::ocp-jobs/dashboard.adoc[]
////
include::ocp-jobs/commented.adoc[]
////
""")
        for name in ("dashboard", "inventory"):
            self.write(f"maps/ocp-jobs/{name}.adoc", "include::modules/overview.adoc[]\n")
        self.write("maps/ocp-jobs/utilization.adoc", """include::modules/overview.adoc[]
include::modules/utilization.adoc[]
include::nested.adoc[]
""")

    def test_identical_and_contained_pairs_include_unique_targets(self):
        self.dashboard_fixture()
        output = self.report("--compare-jobs", "--similarity", "100", "-c", "observe", "ocp")
        self.assertIn("Identical: 1; fully contained: 2; similar: 0 job pairs", output)
        self.assertIn("[IDENTICAL] 100.0%", output)
        self.assertEqual(output.count("[CONTAINED]"), 2)
        self.assertIn("Only A (0): none", output)
        self.assertIn("Only B (2):", output)
        self.assertIn("modules/utilization.adoc", output)
        self.assertIn("nested.adoc", output)

    def test_identical_only_excludes_contained_and_similar_pairs(self):
        self.dashboard_fixture()
        category = self.root / "maps/ocp/observe.adoc"
        category.write_text(category.read_text() + 'include::ocp-jobs/near.adoc[]\n')
        self.write("maps/ocp-jobs/near.adoc",
                   'include::modules/overview.adoc[]\ninclude::modules/extra.adoc[]\n')
        unfiltered = self.report("-j", "--similarity", "1", "ocp")
        self.assertIn("[CONTAINED]", unfiltered)
        self.assertIn("[SIMILAR]", unfiltered)
        output = self.report("-j", "--identical-only", "--similarity", "1", "-c", "observe", "ocp")
        self.assertEqual(output.count("[IDENTICAL]"), 1)
        self.assertIn("Identical: 1 job pairs", output)
        self.assertNotIn("[CONTAINED]", output)
        self.assertNotIn("[SIMILAR]", output)
        self.assertNotIn("ocp-jobs/utilization.adoc", output)
        self.assertNotIn("ocp-jobs/near.adoc", output)

    def test_identical_only_summary_counts_filtered_pairs(self):
        self.dashboard_fixture()
        output = self.report("-js", "--identical-only", "-c", "observe", "ocp")
        self.assertIn("ocp/observe", output)
        self.assertIn("Identical: 1 job pairs", output)
        self.assertNotIn("fully contained", output)
        self.assertNotIn("[IDENTICAL]", output)

    def test_identical_only_reports_no_matches_for_contained_pairs(self):
        self.dashboard_fixture()
        self.write("maps/ocp-jobs/inventory.adoc",
                   'include::modules/overview.adoc[]\ninclude::modules/inventory.adoc[]\n')
        output = self.report("-j", "--identical-only", "ocp")
        self.assertIn("Identical: 0 job pairs", output)
        self.assertIn("No matching job pairs.", output)
        self.assertNotIn("[CONTAINED]", output)

    def test_containment_puts_smaller_job_first_regardless_of_name(self):
        result = audit.compare_job_includes({"a-large": {"x", "y"}, "z-small": {"x"}}, 100)
        self.assertEqual(len(result), 1)
        self.assertEqual((result[0]["a"], result[0]["b"]), ("z-small", "a-large"))
        self.assertEqual(result[0]["only_a"], set())
        self.assertEqual(result[0]["only_b"], {"y"})

    def test_similarity_uses_union_and_honors_cutoff(self):
        jobs = {"a": {"one", "two", "three"}, "b": {"one", "two", "four"}}
        result = audit.compare_job_includes(jobs, 50)
        self.assertEqual(result[0]["kind"], "SIMILAR")
        self.assertEqual(result[0]["similarity"], 50)
        self.assertEqual(result[0]["only_a"], {"three"})
        self.assertEqual(result[0]["only_b"], {"four"})
        self.assertEqual(audit.compare_job_includes(jobs, 51), [])

    def test_empty_and_disjoint_jobs_do_not_match(self):
        jobs = {"empty-a": set(), "empty-b": set(), "a": {"x"}, "b": {"y"}}
        self.assertEqual(audit.compare_job_includes(jobs, 1), [])

    def test_comment_blocks_ignored_attributes_and_repetitions_do_not_affect_sets(self):
        path = self.write("job.adoc", """// include::modules/commented.adoc[]
////
include::modules/also-commented.adoc[]
////
include::modules/a.adoc[leveloffset=+1]
include::modules/b.adoc[tags=part]
include::modules/a.adoc[leveloffset=+2]
""")
        self.assertEqual(audit.read_include_targets(path), {"modules/a.adoc", "modules/b.adoc"})

    def test_nested_and_non_module_includes_are_compared_without_expansion(self):
        self.dashboard_fixture()
        self.write("maps/ocp-jobs/dashboard.adoc", "include::child-a.adoc[]\n")
        self.write("maps/ocp-jobs/inventory.adoc", "include::child-b.adoc[]\n")
        output = self.report("-j", "-c", "observe", "ocp")
        self.assertIn("No matching job pairs.", output)

    def test_category_filter_summary_and_pairing_stay_within_category(self):
        self.dashboard_fixture()
        self.write("maps/ocp/other.adoc", "include::ocp-jobs/dashboard.adoc[]\n")
        self.write("maps/ocp/navigation.adoc", "include::ocp-jobs/dashboard.adoc[]\n")
        output = self.report("-js", "-c", "observe", "ocp")
        self.assertIn("Identical: 1; fully contained: 2; similar: 0 job pairs", output)
        self.assertNotIn("[IDENTICAL]", output)
        self.assertNotIn("ocp/other", output)
        output = self.report("-js", "ocp")
        self.assertIn("ocp/other", output)
        self.assertEqual(output.count("Identical: 1; fully contained: 2; similar: 0"), 1)
        self.assertNotIn("ocp/navigation", output)

    def test_missing_or_unreadable_jobs_are_warned_and_excluded(self):
        self.write("maps/ocp/observe.adoc", """include::ocp-jobs/missing.adoc[]
include::ocp-jobs/invalid.adoc[]
""")
        invalid = self.write("maps/ocp-jobs/invalid.adoc", "")
        invalid.write_bytes(b"\xff")
        errors = io.StringIO()
        with contextlib.redirect_stderr(errors):
            output = self.report("-j", "ocp")
        self.assertEqual(errors.getvalue().count("Warning: could not read"), 2)
        self.assertIn("No matching job pairs.", output)

    def test_existing_module_report_still_counts_repeated_module_includes(self):
        self.dashboard_fixture()
        self.write("maps/ocp-jobs/dashboard.adoc", "include::modules/overview.adoc[]\n" * 2)
        output = self.report("-r", "-c", "observe", "ocp")
        self.assertIn("Module usage report: ocp", output)
        self.assertIn("[DUP+CROSS]", output)
        self.assertIn("ocp-jobs/dashboard.adoc (x4)", output)
        self.assertNotIn("Job include comparison", output)

    def test_invalid_cli_options_fail_with_usage_error(self):
        cases = [
            ["-j", "--similarity", "0"], ["-j", "--similarity", "101"],
            ["-j", "--similarity", "bad"], ["-j", "--similarity"],
            ["--similarity", "80"], ["-jd"], ["-jr"], ["-j", "-t", "2"],
            ["--not-a-flag"],
            ["--identical-only"],
        ]
        for args in cases:
            with self.subTest(args=args):
                result = subprocess.run([sys.executable, str(SCRIPT), *args],
                                        text=True, capture_output=True)
                self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
                self.assertTrue(result.stderr)


if __name__ == "__main__":
    unittest.main()
