# JTBD map preview

`preview-jtbd-maps.sh` builds a local, multi-page HTML preview from
`maps/<distro>/navigation.adoc`.

It uses the same `asciidoctor-multipage` approach as `preview-maps.sh`:

* Asciidoctor generates the content and the left navigation.
* The multipage backend creates one HTML page per navigation level.
* `preview-jtbd-right-toc.py` adds an `On this page` navigation from the
  headings on each generated page.

The command does not create a worktree, commit files, or push to GitHub Pages.
If the output directory already exists, the command only replaces it when it
contains the marker created by this tool.

Before rendering, the command runs `audit-map-includes.py` against each selected
`navigation.adoc`. The audit follows includes recursively, including includes
through the `maps/rhcl/jobs` and `maps/rhcl/jobs/modules` symlinks.

For each missing target, either restore or create the expected `.adoc` file at
the reported path, or update the include directive in the reported source file
to point to the file that replaced it. The path is resolved relative to the
file containing the include, not relative to the repository root.

The preview continues when includes are missing so that the available content
can still be reviewed. In that case, every generated page receives a red
warning banner with an expandable missing-include report. Treat that preview
as incomplete and fix the reported paths before using it as a content review
baseline. The banner also includes expandable remediation guidance. The
standalone audit still exits with status 1 when a target is missing.

To run the audit by itself:

```console
python3 scripts/audit-map-includes.py maps/rhcl/navigation.adoc
```

## Requirements

Install the multipage backend if needed:

```console
gem install asciidoctor-multipage
```

## Usage

Run from the repository root:

```console
bash scripts/preview-jtbd-maps.sh -d microshift
```

The default output directory is `build/jtbd-preview`. Use `-o` to select a
different directory:

```console
bash scripts/preview-jtbd-maps.sh -d microshift -o /tmp/microshift-preview
```

The generated entry page is:

```text
/tmp/microshift-preview/index.html
```

To view the preview with working local links, serve the generated directory:

```console
python3 -m http.server 8000 --directory /tmp/microshift-preview
```

Then open `http://localhost:8000`. The left navigation is
provided by `asciidoctor-multipage`; the right `On this page` navigation is
added by the postprocessor for headings on the current page.

## Publish to GitHub Pages

To publish the same JTBD preview to the configured fork's `gh-pages` branch,
run this from the repository root:

```console
bash scripts/publish-jtbd-maps.sh -d rhcl
```

The preview is published under the current branch name. For example, from the
`OSDOCS-21105` branch, the RHCL navigation page is:

```text
https://<user>.github.io/openshift-docs/OSDOCS-21105/rhcl/navigation.html
```

The publisher requires push access to `origin`, a remote `gh-pages` branch,
and GitHub Pages configured to deploy from that branch. It preserves the
missing-content warning when the include preflight reports unresolved files.

## Automatic publishing on GitHub commits

The repository includes `.github/workflows/publish-jtbd-maps.yml`. On the
`OSDOCS-21105` branch, each push runs the publisher automatically and updates
the matching branch directory on `gh-pages`. You can also start the workflow
manually from the GitHub Actions tab with **Run workflow**.

The workflow needs the repository Actions setting to allow workflows to write
repository contents. It uses the workflow token to update `gh-pages`; no
personal access token is stored in the repository.
