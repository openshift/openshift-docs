# Feature-name migration edge cases: OpenShift 4.20

Status: archival review only

This branch records likely migration problems and expected review failures. Do not merge this branch without validating each item.

- Branch: `aem-4.20-feature-name-edge-cases`
- Migration parent: `upstream/migration-enterprise-4.20`
- Purpose: preserve the findings as a branch-local archive instead of opening a Jira now.

The shared inventory follows. Version-specific applicability is called out in the inventory.

# `:FeatureName:` medium and low confidence backlog

Date: 2026-11-04

## Purpose

This file records the remaining `:FeatureName:` and feature-admonition cases that need human judgment or visual review. The worktrees listed here are intentionally at their `migration-*` parents with no commits. They are placeholders for future per-branch work, not review-ready PRs.

## Worktrees

| Version | Local branch | Migration parent |
|---|---|---|
| main | `aem-main-feature-name-edge-cases` | `upstream/migration-main` |
| 5.0 | `aem-5.0-feature-name-edge-cases` | `upstream/migration-enterprise-5.0` |
| 4.22 | `aem-4.22-feature-name-edge-cases` | `upstream/migration-enterprise-4.22` |
| 4.21 | `aem-4.21-feature-name-edge-cases` | `upstream/migration-enterprise-4.21` |
| 4.20 | `aem-4.20-feature-name-edge-cases` | `upstream/migration-enterprise-4.20` |

## Medium confidence items

### Deprecated-feature snippet guard

File:

- `snippets/deprecated-feature.adoc`

Issue:

- The guard currently covers `openshift-rosa` and `openshift-dedicated`, but not `openshift-rosa-hcp`.
- ROSA HCP publishing consumers include `cli_reference/opm/cli-opm-ref.adoc` and the OLM custom-catalog content.
- This needs a managed-docs build check before merging.

Applies to:

- main, 5.0, 4.22, 4.21, 4.20

### Duplicate deprecated-feature module

Files:

- `modules/deprecated-feature.adoc`
- `service_mesh/v2x/ossm-traffic-manage.adoc`
- `metering/metering-upgrading-metering.adoc` where present
- `contributing_to_docs/doc_guidelines.adoc`

Issue:

- The module variant differs from the canonical snippet.
- The module variant lacks the snippet content-type marker and managed-docs release-note guard.
- The contributor guide still points writers to the module path.
- Consolidation changes include paths and needs owner review.

Applies to:

- main, 5.0, 4.22, 4.21, 4.20
- `metering/metering-upgrading-metering.adoc` applies to 5.0, 4.22, 4.21, and 4.20

### Stale orphan `:FeatureName:` lines

Files:

- `modules/install-osp-dualstack.adoc`
- `modules/oadp-using-data-mover-for-csi-snapshots.adoc`

Issue:

- The listed attributes have no adjacent feature-admonition include.
- The OADP file has a second valid Technology Preview attribute later in the file, so only the first line is in scope.

Applies to:

- main, 5.0, 4.22, 4.21, 4.20

### Hand-written deprecation boilerplate

Files:

- `modules/images-configuration-registry-mirror.adoc`
- `modules/images-configuration-registry-mirror-convert.adoc`
- `storage/persistent_storage/persistent-storage-flexvolume.adoc`

Issue:

- The wording duplicates the canonical deprecated-feature snippet with drift.
- Conversion changes admonition type, adds the release-notes reference, or changes rendering around adjacent CSI content.
- Visual review is required.

Applies to:

- main, 5.0, 4.22, 4.21, 4.20

## Low confidence or ambiguous items

- `snippets/siteconfig-deprecation-notice.adoc` has no references in any of the five migration branches. Treat as a possible orphan before deleting.
- `metering/metering-upgrading-metering.adoc` exists in 5.0, 4.22, 4.21, and 4.20 but is absent from the topic maps. Confirm whether the content is still published before changing it.
- `snippets/cluster-sampler-operator-deprecation.adoc` combines a bulleted list and a notice. Mechanical conversion would alter list rendering.
- `snippets/pgt-deprecation-notice.adoc` has semantic drift. The 4.20, 4.21, and 4.22 wording describes a future deprecation, while main and 5.0 describe an active deprecation and future removal.
- `snippets/logging-elastic-dep-snip.adoc` describes a lifecycle event rather than a standard deprecation. Converting it would lose meaning.
- Generic plural deprecation boilerplate appears in `modules/ossm-rn-deprecated-features.adoc`, `modules/ossm-rn-deprecated-features-1x.adoc`, `modules/rosa-release-notes-deprecated-removed-features.adoc`, and `modules/serverless-deprecated-removed-features.adoc`. These need a plural-aware snippet shape rather than the single-feature snippet.
- The 4.20 Developer Preview snippet still warns against use in core OpenShift docs while the sole include is a core OCP release-notes module. This contradiction predates the migration work.

## Related review-ready branches

- Deprecated-feature standardization: `aem-<version>-deprecation-refactor`
- ROSA Classic conditional notice: `aem-<version>-rosa-classic-refactor`
- OSD Developer Preview cleanup: `aem-<version>-dp-osd-refactor`
- 4.20 generic Developer Preview cleanup: `aem-4.20-dp-refactor`
