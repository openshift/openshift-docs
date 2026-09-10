#!/usr/bin/env python3
"""Generate RHCL JTBD job maps from coverage map CSV and Jobs by Category metadata."""

import csv
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
JOBS_CSV = Path("/Users/shdiaz/Desktop/DITA maps/RHCL JTBD DITA map worksheet copy - Jobs by Category.csv")
COVERAGE_CSV = Path("/Users/shdiaz/Downloads/RHCL-jtbd-coverage-map.csv")
OUT_COVERAGE = REPO / "RHCL-jtbd-coverage-map.csv"
JOBS_DIR = REPO / "maps" / "jobs"
MODULES_DIR = REPO / "modules"
RHCL_MAPS = REPO / "maps" / "rhcl"

CATEGORY_FILES = {
    "Administer": "administer.adoc",
    "Configure": "configure.adoc",
    "Develop": "develop.adoc",
    "Discover": "discover.adoc",
    "Install": "install.adoc",
    "Observe": "observe.adoc",
    "Plan": "plan.adoc",
    "Reference": "reference.adoc",
    "Secure": "secure.adoc",
    "Troubleshoot": "troubleshoot.adoc",
    "Upgrade": "upgrade.adoc",
}

CATEGORY_PARENTS = {
    "Install",
    "Configure",
    "Develop",
    "Administer",
    "Secure",
    "Plan",
    "Observe",
    "Troubleshoot",
    "Discover",
    "Reference",
    "Upgrade",
}


def slugify(text: str, max_len: int = 72) -> str:
    s = text.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return (s or "job")[:max_len]


def load_jobs_meta():
    meta = {}
    with JOBS_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            num_s = row.get("Job #", "").strip()
            if not num_s:
                continue
            num = int(num_s)
            top = row.get("Top job", "").strip()
            sec = row.get("Secondary job", "").strip()
            statement = row.get("Job statement", "").strip()
            is_new = row.get("New", "").strip().upper() == "NEW"
            if is_new and top and sec in CATEGORY_PARENTS:
                name = top
                parent = sec
                statement = statement or ""
            elif not statement and sec.lower().startswith("when i") and top:
                # Reference jobs store the JTBD statement in Secondary job.
                name = top
                statement = sec
                parent = ""
            elif sec:
                name = sec
                parent = top
            elif top:
                name = top
                parent = ""
            else:
                name = f"Job {num}"
                parent = ""
            meta[num] = {
                "num": num,
                "category": row["Job category"].strip(),
                "name": name,
                "statement": statement,
                "parent": parent if parent and parent != name else "",
                "is_new": is_new,
            }
    return meta


def enrich_coverage(meta):
    rows = list(csv.DictReader(COVERAGE_CSV.open(encoding="utf-8")))
    fieldnames = [
        "job_category",
        "job_number",
        "job_name",
        "job_statement",
        "parent_job",
        "job_coverage",
        "module_file",
        "module_status",
        "module_note",
        "job_notes",
    ]

    def resolve_job(row):
        stmt = row.get("job_statement", "").strip()
        name = row.get("job_name", "").strip()
        parent = row.get("parent_job", "").strip()
        if stmt:
            for rec in meta.values():
                if stmt == rec["statement"]:
                    return rec
        if name:
            for rec in meta.values():
                if name == rec["statement"]:
                    return rec
            matches = [rec for rec in meta.values() if rec["name"] == name]
            if len(matches) == 1:
                return matches[0]
            if stmt:
                matches = [rec for rec in meta.values() if rec["name"] == name and rec["statement"] == stmt]
                if matches:
                    return matches[0]
            # Reference rows may store the job statement in job_name with the real
            # title in parent_job from an earlier coverage export.
            if parent:
                matches = [rec for rec in meta.values() if rec["name"] == parent]
                if len(matches) == 1:
                    return matches[0]
        return None

    out = []
    for row in rows:
        new = {k: "" for k in fieldnames}
        if row.get("job_name", "").strip() or row.get("job_statement", "").strip():
            rec = resolve_job(row)
            if rec:
                new["job_category"] = rec["category"]
                new["job_number"] = str(rec["num"])
                new["job_name"] = rec["name"]
                new["job_statement"] = rec["statement"]
                new["parent_job"] = rec["parent"]
                new["job_coverage"] = row.get("job_coverage", "")
                new["module_file"] = row.get("module_file", "")
                new["module_status"] = row.get("module_status", "")
                new["module_note"] = row.get("module_note", "")
                new["job_notes"] = row.get("job_notes", "")
            else:
                new.update({k: row.get(k, "") for k in row if k in fieldnames})
        out.append(new)

    with OUT_COVERAGE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(out)
    return out


