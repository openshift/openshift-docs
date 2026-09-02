#!/usr/bin/env python3
"""
Generate JTBD job map files and category maps for OpenShift Enterprise.

Strategy:
  Phase 1: Restore ALL 846 existing job files from git in MAP format.
  Phase 2: Parse CSVs. For each entry, match to an existing filename
           within the same category using fuzzy matching.
  Phase 3: Create new stub job files for unmatched CSV entries.
  Phase 4: Write category maps from CSV data.

Categories NOT in the CSVs (install, upgrade, migrate, what-s-new)
keep their existing category maps unchanged.
"""

import csv
import subprocess
import os
import re
import sys
from pathlib import Path
from collections import defaultdict, OrderedDict
import glob

REPO = "/home/avbhatt/ocp-repos/openshift-docs"
CSV_DIR = "/home/avbhatt/ocp-repos/csv-jtbd-skill"
JOBS_DIR = os.path.join(REPO, "maps", "jobs-openshift-enterprise")
CATS_DIR = os.path.join(REPO, "maps", "openshift-enterprise")
PRE_DELETE_COMMIT = "b8ddfd9258^"

CATEGORY_FILE_MAP = {
    "Administer": "administer",
    "Configure": "configure",
    "Deploy": "deploy",
    "Develop": "develop",
    "Disconnected": "disconnected-environments",
    "Discover": "discover",
    "Extend": "extend",
    "Get Started": "get-started",
    "Integrate": "integrate",
    "Networking": "network",
    "Observe": "observe",
    "Optimize": "optimize",
    "Plan": "plan",
    "Secure": "secure",
    "Storage": "storage",
    "Troubleshoot": "troubleshoot",
    "Validate": "reference",
}

CATEGORY_TITLES = {
    "administer": "Administer",
    "configure": "Configure",
    "deploy": "Deploy",
    "develop": "Develop",
    "disconnected-environments": "Disconnected environments",
    "discover": "Discover",
    "extend": "Extend",
    "get-started": "Get Started",
    "install": "Install",
    "integrate": "Integrate",
    "migrate": "Migrate",
    "network": "Network",
    "observe": "Observe",
    "optimize": "Optimize",
    "plan": "Plan",
    "reference": "Reference",
    "secure": "Secure",
    "storage": "Storage",
    "troubleshoot": "Troubleshoot",
    "upgrade": "Upgrade",
    "what-s-new": "What's new",
}

ABBREVIATIONS = {
    "lso": "local storage operator",
    "lvm": "logical volume manager",
    "mco": "machine config operator",
    "rbac": "role based access control",
    "scc": "security context constraint",
    "csi": "container storage interface",
    "cni": "container network interface",
    "rhacm": "red hat advanced cluster management",
    "talm": "topology aware lifecycle manager",
    "sdn": "software defined networking",
    "ovn": "open virtual network",
    "gpu": "graphics processing unit",
    "ebs": "elastic block store",
    "efs": "elastic file system",
    "gcp": "google cloud platform",
    "aws": "amazon web services",
    "nfs": "network file system",
    "cifs": "common internet file system",
    "smb": "server message block",
    "pvc": "persistent volume claim",
    "hcp": "hosted control planes",
    "ipi": "installer provisioned infrastructure",
    "upi": "user provisioned infrastructure",
    "sno": "single node openshift",
    "numa": "non uniform memory access",
    "pid": "process id",
    "dns": "domain name system",
    "tls": "transport layer security",
    "iscsi": "internet small computer systems interface",
    "nfv": "network function virtualization",
    "ztp": "zero touch provisioning",
    "rhcos": "red hat coreos",
    "rhel": "red hat enterprise linux",
    "pxe": "preboot execution environment",
    "api": "application programming interface",
    "oauth": "oauth",
    "oidc": "openid connect",
    "etcd": "etcd",
    "keda": "kubernetes event driven autoscaler",
}


def run_git(args, cwd=REPO):
    result = subprocess.run(
        ["git"] + args, capture_output=True, text=True, cwd=cwd
    )
    return result.stdout.strip() if result.returncode == 0 else None


def to_kebab(name):
    s = name.strip()
    s = re.sub(r"^\s*[-–—•·]\s*", "", s)
    s = re.sub(r"^\d+[\.\)]\s*\d*[\.\)]?\s*", "", s)
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = s.lower().strip("-")
    s = re.sub(r"-+", "-", s)
    return s


