# AsciiDoc path-based xref to ID-based xref conversion

This document covers converting cross-references before migrating OpenShift docs from
AsciiDoc into Adobe Experience Manager (AEM), which uses a Darwin Information Typing
Architecture (DITA) content model.

## 1. Problem

OpenShift docs link between topics with path-based cross-references:

```
xref:../security/cert_manager_operator/cert-manager-operator-install.adoc#cert-manager-operator-install[{cert-manager-operator}]
```

A path-based xref has two independent addressing systems for the same target: 

- the **path**: where the file is, relative to the current file
- the **#anchor** the ID of an element inside that file

AEM addresses content by per-file GUID, not by directory path. After migration, the folder structure that `../../` depends on no longer exists, so the path becomes meaningless. The anchor ID survives, because DITA links natively by ID. Every path-based xref must therefore drop its path:

```
xref:cert-manager-operator-install[{cert-manager-operator}]
```

Because assemblies reuse modules, module IDs take a parameter to avoid duplicates in a built book:

```
[id="cert-manager-operator-install_{context}"]
```

The build substitutes `{context}` from the including assembly's `:context:`. Writers edit the **resolved** anchor directly in the xref. For example, `#prerequisites_aws-install`, not `#prerequisites_{context}`). The target ID is therefore already present and already resolved in the anchor of every xref. Only 9 of 14,590 xrefs leave a literal `{context}` in the anchor.

### ID-based links need unique IDs

Today, the path makes clear that `a.adoc#foo` and `b.adoc#foo` are distinct. Strip the
paths and both become `xref:foo[]`. The test that matters is **within-scope uniqueness**:
AEM resolves a reference within its containing DITA map and binds it to one file GUID, so a
bare `xref:id[]` is safe only if, resolved from its own scope, it points at exactly one
file. The same ID in two different scopes is fine, because each map is its own GUID
namespace. (Confirmed by the migration team and by the DITA spec, which scopes element IDs
per topic.)

"Scope" means different things for the two kinds of source, because they map to the DITA
target differently (see "Two classifiers" below):

- an **assembly's** scope is its **book**: the legacy source top-level directory it lives in;
- a **module's** scope is its **category map** in `/maps`: the DITA map that includes it.

The conversion then splits into two paths:

1. **convert** where the ID is unique within its scope
2. **quarantine** where it is not

## 2. The numbers (measured)

| Metric | Count |
|--------|------:|
| ASSEMBLY files | 2,615 |
| Path-based xrefs (total) | ~14,590 |
| Anchor ≠ filename stem | 7,079 (48%); *never derive the ID from the filename* |
| **Convert automatically** | **14,454 (99.1%)** |
| **Need human review** | **149 (0.9%)** |

An *instance* is one xref occurrence (a `file:line`); one ambiguous *ID* can appear in many instances (for example, `scale-autoscaling-v1` is 59 of the instances below). The 149 that need review break down as:

| Needs review | IDs | Instances | Why | Owner |
|--------------|----:|----------:|-----|-------|
| Within-book conflict | 11 | 99 | Same anchor resolves to two files in one book, so a bare ID is ambiguous | Writers: pick the intended target per reference |
| Book-landing `index` | 1 | 6 | Several books have `index.adoc` with anchor `#index` | Architecture: map each index to its DITA map landing topic |
| Anchorless | n/a | 35 | `xref:../foo.adoc[Text]` has no `#anchor` to lift | Writers/migration: synthesize the target ID |
| Broken `{context}` | n/a | 9 | Author left `#...{context}[]` unresolved | Writers: supply the resolved context value |
| **Total** | **12** | **149** | | |

## 3. Solution

### Conversion rule

For each `xref:<path>.adoc#<anchor>[<text>]` whose anchor is unique within its scope, has an anchor, and is not `{context}`-bearing: produce `xref:<anchor>[<text>]`. Copy the anchor and text verbatim, including `{attributes}`, backticks, and nested brackets. Do not reconstruct the ID from the filename.

