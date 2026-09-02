#!/usr/bin/env python3
"""
Step 1: Fill stub job files with module includes by matching to assemblies.
Step 2: Fix broken ../topic/modules/ include paths in restored jobs.
Step 3: Clean up long filenames (>60 chars).

All paths are relative to REPO root.
"""

import os
import re
import sys
from collections import defaultdict

REPO = "/home/avbhatt/ocp-repos/openshift-docs"
JOBS_DIR = os.path.join(REPO, "maps", "jobs-openshift-enterprise")
CATS_DIR = os.path.join(REPO, "maps", "openshift-enterprise")
MODULES_DIR = os.path.join(REPO, "modules")

STOP_WORDS = {
    "the", "a", "an", "to", "for", "of", "in", "on", "my", "i", "and",
    "or", "is", "are", "can", "so", "that", "with", "by", "as", "at",
    "from", "be", "it", "its", "this", "when", "how", "what", "which",
    "your", "want", "need", "use", "using", "understand", "configure",
    "about", "create", "set", "up", "manage", "install", "enable",
}

ABBREVIATIONS = {
    "lso": {"local", "storage", "operator"},
    "lvm": {"logical", "volume", "manager"},
    "mco": {"machine", "config", "operator"},
    "scc": {"security", "context", "constraint"},
    "csi": {"container", "storage", "interface"},
    "cni": {"container", "network", "interface"},
    "sdn": {"software", "defined", "networking"},
    "ovn": {"open", "virtual", "network"},
    "gpu": {"graphics", "processing", "unit"},
    "ebs": {"elastic", "block", "store"},
    "efs": {"elastic", "file", "system"},
    "nfs": {"network", "file", "system"},
    "pvc": {"persistent", "volume", "claim"},
    "hcp": {"hosted", "control", "planes"},
    "dns": {"domain", "name", "system"},
    "tls": {"transport", "layer", "security"},
    "rbac": {"role", "based", "access", "control"},
    "numa": {"non", "uniform", "memory", "access"},
    "ztp": {"zero", "touch", "provisioning"},
    "keda": {"kubernetes", "event", "driven", "autoscaler"},
}


def tokenize(s, keep_stop=False):
    words = set(re.split(r"[-_\s/\.]+", s.lower()))
    words.discard("")
    expanded = set()
    for w in words:
        expanded.add(w)
        if w in ABBREVIATIONS:
            expanded.update(ABBREVIATIONS[w])
    if not keep_stop:
        expanded -= STOP_WORDS
    return expanded


def match_score(a, b):
    if not a or not b:
        return 0.0
    intersection = a & b
    union = a | b
    jaccard = len(intersection) / len(union) if union else 0.0
    shorter = a if len(a) <= len(b) else b
    longer = b if len(a) <= len(b) else a
    if shorter and len(shorter) >= 2 and shorter.issubset(longer):
        jaccard = max(jaccard, 0.7)
    return jaccard


# ─── Phase A: Build assembly index ───

def build_assembly_index():
    """Index all assembly files: title, module includes."""
    print("  Indexing assemblies...")
    assemblies = {}
    skip_dirs = {"maps", "modules", "_unused_topics", "_attributes",
                 "_images", "images", "_javascripts", "_gemfiles",
                 "_converters", "drupal-build", "contributing_to_docs",
                 ".git", "scripts", "rest_api", "snippets"}

    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith(".")]
        rel_root = os.path.relpath(root, REPO)
        if rel_root.startswith("maps"):
            continue

        for fname in files:
            if not fname.endswith(".adoc"):
                continue
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read(8000)  # Read enough for title + includes
            except:
                continue

            # Check if it's an assembly
            if ":_mod-docs-content-type: ASSEMBLY" not in content:
                continue

            # Extract title
            title = ""
            for line in content.split("\n"):
                if line.startswith("= "):
                    title = line[2:].strip()
                    break

            # Extract module includes
            mod_includes = []
            for line in content.split("\n"):
                line = line.strip()
                if line.startswith("include::") and "modules/" in line:
                    # Extract just the module filename
                    m = re.search(r"include::.*?modules/([^[]+)\[(.+?)\]", line)
                    if m:
                        mod_file = m.group(1)
                        attrs = m.group(2)
                        # Verify module exists in shared modules/
                        if os.path.exists(os.path.join(MODULES_DIR, mod_file)):
                            mod_includes.append((mod_file, attrs))

            if title or mod_includes:
                rel_path = os.path.relpath(fpath, REPO)
                assemblies[rel_path] = {
                    "title": title,
                    "modules": mod_includes,
                    "tokens": tokenize(title) if title else set(),
                }

    print(f"  Indexed {len(assemblies)} assemblies")
    return assemblies


