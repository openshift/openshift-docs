#!/usr/bin/env python3
"""Add a visible warning to preview pages when content is missing."""

from __future__ import annotations

import html
import sys
from pathlib import Path
import re


BODY_RE = re.compile(r"<body\b[^>]*>", re.IGNORECASE)
HEAD_CLOSE_RE = re.compile(r"</head>", re.IGNORECASE)


WARNING_STYLE = """<!-- jtbd-preview-warning-start -->
<style>
  .jtbd-preview-warning {
    background: #fff1f1;
    border: 2px solid #c9190b;
    border-radius: 4px;
    color: #3b0a0a;
    font-family: "Open Sans", "DejaVu Sans", sans-serif;
    margin: 1em auto;
    max-width: 70em;
    padding: 1em 1.25em;
  }
  .jtbd-preview-warning strong { color: #a30000; }
  .jtbd-preview-warning details { margin-top: .75em; }
  .jtbd-preview-warning pre {
    background: #fff;
    border: 1px solid #d7d7d7;
    max-height: 20em;
    overflow: auto;
    padding: .75em;
    white-space: pre-wrap;
  }
</style>
<!-- jtbd-preview-warning-end -->"""


def warning_markup(report: str) -> str:
    escaped = html.escape(report)
    return (
        '<div class="jtbd-preview-warning" role="alert">'
        "<strong>Preview warning: this preview is incomplete.</strong>"
        "<p>One or more AsciiDoc includes are missing. Content may be absent "
        "from this page or from related pages.</p>"
        "<details><summary>Show missing-include report</summary>"
        f"<pre>{escaped}</pre></details>"
        "<details><summary>How to remediate missing content</summary>"
        "<ol>"
        "<li>Restore or create the expected <code>.adoc</code> file at the "
        "reported path, including its required content and attributes.</li>"
        "<li>If the topic was renamed or moved, update the reported "
        "<code>include::</code> directive to point to the existing file. "
        "The path is relative to the file containing the directive.</li>"
        "<li>If the topic is intentionally not ready, remove the include "
        "from the map and track the content gap separately. Do not use an "
        "empty placeholder as a substitute for content.</li>"
        "</ol>"
        "<p>After making the change, run "
        "<code>python3 scripts/audit-map-includes.py "
        "maps/rhcl/navigation.adoc</code>. Once the audit passes, run "
        "<code>bash scripts/preview-jtbd-maps.sh -d rhcl "
        "-o /tmp/rhcl-jtbd-preview</code> to rebuild the preview.</p>"
        "</details></div>"
    )


def process(path: Path, report: str) -> bool:
    source = path.read_text(encoding="utf-8")
    if "<!-- jtbd-preview-warning-start -->" in source:
        return False
    head = HEAD_CLOSE_RE.search(source)
    body = BODY_RE.search(source)
    if not head or not body:
        return False
    source = (
        source[: head.start()]
        + WARNING_STYLE
        + "\n"
        + source[head.start() :]
    )
    body = BODY_RE.search(source)
    assert body is not None
    source = source[: body.end()] + "\n" + warning_markup(report) + source[body.end() :]
    path.write_text(source, encoding="utf-8")
    return True


def main() -> int:
    if len(sys.argv) != 3:
        print(
            f"Usage: {Path(sys.argv[0]).name} OUTPUT_DIR PREFLIGHT_REPORT",
            file=sys.stderr,
        )
        return 2

    output = Path(sys.argv[1])
    report = Path(sys.argv[2]).read_text(encoding="utf-8")
    changed = sum(process(path, report) for path in sorted(output.glob("*.html")))
    print(f"Added missing-content warning to {changed} HTML pages in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
