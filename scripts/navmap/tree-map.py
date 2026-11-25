#!/usr/bin/env python3
"""
tree-map.py - Visualize the hierarchical include structure of navigation maps

Displays a tree view showing how jobs and modules are nested within category maps.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Set, Optional, List, Dict

from job_comparison import MapComparison, compare_job_includes

# ANSI color codes
class Colors:
    CATEGORY = '\033[1;34m'  # Bold Blue
    JOB = '\033[0;36m'       # Cyan
    MODULE = '\033[0;32m'    # Green
    SNIPPET = '\033[0;33m'   # Yellow
    ERROR = '\033[0;31m'     # Red
    WARNING = '\033[1;33m'   # Bold Yellow
    RESET = '\033[0m'        # Reset
    GRAY = '\033[0;90m'      # Gray

# Tree drawing characters
TREE_BRANCH = "├── "
TREE_LAST = "└── "
TREE_PIPE = "│   "
TREE_SPACE = "    "

# Validation issue tracking
class ValidationIssue:
    def __init__(self, level: str, message: str, file_path: Path, line: Optional[int] = None):
        self.level = level  # 'ERROR' or 'WARNING'
        self.message = message
        self.file_path = file_path
        self.line = line

class ValidationTracker:
    def __init__(self):
        self.errors: List[ValidationIssue] = []
        self.warnings: List[ValidationIssue] = []
        self.redundancies: List[Dict] = []  # Parent-child redundancy tracking
        self.heading_cache: Dict[Path, Optional[list]] = {}
        self.compared_jobs = 0
        self.identical_job_groups: Dict[tuple, str] = {}

    def add_error(self, message: str, file_path: Path, line: Optional[int] = None):
        self.errors.append(ValidationIssue('ERROR', message, file_path, line))

    def add_warning(self, message: str, file_path: Path, line: Optional[int] = None):
        self.warnings.append(ValidationIssue('WARNING', message, file_path, line))

    def add_redundancy(self, module: Path, child_file: Path, child_line: int,
                       parent_file: Path, parent_line: int):
        self.redundancies.append({
            'module': module,
            'child_file': child_file,
            'child_line': child_line,
            'parent_file': parent_file,
            'parent_line': parent_line
        })

    def has_issues(self):
        return len(self.errors) > 0 or len(self.warnings) > 0 or len(self.redundancies) > 0

    def has_errors(self):
        return len(self.errors) > 0

def parse_includes(file_path: Path) -> list:
    """Extract include directives from an AsciiDoc file."""
    includes = []

    in_comment = False
    with file_path.open(encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if line.strip() == '////':
                in_comment = not in_comment
                continue
            if in_comment:
                continue
            # Match include:: directives
            match = re.match(r'^\s*include::([^\[]+)\[(.*)\]', line)
            if match:
                include_path = match.group(1).strip()
                attributes = match.group(2) or ''

                # Extract leveloffset if present
                leveloffset = None
                leveloffset_match = re.search(r'(?:^|,)\s*leveloffset\s*=\s*["\']?([+-]?\d+)["\']?\s*(?:,|$)', attributes)
                if leveloffset_match:
                    leveloffset = leveloffset_match.group(1)

                includes.append({
                    'path': include_path,
                    'line': line_num,
                    'leveloffset': leveloffset
                })
    return includes

def resolve_include_path(include_path: str, current_file: Path) -> Optional[Path]:
    """Resolve an include path relative to the current file."""
    # Try relative to current file's directory
    current_dir = current_file.parent
    resolved = current_dir / include_path

    if resolved.is_file():
        return resolved

    return None

def classify_file(file_path: Path) -> str:
    """Classify file type based on path."""
    file_path = file_path.resolve()
    path_str = str(file_path)

    # Check modules and snippets first (they can be under ocp-jobs/)
    if '/modules/' in path_str:
        return 'module'
    elif '/snippets/' in path_str:
        return 'snippet'
    # Check job directories (handle both maps/ocp-jobs/ and maps/ocp/ocp-jobs/ symlink)
    elif any(part == 'jobs' or part.endswith('-jobs') for part in file_path.parts[:-1]):
        return 'job'
    elif file_path.parent.parent.name == 'maps' and file_path.name != 'navigation.adoc':
        return 'category'
    else:
        return 'other'


def cached_includes(file_path: Path, include_cache: dict) -> list:
    """Read and resolve a file's includes once for analysis and display."""
    if file_path not in include_cache:
        include_cache[file_path] = [
            dict(inc, resolved=resolve_include_path(inc['path'], file_path))
            for inc in parse_includes(file_path)
        ]
    return include_cache[file_path]


