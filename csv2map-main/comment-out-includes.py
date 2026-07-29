#!/usr/bin/env python3
"""
Comment out AsciiDoc include directives in ASSEMBLY and IGNORE files.

Finds all .adoc files under the given path. Each file must declare a content
type via :_mod-docs-content-type: (preferred) or :_content-type:. Files
without either attribute are skipped with a warning. Only files whose content
type is ASSEMBLY or IGNORE (case-insensitive) have their include:: lines
commented out.
"""

import argparse
import logging
import os
import re
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

PROCESS_TYPES = {'assembly', 'ignore'}

_MOD_CONTENT_TYPE_RE = re.compile(r'''
    ^                           # start of a line (MULTILINE makes ^ match after each newline)
    :_mod-docs-content-type:   # exact attribute name enclosed in colons
    \s*                         # zero or more spaces between the colon and the value
    (\S+)                       # capture group: one or more non-whitespace chars = the value
''', re.MULTILINE | re.VERBOSE)

_CONTENT_TYPE_RE = re.compile(r'''
    ^                   # start of a line
    :_content-type:     # exact attribute name enclosed in colons
    \s*                 # zero or more spaces between the colon and the value
    (\S+)               # capture group: one or more non-whitespace chars = the value
''', re.MULTILINE | re.VERBOSE)

_MODULE_TYPE_RE = re.compile(r'''
    ^               # start of a line
    :_module-type:  # exact attribute name enclosed in colons
    \s*             # zero or more spaces between the colon and the value
    (\S+)           # capture group: one or more non-whitespace chars = the value
''', re.MULTILINE | re.VERBOSE)


def get_content_type(filepath: str, text: str) -> str | None:
    """Return the effective content type, warning about duplicates. None if absent."""
    mod_matches = _MOD_CONTENT_TYPE_RE.findall(text)
    ct_matches = _CONTENT_TYPE_RE.findall(text)
    module_matches = _MODULE_TYPE_RE.findall(text)

    if len(mod_matches) + len(ct_matches) + len(module_matches) > 1:
        logger.warning(f"{filepath}: multiple content type definitions found")

    if mod_matches:
        return mod_matches[0]
    if ct_matches:
        return ct_matches[0]
    if module_matches:
        return module_matches[0]
    return None


def comment_out_includes(filepath: str) -> int:
    """Comment out include:: lines if the file content type warrants it. Returns change count."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    content_type = get_content_type(filepath, text)
    if content_type is None:
        logger.warning(f"{filepath}: no content type attribute found, skipping")
        return 0

    if content_type.lower() not in PROCESS_TYPES:
        logger.debug(f"{filepath}: content type '{content_type}', skipping")
        return 0

    is_ignore = content_type.lower() == 'ignore'
    IGNORE_WARNING = ('*WARNING: a file with the content type IGNORE should not be in your build.'
                      ' Review your Asciidoc maps or change the content type*\n')

    lines = text.splitlines(keepends=True)
    after_header = False
    warning_inserted = False
    changed = 0
    new_lines = []
    for line in lines:
        if not after_header and line.startswith('= '):
            after_header = True
            new_lines.append(line)
            if is_ignore:
                new_lines.append(IGNORE_WARNING)
                warning_inserted = True
            continue
        if after_header and line.lstrip().startswith('include::'):
            new_lines.append('// ' + line)
            changed += 1
        else:
            new_lines.append(line)

    if not after_header:
        if is_ignore:
            new_lines.insert(0, IGNORE_WARNING)
            warning_inserted = True
        else:
            logger.warning(f"{filepath}: no level-1 header found, skipping")
            return 0

    if is_ignore:
        logger.warning(f"{filepath}: content type IGNORE — this file should not be in your build")

    if changed or warning_inserted:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        logger.info(f"{filepath}: content type '{content_type}', commented out {changed} include(s)")

    return changed


def collect_adoc_files(path: str):
    """Yield .adoc file paths under path (recursively if directory)."""
    if os.path.isfile(path):
        if path.endswith('.adoc'):
            yield path
    else:
        for root, _dirs, files in os.walk(path):
            for name in files:
                if name.endswith('.adoc'):
                    yield os.path.join(root, name)


def main():
    parser = argparse.ArgumentParser(
        description=(
            'Comment out AsciiDoc include:: directives. '
            'Accepts a file or directory path (use . for the current directory). '
            'Every include:: line in each .adoc file found is prefixed with "// " '
            'so it is disabled but remains visible in the source.'
        )
    )
    parser.add_argument(
        'path',
        nargs='?',
        help='File or directory to process (.adoc files are searched recursively)',
    )
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logging')

    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    if args.path is None:
        parser.print_help()
        sys.exit(0)

    if not os.path.exists(args.path):
        logger.error(f"Path does not exist: {args.path}")
        sys.exit(1)

    total_files = 0
    total_includes = 0
    for filepath in collect_adoc_files(args.path):
        total_files += 1
        total_includes += comment_out_includes(filepath)

    if total_files == 0:
        logger.warning(f"No .adoc files found under: {args.path}")
    else:
        logger.info(f"Processed {total_files} file(s), commented out {total_includes} include(s) total")


if __name__ == '__main__':
    main()
