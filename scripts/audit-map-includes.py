#!/usr/bin/env python3
"""Audit the recursive AsciiDoc include graph for one or more map entries."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


INCLUDE_RE = re.compile(r"^[ \t]*include::([^\[]+)\[", re.MULTILINE)


@dataclass(frozen=True)
class MissingInclude:
    source: Path
    line: int
    directive: str
    target: Path


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def entry_path(value: str, root: Path) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = Path.cwd() / candidate
    if not candidate.exists():
        candidate = root / value
    return candidate


def audit_entry(
    entry: Path, root: Path
) -> tuple[int, int, set[Path], list[MissingInclude]]:
    """Walk an entry map and return file/include counts and missing targets."""
    seen: set[Path] = set()
    missing: list[MissingInclude] = []
    include_count = 0

    def visit(path: Path) -> None:
        nonlocal include_count
        canonical = path.resolve()
        if canonical in seen:
            return
        seen.add(canonical)

        if not path.is_file():
            return

        source = path.read_text(encoding="utf-8")
        for match in INCLUDE_RE.finditer(source):
            include_count += 1
            reference = match.group(1).strip()
            target = path.parent / reference
            if not target.is_file():
                line = source.count("\n", 0, match.start()) + 1
                line_text = source.splitlines()[line - 1].strip()
                missing.append(
                    MissingInclude(
                        source=path,
                        line=line,
                        directive=line_text,
                        target=target,
                    )
                )
                continue
            visit(target)

    if not entry.is_file():
        missing.append(MissingInclude(entry, 0, "entry map", entry))
    else:
        visit(entry)

    return len(seen), include_count, seen, missing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check recursive AsciiDoc includes before rendering a map preview."
    )
    parser.add_argument(
        "entries",
        nargs="+",
        help="Entry map files, for example maps/rhcl/navigation.adoc",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent.parent
    all_missing: list[MissingInclude] = []
    total_files = 0
    total_includes = 0

    for value in args.entries:
        entry = entry_path(value, root)
        files, includes, _, missing = audit_entry(entry, root)
        total_files += files
        total_includes += includes
        all_missing.extend(missing)

        label = display_path(entry, root)
        if missing:
            print(f"Include preflight failed for {label}", file=sys.stderr)
        else:
            print(
                f"Include preflight passed for {label} "
                f"({files} source files, {includes} include directives)"
            )

    if not all_missing:
        if len(args.entries) > 1:
            print(
                f"Include preflight passed: {total_files} source files, "
                f"{total_includes} include directives"
            )
        return 0

    print("", file=sys.stderr)
    print("Missing include targets:", file=sys.stderr)
    for item in all_missing:
        source = display_path(item.source, root)
        target = display_path(item.target, root)
        location = f"{source}:{item.line}" if item.line else source
        print(f"  {location}", file=sys.stderr)
        print(f"    {item.directive}", file=sys.stderr)
        print(f"    expected: {target}", file=sys.stderr)

    print("", file=sys.stderr)
    print("How to fix these errors:", file=sys.stderr)
    print(
        "  1. Restore or create the expected .adoc file, preserving the "
        "path relative to the referring map; or",
        file=sys.stderr,
    )
    print(
        "  2. Change the include directive to the path of the existing "
        "source file if the topic was renamed or moved.",
        file=sys.stderr,
    )
    print(
        "  Then rerun this audit and the preview. Do not ignore the error: "
        "Asciidoctor can otherwise generate incomplete HTML.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