def prepare_include_tree(file_path, include_cache, max_depth=None, depth=0, visited=frozenset()):
    """Cache exactly the traversal that will be displayed, without printing it."""
    canonical = file_path.resolve()
    if canonical in visited or (max_depth is not None and depth >= max_depth):
        return
    try:
        includes = cached_includes(file_path, include_cache)
    except (OSError, UnicodeError):
        return  # The display pass reports the read failure through its validator.
    for include in includes:
        target = include['resolved']
        if target and (classify_file(target) in ('category', 'job') or max_depth is not None):
            prepare_include_tree(target, include_cache, max_depth, depth + 1, visited | {canonical})


def get_color(file_type: str) -> str:
    """Get color code for file type."""
    colors = {
        'category': Colors.CATEGORY,
        'job': Colors.JOB,
        'module': Colors.MODULE,
        'snippet': Colors.SNIPPET,
        'other': Colors.RESET
    }
    return colors.get(file_type, Colors.RESET)

def get_type_marker(file_type: str) -> str:
    """Get type marker for file."""
    markers = {
        'category': '[CAT]',
        'job': '[JOB]',
        'module': '[MOD]',
        'snippet': '[SNP]',
        'other': '[---]'
    }
    return markers.get(file_type, '[???]')

def display_path(file_path: Path, repo_root: Path) -> str:
    """Keep source paths distinct in diagnostics without an absolute repo prefix."""
    try:
        return str(file_path.relative_to(repo_root))
    except ValueError:
        return str(file_path)

def heading_events(file_path: Path, cache: dict) -> Optional[list]:
    """Read literal headings and include positions, leaving uncertain content unknown.

    Heading levels use AsciiDoc section numbering: a document title is level 0.
    Delimited examples are excluded so sample headings do not affect the outline.
    """
    canonical = file_path.resolve()
    if canonical in cache:
        return cache[canonical]
    events = []
    delimiter = None
    conditional_depth = 0
    try:
        source = file_path.read_text(encoding='utf-8')
    except (OSError, UnicodeError):
        cache[canonical] = None
        return None
    for line_number, line in enumerate(source.splitlines(), 1):
        stripped = line.strip()
        if delimiter:
            if stripped == delimiter:
                delimiter = None
            continue
        if re.fullmatch(r'(?:/{4,}|-{4,}|\.{4,}|\+{4,}|={4,}|\*{4,}|_{4,}|`{3,}|~{3,}|\|===)', stripped):
            delimiter = stripped
            continue
        if stripped.startswith('//'):
            continue
        if re.match(r'(?:ifdef|ifndef|ifeval)::', stripped):
            if stripped.endswith('[]') or stripped.startswith('ifeval::'):
                conditional_depth += 1
            elif re.search(r'include::|\[=+\s|:leveloffset', stripped):
                events.append((line_number, None))
            continue
        if stripped.startswith('endif::'):
            conditional_depth = max(0, conditional_depth - 1)
            continue
        if conditional_depth:
            if re.match(r'(?:=+\s|include::|:leveloffset)', stripped):
                events.append((line_number, None))
            continue
        if re.match(r':leveloffset[!:]|:!leveloffset:', stripped):
            # Attribute-driven offsets require an Asciidoctor evaluation.
            cache[canonical] = None
            return None
        heading = re.match(r'^(=+)\s+\S', line)
        if heading:
            events.append((line_number, len(heading.group(1)) - 1))
        elif re.match(r'^\s*include::', line):
            events.append((line_number, ('include', line)))
    cache[canonical] = events
    return events


