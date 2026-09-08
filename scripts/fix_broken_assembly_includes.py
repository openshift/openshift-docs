#!/usr/bin/env python3
"""
Fix broken assembly includes in job map files.

These are includes like:
  include::../storage/persistent_storage_local/persistent-storage-local.adoc[...]
that resolve to maps/storage/... (doesn't exist).

The actual file is at repo root: storage/persistent_storage_local/persistent-storage-local.adoc

If the target is an assembly, decompose it into its constituent module includes.
If the target is a module, rewrite as modules/<filename>.adoc.
If the target doesn't exist, mark with // FIXME comment.
"""

import os
import re

REPO = "/home/avbhatt/ocp-repos/openshift-docs"
JOBS_DIR = os.path.join(REPO, "maps", "jobs-openshift-enterprise")
MODULES_DIR = os.path.join(REPO, "modules")


def find_actual_path(broken_include, job_file_dir):
    """Given an include path relative to the job file, find the actual repo path."""
    # The include is relative to maps/jobs-openshift-enterprise/
    # ../foo/bar.adoc → maps/foo/bar.adoc (doesn't exist)
    # The ACTUAL file is at repo root: foo/bar.adoc

    m = re.search(r"include::(.+?)\[", broken_include)
    if not m:
        return None

    inc_path = m.group(1)

    # If it starts with ../, strip the ../ and check at repo root
    if inc_path.startswith("../"):
        # From maps/jobs-openshift-enterprise/, ../ goes to maps/
        # So ../foo/bar = maps/foo/bar which should be foo/bar at repo root
        repo_path = inc_path.replace("../", "", 1)
        full = os.path.join(REPO, repo_path)
        if os.path.exists(full):
            return full

        # Try one more level: ../../foo/bar (repo root)
        repo_path2 = inc_path.replace("../", "", 1)
        # The maps/ doesn't exist at repo root, so just try the path directly
        # Sometimes the include uses ../topic/subtopic/file.adoc
        # where topic/subtopic/file.adoc exists at repo root
        return full if os.path.exists(full) else None

    # modules/ path that doesn't resolve
    if inc_path.startswith("modules/"):
        mod_file = inc_path.replace("modules/", "")
        full = os.path.join(MODULES_DIR, mod_file)
        return full if os.path.exists(full) else None

    return None


def extract_module_includes_from_assembly(asm_path):
    """Read an assembly and extract its include::modules/... lines."""
    try:
        with open(asm_path, "r", errors="replace") as f:
            content = f.read()
    except:
        return []

    modules = []
    for line in content.split("\n"):
        line = line.strip()
        if not line.startswith("include::"):
            continue
        # Extract module filename from various include patterns
        m = re.search(r"include::.*?modules/([^[]+)\[(.+?)\]", line)
        if m:
            mod_file = m.group(1)
            attrs = m.group(2)
            # Verify it exists in shared modules/
            if os.path.exists(os.path.join(MODULES_DIR, mod_file)):
                modules.append((mod_file, attrs))

    return modules


def is_assembly(filepath):
    """Check if a file is an assembly."""
    try:
        with open(filepath, "r", errors="replace") as f:
            head = f.read(500)
        return ":_mod-docs-content-type: ASSEMBLY" in head
    except:
        return False


def fix_job_file(job_path):
    """Fix broken includes in a job file by decomposing assemblies."""
    with open(job_path) as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    fixed = False
    is_first_include = True

    for line in lines:
        stripped = line.strip()

        if not stripped.startswith("include::"):
            new_lines.append(line)
            continue

        # Check if this include has a broken path (../something that's not modules/)
        if "../" in stripped and "modules/" not in stripped.split("[")[0].split("/")[-2:][0]:
            # This includes a non-module file via relative path
            actual_path = find_actual_path(stripped, JOBS_DIR)

            if actual_path and os.path.exists(actual_path):
                if is_assembly(actual_path):
                    # Decompose assembly into its modules
                    rel_asm = os.path.relpath(actual_path, REPO)
                    new_lines.append(f"// Decomposed from {rel_asm}")
                    modules = extract_module_includes_from_assembly(actual_path)

                    if modules:
                        for i, (mod_file, attrs) in enumerate(modules):
                            if is_first_include and i == 0:
                                new_lines.append(
                                    f'include::modules/{mod_file}[leveloffset=+0,chunk="to-content"]'
                                )
                                is_first_include = False
                            else:
                                lo_match = re.search(r"leveloffset=(\+\d+)", attrs)
                                lo = lo_match.group(1) if lo_match else "+1"
                                new_lines.append(
                                    f'include::modules/{mod_file}[leveloffset={lo},toc="no"]'
                                )
                            new_lines.append("")
                        fixed = True
                    else:
                        new_lines.append(f"// FIXME: assembly has no module includes: {rel_asm}")
                        new_lines.append(stripped)
                        fixed = True
                else:
                    # It's a module or other file — check if it exists in shared modules/
                    basename = os.path.basename(actual_path)
                    if os.path.exists(os.path.join(MODULES_DIR, basename)):
                        m = re.search(r"\[(.+?)\]", stripped)
                        attrs = m.group(1) if m else "leveloffset=+1"
                        if is_first_include:
                            new_lines.append(
                                f'include::modules/{basename}[leveloffset=+0,chunk="to-content"]'
                            )
                            is_first_include = False
                        else:
                            new_lines.append(
                                f'include::modules/{basename}[{attrs},toc="no"]'
                            )
                        new_lines.append("")
                        fixed = True
                    else:
                        new_lines.append(f"// FIXME: cannot resolve to shared modules/: {basename}")
                        new_lines.append(stripped)
                        fixed = True
            else:
                # File doesn't exist at all
                m = re.search(r"include::(.+?)\[", stripped)
                inc_path = m.group(1) if m else "unknown"
                new_lines.append(f"// FIXME: file not found: {inc_path}")
                new_lines.append(f"// {stripped}")
                fixed = True
                is_first_include = False
        else:
            new_lines.append(line)
            if stripped.startswith("include::"):
                is_first_include = False

    if fixed:
        with open(job_path, "w") as f:
            f.write("\n".join(new_lines))

    return fixed


def main():
    print("=" * 70)
    print("Fix Broken Assembly Includes")
    print("=" * 70)

    fixed_count = 0
    total_checked = 0

    for fname in sorted(os.listdir(JOBS_DIR)):
        if not fname.endswith(".adoc"):
            continue
        fpath = os.path.join(JOBS_DIR, fname)
        with open(fpath) as f:
            content = f.read()

        # Skip stubs
        if "// TODO: Add module includes" in content:
            continue

        # Check for broken includes (non-module ../ paths)
        has_broken = False
        for line in content.split("\n"):
            if line.strip().startswith("include::") and "../" in line:
                # Check if it's a module include (already fixed) or assembly include
                inc_part = line.split("[")[0].replace("include::", "")
                if not inc_part.startswith("modules/"):
                    has_broken = True
                    break

        if not has_broken:
            continue

        total_checked += 1
        if fix_job_file(fpath):
            fixed_count += 1
            if fixed_count <= 10:
                print(f"  Fixed: {fname}")

    if fixed_count > 10:
        print(f"  ... and {fixed_count - 10} more")

    print(f"\nTotal files checked: {total_checked}")
    print(f"Files fixed: {fixed_count}")


if __name__ == "__main__":
    main()
