#!/usr/bin/env bash
# changed-maps.sh <base-sha>
#
# Prints the set of root ditamaps affected by the changes in this PR, so the
# gate validates only the books a change actually touches instead of the whole
# repo. At openshift-docs scale this is the difference between a 40-second PR
# check and a 40-minute one.
#
# Heuristic (good enough for a starter, see LIMITATIONS):
#   - a changed .ditamap is itself an affected map
#   - a changed .dita topic affects every map that references its filename
set -euo pipefail

BASE_SHA="${1:?usage: changed-maps.sh <base-sha>}"

mapfile -t CHANGED < <(
  git diff --name-only "${BASE_SHA}"...HEAD -- '*.dita' '*.ditamap' 2>/dev/null || true
)

declare -A MAPS=()
for f in "${CHANGED[@]:-}"; do
  [ -z "$f" ] && continue
  case "$f" in
    *.ditamap)
      MAPS["$f"]=1
      ;;
    *.dita)
      base="$(basename "$f")"
      # Any ditamap that mentions this topic filename is (transitively) affected.
      while IFS= read -r m; do
        [ -n "$m" ] && MAPS["${m#./}"]=1
      done < <(grep -rlF --include='*.ditamap' "$base" . 2>/dev/null || true)
      ;;
  esac
done

printf '%s\n' "${!MAPS[@]:-}" | sed '/^$/d' | sort -u

# LIMITATIONS (worth hardening before openshift-docs rollout):
#   - filename match is coarse; two topics sharing a basename over-select. Fine
#     (safe) for a gate — it only ever validates more, never less.
#   - does not follow nested map -> submap references. For deep map trees, swap
#     this for a real dependency walk (e.g. parse topicref/@href + mapref/@href
#     recursively, or reuse DITA-OT's job.xml after one preprocess).
