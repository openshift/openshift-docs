#!/usr/bin/env python3

# Converts AsciiDoc path-based xrefs (xref:../f.adoc#id[Text]) to ID-based xrefs
# (xref:id[Text]), in preparation for AEM/DITA migration.
#
# The string rewrite is the same for every file: drop the path, keep the bare id.
# What differs is WHICH files are edited and HOW the uniqueness scope is computed,
# so there are two classifiers selected by --target:
#
#   assembly : edits ASSEMBLY .adoc files; an id is safe if it is unique within the
#              assembly's own BOOK (top-level directory). Assemblies live in the
#              legacy book tree and are not referenced by /maps.
#   module   : edits modules/*.adoc; an id is safe if, within every CATEGORY the
#              source module belongs to (read from /maps: category map -> job map ->
#              module), the id resolves to exactly one file. Modules are what /maps
#              composes, so their migrated scope is the category.
#
# After migration AEM resolves a reference by file GUID within its map, so within-
# scope uniqueness is the proxy for "binds to exactly one GUID". Ambiguous,
# anchorless, or broken-{context} xrefs are left untouched and reported.
# See XREF-CONVERSION.md. Run with -h for usage.

from __future__ import annotations

import argparse
import collections
import difflib
import os
import re
import subprocess
import sys
from dataclasses import dataclass

ASSEMBLY_MARK = ":_mod-docs-content-type: ASSEMBLY"
MODULES_DIR = "modules"
MAPS_DIR = "maps"

# Directories with no convertible source / that must not seed the id or target index.
# drupal-build is git-ignored generated output; its duplicate id definitions would
# create phantom collisions.
SKIP_TOP_DIRS = {".git", "xref-migration", "_attributes", "snippets", "drupal-build"}

# Directories under maps/ that hold job maps (not category maps).
JOB_MAP_DIRS = {"ocp-jobs", "osd-jobs", "hcm-jobs", "virt-jobs", "rosa-hcp-jobs",
                "rosa-classic-jobs", "microshift-jobs", "jobs"}

# A category nested under another (install umbrella): a module in both is not a
# cross-category case. Keys and values are category file basenames without .adoc.
NESTED_CATEGORIES = {"disconnected-environments": "install"}

PATH_ANCHOR_RE = re.compile(r"xref:([^#\[\s]+\.adoc)#([^\[\]]+)\[")
PATH_NOANCHOR_RE = re.compile(r"xref:([^#\[\s]+\.adoc)\[")
INCLUDE_RE = re.compile(r"include::([^\[]+)\[")

FRAG_LEN = 160


@dataclass(frozen=True)
class Xref:
    """A single path-based xref occurrence found in a source file."""

    src: str
    line: int
    path: str
    anchor: str
    fragment: str

    @property
    def old_text(self):
        """The exact substring to replace: 'xref:<path>#<anchor>['."""
        return f"xref:{self.path}#{self.anchor}["

    @property
    def new_text(self):
        """The converted form: 'xref:<anchor>['."""
        return f"xref:{self.anchor}["


