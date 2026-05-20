# Cursor: DITA migration workflow (OpenShift documentation)

This folder contains **Cursor commands** and **shared resources** for preparing modular AsciiDoc assemblies for DITA migration.

## Vale: use the repository config (no extra setup)

**You do not need a personal Vale config or shell alias.** This workflow uses the **openshift-docs** [`.vale.ini`](../.vale.ini) at the repository root—the same file used for normal contributor linting and CI.

That file already includes:

- **RedHat**, **AsciiDoc**, and **OpenShiftAsciiDoc** styles
- **AsciiDocDITA** (DITA migration rules from `asciidoctor-dita-vale`)
- **OpenShiftDocs** vocabulary
- AsciiDocDITA checks set to **error** (for example `ShortDescription`, `CalloutList`, `NestedSection`)

Cursor commands run Vale from the **repository root** with:

```bash
vale --config=.vale.ini --output=line path/to/file.adoc
```

**One-time step** after clone (installs Vale packages listed in `.vale.ini`):

```bash
vale sync
```

Do **not** point commands at a separate `~/.vale.ini` or a `ditavaleocp`-style alias unless you are working outside this repository.

## Other prerequisites

Install on your workstation:

| Tool | Purpose |
| --- | --- |
| [Vale](https://vale.sh/docs/install) | Uses repo `.vale.ini` (see above) |
| `poppler-utils` (`pdftotext`) | Style checker PDF corpus verification |
| `hunspell` + `en_US` dictionary | Spelling in `/check-doc-style` (on by default; use `--no-spell` to skip) |
| Python 3 | `check-ibm-style.py` |

## One-time resource setup

Large reference files (IBM quick-style PDF, RH supplementary guide, OSDOCS migration PDF) are copied by a script so they stay next to the checker and commands:

```bash
./scripts/sync-cursor-dita-resources.sh
```

The script reads from your local copies (defaults below) and fills `.cursor/resources/`. Re-run after clone if `style-guide/*.pdf` is missing.

| Default source | Contents |
| --- | --- |
| `~/ibm-style-guide/` | `check-ibm-style.py`, `IBMQuickStyle.pdf`, RH supplementary PDF, `ocp-documentation-guidelines.md` |
| `~/cqa-cursor/` | OSDOCS DITA migration PDF, modular-docs templates |

Override sources with environment variables:

```bash
IBM_STYLE_GUIDE_SRC=/path/to/ibm-style-guide \
CQA_CURSOR_SRC=/path/to/cqa-cursor \
./scripts/sync-cursor-dita-resources.sh
```

## Commands

Run these in Cursor from the **openshift-docs** repo (open the repo root as the workspace).

| Command | Purpose |
| --- | --- |
| `/prepare-dita` | **Master:** one assembly (+ includes) or one module — Vale → abstract → content type → style → report |
| `/fix-dita-vale` | Run Vale (AsciiDocDITA) and fix violations |
| `/fix-dita-callouts` | Fix **CalloutList**; preserve callout wording and all `ifdef`/`ifndef` blocks; Pattern E **Specifies** opening; full-path `::` terms |
| `/fix-content-type` | Fix wrong **`:_mod-docs-content-type:`** only; defer abstracts to `/write-dita-abstract` |
| `/write-dita-abstract` | Rewrite `[role="_abstract"]` short descriptions (required in `/prepare-dita`; not label-only) |
| `/check-doc-style` | Hunspell spelling + IBM/RH supplementary + OCP structural checks |

**Renamed commands** (update bookmarks): `/fix-dita-assembly` → `/prepare-dita`, `/asciidoctor-dita-vale-resolution` → `/fix-dita-vale`, `/resolve-dita-callouts` → `/fix-dita-callouts`, `/write-abstract` → `/write-dita-abstract`, `/align-content-type-with-template` → `/fix-content-type`, `/check-ibm-sg` → `/check-doc-style`.

### Examples

**Single module** (only that file; no `include::` discovery):

```text
/prepare-dita @modules/installation-azure-stack-hub-config-yaml.adoc
```

**Assembly** (assembly + every active `include::` module):

```text
/prepare-dita installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
```

Paths under `modules/` always run in single-module mode. Other paths use assembly mode when the file contains active `include::` lines.

Open the **openshift-docs repository root** as your Cursor workspace so Vale and paths resolve correctly.

## Directory layout

```text
.cursor/
  README.md                 ← this file
  commands/                 ← Cursor slash commands
  resources/
    style-guide/            ← IBM SG checker + quick/RH PDF corpus (after sync)
    dita-migration/
      templates/            ← Modular-docs TEMPLATE_*.adoc
      OSDOCS-*.pdf          ← Vale rule actions reference (after sync)
scripts/
  sync-cursor-dita-resources.sh
```

## Sharing with the team

Commit `.cursor/commands/`, `scripts/sync-cursor-dita-resources.sh`, templates, and `check-ibm-style.py`. PDFs may be large; either:

- Run `sync-cursor-dita-resources.sh` locally and do not commit PDFs, or
- Commit PDFs if your team policy allows (internal Red Hat sources only).

Do **not** commit `ibm-style-documentation.pdf` (full IBM Style); it is gitignored under `style-guide/`.

Do not commit personal Cursor settings; only this `.cursor/` tree and the sync script.
