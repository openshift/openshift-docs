# DITA CI starter: Git-source authoring, AEM publishing

A refactor of `LJSpiller/github-pr-dita`'s single demo workflow into a pipeline
for the **author-in-Git, publish-from-AEM-Guides** model.

The original `build-dita.yml` treated CI as the *publisher* (it built HTML5/PDF).
This set inverts that: **AEM Guides remains the publishing and translation
system**, and CI's job becomes **gate → normalize → sync**. Nothing here renders
production output.

## Flow

```
 PR opened ──► pr-gate.yml ──► (well-formedness + preprocess validation + link check)
                                 │  merge blocked while red
 merge to  ──► normalize-sync.yml ──► dita2dita (resolve keys/conrefs/maprefs)
 release br                          └─► push to sync/<branch>
                                            │
                                   Adobe Git Connector (one-way, GUID-preserving)
                                            ▼
                                       AEM Guides  ──► publish + translate (unchanged)
```

## Files

| File | Trigger | Purpose |
|---|---|---|
| `.github/workflows/pr-gate.yml` | `pull_request` | Merge-blocking quality wall. Scopes checks to changed maps. |
| `.github/workflows/normalize-sync.yml` | `push` to release branch | Resolves keys/conrefs to plain DITA, pushes to `sync/<branch>`. |
| `.github/workflows/release-preview.yml` | manual | Optional offline HTML5 preview. Off the critical path. |
| `ci/changed-maps.sh` | — | Lists root maps affected by a PR (scales the gate). |
| `ci/linkcheck.sh` | — | Fails on broken on-disk `href`/`conref` targets. Tested. |
| `ci/push-sync-branch.sh` | — | Mirrors normalized output to `sync/<branch>` and pushes. |
| `ci/schematron.sh` | — | **Stub.** Wire to CCS Schematron rules before production. |

## Per-repo setup

1. Set `ROOT_MAP` in `normalize-sync.yml` and `release-preview.yml`.
2. Set the release-branch globs (`enterprise-4.*`, etc.) to match your repo.
3. Pin `DITA_IMAGE` to a digest, not a floating tag.
4. Configure the Adobe Git Connector data source to watch `sync/*`, one data
   source per maintained branch, each targeting a separate AEM root path.
5. Wire `ci/schematron.sh` to the real CCS rules, then add it to `pr-gate.yml`.

## Why these choices

- **Runs DITA-OT via `docker run` on `ubuntu-latest`**, not as a job `container:`.
  The DITA-OT image lacks git/node that `actions/checkout` and the diff steps
  need. This matches the proven approach in the original repo.
- **`--format=dita` is both validator and normalizer.** The preprocess fails on
  unresolved keys and broken conref/mapref, so the gate and the sync step share
  one mechanism.
- **Link check runs on resolved output**, so keyref/conkeyref are already files.
- **Changed-maps scoping** is what makes this viable at openshift-docs scale
  (branch-per-version, hundreds of assemblies). See the script's LIMITATIONS note
  — the filename heuristic is safe (over-selects, never under-selects) but should
  graduate to a real map-dependency walk before full rollout.

## Validate before betting a rollout on it (from the proposal)

1. **Does `dita2dita` round-trip at real conditionalization volume** without
   breaking the DITAVAL filtering AEM still needs downstream? Test in Phase 1.
2. **GUID stability across re-syncs** under real churn — verify on your own
   content, don't take the connector's promise on faith.

## Not covered yet (deliberate next steps)

- External link liveness (flaky in a merge gate — run on a schedule instead).
- Per-version matrix over the `-CP` cherry-pick branch pattern via a reusable
  workflow.
- Caching of the DITA-OT temp/plugin dirs.
- Commit-SHA traceability onto AEM versions (needs the Adobe RFE in the proposal).
