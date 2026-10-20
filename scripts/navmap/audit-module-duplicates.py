#!/usr/bin/env python3
"""Report module usage within categories, detecting both duplicates and cross-job redundancy.

Scans category files to find all job includes, then scans each job to find module
includes. Reports how many times each module appears in a category, whether from
the same job (duplicate) or across multiple jobs (valid but redundant).

Usage:
    python3 scripts/navmap/audit-module-duplicates.py [FLAGS] [DISTRO ...]

Flags:
    --category CAT, -c CAT      Filter to specific category file(s) (repeatable)
    --duplicates-only, -d       Show only modules with duplicates in same job
    --redundant-only, -r        Show only modules appearing in 2+ jobs
    --threshold N, -t N         Show only modules appearing N+ times (default: 2)
    --compare-jobs, -j          Compare jobs' direct include target sets
    --identical-only           Show only identical job pairs (requires -j)
    --similarity N             Minimum similarity percentage (1-100; default: 80)
    --summary, -s               Show summary table only
    --help, -h                  Show this help

Examples:
    python3 scripts/navmap/audit-module-duplicates.py ocp
    python3 scripts/navmap/audit-module-duplicates.py -c install ocp
    python3 scripts/navmap/audit-module-duplicates.py -d ocp     # duplicates only
    python3 scripts/navmap/audit-module-duplicates.py -t 3 ocp   # 3+ appearances
    python3 scripts/navmap/audit-module-duplicates.py -r rosa-hcp  # cross-job redundancy
    python3 scripts/navmap/audit-module-duplicates.py -j -c observe ocp
    python3 scripts/navmap/audit-module-duplicates.py -j --similarity 70 ocp
    python3 scripts/navmap/audit-module-duplicates.py -j --identical-only ocp

Job comparison reports identical sets, full containment, and similar sets within
each category. Similarity is shared targets / all distinct targets in both jobs.
By default, identical and contained pairs are reported regardless of the cutoff.
Use --identical-only to exclude contained and similar pairs.
Order, repetitions, and include attributes are ignored; nested jobs are not
expanded and AsciiDoc conditionals are not evaluated. Matches are review candidates.
The module filters -d, -r, and -t cannot be combined with --compare-jobs.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from job_comparison import compare_job_includes

INCLUDE_RE = re.compile(r"^include::(.+?)\[", re.MULTILINE)
JOBS_DIR_RE = re.compile(r"^([a-z][a-z0-9_-]*-jobs)/(.+\.adoc)$")
MODULE_RE = re.compile(r"^modules/(.+\.adoc)$")
REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def parse_args(argv: list[str]) -> tuple[dict, list[str], list[str]]:
    """Parse flags, category filters, and distro names.

    Returns (options, distros, categories).
    """
    options = {
        "duplicates_only": False,
        "redundant_only": False,
        "threshold": 2,
        "summary_only": False,
        "compare_jobs": False,
        "identical_only": False,
        "similarity": 80,
    }
    distros: list[str] = []
    categories: list[str] = []
    expect_category = False
    expect_threshold = False
    expect_similarity = False
    module_filters = False
    similarity_given = False

    for arg in argv[1:]:
        if expect_similarity:
            try:
                options["similarity"] = int(arg)
            except ValueError:
                print("Error: --similarity must be an integer from 1 to 100.", file=sys.stderr)
                raise SystemExit(2)
            if not 1 <= options["similarity"] <= 100:
                print("Error: --similarity must be an integer from 1 to 100.", file=sys.stderr)
                raise SystemExit(2)
            expect_similarity = False
            continue

        if expect_category:
            cat = arg if arg.endswith(".adoc") else f"{arg}.adoc"
            categories.append(cat)
            expect_category = False
            continue

        if expect_threshold:
            try:
                options["threshold"] = int(arg)
            except ValueError:
                print(f"Error: threshold must be an integer, got '{arg}'", file=sys.stderr)
                raise SystemExit(2)
            expect_threshold = False
            continue

        if arg in ("-c", "--category"):
            expect_category = True
        elif arg in ("-t", "--threshold"):
            expect_threshold = True
            module_filters = True
        elif arg in ("-d", "--duplicates-only"):
            options["duplicates_only"] = True
            module_filters = True
        elif arg in ("-r", "--redundant-only"):
            options["redundant_only"] = True
            module_filters = True
        elif arg in ("-j", "--compare-jobs"):
            options["compare_jobs"] = True
        elif arg == "--identical-only":
            options["identical_only"] = True
        elif arg == "--similarity":
            expect_similarity = True
            similarity_given = True
        elif arg in ("-s", "--summary"):
            options["summary_only"] = True
        elif arg in ("-h", "--help"):
            print(__doc__)
            raise SystemExit(0)
        elif arg.startswith("-") and not arg.startswith("--"):
            # Combined short flags
            for ch in arg[1:]:
                if ch in "drt":
                    module_filters = True
                if ch == "d":
                    options["duplicates_only"] = True
                elif ch == "r":
                    options["redundant_only"] = True
                elif ch == "s":
                    options["summary_only"] = True
                elif ch == "j":
                    options["compare_jobs"] = True
                elif ch == "c":
                    expect_category = True
                elif ch == "t":
                    expect_threshold = True
                elif ch == "h":
                    print(__doc__)
                    raise SystemExit(0)
                else:
                    print(f"Unknown flag: -{ch}", file=sys.stderr)
                    raise SystemExit(2)
        elif arg.startswith("-"):
            print(f"Unknown flag: {arg}", file=sys.stderr)
            raise SystemExit(2)
        else:
            distros.append(arg)

    if expect_category:
        print("Error: --category requires a value.", file=sys.stderr)
        raise SystemExit(2)
    if expect_threshold:
        print("Error: --threshold requires a value.", file=sys.stderr)
        raise SystemExit(2)
    if expect_similarity:
        print("Error: --similarity requires a value.", file=sys.stderr)
        raise SystemExit(2)
    if options["compare_jobs"] and module_filters:
        print("Error: --compare-jobs cannot be combined with -d, -r, or -t.", file=sys.stderr)
        raise SystemExit(2)
    if similarity_given and not options["compare_jobs"]:
        print("Error: --similarity requires --compare-jobs.", file=sys.stderr)
        raise SystemExit(2)
    if options["identical_only"] and not options["compare_jobs"]:
        print("Error: --identical-only requires --compare-jobs (-j).", file=sys.stderr)
        raise SystemExit(2)

    return options, distros, categories


def discover_distros() -> list[str]:
    """Find distro directories under maps/ (excluding *-jobs dirs)."""
    maps = REPO_ROOT / "maps"
    distros = []
    for d in sorted(maps.iterdir()):
        if d.is_dir() and not d.name.endswith("-jobs"):
            if list(d.glob("*.adoc")):
                distros.append(d.name)
    return distros


def scan_job_for_modules(job_path: Path) -> list[str]:
    """Return list of module paths included in this job file (preserves duplicates)."""
    if not job_path.exists():
        return []

    try:
        text = job_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: could not read {job_path}: {e}", file=sys.stderr)
        return []

    modules = []
    for match in INCLUDE_RE.finditer(text):
        ref = match.group(1).strip()
        if MODULE_RE.match(ref):
            modules.append(ref)

    return modules


def audit_category(
    distro: str,
    category_file: Path,
    options: dict,
) -> dict[str, dict]:
    """Audit one category file for module usage.

    Returns {module_path: {"total": N, "jobs": {job_name: count}}}
    """
    maps = REPO_ROOT / "maps"

    if not category_file.exists():
        return {}

    try:
        text = category_file.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: could not read {category_file}: {e}", file=sys.stderr)
        return {}

    # Find all job includes in this category
    job_includes: list[str] = []
    for match in INCLUDE_RE.finditer(text):
        ref = match.group(1).strip()
        m = JOBS_DIR_RE.match(ref)
        if m:
            job_includes.append(ref)

    if not job_includes:
        return {}

    # Track module usage: {module_path: {job_name: count}}
    module_usage: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    # Scan each job for module includes
    for job_ref in job_includes:
        job_path = maps / job_ref
        modules = scan_job_for_modules(job_path)

        for module in modules:
            module_usage[module][job_ref] += 1

    # Convert to final format with totals
    result = {}
    for module, job_counts in module_usage.items():
        total = sum(job_counts.values())
        result[module] = {
            "total": total,
            "jobs": dict(job_counts),
        }

    return result


def read_include_targets(path: Path) -> set[str] | None:
    """Read direct include targets, excluding line and block comments.

    This is a source comparison, not an AsciiDoc render: include attributes and
    conditionals are deliberately not interpreted. None means the read failed.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Warning: could not read {path}: {error}", file=sys.stderr)
        return None

    targets = set()
    in_comment = False
    for line in text.splitlines():
        if line.strip() == "////":
            in_comment = not in_comment
            continue
        if in_comment:
            continue
        match = INCLUDE_RE.match(line)
        if match:
            targets.add(match.group(1).strip())
    return targets


