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

## Setting up the `gh-pages` branch on your fork

1. Log in to GitHub and go to your fork of the `openshift-docs` repo (for example, `https://github.com/<your_username>/openshift-docs`).
2. Go to `https://github.com/<your_username>/openshift-docs/branches` (or click the **Branches** button on the repo page), and then click **New branch**.
3. Fill out the branch creation form:
   - **New branch name:** `gh-pages`
   - **Source repository:** select `openshift/openshift-docs` from the first dropdown
   - **Source branch:** enter `gh-pages` in the second dropdown
4. Click **Create new branch**.
5. Go to your fork's **Settings** (from the menu across the top of the page), and then select **Pages** from the left-hand nav, or go directly to `https://github.com/<your_username>/openshift-docs/settings/pages`.
6. Under **Build and deployment**, ensure **Source** is set to **Deploy from a branch**.
7. Select the `gh-pages` branch from the **Branch** dropdown.
8. Click **Save** if these settings were not already correct.

## Running the script

1. Ensure your branch is up to date with the upstream repo so that it contains the `scripts/preview-maps.sh` file and the `maps/docinfo-footer.html` file.
2. Run the script from the root directory of the repo, from a feature branch that has maps you want to preview.

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