The string rewrite is identical for every file. What differs is the file selection and how "scope" is computed for the uniqueness test, so there are two classifiers.

### Two classifiers: assembly and module

The conversion runs in one of two modes, because an assembly and a module resolve
within different scopes after migration:

| | Files edited | Uniqueness scope | Why |
|---|---|---|---|
| **assembly** | ASSEMBLY `.adoc` files | the assembly's own **book** (top-level directory) | Assemblies live in the legacy book tree and are **not** referenced by `/maps`; the job maps that replace them include `modules/` directly. Their scope is still their book. |
| **module** | `modules/*.adoc` | the module's **category** in `/maps` (`maps/<distro>/<category>.adoc`) | Modules are what `/maps` composes (module ← job map ← category map), so a module's migrated home is its category, read from `/maps`. |

Scope is **per distro**: a module reused across distros (for example, an OpenShift module
used in ROSA or OSD) gets its own copy and GUID, so that is safe. Reuse across **categories
within one distro** might not be permitted and is flagged.

Category maps can themselves be nested: a category map can include another as a sub-map, so
the child's content belongs to the parent's scope. A module appearing in both a parent and
its nested child is therefore **not** a cross-category case. For example,
`disconnected-environments` is nested under `install`, so a module used in both resolves
within the single `install` scope. The converter accounts for such nesting when computing a
module's categories.

Both classifiers share everything else: parsing, the rewrite, the modes
(`report`/`dry-run`/`apply`), repeat-safe application, and the review reports. Only file
selection and the scope computation differ. `/maps` scoping is **not** valid for assemblies.
Their targets are not in `/maps`, so it would mark nearly all of them as having no scope.

### Quarantine instead of converting

The script leaves every ambiguous, anchorless, or broken-`{context}` xref untouched in place and writes it to a review queue. Auto-converting an ambiguous ID produces a link that looks correct but silently resolves to the wrong topic.

### Out of scope

- **Other non-assembly, non-module `.adoc` files** (~200 path-based xrefs) are not handled by either classifier.
- **Within-topic duplicates**, where two same-titled sections share one anchor, are a separate collision class, handled by the pre-conversion validation
  (`conversion-prechecks` / Vale AsciiDocDITA), not by this script
- **Anchorless and broken-`{context}`** cases from the review table are reported, not converted; writers should resolve them.

## 4. Usage

Run `convert-xrefs.py <target> <mode>`, where target is `assembly` or `module` (see
"Two classifiers" above) and mode is one of:

```
convert-xrefs.py <target> report     # classify only; refresh reports; change nothing
convert-xrefs.py <target> dry-run    # print the diff apply would make; change nothing
convert-xrefs.py <target> apply      # rewrite clean xrefs in place
```

Options:

| Option | Effect |
|--------|--------|
| `--root DIR` | Repo root to scan (default: the git top-level directory). |
| `--out DIR` | Directory for the reports (default: `<root>/xref-migration`). |
| `--backup` | Write a `.bak` file next to each file before editing, in `apply` mode. |
| `--only-from FILE` | Restrict conversion to the source files listed in FILE (plain paths or grep-style `path:match` lines, such as `~/xref.txt`). The scope index still uses the whole repo. |

### When to use each mode

- **`report`**: get current counts and refresh the review queues. Use it first, and
  again after writers resolve issues.
- **`dry-run`**: review the exact conversions before committing to them. Redirect to a
  file (`convert-xrefs.py module dry-run > preview.diff`).
- **`apply`**: perform the conversion. Run it on a branch so `git restore .` can undo
  everything, or add `--backup` for `.bak` copies.

### Recommended workflow

```
git switch -c xref-conversion               # isolate the change
convert-xrefs.py module dry-run | less      # review
convert-xrefs.py module apply               # convert the clean set
```

### Reading the apply count

`apply` reports the number of unique string replacements, which is lower than the 14,454 clean instances of xrefs for conversion in the table. Those are two different units:

