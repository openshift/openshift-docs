#!/usr/bin/env python3

"""Format AsciiDoc spacing - ensures blank lines after headings and around include directives"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple


# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'  # No Color


def print_colored(message: str, color: str = Colors.NC) -> None:
    """Print message with color"""
    print(f"{color}{message}{Colors.NC}")


def process_file(file_path: Path, dry_run: bool = False, verbose: bool = False) -> bool:
    """
    Process a single AsciiDoc file to fix spacing issues.

    Args:
        file_path: Path to the file to process
        dry_run: If True, show what would be changed without modifying
        verbose: If True, show detailed output

    Returns:
        True if changes were made (or would be made in dry-run), False otherwise
    """
    if verbose:
        print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except (IOError, UnicodeDecodeError) as e:
        print_colored(f"Error reading {file_path}: {e}", Colors.RED)
        return False

    # Remove trailing newlines from lines for processing
    lines = [line.rstrip('\n\r') for line in lines]

    new_lines = []
    changes_made = False

    for i, current_line in enumerate(lines):
        prev_line = lines[i-1] if i > 0 else ""
        next_line = lines[i+1] if i + 1 < len(lines) else ""

        # Check if current line is a heading
        if re.match(r'^=+', current_line):
            new_lines.append(current_line)

            # Check if next line is not empty and not another heading
            if (next_line and
                not re.match(r'^=+', next_line) and
                not re.match(r'^\s*$', next_line)):
                new_lines.append("")
                changes_made = True
                if verbose:
                    truncated = current_line[:50] + "..." if len(current_line) > 50 else current_line
                    print(f"  Added blank line after heading: {truncated}")

        # Check if current line is an include directive
        elif re.match(r'^include::', current_line):
            # Add blank line before include if previous line is not empty and not an include
            if (prev_line and
                not re.match(r'^\s*$', prev_line) and
                not re.match(r'^include::', prev_line)):
                new_lines.append("")
                changes_made = True
                if verbose:
                    truncated = current_line[:50] + "..." if len(current_line) > 50 else current_line
                    print(f"  Added blank line before include: {truncated}")

            new_lines.append(current_line)

            # Add blank line after include if next line exists and is not empty and not an include
            if (next_line and
                not re.match(r'^\s*$', next_line) and
                not re.match(r'^include::', next_line)):
                new_lines.append("")
                changes_made = True
                if verbose:
                    truncated = current_line[:50] + "..." if len(current_line) > 50 else current_line
                    print(f"  Added blank line after include: {truncated}")

        else:
            new_lines.append(current_line)

    # Apply changes if any were made
    if changes_made:
        if dry_run:
            print_colored(f"Would modify: {file_path}", Colors.YELLOW)
        else:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    for line in new_lines:
                        f.write(line + '\n')
                print_colored(f"Modified: {file_path}", Colors.GREEN)
            except IOError as e:
                print_colored(f"Error writing {file_path}: {e}", Colors.RED)
                return False
    else:
        if verbose:
            print("  No changes needed")

    return changes_made


def find_adoc_files(path: Path) -> List[Path]:
    """Find all .adoc files in the given path"""
    adoc_files = []

    if path.is_file():
        if path.suffix == '.adoc':
            adoc_files.append(path)
        else:
            print_colored(f"Warning: {path} is not an AsciiDoc file (.adoc)", Colors.YELLOW)
    elif path.is_dir():
        adoc_files = list(path.rglob('*.adoc'))

    return adoc_files


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Format AsciiDoc files to ensure proper spacing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Format AsciiDoc files to ensure proper spacing:
- Blank line after headings (=, ==, ===, etc.)
- Blank lines around include:: directives

Examples:
  %(prog)s                                    # Process all .adoc files in current directory
  %(prog)s modules/                          # Process all .adoc files in modules/
  %(prog)s assemblies/my-guide.adoc          # Process single file
  %(prog)s --dry-run modules/               # Preview changes without modifying
        """
    )

    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='File or directory to process (default: current directory)'
    )
    parser.add_argument(
        '-n', '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output'
    )

    args = parser.parse_args()

    # Convert path to Path object
    target_path = Path(args.path)

    # Check if path exists
    if not target_path.exists():
        print_colored(f"Error: Path does not exist: {target_path}", Colors.RED)
        sys.exit(1)

    # Display dry-run mode message
    if args.dry_run:
        print_colored("DRY RUN MODE - No files will be modified", Colors.YELLOW)

    # Find all AsciiDoc files
    adoc_files = find_adoc_files(target_path)

    if not adoc_files:
        print(f"Processed 0 AsciiDoc file(s)")
        print("AsciiDoc spacing formatting complete!")
        return

    # Process each file
    files_processed = 0
    for file_path in adoc_files:
        try:
            process_file(file_path, args.dry_run, args.verbose)
            files_processed += 1
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled by user", Colors.YELLOW)
            sys.exit(1)
        except Exception as e:
            print_colored(f"Unexpected error processing {file_path}: {e}", Colors.RED)

    print(f"Processed {files_processed} AsciiDoc file(s)")
    print("AsciiDoc spacing formatting complete!")


if __name__ == "__main__":
    main()