def module_is_concept(module_file: str) -> bool:
    path = REPO / module_file.replace("modules/", "modules/")
    if not path.exists():
        return module_file.startswith("modules/con-")
    head = path.read_text(encoding="utf-8", errors="replace")[:400]
    return ":_mod-docs-content-type: CONCEPT" in head or "/con-" in module_file


def statement_to_abstract(statement: str) -> str:
    if not statement:
        return ""
    m = re.match(r"When .+?, I want (.+?), so I can (.+?)\.?$", statement, re.I)
    if m:
        return f"{m.group(1).capitalize()} so you can {m.group(2)}."
    return statement


def create_intro_module(slug: str, title: str, statement: str) -> str:
    module_name = f"con-rhcl-jtbd-{slug}.adoc"
    path = MODULES_DIR / module_name
    abstract = statement_to_abstract(statement)
    content = f"""// Job intro concept for JTBD map: {slug}

:_mod-docs-content-type: CONCEPT
[id="rhcl-jtbd-{slug}_{{context}}"]
= {title}

[role="_abstract"]
{abstract}
"""
    path.write_text(content, encoding="utf-8")
    return f"modules/{module_name}"


def build_jobs_from_coverage(coverage_rows, meta):
    by_num = defaultdict(lambda: {"modules": [], "coverage": "", "notes": ""})
    for row in coverage_rows:
        if not row.get("job_number", "").strip():
            continue
        num = int(row["job_number"])
        mod = row.get("module_file", "").strip()
        if mod:
            by_num[num]["modules"].append(
                {
                    "file": mod,
                    "status": row.get("module_status", ""),
                    "note": row.get("module_note", ""),
                }
            )
        by_num[num]["coverage"] = row.get("job_coverage", "") or by_num[num]["coverage"]
        by_num[num]["notes"] = row.get("job_notes", "") or by_num[num]["notes"]

    slug_counts = defaultdict(int)
    jobs = {}
    intro_created = []

    for num in sorted(by_num):
        if num not in meta:
            continue
        info = meta[num]
        if not info["name"] or not info["category"]:
            continue

        base_slug = slugify(info["name"])
        slug_counts[base_slug] += 1
        slug = base_slug if slug_counts[base_slug] == 1 else f"{base_slug}-{num}"

        modules = []
        seen = set()
        for mod in by_num[num]["modules"]:
            if mod["file"] in seen:
                continue
            seen.add(mod["file"])
            modules.append(mod)

        concept_modules = [m for m in modules if module_is_concept(m["file"])]
        intro = concept_modules[0]["file"] if concept_modules else None
        body_modules = [m["file"] for m in modules if m["file"] != intro]

        if not intro:
            intro = create_intro_module(slug, info["name"], info["statement"])
            intro_created.append(intro)

        jobs[num] = {
            "num": num,
            "slug": slug,
            "name": info["name"],
            "category": info["category"],
            "parent": info["parent"],
            "coverage": by_num[num]["coverage"],
            "notes": by_num[num]["notes"],
            "intro": intro,
            "modules": body_modules,
        }

    # synthetic parent jobs referenced by children
    parent_names = {info["parent"] for info in meta.values() if info["parent"]}
    parent_names -= CATEGORY_PARENTS
    child_by_parent = defaultdict(list)
    for num, job in jobs.items():
        if not isinstance(num, int):
            continue
        if job["parent"] and job["parent"] not in CATEGORY_PARENTS:
            child_by_parent[job["parent"]].append(num)

    for parent_name in sorted(parent_names):
        if parent_name not in child_by_parent:
            continue
        slug = slugify(parent_name)
        if slug in {j["slug"] for j in jobs.values()}:
            slug = f"{slug}-parent"
        intro = create_intro_module(
            slug,
            parent_name,
            f"When I need to {parent_name.lower()}, I want to complete the related configuration tasks.",
        )
        intro_created.append(intro)
        jobs[f"parent:{parent_name}"] = {
            "num": None,
            "slug": slug,
            "name": parent_name,
            "category": meta[child_by_parent[parent_name][0]]["category"],
            "parent": "",
            "coverage": "",
            "notes": "",
            "intro": intro,
            "modules": [],
            "children": [jobs[n]["slug"] for n in child_by_parent[parent_name]],
        }

    return jobs, intro_created


