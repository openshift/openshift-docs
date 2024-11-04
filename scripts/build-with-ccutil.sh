#!/bin/bash

podman run --privileged -d -v ${HOME}:/docs:rw --replace --name bccutil quay.io/ivanhorvath/ccutil:amazing

OUT_FOLDER="${PWD}/drupal-build"

find "$OUT_FOLDER" -type f -name "master.adoc" | while read -r MASTER_FILE; do
    FOLDER=$(dirname "$MASTER_FILE")

    cd "${FOLDER}" || exit

    podman exec -w "/docs/${FOLDER/${HOME}\//}" bccutil ccutil compile --lang en_US --type asciidoc --main-file master.adoc
done