- `report` counts every xref *occurrence*
- `apply` replaces each distinct `old → new` string once per file

So identical repeated xrefs in a file collapse into one replacement.

For example, the full repo run converted all 14,454 occurrences through 8,159 replacements across 1,631 files. `git diff --shortstat` shows the per-line total (14,459 lines), since one line can hold more than one xref. All three numbers describe the same conversion.

## 5. Exception handling

Review queues live in `xref-migration/reports/`, named by target (`assembly_*` /
`module_*`). Empty queues are not written. Each is grouped for readability, by the
conflict's natural unit:

| File | Contents | Grouped by | Owner |
|------|----------|-----------|-------|
| `assembly_ambiguous.txt` | ids resolving to >1 file in a book, with those files + references | ambiguous id | Writers |
| `module_ambiguous.txt` | module ids defined in >1 file within a category | ambiguous id | Writers |
| `module_multi_category.txt` | modules reused across categories, with the categories | module | Architecture/Writers |
| `module_no_category.txt` | modules not yet in any `/maps` category | module | Writers/migration |
| `<target>_anchorless.txt` | xrefs with no `#anchor` to lift | source file | Writers/migration |
| `<target>_broken_context.txt` | xrefs with literal `{context}` unresolved | source file | Writers |

### Workflow

1. Run `convert-xrefs.py <target> dry-run` to refresh the reports and preview the diff.
2. Writers clear the ambiguous / multi-category conflicts and the edge cases (anchorless, broken).
3. Run `convert-xrefs.py <target> apply` to convert the clean set; quarantined cases stay for their owners.
4. Re-run until the quarantine queues are empty.

### The 11 within-book-conflict IDs needing human judgment

Each row is one anchor ID that resolves to more than one file in the same book, so a
bare `xref:id[]` is ambiguous. A writer must decide which file each reference means.
Typical causes: a content reorg leaving an earlier and a new file sharing an ID, or an
API topic whose ID is also present on that book's `objects/index.adoc` aggregation page.

| Anchor ID | Conflicting files (same book) |
|-----------|-------------------------------|
| `about-ocp-monitoring` | `observability/monitoring/about-ocp-monitoring.adoc`, `.../about-ocp-monitoring/about-ocp-monitoring.adoc` |
| `backing-up-applications` | `.../backing-up-applications.adoc`, `.../oadp-backing-up-applications-restic-doc.adoc` |
| `eviction-policy-v1` | `rest_api/policy_apis/eviction-policy-v1.adoc`, `rest_api/objects/index.adoc` |
| `lifecycle-hooks` | `applications/deployment_strategies.adoc`, `dev_guide/deployments/deployment_strategies.adoc` |
| `nodes-nodes-managing` | `nodes/nodes/nodes-nodes-managing.adoc`, `support/gathering-cluster-data.adoc` |
| `nw-ingress-route-secret-load-external-cert_secured-routes` | `.../routes/nw-configuring-routes.adoc`, `.../routes/securing-routes.adoc` |
| `olm-operatorconditions` | `operators/admin/olm-managing-operatorconditions.adoc`, `operators/understanding/olm/olm-operatorconditions.adoc` |
| `ossm-tutorial-bookinfo-overview_ossm-create-mesh` | `service_mesh/v2x/ossm-create-mesh.adoc`, `.../prepare-to-deploy-applications-ossm.adoc` |
| `scale-autoscaling-v1` | `rest_api/autoscale_apis/scale-autoscaling-v1.adoc`, `rest_api/objects/index.adoc` |
| `tokenrequest-authentication-k8s-io-v1` | `rest_api/authorization_apis/tokenrequest-authentication-k8s-io-v1.adoc`, `rest_api/objects/index.adoc` |
| `understanding-multiple-networks` | `.../multiple_networks/primary_networks/about-primary-nwt-nad.adoc`, `.../multiple_networks/understanding-multiple-networks.adoc` |

See `assembly_ambiguous.txt` for the complete target paths.
