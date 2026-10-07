# ACS conversion maps: changes applied and items still open

Tracking: [CCSINTL-4040](https://redhat.atlassian.net/browse/CCSINTL-4040)

Sheet: [JTBD mapping](https://docs.google.com/spreadsheets/d/1Mq2qSRk0icBfAOz_OKcZ4UqChwaRFf7-CEyGaGa2sKQ/edit?gid=2134905348#gid=2134905348),
tab `JTBD - all the new jobs topics added`

Generated 7 Oct 2026 with `csv2map` at commit `da00c74`. Row numbers are sheet rows
and match the line numbers in the `csv2map` log.

A snapshot of the tab taken before any edits is saved at
`_conversion-acs/jtbd-acs-PRE-EDIT-backup.csv`. It is the full tab, including the
appendix, so it can be used to restore any cell.

## Result

| | csv2map errors | csv2map warnings | asciidoctor errors | asciidoctor warnings |
|---|---|---|---|---|
| Before | 242 | 704 | 11 | 25 |
| After | **0** | 19 | **0** | 17 |

Output in `_conversion-acs/maps/`: `rhacs-4-11-navigation.adoc`, 13 category maps,
45 job submaps. Preview at `_conversion-acs/preview/index.html`.

The navigation map previously had 15 categories, of which 3 were junk and 2 real ones
were missing. It now has 13 real ones. `Develop` is still absent, for the reason
below.

## Changes applied to the sheet

24 cells, in one `values.batchUpdate` call.

### Stray notes in column A, cleared

Each was being read as a category name, because `csv2map` treats any non-empty
column A as a category.

| Cell | Value removed |
|---|---|
| A517 | `QUESTIONS` |
| A703 | `ARE SOME TAILORED PROFILE FILES MISSING?` |
| A786 | `CHANGE job name?` plus a nesting note |

Clearing A517 also restored the `Migrate` category. The real Migrate job sits on row
517, so the stray label had been stealing the category name and leaving `Migrate` on
row 516 childless, which `csv2map` then dropped.

### Missing `Is a job?` values, set to FALSE

Column H was empty on these rows, so `csv2map` raised `IndexError` and skipped each
row entirely.

Rows 12, 23, 862, 863, 1030, 1231.

### Orphan checkbox cells, cleared

H24, H864, and H913 each held a lone `FALSE` with nothing else on the row. For rows
23 and 863 the checkbox had landed one row low, which looks like a row-insertion
artifact.

### Invisible character removed from five paths

Each of these column G values began with a U+200E LEFT-TO-RIGHT MARK, which Python
`.strip()` does not remove, so the generated include could not resolve.

G198, G686, G706, G813, G1005. Each was rewritten to the same path without the mark.

### Wrong or malformed paths corrected

| Cell | Was | Now |
|---|---|---|
| G454 | `managing-feature-flags-procedure.adoc` | `modules/managing-feature-flags-procedure.adoc` |
| G789 | `modules/modules/network-graph-overview.adoc` | `modules/network-graph-overview.adoc` |
| G1198 | `...-overview.ado` | `modules/generic-webhooks-integration-overview.adoc` |
| G1302 | `support/generating-diagnostic-bundle.adoc` plus an inline note | `modules/generating-diagnostic-bundle.adoc` |
| G1303 | `modules/diagnostic-bundle-overview.adoc` | `modules/generate-diagnostic-bundle-overview.adoc` |

Every new target was confirmed to exist in the repo. The note that had been appended
to G1302, `****CHANGE TO ASSEMBLY IN SUPPORT DIR**** keep note from PR 111538`, was
moved to J1302, which `csv2map` ignores.

### One path cleared

G681, `modules/compliance-operator-configure-scanning.adoc`, matched nothing in the
repo. Its title is `Configuring the ScanSettingBinding object`, and that content
currently lives inside `modules/compliance-operator-install.adoc`, which row 680
already maps. The cell was cleared rather than pointed at a duplicate, so the row now
appears in the unmapped list below.

## Change applied to the repo

`modules/medium-sev-security-policies.adoc` line 29 was missing the leading `|` on a
table row, giving it 3 cells instead of 4. Asciidoctor reported this as
`dropping cells from incomplete row` at the end of the table. This was the last build
error and is unrelated to the maps — it is a pre-existing content bug that the new
structure surfaced.

This is the only tracked file modified. The `comment-out-includes.py` changes needed
for the preview were made on a scratch branch and reverted.

## Still open

### The Develop category is empty

Row 912 declares `Develop` and row 916 starts `Configure`, with nothing in between.
`csv2map` drops it. Either rows are missing or the category is a placeholder that
should be removed. This needs a content decision, so it was left alone.

### Eighteen rows have a title but no file path

These produce the 19 remaining `csv2map` warnings, along with `Develop`. Each has
`Is a job?` set to FALSE and nothing in column G, so the row is skipped and does not
reach the maps. Supply a path in column G for any that should appear in the
navigation.

| Rows | Titles |
|---|---|
| 91, 138 | Setting up RHACS Cloud Service with Red Hat OpenShift / with Kubernetes secured clusters |
| 170 | Upgrading RHACS Cloud Service |
| 681 | Configuring the ScanSettingBinding object |
| 1058 | Scale considerations |
| 1067-1076 | Claim mappings, the six default claim mapping topics, Rules, Minimum access role, Required attributes |
| 1088 | Adding group claims to tokens for SAML applications using SSO configuration |
| 1095, 1096 | Understanding resource scoping, Multi-tenancy per namespace configuration example |

### Seventeen duplicate anchor IDs in the build

The remaining asciidoctor warnings are all `id assigned to section already in use`,
mostly roxctl CLI modules plus a few others such as
`install-secured-cluster-services-helm-chart` and `scanner-v4-db-requirements`. They
occur where the new structure includes the same module under more than one job. That
is often intended in a JTBD layout, but each duplicate needs a decision on whether to
reuse the module or split it.

## Question for the sheet owner

How should the `UNMAPPED FILES` appendix in rows 1395-1646 be handled?

It was the single largest source of noise, accounting for every one of the original
242 errors. It is not navigation content, but `csv2map` reads each populated column A
as a category, so it produced roughly 250 of them and a long run of duplicate-category
errors for `roxctl CLI`, `Operating`, and `RHACS Cloud Service`.

The current workaround caps the export at row 1394, which is why the error count is
now 0. That works today but bakes a magic row number into the tooling, and it will
silently truncate real content as soon as rows are added above the cap. Moving the
appendix to its own tab would remove the need for the cap. Deleting it would too, but
the rows look like tracking data worth keeping.

## Reproducing

```
mkdir -p _conversion-acs/maps
gws sheets spreadsheets values get \
  --params '{"spreadsheetId":"1Mq2qSRk0icBfAOz_OKcZ4UqChwaRFf7-CEyGaGa2sKQ","range":"JTBD - all the new jobs topics added!A1:I1394"}' \
  --format csv > _conversion-acs/maps/jtbd-acs.csv

python3 -I /path/to/csv2map/csv2map.py _conversion-acs/maps/jtbd-acs.csv \
  --prefix rhacs-4-11 --output-dir _conversion-acs/maps
```

Full procedure, including the preview build, is in
`.claude/prompts/generate-acs-conversion-maps.md`.
