#!/usr/bin/env bash
# Copy style-guide and DITA migration resources into openshift-docs/.cursor/resources/
# for Cursor commands (prepare-dita workflow). Safe to re-run.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IBM_SRC="${IBM_STYLE_GUIDE_SRC:-$HOME/ibm-style-guide}"
CQA_SRC="${CQA_CURSOR_SRC:-$HOME/cqa-cursor}"

STYLE_DEST="$REPO_ROOT/.cursor/resources/style-guide"
DITA_DEST="$REPO_ROOT/.cursor/resources/dita-migration"
TEMPLATE_DEST="$DITA_DEST/templates"

mkdir -p "$STYLE_DEST" "$TEMPLATE_DEST"

copy_if_exists() {
  local src="$1" dest="$2"
  if [[ -f "$src" ]]; then
    cp -f "$src" "$dest"
    echo "✓ $(basename "$dest")"
  else
    echo "✗ missing: $src" >&2
    return 1
  fi
}

echo "Syncing style-guide resources to $STYLE_DEST"
copy_if_exists "$IBM_SRC/check-ibm-style.py" "$STYLE_DEST/check-ibm-style.py"
chmod +x "$STYLE_DEST/check-ibm-style.py" 2>/dev/null || true
# ibm-style-documentation.pdf is not copied (not redistributable in public repos)
copy_if_exists "$IBM_SRC/IBMQuickStyle.pdf" "$STYLE_DEST/IBMQuickStyle.pdf"
copy_if_exists "$IBM_SRC/red-hat-supplementary-style-guide.pdf" "$STYLE_DEST/red-hat-supplementary-style-guide.pdf"
copy_if_exists "$IBM_SRC/ocp-documentation-guidelines.md" "$STYLE_DEST/ocp-documentation-guidelines.md"

echo "Syncing DITA migration resources to $DITA_DEST"
copy_if_exists "$CQA_SRC/OSDOCS-Content updates in preparation for migrating to DITA-190526-144719.pdf" \
  "$DITA_DEST/OSDOCS-Content updates in preparation for migrating to DITA-190526-144719.pdf"

for t in TEMPLATE_ASSEMBLY_a-collection-of-modules.adoc \
         TEMPLATE_CONCEPT_concept-explanation.adoc \
         TEMPLATE_PROCEDURE_doing-one-procedure.adoc \
         TEMPLATE_REFERENCE_reference-material.adoc; do
  copy_if_exists "$CQA_SRC/$t" "$TEMPLATE_DEST/$t"
done

echo "Done. Resources are ready for Cursor commands under .cursor/"