def extract_job_name_from_jtbd(text):
    """Extract a short action phrase from a JTBD sentence."""
    text = text.strip()
    # "When ... I want to ACTION, so ..."
    m = re.search(r"I want to (.+?)(?:,\s*so\b|,\s*in order\b|,\s*and\b|$)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(".")
    m = re.search(r"I need to (.+?)(?:,\s*so\b|,\s*in order\b|,\s*and\b|$)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(".")
    m = re.search(r"I can (.+?)(?:,\s*so\b|,\s*in order\b|$)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(".")
    return text


def tokenize(s):
    """Tokenize a string into content words, expanding abbreviations."""
    words = set(re.split(r"[-_\s]+", s.lower()))
    words.discard("")
    expanded = set()
    for w in words:
        expanded.add(w)
        if w in ABBREVIATIONS:
            expanded.update(ABBREVIATIONS[w].split())
    # Remove stop words for matching
    stop = {"the", "a", "an", "to", "for", "of", "in", "on", "my", "i",
            "and", "or", "is", "are", "can", "so", "that", "with", "by",
            "as", "at", "from", "be", "it", "its", "this", "when", "how",
            "what", "which", "your", "want", "need", "use", "using"}
    return expanded - stop


def match_score(tokens_a, tokens_b):
    """Weighted Jaccard with bonus for matching key nouns."""
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    jaccard = len(intersection) / len(union) if union else 0.0

    # Bonus: if all words in the shorter set are in the longer set
    shorter = tokens_a if len(tokens_a) <= len(tokens_b) else tokens_b
    longer = tokens_b if len(tokens_a) <= len(tokens_b) else tokens_a
    if shorter and shorter.issubset(longer):
        jaccard = max(jaccard, 0.65)

    return jaccard


def get_all_existing_jobs():
    """Get all job file content from the pre-delete commit."""
    listing = run_git(
        ["ls-tree", "--name-only", PRE_DELETE_COMMIT, "maps/jobs-openshift-enterprise/"]
    )
    if not listing:
        return {}
    jobs = {}
    for line in listing.strip().split("\n"):
        basename = os.path.basename(line.strip())
        if basename.endswith(".adoc"):
            slug = basename.replace(".adoc", "")
            content = run_git(["show", f"{PRE_DELETE_COMMIT}:{line.strip()}"])
            if content:
                jobs[slug] = content
    return jobs


def get_existing_category_refs():
    """Get job slug lists currently in each category map."""
    refs = {}
    for f in sorted(os.listdir(CATS_DIR)):
        if f.endswith(".adoc") and f != "navigation.adoc":
            cat = f.replace(".adoc", "")
            refs[cat] = []
            with open(os.path.join(CATS_DIR, f)) as fh:
                for line in fh:
                    m = re.search(
                        r"include::jobs-openshift-enterprise/(.+?)\.adoc\[", line
                    )
                    if m:
                        refs[cat].append(m.group(1))
    return refs


def convert_to_map_format(slug, old_content):
    """Convert an ASSEMBLY-format job file to MAP format."""
    lines_out = [":_mod-docs-content-type: MAP", f":context: {slug}", ""]

    includes = []
    comments = []
    for line in old_content.strip().split("\n"):
        stripped = line.strip()
        if stripped.startswith("include::"):
            includes.append(stripped)
        elif stripped.startswith("//") and includes == []:
            comments.append(stripped)

    for c in comments:
        lines_out.append(c)
    if comments:
        lines_out.append("")

    for i, inc in enumerate(includes):
        if i == 0:
            inc = re.sub(r"leveloffset=\+\d+", "leveloffset=+0", inc)
            if "chunk=" not in inc:
                inc = inc.replace("]", ',chunk="to-content"]')
        else:
            if "toc=" not in inc:
                inc = inc.replace("]", ',toc="no"]')
        lines_out.append(inc)
        lines_out.append("")

    return "\n".join(lines_out)


def create_stub_job(slug, job_name=""):
    """Create a stub MAP job file."""
    return f""":_mod-docs-content-type: MAP
:context: {slug}

// TODO: Add module includes for this job
// Job name: {job_name or slug}
"""


def parse_csv_entry(row):
    """Parse a CSV row into structured job info. Returns None for junk rows."""
    jn = row.get("job_name", "").strip()
    js = row.get("job_statement", "").strip()
    raw = jn if jn else js

    # Skip empty or numeric-only entries (section numbers like "5.1")
    cleaned = re.sub(r"[\d\.\s\-–—•·]", "", raw)
    if not cleaned or len(cleaned) < 3:
        return None

    # Handle Parent > Child hierarchy
    if ">" in raw:
        parts = [p.strip() for p in raw.split(">")]
        parent_name = parts[0]
        child_name = parts[-1]
        # Skip if parent or child is just a number
        if not re.sub(r"[\d\.\s]", "", parent_name):
            return None
        return {
            "parent_name": parent_name,
            "child_name": child_name,
            "is_child": True,
            "raw": raw,
        }

    # Handle JTBD sentences
    is_jtbd = raw.startswith("When ") or raw.startswith("Because ") or raw.startswith("As a ")
    if is_jtbd:
        extracted = extract_job_name_from_jtbd(raw)
        return {
            "parent_name": None,
            "child_name": None,
            "job_name": extracted,
            "is_child": False,
            "raw": raw,
        }

    # Plain name (possibly from job_name column)
    return {
        "parent_name": None,
        "child_name": None,
        "job_name": jn if jn else js,
        "is_child": False,
        "raw": raw,
    }


def build_parent_jobs(entries):
    """Group CSV entries into parent-level jobs preserving order."""
    parents = OrderedDict()
    for entry in entries:
        if entry["is_child"]:
            parent_key = entry["parent_name"]
            if parent_key not in parents:
                parents[parent_key] = {
                    "name": parent_key,
                    "children": [],
                    "raw": entry["raw"],
                }
            parents[parent_key]["children"].append(entry["child_name"])
        else:
            name = entry.get("job_name", entry["raw"])
            if name not in parents:
                parents[name] = {
                    "name": name,
                    "children": [],
                    "raw": entry["raw"],
                }
    return parents


def find_best_match_in_category(job_name, candidate_tokens, existing_slugs, tokens_cache):
    """Find the best matching existing slug within a category."""
    # First try exact kebab match
    candidate_kebab = to_kebab(job_name)
    if candidate_kebab in existing_slugs:
        return candidate_kebab, 1.0

    # Then try substring containment
    for slug in existing_slugs:
        if candidate_kebab and (candidate_kebab in slug or slug in candidate_kebab):
            return slug, 0.8

    # Fuzzy token match
    if not candidate_tokens:
        return None, 0.0

    best_slug = None
    best_score = 0.0
    for slug in existing_slugs:
        if slug not in tokens_cache:
            tokens_cache[slug] = tokenize(slug)
        score = match_score(candidate_tokens, tokens_cache[slug])
        if score > best_score:
            best_score = score
            best_slug = slug

    if best_score >= 0.40:
        return best_slug, best_score

    return None, 0.0


def main():
    print("=" * 70)
    print("JTBD Job Map Generator for OpenShift Enterprise")
    print("=" * 70)

    # ── Phase 1: Restore ALL existing job files ──
    print("\n[Phase 1] Restoring existing job files from git in MAP format...")
    existing_jobs = get_all_existing_jobs()
    print(f"  Found {len(existing_jobs)} job files in git history")

    os.makedirs(JOBS_DIR, exist_ok=True)
    restored = 0
    for slug, content in existing_jobs.items():
        filepath = os.path.join(JOBS_DIR, f"{slug}.adoc")
        map_content = convert_to_map_format(slug, content)
        with open(filepath, "w") as f:
            f.write(map_content)
        restored += 1
    print(f"  Restored {restored} job files in MAP format")

    # ── Phase 2: Parse CSVs & match to existing filenames ──
    print("\n[Phase 2] Parsing CSVs and matching to existing filenames...")

    existing_cat_refs = get_existing_category_refs()
    csv_categories = set(CATEGORY_FILE_MAP.values())

    # ONLY match against slugs that have actual file content (from git history)
    real_file_slugs = set(existing_jobs.keys())

    tokens_cache = {}
    category_results = OrderedDict()
    all_new_stubs = {}

    total_csv_parents = 0
    total_matched = 0
    total_new = 0

    # Global used set to avoid giving two CSV entries the same slug
    global_used = set()

    for csv_file in sorted(glob.glob(os.path.join(CSV_DIR, "*.csv"))):
        csv_cat = re.search(r"- (.+)\.csv$", csv_file).group(1)
        cat_file = CATEGORY_FILE_MAP.get(csv_cat)
        if not cat_file:
            continue

        # Parse CSV
        entries = []
        with open(csv_file) as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                parsed = parse_csv_entry(row)
                if parsed is not None:
                    entries.append(parsed)

        # Build parent job hierarchy
        parents = build_parent_jobs(entries)
        total_csv_parents += len(parents)

        # For category-scoped matching, prefer files that were ALSO
        # referenced in this category's existing map
        existing_in_cat = set(existing_cat_refs.get(cat_file, [])) & real_file_slugs

        cat_includes = []

        for job_name, job_info in parents.items():
            job_tokens = tokenize(job_name)

            # Try matching within this category's existing refs first
            match_slug, score = find_best_match_in_category(
                job_name, job_tokens,
                existing_in_cat - global_used, tokens_cache,
            )

            if not match_slug or score < 0.40:
                # Fall back to ALL real file slugs
                match_slug, score = find_best_match_in_category(
                    job_name, job_tokens,
                    real_file_slugs - global_used, tokens_cache,
                )

            if match_slug and score >= 0.40:
                final_slug = match_slug
                global_used.add(match_slug)
                total_matched += 1
            else:
                # Create new slug from job name
                final_slug = to_kebab(job_name)
                if len(final_slug) > 80:
                    words = final_slug.split("-")
                    final_slug = "-".join(words[:10])
                base = final_slug
                counter = 1
                while final_slug in real_file_slugs or final_slug in all_new_stubs:
                    final_slug = f"{base}-{counter}"
                    counter += 1

                all_new_stubs[final_slug] = job_info["name"]
                total_new += 1

            cat_includes.append(final_slug)

        category_results[cat_file] = cat_includes
        print(f"  {csv_cat} → {cat_file}.adoc: {len(parents)} parent jobs → "
              f"{len(parents) - len([s for s in cat_includes if s in all_new_stubs])} matched, "
              f"{len([s for s in cat_includes if s in all_new_stubs])} new")

    print(f"\n  Total parent jobs from CSVs: {total_csv_parents}")
    print(f"  Matched to existing files: {total_matched}")
    print(f"  New stubs needed: {total_new}")

    # ── Phase 3: Create stub files for new jobs ──
    print(f"\n[Phase 3] Creating {len(all_new_stubs)} new stub job files...")
    for slug, name in sorted(all_new_stubs.items()):
        filepath = os.path.join(JOBS_DIR, f"{slug}.adoc")
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(create_stub_job(slug, name))
    print(f"  Created {len(all_new_stubs)} stub files")

    # ── Phase 4: Write category maps ──
    print(f"\n[Phase 4] Writing category maps...")
    for cat_file, includes in category_results.items():
        filepath = os.path.join(CATS_DIR, f"{cat_file}.adoc")
        title = CATEGORY_TITLES.get(cat_file, cat_file.replace("-", " ").title())

        lines = [":_mod-docs-content-type: MAP", "", f"= {title}", ""]
        for slug in includes:
            lines.append(
                f"include::jobs-openshift-enterprise/{slug}.adoc[leveloffset=+1]"
            )
            lines.append("")
        with open(filepath, "w") as f:
            f.write("\n".join(lines))
        print(f"  {cat_file}.adoc: {len(includes)} jobs")

    # Categories not in CSVs: preserve existing maps
    for cat_file in existing_cat_refs:
        if cat_file not in category_results:
            print(f"  {cat_file}.adoc: preserved (not in CSVs, {len(existing_cat_refs[cat_file])} jobs)")

    # ── Summary ──
    total_jobs = len(os.listdir(JOBS_DIR))
    adoc_count = len([f for f in os.listdir(JOBS_DIR) if f.endswith(".adoc")])
    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    print(f"Job .adoc files in {JOBS_DIR}: {adoc_count}")
    print(f"  Restored from git (MAP format): {restored}")
    print(f"  New stubs: {len(all_new_stubs)}")
    print(f"Category maps written: {len(category_results)}")
    print(f"Category maps preserved: {len(existing_cat_refs) - len(category_results)}")

    # Report stubs
    if all_new_stubs:
        print(f"\nNew stub files (need module includes):")
        for i, (slug, name) in enumerate(sorted(all_new_stubs.items())):
            if i < 40:
                print(f"  {slug}.adoc  ←  \"{name}\"")
            elif i == 40:
                print(f"  ... and {len(all_new_stubs) - 40} more")
                break

    # Report matching quality
    print(f"\nMatching quality check (sample fuzzy matches):")
    # Re-run a sample to show matches
    sample_count = 0
    for csv_file in sorted(glob.glob(os.path.join(CSV_DIR, "*.csv"))):
        csv_cat = re.search(r"- (.+)\.csv$", csv_file).group(1)
        cat_file = CATEGORY_FILE_MAP.get(csv_cat)
        if not cat_file or cat_file not in ("storage", "configure", "administer"):
            continue
        with open(csv_file) as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                entry = parse_csv_entry(row)
                if entry["is_child"]:
                    continue
                name = entry.get("job_name", entry["raw"])
                tokens = tokenize(name)
                existing_in_cat = set(existing_cat_refs.get(cat_file, []))
                match_slug, score = find_best_match_in_category(
                    name, tokens, existing_in_cat, tokens_cache
                )
                if match_slug and 0.40 <= score < 0.95:
                    kebab = to_kebab(name)
                    print(f"  [{csv_cat}] \"{name[:60]}\" → {match_slug} (score={score:.2f})")
                    sample_count += 1
                    if sample_count >= 15:
                        break
        if sample_count >= 15:
            break


if __name__ == "__main__":
    main()
