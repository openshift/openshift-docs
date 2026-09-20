#!/usr/bin/env python3
"""Add a page-local right-hand TOC to Asciidoctor multipage output."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(
    r'<h([2-6])\b([^>]*)\bid="([^"]+)"([^>]*)>(.*?)</h\1>',
    re.DOTALL | re.IGNORECASE,
)
BODY_RE = re.compile(r'<body\b([^>]*)>', re.IGNORECASE)
CONTENT_RE = re.compile(r'<div\b[^>]*\bid="content"[^>]*>', re.IGNORECASE)
RIGHT_TOC_RE = re.compile(
    r'\s*<aside id="jtbd-right-toc".*?</aside>\s*',
    re.DOTALL,
)
RIGHT_STYLE_RE = re.compile(
    r'\s*<!-- jtbd-right-toc-start -->.*?<!-- jtbd-right-toc-end -->\s*',
    re.DOTALL,
)
TAG_RE = re.compile(r'<[^>]+>')
ID_RE = re.compile(r'\bid="([^"]+)"')
HREF_RE = re.compile(r'(?P<prefix>href=")(?P<href>[^"]+)(?P<suffix>")')
HTML_TAG_RE = re.compile(r'<(/?)([A-Za-z][\w:-]*)(?:\s[^>]*)?>', re.DOTALL)
TOC_ROOT_RE = re.compile(
    r'<ul\b[^>]*\bclass="[^"]*\bsectlevel1\b[^"]*"[^>]*>',
    re.IGNORECASE,
)
TOC_PARENT_RE = re.compile(
    r'(?P<li><li>)(?!\s*<button\s+class="toc-toggle")'
    r'(?P<link>(?:(?!</li>).)*?<a\b[^>]*>(?:(?!</a>).)*</a>\s*)'
    r'(?P<ul><ul\s+class="sectlevel)',
    re.DOTALL | re.IGNORECASE,
)


RIGHT_TOC_STYLE = """<!-- jtbd-right-toc-start -->
<style>
  body.jtbd-has-right-toc { padding-right: 18em; }
  #jtbd-right-toc {
    position: fixed;
    top: 0;
    right: 0;
    width: 16em;
    height: 100%;
    overflow: auto;
    padding: 1.25em 1em;
    background: #f8f8f7;
    border-left: 1px solid #e7e7e9;
    z-index: 1000;
    font-family: "Open Sans", "DejaVu Sans", sans-serif;
    font-size: .9em;
  }
  #jtbd-right-toc h2 { margin-top: 0; font-size: 1.1em; }
  #jtbd-right-toc ul { list-style: none; margin: 0; padding: 0; }
  #jtbd-right-toc li { line-height: 1.35; margin: .4em 0; }
  #jtbd-right-toc li.level-3 { padding-left: 1em; }
  #jtbd-right-toc li.level-4 { padding-left: 2em; }
  #jtbd-right-toc li.level-5,
  #jtbd-right-toc li.level-6 { padding-left: 3em; }
  #jtbd-right-toc a { text-decoration: none; }
  @media screen and (max-width: 1023px) {
    body.jtbd-has-right-toc { padding-right: 0; }
    #jtbd-right-toc {
      position: static;
      width: auto;
      height: auto;
      margin: 1em;
      border: 1px solid #e7e7e9;
      border-radius: 4px;
    }
  }
