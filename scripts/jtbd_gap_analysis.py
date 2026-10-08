#!/usr/bin/env python

"""
Reports which modules used by the live documentation are not yet reachable from
the JTBD job maps.

The live documentation is enumerated by a topic map (`_topic_maps/_topic_map.yml`),
which lists assemblies. The JTBD documentation is enumerated by a navigation map
(`maps/ocp/navigation.adoc`), which includes category maps, which include job maps.
Both sides ultimately resolve to files under `modules/`, so the gap is the set
difference between them.

Run in two stages. First analyze each branch, from a worktree of that branch:

    python scripts/jtbd_gap_analysis.py analyze . --label main -o /tmp/main.json
    python scripts/jtbd_gap_analysis.py analyze ../wt-4.20 --label 4.20 -o /tmp/4.20.json

Then combine the results into CSV and Markdown reports:

    python scripts/jtbd_gap_analysis.py report /tmp/*.json --base main --outdir maps/ocp

The `report` stage classifies every gap by which branches share it, so that work
which can be done once on the base branch and backported verbatim is separated
from work that is specific to a single branch.

Includes are matched textually and conditional directives (`ifdef`, `ifeval`) are
not evaluated, so a module included only under a non-OCP condition is counted as
live. This over-reports the gap rather than under-reporting it. Commented-out
includes (`// include::`) are ignored.

Coverage is reachability, not existence: a job map that no category map includes
never reaches the navigation, so its modules are reported as a gap. Those maps
are listed separately, because wiring one in closes its part of the gap without
any mapping work.
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict

import yaml

INCLUDE = re.compile(r'^[ \t]*include::([^\[]+)\[', re.M)

DEFAULT_TOPIC_MAP = "_topic_maps/_topic_map.yml"
DEFAULT_NAVIGATION = "maps/ocp/navigation.adoc"
DEFAULT_DISTRO = "openshift-enterprise"


def read_includes(root, path):
    """Return the include targets in a file, or None if the file is absent."""
    full = os.path.join(root, path)
    if not os.path.isfile(full):
        return None
    with open(full, encoding="utf-8", errors="replace") as handle:
        return INCLUDE.findall(handle.read())


def topic_map_assemblies(root, topic_map, distro):
    """Return the assemblies the topic map publishes for a distro.

    The topic map is a multi-document YAML file of nested records. Each record
    carries a `Dir`, and either a `Topics` list of child records or a `File`
    naming an assembly under the accumulated directory path. `Distros` is
    inherited by child records unless they override it.
    """
    assemblies = []

    def walk(node, dirs, distros):
        distros = node.get("Distros", distros)
        path = dirs + ([node["Dir"]] if node.get("Dir") else [])
        if "Topics" in node:
            for topic in node["Topics"]:
                walk(topic, path, distros)
        elif node.get("File"):
            if distro in [d.strip() for d in str(distros).split(",")]:
                assemblies.append("/".join(path + [node["File"]]) + ".adoc")

    with open(os.path.join(root, topic_map), encoding="utf-8") as handle:
        for document in yaml.safe_load_all(handle):
            if document:
                walk(document, [], "")
    return assemblies


def live_modules(root, topic_map, distro):
    """Map each published assembly to the modules it includes."""
    by_assembly = {}
    missing = []
    for assembly in topic_map_assemblies(root, topic_map, distro):
        includes = read_includes(root, assembly)
        if includes is None:
            missing.append(assembly)
            continue
        by_assembly[assembly] = sorted(
            {i for i in includes if i.startswith("modules/")}
        )
    return by_assembly, missing


def job_map_modules(root, navigation):
    """Map each module reachable from the navigation map to the job maps using it.

    Walks navigation -> category maps -> job maps -> modules. Include targets are
    resolved relative to the repository root first, then relative to the including
    file, which is how Asciidoctor resolves them under the maps build.
    """
    by_module = defaultdict(set)
    missing = set()
    visited = set()

    def resolve(path, parent):
        if os.path.isfile(os.path.join(root, path)):
            return os.path.normpath(path)
        return os.path.normpath(os.path.join(os.path.dirname(parent), path))

    def walk(path, job_map):
        if path in visited:
            return
        visited.add(path)
        includes = read_includes(root, path)
        if includes is None:
            missing.add(path)
            return
        for target in includes:
            if target.startswith("modules/"):
                by_module[target].add(job_map or path)
                if not os.path.isfile(os.path.join(root, target)):
                    missing.add(target)
            elif target.endswith(".adoc") and not target.startswith("_attributes"):
                child = resolve(target, path)
                walk(child, job_map or child)

    walk(navigation, None)
    return {m: sorted(j) for m, j in by_module.items()}, sorted(missing), visited


def unreachable_maps(root, navigation, visited):
    """Return the map files that sit beside a reachable map but are not included.

    A job map only reaches the published navigation if some category map includes
    it. One that nothing includes is still a file on disk holding real includes,
    so its modules count as a gap even though the mapping work is already done.

    The candidate directories are the ones the reachable maps live in, which
    keeps this scoped to the navigation being analyzed rather than straying into
    the other distros under `maps/`. Directories outside the map tree are
    dropped, because the walk also reaches `snippets/`, which holds content
    rather than maps. Paths are canonicalized, since the map tree reaches its
    job maps through a symlink (`maps/ocp/ocp-jobs` -> `maps/ocp-jobs`) and the
    same file must not be both visited and unvisited.
    """
    base = os.path.realpath(root)

    def canon(path):
        real = os.path.realpath(os.path.join(root, path))
        return os.path.relpath(real, base)

    tree = navigation.split(os.sep)[0]
    seen = {canon(p) for p in visited}
    directories = {os.path.dirname(canon(p)) for p in visited}

    orphans = {}
    for directory in directories:
        if directory.split(os.sep)[0] != tree:
            continue
        try:
            names = os.listdir(os.path.join(base, directory))
        except OSError:
            continue
        for name in names:
            if not name.endswith(".adoc"):
                continue
            path = os.path.normpath(os.path.join(directory, name))
            if path in seen or not os.path.isfile(os.path.join(base, path)):
                continue
            includes = read_includes(base, path) or []
            modules = sorted({i for i in includes if i.startswith("modules/")})
            orphans[path] = {
                "modules": modules,
                "missing": sorted(
                    m for m in modules
                    if not os.path.isfile(os.path.join(base, m))
                ),
            }
    return orphans


def analyze(args):
    by_assembly, missing_assemblies = live_modules(
        args.root, args.topic_map, args.distro
    )
    by_module, missing_modules, visited = job_map_modules(
        args.root, args.navigation
    )
    result = {
        "label": args.label,
        "assemblies": by_assembly,
        "job_maps": by_module,
        "missing_assemblies": missing_assemblies,
        "missing_modules": missing_modules,
        "orphan_maps": unreachable_maps(args.root, args.navigation, visited),
    }
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=1, sort_keys=True)
    live = {m for mods in by_assembly.values() for m in mods}
    gap = live - set(by_module)
    stranded = {m for o in result["orphan_maps"].values() for m in o["modules"]}
    print(
        "%s: %d assemblies, %d live modules, %d in job maps, %d gap "
        "(%d of it in %d unreachable maps)"
        % (
            args.label,
            len(by_assembly),
            len(live),
            len(by_module),
            len(gap),
            len(gap & stranded),
            len(result["orphan_maps"]),
        ),
        file=sys.stderr,
    )


def gap_set(data):
    """Modules the live docs use that no job map includes."""
    live = {m for mods in data["assemblies"].values() for m in mods}
    return live - set(data["job_maps"])


def assembly_rows(data, gap, universal=None):
    """One row per assembly that has at least one module in `gap`."""
    rows = []
    for assembly, modules in sorted(data["assemblies"].items()):
        uncovered = sorted(set(modules) & gap)
        if not uncovered:
            continue
        if universal is None:
            shared = ""
        elif all(m in universal for m in uncovered):
            shared = "yes"
        elif any(m in universal for m in uncovered):
            shared = "partial"
        else:
            shared = "no"
        rows.append(
            {
                "source_assembly": assembly,
                "docs_dir": assembly.split("/")[0],
                "total_modules": len(modules),
                "uncovered": len(uncovered),
                "coverage": "%d%%"
                % round(100 * (len(modules) - len(uncovered)) / len(modules)),
                "all_branches": shared,
            }
        )
    rows.sort(key=lambda r: (-r["uncovered"], r["source_assembly"]))
    return rows


ROLLUP_FIELDS = [
    "source_assembly",
    "docs_dir",
    "total_modules",
    "uncovered",
    "coverage",
    "all_branches",
]

DETAIL_FIELDS = [
    "module",
    "source_assembly",
    "docs_dir",
    "gap_branch_count",
    "gap_on",
    "all_branches",
]


def write_csv(path, rows, fields):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def detail_rows(branches, gaps, labels):
    """One row per (module, source assembly), with the branches it is a gap on.

    Covers the union of every branch's gap, so a module that is only a gap on an
    older branch still appears. The assembly a module belongs to is taken from
    the first branch that publishes it, preferring the base branch.
    """
    everywhere = set.union(*gaps.values())
    owners = defaultdict(set)
    for label in labels:
        for assembly, modules in branches[label]["assemblies"].items():
            for module in modules:
                if module in everywhere:
                    owners[module].add(assembly)

    rows = []
    for module in sorted(everywhere):
        gap_on = [l for l in labels if module in gaps[l]]
        for assembly in sorted(owners[module]) or [""]:
            rows.append(
                {
                    "module": module,
                    "source_assembly": assembly,
                    "docs_dir": assembly.split("/")[0] if assembly else "",
                    "gap_branch_count": len(gap_on),
                    "gap_on": ";".join(gap_on),
                    "all_branches": "yes" if len(gap_on) == len(labels) else "no",
                }
            )
    rows.sort(key=lambda r: (-r["gap_branch_count"], r["source_assembly"],
                             r["module"]))
    return rows


def report(args):
    branches = {}
    for path in args.results:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        branches[data["label"]] = data
    if args.base not in branches:
        sys.exit("no results for base branch %r; got %s"
                 % (args.base, ", ".join(sorted(branches))))

    gaps = {label: gap_set(data) for label, data in branches.items()}
    universal = set.intersection(*gaps.values())
    others = sorted(l for l in branches if l != args.base)

    os.makedirs(args.outdir, exist_ok=True)
    written = []

    base_rows = assembly_rows(branches[args.base], gaps[args.base], universal)
    base_csv = os.path.join(args.outdir, "gap_analysis_%s.csv" % args.base)
    write_csv(base_csv, base_rows, ROLLUP_FIELDS)
    written.append(base_csv)

    unique = {}
    for label in sorted(branches):
        elsewhere = set.union(*[gaps[l] for l in branches if l != label])
        unique[label] = gaps[label] - elsewhere
        if label == args.base:
            continue
        rows = assembly_rows(branches[label], unique[label])
        path = os.path.join(args.outdir, "gap_analysis_%s_unique.csv" % label)
        write_csv(path, rows, ROLLUP_FIELDS)
        written.append(path)

    detail_csv = os.path.join(args.outdir, "gap_analysis_modules.csv")
    write_csv(detail_csv,
              detail_rows(branches, gaps, [args.base] + others),
              DETAIL_FIELDS)
    written.append(detail_csv)

    summary = os.path.join(args.outdir, "gap_analysis_summary.md")
    with open(summary, "w", encoding="utf-8") as handle:
        write_summary(handle, args.base, others, branches, gaps, universal,
                      unique, base_rows)
    written.append(summary)

    for path in written:
        print(path)


def write_unreachable(out, base, data, gap):
    """Report job maps that exist on disk but no category map includes."""
    orphans = data.get("orphan_maps") or {}
    stranded = {m for o in orphans.values() for m in o["modules"]} & gap

    out.write("\n## Job maps not reachable from the navigation map\n\n")
    out.write(
        "The gap is measured against what the navigation map reaches, so a job "
        "map that no category map includes does not count as coverage. Its "
        "modules are reported as uncovered even though the mapping work is "
        "already done. Wiring one of these in, or deleting it as superseded, is "
        "cheaper than mapping its modules from scratch, so check this list "
        "before starting on a directory in the table above.\n\n"
    )
    if not orphans:
        out.write("None on `%s`. Every map beside a reachable map is included by "
                  "one.\n" % base)
        return
    out.write(
        "`Gap modules` is how many of the map's modules the report currently "
        "counts as uncovered, which is what wiring it in would close. A map with "
        "`0` is fully redundant with what the navigation already reaches.\n\n"
    )
    out.write("On `%s`: %d maps, holding %d of the %d gap modules.\n\n"
              % (base, len(orphans), len(stranded), len(gap)))
    out.write("| Map | Modules | Gap modules | Broken includes |\n")
    out.write("| --- | ---: | ---: | ---: |\n")
    for path in sorted(orphans, key=lambda p: (-len(set(orphans[p]["modules"]) & gap), p)):
        info = orphans[path]
        out.write("| `%s` | %d | %d | %d |\n"
                  % (path, len(info["modules"]),
                     len(set(info["modules"]) & gap), len(info["missing"])))

    broken = {p: i["missing"] for p, i in orphans.items() if i["missing"]}
    if broken:
        out.write(
            "\nThe broken includes above are not in the section before this one, "
            "because that section only sees maps the navigation reaches. Each one "
            "fails the build the moment the map is wired in.\n\n"
        )
        for path in sorted(broken):
            out.write("- `%s`\n" % path)
            for module in broken[path]:
                out.write("  - `%s`\n" % module)


def write_summary(out, base, others, branches, gaps, universal, unique, base_rows):
    labels = [base] + others
    backport_ready = [r for r in base_rows if r["all_branches"] == "yes"]

    out.write("# JTBD job map gap analysis\n\n")
    out.write(
        "Modules used by the live documentation that no job map includes. "
        "Generated by `scripts/jtbd_gap_analysis.py`.\n\n"
    )

    out.write("## The files\n\n")
    out.write(
        "| File | One row is | Use it to |\n| --- | --- | --- |\n"
        "| `gap_analysis_%s.csv` | an assembly with uncovered modules | "
        "pick what to map next |\n"
        "| `gap_analysis_<branch>_unique.csv` | an assembly whose gap exists "
        "only on that branch | find branch-specific work |\n"
        "| `gap_analysis_modules.csv` | a module, per assembly that includes it | "
        "look up one module, or filter to a directory |\n\n" % base
    )
    out.write("Start with `gap_analysis_%s.csv`. Sort by `uncovered` "
              "descending for the biggest wins, or by `coverage` ascending for "
              "the least-touched areas. Filter `all_branches` to `yes` for work "
              "that backports verbatim.\n\n" % base)
    out.write(
        "The two are joinable on `source_assembly`: find an assembly worth "
        "mapping in the rollup, then filter `gap_analysis_modules.csv` to that "
        "assembly for the module list to put in the job map.\n\n"
    )
    out.write("Column meanings:\n\n")
    out.write(
        "- `total_modules` / `uncovered` — modules the assembly includes, and "
        "how many no job map reachable from the navigation map has picked up. A "
        "module sitting in a job map that no category includes counts as "
        "uncovered; see `Job maps not reachable from the navigation map` below.\n"
        "- `coverage` — the share already in a job map. `0%%` means the assembly "
        "has not been touched at all.\n"
        "- `all_branches` — `yes` if every uncovered module in the row is also a "
        "gap on every branch, so mapping it on `%s` backports verbatim. "
        "`partial` means some modules are newer than the oldest branch. `no` "
        "means none of them are shared.\n"
        "- `gap_on` / `gap_branch_count` — which branches a module is missing "
        "from, and how many.\n\n" % base
    )

    out.write("## Coverage by branch\n\n")
    out.write("| Branch | Assemblies | Live modules | In job maps | Gap | Coverage |\n")
    out.write("| --- | ---: | ---: | ---: | ---: | ---: |\n")
    for label in labels:
        data = branches[label]
        live = {m for mods in data["assemblies"].values() for m in mods}
        covered = len(live) - len(gaps[label])
        out.write(
            "| %s | %d | %d | %d | %d | %d%% |\n"
            % (label, len(data["assemblies"]), len(live), len(data["job_maps"]),
               len(gaps[label]), round(100 * covered / len(live)))
        )

    out.write("\n## Where the work splits\n\n")
    out.write(
        "- **%d modules are a gap on every branch** (%d%% of the %s gap). "
        "Map these on `%s` and backport verbatim.\n"
        % (len(universal), round(100 * len(universal) / len(gaps[base])), base, base)
    )
    out.write(
        "  - `gap_analysis_%s.csv`, rows where `all_branches` is `yes`: "
        "%d assemblies whose entire gap is shared.\n" % (base, len(backport_ready))
    )
    out.write("- Gaps unique to one branch, which need branch-specific work:\n\n")
    out.write(
        "  Counts below are distinct modules. The `uncovered` column in the CSVs "
        "sums higher, because a module included by two assemblies is a row in "
        "each.\n\n"
    )
    out.write("| Branch | Unique gap modules | Report |\n")
    out.write("| --- | ---: | --- |\n")
    for label in labels:
        report_file = ("gap_analysis_%s.csv (filter `all_branches` = `no`)" % base
                       if label == base else "gap_analysis_%s_unique.csv" % label)
        out.write("| %s | %d | %s |\n" % (label, len(unique[label]), report_file))

    out.write("\n## Gap by documentation area (%s)\n\n" % base)
    out.write(
        "Sorted by coverage, not by gap size. A large directory can show a large "
        "uncovered count and still be well covered; a directory near 0% is a "
        "product area the job maps never reached, which is either real work or a "
        "scope decision to record.\n\n"
    )
    dir_live = defaultdict(set)
    dir_gap = defaultdict(set)
    for assembly, modules in branches[base]["assemblies"].items():
        area = assembly.split("/")[0]
        dir_live[area].update(modules)
        dir_gap[area].update(set(modules) & gaps[base])
    out.write("| Directory | Live modules | Uncovered | Coverage |\n")
    out.write("| --- | ---: | ---: | ---: |\n")
    areas = [a for a in dir_live if dir_gap[a]]
    for area in sorted(areas, key=lambda a: (len(dir_gap[a]) / len(dir_live[a]),
                                             -len(dir_gap[a])), reverse=True):
        live, uncovered = len(dir_live[area]), len(dir_gap[area])
        out.write("| `%s` | %d | %d | %d%% |\n"
                  % (area, live, uncovered, round(100 * (live - uncovered) / live)))

    broken = {l: branches[l]["missing_modules"] for l in labels
              if branches[l]["missing_modules"]}
    out.write("\n## Broken includes in job maps\n\n")
    if not broken:
        out.write("None. Every module a job map includes exists on its branch.\n")
    else:
        out.write(
            "Job maps that include a module which does not exist on that branch. "
            "Asciidoctor reports these as `include file not found`, and the "
            "validation build runs with `--failure-level WARN`, so each one fails "
            "the build. Remove or comment out the include.\n\n"
        )
        for label, modules in broken.items():
            out.write("\n### %s (%d)\n\n" % (label, len(modules)))
            for module in modules:
                out.write("- `%s`\n" % module)

    write_unreachable(out, base, branches[base], gaps[base])

    orphan = {l: sorted(set(branches[l]["job_maps"]) -
                        {m for mods in branches[l]["assemblies"].values() for m in mods})
              for l in labels}
    out.write("\n## Modules in job maps but not in the live docs\n\n")
    out.write(
        "Expected to be non-zero: job maps introduce their own intro and concept "
        "modules. A branch that is much higher than the others is carrying content "
        "its topic map has dropped.\n\n"
    )
    out.write("| Branch | Modules |\n| --- | ---: |\n")
    for label in labels:
        out.write("| %s | %d |\n" % (label, len(orphan[label])))

    out.write("\n## Regenerating\n\n")
    out.write("```\n")
    for label in others:
        out.write("git worktree add --detach /tmp/jtbd-gap/%s upstream/enterprise-%s\n"
                  % (label, label))
    out.write("\npython scripts/jtbd_gap_analysis.py analyze . --label %s \\\n"
              "    -o /tmp/jtbd-gap/%s.json\n" % (base, base))
    for label in others:
        out.write("python scripts/jtbd_gap_analysis.py analyze /tmp/jtbd-gap/%s "
                  "--label %s \\\n    -o /tmp/jtbd-gap/%s.json\n"
                  % (label, label, label))
    out.write("\npython scripts/jtbd_gap_analysis.py report /tmp/jtbd-gap/*.json \\\n"
              "    --base %s --outdir maps/ocp\n" % base)
    out.write("```\n\n")
    out.write(
        "Includes are matched textually; `ifdef` and `ifeval` are not evaluated, so "
        "a module included only under a non-OCP condition counts as live. The gap is "
        "over-reported rather than under-reported.\n"
    )


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subcommands = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subcommands.add_parser(
        "analyze", help="resolve one branch's live and job map modules to JSON"
    )
    analyze_parser.add_argument("root", help="path to the root of the repository")
    analyze_parser.add_argument("--label", required=True, help="branch name")
    analyze_parser.add_argument("-o", "--output", required=True, help="JSON output")
    analyze_parser.add_argument("--topic-map", default=DEFAULT_TOPIC_MAP)
    analyze_parser.add_argument("--navigation", default=DEFAULT_NAVIGATION)
    analyze_parser.add_argument("--distro", default=DEFAULT_DISTRO)
    analyze_parser.set_defaults(func=analyze)

    report_parser = subcommands.add_parser(
        "report", help="combine analyze results into CSV and Markdown reports"
    )
    report_parser.add_argument("results", nargs="+", help="JSON files from analyze")
    report_parser.add_argument("--base", default="main", help="branch to map first")
    report_parser.add_argument("--outdir", default="maps/ocp")
    report_parser.set_defaults(func=report)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
