#!/bin/bash

IMAGE_NAME="openshift-docs:ascii-binder"

podman run \
	   --rm=true \
	   --tty \
	   --workdir /workdir \
	   --env LC_ALL=C.UTF-8 \
	   -v $(pwd):/workdir:Z \
	   "${IMAGE_NAME}" \
       asciibinder clean