def validate_leveloffsets(includes: list, file_path: Path,
                          validator: ValidationTracker) -> Dict[int, str]:
    """Warn about demonstrable heading gaps, rather than differing offsets."""
    events = heading_events(file_path, validator.heading_cache)
    if events is None:
        return {}
    by_line = {inc['line']: (index, inc) for index, inc in enumerate(includes)}
    issues = {}
    previous_level = 0  # The enclosing map/job provides the parent context.
    for line, event in events:
        if event is None:
            previous_level = None
            continue
        if isinstance(event, int):
            previous_level = event
            continue
        if line not in by_line:
            previous_level = None
            continue
        index, inc = by_line[line]
        target = inc['resolved']
        if target is None:
            previous_level = None
            continue
        offset = inc['leveloffset']
        # Unsigned absolute offsets and unresolved attributes depend on the
        # inherited rendering context. Partial includes can omit headings.
        source_line = event[1]
        if ((offset is not None and not offset.startswith(('+', '-')))
                or ('leveloffset' in source_line and offset is None)
                or re.search(r'\b(?:tags?|lines)\s*=', source_line)):
            previous_level = None
            continue
        outline = heading_events(target, validator.heading_cache)
        if outline is None or any(not isinstance(level, int) for _, level in outline):
            previous_level = None
            continue
        if not outline:
            continue  # Headingless content does not change the outline.
        shift = int(offset or 0)
        first_level = outline[0][1] + shift
        last_level = outline[-1][1] + shift
        message = None
        if first_level < 0:
            message = f"leveloffset={offset} places a heading above its containing document"
        elif previous_level is not None and first_level > previous_level + 1:
            message = (f"leveloffset={offset or '(unset)'} skips a parent heading "
                       f"(section level {previous_level} to {first_level})")
        if message:
            validator.add_warning(message, file_path, inc['line'])
            issues[index] = 'WARNING'
        previous_level = last_level
    return issues