# ─── Phase B: Build module title index ───

def build_module_index():
    """Index module files by title for direct matching."""
    print("  Indexing module titles...")
    modules = {}
    for fname in os.listdir(MODULES_DIR):
        if not fname.endswith(".adoc"):
            continue
        fpath = os.path.join(MODULES_DIR, fname)
        try:
            with open(fpath, "r", errors="replace") as f:
                head = f.read(500)
        except:
            continue

        title = ""
        content_type = ""
        for line in head.split("\n"):
            if line.startswith("= "):
                title = line[2:].strip()
            if ":_mod-docs-content-type:" in line:
                content_type = line.split(":")[-1].strip()

        if title:
            modules[fname] = {
                "title": title,
                "type": content_type,
                "tokens": tokenize(title),
            }

    print(f"  Indexed {len(modules)} module titles")
    return modules


# ─── Phase C: Fill stubs ───

def fill_stubs(assemblies, modules):
    """Match each stub to assemblies/modules and fill with includes."""
    print("\n  Filling stub jobs...")

    stubs = []
    for fname in sorted(os.listdir(JOBS_DIR)):
        if not fname.endswith(".adoc"):
            continue
        fpath = os.path.join(JOBS_DIR, fname)
        with open(fpath) as f:
            content = f.read()
        if "// TODO: Add module includes" in content:
            # Extract job name from comment
            m = re.search(r"// Job name: (.+)", content)
            job_name = m.group(1).strip() if m else fname.replace(".adoc", "").replace("-", " ")
            stubs.append((fname, fpath, job_name))

    print(f"  Found {len(stubs)} stubs to fill")

    # Pre-compute assembly tokens
    asm_list = [(path, info) for path, info in assemblies.items() if info["modules"]]

    filled = 0
    partial = 0

    for fname, fpath, job_name in stubs:
        slug = fname.replace(".adoc", "")
        job_tokens = tokenize(job_name)

        # Strategy 1: Match to assemblies by title
        best_asm = None
        best_score = 0.0
        for asm_path, asm_info in asm_list:
            score = match_score(job_tokens, asm_info["tokens"])
            if score > best_score:
                best_score = score
                best_asm = asm_info

        # Strategy 2: Match individual modules by title
        matching_modules = []
        for mod_fname, mod_info in modules.items():
            score = match_score(job_tokens, mod_info["tokens"])
            if score >= 0.45:
                matching_modules.append((mod_fname, score, mod_info))

        matching_modules.sort(key=lambda x: -x[1])

        # Decide which source to use
        mod_includes = []

        if best_asm and best_score >= 0.45 and best_asm["modules"]:
            # Use assembly's modules
            mod_includes = best_asm["modules"]
            source = f"assembly: {best_asm['title'][:60]} (score={best_score:.2f})"
        elif matching_modules:
            # Use individually matched modules (top 6)
            for mod_fname, score, mod_info in matching_modules[:6]:
                mod_includes.append((mod_fname, f"leveloffset=+1"))
            source = f"individual modules (top {len(mod_includes)} matches)"
        else:
            continue  # Leave as stub

        if not mod_includes:
            continue

        # Write the filled job file
        lines = [
            f":_mod-docs-content-type: MAP",
            f":context: {slug}",
            "",
        ]

        # Add source comment
        lines.append(f"// Matched from {source}")
        lines.append("")

        for i, (mod_file, attrs) in enumerate(mod_includes):
            # Normalize attrs
            if i == 0:
                lines.append(
                    f'include::modules/{mod_file}[leveloffset=+0,chunk="to-content"]'
                )
            else:
                # Parse existing leveloffset or default to +1
                lo_match = re.search(r"leveloffset=(\+\d+)", attrs)
                lo = lo_match.group(1) if lo_match else "+1"
                lines.append(
                    f'include::modules/{mod_file}[leveloffset={lo},toc="no"]'
                )
            lines.append("")

        with open(fpath, "w") as f:
            f.write("\n".join(lines))
        filled += 1

    print(f"  Filled {filled} stubs with module includes")
    print(f"  Remaining stubs: {len(stubs) - filled}")
    return filled


# ─── Phase D: Fix broken relative include paths ───