def write_job_map(job):
    path = JOBS_DIR / f"{job['slug']}.adoc"
    lines = [
        ":_mod-docs-content-type: MAP",
        f":context: {job['slug']}",
        "",
        f"= {job['name']}",
        "",
    ]

    if job.get("coverage") == "gap":
        lines.append("// Coverage gap: no existing modules mapped for this job.")
        lines.append("")

    intro = job["intro"].replace("modules/", "")
    lines.append(f'include::modules/{intro}[leveloffset=+0,chunk="to-content",toc="no"]')
    lines.append("")

    for mod in job["modules"]:
        mod_path = mod.replace("modules/", "")
        lines.append(f'include::modules/{mod_path}[leveloffset=+1,toc="no"]')

    for child_slug in job.get("children", []):
        lines.append(f'include::{child_slug}.adoc[leveloffset=+1]')

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_category_maps(jobs, meta):
    top_level = []
    child_slugs = set()
    for job in jobs.values():
        for child in job.get("children", []):
            child_slugs.add(child)

    for num, job in sorted(
        ((j["num"], j) for j in jobs.values() if isinstance(j.get("num"), int)),
        key=lambda x: x[0],
    ):
        if job["slug"] in child_slugs:
            continue
        if job["parent"] and job["parent"] not in CATEGORY_PARENTS:
            continue
        top_level.append(job)

    by_category = defaultdict(list)
    for job in top_level:
        by_category[job["category"]].append(job)

    for parent_key, job in jobs.items():
        if not str(parent_key).startswith("parent:"):
            continue
        by_category[job["category"]].append(job)

    for category, cat_jobs in by_category.items():
        cat_file = CATEGORY_FILES.get(category)
        if not cat_file:
            continue
        cat_jobs.sort(key=lambda j: (j["num"] is None, j["num"] or 0))
        lines = [
            ":_mod-docs-content-type: MAP",
            "",
            f"= {category}",
            "",
        ]
        for job in cat_jobs:
            lines.append(f"include::jobs/{job['slug']}.adoc[leveloffset=+1]")
            lines.append("")
        (RHCL_MAPS / cat_file).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main():
    meta = load_jobs_meta()
    coverage = enrich_coverage(meta)
    jobs, intro_created = build_jobs_from_coverage(coverage, meta)

    for job in jobs.values():
        write_job_map(job)

    write_category_maps(jobs, meta)

    job_maps = sorted(JOBS_DIR.glob("*.adoc"))
    print(f"Wrote enriched coverage map: {OUT_COVERAGE}")
    print(f"Created {len(intro_created)} intro concept modules")
    print(f"Created {len(job_maps)} job map files")
    for cat in sorted(CATEGORY_FILES):
        path = RHCL_MAPS / CATEGORY_FILES[cat]
        count = sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("include::jobs/"))
        print(f"  {cat}: {count} jobs in {path.name}")


if __name__ == "__main__":
    main()
