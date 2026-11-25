"""Static include comparisons and removal impact analysis for navigation maps."""

import os
import re
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path


def compare_job_includes(jobs: dict, similarity: int) -> list[dict]:
    """Compare nonempty sets, with the smaller job first for containment."""
    matches = []
    for a, b in combinations(sorted(jobs), 2):
        left, right = jobs[a], jobs[b]
        if not left or not right:
            continue
        shared = left & right
        union = left | right
        if left == right:
            kind = "IDENTICAL"
        elif left < right or right < left:
            kind = "CONTAINED"
            if right < left:
                a, b, left, right = b, a, right, left
        elif len(shared) * 100 >= similarity * len(union):
            kind = "SIMILAR"
        else:
            continue
        matches.append(dict(kind=kind, a=a, b=b, shared=shared,
                            only_a=left - right, only_b=right - left,
                            similarity=len(shared) * 100 / len(union)))
    return matches


@dataclass
class Source:
    includes: list = field(default_factory=list)
    body: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    contexts: set = field(default_factory=set)
    anchors: set = field(default_factory=set)
    issues: set = field(default_factory=set)
    errors: set = field(default_factory=set)
    text_reviews: set = field(default_factory=set)


@dataclass
class Snapshot:
    targets: set = field(default_factory=set)
    jobs: set = field(default_factory=set)
    groups: dict = field(default_factory=dict)
    edges: set = field(default_factory=set)
    issues: set = field(default_factory=set)
    errors: set = field(default_factory=set)
    job_selections: dict = field(default_factory=dict)
    text_reviews: set = field(default_factory=set)