def fix_broken_includes():
    """Convert ../topic/modules/X.adoc to modules/X.adoc in job files."""
    print("\n  Fixing broken relative include paths...")
    fixed_files = 0
    fixed_includes = 0

    for fname in sorted(os.listdir(JOBS_DIR)):
        if not fname.endswith(".adoc"):
            continue
        fpath = os.path.join(JOBS_DIR, fname)
        with open(fpath) as f:
            content = f.read()

        if "../" not in content:
            continue

        new_lines = []
        file_changed = False
        for line in content.split("\n"):
            if line.strip().startswith("include::") and "../" in line:
                # Extract the module filename from any relative path
                m = re.search(r"include::.*?/modules/([^[]+)\[(.+?)\]", line)
                if m:
                    mod_file = m.group(1)
                    attrs = m.group(2)
                    # Check if module exists in shared modules/
                    if os.path.exists(os.path.join(MODULES_DIR, mod_file)):
                        new_line = f"include::modules/{mod_file}[{attrs}]"
                        new_lines.append(new_line)
                        fixed_includes += 1
                        file_changed = True
                        continue
                    else:
                        # Module not in shared dir - mark with comment
                        new_lines.append(f"// FIXME: module not found in modules/: {mod_file}")
                        new_lines.append(line)
                        file_changed = True
                        continue
            new_lines.append(line)

        if file_changed:
            with open(fpath, "w") as f:
                f.write("\n".join(new_lines))
            fixed_files += 1

    print(f"  Fixed {fixed_includes} include paths across {fixed_files} files")
    return fixed_files


# ─── Phase E: Clean long filenames ───

def clean_long_filenames():
    """Shorten filenames >60 chars and update category map references."""
    print("\n  Cleaning long filenames...")
    renames = {}

    for fname in sorted(os.listdir(JOBS_DIR)):
        if not fname.endswith(".adoc"):
            continue
        slug = fname.replace(".adoc", "")
        if len(slug) <= 60:
            continue

        # Truncate intelligently
        words = slug.split("-")
        new_slug = ""
        for w in words:
            candidate = f"{new_slug}-{w}" if new_slug else w
            if len(candidate) > 55:
                break
            new_slug = candidate

        if not new_slug or new_slug == slug:
            new_slug = "-".join(words[:8])

        # Avoid collision
        base = new_slug
        counter = 0
        while os.path.exists(os.path.join(JOBS_DIR, f"{new_slug}.adoc")) and new_slug != slug:
            counter += 1
            new_slug = f"{base}-{counter}"

        if new_slug != slug:
            renames[slug] = new_slug

    # Apply renames
    for old_slug, new_slug in renames.items():
        old_path = os.path.join(JOBS_DIR, f"{old_slug}.adoc")
        new_path = os.path.join(JOBS_DIR, f"{new_slug}.adoc")

        # Update :context: inside file
        with open(old_path) as f:
            content = f.read()
        content = content.replace(f":context: {old_slug}", f":context: {new_slug}")
        with open(new_path, "w") as f:
            f.write(content)
        os.remove(old_path)

    # Update category map references
    if renames:
        for cat_file in os.listdir(CATS_DIR):
            if not cat_file.endswith(".adoc"):
                continue
            cat_path = os.path.join(CATS_DIR, cat_file)
            with open(cat_path) as f:
                content = f.read()
            changed = False
            for old_slug, new_slug in renames.items():
                old_ref = f"jobs-openshift-enterprise/{old_slug}.adoc"
                new_ref = f"jobs-openshift-enterprise/{new_slug}.adoc"
                if old_ref in content:
                    content = content.replace(old_ref, new_ref)
                    changed = True
            if changed:
                with open(cat_path, "w") as f:
                    f.write(content)

    print(f"  Renamed {len(renames)} files (slug > 60 chars)")
    if renames:
        for old, new in list(renames.items())[:10]:
            print(f"    {old}.adoc → {new}.adoc")
        if len(renames) > 10:
            print(f"    ... and {len(renames) - 10} more")

    return len(renames)


def main():
    print("=" * 70)
    print("Fill Stubs, Fix Paths, Clean Filenames")
    print("=" * 70)

    # Build indexes
    print("\n[Phase A] Building assembly index...")
    assemblies = build_assembly_index()

    print("\n[Phase B] Building module title index...")
    modules = build_module_index()

    # Fill stubs
    print("\n[Phase C] Filling stub jobs...")
    filled = fill_stubs(assemblies, modules)

    # Fix broken paths
    print("\n[Phase D] Fixing broken include paths...")
    fixed = fix_broken_includes()

    # Clean filenames
    print("\n[Phase E] Cleaning long filenames...")
    renamed = clean_long_filenames()

    # Summary
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"Stubs filled with module includes: {filled}")
    print(f"Files with fixed include paths: {fixed}")
    print(f"Files renamed (shortened): {renamed}")

    # Count remaining stubs
    remaining = 0
    for fname in os.listdir(JOBS_DIR):
        if not fname.endswith(".adoc"):
            continue
        with open(os.path.join(JOBS_DIR, fname)) as f:
            if "// TODO: Add module includes" in f.read():
                remaining += 1
    print(f"Remaining unfilled stubs: {remaining}")


if __name__ == "__main__":
    main()