</style>
<!-- jtbd-right-toc-end -->"""


def visible_text(fragment: str) -> str:
    text = TAG_RE.sub("", fragment)
    return " ".join(html.unescape(text).split())


def build_toc(headings: list[tuple[int, str, str]]) -> str:
    items = []
    for level, anchor, label in headings:
        items.append(
            f'<li class="level-{level}"><a href="#{html.escape(anchor, quote=True)}">'
            f'{html.escape(label)}</a></li>'
        )
    return (
        '<aside id="jtbd-right-toc" aria-label="On this page">'
        '<h2>On this page</h2><ul>'
        + "".join(items)
        + "</ul></aside>"
    )


def set_right_toc_class(source: str, enabled: bool) -> str:
    body = BODY_RE.search(source)
    if not body:
        return source

    body_attrs = body.group(1)
    class_match = re.search(r'\bclass="([^"]*)"', body_attrs, re.IGNORECASE)
    if class_match:
        classes = class_match.group(1).split()
        if enabled and "jtbd-has-right-toc" not in classes:
            classes.append("jtbd-has-right-toc")
        if not enabled:
            classes = [item for item in classes if item != "jtbd-has-right-toc"]
        if classes:
            replacement = f'class="{" ".join(classes)}"'
            body_attrs = (
                body_attrs[: class_match.start()]
                + replacement
                + body_attrs[class_match.end() :]
            )
        else:
            body_attrs = body_attrs[: class_match.start()] + body_attrs[class_match.end() :]
    elif enabled:
        body_attrs = f' class="jtbd-has-right-toc"{body_attrs}'

    return source[:body.start()] + f"<body{body_attrs}>" + source[body.end() :]


def rewrite_internal_links(source: str, page: Path, anchor_pages: dict[str, str]) -> str:
    def replace(match: re.Match[str]) -> str:
        href = match.group("href")
        if "://" in href or href.startswith(("/", "mailto:", "javascript:")):
            return match.group(0)
        if "#" not in href:
            return match.group(0)

        _, fragment = href.split("#", 1)
        target_page = anchor_pages.get(fragment)
        if not target_page:
            return match.group(0)

        target = f"#{fragment}" if target_page == page.name else f"{target_page}#{fragment}"
        return f'{match.group("prefix")}{target}{match.group("suffix")}'

    return HREF_RE.sub(replace, source)


def add_static_toc_toggles(source: str) -> str:
    def replace(match: re.Match[str]) -> str:
        href = re.search(r'href="([^"]+)"', match.group("link"), re.IGNORECASE)
        key = href.group(1).split("#", 1)[0] if href else ""
        button = (
            '<button class="toc-toggle" type="button" '
            f'data-toc-key="{html.escape(key, quote=True)}">▶</button>'
        )
        return f'{match.group("li")}{button}{match.group("link")}{match.group("ul")}'

    return TOC_PARENT_RE.sub(replace, source)


def matching_element_end(source: str, opening: re.Match[str], tag_name: str) -> int:
    """Return the end offset of the element opened by *opening*."""
    depth = 1
    for token in HTML_TAG_RE.finditer(source, opening.end()):
        if token.group(2).lower() != tag_name.lower():
            continue
        if token.group(1):
            depth -= 1
            if depth == 0:
                return token.end()
        elif not token.group(0).rstrip().endswith('/>'):
            depth += 1
    raise ValueError(f"Unclosed <{tag_name}> element")


def root_toc_bounds(source: str) -> tuple[int, int, int] | None:
    """Return (start, opening_end, end) for the top-level TOC list."""
    opening = TOC_ROOT_RE.search(source)
    if not opening:
        return None
    return opening.start(), opening.end(), matching_element_end(source, opening, "ul")


def direct_child_bounds(
    source: str, opening_start: int, opening_end: int, end: int, tag_name: str
) -> list[tuple[int, int, int]]:
    """Find direct child elements as (start, opening_end, end) tuples."""
    children = []
    depth = 0
    for token in HTML_TAG_RE.finditer(source, opening_end, end):
        if token.group(2).lower() != tag_name.lower():
            continue
        if token.group(1):
            depth -= 1
            if depth == 0 and children and children[-1][2] is None:
                start, child_opening_end, _ = children[-1]
                children[-1] = (start, child_opening_end, token.end())
        elif not token.group(0).rstrip().endswith('/>'):
            if depth == 0:
                children.append((token.start(), token.end(), None))
            depth += 1
    return [child for child in children if child[2] is not None]


def toc_children(source: str) -> dict[str, str]:
    """Return top-level category hrefs and their child-list markup."""
    bounds = root_toc_bounds(source)
    if not bounds:
        return {}
    root_start, root_opening_end, root_end = bounds
    result = {}
    for li_start, li_opening_end, li_end in direct_child_bounds(
        source, root_start, root_opening_end, root_end, "li"
    ):
        li_source = source[li_start:li_end]
        link = re.search(r'<a\b[^>]*\bhref="([^"]+)"', li_source, re.IGNORECASE)
        if not link:
            continue
        child_lists = direct_child_bounds(
            source, li_start, li_opening_end, li_end, "ul"
        )
        if child_lists:
            child_start, _, child_end = child_lists[0]
            result.setdefault(link.group(1).split("#", 1)[0], source[child_start:child_end])
    return result


def merge_toc_children(source: str, all_children: dict[str, str]) -> str:
    """Populate each page's left TOC with child lists discovered on other pages."""
    bounds = root_toc_bounds(source)
    if not bounds:
        return source
    root_start, root_opening_end, root_end = bounds
    insertions = []
    for li_start, li_opening_end, li_end in direct_child_bounds(
        source, root_start, root_opening_end, root_end, "li"
    ):
        li_source = source[li_start:li_end]
        link = re.search(r'<a\b[^>]*\bhref="([^"]+)"', li_source, re.IGNORECASE)
        if not link:
            continue
        if direct_child_bounds(source, li_start, li_opening_end, li_end, "ul"):
            continue
        child_markup = all_children.get(link.group(1).split("#", 1)[0])
        if not child_markup:
            continue
        closing = source.rfind("</li>", li_start, li_end)
        if closing >= 0:
            insertions.append((closing, "\n" + child_markup + "\n"))

    for position, markup in reversed(insertions):
        source = source[:position] + markup + source[position:]
    return source


