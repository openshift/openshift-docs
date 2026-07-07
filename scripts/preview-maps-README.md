# preview-maps.sh

Builds HTML previews of JTBD navigation maps and publishes them to GitHub Pages.

## What it does

For each requested distro (or all distros found under `maps/`), the script:

1. Runs `asciidoctor-multipage` against its `maps/<distro>/navigation.adoc` file to produce HTML preview
2. Commits the output to the `gh-pages` branch using a temporary git worktree
3. Pushes to the repo, making a browsable preview available at `https://<user>.github.io/<repo>/<branch>/<distro>/navigation.html`

It also generates index pages listing all previewed distros for the branch and all previewed branches for the repo.

## Prerequisites

- The `asciidoctor-multipage` Ruby gem must be installed (`gem install asciidoctor-multipage`)
- A `gh-pages` branch must exist on the writer's fork

## Usage

```
./scripts/preview-maps.sh [-b branch] [-d distro] [-d distro] ...
```

| Flag | Description | Default |
|------|-------------|---------|
| `-b, --branch` | Branch name for the preview | Current git branch |
| `-d, --distro` | Distro to build (repeatable) | All distros under `maps/` |

## Examples

```bash
# Build previews for all distros on the current branch
./scripts/preview-maps.sh

# Build a single distro
./scripts/preview-maps.sh -d openshift-enterprise

# Build two distros on a specific branch
./scripts/preview-maps.sh -b my-feature -d openshift-enterprise -d rosa
```
