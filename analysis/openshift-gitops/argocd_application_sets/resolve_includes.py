#!/usr/bin/env python3
"""
Manual AsciiDoc include resolver
Recursively resolves include:: directives in AsciiDoc files
"""

import os
import re
from pathlib import Path

def resolve_includes(file_path, base_dir, visited=None, depth=0, max_depth=10):
    """
    Recursively resolve include:: directives in an AsciiDoc file

    Args:
        file_path: Path to the file to process
        base_dir: Base directory for resolving relative includes
        visited: Set of already visited files to prevent infinite loops
        depth: Current recursion depth
        max_depth: Maximum recursion depth to prevent stack overflow

    Returns:
        String with all includes resolved
    """
    if visited is None:
        visited = set()

    if depth > max_depth:
        return f"// ERROR: Maximum include depth ({max_depth}) exceeded\n"

    # Convert to absolute path
    abs_path = Path(file_path).resolve()

    # Check for circular includes
    if str(abs_path) in visited:
        return f"// WARNING: Circular include detected: {abs_path}\n"

    visited.add(str(abs_path))

    # Check if file exists
    if not abs_path.exists():
        return f"// ERROR: Include file not found: {file_path}\n"

    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return f"// ERROR reading {abs_path}: {e}\n"

    # Pattern to match include:: directives
    # include::path/to/file.adoc[leveloffset=+1]
    include_pattern = re.compile(r'^include::([^\[]+)\[(.*?)\]', re.MULTILINE)

    def replace_include(match):
        include_path = match.group(1)
        include_attrs = match.group(2)

        # Resolve the include path relative to the current file's directory
        current_dir = abs_path.parent
        resolved_path = (current_dir / include_path).resolve()

        # Recursively resolve the included file
        included_content = resolve_includes(
            resolved_path,
            base_dir,
            visited.copy(),  # Pass a copy to allow the same file in different branches
            depth + 1,
            max_depth
        )

        # Add a comment to show where this content came from
        header = f"// BEGIN INCLUDE: {include_path}\n"
        footer = f"// END INCLUDE: {include_path}\n"

        return header + included_content + footer

    # Replace all includes
    resolved_content = include_pattern.sub(replace_include, content)

    return resolved_content


def main():
    import sys

    if len(sys.argv) < 3:
        print("Usage: resolve_includes.py <input_file> <output_file> [base_dir]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    base_dir = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(input_file)

    print(f"Resolving includes in: {input_file}")
    print(f"Base directory: {base_dir}")

    resolved = resolve_includes(input_file, base_dir)

    # Write the resolved content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(resolved)

    print(f"Resolved content written to: {output_file}")

    # Count lines
    line_count = len(resolved.splitlines())
    print(f"Total lines: {line_count}")


if __name__ == "__main__":
    main()