def read_text(path):
    """Returns the file contents, or an empty string if it cannot be read."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def top_dir(root, abspath):
    """Returns the first path segment of abspath relative to root (its book)."""
    return os.path.relpath(abspath, root).split(os.sep)[0]


def resolve_target(src_file, rel_path):
    """Returns the normalized absolute path that rel_path points to."""
    src_dir = os.path.dirname(os.path.abspath(src_file))
    return os.path.normpath(os.path.join(src_dir, rel_path))


def all_adoc_files(root):
    """Returns every .adoc file under root, skipping SKIP_TOP_DIRS."""
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.relpath(dirpath, root).split(os.sep)[0] in SKIP_TOP_DIRS:
            dirnames[:] = []
            continue
        for name in filenames:
            if name.endswith(".adoc"):
                found.append(os.path.join(dirpath, name))
    return found


# --- file selection (differs by target) -------------------------------------

def find_assembly_files(root):
    """Returns all ASSEMBLY-type .adoc files under root, skipping SKIP_TOP_DIRS."""
    return [f for f in all_adoc_files(root)
            if ASSEMBLY_MARK in read_text(f)[:4000]]


def find_module_files(root):
    """Returns all module .adoc files under modules/."""
    modules_root = os.path.join(root, MODULES_DIR)
    return sorted(os.path.join(modules_root, name)
                  for name in os.listdir(modules_root)
                  if name.endswith(".adoc"))


# --- shared parsing ---------------------------------------------------------

def parse_xrefs(root, files):
    """Returns (path+anchor xrefs, anchorless occurrences) across the given files."""
    xrefs = []
    anchorless = []
    for src in files:
        rel = os.path.relpath(src, root)
        for line_no, line in enumerate(read_text(src).splitlines(), start=1):
            for m in PATH_ANCHOR_RE.finditer(line):
                fragment = line[m.start():m.start() + FRAG_LEN].rstrip()
                xrefs.append(Xref(src, line_no, m.group(1),
                                  m.group(2).strip(), fragment))
            for m in PATH_NOANCHOR_RE.finditer(line):
                fragment = line[m.start():m.start() + FRAG_LEN].rstrip()
                anchorless.append((rel, line_no, fragment))
    return xrefs, anchorless


# --- assembly scope: target id unique within the target's book --------------

def index_assembly_targets(root, files):
    """Returns (book, anchor) -> set of target files that xrefs resolve to.

    Built from every path+anchor xref across the repo. The book is the TARGET
    file's top-level directory.
    """
    by_book_id = {}
    for src in files:
        for m in PATH_ANCHOR_RE.finditer(read_text(src)):
            anchor = m.group(2).strip()
            if "{context}" in anchor:
                continue
            target = resolve_target(src, m.group(1))
            by_book_id.setdefault((top_dir(root, target), anchor), set()).add(target)
    return by_book_id


def classify_assembly(x, root, index):
    """Returns the outcome for one assembly xref: CLEAN, AMBIGUOUS, or BROKEN."""
    if "{context}" in x.anchor:
        return "BROKEN"
    target = resolve_target(x.src, x.path)
    book = top_dir(root, target)
    # Safe only if the target id resolves to one file in the target's book.
    if len(index.get((book, x.anchor), {target})) > 1:
        return "AMBIGUOUS"
    return "CLEAN"


# --- module scope: id unique within every /maps category of the module ------

def includes_of(map_file, maps_root):
    """Returns the include:: targets of a map file, as paths under maps_root."""
    return [os.path.normpath(os.path.join(maps_root, m.group(1).strip()))
            for m in INCLUDE_RE.finditer(read_text(map_file))]


def category_scope(category_file):
    """Returns the effective scope name for a category map, collapsing nesting."""
    name = os.path.basename(category_file)[: -len(".adoc")]
    return NESTED_CATEGORIES.get(name, name)


def build_module_index(root):
    """Returns (module_scopes, scope_id_files) describing the /maps category layout.

    module_scopes: module basename -> set of effective scope names it belongs to.
    scope_id_files: (distro, scope) -> {resolved-or-prefix id -> set of module files}.
    The id map is {context}-aware: [id="name_{context}"] is stored under prefix name_.
    """
    maps_root = os.path.join(root, MAPS_DIR)
    id_def_re = re.compile(r'\[id="([^"]+)"\]')

    def file_ids(path):
        """Resolved id or {context} prefix for each [id=] in a file."""
        ids = set()
        for declared in id_def_re.findall(read_text(path)):
            if declared.endswith("_{context}"):
                ids.add(declared[: -len("{context}")])
            else:
                ids.add(declared)
        return ids

    module_scopes = collections.defaultdict(set)
    scope_modules = collections.defaultdict(set)   # (distro, scope) -> module files
    for distro in sorted(os.listdir(maps_root)):
        distro_dir = os.path.join(maps_root, distro)
        if not os.path.isdir(distro_dir) or distro in JOB_MAP_DIRS:
            continue
        for name in sorted(os.listdir(distro_dir)):
            if not name.endswith(".adoc") or name == "navigation.adoc":
                continue
            scope = category_scope(name)
            category = os.path.join(distro_dir, name)
            for job_map in includes_of(category, maps_root):
                if not job_map.endswith(".adoc"):
                    continue
                for included in includes_of(job_map, maps_root):
                    if os.path.basename(os.path.dirname(included)) == MODULES_DIR:
                        module_scopes[os.path.basename(included)].add((distro, scope))
                        scope_modules[(distro, scope)].add(included)

    scope_id_files = {}
    for scope_key, module_files in scope_modules.items():
        id_files = {}
        for mf in module_files:
            for anchor_id in file_ids(mf):
                id_files.setdefault(anchor_id, set()).add(mf)
        scope_id_files[scope_key] = id_files
    return module_scopes, scope_id_files


def classify_module(x, index):
    """Returns the outcome for one module xref against the /maps scopes.

    Outcomes: CLEAN, AMBIGUOUS, NO_CATEGORY, MULTI_CATEGORY, or BROKEN.
    """
    module_scopes, scope_id_files = index
    if "{context}" in x.anchor:
        return "BROKEN"
    scopes = module_scopes.get(os.path.basename(x.src), set())
    # A module not reachable from any category map has no scope to validate against.
    if not scopes:
        return "NO_CATEGORY"
    # Reuse across categories within one distro may not be permitted; flag it.
    distro_scopes = collections.defaultdict(set)
    for distro, scope in scopes:
        distro_scopes[distro].add(scope)
    if any(len(s) > 1 for s in distro_scopes.values()):
        return "MULTI_CATEGORY"
    # Safe only if the id resolves to one file in each scope the module is in.
    for scope_key in scopes:
        definers = scope_id_files.get(scope_key, {})
        if _matches_multiple(x.anchor, definers):
            return "AMBIGUOUS"
    return "CLEAN"


def _matches_multiple(anchor, id_files):
    """True if the anchor matches ids defined in more than one file ({context}-aware)."""
    files = set()
    for anchor_id, defining in id_files.items():
        if anchor == anchor_id or anchor.startswith(anchor_id):
            files |= defining
    return len(files) > 1


# --- plan: classify everything into edits + report rows ---------------------

@dataclass
class Plan:
    """The edits to make and the report rows to write, for the chosen mode."""

    edits_by_file: dict
    rows: dict
    clean_count: int
    outcomes: tuple          # ordered non-CLEAN outcome names for this target


def build_plan(root, xrefs, anchorless, classifier, outcomes):
    """Classifies every xref into edits (CLEAN) and per-outcome report rows."""
    edits_by_file = {}
    rows = {name: [] for name in outcomes}
    rows["ANCHORLESS"] = []
    clean_count = 0

    for x in xrefs:
        outcome = classifier(x)
        rel = os.path.relpath(x.src, root)
        if outcome == "CLEAN":
            edits_by_file.setdefault(x.src, []).append((x.old_text, x.new_text))
            clean_count += 1
        elif outcome == "BROKEN":
            rows["BROKEN"].append(f"{rel}:{x.line}\t{x.fragment}")
        else:
            rows[outcome].append(f"{rel}:{x.line}\t{x.anchor}\t{x.fragment}")

    rows["ANCHORLESS"] = [f"{rel}:{ln}\t{frag}" for rel, ln, frag in anchorless]
    return Plan(edits_by_file, rows, clean_count, outcomes)


# --- reports ----------------------------------------------------------------

def write_report(reports_dir, filename, header, rows):
    """Writes one report file: a header block followed by its data rows."""
    with open(os.path.join(reports_dir, filename), "w") as f:
        f.write(header.rstrip() + "\n")
        f.write("".join(row + "\n" for row in rows))


# Report file + header for each outcome, per target.
REPORTS = {
    "assembly": {
        "AMBIGUOUS": ("assembly_ambiguous.txt",
                      "# Assembly xrefs whose target id is ambiguous within the target's book.\n"
                      "# HUMAN REVIEW: pick the intended target per reference."),
    },
    "module": {
        "AMBIGUOUS": ("module_ambiguous.txt",
                      "# Module xrefs whose id is defined in >1 file within a category.\n"
                      "# HUMAN REVIEW: pick the intended target per reference."),
        "MULTI_CATEGORY": ("module_multi_category.txt",
                           "# Module used across >1 category within a distro; may not be\n"
                           "# permitted. Decide the module's single category before converting."),
        "NO_CATEGORY": ("module_no_category.txt",
                        "# Module not reachable from any /maps category; no scope to\n"
                        "# validate against. Revisit once the module is mapped."),
    },
}


def write_all_reports(reports_dir, plan, target):
    """Writes every review-queue report for the target to reports_dir."""
    os.makedirs(reports_dir, exist_ok=True)
    prefix = "assembly" if target == "assembly" else "module"
    for outcome, (filename, header) in REPORTS[target].items():
        write_report(reports_dir, filename, header, plan.rows[outcome])
    write_report(reports_dir, f"{prefix}_anchorless.txt",
                 "# Anchorless path xrefs (no #anchor). Synthesize target id per case.",
                 plan.rows["ANCHORLESS"])
    write_report(reports_dir, f"{prefix}_broken_context.txt",
                 "# Literal {context} left in an anchor. Author supplies resolved value.",
                 plan.rows["BROKEN"])


# --- apply / preview --------------------------------------------------------

def rewrite_file(src, edits):
    """Returns (old_text, new_text) for src after applying edits, without writing."""
    old_text = read_text(src)
    new_text = old_text
    for old, new in dict(edits).items():
        new_text = new_text.replace(old, new)
    return old_text, new_text


def apply_plan(plan, root, write, backup):
    """Applies or previews all edits; returns (files, links, diff text)."""
    files_changed = 0
    links_changed = 0
    diff = []

    for src, edits in sorted(plan.edits_by_file.items()):
        old_text, new_text = rewrite_file(src, edits)
        if old_text == new_text:
            continue
        files_changed += 1
        links_changed += len(dict(edits))
        if write:
            if backup:
                with open(src + ".bak", "w", encoding="utf-8") as f:
                    f.write(old_text)
            with open(src, "w", encoding="utf-8") as f:
                f.write(new_text)
        else:
            rel = os.path.relpath(src, root)
            diff += difflib.unified_diff(old_text.splitlines(keepends=True),
                                         new_text.splitlines(keepends=True),
                                         fromfile=f"a/{rel}", tofile=f"b/{rel}")
    return files_changed, links_changed, "".join(diff)


# --- summary ----------------------------------------------------------------

# Human-readable label for each non-CLEAN outcome in the summary.
OUTCOME_LABELS = {
    "AMBIGUOUS": "ambiguous in scope",
    "MULTI_CATEGORY": "multi-category (review)",
    "NO_CATEGORY": "no category (unmapped)",
    "BROKEN": "broken {context}",
}


def print_summary(plan, target, file_count, mode, files_changed, links_changed):
    """Prints the classification summary and the result of the chosen mode."""
    r = plan.rows
    counts = [(f"{target} files scanned", file_count),
              ("CLEAN (convertible)", plan.clean_count)]
    for outcome in plan.outcomes:
        counts.append((OUTCOME_LABELS.get(outcome, outcome.lower()), len(r[outcome])))
    counts.append(("anchorless", len(r["ANCHORLESS"])))

    print("=" * 50)
    for label, value in counts:
        print(f"{label:.<32} {value}")
    print("-" * 50)
    if mode == "report":
        print("report: no files modified; reports refreshed.")
    elif mode == "dry-run":
        print(f"dry-run: would convert {links_changed} links in {files_changed} files.")
    elif mode == "apply":
        print(f"apply: converted {links_changed} links in {files_changed} files.")
    print("=" * 50)


# --- orchestration ----------------------------------------------------------

def default_root():
    """Returns the git toplevel if inside a repo, otherwise the current dir."""
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return os.getcwd()


def parse_args(argv):
    """Parses the command line into target, mode, root, out, and backup."""
    parser = argparse.ArgumentParser(
        description="Convert AsciiDoc path-based xrefs to ID-based xrefs.")
    parser.add_argument("target", choices=["assembly", "module"],
                        help="which files to convert and how to scope uniqueness")
    parser.add_argument("mode", choices=["report", "dry-run", "apply"])
    parser.add_argument("--root", help="repo root (default: git toplevel)")
    parser.add_argument("--out", help="reports dir (default: <root>/xref-migration)")
    parser.add_argument("--backup", action="store_true",
                        help="write .bak files before editing")
    parser.add_argument("--only-from", metavar="FILE",
                        help="restrict conversion to the source files listed in FILE "
                             "(one 'path:...' or 'path' per line); scope index still uses "
                             "the whole repo")
    return parser.parse_args(argv)


def only_from_files(path, root):
    """Returns the set of absolute source paths listed in an --only-from file.

    Accepts plain repo-relative paths or grep-style 'path:match' lines (such as
    ~/xref.txt); only the leading path before the first ':' is used.
    """
    wanted = set()
    for line in read_text(path).splitlines():
        line = line.strip()
        if not line:
            continue
        rel = line.split(":", 1)[0]
        wanted.add(os.path.normpath(os.path.abspath(os.path.join(root, rel))))
    return wanted


def main(argv):
    """Runs the full pipeline: select files, index scope, classify, report, apply."""
    args = parse_args(argv)
    root = args.root or default_root()
    reports_dir = os.path.join(
        args.out or os.path.join(root, "xref-migration"), "reports")

    # File selection and classifier are the only things that differ by target.
    if args.target == "assembly":
        files = find_assembly_files(root)
        index = index_assembly_targets(root, all_adoc_files(root))
        classifier = lambda x: classify_assembly(x, root, index)
        outcomes = ("AMBIGUOUS", "BROKEN")
    else:
        files = find_module_files(root)
        index = build_module_index(root)
        classifier = lambda x: classify_module(x, index)
        outcomes = ("AMBIGUOUS", "MULTI_CATEGORY", "NO_CATEGORY", "BROKEN")

    # Optionally restrict which source files are converted (scope index unchanged).
    if args.only_from:
        wanted = only_from_files(args.only_from, root)
        files = [f for f in files if os.path.normpath(os.path.abspath(f)) in wanted]

    xrefs, anchorless = parse_xrefs(root, files)
    plan = build_plan(root, xrefs, anchorless, classifier, outcomes)

    write_all_reports(reports_dir, plan, args.target)
    files_changed, links_changed, diff = apply_plan(
        plan, root, write=(args.mode == "apply"), backup=args.backup)
    if args.mode == "dry-run":
        sys.stdout.write(diff)

    print_summary(plan, args.target, len(files), args.mode,
                  files_changed, links_changed)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
