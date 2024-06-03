#!/bin/bash
#================================================================
# HEADER
#================================================================
#%
#%OVERVIEW 📑
#+    ./scripts/prow-smoke-test.sh [--validate --preview]
#%
#%DESCRIPTION 💡
#%    Validates openshift-docs AsciiDoc source files using the same tools that run in the Prow CI
#%
#%OPTIONS ⚙️
#%    -v, --validate $DISTRO                            Validate the AsciiDoc source. Use --validate to run with default options
#%    -l, --lint-topicmaps                              Lint topic-map YAML
#%    -p, --preview $DISTRO "$PRODUCT_NAME" $VERSION    Use --preview to run with default options
#%    -h, --help                                        Print this help
#%
#%EXAMPLES 🤔
#%    ./scripts/prow-smoke-test.sh --validate
#%    ./scripts/prow-smoke-test.sh --validate openshift-rosa
#%    ./scripts/prow-smoke-test.sh --lint-topicmaps
#%    ./scripts/prow-smoke-test.sh --preview
#%    ./scripts/prow-smoke-test.sh --preview openshift-rosa
#%    ./scripts/prow-smoke-test.sh --preview openshift-pipelines "Red Hat OpenShift Pipelines" 1.14
#================================================================
# END_OF_HEADER
#================================================================

set -e

TEST=$1
DISTRO=$2
PRODUCT_NAME=$3
VERSION=$4
ARCH=$(uname -m)
if [[ $ARCH == x86_64 ]]; then
    TAG=latest
elif [[ $ARCH == aarch64 ]]; then
    TAG=multiarch
fi
CONTAINER_IMAGE=quay.io/redhat-docs/openshift-docs-asciidoc:$TAG
SCRIPT_HEADSIZE=$(head -30 ${0} |grep -n "^# END_OF_HEADER" | cut -f1 -d:)

if [[ "$1" == "--help" || "$1" == "-h" ]]; then
    usage
fi

# Assign default variables
: ${PRODUCT_NAME:="OpenShift Container Platform"}
: ${VERSION:="4.16"}
: ${DISTRO:="openshift-enterprise"}

# Allow podman or docker
if hash podman 2>/dev/null; then
    CONTAINER_ENGINE=podman
elif hash docker 2>/dev/null; then
    CONTAINER_ENGINE=docker
else
    echo >&2 "Container engine not installed. Install Podman or Docker and run the script again."
    exit 1
fi

echo "CONTAINER_ENGINE=$CONTAINER_ENGINE 🐳"
echo "CONTAINER_IMAGE=$CONTAINER_IMAGE"

# Get the default container $WORKDIR
CONTAINER_WORKDIR=$($CONTAINER_ENGINE run --rm $CONTAINER_IMAGE /bin/bash -c 'echo $PWD')

# Grep the commented script preamble and return it as help
display_help() { head -${SCRIPT_HEADSIZE:-99} ${0} | grep -e "^#[%+-]" | sed -e "s/^#[%+-]//g" ; }

# Exit and show the help if no parameters are passed
if [ $# -eq 0 ]; then
    display_help
fi

if [[ "$TEST" == "--preview" || "$TEST" == "-p" ]] && [[ -z "$DISTRO" ]]; then
    echo ""
    echo "🚧 Building with openshift-enterprise distro..."
    $CONTAINER_ENGINE run --rm -it -v "$(pwd)":${CONTAINER_WORKDIR}:Z $CONTAINER_IMAGE asciibinder build -d "$DISTRO"

elif [[ "$TEST" == "--preview" || "$TEST" == "-p" ]] && [[ -n "$DISTRO" ]]; then
    echo ""
    echo "🚧 Building $DISTRO distro..."
    $CONTAINER_ENGINE run --rm -it -v "$(pwd)":${CONTAINER_WORKDIR}:Z $CONTAINER_IMAGE asciibinder build -d "$DISTRO"

elif [[ "$TEST" == "--validate" || "$TEST" == "-v" ]]; then
    echo ""
    echo "🚧 Validating the docs..."
    $CONTAINER_ENGINE run --rm -it -v "$(pwd)":${CONTAINER_WORKDIR}:Z $CONTAINER_IMAGE sh -c 'scripts/check-asciidoctor-build.sh && python3 build_for_portal.py --distro '${DISTRO}' --product "'"${PRODUCT_NAME}"'" --version '${VERSION}' --no-upstream-fetch && python3 makeBuild.py'

elif [[ "$TEST" == "--lint-topicmaps" || "$TEST" == "-l" ]]; then
    echo ""
    echo "🚧 Linting the topicmap YAML..."
    $CONTAINER_ENGINE run --rm -it -v "$(pwd)":${CONTAINER_WORKDIR}:Z $CONTAINER_IMAGE sh -c 'yamllint _topic_maps'
fi