def build_tree(
    file_path: Path,
    repo_root: Path,
    prefix: str = "",
    visited: Optional[Set[Path]] = None,
    show_line_numbers: bool = False,
    show_leveloffset: bool = False,
    max_depth: Optional[int] = None,
    current_depth: int = 0,
    no_color: bool = False,
    validator: Optional[ValidationTracker] = None,
    check_redundancy: bool = False,
    parent_modules: Optional[Dict[Path, tuple]] = None,
    validate_offsets: bool = True,
    include_cache: Optional[Dict[Path, list]] = None,
    job_annotations: Optional[Dict[tuple, str]] = None,
    comparison_category: Optional[Path] = None,
) -> None:
    """Recursively build and print the include tree."""

    if visited is None:
        visited = set()

    if parent_modules is None:
        parent_modules = {}
    if include_cache is None:
        include_cache = {}

    # Check for circular includes
    canonical = file_path.resolve()
    if classify_file(file_path) == 'category' or comparison_category is None:
        comparison_category = canonical
    if canonical in visited:
        marker = "(circular reference)" if no_color else f"{Colors.ERROR}(circular reference){Colors.RESET}"
        print(f"{prefix}{marker}")
        if validator:
            validator.add_error("Circular include reference", file_path)
        return

    visited = visited | {canonical}

    # Check max depth
    if max_depth is not None and current_depth >= max_depth:
        marker = "..." if no_color else f"{Colors.GRAY}...{Colors.RESET}"
        print(f"{prefix}{marker}")
        return

    # Get includes from this file
    try:
        includes = cached_includes(file_path, include_cache)
    except (OSError, UnicodeError) as exc:
        if validator:
            validator.add_error(f"Cannot read file: {exc}", file_path)
        else:
            print(f"Error reading {file_path}: {exc}", file=sys.stderr)
            raise SystemExit(1)
        return

    # Check heading continuity when the source outline is unambiguous.
    offset_issues = validate_leveloffsets(includes, file_path, validator) if validator and validate_offsets else {}

    # Collect every direct module before descending, including modules listed
    # after a child job. Keep the nearest ancestor's source location.
    child_parent_modules = parent_modules
    if check_redundancy:
        child_parent_modules = parent_modules.copy()
        for inc in includes:
            target = inc['resolved']
            if target and classify_file(target) == 'module':
                child_parent_modules[target.resolve()] = (file_path, inc['line'])

    for i, include_info in enumerate(includes):
        # Build tree characters
        if i == len(includes) - 1:
            branch = TREE_LAST
            extension = TREE_SPACE
        else:
            branch = TREE_BRANCH
            extension = TREE_PIPE

        # Resolve include path
        included_file = include_info['resolved']

        if included_file is None:
            # File not found - ERROR
            display_name = include_info['path']
            if no_color:
                marker = "[MISSING]"
            else:
                marker = f"{Colors.ERROR}[MISSING]{Colors.RESET}"

            line_info = f" (line {include_info['line']})" if show_line_numbers else ""
            print(f"{prefix}{branch}{marker} {display_name}{line_info}")

            if validator:
                validator.add_error(f"Missing file: {display_name}", file_path, include_info['line'])
            continue

        # Classify and colorize
        file_type = classify_file(included_file)
        color = "" if no_color else get_color(file_type)
        reset = "" if no_color else Colors.RESET
        type_marker = get_type_marker(file_type)

        # Build display name
        display_name = included_file.name
        comparison_marker = (job_annotations or {}).get((comparison_category, included_file.resolve()), '')
        if comparison_marker:
            comparison_marker = ' ' + comparison_marker
        identical_marker = ''
        if validator:
            group = validator.identical_job_groups.get((comparison_category, included_file.resolve()))
            if group:
                marker = f'[IDENTICAL {group}]'
                identical_marker = ' ' + (marker if no_color else f'{Colors.WARNING}{marker}{reset}')

        # Check for parent-child redundancy (modules only)
        redundancy_marker = ""
        if check_redundancy and file_type == 'module':
            if included_file.resolve() in parent_modules:
                parent_info = parent_modules[included_file.resolve()]
                redundancy_marker = " 🔁" if not no_color else " [REUSED]"
                if validator:
                    validator.add_redundancy(
                        included_file,
                        file_path,
                        include_info['line'],
                        parent_info[0],  # parent file
                        parent_info[1]   # parent line
                    )

        issue_marker = ""
        if i in offset_issues:
            issue_marker = " ⚠️" if not no_color else " [WARN]"

        # Add optional information
        extras = []
        if show_line_numbers:
            extras.append(f"line {include_info['line']}")
        if show_leveloffset and include_info['leveloffset']:
            extras.append(f"leveloffset={include_info['leveloffset']}")

        extra_info = f" ({', '.join(extras)})" if extras else ""

        # Print this node
        gray = "" if no_color else Colors.GRAY
        warning_color = "" if no_color or not issue_marker else Colors.WARNING
        redundancy_color = "" if no_color else (Colors.WARNING if redundancy_marker else "")
        print(f"{prefix}{branch}{color}{type_marker} {display_name}{reset}{gray}{extra_info}{reset}{warning_color}{issue_marker}{reset}{redundancy_color}{redundancy_marker}{reset}{comparison_marker}{identical_marker}")

        # Recurse for non-module files (to avoid too much depth in typical cases)
        # But allow modules if explicitly requested via max_depth
        if file_type in ['category', 'job'] or (max_depth is not None):
            if included_file.resolve() in visited:
                print(f"{prefix}{extension}(circular reference)")
                if validator:
                    validator.add_error(f"Circular include reference: {included_file.name}", file_path, include_info['line'])
                continue
            build_tree(
                included_file,
                repo_root,
                prefix=prefix + extension,
                visited=visited,
                show_line_numbers=show_line_numbers,
                show_leveloffset=show_leveloffset,
                max_depth=max_depth,
                current_depth=current_depth + 1,
                no_color=no_color,
                validator=validator,
                check_redundancy=check_redundancy,
                parent_modules=child_parent_modules,
                validate_offsets=validate_offsets,
                include_cache=include_cache,
                job_annotations=job_annotations,
                comparison_category=comparison_category,
            )