def report_job_comparisons(distro: str, categories: list[Path], options: dict) -> None:
    """Report matching job pairs separately for each category."""
    print(f"\n{'=' * 80}\n  Job include comparison: {distro}\n{'=' * 80}")
    print("  Direct target sets; order, repetitions, and include attributes ignored.")
    print("  Nested jobs are not expanded; conditionals are not evaluated.")
    print("  Matching include paths do not guarantee identical rendered content.")
    print("  Check conditional includes before removing either job.")
    if options["identical_only"]:
        print("  Filter: identical target sets only.")
    else:
        print(f"  Similarity cutoff: {options['similarity']}%; identical/contained pairs always included.")

    cache: dict[str, set[str] | None] = {}
    for category in categories:
        targets = read_include_targets(category)
        if targets is None:
            continue
        jobs = {}
        for ref in sorted(targets):
            if not JOBS_DIR_RE.match(ref):
                continue
            if ref not in cache:
                cache[ref] = read_include_targets(REPO_ROOT / "maps" / ref)
            if cache[ref]:
                jobs[ref] = cache[ref]
        matches = compare_job_includes(jobs, options["similarity"])
        if options["identical_only"]:
            matches = [match for match in matches if match["kind"] == "IDENTICAL"]
        print(f"\n  ── {distro}/{category.stem} ──")
        counts = Counter(match["kind"] for match in matches)
        if options["identical_only"]:
            print(f"     Identical: {counts['IDENTICAL']} job pairs")
        else:
            print(f"     Identical: {counts['IDENTICAL']}; fully contained: {counts['CONTAINED']}; "
                  f"similar: {counts['SIMILAR']} job pairs")
        if not matches:
            print("     No matching job pairs.")
        if options["summary_only"]:
            continue
        for match in matches:
            print(f"\n     [{match['kind']}] {match['similarity']:.1f}% similarity")
            print(f"       A: {match['a']} ({len(jobs[match['a']])} targets)")
            print(f"       B: {match['b']} ({len(jobs[match['b']])} targets)")
            if match["kind"] == "CONTAINED":
                print("       All A targets are included in B.")
            for label, key in (("Shared", "shared"), ("Only A", "only_a"), ("Only B", "only_b")):
                targets = sorted(match[key])
                print(f"       {label} ({len(targets)}):" + (" none" if not targets else ""))
                for target in targets:
                    print(f"         {target}")


