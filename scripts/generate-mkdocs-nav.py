#!/usr/bin/env python3
"""
Convert _topic_map.yaml to MkDocs nav.yml format.
Note: _topic_map.yml is no longer updated.
This script ignores missing files.

Example:
  python scripts/generate-mkdocs-nav.py \
    _topic_maps/_topic_map.yml \
    -d openshift-enterprise \
    -o nav.yml
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

try:
    import yaml  # pip install pyyaml
except ModuleNotFoundError:
    sys.stderr.write("Error: PyYAML is required. Install with: pip install pyyaml\n")
    sys.exit(1)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert topic_map.yaml to MkDocs nav YAML.")
    p.add_argument("input", nargs="?", default="_topic_maps/_topic_map.yml")
    p.add_argument("-o", "--out")
    p.add_argument("-d", "--distro")
    p.add_argument("-r", "--repo-root", default=".", help="Repository root directory")
    p.add_argument("-i", "--index", help="Index file to add at top of nav (e.g., index.md)")
    return p.parse_args()


def normjoin(a: str | None, b: str | None) -> str:
    a = (a or "").rstrip("/")
    b = (b or "").lstrip("/")
    if not a:
        return b
    if not b:
        return a
    return f"{a}/{b}"


def add_ext(stem: str) -> str:
    last = stem.rsplit("/", 1)[-1]
    if "." in last:
        return stem
    return f"{stem}.adoc"


def make_items(items, base_dir, distro=None, repo_root="."):
    out = []
    for it in items or []:
        if not isinstance(it, dict):
            continue

        # Filter by distro if specified
        if distro:
            distros = it.get("Distros", "")
            if distros:  # If Distros field exists
                distro_list = [d.strip() for d in distros.split(",")]
                if distro not in distro_list:
                    continue  # Skip this item if distro doesn't match

        title = it.get("Name") or it.get("Title") or "Untitled"
        sub = it.get("Topics") or it.get("topics")
        item_dir = normjoin(base_dir, it.get("Dir")) if it.get("Dir") else base_dir
        file_stem = it.get("File") or it.get("file")

        if file_stem:
            file_path = normjoin(item_dir, add_ext(file_stem))
            # Check if file exists in repo
            full_path = Path(repo_root) / file_path
            if full_path.exists():
                out.append({title: file_path})
        elif sub:
            sub_items = make_items(sub, item_dir, distro, repo_root)
            # Only add section if it has items
            if sub_items:
                out.append({title: sub_items})
        else:
            # Skip headings with no File/Topics
            continue
    return out


def build_sections(root, distro=None, repo_root="."):
    sections = []
    if isinstance(root, list):
        for d in root:
            if not isinstance(d, dict):
                continue

            # Filter by distro if specified
            if distro:
                distros = d.get("Distros", "")
                if distros:  # If Distros field exists
                    distro_list = [dist.strip() for dist in distros.split(",")]
                    if distro not in distro_list:
                        continue  # Skip this section if distro doesn't match

            name = d.get("Name") or d.get("Title") or "Section"
            base = d.get("Dir", "")
            items = make_items(d.get("Topics") or [], base, distro, repo_root)
            # Only add section if it has items
            if items:
                sections.append({name: items})
    elif isinstance(root, dict):
        # Filter by distro if specified
        if distro:
            distros = root.get("Distros", "")
            if distros:  # If Distros field exists
                distro_list = [dist.strip() for dist in distros.split(",")]
                if distro not in distro_list:
                    return []  # Skip entire root if distro doesn't match

        name = root.get("Name") or root.get("Title") or "Documentation"
        base = root.get("Dir", "")
        items = make_items(root.get("Topics") or [], base, distro, repo_root)
        # Only add section if it has items
        if items:
            sections.append({name: items})
    return sections


def main():
    args = parse_args()
    src = Path(args.input)
    if not src.exists():
        sys.stderr.write(f"Error: input not found: {src}\n")
        sys.exit(1)

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        sys.stderr.write(f"Error: repo root not found: {repo_root}\n")
        sys.exit(1)

    with src.open("r", encoding="utf-8") as f:
        # Accept multi-document YAML (--- ... ---)
        docs = [d for d in yaml.safe_load_all(f) if d not in (None, "", [])]

    root = docs[0] if len(docs) == 1 else docs  # single doc or list of docs
    nav = build_sections(root, args.distro, repo_root)

    # Generate nav YAML and manually indent it under 'nav:' key
    nav_yaml = yaml.safe_dump(nav, sort_keys=False, width=1000, allow_unicode=True, default_flow_style=False)
    # Indent each line of the nav content by 2 spaces
    indented_nav = '\n'.join('  ' + line if line else line for line in nav_yaml.splitlines())
    text = 'nav:\n' + indented_nav

    if args.out == "-" or not args.out:
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