def validate_identical_jobs(map_file, repo_root, validator, include_cache):
    """Warn about identical direct target sets among jobs actually traversed.

    Keep this check within the displayed traversal/depth limit. Conditions and
    include attributes do not prove rendered equivalence; matches are warnings.
    """
    cache = {path.resolve(): includes for path, includes in include_cache.items()}
    groups = {}
    visited = set()

    def collect(path, category):
        path = path.resolve()
        if path not in cache:
            return
        kind = classify_file(path)
        if kind == 'category':
            category = path
        key = (category, path)
        if key in visited:
            return
        visited.add(key)
        if kind == 'job':
            groups.setdefault(category, set()).add(path)
        for include in cache[path]:
            if include['resolved']:
                collect(include['resolved'], category)

    collect(map_file, map_file.resolve())
    all_jobs = set().union(*groups.values())
    validator.compared_jobs = len(all_jobs)
    group_ids = {}
    targets = {}
    for job in all_jobs:
        targets[job] = set()
        for include in cache[job]:
            ref = include['path']
            if include['resolved']:
                target = str(include['resolved'].resolve())
            elif re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', ref):
                target = ref
            else:
                target = str((job.parent / ref).resolve())
            targets[job].add(target)
    for category, jobs in sorted(groups.items()):
        matches = compare_job_includes({job: targets[job] for job in jobs}, 100)
        for match in matches:
            if match['kind'] == 'IDENTICAL':
                key = (category, frozenset(match['shared']))
                group = group_ids.setdefault(key, f'G{len(group_ids) + 1}')
                validator.identical_job_groups[category, match['a']] = group
                validator.identical_job_groups[category, match['b']] = group
                validator.add_warning(
                    f"[IDENTICAL {group}] Identical direct include target set as {display_path(match['b'], repo_root)} "
                    f"in {display_path(category, repo_root)} ({len(match['shared'])} targets). "
                    "Check conditional includes and include attributes before removing either job.",
                    match['a'])


def resolve_map_selection(target: str, categories: list[str], repo_root: Path) -> list[Path]:
    """Resolve distro/category shorthand or an existing explicit map path."""
    maps = repo_root / 'maps'
    distros = sorted(path.name for path in maps.iterdir()
                     if path.is_dir() and (path / 'navigation.adoc').is_file()) if maps.is_dir() else []
    if target in distros:
        distro_dir = maps / target
        if not categories:
            return [distro_dir / 'navigation.adoc']
        selected = []
        available = ', '.join(path.stem for path in sorted(distro_dir.glob('*.adoc'))
                              if path.name != 'navigation.adoc')
        for category in dict.fromkeys(categories):
            if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]*(?:\.adoc)?', category):
                raise ValueError(f"Invalid category '{category}'; use a category name, such as observe")
            filename = category if category.endswith('.adoc') else category + '.adoc'
            path = distro_dir / filename
            if not path.is_file():
                raise ValueError(f"Category '{category}' not found in '{target}'. Available categories: {available}")
            if path not in selected:
                selected.append(path)
        return selected

    path = Path(target)
    if not path.is_absolute():
        path = repo_root / path
    if path.is_file():
        if categories:
            raise ValueError('Category selection requires a distro name; an explicit map path selects one file')
        return [path]
    if len(Path(target).parts) == 1 and not Path(target).suffix:
        raise ValueError(f"Unknown distro '{target}'. Available distros: {', '.join(distros) or '(none)'}")
    raise FileNotFoundError(f'File not found: {target}')


