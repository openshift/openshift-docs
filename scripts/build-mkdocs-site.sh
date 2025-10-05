#!/usr/bin/env bash

set -euo pipefail

setup() {
  if [[ "${CI:-}" == "true" ]]; then
    rm -rf .venv
  fi

  if [[ ! -d .venv ]]; then
    python -m venv .venv
  fi

  source .venv/bin/activate
  pip install --upgrade pip
  pip install "mkdocs-material[imaging]"

  # Install pngquant for image optimization
  if command -v dnf &>/dev/null; then
    sudo dnf install -y pngquant
  elif command -v apt-get &>/dev/null; then
    sudo apt-get install -y pngquant
  else
    echo "Warning: Could not install pngquant. No supported package manager found."
  fi

  pip install --upgrade --force-reinstall mkdocs-material mkdocs-minify-plugin markdown_gfm_admonition mkdocs-asciidoctor-backend mkdocs-exclude-search
}

generate_nav() {
  python scripts/generate-mkdocs-nav.py \
    _topic_maps/_topic_map.yml \
    -d openshift-enterprise \
    -i index.md \
    -o nav.yml
}

create_config() {
  cat mkdocs.yml nav.yml > mkdocs.tmp.yml
}


cleanup() {
  rm -f mkdocs.tmp.yml
}

build_site() {
  generate_nav
  create_config
  python -m mkdocs build -f mkdocs.tmp.yml --clean --verbose
  cleanup
}

serve_site() {
  generate_nav
  create_config
  trap cleanup EXIT
  python -m mkdocs serve -f mkdocs.tmp.yml --verbose
}

main() {
  setup

  case "${1:-}" in
    --build)
      build_site
      ;;
    --serve)
      serve_site
      ;;
    *)
      if [[ "${GITHUB_ACTIONS:-}" == "true" ]]; then
        build_site
      else
        serve_site
      fi
      ;;
  esac
}

main "$@"