def process(
    path: Path, anchor_pages: dict[str, str], all_children: dict[str, str]
) -> bool:
    source = path.read_text(encoding="utf-8")
    source = merge_toc_children(source, all_children)
    headings = []
    for match in HEADING_RE.finditer(source):
        level = int(match.group(1))
        anchor = match.group(3)
        label = visible_text(match.group(5))
        if label:
            headings.append((level, anchor, label))

    # The first heading is the current page title. It is already represented
    # by the left navigation, so the right navigation should list only the
    # topics below it.
    headings = headings[1:]

    source = RIGHT_TOC_RE.sub("", source)
    source = RIGHT_STYLE_RE.sub("", source)
    source = source.replace("<!-- jtbd-right-toc-start -->", "")

    if not headings:
        source = set_right_toc_class(source, False)
        source = rewrite_internal_links(source, path, anchor_pages)
        source = add_static_toc_toggles(source)
        path.write_text(source, encoding="utf-8")
        return False

    body = BODY_RE.search(source)
    if not body:
        raise ValueError(f"No body element found in {path}")

    source = set_right_toc_class(source, True)

    source = source.replace("</head>", RIGHT_TOC_STYLE + "\n</head>", 1)
    content = CONTENT_RE.search(source)
    if not content:
        raise ValueError(f"No content element found in {path}")
    source = source[: content.start()] + build_toc(headings) + "\n" + source[content.start() :]
    source = rewrite_internal_links(source, path, anchor_pages)
    source = add_static_toc_toggles(source)
    path.write_text(source, encoding="utf-8")
    return True


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} OUTPUT_DIR", file=sys.stderr)
        return 2

    output = Path(sys.argv[1])
    pages = sorted(output.glob("*.html"))
    anchor_pages = {}
    all_children = {}
    for page in pages:
        source = page.read_text(encoding="utf-8")
        for anchor in ID_RE.findall(source):
            anchor_pages.setdefault(anchor, page.name)
        for href, child_markup in toc_children(source).items():
            all_children.setdefault(href, child_markup)

    changed = sum(process(page, anchor_pages, all_children) for page in pages)
    print(f"Added right TOCs to {changed} of {len(pages)} HTML pages in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
