#!/bin/bash

IMAGE_NAME="openshift-docs:ascii-binder"

podman build --tag "${IMAGE_NAME}" -f ./Dockerfile

# We do not want selinux relabeling done if we're on a Mac.
# https://github.com/containers/podman/issues/13631
systype=$(uname)
if [ "$systype" = "Darwin" ]; then
    selinux_suffix=""
else
    selinux_suffix=":Z"
fi

podman run \
	   --rm=true \
	   --tty \
	   --workdir /workdir \
	   --env LC_ALL=C.UTF-8 \
	   -v $(pwd):/workdir${selinux_suffix} \
	   "${IMAGE_NAME}" \
       asciibinder build $@
