#!/usr/bin/env python3
"""
Build include graph from AsciiDoc assembly files
"""

import json
import re
from pathlib import Path

def detect_module_type(module_path, base_dir):
    """Detect module type from filename prefix or metadata"""
    filename = Path(module_path).name.lower()

    # Try filename prefix first
    if filename.startswith('con-'):
        return 'CONCEPT'
    elif filename.startswith('proc-'):
        return 'PROCEDURE'
    elif filename.startswith('ref-'):
        return 'REFERENCE'
    elif filename.startswith('snip-'):
        return 'SNIPPET'

    # Try to read module file and extract :_mod-docs-content-type: metadata
    try:
        # Resolve module path relative to base_dir
        full_path = Path(base_dir) / module_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                # Read first 10 lines to find metadata
                for _ in range(10):
                    line = f.readline()
                    if not line:
                        break
                    if ':_mod-docs-content-type:' in line:
                        # Extract the type (e.g., ":_mod-docs-content-type: PROCEDURE")
                        parts = line.split(':')
                        if len(parts) >= 3:
                            content_type = parts[2].strip().upper()
                            return content_type
    except Exception:
        pass

    return 'UNKNOWN'


def parse_assembly(assembly_path, assembly_name, base_dir):
    """Parse an assembly file and extract include information"""
    includes = []

    try:
        with open(assembly_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR reading {assembly_path}: {e}")
        return includes

    # Pattern to match include:: directives
    include_pattern = re.compile(r'^include::([^\[]+)\[([^\]]*)\]', re.MULTILINE)

    for match in include_pattern.finditer(content):
        include_path = match.group(1)
        include_attrs = match.group(2)

        # Extract leveloffset if present
        leveloffset = None
        leveloffset_match = re.search(r'leveloffset=([+-]?\d+)', include_attrs)
        if leveloffset_match:
            leveloffset = leveloffset_match.group(1)

        # Determine module type
        module_type = detect_module_type(include_path, base_dir)

        includes.append({
            'assembly': assembly_name,
            'module_path': include_path,
            'module_type': module_type,
            'leveloffset': leveloffset
        })

    return includes


def main():
    import sys

    if len(sys.argv) < 4:
        print("Usage: build_include_graph.py <output_json> <base_dir> <assembly1> [assembly2] ...")
        sys.exit(1)

    output_file = sys.argv[1]
    base_dir = sys.argv[2]
    assembly_files = sys.argv[3:]

    include_graph = []

    for assembly_file in assembly_files:
        assembly_path = Path(assembly_file)
        assembly_name = assembly_path.stem  # filename without extension

        print(f"Parsing assembly: {assembly_name}")
        includes = parse_assembly(assembly_path, assembly_name, base_dir)
        include_graph.extend(includes)

    # Write JSON output
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(include_graph, f, indent=2)

    print(f"\nInclude graph written to: {output_file}")
    print(f"Total includes: {len(include_graph)}")

    # Summary by module type
    type_counts = {}
    for item in include_graph:
        mtype = item['module_type']
        type_counts[mtype] = type_counts.get(mtype, 0) + 1

    print("\nModule types:")
    for mtype, count in sorted(type_counts.items()):
        print(f"  {mtype}: {count}")


if __name__ == "__main__":
    main()