def main():
    parser = argparse.ArgumentParser(
        description='Visualize navigation map include hierarchy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Compare jobs across all OCP categories
  %(prog)s --compare-jobs ocp

  # Review specific categories in a distro
  %(prog)s --compare-jobs ocp observe optimize
  %(prog)s --compare-jobs -c observe rosa-hcp

  # Show tree for OCP install category
  %(prog)s maps/ocp/install.adoc

  # Show full navigation tree
  %(prog)s maps/ocp/navigation.adoc

  # Show with line numbers and leveloffset
  %(prog)s -l -o maps/ocp/install.adoc

  # Limit depth to 3 levels
  %(prog)s -d 3 maps/ocp/install.adoc

  # No colors (for piping to file)
  %(prog)s --no-color maps/ocp/install.adoc > tree.txt

  # Validate leveloffset patterns
  %(prog)s --validate -o maps/ocp/install.adoc
        '''
    )

    parser.add_argument(
        'target', metavar='DISTRO_OR_MAP',
        help='Distro name (e.g., ocp, rosa-hcp) or an explicit map file path'
    )
    parser.add_argument(
        'categories', nargs='*', metavar='CATEGORY',
        help='Category names within the distro (default: its full navigation)'
    )
    parser.add_argument(
        '-c', '--category', action='append', default=[], metavar='CATEGORY',
        help='Select a category within the distro (repeatable; also accepted positionally)'
    )
    parser.add_argument(
        '-l', '--line-numbers',
        action='store_true',
        help='Show line numbers where includes occur'
    )
    parser.add_argument(
        '-o', '--leveloffset',
        action='store_true',
        help='Show leveloffset values'
    )
    parser.add_argument(
        '-d', '--max-depth',
        type=int,
        metavar='N',
        help='Maximum depth to traverse (default: unlimited for jobs, stop at modules)'
    )
    parser.add_argument(
        '--no-color',
        action='store_true',
        help='Disable colored output'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Check include structure, heading levels, parent-child reuse, and identical job include target sets'
    )
    parser.add_argument(
        '--check-redundancy',
        action='store_true',
        help='Check for parent-child module redundancy (modules included in both parent and child jobs, shown with 🔁)'
    )
    parser.add_argument(
        '--compare-jobs', action='store_true',
        help='Annotate jobs with shared and unique include coverage within each category'
    )
    parser.add_argument(
        '--similarity', type=int, default=None, metavar='PERCENT',
        help='Similarity cutoff for job annotations (1-100; default: 80)'
    )
    parser.add_argument(
        '--removal-impact', action='append', default=[], metavar='JOB',
        help='Simulate removing a reachable job (repeat to assess removals together); implies --compare-jobs'
    )

    args = parser.parse_intermixed_args()
    if args.max_depth is not None and args.max_depth < 0:
        parser.error('--max-depth must be zero or greater')
    if args.similarity is not None:
        if not 1 <= args.similarity <= 100:
            parser.error('--similarity must be from 1 to 100')
        if not (args.compare_jobs or args.removal_impact):
            parser.error('--similarity requires --compare-jobs or --removal-impact')

    # Find repo root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    try:
        map_files = resolve_map_selection(args.target, args.categories + args.category, repo_root)
    except FileNotFoundError as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        parser.error(str(error))

    comparisons = {}
    removed = set()
    if args.compare_jobs or args.removal_impact:
        comparisons = {path: MapComparison(path, repo_root, classify_file, args.similarity or 80)
                       for path in map_files}
        reachable = set().union(*(comparison.before.jobs for comparison in comparisons.values()))
        try:
            removed = comparisons[map_files[0]].select_jobs(args.removal_impact, reachable)
        except ValueError as error:
            parser.error(str(error))

    failed = False
    for map_file in map_files:
        if len(map_files) > 1:
            print(f'\nMap: {display_path(map_file, repo_root)}')
        comparison = comparisons.get(map_file)
        selected_here = removed & comparison.before.jobs if comparison else set()
        failed = show_map(map_file, repo_root, args, comparison, selected_here) or failed
        if removed and not selected_here:
            print('  No selected removal jobs occur in this map.')
    if failed:
        sys.exit(1)


def show_map(map_file, repo_root, args, comparison=None, removed=frozenset()):
    """Display one selected map and return whether its checks failed."""
    # Classify root file
    file_type = classify_file(map_file)
    color = "" if args.no_color else get_color(file_type)
    reset = "" if args.no_color else Colors.RESET
    type_marker = get_type_marker(file_type)

    # Create validator if validation or redundancy checking enabled
    validator = ValidationTracker() if (args.validate or args.check_redundancy) else None

    # Enable redundancy checking if --validate OR --check-redundancy
    check_redundancy = args.validate or args.check_redundancy

    # Print root
    print(f"{color}{type_marker} {map_file.name}{reset}")

    # Build tree
    include_cache = {}
    if args.validate:
        prepare_include_tree(map_file, include_cache, args.max_depth)
        validate_identical_jobs(map_file, repo_root, validator, include_cache)
    build_tree(
        map_file,
        repo_root,
        prefix="",
        show_line_numbers=args.line_numbers,
        show_leveloffset=args.leveloffset,
        max_depth=args.max_depth,
        no_color=args.no_color,
        validator=validator,
        check_redundancy=check_redundancy,
        validate_offsets=args.validate,
        job_annotations=comparison.annotations() if comparison else None,
        include_cache=include_cache,
    )

    if args.validate:
        print(f'\nValidation scope: traversed includes and heading checks; '
              f'{validator.compared_jobs} jobs compared for identical direct include target sets.')
        if validator.identical_job_groups:
            print('Jobs with the same [IDENTICAL G#] marker share a direct include target set; see the warnings below.')
        print('Conditions, include selections, and rendered content are not evaluated for job equality.')

    comparison_errors = False
    if comparison:
        print('\nJOB COMPARISON')
        print('  Resolved include coverage, including nested jobs, modules, and snippets.')
        print('  Targets with different selection attributes are compared separately.')
        print('  Unique counts compare each job with the other jobs in its category.')
        print('  Zero unique targets does not mean all matching jobs can be removed together.')
        print('  Local job text, contexts, ordering, and level offsets need separate review.')
        print('  Analysis traverses the full selected map, regardless of --max-depth.')
        if comparison.before.issues:
            print(f'  {len(comparison.before.issues)} analysis notes affect include coverage; '
                  'affected jobs are marked incomplete.')
            print('  Use --removal-impact JOB for notes relevant to a removal.')
        if comparison.before.text_reviews:
            print('  Conditional text review locations:')
            for note in sorted(comparison.before.text_reviews):
                print(f'    {note}')
        for issue in sorted(comparison.before.errors):
            print(f'  ERROR: {issue}')
        comparison_errors = bool(comparison.before.errors)
        if removed:
            comparison_errors = comparison.print_impact(removed)

    # Print validation summary if enabled
    if validator and validator.has_issues():
        print()
        print("=" * 70)
        if args.check_redundancy and not args.validate:
            print(f"{'Redundancy Check Summary':^70}")
        else:
            print(f"{'Validation Summary':^70}")
        print("=" * 70)
        print()

        if validator.errors:
            error_color = "" if args.no_color else Colors.ERROR
            print(f"{error_color}ERRORS (must fix):{reset}")
            for err in validator.errors:
                location = display_path(err.file_path, repo_root)
                if err.line:
                    location += f":line {err.line}"
                print(f"  ❌ {location}")
                print(f"     {err.message}")
            print()

        if validator.warnings:
            warn_color = "" if args.no_color else Colors.WARNING
            print(f"{warn_color}WARNINGS (review recommended):{reset}")
            for warn in validator.warnings:
                location = display_path(warn.file_path, repo_root)
                if warn.line:
                    location += f":line {warn.line}"
                print(f"  ⚠️  {location}")
                print(f"     {warn.message}")
            print()

        if validator.redundancies:
            redundancy_color = "" if args.no_color else Colors.WARNING
            print(f"{redundancy_color}PARENT-CHILD REDUNDANCY (review for duplication):{reset}")
            for red in validator.redundancies:
                child_location = f"{display_path(red['child_file'], repo_root)}:line {red['child_line']}"
                parent_location = f"{display_path(red['parent_file'], repo_root)}:line {red['parent_line']}"
                print(f"  🔁 {red['module'].name}")
                print(f"     In child:  {child_location}")
                print(f"     In parent: {parent_location}")
            print()

        print("=" * 70)
        redundancy_count = len(validator.redundancies) if validator.redundancies else 0

        # Build summary line
        summary_parts = []
        if validator.errors:
            summary_parts.append(f"{len(validator.errors)} error(s)")
        if validator.warnings:
            summary_parts.append(f"{len(validator.warnings)} warning(s)")
        if redundancy_count > 0:
            summary_parts.append(f"{redundancy_count} redundanc{'y' if redundancy_count == 1 else 'ies'}")

        print(f"Total: {', '.join(summary_parts)}")
        print("=" * 70)

        # Exit with error code if errors found
        if validator.has_errors():
            return True
    elif validator:
        # Validation enabled but no issues
        success_color = "" if args.no_color else Colors.MODULE
        print()
        if args.check_redundancy and not args.validate:
            print(f"{success_color}✓ No parent-child redundancy found{reset}")
        else:
            print(f"{success_color}✓ No issues found in the checks performed within the traversed tree.{reset}")

    return comparison_errors

if __name__ == '__main__':
    main()
