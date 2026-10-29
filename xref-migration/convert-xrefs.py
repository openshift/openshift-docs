#!/usr/bin/env python3

# Converts AsciiDoc path-based xrefs (xref:../f.adoc#id[Text]) to ID-based
# xrefs (xref:id[Text]) in ASSEMBLY files, in preparation for AEM/DITA migration.
#
# An xref is converted only if its id is unique within the book that references
# it, because AEM resolves references per book, by file GUID. Any xref whose id
# is ambiguous within its book is left untouched and written to a review report.
# See XREF-CONVERSION.md for the full rationale. Run with -h for usage.

from __future__ import annotations

import argparse
import difflib
import os
import re
import subprocess
import sys
from dataclasses import dataclass

# Marker that identifies an ASSEMBLY source file
ASSEMBLY_MARK = ":_mod-docs-content-type: ASSEMBLY"

# Top-level directories that never contain ASSEMBLY source we want to rewrite
SKIP_TOP_DIRS = {"modules", ".git", "xref-migration", "_attributes", "snippets"}

# Matches a path-based xref with an anchor, and one without
PATH_ANCHOR_RE = re.compile(r"xref:([^#\[\s]+\.adoc)#([^\[\]]+)\[")
PATH_NOANCHOR_RE = re.compile(r"xref:([^#\[\s]+\.adoc)\[")

# Characters of surrounding text captured per xref for the review reports
FRAG_LEN = 160


@dataclass(frozen=True)
class Xref:
    """A single path-based xref occurrence found in a source file."""

    src: str
    book: str
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


def top_dir(root, abspath):
    """Returns the first path segment of abspath relative to root (its book)."""
    return os.path.relpath(abspath, root).split(os.sep)[0]


def resolve_target(src_file, rel_path):
    """Returns the normalized absolute path that rel_path points to."""
    src_dir = os.path.dirname(os.path.abspath(src_file))
    return os.path.normpath(os.path.join(src_dir, rel_path))