class MapComparison:
    """Compare resolved include graphs without claiming rendered equivalence.

    Target identity includes content-selecting attributes. Selected fragments and
    dynamic directives make the analysis uncertain rather than proving coverage.
    """

    def __init__(self, root, repo_root, classify, similarity=80):
        self.root = root.resolve()
        self.repo_root = repo_root.resolve()
        self.classify = classify
        self.similarity = similarity
        self.sources = {}
        self.before = self.snapshot()
        self.coverage = {}
        for job in self.before.jobs:
            selectors = self.before.job_selections[job]
            coverage = self.snapshot(root=job) if "" in selectors else Snapshot()
            for selector in selectors - {""}:
                coverage.targets.add((job, selector))
                coverage.issues.add(f"{self.name(job)}: job fragment [{selector}] not expanded; "
                                    "render review required")
            self.coverage[job] = coverage

    def name(self, path):
        if isinstance(path, str):
            return path  # Remote include identity; no network fetch is performed.
        try:
            return str(path.relative_to(self.repo_root))
        except ValueError:
            return str(path)

    def source(self, path):
        if path in self.sources:
            return self.sources[path]
        source = Source()
        self.sources[path] = source
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            source.issues.add(f"{self.name(path)}: cannot read source: {error}")
            source.errors.update(source.issues)
            return source
        comment = False
        todo_comment = False
        conditional_depth = 0
        for number, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            location = f"{self.name(path)}:{number}"
            if stripped == "////":
                comment = not comment
                continue
            if comment or stripped.startswith("//"):
                if "TODO" in line:
                    todo_comment = True
                if todo_comment:
                    source.notes.append((number, stripped))
                continue
            todo_comment = False
            if not stripped:
                continue
            include = re.match(r"^include::([^\[]+)\[(.*)\]\s*$", stripped)
            if include:
                target, attributes = include.groups()
                # Split on commas outside quotes; only leveloffset is cosmetic
                # for this content comparison. Preserve all other attributes.
                parts = re.findall(r'''(?:[^,"']|"[^"]*"|'[^']*')+''', attributes)
                selectors = []
                for part in parts:
                    key, separator, value = part.strip().partition("=")
                    if key.strip() == "leveloffset":
                        if not re.fullmatch(r'''["']?[+-]?\d+["']?''', value.strip()):
                            source.issues.add(f"{location}: dynamic leveloffset needs review")
                    elif part.strip():
                        selectors.append(key.strip() + separator + value.strip().strip("\"'"))
                source.includes.append((target.strip(), ",".join(sorted(selectors)), number))
                if conditional_depth:
                    source.issues.add(f"{location}: conditional include needs review")
                continue
            if re.match(r"^(?:ifdef|ifndef|ifeval|endif|else)::", stripped):
                if stripped.startswith('endif::'):
                    conditional_depth = max(0, conditional_depth - 1)
                elif not stripped.startswith('else::'):
                    source.text_reviews.add(f"{location}: distro-specific or conditional text needs review")
                    if stripped.startswith('ifeval::') or re.search(r'\[\]\s*$', stripped):
                        conditional_depth += 1
                    elif 'include::' in stripped:
                        source.issues.add(f"{location}: inline conditional include needs review")
                continue
            context = re.match(r"^:context:\s*(.*)", stripped)
            if context:
                source.contexts.add(context.group(1))
                continue
            if stripped.startswith(":_mod-docs-content-type:"):
                continue
            if stripped.startswith(":"):
                source.issues.add(f"{location}: local attributes need review")
            for anchor in re.findall(r'''\[id=["']([^"']+)["']\]|\[\[([^\],]+)''', stripped):
                source.anchors.update(value for value in anchor if value)
            source.body.append((number, stripped))
        if comment:
            source.issues.add(f"{self.name(path)}: unclosed comment block")
        # Conditions and attributes inside a leaf module do not change which
        # file is included. Review them only when they can affect the graph.
        if not source.includes and self.classify(path) not in ("job", "category"):
            source.issues = set(source.errors)
        return source

    def snapshot(self, removed=frozenset(), root=None):
        result = Snapshot()

        def walk(path, stack, category):
            if path in removed:
                return
            if path in stack:
                result.issues.add(f"{self.name(path)}: circular include")
                result.errors.add(f"{self.name(path)}: circular include")
                return
            kind = self.classify(path)
            if kind == "category":
                category = path
            if kind == "job":
                result.jobs.add(path)
                result.groups.setdefault(category, set()).add(path)
                result.job_selections.setdefault(path, set()).add("")
            source = self.source(path)
            result.issues.update(source.issues)
            result.errors.update(source.errors)
            result.text_reviews.update(source.text_reviews)
            for ref, selectors, line in source.includes:
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', ref):
                    result.edges.add((path, line, ref))
                    result.targets.add((ref, selectors))
                    result.issues.add(f"{self.name(path)}:{line}: remote include {ref} "
                                      "not fetched; external content needs review")
                    continue
                target = (path.parent / ref).resolve()
                result.edges.add((path, line, target))
                if target in removed:
                    continue
                if "{" in ref or not target.is_file():
                    issue = f"{self.name(path)}:{line}: unresolved include {ref}"
                    result.issues.add(issue)
                    if "{" not in ref:
                        result.errors.add(issue)
                    continue
                child_kind = self.classify(target)
                if child_kind not in ("job", "category"):
                    result.targets.add((target, selectors))
                if selectors:
                    if child_kind == "job":
                        result.jobs.add(target)
                        result.groups.setdefault(category, set()).add(target)
                        result.job_selections.setdefault(target, set()).add(selectors)
                        result.targets.add((target, selectors))
                    result.issues.add(f"{self.name(path)}:{line}: include attributes [{selectors}] "
                                      "need render review; fragment not expanded")
                    continue
                walk(target, stack | {path}, category)

        start = root or self.root
        walk(start, set(), start)
        return result

    def annotations(self):
        annotations = {}
        for category, jobs in self.before.groups.items():
            matches = compare_job_includes(
                {str(job): self.coverage[job].targets for job in jobs
                 if not self.coverage[job].issues}, self.similarity)
            for job in sorted(jobs):
                own = self.coverage[job]
                others = sorted(jobs - {job})
                others_targets = set().union(*(self.coverage[other].targets for other in others))
                unique = len(own.targets - others_targets)
                conditional_parent = self.source(category).issues | self.source(self.root).issues
                if own.issues or any('conditional include' in issue for issue in conditional_parent):
                    annotations[category, job] = "[include comparison incomplete; review required]"
                    continue
                covering = [other for other in others if own.targets and
                            own.targets <= self.coverage[other].targets and
                            not self.coverage[other].issues]
                if covering:
                    keeper = min(covering, key=lambda other: (-len(self.coverage[other].targets), str(other)))
                    annotations[category, job] = f"[0 unique include targets; all also in {self.name(keeper)}]"
                else:
                    label = f"[{unique} unique include targets in category]"
                    similar = [match for match in matches if match["kind"] == "SIMILAR"
                               and str(job) in (match["a"], match["b"])]
                    if similar:
                        best = max(similar, key=lambda match: match["similarity"])
                        other = best["b"] if best["a"] == str(job) else best["a"]
                        label += f" [SIMILAR {best['similarity']:.1f}% to {self.name(Path(other))}]"
                    annotations[category, job] = label
        for (category, job), label in annotations.items():
            text_reviews = (self.coverage[job].text_reviews | self.source(category).text_reviews
                            | self.source(self.root).text_reviews)
            if text_reviews:
                annotations[category, job] = label + ' [distro-specific or conditional text needs review]'
        return annotations

    def select_jobs(self, names, reachable=None):
        """Resolve job names across one map or a supplied selection of maps."""
        reachable = self.before.jobs if reachable is None else reachable
        selected = set()
        for name in names:
            path = Path(name)
            candidates = {job for job in reachable if
                          (job == (self.repo_root / path).resolve() or
                           job == (self.root.parent / path).resolve() or
                           (len(path.parts) == 1 and job.name == name))}
            if len(candidates) != 1:
                raise ValueError(f"{name}: expected one reachable job, found {len(candidates)}; "
                                 "use a repository-relative path to disambiguate")
            selected.update(candidates)
        if self.root in selected:
            raise ValueError("Select a job included by the map, rather than the root itself")
        return selected

    def references(self, jobs):
        """Find literal references and include users; dynamic references need review."""
        needles = {job.name for job in jobs} | {job.stem for job in jobs}
        for job in jobs:
            needles.update(self.source(job).contexts)
            needles.update(anchor for anchor in self.source(job).anchors if "{" not in anchor)
        needles.discard("")
        references, errors = [], []
        def scan_error(error):
            errors.append(f"Reference scan failed: {error}")

        for directory, dirs, files in os.walk(self.repo_root, followlinks=False, onerror=scan_error):
            dirs[:] = sorted(d for d in dirs if d not in (".git", "node_modules", "__pycache__"))
            for name in sorted(files):
                path = Path(directory) / name
                if path.suffix != ".adoc" or path.is_symlink() or path.resolve() in jobs:
                    continue
                try:
                    lines = path.read_text(encoding="utf-8").splitlines()
                except (OSError, UnicodeError) as error:
                    errors.append(f"{self.name(path)}: reference scan failed: {error}")
                    continue
                comment = False
                for number, line in enumerate(lines, 1):
                    if line.strip() == "////":
                        comment = not comment
                        continue
                    if comment or line.lstrip().startswith("//"):
                        continue
                    include = re.match(r"^\s*include::([^\[]+)\[", line)
                    resolved_user = bool(include and
                                         (path.parent / include.group(1).strip()).resolve() in jobs)
                    if resolved_user or (any(needle in line for needle in needles)
                                         and re.search(r"xref:|<<|include::", line)):
                        references.append((path, number, line.strip()))
        return references, errors

    def print_impact(self, removed):
        after = self.snapshot(removed)
        lost = self.before.targets - after.targets
        retained = self.before.targets & after.targets
        lost_jobs = self.before.jobs - after.jobs
        print("\nREMOVAL IMPACT (simulation only)")
        print(f"  Scope: {self.name(self.root)}; remove all occurrences of the selected jobs here.")
        for job in sorted(removed):
            print(f"  Remove: {self.name(job)}")
        print("  Include locations removed:")
        removed_edges = {(path, line, target) for path, line, target in self.before.edges
                         if target in removed and path not in lost_jobs}
        for path, line, target in sorted(removed_edges):
            print(f"    {self.name(path)}:{line} -> {self.name(target)}")
        print(f"  Include targets lost: {len(lost)}")
        for target, selectors in sorted(lost, key=lambda item: (self.name(item[0]), item[1])):
            print(f"    {self.name(target)}" + (f" [{selectors}]" if selectors else ""))
        print(f"  Include targets retained: {len(retained)}")
        for job in sorted(removed):
            remaining = self.coverage[job].targets & after.targets
            print(f"  Retained content from {self.name(job)}: {len(remaining)} targets")
            keepers = [(other, self.coverage[other].targets & remaining) for other in sorted(after.jobs)]
            for other, shared in keepers:
                if shared:
                    print(f"    Keep {self.name(other)} ({len(shared)} shared targets)")
            for target, selectors in sorted(remaining, key=lambda item: (self.name(item[0]), item[1])):
                print(f"      {self.name(target)}" + (f" [{selectors}]" if selectors else ""))
                for path, line, child in sorted(after.edges):
                    if child == target and any(number == line and attrs == selectors
                                               for _, attrs, number in self.source(path).includes):
                        print(f"        Retained at {self.name(path)}:{line}")

        # Uncertainty unrelated to the selected removals is summarized in the
        # tree. The impact details focus on removed branches and their keepers.
        review = (self.before.errors | after.errors | self.source(self.root).issues
                  | self.source(self.root).text_reviews)
        for category, jobs in self.before.groups.items():
            if jobs & removed:
                review.update(self.source(category).issues | self.source(category).text_reviews)
        for job in removed:
            review.update(self.coverage[job].issues)
            review.update(self.coverage[job].text_reviews)
            for other in after.jobs:
                if self.coverage[job].targets & self.coverage[other].targets:
                    review.update(self.coverage[other].issues)
                    review.update(self.coverage[other].text_reviews)
        for job in sorted(lost_jobs):
            source = self.source(job)
            review.update(source.text_reviews)
            if source.body:
                review.add(f"{self.name(job)}: local text/anchors would leave this map")
                for line, text in source.body:
                    print(f"  Local content lost at {self.name(job)}:{line}: {text}")
            if source.contexts:
                review.add(f"{self.name(job)}: context-dependent anchors/attributes need review "
                           f"({', '.join(sorted(source.contexts))})")
            for line, note in source.notes:
                print(f"  Preserve review note {self.name(job)}:{line}: {note}")
        # An edited parent may be reused by another map even when that parent
        # remains in this map. Include its users in the reference review too.
        edited_parents = {path for path, _, _ in removed_edges if path != self.root}
        references, errors = self.references(lost_jobs | edited_parents)
        review.update(errors)
        print("  Repository references/include users to review:")
        for path, line, text in references:
            print(f"    {self.name(path)}:{line}: {text}")
        if not references:
            print("    No literal matches found; generated or dynamic references are not verified.")
        else:
            review.add("Review listed references before changing mappings or deleting job files")
        if review:
            print("  REVIEW REQUIRED:")
            for issue in sorted(review):
                print(f"    {issue}")
        print("  Counts describe included file/selection coverage, not equivalent rendered content.")
        print("  Keep the listed covering jobs; review context, links, ordering, and headings before editing.")
        return bool(self.before.errors or after.errors or errors)