def audit_distro(
    distro: str,
    options: dict,
    category_filter: list[str] | None = None,
) -> None:
    """Audit one distro and print its report."""
    maps = REPO_ROOT / "maps"
    distro_dir = maps / distro

    if not distro_dir.is_dir():
        print(f"Error: {distro_dir} does not exist.", file=sys.stderr)
        return

    category_files = sorted(
        p for p in distro_dir.glob("*.adoc") if p.name != "navigation.adoc"
    )

    if category_filter:
        category_files = [p for p in category_files if p.name in category_filter]
        if not category_files:
            names = ", ".join(category_filter)
            print(f"No matching category files for [{names}] in {distro_dir}.",
                  file=sys.stderr)
            return

    if not category_files:
        print(f"No category .adoc files found in {distro_dir}.", file=sys.stderr)
        return

    if options["compare_jobs"]:
        report_job_comparisons(distro, category_files, options)
        return

    # Collect module usage across all categories
    all_results: dict[str, dict[str, dict]] = {}  # {category_name: {module: data}}

    for cat_file in category_files:
        result = audit_category(distro, cat_file, options)
        if result:
            all_results[cat_file.name] = result

    if not all_results:
        print(f"\n  {distro}: no module includes found in job files.")
        return

    # --- Report header ---
    print(f"\n{'=' * 80}")
    title = f"Module usage report: {distro}"
    if category_filter:
        title += f" (categories: {', '.join(c.removesuffix('.adoc') for c in category_filter)})"
    print(f"  {title}")
    print(f"{'=' * 80}")

    threshold = options["threshold"]
    duplicates_only = options["duplicates_only"]
    redundant_only = options["redundant_only"]
    summary_only = options["summary_only"]

    # Process each category
    for category_name in sorted(all_results.keys()):
        module_data = all_results[category_name]

        # Filter based on options
        filtered_modules = {}
        for module, data in module_data.items():
            total = data["total"]
            job_counts = data["jobs"]

            # Check threshold
            if total < threshold:
                continue

            # Check duplicates_only: module appears 2+ times in at least one job
            if duplicates_only:
                if not any(count >= 2 for count in job_counts.values()):
                    continue

            # Check redundant_only: module appears in 2+ different jobs
            if redundant_only:
                if len(job_counts) < 2:
                    continue

            filtered_modules[module] = data

        if not filtered_modules:
            continue

        # Category header
        print(f"\n  ── {distro}/{category_name.removesuffix('.adoc')} ──")

        if summary_only:
            # Just show counts
            total_modules = len(filtered_modules)
            total_appearances = sum(d["total"] for d in filtered_modules.values())
            duplicates = sum(
                1 for d in filtered_modules.values()
                if any(c >= 2 for c in d["jobs"].values())
            )
            cross_job = sum(
                1 for d in filtered_modules.values()
                if len(d["jobs"]) >= 2
            )

            print(f"     Modules with {threshold}+ appearances: {total_modules}")
            print(f"     Total module appearances: {total_appearances}")
            print(f"     Modules with duplicates in same job: {duplicates}")
            print(f"     Modules appearing in 2+ jobs: {cross_job}")
        else:
            # Detailed listing
            print(f"\n     {'Module':<60} {'Total':>5}  Jobs")
            print(f"     {'-' * 60} {'-' * 5}  {'-' * 40}")

            # Sort by total count descending
            sorted_modules = sorted(
                filtered_modules.items(),
                key=lambda x: (-x[1]["total"], x[0])
            )

            for module, data in sorted_modules:
                total = data["total"]
                job_counts = data["jobs"]

                # Determine if this is a duplicate or cross-job redundancy
                has_duplicates = any(c >= 2 for c in job_counts.values())
                is_cross_job = len(job_counts) >= 2

                marker = ""
                if has_duplicates and is_cross_job:
                    marker = " [DUP+CROSS]"
                elif has_duplicates:
                    marker = " [DUP]"
                elif is_cross_job:
                    marker = " [CROSS]"

                print(f"     {module:<60} {total:>5}{marker}")

                # Show job breakdown
                for job_ref, count in sorted(job_counts.items()):
                    indent = " " * 7
                    count_str = f"(x{count})" if count > 1 else ""
                    print(f"{indent}└─ {job_ref} {count_str}")


def main() -> int:
    maps = REPO_ROOT / "maps"
    if not maps.is_dir():
        print("Error: run from the repository root (maps/ not found).", file=sys.stderr)
        return 1

    options, distros, categories = parse_args(sys.argv)

    if not distros:
        distros = discover_distros()
    if not distros:
        print("No distro directories found under maps/.", file=sys.stderr)
        return 1

    cat_filter = categories or None

    for distro in distros:
        audit_distro(distro, options, cat_filter)

    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