def read_text(path):
    """Returns the file contents, or an empty string if it cannot be read."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def find_assembly_files(root):
    """Returns all ASSEMBLY-type .adoc files under root, skipping SKIP_TOP_DIRS."""
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune directories we never want to descend into
        if os.path.relpath(dirpath, root).split(os.sep)[0] in SKIP_TOP_DIRS:
            dirnames[:] = []
            continue
        for name in filenames:
            path = os.path.join(dirpath, name)
            if name.endswith(".adoc") and ASSEMBLY_MARK in read_text(path)[:4000]:
                found.append(path)
    return sorted(found)


def parse_xrefs(root, files):
    """Returns (path+anchor xrefs, anchorless occurrences) across all files."""
    xrefs = []
    anchorless = []
    for src in files:
        book = top_dir(root, os.path.abspath(src))
        rel = os.path.relpath(src, root)
        for line_no, line in enumerate(read_text(src).splitlines(), start=1):
            # Collect xrefs that carry an #anchor (the convertible kind)
            for m in PATH_ANCHOR_RE.finditer(line):
                fragment = line[m.start():m.start() + FRAG_LEN].rstrip()
                xrefs.append(Xref(src, book, line_no, m.group(1),
                                  m.group(2).strip(), fragment))
            # Record anchorless xrefs separately; they have no id to lift
            for m in PATH_NOANCHOR_RE.finditer(line):
                fragment = line[m.start():m.start() + FRAG_LEN].rstrip()
                anchorless.append((rel, line_no, fragment))
    return xrefs, anchorless


def index_targets(root, xrefs):
    """Returns (anchor -> targets, (book, anchor) -> targets) lookup tables.

    Anchors containing {context} are skipped, since their text is not a real
    resolved id; they are reported separately as broken.
    """
    by_id = {}
    by_book_id = {}
    for x in xrefs:
        if "{context}" in x.anchor:
            continue
        target = resolve_target(x.src, x.path)
        by_id.setdefault(x.anchor, set()).add(target)
        by_book_id.setdefault((x.book, x.anchor), set()).add(target)
    return by_id, by_book_id


def bucket(anchor):
    """Returns the quarantine kind (INDEX or CONFLICT) for a within-book-ambiguous anchor."""
    # The book-landing 'index' anchor is its own structural case
    if anchor == "index":
        return "INDEX"
    # Everything else is a genuine within-book content conflict
    return "CONFLICT"


def classify(x, by_book_id):
    """Returns the outcome for one xref: CLEAN, INDEX, CONFLICT, or BROKEN."""
    # An unresolved {context} in the anchor cannot be converted
    if "{context}" in x.anchor:
        return "BROKEN"
    # The decisive test: is the id unique within the book it is referenced from?
    # AEM resolves per book by file GUID, so within-book uniqueness is sufficient.
    if len(by_book_id.get((x.book, x.anchor), ())) <= 1:
        return "CLEAN"
    # Otherwise it is ambiguous within its book; sort it into a quarantine kind
    return bucket(x.anchor)


@dataclass
class Plan:
    """The edits to make and the report rows to write, for the chosen mode."""

    edits_by_file: dict
    rows: dict
    clean_count: int


def build_plan(xrefs, anchorless, by_book_id, root):
    """Classifies every xref into edits (CLEAN) and quarantine report rows."""
    edits_by_file = {}
    rows = {k: [] for k in ("INDEX", "CONFLICT", "BROKEN")}
    clean_count = 0

    for x in xrefs:
        outcome = classify(x, by_book_id)
        rel = os.path.relpath(x.src, root)
        # CLEAN xrefs become edits; everything else is quarantined for review
        if outcome == "CLEAN":
            edits_by_file.setdefault(x.src, []).append((x.old_text, x.new_text))
            clean_count += 1
        elif outcome == "BROKEN":
            rows["BROKEN"].append(f"{rel}:{x.line}\t{x.fragment}")
        else:
            rows[outcome].append(f"{rel}:{x.line}\t{x.anchor}\t{x.fragment}")

    # Anchorless xrefs are collected in parse_xrefs, not classified per id
    rows["ANCHORLESS"] = [f"{rel}:{ln}\t{frag}" for rel, ln, frag in anchorless]
    return Plan(edits_by_file, rows, clean_count)


def write_report(reports_dir, filename, header, rows):
    """Writes one report file: a header block followed by its data rows."""
    with open(os.path.join(reports_dir, filename), "w") as f:
        f.write(header.rstrip() + "\n")
        f.write("".join(row + "\n" for row in rows))


def write_all_reports(reports_dir, plan, by_id, by_book_id, root):
    """Writes every review-queue report to reports_dir."""
    os.makedirs(reports_dir, exist_ok=True)

    # Only IDs that are ambiguous WITHIN a book are quarantined and listed here.
    within_book_ambiguous = sorted({
        anchor for (book, anchor), targets in by_book_id.items() if len(targets) > 1})

    def id_rows(kind):
        """Builds '<id>\t<target1> | <target2>' rows for one quarantine kind."""
        return [f"{a}\t" + " | ".join(sorted(os.path.relpath(t, root)
                                              for t in by_id[a]))
                for a in within_book_ambiguous if bucket(a) == kind]

    r = plan.rows

    # The book-landing 'index' anchor
    write_report(reports_dir, "ambiguous_index.txt",
                 "# Book-landing 'index' anchor.\n"
                 "# Map each book index to its DITA map landing topic.",
                 id_rows("INDEX"))

    # Genuine within-book conflicts needing human review
    write_report(reports_dir, "ambiguous_within_book.txt",
                 "# Within-book conflicts. HUMAN REVIEW REQUIRED.",
                 id_rows("CONFLICT"))

    # The flat index of every quarantined instance, for triage
    write_report(reports_dir, "ambiguous_instances_all.txt",
                 f"# Quarantined instances. index={len(r['INDEX'])} conflict={len(r['CONFLICT'])}",
                 r["INDEX"] + r["CONFLICT"])

    # The two edge-case queues
    write_report(reports_dir, "anchorless_xrefs.txt",
                 "# Anchorless path xrefs (no #anchor). Synthesize target id per case.",
                 r["ANCHORLESS"])
    write_report(reports_dir, "broken_context_xrefs.txt",
                 "# Literal {context} left in anchor. Author supplies resolved value.",
                 r["BROKEN"])


def rewrite_file(src, edits):
    """Returns (old_text, new_text) for src after applying edits, without writing.

    Each edit is a literal, fully-qualified xref prefix, so a plain replace is
    both safe and idempotent: already-converted bare xrefs are never matched.
    """
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
        # Skip files the edits did not actually change
        if old_text == new_text:
            continue
        files_changed += 1
        links_changed += len(dict(edits))
        if write:
            # Optionally preserve the original before overwriting
            if backup:
                with open(src + ".bak", "w", encoding="utf-8") as f:
                    f.write(old_text)
            with open(src, "w", encoding="utf-8") as f:
                f.write(new_text)
        else:
            # Collect a unified diff instead of writing
            rel = os.path.relpath(src, root)
            diff += difflib.unified_diff(old_text.splitlines(keepends=True),
                                         new_text.splitlines(keepends=True),
                                         fromfile=f"a/{rel}", tofile=f"b/{rel}")

    return files_changed, links_changed, "".join(diff)


def print_summary(plan, file_count, mode, files_changed, links_changed):
    """Prints the classification summary and the result of the chosen mode."""
    r = plan.rows
    quarantined = len(r["INDEX"]) + len(r["CONFLICT"])

    # The counts, as (label, value) pairs for aligned printing
    counts = [
        ("ASSEMBLY files", file_count),
        ("CLEAN (convertible)", plan.clean_count),
        ("quarantined ambiguous", quarantined),
        ("  index landing", len(r["INDEX"])),
        ("  within-book conflict", len(r["CONFLICT"])),
        ("anchorless", len(r["ANCHORLESS"])),
        ("broken {context}", len(r["BROKEN"])),
    ]
    print("=" * 50)
    for label, value in counts:
        print(f"{label:.<32} {value}")
    print("-" * 50)

    # The closing line depends on which mode ran
    if mode == "report":
        print("report: no files modified; reports refreshed.")
    elif mode == "dry-run":
        print(f"dry-run: would convert {links_changed} links in {files_changed} files.")
    elif mode == "apply":
        print(f"apply: converted {links_changed} links in {files_changed} files.")
    print("=" * 50)


def default_root():
    """Returns the git toplevel if inside a repo, otherwise the current dir."""
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return os.getcwd()


def parse_args(argv):
    """Parses the command line into mode, root, out, and backup."""
    parser = argparse.ArgumentParser(
        description="Convert AsciiDoc path-based xrefs to ID-based xrefs.")
    parser.add_argument("mode", choices=["report", "dry-run", "apply"])
    parser.add_argument("--root", help="repo root (default: git toplevel)")
    parser.add_argument("--out", help="reports dir (default: <root>/xref-migration)")
    parser.add_argument("--backup", action="store_true",
                        help="write .bak files before editing")
    return parser.parse_args(argv)


def main(argv):
    """Runs the full pipeline: find, parse, classify, report, then apply."""
    args = parse_args(argv)
    root = args.root or default_root()
    reports_dir = os.path.join(
        args.out or os.path.join(root, "xref-migration"), "reports")

    # Discover source files and the xrefs within them
    files = find_assembly_files(root)
    xrefs, anchorless = parse_xrefs(root, files)

    # Index where every id resolves, then classify each xref
    by_id, by_book_id = index_targets(root, xrefs)
    plan = build_plan(xrefs, anchorless, by_book_id, root)

    # Always refresh the review reports
    write_all_reports(reports_dir, plan, by_id, by_book_id, root)

    # Apply the edits, or preview them for dry-run
    files_changed, links_changed, diff = apply_plan(
        plan, root, write=(args.mode == "apply"), backup=args.backup)
    if args.mode == "dry-run":
        sys.stdout.write(diff)

    print_summary(plan, len(files), args.mode, files_changed, links_changed)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
