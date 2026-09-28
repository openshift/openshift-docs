#!/usr/bin/env python3
"""Report which jobs are mapped to categories and which are unmapped.

Scans category .adoc files under maps/<distro>/ for include directives that
reference jobs from any *-jobs/ directory, then produces a coverage report.

A distro's categories may reference multiple job pools (e.g. hcm-jobs and
ocp-jobs).  The script auto-discovers which pools are used.

Usage:
    python3 scripts/navmap/audit-map-jobs.py [FLAGS] [DISTRO ...]

Flags (filter output — default shows all sections):
    --mapped,       -m          Show mapped jobs and their categories
    --unmapped,     -u          Show unmapped (uncategorised) jobs
    --multi,        -M          Show jobs that appear in multiple categories
    --duplicates,   -D          Show jobs included more than once in the same category
    --summary,      -s          Show only the summary table (no individual jobs)
    --category CAT, -c CAT      Filter to a specific category file (repeatable)

Flags can be combined:  -Mu  shows multi-category and unmapped jobs.
If no flags are given, all sections are shown.

Examples:
    python3 scripts/navmap/audit-map-jobs.py                  # all distros, full report
    python3 scripts/navmap/audit-map-jobs.py ocp              # OCP full report
    python3 scripts/navmap/audit-map-jobs.py -M ocp           # OCP multi-category only
    python3 scripts/navmap/audit-map-jobs.py -D rosa-hcp osd  # duplicates across distros
    python3 scripts/navmap/audit-map-jobs.py -s               # summary tables only
    python3 scripts/navmap/audit-map-jobs.py -c disconnected-environments ocp
    python3 scripts/navmap/audit-map-jobs.py -c develop -c extend ocp
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

INCLUDE_RE = re.compile(r"^include::(.+?)\[", re.MULTILINE)
JOBS_DIR_RE = re.compile(r"^([a-z][a-z0-9_-]*-jobs)/(.+)$")
REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Output sections that can be toggled
SHOW_MAPPED = "mapped"
SHOW_UNMAPPED = "unmapped"
SHOW_MULTI = "multi"
SHOW_DUPLICATES = "duplicates"
SHOW_SUMMARY = "summary"


def parse_args(argv: list[str]) -> tuple[set[str], list[str], list[str]]:
    """Parse flags, category filters, and distro names from argv.

    Returns (sections, distros, categories).
    """
    flag_map = {
        "-m": SHOW_MAPPED, "--mapped": SHOW_MAPPED,
        "-u": SHOW_UNMAPPED, "--unmapped": SHOW_UNMAPPED,
        "-M": SHOW_MULTI, "--multi": SHOW_MULTI,
        "-D": SHOW_DUPLICATES, "--duplicates": SHOW_DUPLICATES,
        "-s": SHOW_SUMMARY, "--summary": SHOW_SUMMARY,
        "-h": "help", "--help": "help",
    }

    sections: set[str] = set()
    distros: list[str] = []
    categories: list[str] = []
    expect_category = False

    for arg in argv[1:]:
        if expect_category:
            cat = arg if arg.endswith(".adoc") else f"{arg}.adoc"
            categories.append(cat)
            expect_category = False
            continue

        if arg in ("-c", "--category"):
            expect_category = True
            continue

        if arg.startswith("-") and not arg.startswith("--") and len(arg) > 2:
            for i, ch in enumerate(arg[1:]):
                flag = f"-{ch}"
                if flag == "-c":
                    # -c embedded in combined flags: rest of string is not category
                    # just set expect_category for next argv
                    expect_category = True
                elif flag in flag_map:
                    sections.add(flag_map[flag])
                else:
                    print(f"Unknown flag: {flag}", file=sys.stderr)
                    sections.add("help")
        elif arg in flag_map:
            sections.add(flag_map[arg])
        else:
            distros.append(arg)

    if expect_category:
        print("Error: --category requires a value.", file=sys.stderr)
        raise SystemExit(2)

    if "help" in sections:
        print(__doc__)
        raise SystemExit(0)

    if not sections:
        sections = {SHOW_MAPPED, SHOW_UNMAPPED, SHOW_MULTI, SHOW_DUPLICATES, SHOW_SUMMARY}

    sections.add(SHOW_SUMMARY)

    return sections, distros, categories


def discover_distros() -> list[str]:
    """Find distro directories under maps/ (excluding *-jobs dirs)."""
    maps = REPO_ROOT / "maps"
    distros = []
    for d in sorted(maps.iterdir()):
        if d.is_dir() and not d.name.endswith("-jobs"):
            if list(d.glob("*.adoc")):
                distros.append(d.name)
    return distros


def collect_job_pools(maps: Path) -> dict[str, set[str]]:
    """Return {pool_name: set of job filenames} for every *-jobs dir."""
    pools: dict[str, set[str]] = {}
    for d in sorted(maps.iterdir()):
        if d.is_dir() and d.name.endswith("-jobs"):
            jobs = {p.name for p in d.glob("*.adoc")}
            if jobs:
                pools[d.name] = jobs
    return pools


def audit_distro(
    distro: str,
    all_pools: dict[str, set[str]],
    sections: set[str],
    category_filter: list[str] | None = None,
) -> dict[str, tuple[int, int]]:
    """Audit one distro and print its report.

    Returns {pool_name: (mapped_count, total_count)} for pools referenced.
    """
    maps = REPO_ROOT / "maps"
    distro_dir = maps / distro

    if not distro_dir.is_dir():
        print(f"Error: {distro_dir} does not exist.", file=sys.stderr)
        return {}

    category_files = sorted(
        p for p in distro_dir.glob("*.adoc") if p.name != "navigation.adoc"
    )

    if category_filter:
        category_files = [p for p in category_files if p.name in category_filter]
        if not category_files:
            names = ", ".join(category_filter)
            print(f"No matching category files for [{names}] in {distro_dir}.",
                  file=sys.stderr)
            return {}

    if not category_files:
        print(f"No category .adoc files found in {distro_dir}.", file=sys.stderr)
        return {}

    # job_key (pool/filename) -> list of category filenames (preserves dupes)
    job_to_categories: dict[str, list[str]] = defaultdict(list)
    referenced_pools: set[str] = set()

    for cat_file in category_files:
        text = cat_file.read_text(encoding="utf-8", errors="replace")
        for match in INCLUDE_RE.finditer(text):
            ref = match.group(1).strip()
            m = JOBS_DIR_RE.match(ref)
            if m:
                pool_name, job_file = m.group(1), m.group(2)
                referenced_pools.add(pool_name)
                job_to_categories[f"{pool_name}/{job_file}"].append(cat_file.name)

    if not referenced_pools:
        print(f"\n  {distro}: no *-jobs/ includes found in category files.")
        return {}

    # --- Report header ---
    print(f"\n{'=' * 72}")
    title = f"Job coverage report: {distro}"
    if category_filter:
        title += f" (categories: {', '.join(c.removesuffix('.adoc') for c in category_filter)})"
    print(f"  {title}")
    print(f"{'=' * 72}")
    print(f"  Job pools referenced: {', '.join(sorted(referenced_pools))}")

    pool_results: dict[str, tuple[int, int]] = {}

    for pool_name in sorted(referenced_pools):
        pool_jobs = all_pools.get(pool_name, set())
        if not pool_jobs:
            print(f"\n  WARNING: {pool_name}/ directory not found or empty.")
            continue

        mapped_in_pool = {
            k.split("/", 1)[1]
            for k in job_to_categories
            if k.startswith(f"{pool_name}/") and k.split("/", 1)[1] in pool_jobs
        }
        unmapped_in_pool = sorted(pool_jobs - mapped_in_pool)

        pool_results[pool_name] = (len(mapped_in_pool), len(pool_jobs))

        # --- Summary (always shown) ---
        print(f"\n  ── {pool_name} ({len(mapped_in_pool)}/{len(pool_jobs)} mapped, "
              f"{len(unmapped_in_pool)} unmapped, "
              f"{len(mapped_in_pool) * 100 // len(pool_jobs)}% coverage) ──")

        cat_to_jobs: dict[str, list[str]] = defaultdict(list)
        for key, cats in sorted(job_to_categories.items()):
            if not key.startswith(f"{pool_name}/"):
                continue
            job_file = key.split("/", 1)[1]
            for cat in cats:
                cat_to_jobs[cat].append(job_file)

        if cat_to_jobs and SHOW_SUMMARY in sections:
            print(f"\n  {'Category':<40} {'Jobs':>5}")
            print(f"  {'-' * 40} {'-' * 5}")
            for cat in sorted(cat_to_jobs, key=lambda c: -len(cat_to_jobs[c])):
                print(f"  {distro}/{cat:<39} {len(cat_to_jobs[cat]):>5}")

        # --- Mapped jobs ---
        if SHOW_MAPPED in sections and mapped_in_pool:
            print(f"\n  Mapped jobs ({len(mapped_in_pool)}):")
            for job_file in sorted(mapped_in_pool):
                key = f"{pool_name}/{job_file}"
                cats = job_to_categories[key]
                unique_cats = sorted(set(cats))
                targets = ", ".join(f"{distro}/{c}" for c in unique_cats)
                print(f"    {pool_name}/{job_file:<55} -> {targets}")

        # --- Multi-category jobs ---
        if SHOW_MULTI in sections:
            multi = {
                k: v for k, v in job_to_categories.items()
                if k.startswith(f"{pool_name}/")
                and len(set(v)) > 1
                and k.split("/", 1)[1] in pool_jobs
            }
            if multi:
                print(f"\n  Jobs in multiple categories ({len(multi)}):")
                for key in sorted(multi):
                    unique_cats = sorted(set(multi[key]))
                    cats_str = ", ".join(f"{distro}/{c}" for c in unique_cats)
                    job_file = key.split("/", 1)[1]
                    print(f"    {pool_name}/{job_file:<55} -> {cats_str}")
            elif sections == {SHOW_MULTI, SHOW_SUMMARY}:
                print(f"\n  No jobs appear in multiple categories.")

        # --- Duplicate jobs (same job included >1 time in the same category) ---
        if SHOW_DUPLICATES in sections:
            dupes: list[tuple[str, str, int]] = []
            for key, cats in job_to_categories.items():
                if not key.startswith(f"{pool_name}/"):
                    continue
                job_file = key.split("/", 1)[1]
                if job_file not in pool_jobs:
                    continue
                counts = Counter(cats)
                for cat, count in counts.items():
                    if count > 1:
                        dupes.append((job_file, cat, count))

            if dupes:
                dupes.sort()
                print(f"\n  Duplicate includes ({len(dupes)} "
                      f"job{'s' if len(dupes) != 1 else ''} included multiple "
                      f"times in the same category):")
                for job_file, cat, count in dupes:
                    print(f"    {pool_name}/{job_file:<55}  "
                          f"{distro}/{cat} (x{count})")
            elif sections == {SHOW_DUPLICATES, SHOW_SUMMARY}:
                print(f"\n  No duplicate includes found.")

        # --- Unmapped jobs ---
        if SHOW_UNMAPPED in sections and unmapped_in_pool:
            print(f"\n  Unmapped jobs ({len(unmapped_in_pool)}):")
            for job_file in unmapped_in_pool:
                print(f"    {pool_name}/{job_file}")

    return pool_results


def main() -> int:
    maps = REPO_ROOT / "maps"
    if not maps.is_dir():
        print("Error: run from the repository root (maps/ not found).", file=sys.stderr)
        return 1

    sections, distros, categories = parse_args(sys.argv)
    if not distros:
        distros = discover_distros()
    if not distros:
        print("No distro directories found under maps/.", file=sys.stderr)
        return 1

    all_pools = collect_job_pools(maps)
    if not all_pools:
        print("No *-jobs/ directories found under maps/.", file=sys.stderr)
        return 1

    grand_mapped = 0
    grand_total = 0
    cat_filter = categories or None

    for distro in distros:
        pool_results = audit_distro(distro, all_pools, sections, cat_filter)
        for mapped, total in pool_results.values():
            grand_mapped += mapped
            grand_total += total

    if len(distros) > 1 and grand_total:
        print(f"\n{'=' * 72}")
        print(f"  Overall: {grand_mapped}/{grand_total} job-references mapped "
              f"({grand_mapped * 100 // grand_total}%)")
        print(f"{'=' * 72}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
